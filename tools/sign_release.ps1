<#
.SYNOPSIS
  Authenticode-signs the release files with the Certum "Open Source Developer" code-signing certificate
  (private key on the cryptoCertum smart card) and verifies the result.

.DESCRIPTION
  release.ps1 calls this after the build (the exe) and after staging (the installer scripts). It can also be
  run on its own:

      .\tools\sign_release.ps1 -Thumbprint 0123ABCD... -Path "dist\ClaudeUsageMonitor\ClaudeUsageMonitor.exe;installer\Install.ps1"
      .\tools\sign_release.ps1 -Thumbprint 0123ABCD... -Path build\package\** -Verify      # only check
  Several files go in ONE ';'-joined -Path value (a comma list does not survive `powershell.exe -File`).

  How it signs:
    * The certificate is taken from the Windows certificate store (Cert:\CurrentUser\My) - proCertum CardManager
      registers the card's certificate there. The private key never leaves the card; the card asks for its PIN.
    * signtool.exe (Windows SDK) is used when it can be found: the SDK under "Windows Kits", or the copy that
      tools\get_signtool.ps1 puts into tools\signtool\. It signs with SHA-256 and an RFC 3161 time stamp, so the
      signature stays valid after the certificate expires.
    * Without signtool it falls back to PowerShell's Set-AuthenticodeSignature (SHA-256, time-stamped) - the result
      is a normal Authenticode signature too.
    * A file that already carries a valid signature from the SAME certificate is left alone (re-runs are safe).

  Exit code 1 when any file could not be signed or does not verify.
#>
param(
    [string]$Thumbprint = "",
    [string]$Subject = "",                              # alternative to the thumbprint: a substring of the subject
    # files or wildcards; "**" under a folder = every signable file. Several files: separate tokens or one
    # ';'-joined string - both survive `powershell.exe -File`, where a comma list does NOT.
    [Parameter(Mandatory = $true, Position = 0, ValueFromRemainingArguments = $true)][string[]]$Path,
    [string]$TimestampUrl = "http://time.certum.pl",
    [string]$SignTool = "",
    [string]$Description = "Claude Usage Monitor",
    [string]$DescriptionUrl = "https://claudeusagemonitor.com/",
    [switch]$Verify,
    [switch]$AllowUntrusted                             # tests only: accept a self-signed certificate whose chain Windows does not trust
)
$ErrorActionPreference = "Stop"
$signable = @(".exe", ".dll", ".pyd", ".ps1", ".psm1", ".psd1", ".msi", ".cat", ".sys", ".ocx")

function Find-SignTool([string]$given) {
    if ($given) { if (Test-Path $given) { return (Resolve-Path $given).Path } else { throw "signtool not found: $given" } }
    $local = Join-Path (Split-Path $PSScriptRoot -Parent) "tools\signtool\signtool.exe"
    if (Test-Path $local) { return $local }
    $kits = Get-ChildItem "C:\Program Files (x86)\Windows Kits\10\bin\*\x64\signtool.exe" -ErrorAction SilentlyContinue |
        Sort-Object FullName -Descending | Select-Object -First 1
    if ($kits) { return $kits.FullName }
    $cmd = Get-Command signtool.exe -ErrorAction SilentlyContinue
    if ($cmd) { return $cmd.Source }
    return ""
}

function Find-Cert([string]$tp, [string]$subj) {
    $all = @(Get-ChildItem Cert:\CurrentUser\My, Cert:\LocalMachine\My -ErrorAction SilentlyContinue |
        Where-Object { $_.HasPrivateKey -and ($_.EnhancedKeyUsageList | Where-Object { $_.ObjectId -eq "1.3.6.1.5.5.7.3.3" }) })
    $hits = if ($tp) { $all | Where-Object { $_.Thumbprint -eq ($tp -replace '[^0-9A-Fa-f]', '').ToUpper() } }
            elseif ($subj) { $all | Where-Object { $_.Subject -like "*$subj*" } }
            else { @() }
    $hits = @($hits | Sort-Object NotAfter -Descending)
    if (-not $hits) {
        $have = ($all | ForEach-Object { "    $($_.Thumbprint)  $($_.Subject)  (until $($_.NotAfter.ToString('yyyy-MM-dd')))" }) -join "`n"
        throw "No code-signing certificate for thumbprint '$tp' / subject '$subj'. Is the card in the reader and proCertum CardManager running?`n  Code-signing certificates in the store:`n$have"
    }
    $c = $hits[0]
    if ($c.NotAfter -lt (Get-Date)) { throw "The certificate expired on $($c.NotAfter): $($c.Subject)" }
    if ($c.NotAfter -lt (Get-Date).AddDays(30)) { Write-Host "  WARNING: the certificate expires on $($c.NotAfter.ToString('yyyy-MM-dd')) - renew it soon." -ForegroundColor Yellow }
    return $c
}

function Expand-Paths([string[]]$items) {
    $out = New-Object System.Collections.Generic.List[string]
    $items = @($items | ForEach-Object { ([string]$_).TrimEnd(',') -split ';' } | ForEach-Object { $_.Trim() } | Where-Object { $_ })
    foreach ($p in $items) {
        if ($p -like "*\**" -or $p -like "*/**") {
            $root = $p -replace '[\\/]\*\*$', ''
            Get-ChildItem $root -Recurse -File | Where-Object { $signable -contains $_.Extension.ToLower() } | ForEach-Object { $out.Add($_.FullName) }
        } elseif ($p -match '[\*\?]') {
            Get-ChildItem $p -File -ErrorAction SilentlyContinue | ForEach-Object { $out.Add($_.FullName) }
        } else {
            if (-not (Test-Path $p)) { throw "File not found: $p" }
            $out.Add((Resolve-Path $p).Path)
        }
    }
    return $out | Select-Object -Unique
}

$files = @(Expand-Paths $Path)
if (-not $files) { Write-Host "  nothing to sign"; exit 0 }
$cert = Find-Cert $Thumbprint $Subject
$tool = Find-SignTool $SignTool
Write-Host ("  certificate: {0}  (until {1})" -f $cert.Subject, $cert.NotAfter.ToString("yyyy-MM-dd"))
Write-Host ("  signer: {0}" -f $(if ($tool) { $tool } else { "PowerShell Set-AuthenticodeSignature (signtool not found - tools\get_signtool.ps1 fetches it)" }))

$okStatus = @("Valid"); if ($AllowUntrusted) { $okStatus += @("NotTrusted", "UnknownError") }
function Good($s) { ($okStatus -contains [string]$s.Status) -and $s.SignerCertificate -and $s.SignerCertificate.Thumbprint -eq $cert.Thumbprint }

$failed = 0; $signed = 0; $kept = 0
foreach ($f in $files) {
    $rel = $f.Replace((Split-Path $PSScriptRoot -Parent) + "\", "")
    $sig = Get-AuthenticodeSignature -FilePath $f
    $same = Good $sig
    if ($Verify) {
        if ($same) { Write-Host "  ok    $rel" -ForegroundColor Green } else { Write-Host "  BAD   $rel  ($($sig.Status))" -ForegroundColor Red; $failed++ }
        continue
    }
    if ($same) { $kept++; Write-Host "  kept  $rel (already signed)" -ForegroundColor DarkGray; continue }
    try {
        if ($tool) {
            $prev = $ErrorActionPreference; $ErrorActionPreference = "Continue"
            $out = & $tool sign /sha1 $cert.Thumbprint /fd SHA256 /tr $TimestampUrl /td SHA256 /d $Description /du $DescriptionUrl "$f" 2>&1
            $code = $LASTEXITCODE; $ErrorActionPreference = $prev
            if ($code -ne 0) { throw ("signtool exit $code`n" + ($out -join "`n")) }
        } else {
            $r = Set-AuthenticodeSignature -FilePath $f -Certificate $cert -HashAlgorithm SHA256 -TimestampServer $TimestampUrl -IncludeChain All
            if ($okStatus -notcontains [string]$r.Status) { throw "Set-AuthenticodeSignature: $($r.Status) - $($r.StatusMessage)" }
        }
        $chk = Get-AuthenticodeSignature -FilePath $f
        if (-not (Good $chk)) { throw "verification after signing: $($chk.Status) - $($chk.StatusMessage)" }
        $signed++
        Write-Host "  signed $rel" -ForegroundColor Green
    } catch {
        $failed++
        Write-Host "  FAILED $rel`n    $($_.Exception.Message)" -ForegroundColor Red
    }
}
if ($Verify) { Write-Host ("  verified: {0} file(s), {1} bad" -f $files.Count, $failed) }
else { Write-Host ("  signed: {0}, already signed: {1}, failed: {2}" -f $signed, $kept, $failed) }
exit $(if ($failed) { 1 } else { 0 })
