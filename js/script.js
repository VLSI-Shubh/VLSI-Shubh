// Reveal-on-scroll animations
const reveals = document.querySelectorAll(".reveal");
if ('IntersectionObserver' in window) {
  reveals.forEach(el => el.classList.add('is-hidden'));
  const io = new IntersectionObserver((entries) => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        e.target.classList.add('is-visible');
        io.unobserve(e.target);
      }
    });
  }, { threshold: 0.05 });
  reveals.forEach(el => io.observe(el));
}

// Theme toggle: System → Dark → Light
(function(){
  const btn = document.getElementById('themeToggle');
  const root = document.documentElement;
  const KEY = 'themePreference';

  const icons = {
    system:`<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="14" rx="2"></rect><line x1="8" y1="22" x2="16" y2="22"></line><line x1="12" y1="18" x2="12" y2="22"></line></svg>`,
    dark:`<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>`,
    light:`<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/><line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/></svg>`
  };

  const sysPrefersDark = () => window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
  const load = () => { try { return localStorage.getItem(KEY) || 'system'; } catch { return 'system'; } };
  const save = v => { try { localStorage.setItem(KEY, v); } catch {} };
  const next = v => v==='system' ? 'dark' : v==='dark' ? 'light' : 'system';

  function apply(pref){
    const theme = pref === 'system' ? (sysPrefersDark() ? 'dark' : 'light') : pref;
    root.setAttribute('data-theme', theme);
    btn.innerHTML = icons[pref] || icons.system;
    btn.setAttribute('aria-label', `Theme: ${pref}`);
  }

  let pref = load();
  apply(pref);
  btn.addEventListener('click', () => {
    pref = next(pref);
    save(pref);
    apply(pref);
  });

  const mq = window.matchMedia('(prefers-color-scheme: dark)');
  mq.addEventListener?.('change', () => { if (load()==='system') apply('system'); });
})();

// Hamburger menu toggle
(function(){
  const hamburger = document.getElementById('hamburger');
  const navMenu = document.getElementById('navMenu');
  const navLinks = document.querySelectorAll('.nav-link');

  hamburger.addEventListener('click', () => {
    hamburger.classList.toggle('active');
    navMenu.classList.toggle('active');
    document.body.style.overflow = navMenu.classList.contains('active') ? 'hidden' : '';
  });

  navLinks.forEach(link => {
    link.addEventListener('click', () => {
      hamburger.classList.remove('active');
      navMenu.classList.remove('active');
      document.body.style.overflow = '';
    });
  });
})();

// Smart sticky nav (shows/hides navbar background on scroll)
(function(){
  let lastY = window.scrollY || 0;
  const body = document.body;

  const onScroll = () => {
    const y = window.scrollY || 0;
    if (y > 8) body.classList.add('nav-scrolled');
    else body.classList.remove('nav-scrolled');
    lastY = y;
  };

  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();
})();

// Go to Top button
(function(){
  const goToTopBtn = document.getElementById('goToTop');

  window.addEventListener('scroll', () => {
    if (window.scrollY > 500) {
      goToTopBtn.classList.add('visible');
    } else {
      goToTopBtn.classList.remove('visible');
    }
  }, { passive: true });

  goToTopBtn.addEventListener('click', () => {
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
  });
})();

// Certificate preview modal
(function(){
  const modal = document.getElementById('certModal');
  const modalImg = document.getElementById('certModalImg');
  const modalTitle = document.getElementById('certModalTitle');
  const closeBtn = document.getElementById('certModalClose');

  if (!modal || !modalImg || !modalTitle || !closeBtn) return;

  const openModal = (title, src) => {
    modalTitle.textContent = title || 'Preview';
    modalImg.src = src;
    modal.classList.add('open');
    document.body.style.overflow = 'hidden';
  };

  const closeModal = () => {
    modal.classList.remove('open');
    modalImg.src = '';
    document.body.style.overflow = '';
  };

  closeBtn.addEventListener('click', closeModal);
  modal.addEventListener('click', (e) => { if (e.target === modal) closeModal(); });
  window.addEventListener('keydown', (e) => { if (e.key === 'Escape') closeModal(); });

  // Bind preview buttons to the image in the same cert card
  document.querySelectorAll('.cert-preview-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const card = btn.closest('.cert-card');
      const img = card ? card.querySelector('.cert-image img') : null;
      if (!img) return;

      const src = img.getAttribute('src');
      if (!src) return;

      const title =
        (card.querySelector('.cert-title') && card.querySelector('.cert-title').textContent) ||
        (card.querySelector('h3') && card.querySelector('h3').textContent) ||
        'Certificate';

      openModal(title.trim(), src);
    });
  });

  // Also allow clicking the certificate image to preview
  document.querySelectorAll('.cert-image img').forEach(img => {
    img.style.cursor = 'pointer';
    img.addEventListener('click', () => {
      const card = img.closest('.cert-card');
      const title =
        (card && card.querySelector('.cert-title') && card.querySelector('.cert-title').textContent) ||
        (card && card.querySelector('h3') && card.querySelector('h3').textContent) ||
        'Certificate';

      openModal(title.trim(), img.getAttribute('src'));
    });
  });
})();
