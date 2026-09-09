(function () {
  "use strict";

  var STORAGE_KEY = "bi_python_zth_site_progress_v1";
  var TOTAL = document.querySelectorAll(".module-card[data-module]").length;

  function load() {
    try {
      var raw = localStorage.getItem(STORAGE_KEY);
      var arr = raw ? JSON.parse(raw) : [];
      return new Set(Array.isArray(arr) ? arr : []);
    } catch (e) {
      return new Set();
    }
  }

  function save(set) {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(Array.from(set)));
    } catch (e) {
      // Sin localStorage (modo privado, etc.) el sitio sigue funcionando, solo sin memoria.
    }
  }

  var visited = load();

  function render() {
    document.querySelectorAll(".module-card[data-module]").forEach(function (card) {
      var id = card.getAttribute("data-module");
      card.classList.toggle("module-visited", visited.has(id));
    });

    var countEl = document.getElementById("progressCount");
    var fillEl = document.getElementById("progressFill");
    var resetBtn = document.getElementById("progressReset");
    if (!countEl || !fillEl) return;

    var n = visited.size;
    var pct = TOTAL ? Math.round((n / TOTAL) * 100) : 0;
    countEl.textContent = n + " / " + TOTAL + " modulos visitados";
    fillEl.style.width = pct + "%";
    if (resetBtn) resetBtn.hidden = n === 0;
  }

  document.querySelectorAll('.module-card[data-module] a.view-link').forEach(function (link) {
    link.addEventListener("click", function () {
      var card = link.closest(".module-card[data-module]");
      if (!card) return;
      visited.add(card.getAttribute("data-module"));
      save(visited);
      render();
    });
  });

  var resetBtn = document.getElementById("progressReset");
  if (resetBtn) {
    resetBtn.addEventListener("click", function () {
      visited = new Set();
      save(visited);
      render();
    });
  }

  render();
})();
