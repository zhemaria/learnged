/* LearnGED · lesson engine (shared by all math lessons)
   Each page defines window.LESSON = {
     practice: { p1: { ok, hints: {key: text}, right, solution }, ... },
     quiz:     { A: { ok, hints: {key: text}, solution }, ... },
     next: "Lesson 1.2", review: "sections 2, 4, and 5" }
   Feedback as in Lumi: a wrong answer gets a hint and a second try; after the
   second try the solution is shown and explained. Two-option questions show
   the explanation at once (a second try would teach nothing). */
(function () {
  "use strict";
  var L = window.LESSON || {};
  /* Language of the page: <html lang="es"> → Spanish texts; anything else → English */
  var ES = (document.documentElement.lang || "").toLowerCase().indexOf("es") === 0;
  var W = ES ? {
    bien: "<strong>Correcto.</strong>", todavia: "<strong>Todavía no.</strong> ", otraVez: " <strong>Inténtelo de nuevo.</strong>",
    releaEj: "Lea otra vez la pregunta y repase el ejemplo.", relea: "Lea otra vez la pregunta.", eligaOtra: " <strong>Elija otra vez.</strong>",
    sinResp: "<strong>No respondió esta pregunta.</strong> Elija una respuesta.", asi: "<strong>Así se resuelve.</strong> ",
    primera: function (r, t) { return r + " de " + t + " correctas al primer intento"; },
    pend: function (n) { return "Lea las pistas y vuelva a elegir en " + (n === 1 ? "la pregunta marcada" : "las " + n + " preguntas marcadas") + " en amarillo. Después pulse «Revisar otra vez»."; },
    revisarOtra: "Revisar otra vez", revisar: "Revisar mis respuestas",
    exc: function (nx) { return "Excelente. Acertó todas las preguntas al primer intento. El trabajo cuidadoso, paso a paso, da resultado." + (nx ? " Está listo para la " + nx + "." : ""); },
    buen: function (pistas) { return "Buen trabajo. " + (pistas ? "Usó las pistas para corregir sus respuestas: así se aprende. " : "") + "Repase las soluciones que se muestran y haga el quiz una vez más."; },
    repaso: function (rv) { return "Repasemos juntos. Vuelva a leer " + (rv || "la lección") + " y use las actividades de práctica. Después intente el quiz otra vez. Cada intento lo hace más fuerte."; },
    final: function (r, t, f) { return r + " de " + t + " correctas (" + f + " al primer intento, " + (r - f) + " después de una pista)"; },
    tabla: "Tabla de datos", desliza: " (tabla desplazable horizontalmente)", aviso: "↔ Deslice la tabla horizontalmente para ver todas las columnas."
  } : {
    bien: "<strong>Correct.</strong>", todavia: "<strong>Not yet.</strong> ", otraVez: " <strong>Try again.</strong>",
    releaEj: "Read the question again and look back at the example.", relea: "Read the question again.", eligaOtra: " <strong>Choose again.</strong>",
    sinResp: "<strong>You did not answer this one.</strong> Choose an answer.", asi: "<strong>Here is how to solve it.</strong> ",
    primera: function (r, t) { return r + " of " + t + " correct on the first try"; },
    pend: function (n) { return "Read the hints and choose again for the " + n + (n === 1 ? " question" : " questions") + " marked in yellow. Then press \"Check again.\""; },
    revisarOtra: "Check again", revisar: "Check my answers",
    exc: function (nx) { return "Excellent. You got every question on the first try. Careful, step-by-step work pays off." + (nx ? " You are ready for " + nx + "." : ""); },
    buen: function (pistas) { return "Good work. " + (pistas ? "You used the hints to fix your answers. That is how we learn. " : "") + "Look again at the solutions shown, then take the quiz once more."; },
    repaso: function (rv) { return "Let’s review together. Read " + (rv || "the lesson") + " again and use the practice activities. Then try the quiz again. Every try makes you stronger."; },
    final: function (r, t, f) { return r + " of " + t + " correct (" + f + " on the first try, " + (r - f) + " after a hint)"; },
    tabla: "Data table", desliza: " (table you can scroll sideways)", aviso: "↔ Slide the table sideways to see all the columns."
  };
  var PRAISE1 = ES ? ["Trabajó paso a paso. Esa estrategia funciona.", "Buena estrategia: revisó cada parte antes de responder.", "El trabajo cuidadoso da resultado.", "Aplicó bien la regla."] : ["You worked step by step. That strategy works.", "Good strategy: you checked each part before you answered.", "Careful work pays off.", "You used the rule correctly."];
  var PRAISE2 = ES ? ["Aprovechó bien la pista.", "Buena corrección: revisó su trabajo y lo arregló.", "Los errores nos enseñan. Encontró la respuesta correcta."] : ["You used the hint well.", "Good recovery: you checked your work and fixed it.", "Mistakes help us learn. You found the right answer."];
  function one(list) { return list[Math.floor(Math.random() * list.length)]; }
  function mark(o, txt) { var m = o.querySelector('.marca'); if (m) m.remove(); o.insertAdjacentHTML('afterbegin', '<span class="marca">' + txt + '</span>'); }

  /* ---------- Practice ---------- */
  document.querySelectorAll('.opciones[data-practica]').forEach(function (group) {
    var id = group.getAttribute('data-practica'), d = (L.practice || {})[id], tries = 0, r = document.getElementById('r-' + id);
    if (!d) return;
    var options = group.querySelectorAll('.opcion'), binary = options.length <= 2;
    options.forEach(function (op) {
      op.addEventListener('click', function () {
        if (op.disabled) return;
        var k = op.getAttribute('data-k');
        tries++;
        if (k === d.ok) {
          op.classList.add('correcta'); mark(op, '✓ ');
          options.forEach(function (o) { o.disabled = true; });
          r.className = 'respuesta-int bien';
          r.innerHTML = W.bien + ' ' + d.right + ' <em>' + (tries === 1 ? one(PRAISE1) : one(PRAISE2)) + '</em>';
        } else if (tries === 1 && !binary) {
          op.classList.add('incorrecta'); op.disabled = true; mark(op, '✗ ');
          r.className = 'respuesta-int pista';
          r.innerHTML = W.todavia + ((d.hints || {})[k] || d.hint || W.releaEj) + W.otraVez;
        } else {
          op.classList.add('incorrecta'); mark(op, '✗ ');
          options.forEach(function (o) {
            o.disabled = true;
            if (o.getAttribute('data-k') === d.ok) { o.classList.add('correcta'); mark(o, '✓ '); }
          });
          r.className = 'respuesta-int mal';
          r.innerHTML = W.asi + d.solution;
        }
      });
    });
  });

  /* ---------- Practice quiz (two rounds) ---------- */
  var Q = L.quiz || {}, round = 1, first = 0;
  var blocks = document.querySelectorAll('#quiz .quiz-bloque');
  var btn = document.getElementById('btn-calificar'), again = document.getElementById('btn-reintentar');
  if (blocks.length && btn) {
    blocks.forEach(function (bl) {
      bl.querySelectorAll('.opcion').forEach(function (op) {
        op.setAttribute('aria-pressed', 'false');
        op.addEventListener('click', function () {
          if (op.disabled) return;
          bl.querySelectorAll('.opcion').forEach(function (o) { o.classList.remove('elegida'); o.setAttribute('aria-pressed', 'false'); });
          op.classList.add('elegida'); op.setAttribute('aria-pressed', 'true');
        });
      });
    });
    btn.addEventListener('click', function () {
      var right = 0, pending = 0;
      blocks.forEach(function (bl) {
        if (bl.getAttribute('data-hecho') === 'si') { right++; return; }
        var d = Q[bl.getAttribute('data-q')], r = bl.querySelector('.respuesta-int'), el = bl.querySelector('.opcion.elegida');
        var k = el ? el.getAttribute('data-k') : null, binary = bl.querySelectorAll('.opcion').length <= 2;
        if (k === d.ok) {
          right++; if (round === 1) first++;
          bl.setAttribute('data-hecho', 'si');
          bl.querySelectorAll('.opcion').forEach(function (o) { o.disabled = true; });
          el.classList.add('correcta'); mark(el, '✓ ');
          r.className = 'respuesta-int bien'; r.innerHTML = W.bien;
        } else if (round === 1 && !binary) {
          pending++;
          if (el) { el.classList.remove('elegida'); el.classList.add('incorrecta'); el.disabled = true; el.setAttribute('aria-pressed', 'false'); mark(el, '✗ '); }
          r.className = 'respuesta-int pista';
          r.innerHTML = el ? W.todavia + ((d.hints || {})[k] || W.relea) + W.eligaOtra : W.sinResp;
        } else {
          bl.setAttribute('data-hecho', 'si');
          bl.querySelectorAll('.opcion').forEach(function (o) {
            o.disabled = true;
            if (o.getAttribute('data-k') === d.ok) { o.classList.add('correcta'); mark(o, '✓ '); }
          });
          if (el) { el.classList.add('incorrecta'); mark(el, '✗ '); }
          r.className = 'respuesta-int mal'; r.innerHTML = W.asi + d.solution;
        }
      });
      var total = blocks.length, box = document.getElementById('marcador');
      if (round === 1 && pending > 0) {
        round = 2;
        document.getElementById('puntaje').textContent = W.primera(right, total);
        document.getElementById('mensaje').textContent = W.pend(pending);
        box.style.background = '#fdf3df';
        document.getElementById('barra').style.width = Math.round(right / total * 100) + '%';
        box.classList.add('visible');
        btn.textContent = W.revisarOtra;
        var f = document.querySelector('#quiz .quiz-bloque:not([data-hecho]) .opcion:not([disabled])'); if (f) f.focus();
        return;
      }
      var pct = Math.round(right / total * 100), msg, color;
      if (first === total) { msg = W.exc(L.next); color = '#e7f4ec'; }
      else if (pct >= 75) { msg = W.buen(right > first); color = '#e7f4ec'; }
      else { msg = W.repaso(L.review); color = '#fdecea'; }
      document.getElementById('puntaje').textContent = W.final(right, total, first);
      document.getElementById('mensaje').textContent = msg;
      var pose = first === total ? 'felicidades' : (pct >= 75 ? 'bien' : 'piensa'), oldImg = box.querySelector('.leo-final');
      if (oldImg) oldImg.remove();
      if (window.leoImg) box.insertAdjacentHTML('afterbegin', window.leoImg(pose, 'leo-final', 120));
      box.style.background = color; box.classList.add('visible');
      document.getElementById('barra').style.width = pct + '%';
      btn.style.display = 'none';
      again.style.display = 'inline-block'; again.focus();
    });
    again.addEventListener('click', function () {
      round = 1; first = 0;
      blocks.forEach(function (bl) {
        bl.removeAttribute('data-hecho');
        var r = bl.querySelector('.respuesta-int'); r.className = 'respuesta-int'; r.innerHTML = '';
        bl.querySelectorAll('.opcion').forEach(function (o) { o.disabled = false; o.classList.remove('correcta', 'incorrecta', 'elegida'); o.setAttribute('aria-pressed', 'false'); var m = o.querySelector('.marca'); if (m) m.remove(); });
      });
      var lf = document.querySelector('#marcador .leo-final'); if (lf) lf.remove();
      document.getElementById('marcador').classList.remove('visible');
      document.getElementById('puntaje').textContent = ''; document.getElementById('mensaje').textContent = '';
      btn.textContent = W.revisar; btn.style.display = 'inline-block';
      again.style.display = 'none';
      var f = document.querySelector('#quiz .opcion'); if (f) f.focus();
    });
  }

  /* ---------- Responsive tables: show the "slide" hint only when needed ---------- */
  var pairs = [];
  document.querySelectorAll('table').forEach(function (t) {
    var box = t.parentNode;
    if (!box.classList.contains('tabla-scroll')) {
      var cap = t.querySelector('caption');
      var wrap = document.createElement('div');
      wrap.className = 'tabla-scroll'; wrap.setAttribute('role', 'region'); wrap.setAttribute('tabindex', '0');
      wrap.setAttribute('aria-label', (cap ? cap.textContent.trim() : W.tabla) + W.desliza);
      t.parentNode.insertBefore(wrap, t); wrap.appendChild(t); box = wrap;
    }
    var hint = box.nextElementSibling;
    if (!hint || !hint.classList.contains('aviso-desliza')) {
      hint = document.createElement('p'); hint.className = 'aviso-desliza';
      hint.textContent = W.aviso;
      box.parentNode.insertBefore(hint, box.nextSibling);
    }
    pairs.push({ box: box, hint: hint });
  });
  function update() { pairs.forEach(function (p) { p.hint.style.display = (p.box.scrollWidth > p.box.clientWidth + 2) ? 'block' : 'none'; }); }
  update();
  var tm; window.addEventListener('resize', function () { clearTimeout(tm); tm = setTimeout(update, 150); });
})();

/* ---------- Leo, the LearnGED owl (decorative: the text already says everything) ----------
   Right answer → leo-bien · first mistake (hint) → leo-piensa · solution shown → leo-pista
   The lesson header gets Leo waving. Images use alt="" so screen readers skip them. */
(function () {
  var POSE = { bien: "bien", pista: "piensa", mal: "pista" };
  function leoImg(pose, cls, size) { return '<img class="' + cls + '" src="/img/leo-' + pose + '.svg" alt="" aria-hidden="true" data-pose="' + pose + '" width="' + size + '" height="' + size + '">'; }
  window.leoImg = leoImg;
  function pon(el) {
    var pose = null;
    for (var k in POSE) if (el.classList.contains(k)) pose = POSE[k];
    var img = null;
    for (var i = 0; i < el.children.length; i++) if (el.children[i].classList.contains("leo-fb")) img = el.children[i];
    if (!pose || !el.textContent.trim()) { if (img) img.remove(); return; }
    if (img && img.getAttribute("data-pose") === pose) return;
    if (img) img.remove();
    el.insertAdjacentHTML("afterbegin", leoImg(pose, "leo-fb", 56));
  }
  document.querySelectorAll(".fb, .respuesta-int").forEach(function (el) {
    pon(el);
    new MutationObserver(function () { pon(el); }).observe(el, { childList: true, attributes: true, attributeFilter: ["class"] });
  });
  var head = document.querySelector("header.principal .envoltura-header") || document.querySelector("header.principal");
  if (head && !head.querySelector(".leo-hola")) head.insertAdjacentHTML("afterbegin", leoImg("saludo", "leo-hola", 110));
})();
