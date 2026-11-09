/* Scroll reveal, count-up numbers, and pausing SVG animations for reduced-motion users. */
(() => {
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (reduce) document.querySelectorAll('svg').forEach(s => s.pauseAnimations && s.pauseAnimations());

  const countUp = el => {
    const m = el.textContent.match(/^(\D*)(\d+)(.*)$/); if (!m || reduce) return;
    const [, pre, n, post] = m, end = +n, t0 = performance.now(), dur = 1200;
    const tick = now => { const k = Math.min(1, (now - t0) / dur), e = 1 - Math.pow(1 - k, 3);
      el.textContent = pre + Math.round(end * e) + post; if (k < 1) requestAnimationFrame(tick); };
    requestAnimationFrame(tick);
  };

  const io = new IntersectionObserver(entries => entries.forEach(en => {
    if (!en.isIntersecting) return;
    en.target.classList.add('in');
    en.target.querySelectorAll('[data-count]').forEach(countUp);
    io.unobserve(en.target);
  }), { threshold: 0.12 });
  document.querySelectorAll('.reveal').forEach(el => io.observe(el));
})();
