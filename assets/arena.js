/* A small top-down arena: four fixed-wing aircraft with a pursuit / patrol mix.
   Each aircraft has a forward camera cone; holding a target in it for 4 s scores a lock (+10, target −2),
   using the same rules as the real referee. Purely decorative and self-contained. */
(() => {
  const cv = document.getElementById('arena'), ctx = cv.getContext('2d');
  const W = cv.width, H = cv.height, R = 10;                // px per "10 m"
  const teams = [
    { name:'Kartal',  color:'#2f6fde' }, { name:'Şimşek', color:'#c2412d' },
    { name:'Doğan',   color:'#2e8b57' }, { name:'Martı',  color:'#c98a12' } ];
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const css = n => getComputedStyle(document.documentElement).getPropertyValue(n).trim();
  const ac = teams.map((t, i) => ({ ...t, i, score:0, x: W*(.2+.6*Math.random()), y: H*(.2+.6*Math.random()),
     h: Math.random()*6.283, v: 1.6 + Math.random()*.5, hunter: i % 2 === 0, target: null, hold:0, trail:[] }));
  const board = document.getElementById('board'), feed = document.getElementById('feed');
  const clockEl = document.getElementById('clock');
  const T = Object.assign({ start:'Match started · 4 teams airborne', lock:'{a} lock on {b}  +10', attack:'attack', evade:'evade' }, window.ARENA_TEXT || {});
  let t = 0, lines = [];
  const log = (s, cls) => { const m = String(Math.floor(t/60)).padStart(2,'0')+':'+String(Math.floor(t%60)).padStart(2,'0');
    lines.unshift(`<div class="${cls||''}">${m}  ${s}</div>`); lines = lines.slice(0,3); feed.innerHTML = lines.join(''); };
  const drawBoard = () => board.innerHTML = ac.map(a =>
    `<div><span class="sw" style="background:${a.color}"></span>${a.name}<b>${a.score}</b></div>`).join('');
  drawBoard(); log(T.start);

  const ang = (a) => Math.atan2(Math.sin(a), Math.cos(a));
  const FOV = 0.38, RANGE = 150;

  function step(dt) {
    t += dt;
    for (const a of ac) {
      // pick nearest other as target (hunters) or wander (patrol)
      let desired;
      if (a.hunter) {
        let best = null, bd = 1e9;
        for (const b of ac) if (b !== a) { const d = Math.hypot(b.x-a.x, b.y-a.y); if (d < bd) { bd = d; best = b; } }
        a.target = best;
        desired = Math.atan2(best.y - a.y, best.x - a.x);
      } else {
        desired = a.h + Math.sin(t*0.6 + a.i) * 0.9;
      }
      // geofence: steer back toward centre near edges
      const m = 50; if (a.x < m || a.x > W-m || a.y < m || a.y > H-m) desired = Math.atan2(H/2 - a.y, W/2 - a.x);
      const turn = Math.max(-0.045, Math.min(0.045, ang(desired - a.h)));   // bank-limited turn rate
      a.h += turn * dt * 60;
      a.x += Math.cos(a.h) * a.v * dt * 60; a.y += Math.sin(a.h) * a.v * dt * 60;
      a.trail.push([a.x, a.y]); if (a.trail.length > 70) a.trail.shift();
    }
    // lock-on check (hunters only, target must stay in cone 4 s)
    for (const a of ac) {
      if (!a.hunter || !a.target) continue;
      const b = a.target, d = Math.hypot(b.x-a.x, b.y-a.y), off = Math.abs(ang(Math.atan2(b.y-a.y, b.x-a.x) - a.h));
      if (d < RANGE && off < FOV) { a.hold += dt; if (a.hold >= 4) { a.score += 10; b.score -= 2; a.hold = 0;
          log(T.lock.replace('{a}', a.name).replace('{b}', b.name), 'pos'); drawBoard(); a.v = 1.4 + Math.random()*.6; } }
      else if (a.hold > 0) { a.hold = Math.max(0, a.hold - dt*3); }
    }
    // occasional role swap keeps it lively (evasion matters too)
    if (Math.random() < dt * 0.04) { const a = ac[Math.floor(Math.random()*4)]; a.hunter = !a.hunter; a.hold = 0;
      log(`${a.name} → ${a.hunter ? T.attack : T.evade}`); }
    clockEl.textContent = String(Math.floor(t/60)).padStart(2,'0')+':'+String(Math.floor(t%60)).padStart(2,'0');
  }

  function draw() {
    const line = css('--line'), quiet = css('--quiet');
    ctx.clearRect(0,0,W,H);
    // grid
    ctx.strokeStyle = line; ctx.lineWidth = 1; ctx.globalAlpha = .6;
    for (let x = 0; x <= W; x += 64) { ctx.beginPath(); ctx.moveTo(x,0); ctx.lineTo(x,H); ctx.stroke(); }
    for (let y = 0; y <= H; y += 64) { ctx.beginPath(); ctx.moveTo(0,y); ctx.lineTo(W,y); ctx.stroke(); }
    ctx.globalAlpha = 1;
    // geofence + QR target
    ctx.setLineDash([6,6]); ctx.strokeStyle = quiet; ctx.strokeRect(30,30,W-60,H-60); ctx.setLineDash([]);
    ctx.fillStyle = quiet; ctx.font = '11px ui-monospace, monospace'; ctx.fillText('GEOFENCE', 36, 46);
    ctx.strokeStyle = quiet; ctx.strokeRect(W/2-9, H/2-9, 18, 18); ctx.fillText('QR', W/2-7, H/2+24);
    for (const a of ac) {
      // trail
      ctx.strokeStyle = a.color; ctx.globalAlpha = .35; ctx.lineWidth = 2; ctx.beginPath();
      a.trail.forEach(([x,y],k) => k ? ctx.lineTo(x,y) : ctx.moveTo(x,y)); ctx.stroke(); ctx.globalAlpha = 1;
      // camera cone
      if (a.hunter) {
        ctx.fillStyle = a.color; ctx.globalAlpha = a.hold > 0 ? .10 + .25*(a.hold/4) : .07;
        ctx.beginPath(); ctx.moveTo(a.x,a.y); ctx.arc(a.x,a.y,RANGE,a.h-FOV,a.h+FOV); ctx.closePath(); ctx.fill(); ctx.globalAlpha = 1;
        if (a.hold > 0 && a.target) { // lock progress ring on target
          ctx.strokeStyle = a.color; ctx.lineWidth = 2.5; ctx.beginPath();
          ctx.arc(a.target.x, a.target.y, 14, -1.571, -1.571 + 6.283*(a.hold/4)); ctx.stroke(); }
      }
      // aircraft glyph
      ctx.save(); ctx.translate(a.x,a.y); ctx.rotate(a.h); ctx.fillStyle = a.color;
      ctx.beginPath(); ctx.moveTo(9,0); ctx.lineTo(-6,-8); ctx.lineTo(-3,0); ctx.lineTo(-6,8); ctx.closePath(); ctx.fill();
      ctx.restore();
    }
  }

  let last = performance.now();
  function frame(now) { const dt = Math.min(.05, (now-last)/1000); last = now; step(dt); draw(); requestAnimationFrame(frame); }
  if (reduce) { for (let k = 0; k < 400; k++) step(1/30); draw(); } else requestAnimationFrame(frame);
})();
