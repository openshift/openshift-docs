(function() {
  var KEY = 'nav-expanded';

  function load() {
    try { return new Set(JSON.parse(localStorage.getItem(KEY))); }
    catch(e) { return new Set(); }
  }

  function save(set) {
    try { localStorage.setItem(KEY, JSON.stringify(Array.from(set))); }
    catch(e) {}
  }

  function toggle(li, expanded) {
    var a = li.querySelector('.nav-item > a');
    var k = a ? a.getAttribute('href') : null;
    if (li.classList.contains('expanded')) {
      li.classList.remove('expanded');
      if (k) expanded.delete(k);
    } else {
      li.classList.add('expanded');
      if (k) expanded.add(k);
    }
    save(expanded);
  }

  var expanded = load();

  // Restore previously expanded items
  document.querySelectorAll('#left-nav li').forEach(function(li) {
    var a = li.querySelector(':scope > .nav-item > a');
    var k = a ? a.getAttribute('href') : null;
    if (k && expanded.has(k)) {
      li.classList.add('expanded');
    }
  });

  // Auto-expand path to active item
  var active = document.querySelector('#left-nav a.active');
  if (active) {
    var el = active.closest('li');
    while (el && el.id !== 'left-nav') {
      if (el.tagName === 'LI') {
        el.classList.add('expanded');
        var a = el.querySelector(':scope > .nav-item > a');
        var k = a ? a.getAttribute('href') : null;
        if (k) expanded.add(k);
      }
      el = el.parentElement;
    }
  }
  save(expanded);

  // Toggle arrow: expand/collapse children
  // Link: navigate to the page (default browser behavior)
  document.querySelectorAll('#left-nav .nav-toggle').forEach(function(t) {
    t.addEventListener('click', function(e) {
      e.preventDefault();
      e.stopPropagation();
      toggle(t.closest('li'), expanded);
    });
  });

  // Right TOC: scroll highlight
  var rightToc = document.getElementById('right-toc');
  if (!rightToc) return;
  var links = rightToc.querySelectorAll('a');
  if (links.length === 0) return;
  function update() {
    var cur = null;
    links.forEach(function(a) {
      a.classList.remove('active');
      var el = document.getElementById(a.getAttribute('href').substring(1));
      if (el && el.getBoundingClientRect().top <= 100) cur = a;
    });
    if (cur) cur.classList.add('active');
  }
  window.addEventListener('scroll', function() { requestAnimationFrame(update); });
  update();
})();
