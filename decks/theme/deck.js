(function () {
  const slides = document.querySelectorAll('.slide');
  const bar = document.getElementById('bar');
  const stage = document.getElementById('stage');
  let current = 0;
  const total = slides.length;

  function fitStage() {
    const w = 1600, h = 900;
    const scale = Math.min(window.innerWidth / w, window.innerHeight / h);
    stage.style.transform = `scale(${scale})`;
    stage.style.left = `${(window.innerWidth - w * scale) / 2}px`;
    stage.style.top = `${(window.innerHeight - h * scale) / 2}px`;
  }
  window.addEventListener('resize', fitStage);
  fitStage();

  function show(i) {
    if (i < 0) i = 0;
    if (i >= total) i = total - 1;
    slides[current].classList.remove('active');
    current = i;
    slides[current].classList.add('active');
    bar.style.width = `${((current + 1) / total) * 100}%`;
  }

  window.addEventListener('keydown', function (e) {
    switch (e.key) {
      case 'ArrowRight': case 'ArrowDown': case 'PageDown': case ' ': case 'Enter':
        e.preventDefault(); show(current + 1); break;
      case 'ArrowLeft': case 'ArrowUp': case 'PageUp': case 'Backspace':
        e.preventDefault(); show(current - 1); break;
      case 'Home': e.preventDefault(); show(0); break;
      case 'End':  e.preventDefault(); show(total - 1); break;
      case 'f': case 'F':
        if (!document.fullscreenElement) document.documentElement.requestFullscreen().catch(() => {});
        else document.exitFullscreen().catch(() => {});
        break;
    }
  });

  stage.addEventListener('click', function (e) {
    const rect = stage.getBoundingClientRect();
    if (e.clientX - rect.left < rect.width * 0.3) show(current - 1); else show(current + 1);
  });
  stage.addEventListener('contextmenu', function (e) { e.preventDefault(); show(current - 1); });

  show(0);
})();
