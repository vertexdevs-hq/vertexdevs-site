/* Vertex · interações do site claro. Dados em casos.js (window.VX). Sem dependências. */
(() => {
  document.documentElement.classList.add('js');
  const VX = window.VX || { areas: [], casos: [] };
  const $ = (s, el = document) => el.querySelector(s);
  const $$ = (s, el = document) => [...el.querySelectorAll(s)];
  const esc = (t) => String(t ?? '').replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
  const AREA = Object.fromEntries(VX.areas.map((a) => [a.id, a]));
  const MOMENTO = { ideia: 'Do zero', rodando: 'Processo rodando', time: 'Time não AI-first' };

  /* ---------- entrada suave ---------- */
  const showIn = (el) => {
    el.classList.add('in');
    $$('.bar .fill', el).forEach((f) => { f.style.width = f.dataset.w; });
  };
  if ('IntersectionObserver' in window) {
    const io = new IntersectionObserver((ents) => ents.forEach((e) => { if (e.isIntersecting) { showIn(e.target); io.unobserve(e.target); } }), { rootMargin: '0px 0px -8% 0px' });
    const watch = () => $$('.reveal:not(.in)').forEach((el) => io.observe(el));
    watch();
    window.__vxWatch = watch;
  } else {
    $$('.reveal').forEach(showIn);
    window.__vxWatch = () => $$('.reveal').forEach(showIn);
  }

  /* ---------- peças reutilizáveis ---------- */
  const bars = (b) => {
    if (!b) return '';
    const max = Math.max(b.antes.v, b.depois.v) || 1;
    const w = (v) => `${v === 0 ? 1 : Math.max(4, Math.round((v / max) * 100))}%`;
    return `<div class="bars" aria-label="${esc(b.rotulo)}">
      <div class="src">${esc(b.rotulo)}</div>
      <div class="bar"><span>${esc(b.antes.nome || 'Antes')}</span><div class="track"><div class="fill" data-w="${w(b.antes.v)}"></div></div><em>${esc(b.antes.label)}</em></div>
      <div class="bar after"><span>${esc(b.depois.nome || 'Depois')}</span><div class="track"><div class="fill" data-w="${w(b.depois.v)}"></div></div><em>${esc(b.depois.label)}</em></div>
    </div>`;
  };
  const flow = (antes, depois) => `<div class="flow">
    ${antes ? `<div class="flow-row"><span class="flow-label">Antes</span><div class="flow-steps">${antes.map((n, i) => `${i ? '<span class="arrow">→</span>' : ''}<span class="node${n.slow ? ' slow' : ''}">${esc(n.t || n)}</span>`).join('')}</div></div>` : ''}
    <div class="flow-row"><span class="flow-label">Com a Vertex</span><div class="flow-steps">${depois.map((n, i) => `${i ? '<span class="arrow">→</span>' : ''}<span class="node${n.ai ? ' ai' : ''}${n.win ? ' win' : ''}">${esc(n.t || n)}</span>`).join('')}</div></div>
  </div>`;
  const caseCard = (c) => `<button class="case reveal" type="button" data-case="${esc(c.id)}" aria-haspopup="dialog">
      <div class="case-tags"><span class="chip area">${esc(AREA[c.area]?.nome || c.area)}</span><span class="chip">${esc(MOMENTO[c.momento] || '')}</span></div>
      <div class="case-big num">${esc(c.grande.valor)}</div>
      <div class="case-big-label">${esc(c.grande.rotulo)}</div>
      <h3>${esc(c.titulo)}</h3>
      ${bars(c.barras)}
      <span class="case-more">Ver o case →</span>
    </button>`;

  /* ---------- abas de áreas (home) ---------- */
  const tabsEl = $('#area-tabs');
  const panelsEl = $('#area-panels');
  if (tabsEl && panelsEl) {
    VX.areas.forEach((a, i) => {
      tabsEl.insertAdjacentHTML('beforeend', `<button class="tab" role="tab" id="tab-${a.id}" aria-controls="panel-${a.id}" aria-selected="${i === 0}" tabindex="${i === 0 ? 0 : -1}">${esc(a.nome)}</button>`);
      const cs = VX.casos.filter((c) => c.area === a.id);
      const ms = cs.flatMap((c) => [c.grande, ...c.metricas]).slice(0, 3);
      panelsEl.insertAdjacentHTML('beforeend', `<div class="panel" role="tabpanel" id="panel-${a.id}" aria-labelledby="tab-${a.id}" ${i ? 'hidden' : ''}>
        <div class="card"><h3 class="h3">${esc(a.titulo)}</h3><p class="muted">${esc(a.resumo)}</p>${flow(a.antes, a.depois)}</div>
        <div class="card"><div class="metrics">${ms.map((m) => `<div class="metric"><b class="num">${esc(m.valor)}</b><span>${esc(m.rotulo)}</span></div>`).join('')}</div>
        <a class="btn btn-ghost" style="padding-left:0;margin-top:.6rem" href="casos.html?area=${a.id}">${cs.length} ${cs.length === 1 ? 'case' : 'cases'} de ${esc(a.nome.toLowerCase())} →</a></div>
      </div>`);
    });
    const tabs = $$('.tab', tabsEl);
    const select = (t) => {
      tabs.forEach((x) => { const on = x === t; x.setAttribute('aria-selected', on); x.tabIndex = on ? 0 : -1; $('#' + x.getAttribute('aria-controls')).hidden = !on; });
      t.focus({ preventScroll: true });
    };
    tabs.forEach((t, i) => {
      t.addEventListener('click', () => select(t));
      t.addEventListener('keydown', (e) => {
        if (e.key === 'ArrowRight') select(tabs[(i + 1) % tabs.length]);
        if (e.key === 'ArrowLeft') select(tabs[(i - 1 + tabs.length) % tabs.length]);
      });
    });
  }

  /* ---------- momento (home) ---------- */
  const momentBtns = $$('.moment');
  if (momentBtns.length && VX.momentos) {
    const pathEl = $('#moment-path');
    const show = (id) => {
      momentBtns.forEach((b) => b.setAttribute('aria-pressed', b.dataset.m === id));
      const m = VX.momentos[id];
      pathEl.innerHTML = `<ol>${m.passos.map((p) => `<li><b>${esc(p.t)}</b><span>${esc(p.d)}</span></li>`).join('')}</ol>`;
    };
    momentBtns.forEach((b) => b.addEventListener('click', () => show(b.dataset.m)));
    show(momentBtns[0].dataset.m);
  }

  /* ---------- grade de cases (home: destaques; casos.html: todos com filtro) ---------- */
  const grid = $('#cases-grid');
  if (grid) {
    const destaque = grid.dataset.destaque === 'true';
    const params = new URLSearchParams(location.search);
    const state = { area: params.get('area') || 'todas', momento: params.get('momento') || 'todos' };
    const render = () => {
      let list = VX.casos;
      if (destaque) list = list.filter((c) => c.destaque).slice(0, 6);
      else list = list.filter((c) => (state.area === 'todas' || c.area === state.area) && (state.momento === 'todos' || c.momento === state.momento));
      grid.innerHTML = list.map(caseCard).join('') || '<p class="muted">Nenhum case com esse filtro ainda.</p>';
      const cnt = $('#cases-count');
      if (cnt) cnt.textContent = `${list.length} ${list.length === 1 ? 'case' : 'cases'}`;
      window.__vxWatch();
    };
    const fA = $('#filter-area');
    const fM = $('#filter-momento');
    const chips = (el, key, opts) => {
      if (!el) return;
      el.innerHTML = `<span>${key === 'area' ? 'Área' : 'Momento'}</span>` + opts.map(([v, t]) => `<button type="button" class="tab" data-v="${v}" aria-pressed="${state[key] === v}">${esc(t)}</button>`).join('');
      $$('button', el).forEach((b) => b.addEventListener('click', () => {
        state[key] = b.dataset.v;
        $$('button', el).forEach((x) => x.setAttribute('aria-selected', x === b));
        const q = new URLSearchParams(); if (state.area !== 'todas') q.set('area', state.area); if (state.momento !== 'todos') q.set('momento', state.momento);
        history.replaceState(null, '', q.toString() ? `?${q}` : location.pathname);
        render();
      }));
      $$('button', el).forEach((x) => x.setAttribute('aria-selected', x.dataset.v === state[key]));
    };
    chips(fA, 'area', [['todas', 'Todas'], ...VX.areas.map((a) => [a.id, a.nome])]);
    chips(fM, 'momento', [['todos', 'Todos'], ...Object.entries(MOMENTO)]);
    render();
  }

  /* ---------- folha de detalhe ---------- */
  const sheet = $('#sheet');
  if (sheet) {
    const body = $('.sheet-body', sheet);
    let last = null;
    const open = (id) => {
      const c = VX.casos.find((x) => x.id === id);
      if (!c) return;
      last = document.activeElement;
      body.innerHTML = `<button class="sheet-close" type="button" aria-label="Fechar">✕</button>
        <div class="case-tags"><span class="chip area">${esc(AREA[c.area]?.nome || c.area)}</span><span class="chip">${esc(MOMENTO[c.momento] || '')}</span></div>
        <h2 class="h3" id="sheet-title">${esc(c.titulo)}</h2>
        <div class="metrics">${c.metricas.map((m) => `<div class="metric"><b class="num">${esc(m.valor)}</b><span>${esc(m.rotulo)}</span></div>`).join('')}</div>
        ${c.fluxo ? flow(c.fluxo.antes, c.fluxo.depois) : ''}
        ${bars(c.barras)}
        <dl><div><dt>O problema</dt><dd>${esc(c.problema)}</dd></div><div><dt>O que fizemos</dt><dd>${esc(c.solucao)}</dd></div></dl>
        <a class="btn btn-primary" href="consulta.html">Quero um resultado assim</a>`;
      sheet.classList.add('open');
      sheet.setAttribute('aria-hidden', 'false');
      requestAnimationFrame(() => $$('.bar .fill', body).forEach((f) => { f.style.width = f.dataset.w; }));
      $('.sheet-close', body).focus();
      $('.sheet-close', body).addEventListener('click', close);
    };
    const close = () => { sheet.classList.remove('open'); sheet.setAttribute('aria-hidden', 'true'); if (last) last.focus(); };
    document.addEventListener('click', (e) => { const b = e.target.closest('[data-case]'); if (b) open(b.dataset.case); });
    sheet.addEventListener('click', (e) => { if (e.target === sheet) close(); });
    document.addEventListener('keydown', (e) => { if (e.key === 'Escape' && sheet.classList.contains('open')) close(); });
    const hash = location.hash.slice(1);
    if (hash && VX.casos.some((c) => c.id === hash)) open(hash);
  }

  /* ---------- curva do hero: desenha ao entrar ---------- */
  const res = $('.curve .result');
  if (res && !matchMedia('(prefers-reduced-motion: reduce)').matches) {
    const len = res.getTotalLength();
    res.style.strokeDasharray = len; res.style.strokeDashoffset = len;
    requestAnimationFrame(() => { res.style.transition = 'stroke-dashoffset 2.2s cubic-bezier(.16,1,.3,1) .3s'; res.style.strokeDashoffset = 0; });
  }
})();
