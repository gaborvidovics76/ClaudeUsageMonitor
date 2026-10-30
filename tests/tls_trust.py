"""The sign-in's "[SSL: CERTIFICATE_VERIFY_FAILED] certificate has expired" on claude.ai / platform.claude.com.

Reproduces the trust store of the affected Windows machines without touching the real stores: the real ROOT + CA
stores (as ssl.create_default_context() loads them), minus the self-signed ISRG Root X2 root (never downloaded),
plus the expired cross-signed ISRG Root X2 that the 2024-25 Let's Encrypt ECDSA chains left in the CA cache.
Then checks that claude_usage.tls fixes it. Needs the network. Windows only (on other systems only the
bundle part runs).

    python tests/tls_trust.py
"""

from __future__ import annotations

import os
import socket
import ssl
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT)

from claude_usage import tls  # noqa: E402

HOSTS = ("platform.claude.com", "claude.ai", "api.anthropic.com")

# https://letsencrypt.org/certs/isrg-root-x2-cross-signed.pem - ISRG Root X2 signed by ISRG Root X1, expired 2025-09-15
EXPIRED_X2_CROSS = """-----BEGIN CERTIFICATE-----
MIIEYDCCAkigAwIBAgIQB55JKIY3b9QISMI/xjHkYzANBgkqhkiG9w0BAQsFADBP
MQswCQYDVQQGEwJVUzEpMCcGA1UEChMgSW50ZXJuZXQgU2VjdXJpdHkgUmVzZWFy
Y2ggR3JvdXAxFTATBgNVBAMTDElTUkcgUm9vdCBYMTAeFw0yMDA5MDQwMDAwMDBa
Fw0yNTA5MTUxNjAwMDBaME8xCzAJBgNVBAYTAlVTMSkwJwYDVQQKEyBJbnRlcm5l
dCBTZWN1cml0eSBSZXNlYXJjaCBHcm91cDEVMBMGA1UEAxMMSVNSRyBSb290IFgy
MHYwEAYHKoZIzj0CAQYFK4EEACIDYgAEzZvVn4CDCuwJSvMWSj5cz3es3mcFDR0H
ttwW+1qLFNvicWDEukWVEYmO6gbf9yoWHKS5xcUy4APgHoIYOIvXRdgKam7mAHf7
AlF9ItgKbppbd9/w+kHsOdx1ymgHDB/qo4HlMIHiMA4GA1UdDwEB/wQEAwIBBjAP
BgNVHRMBAf8EBTADAQH/MB0GA1UdDgQWBBR8Qpau3ktIO/qS+J6Mz22LqXI3lTAf
BgNVHSMEGDAWgBR5tFnme7bl5AFzgAiIyBpY9umbbjAyBggrBgEFBQcBAQQmMCQw
IgYIKwYBBQUHMAKGFmh0dHA6Ly94MS5pLmxlbmNyLm9yZy8wJwYDVR0fBCAwHjAc
oBqgGIYWaHR0cDovL3gxLmMubGVuY3Iub3JnLzAiBgNVHSAEGzAZMAgGBmeBDAEC
ATANBgsrBgEEAYLfEwEBATANBgkqhkiG9w0BAQsFAAOCAgEAG38lK5B6CHYAdxjh
wy6KNkxBfr8XS+Mw11sMfpyWmG97sGjAJETM4vL80erb0p8B+RdNDJ1V/aWtbdIv
P0tywC6uc8clFlfCPhWt4DHRCoSEbGJ4QjEiRhrtekC/lxaBRHfKbHtdIVwH8hGR
Ib/hL8Lvbv0FIOS093nzLbs3KvDGsaysUfUfs1oeZs5YBxg4f3GpPIO617yCnpp2
D56wKf3L84kHSBv+q5MuFCENX6+Ot1SrXQ7UW0xx0JLqPaM2m3wf4DtVudhTU8yD
ZrtK3IEGABiL9LPXSLETQbnEtp7PLHeOQiALgH6fxatI27xvBI1sRikCDXCKHfES
c7ZGJEKeKhcY46zHmMJyzG0tdm3dLCsmlqXPIQgb5dovy++fc5Ou+DZfR4+XKM6r
4pgmmIv97igyIintTJUJxCD6B+GGLET2gUfA5GIy7R3YPEiIlsNekbave1mk7uOG
nMeIWMooKmZVm4WAuR3YQCvJHBM8qevemcIWQPb1pK4qJWxSuscETLQyu/w4XKAM
YXtX7HdOUM+vBqIPN4zhDtLTLxq9nHE+zOH40aijvQT2GcD5hq/1DhqqlWvvykdx
S2McTZbbVSMKnQ+BdaDmQPVkRgNuzvpqfQbspDQGdNpT2Lm4xiN9qfgqLaSCpi4t
EcrmzTFYeYXmchynn9NM0GbQp7s=
-----END CERTIFICATE-----
"""


def _decode(pem: str) -> dict:
    import tempfile

    with tempfile.NamedTemporaryFile("w", suffix=".pem", delete=False) as fh:
        fh.write(pem)
    try:
        return ssl._ssl._test_decode_cert(fh.name)  # noqa: SLF001 - the stdlib's own test helper
    finally:
        os.unlink(fh.name)


# the embedded certificate must be the cross-sign (issued by X1) and really expired, or step 3 proves nothing
_d = _decode(EXPIRED_X2_CROSS)
assert dict(_d["subject"][-1])["commonName"] == "ISRG Root X2", _d["subject"]
assert dict(_d["issuer"][-1])["commonName"] == "ISRG Root X1", _d["issuer"]
assert _d["notAfter"].endswith("2025 GMT"), _d["notAfter"]


def _fail(reason: str) -> None:
    print("FAIL:", reason)
    sys.exit(1)


def _verify(ctx: ssl.SSLContext, host: str) -> str:
    try:
        with socket.create_connection((host, 443), timeout=20) as s, ctx.wrap_socket(s, server_hostname=host):
            return "OK"
    except ssl.SSLCertVerificationError as e:
        return e.verify_message or str(e)
    except (OSError, ssl.SSLError) as e:
        return f"network: {e}"


def _bare_context() -> ssl.SSLContext:
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    ctx.verify_mode = ssl.CERT_REQUIRED
    ctx.check_hostname = True
    return ctx


def _contaminated_windows_context() -> ssl.SSLContext:
    """The affected machine: ROOT + CA stores without the self-signed X2 root, the expired X2 cross-sign cached."""
    ctx = _bare_context()
    for store in ("CA", "ROOT"):
        for cert, enc, trust in ssl.enum_certificates(store):
            if enc != "x509_asn" or trust is False:
                continue
            if b"ISRG Root X2" in cert:
                continue            # a machine that never needed the X2 root (or got it only as a cross-sign)
            ctx.load_verify_locations(cadata=cert)
    ctx.load_verify_locations(cadata=EXPIRED_X2_CROSS)
    return ctx


# 1) the real thing the app uses
ctx = tls.context()
assert ctx is tls.context(), "the context must be shared"
assert ctx.verify_mode == ssl.CERT_REQUIRED and ctx.check_hostname, "verification switched off"
assert ctx.minimum_version == ssl.TLSVersion.TLSv1_2, ctx.minimum_version
import certifi  # noqa: E402

bundle = open(certifi.where(), encoding="utf-8").read()
for name in ("ISRG Root X1", "ISRG Root X2", "GTS Root R4"):
    assert name in bundle, f"{name} missing from the certifi bundle"
for host in HOSTS:
    r = _verify(ctx, host)
    if r != "OK":
        _fail(f"the app's context cannot verify {host}: {r}")
print("1) app context (platform stores + certifi): all three Anthropic hosts verify: ok")

# 2) the bundle alone verifies the hosts (machines whose Windows store never downloaded the root)
only_bundle = _bare_context()
assert tls.add_bundle(only_bundle)
for host in HOSTS:
    r = _verify(only_bundle, host)
    if r != "OK":
        _fail(f"the certifi bundle alone cannot verify {host}: {r}")
print("2) certifi bundle alone verifies the hosts: ok")

if sys.platform != "win32":
    print("3-4) skipped (Windows certificate stores)")
    sys.exit(0)

# 3) the reported machine, reproduced: fails exactly like the bug report
broken = _contaminated_windows_context()
r = _verify(broken, "platform.claude.com")
if r.startswith("network"):
    _fail(r)
if "expired" not in r:
    _fail(f"the contaminated store was expected to fail with 'certificate has expired', got: {r} - does "
          "platform.claude.com still send the ISRG Root X2 cross-signed chain? (openssl s_client -showcerts)")
print(f"3) contaminated Windows store (expired X2 cross-sign cached, no X2 root) -> '{r}': reproduced")

# 4) the fix: the same contaminated store plus the bundle verifies
fixed = _contaminated_windows_context()
assert tls.add_bundle(fixed)
for host in HOSTS:
    r = _verify(fixed, host)
    if r != "OK":
        _fail(f"with the bundle added, {host} still fails: {r}")
print("4) the same store + certifi bundle: all hosts verify: fixed")
print("ALL TLS TRUST TESTS OK")
