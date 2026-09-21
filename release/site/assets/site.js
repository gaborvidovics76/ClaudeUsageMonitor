/* Claude Usage Monitor – site logic. No dependencies, no third parties (unless the owner configures Google IDs AND the visitor agrees). */
(function () {
  'use strict';
  var API = '/usage-api/';
  var LANGS = { en: 'English', hu: 'Magyar', de: 'Deutsch', fr: 'Français', es: 'Español', it: 'Italiano', pt: 'Português', pl: 'Polski', nl: 'Nederlands', ru: 'Русский', cs: 'Čeština', tr: 'Türkçe' };
  var html = document.documentElement;
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var store = { get: function (k) { try { return localStorage.getItem(k); } catch (e) { return null; } }, set: function (k, v) { try { localStorage.setItem(k, v); } catch (e) {} } };
  var params = new URLSearchParams(location.search);

  var state = { lang: 'en', dict: {}, en: {}, win: null, mac: null, log: [], token: '', apiOk: false, cfg: { google: {}, legal: {} }, theme: 'midnight', layout: 'panel' };

  function tr(key) { return state.dict[key] || state.en[key] || key; }

  /* ------------------------------------------------------------ platform */
  (function detectOS() {
    var ua = navigator.userAgent || '', p = (navigator.userAgentData && navigator.userAgentData.platform) || navigator.platform || '';
    var mobile = /Android|iPhone|iPad|iPod|Mobile/i.test(ua) || (/Mac/i.test(p) && navigator.maxTouchPoints > 1);
    if (mobile) html.classList.add('is-mobile');
    else if (/Mac/i.test(p) || /Mac OS X/i.test(ua)) html.classList.add('os-mac');
    else if (/Win/i.test(p) || /Windows/i.test(ua)) html.classList.add('os-win');
  })();

  /* ------------------------------------------------------------ i18n
     Every language is a REAL, pre-rendered page (/, /hu/, /de/ ...) so that search engines and AI crawlers,
     which do not run scripts, can read it. The script only needs the dictionary for its own messages. */
  var ROOT = html.getAttribute('data-root') || '';
  function langUrl(l) { return (ROOT || './') + (l === 'en' ? '' : l + '/'); }

  /* Google's guidance: never redirect between language versions on your own. An explicit choice (the visitor picked a
     language here before, or followed an old ?lang= link) is honoured; a browser-language guess only gets a polite hint. */
  var HINT = { en: 'View this page in English', hu: 'Ez az oldal magyarul is elérhető', de: 'Diese Seite gibt es auch auf Deutsch', fr: 'Cette page existe aussi en français',
    es: 'Esta página también está en español', it: 'Questa pagina è disponibile anche in italiano', pt: 'Esta página também está em português', pl: 'Ta strona jest też po polsku',
    nl: 'Deze pagina is er ook in het Nederlands', ru: 'Эта страница есть и на русском', cs: 'Tato stránka je i v češtině', tr: 'Bu sayfa Türkçe olarak da mevcut' };
  (function routeLanguage() {
    var page = html.lang || 'en';
    state.lang = page;
    var q = (params.get('lang') || '').slice(0, 2).toLowerCase(), chosen = store.get('um-lang');
    var explicit = LANGS[q] ? q : (!ROOT && chosen && LANGS[chosen] ? chosen : null);
    if (explicit && explicit !== page) {
      params.delete('lang');
      var rest = params.toString();
      location.replace(langUrl(explicit) + (rest ? '?' + rest : '') + location.hash);
      return;
    }
    if (chosen || store.get('um-hint-off')) return;
    var nav = navigator.languages || [navigator.language || 'en'], guess = null;
    for (var i = 0; i < nav.length && !guess; i++) { var c = String(nav[i]).slice(0, 2).toLowerCase(); if (LANGS[c]) guess = c; }
    if (!guess || guess === page) return;
    var bar = $('#langhint'), go = $('#langhint-go');
    go.textContent = HINT[guess] + ' →'; go.href = langUrl(guess); go.lang = guess; go.hreflang = guess;
    go.onclick = function () { store.set('um-lang', guess); if (location.hash) go.href = langUrl(guess) + location.hash; };
    $('#langhint-x').onclick = function () { bar.hidden = true; store.set('um-hint-off', '1'); };
    bar.hidden = false;
  })();

  function applyDynamic() {
    $('#theme-desc').innerHTML = tr('th.d_' + state.theme);
    duplicateMarquee();
    renderNotes(); renderTimeline(); fillDownloads(); bindLegalLinks();
  }

  function loadJSON(url) { return fetch(ROOT + url, { cache: 'no-cache' }).then(function (r) { if (!r.ok) throw new Error(url); return r.json(); }); }

  function loadDict() {
    var en = loadJSON('i18n/en.json').catch(function () { return {}; });
    var own = state.lang === 'en' ? en : loadJSON('i18n/' + state.lang + '.json').catch(function () { return {}; });
    return Promise.all([en, own]).then(function (r) { state.en = r[0]; state.dict = r[1]; applyDynamic(); });
  }

  (function langMenu() {
    var list = $('#lang-list'), btn = $('.lang__btn');
    $$('a[data-lang]', list).forEach(function (a) {
      a.addEventListener('click', function () {
        store.set('um-lang', a.getAttribute('data-lang')); track('language_switch', { item: a.getAttribute('data-lang') });
        if (location.hash) a.href = a.getAttribute('href').split('#')[0] + location.hash;
      });
    });
    function toggle(open) { list.hidden = !open; btn.setAttribute('aria-expanded', open); }
    btn.onclick = function (e) { e.stopPropagation(); toggle(list.hidden); };
    document.addEventListener('click', function (e) { if (!list.hidden && !list.contains(e.target)) toggle(false); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') toggle(false); });
  })();

  /* ------------------------------------------------------------ marquee */
  function duplicateMarquee() {
    var t = $('#marquee'); if (!t) return;
    $$('[data-clone]', t).forEach(function (n) { n.remove(); });
    $$(':scope > *', t).forEach(function (n) { var c = n.cloneNode(true); c.setAttribute('data-clone', ''); c.removeAttribute('data-i18n'); t.appendChild(c); });
  }

  /* ------------------------------------------------------------ releases: always the newest, straight from the manifests */
  function mb(n) { return n ? Math.round(n / 1048576) + ' MB' : ''; }
  function day(s) { if (!s) return ''; try { return new Date(s).toLocaleDateString(state.lang, { year: 'numeric', month: 'short', day: 'numeric' }); } catch (e) { return String(s).slice(0, 10); } }
  function safeUrl(u) { return /^https:\/\/claudeusagemonitor\.com\//.test(u || '') ? u : null; }

  function fillDownloads() {
    [['win', state.win], ['mac', state.mac]].forEach(function (pair) {
      var os = pair[0], m = pair[1];
      if (!m) return;
      var arch = m.arch === 'arm64' ? 'Apple Silicon' : (m.arch === 'x86_64' ? 'Intel' : (m.arch || ''));
      var map = { version: m.version, size: mb(m.bytes), date: day(m.last_updated), sha: m.sha256, requires: m.requires, arch: arch };
      Object.keys(map).forEach(function (k) { $$('[data-' + os + '="' + k + '"]').forEach(function (el) { if (map[k]) el.textContent = map[k]; }); });
      var direct = safeUrl(m.download_url);
      $$('[data-dl="' + os + '"]').forEach(function (a) {
        a.href = state.apiOk ? API + 'dl.php?os=' + os + '&lang=' + state.lang : (direct || '#download');
        a.setAttribute('rel', 'nofollow');
      });
    });
    if (state.macMissing) { $('#mac-meta').hidden = true; $('#mac-soon').hidden = false; $$('[data-dl="mac"]').forEach(function (a) { a.href = '#download'; }); }
  }

  function parseChangelog(md) {
    var out = [], cur = null, lang = 'en';
    md.split(/\r?\n/).forEach(function (line) {
      var h = line.match(/^## \[(\d+\.\d+\.\d+)\]\s*-\s*(\S+)/);
      if (h) { cur = { version: h[1], date: h[2], en: [], hu: [] }; out.push(cur); lang = 'en'; return; }
      if (!cur) return;
      if (/^\*Magyarul:\*/.test(line)) { lang = 'hu'; return; }
      var b = line.match(/^- (.+)/); if (b) cur[lang].push(b[1]);
    });
    return out;
  }

  function notesFor(entry) { return (state.lang === 'hu' && entry.hu && entry.hu.length) ? entry.hu : (entry.en || []); }

  function renderNotes() {
    var ul = $('#notes'); if (!state.win) return;
    var latest = state.log.filter(function (e) { return e.version === state.win.version; })[0] || { en: (state.win.notes || {}).en, hu: (state.win.notes || {}).hu };
    var list = notesFor(latest) || [];
    ul.textContent = ''; ul.classList.remove('all');
    list.forEach(function (t) { var li = document.createElement('li'); li.textContent = t; ul.appendChild(li); });
    var old = $('#notes-more'); if (old) old.remove();
    if (list.length > 2) {
      var b = document.createElement('button'); b.id = 'notes-more'; b.className = 'morebtn'; b.type = 'button';
      b.textContent = tr('js.more').replace('{n}', list.length - 2);
      b.onclick = function () { ul.classList.add('all'); b.remove(); };
      ul.after(b);
    }
    $('#notes-langnote').hidden = (state.lang === 'en' || state.lang === 'hu');
  }

  function renderTimeline() {
    var box = $('#timeline'); if (!box || !state.log.length) return;
    box.textContent = '';
    state.log.forEach(function (e, i) {
      if (state.win && e.version === state.win.version) return;
      var row = document.createElement('div'); row.className = 'tl';
      var v = document.createElement('div'); v.className = 'tl__v'; v.textContent = e.version;
      var s = document.createElement('small'); s.textContent = day(e.date); v.appendChild(s);
      var ul = document.createElement('ul'); var list = notesFor(e);
      list.forEach(function (t) { var li = document.createElement('li'); li.textContent = t; ul.appendChild(li); });
      var right = document.createElement('div'); right.appendChild(ul);
      if (list.length > 2) {
        var b = document.createElement('button'); b.className = 'morebtn'; b.type = 'button'; b.textContent = tr('js.more').replace('{n}', list.length - 2);
        b.onclick = function () { row.classList.add('all'); b.remove(); }; right.appendChild(b);
      }
      row.appendChild(v); row.appendChild(right); box.appendChild(row);
    });
  }

  /* ------------------------------------------------------------ counter, testimonials, form token */
  function animateCount(el, to) {
    var t0 = null, dur = 1200, fin = function () { el.textContent = to.toLocaleString(state.lang); };
    if (document.hidden || matchMedia('(prefers-reduced-motion: reduce)').matches) { fin(); return; }
    setTimeout(fin, dur + 400);   // a throttled tab never runs the animation: still show the real number
    function step(ts) { if (!t0) t0 = ts; var k = Math.min(1, (ts - t0) / dur); el.textContent = Math.round(to * (1 - Math.pow(1 - k, 3))).toLocaleString(state.lang); if (k < 1) requestAnimationFrame(step); }
    requestAnimationFrame(step);
  }

  function loadStats() {
    return fetch(API + 'stats.php', { cache: 'no-store' }).then(function (r) { return r.json(); }).then(function (s) {
      if (!s.ok) throw 0;
      state.apiOk = true; state.token = s.token; state.tokenAt = Date.now();
      if (s.downloads && s.downloads.total > 0) {
        $$('[data-counter]').forEach(function (n) { n.hidden = false; });
        $$('[data-count]').forEach(function (n) { animateCount(n, s.downloads[n.dataset.count] || 0); });
      }
      if (s.testimonials && s.testimonials.length) {
        var box = $('#testimonials'); box.textContent = ''; box.hidden = false;
        s.testimonials.forEach(function (q) {
          var f = document.createElement('figure'); f.className = 'quote';
          var p = document.createElement('p'); p.textContent = '“' + q.text + '”';
          var c = document.createElement('cite'); c.textContent = q.name;
          f.appendChild(p); f.appendChild(c); box.appendChild(f);
        });
      }
    }).catch(function () { state.apiOk = false; });
  }

  function freshToken() {
    if (state.token && Date.now() - state.tokenAt < 90 * 60000) return Promise.resolve(state.token);
    return loadStats().then(function () { return state.token; });
  }

  /* ------------------------------------------------------------ forms */
  /* reCAPTCHA v3 - optional (config.json -> recaptcha.site_key). Google's script is fetched only when somebody
     actually starts using a form, never on page load. */
  var rcLoading = null;
  function rcKey() { return (state.cfg.recaptcha || {}).site_key || ''; }
  function rcLoad() {
    if (!rcKey()) return Promise.resolve(false);
    return rcLoading || (rcLoading = new Promise(function (res) {
      var s = document.createElement('script'); s.src = 'https://www.google.com/recaptcha/api.js?render=' + encodeURIComponent(rcKey());
      s.onload = function () { window.grecaptcha.ready(function () { res(true); }); }; s.onerror = function () { res(false); };
      document.head.appendChild(s);
    }));
  }
  function rcToken(action) {
    return rcLoad().then(function (ok) { return ok ? window.grecaptcha.execute(rcKey(), { action: action }) : ''; }).catch(function () { return ''; });
  }
  document.addEventListener('focusin', function (e) { if (e.target.closest && e.target.closest('#fb-form, #sub-form')) rcLoad(); });

  function postJSON(file, data) {
    return Promise.all([freshToken(), rcToken(file.replace('.php', ''))]).then(function (r) {
      var tok = r[0]; data.recaptcha = r[1];
      data.token = tok; data.lang = state.lang;
      return fetch(API + file, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(data) });
    }).then(function (r) { return r.json().catch(function () { return { ok: false }; }); });
  }

  function wireForm(form, status, file, collect, okKey) {
    var opened = Date.now();
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      status.className = 'form__status';
      if (!form.checkValidity()) { status.textContent = tr('js.fill'); status.classList.add('err'); form.reportValidity(); return; }
      if (Date.now() - opened < 3500) { opened = Date.now() - 3500; }
      form.classList.add('is-busy'); status.textContent = tr('js.sending');
      var data = collect();
      postJSON(file, data).then(function (res) {
        form.classList.remove('is-busy');
        if (res.ok) { status.textContent = tr(okKey); status.classList.add('ok'); form.reset(); track(file === 'subscribe.php' ? 'sign_up' : 'generate_lead', { method: file === 'subscribe.php' ? 'newsletter' : 'feedback_form', item: (data && data.topic) || (data && data.os) || '' }); }
        else { status.textContent = tr(res.error === 'rate' ? 'js.rate' : (res.error === 'email' ? 'js.bad_email' : 'js.fail')); status.classList.add('err'); if (res.error === 'token') { state.token = ''; } }
      }).catch(function () { form.classList.remove('is-busy'); status.textContent = tr('js.fail'); status.classList.add('err'); });
    });
  }

  var fb = $('#fb-form');
  wireForm(fb, $('#fb-status'), 'feedback.php', function () {
    return { name: fb.name.value, email: fb.email.value, topic: fb.topic.value, message: fb.message.value, publish: fb.publish.checked, website: fb.website.value };
  }, 'js.fb_ok');
  var sf = $('#sub-form');
  wireForm(sf, $('#sub-status'), 'subscribe.php', function () {
    return { email: sf.email.value, os: sf.os.value, consent: sf.consent.checked, website: sf.website.value };
  }, 'js.sub_ok');

  /* links from the e-mails: ?sub=confirmed|invalid|error  and  ?unsub=<token> */
  function mailLinkStates() {
    var dlg = $('#sub-dlg'), yes = $('#sub-dlg-yes'), sub = params.get('sub'), un = params.get('unsub');
    if (!sub && !un) return;
    function show(tk, xk) { $('#sub-dlg-title').textContent = tr(tk); $('#sub-dlg-text').textContent = tr(xk); if (!dlg.open) dlg.showModal(); }
    if (un && /^[a-f0-9]{48}$/.test(un)) {
      yes.hidden = false; show('sub.unsub_h', 'sub.unsub_p');
      yes.onclick = function () {
        yes.classList.add('is-busy');
        fetch(API + 'unsubscribe.php?t=' + un, { method: 'POST' }).then(function (r) { return r.json(); }).then(function (r) {
          yes.hidden = true; yes.classList.remove('is-busy');
          r.ok ? show('sub.bye_h', 'sub.bye_p') : show('sub.err_h', 'sub.err_p');
        }).catch(function () { yes.classList.remove('is-busy'); show('sub.err_h', 'sub.err_p'); });
      };
    } else if (sub === 'confirmed') { show('sub.ok_h', 'sub.ok_p'); }
    else { show('sub.err_h', 'sub.err_p'); }
    history.replaceState(null, '', location.pathname + location.hash);
  }

  /* ------------------------------------------------------------ legal dialog */
  var legalCache = {};
  function openLegal(doc) {
    var l = state.lang === 'hu' ? 'hu' : 'en';
    var p = legalCache[l] || (legalCache[l] = fetch(ROOT + 'legal/' + l + '.html', { cache: 'no-cache' }).then(function (r) { return r.text(); }));
    p.then(function (src) {
      var tmp = document.createElement('div'); tmp.innerHTML = src;
      var sec = tmp.querySelector('[data-doc="' + doc + '"]') || tmp.querySelector('[data-doc]');
      var L = state.cfg.legal || {};
      var body = sec.innerHTML.replace(/\{\{(\w+)\}\}/g, function (_, k) {
        var v = L[k]; if (k === 'google') return '';
        return v ? String(v).replace(/[<>&]/g, '') : '<span class="todo">[' + k + ']</span>';
      });
      $('#legal-body').innerHTML = body;
      $$('#legal-body [data-opt]').forEach(function (n) { n.hidden = !L[n.getAttribute('data-opt')]; });
      $$('#legal-body [data-if-recaptcha]').forEach(function (n) { n.hidden = !rcKey(); });
      $$('#legal-body [data-if-google]').forEach(function (n) { n.hidden = !googleOn(); });
      $$('#legal-body [data-if-no-google]').forEach(function (n) { n.hidden = googleOn(); });
      $('#legal-title').textContent = sec.getAttribute('data-title');
      $('#legal-langnote').hidden = (state.lang === 'hu' || state.lang === 'en');
      var d = $('#legal-dlg'); if (!d.open) d.showModal(); $('#legal-body').scrollTop = 0; d.scrollTop = 0;
    });
  }
  function bindLegalLinks() {
    $$('[data-legal]').forEach(function (a) { a.onclick = function (e) { e.preventDefault(); openLegal(a.getAttribute('data-legal')); track('legal_open', { item: a.getAttribute('data-legal') }); }; });
  }
  $$('dialog').forEach(function (d) { d.addEventListener('click', function (e) { if (e.target === d) d.close(); }); });

  /* ------------------------------------------------------------ Google measurement (optional, consent first) */
  function googleOn() { var g = state.cfg.google || {}; return !!(g.ga4 || g.gtm || g.ads); }
  var gLoaded = false;
  function gtag() { window.dataLayer = window.dataLayer || []; window.dataLayer.push(arguments); }
  function track(name, data) { if (gLoaded) gtag('event', name, data || {}); }

  function loadGoogle(c) {
    var g = state.cfg.google;
    gtag('consent', gLoaded ? 'update' : 'default', {
      analytics_storage: c.analytics ? 'granted' : 'denied',
      ad_storage: c.ads ? 'granted' : 'denied', ad_user_data: c.ads ? 'granted' : 'denied', ad_personalization: c.ads ? 'granted' : 'denied'
    });
    if (gLoaded || (!c.analytics && !c.ads)) return;
    gLoaded = true;
    var s = document.createElement('script'); s.async = true;
    if (g.gtm) {
      window.dataLayer.push({ 'gtm.start': Date.now(), event: 'gtm.js' });
      s.src = 'https://www.googletagmanager.com/gtm.js?id=' + encodeURIComponent(g.gtm);
    } else {
      var first = g.ga4 || g.ads;
      s.src = 'https://www.googletagmanager.com/gtag/js?id=' + encodeURIComponent(first);
      gtag('js', new Date());
      if (g.ga4 && c.analytics) gtag('config', g.ga4, { anonymize_ip: true });
      if (g.ads && c.ads) gtag('config', g.ads);
    }
    document.head.appendChild(s);
  }

  function initConsent() {
    if (!googleOn()) return;
    var box = $('#consent'), link = $('#cookie-settings'), g = state.cfg.google;
    $('#nocookie').innerHTML = tr('foot.cookie_on'); $('#nocookie').setAttribute('data-i18n', 'foot.cookie_on');
    link.hidden = false; $('#ck-ads-row').hidden = !g.ads && !g.gtm;
    function save(c) { store.set('um-consent', JSON.stringify({ a: c.analytics ? 1 : 0, m: c.ads ? 1 : 0, t: Date.now() })); box.hidden = true; loadGoogle(c); }
    var saved = null; try { saved = JSON.parse(store.get('um-consent') || 'null'); } catch (e) {}
    if (saved && Date.now() - saved.t < 180 * 86400000) { loadGoogle({ analytics: !!saved.a, ads: !!saved.m }); } else { box.hidden = false; }
    $('#ck-accept').onclick = function () { save({ analytics: true, ads: !!(g.ads || g.gtm) }); };
    $('#ck-reject').onclick = function () { save({ analytics: false, ads: false }); };
    $('#ck-custom').onclick = function () { $('#consent-opts').hidden = false; $('#ck-save').hidden = false; this.hidden = true; };
    $('#ck-save').onclick = function () { save({ analytics: $('#ck-analytics').checked, ads: $('#ck-ads').checked }); };
    link.onclick = function (e) { e.preventDefault(); box.hidden = false; };
  }

  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('[data-dl]');
    if (a && /dl\.php|\.zip/.test(a.href)) { var sec = a.closest('section,header,div.mbar'); track('file_download', { os: a.getAttribute('data-dl'), version: (state[a.getAttribute('data-dl') === 'mac' ? 'mac' : 'win'] || {}).version, item: (sec && (sec.id || sec.className.split(' ')[0])) || 'page', file_name: a.getAttribute('data-dl') === 'mac' ? 'macOS package' : 'Windows package' }); }
  });

  /* ------------------------------------------------------------ studio: themes + layouts */
  function setStudio() {
    var img = $('#studio-img'), src = ROOT + 'img/' + state.layout + '-' + state.theme + '.webp';
    img.classList.add('swap');
    var pre = new Image(); pre.onload = function () { img.src = src; img.width = pre.naturalWidth; img.height = pre.naturalHeight; img.classList.remove('swap'); }; pre.src = src;
    html.setAttribute('data-theme', state.theme);
    $('#theme-desc').innerHTML = tr('th.d_' + state.theme);
    var hero = $('#hero-img'), full = (state.theme === 'claude') ? ROOT + 'img/panel-full-claude.webp' : (state.theme === 'midnight' ? ROOT + 'img/panel-full-midnight.webp' : null);
    if (full && hero.getAttribute('src') !== full) hero.src = full;
  }
  function radio(group, attr, cb) {
    $$('button', group).forEach(function (b) {
      b.onclick = function () { $$('button', group).forEach(function (x) { x.setAttribute('aria-checked', x === b); }); cb(b.getAttribute(attr)); };
    });
  }
  /* history window shots: range buttons like in the app; follows the warm theme when that one is picked */
  state.range = '7d';
  function setHistory() {
    var img = $('#hist-img'), src = ROOT + 'img/history-' + state.range + '-' + (state.theme === 'claude' ? 'claude' : 'midnight') + '.webp';
    if (img.getAttribute('src') === src) return;
    img.classList.add('swap');
    var pre = new Image(); pre.onload = function () { img.src = src; img.classList.remove('swap'); }; pre.src = src;
  }
  radio($('#hist-range'), 'data-range', function (v) { state.range = v; setHistory(); track('history_range', { item: v }); });
  radio($('#swatches'), 'data-theme', function (v) { state.theme = v; setStudio(); setHistory(); track('select_theme', { item: v }); });
  radio($('#layouts'), 'data-layout', function (v) { state.layout = v; setStudio(); track('select_layout', { item: v }); });

  /* ------------------------------------------------------------ tabs */
  (function () {
    var tabs = $$('#tabs [role=tab]');
    function sel(t) { tabs.forEach(function (x) { var on = x === t; x.setAttribute('aria-selected', on); x.tabIndex = on ? 0 : -1; $('#' + x.getAttribute('aria-controls')).hidden = !on; }); }
    tabs.forEach(function (t, i) {
      t.onclick = function () { sel(t); track('details_tab', { item: t.id }); };
      t.onkeydown = function (e) { var d = e.key === 'ArrowRight' ? 1 : (e.key === 'ArrowLeft' ? -1 : 0); if (d) { var n = tabs[(i + d + tabs.length) % tabs.length]; n.focus(); sel(n); } };
    });
  })();

  /* ------------------------------------------------------------ motion (small, purposeful) */
  var calm = matchMedia('(prefers-reduced-motion: reduce)').matches;
  addEventListener('scroll', function () { $('#nav').classList.toggle('is-stuck', scrollY > 12); if (html.classList.contains('is-mobile')) $('#mbar').classList.toggle('show', scrollY > 500); }, { passive: true });
  if ('IntersectionObserver' in window && !calm) {
    html.classList.add('js-reveal');                        // without script (or on a throttled tab) everything is simply visible
    setTimeout(function () { $$('.reveal').forEach(function (n) { n.classList.add('in'); }); }, 4000);
    var io = new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } }); }, { rootMargin: '0px 0px -8% 0px' });
    $$('.reveal').forEach(function (n, i) { n.style.transitionDelay = (i % 4) * 70 + 'ms'; io.observe(n); });
  } else { $$('.reveal').forEach(function (n) { n.classList.add('in'); }); }
  if (!calm && matchMedia('(hover:hover)').matches) {
    var stage = $('#stage'), heroImg = $('#hero-img');
    $('.hero').addEventListener('mousemove', function (e) { var r = stage.getBoundingClientRect(); var x = (e.clientX - r.left - r.width / 2) / r.width, y = (e.clientY - r.top - r.height / 2) / r.height; heroImg.style.setProperty('--ry', (x * 9).toFixed(2) + 'deg'); heroImg.style.setProperty('--rx', (-y * 6).toFixed(2) + 'deg'); });
    $$('.cell').forEach(function (c) { c.addEventListener('mousemove', function (e) { var r = c.getBoundingClientRect(); c.style.setProperty('--mx', (e.clientX - r.left) + 'px'); c.style.setProperty('--my', (e.clientY - r.top) + 'px'); }); });
  }

  /* ------------------------------------------------------------ phones: a desktop app cannot be installed here -> send the link on */
  function share() {
    var url = 'https://claudeusagemonitor.com/' + (state.lang === 'en' ? '' : state.lang + '/'), data = { title: 'Claude Usage Monitor', text: tr('mobile.share_text'), url: url };
    track('share', { method: navigator.share ? 'native' : 'copy_link', item: state.lang });
    if (navigator.share) { navigator.share(data).catch(function () {}); return; }
    (navigator.clipboard ? navigator.clipboard.writeText(url) : Promise.reject()).then(function () { toast(tr('js.copied')); }).catch(function () { prompt('', url); });
  }
  function toast(t) { var n = document.createElement('div'); n.className = 'toast'; n.textContent = t; document.body.appendChild(n); setTimeout(function () { n.remove(); }, 2600); }
  if (html.classList.contains('is-mobile')) { $('#share-hero').hidden = false; $('#mbar').hidden = false; $('#share-hero').onclick = share; $('#share-bar').onclick = share; }

  /* which FAQ / glossary / install-steps block gets opened, and which section is actually reached */
  document.addEventListener('toggle', function (e) {
    var d = e.target; if (!d.open || d.tagName !== 'DETAILS') return;
    var q = d.querySelector('summary'), key = (q && q.getAttribute('data-i18n')) || d.id || 'details';
    track(d.closest('.faq') ? 'faq_open' : 'details_open', { item: key });
  }, true);
  if ('IntersectionObserver' in window) {
    var seen = new IntersectionObserver(function (es) { es.forEach(function (x) { if (x.isIntersecting) { track('section_view', { item: x.target.id }); seen.unobserve(x.target); } }); }, { threshold: 0.35 });
    $$('main section[id]').forEach(function (n) { seen.observe(n); });
  }

  $('#year').textContent = new Date().getFullYear();

  /* ------------------------------------------------------------ start */
  Promise.all([
    loadJSON('config.json').then(function (c) { state.cfg = c || state.cfg; }).catch(function () {}),
    loadJSON('manifest.json').then(function (m) { state.win = m; }).catch(function () {}),
    loadJSON('macos/manifest.json').then(function (m) { if (safeUrl(m.download_url)) state.mac = m; else state.macMissing = true; }).catch(function () { state.macMissing = true; }),
    fetch(ROOT + 'CHANGELOG.md', { cache: 'no-cache' }).then(function (r) { return r.ok ? r.text() : ''; }).then(function (t) { state.log = parseChangelog(t); }).catch(function () {}),
    loadStats()
  ]).then(loadDict).then(function () {
    initConsent(); mailLinkStates(); $$('[data-if-recaptcha]').forEach(function (n) { n.hidden = !rcKey(); });
    // a shared link such as .../#terms opens that legal text (the README of the Backup Kit points there)
    var h = location.hash.slice(1); if (h === 'terms' || h === 'privacy' || h === 'imprint') openLegal(h);
  });
})();
