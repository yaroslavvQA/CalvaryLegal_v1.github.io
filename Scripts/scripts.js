/* ── SCROLL REVEAL ── */
const reveals = document.querySelectorAll('.reveal');
const obs = new IntersectionObserver(es => {
  es.forEach(e => { if (e.isIntersecting) e.target.classList.add('visible'); });
}, { threshold: 0.1 });
reveals.forEach(el => obs.observe(el));

/* ── NAV SHRINK ── */
window.addEventListener('scroll', () => {
  document.getElementById('mainNav').style.height = window.scrollY > 60 ? '60px' : '72px';
});

/* ── MOBILE MENU ── */
function toggleMenu() {
  document.getElementById('mobileNav').classList.toggle('open');
}

/* ── ACTIVE NAV ON SCROLL ── */
const sections = document.querySelectorAll('section[id]');
window.addEventListener('scroll', () => {
  let current = '';
  sections.forEach(s => {
    if (window.scrollY >= s.offsetTop - 100) current = s.getAttribute('id');
  });
  document.querySelectorAll('.nav-links a').forEach(a => {
    a.classList.remove('active');
    if (a.getAttribute('href') === '#' + current) a.classList.add('active');
  });
});

/* ── JURISDICTION TABS (cross-border.html) ── */
function showJur(key) {
  document.querySelectorAll('.jur-tab').forEach(t => t.classList.remove('active'));
  document.querySelectorAll('.jur-profiles').forEach(p => p.classList.remove('active'));
  event.target.classList.add('active');
  document.getElementById('jur-' + key).classList.add('active');
  document.querySelectorAll('#jur-' + key + ' .reveal:not(.visible)').forEach(el => {
    obs.observe(el);
  });
}
