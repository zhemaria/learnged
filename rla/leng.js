/* LearnGED · Artes del lenguaje: voz y actividades de lectura (lecciones y prácticas).
   Se carga después de /math/lesson.js o de /math/practice.js y /science/sci.js.
   Misma filosofía que el resto de LearnGED: primer error → pista y otro intento;
   segundo error → la respuesta, explicada.
   José M. Fernández · CC BY-NC-SA 4.0 */
(function () {
  "use strict";
  var ES = (document.documentElement.lang || "").toLowerCase().indexOf("es") === 0;
  function $(id) { return document.getElementById(id); }
  function cada(sel, f, raiz) { Array.prototype.forEach.call((raiz || document).querySelectorAll(sel), f); }
  function baraja(a) { a = a.slice(); for (var i = a.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)), t = a[i]; a[i] = a[j]; a[j] = t; } return a; }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }
  var ELO = ["Buen trabajo.", "Así se hace.", "Muy bien leído.", "Excelente."];
  function elogio() { return ELO[Math.floor(Math.random() * ELO.length)]; }

  /* ================= Voz ================= */
  var hay = "speechSynthesis" in window, voz = null;
  function elegir() {
    if (!hay) return;
    var vs = speechSynthesis.getVoices().filter(function (v) { return ES ? /^es/i.test(v.lang) : /^en/i.test(v.lang); });
    var pref = ES ? ["es-us", "es-mx", "es-419", "es-co", "es-es"] : ["en-us", "en-gb"];
    voz = null;
    for (var i = 0; i < pref.length && !voz; i++) voz = vs.filter(function (v) { return v.lang.replace("_", "-").toLowerCase() === pref[i]; })[0] || null;
    if (!voz) voz = vs[0] || null;
  }
  if (hay) { elegir(); speechSynthesis.onvoiceschanged = elegir; }
  function frase(t, vel) {
    var u = new SpeechSynthesisUtterance(t);
    u.lang = voz ? voz.lang : (ES ? "es-US" : "en-US"); if (voz) u.voice = voz; u.rate = vel || 0.9; return u;
  }
  function aviso() { cada(".aviso-voz", function (a) { a.hidden = false; }); }
  /* hablar(texto, velocidad, alTerminar): se lee por oraciones, porque algunos navegadores cortan las lecturas largas */
  function hablar(texto, vel, fin) {
    if (!hay || !texto) { aviso(); if (fin) fin(); return; }
    speechSynthesis.cancel();
    var partes = texto.replace(/\s+/g, " ").match(/[^.!?…]+[.!?…]+[»"”)]*\s*|[^.!?…]+$/g) || [texto];
    partes.forEach(function (t, i) { var u = frase(t.trim(), vel); if (fin && i === partes.length - 1) u.onend = fin; speechSynthesis.speak(u); });
  }
  function hablarPalabras(texto) {
    if (!hay) { aviso(); return; }
    speechSynthesis.cancel();
    texto.replace(/[.,;:¿?¡!—«»]/g, " ").split(/\s+/).filter(Boolean).forEach(function (p) { speechSynthesis.speak(frase(p, 0.7)); });
  }
  function callar() { if (hay) speechSynthesis.cancel(); }
  window.hablar = hablar; window.hablarPalabras = hablarPalabras; window.callar = callar;
  if (!hay) document.addEventListener("DOMContentLoaded", aviso);

  /* Botones [data-hablar="texto"] (velocidad opcional en data-vel), [data-hablar-palabras] y [data-callar].
     Delegación: sirve también para los botones que se crean después (ejercicios nuevos). */
  function botonesVoz(raiz) {
    cada("[data-hablar]", function (b) { if (!b.getAttribute("aria-label") && !b.textContent.replace(/🔊/g, "").trim()) b.setAttribute("aria-label", "Escuchar: " + b.getAttribute("data-hablar")); }, raiz);
  }
  document.addEventListener("click", function (ev) {
    var b = ev.target.closest && ev.target.closest("[data-hablar],[data-hablar-palabras],[data-callar]");
    if (!b) return;
    if (b.hasAttribute("data-callar")) return callar();
    if (b.hasAttribute("data-hablar-palabras")) return hablarPalabras(b.getAttribute("data-hablar-palabras"));
    hablar(b.getAttribute("data-hablar"), parseFloat(b.getAttribute("data-vel")) || 0.85);
  });

  /* Sonidos grabados: <button data-sonido="sal" hidden> y su nota <p class="nota-audio" data-nota="sal">.
     Si existe /es/artes-del-lenguaje/audio/sal.(mp3|m4a|wav), el botón aparece y la nota se oculta. */
  var AUDIO = "/es/artes-del-lenguaje/audio/", EXT = ["mp3", "m4a", "wav"], grab = {};
  function cargar(clave, cb) {
    if (clave in grab) return cb(grab[clave]);
    var i = 0;
    (function prueba() {
      if (i >= EXT.length) { grab[clave] = null; return cb(null); }
      var a = new Audio(), url = AUDIO + clave + "." + EXT[i++];
      a.preload = "metadata";
      a.addEventListener("loadedmetadata", function () { grab[clave] = url; cb(url); }, { once: true });
      a.addEventListener("error", prueba, { once: true });
      a.src = url;
    })();
  }
  function sonidos(raiz) {
    cada("[data-sonido]", function (b) {
      cargar(b.getAttribute("data-sonido"), function (url) {
        if (!url) return;
        b.hidden = false;
        b.addEventListener("click", function () { callar(); new Audio(url).play(); });
        cada(".nota-audio[data-nota]", function (n) {
          var todas = n.getAttribute("data-nota").split(/\s+/).every(function (k) { return grab[k]; });
          if (todas) n.hidden = true;
        });
      });
    }, raiz);
  }
  window.lengSonidos = sonidos;

  /* ================= Abecedario que suena =================
     <div class="abc" data-abc='[{"M":"A","m":"a","p":"árbol","e":"🌳","n":"a","v":"a"},…]'></div>
     n = nombre escrito; v = cómo debe decirlo la voz (si difiere) */
  function abecedario(caja) {
    var L = JSON.parse(caja.getAttribute("data-abc"));
    caja.innerHTML = L.map(function (x, i) {
      return '<button type="button" class="abc-letra" data-i="' + i + '" aria-label="' + esc(x.M + ", " + x.n + ". " + x.p) + '">' +
        '<span class="abc-par"><span class="abc-M">' + x.M + '</span><span class="abc-m">' + x.m + '</span></span>' +
        '<span class="abc-e" aria-hidden="true">' + x.e + '</span><span class="abc-p">' + x.p + '</span><span class="abc-n">«' + x.n + '»</span></button>';
    }).join("");
    function di(i, fin) {
      cada(".abc-letra", function (b) { b.classList.toggle("sonando", +b.getAttribute("data-i") === i); }, caja);
      var x = L[i];
      hablar((x.v || x.n) + ". " + x.p + ".", 0.8, fin);
    }
    caja.addEventListener("click", function (ev) { var b = ev.target.closest(".abc-letra"); if (b) di(+b.getAttribute("data-i")); });
    var todo = $(caja.id + "-todo"), parar = $(caja.id + "-parar"), sigue = false;
    if (todo) todo.addEventListener("click", function () {
      sigue = true; var i = 0;
      (function paso() { if (!sigue || i >= L.length) { sigue = false; cada(".abc-letra", function (b) { b.classList.remove("sonando"); }, caja); return; } di(i++, function () { setTimeout(paso, 250); }); })();
    });
    if (parar) parar.addEventListener("click", function () { sigue = false; callar(); });
  }

  /* ================= Emparejar mayúscula y minúscula =================
     <div class="emparejar" id="emp" data-letras="ABCDE…" data-n="6"></div> */
  function emparejar(caja) {
    var todas = caja.getAttribute("data-letras").split(""), n = +caja.getAttribute("data-n") || 6;
    var est = caja.querySelector(".emp-estado"), sel = null, hechas = 0, tanda, errores = {};
    function pinta() {
      tanda = baraja(todas).slice(0, n); hechas = 0; sel = null; errores = {};
      var izq = tanda.map(function (l) { return '<button type="button" class="emp-b emp-M" data-l="' + l + '">' + l + '</button>'; }).join("");
      var der = baraja(tanda).map(function (l) { return '<button type="button" class="emp-b emp-m" data-l="' + l + '">' + l.toLowerCase() + '</button>'; }).join("");
      caja.querySelector(".emp-cols").innerHTML = '<div class="emp-col" role="group" aria-label="Mayúsculas"><p class="emp-tit">Mayúsculas</p>' + izq +
        '</div><div class="emp-col" role="group" aria-label="Minúsculas"><p class="emp-tit">Minúsculas</p>' + der + '</div>';
      est.className = "fb emp-estado"; est.textContent = "Toque una mayúscula y después su minúscula. Parejas: 0 de " + n + ".";
    }
    caja.addEventListener("click", function (ev) {
      var b = ev.target.closest(".emp-b"); if (!b || b.disabled) return;
      if (b.classList.contains("emp-M")) { cada(".emp-M", function (x) { x.classList.remove("elegida"); x.setAttribute("aria-pressed", "false"); }, caja); b.classList.add("elegida"); b.setAttribute("aria-pressed", "true"); sel = b; return; }
      if (!sel) { est.className = "fb emp-estado pista"; est.textContent = "Primero toque una mayúscula, en la columna de la izquierda."; return; }
      var L = sel.getAttribute("data-l");
      if (b.getAttribute("data-l") === L) {
        sel.disabled = b.disabled = true; sel.classList.remove("elegida"); sel.classList.add("correcta"); b.classList.add("correcta"); hechas++; sel = null;
        est.className = "fb emp-estado bien";
        est.textContent = hechas === n ? "✓ Las " + n + " parejas están completas. " + elogio() + " Pulse «Otra tanda de letras» para seguir." : "✓ " + L + " y " + L.toLowerCase() + " van juntas. Parejas: " + hechas + " de " + n + ".";
      } else {
        errores[L] = (errores[L] || 0) + 1;
        est.className = "fb emp-estado pista";
        est.textContent = errores[L] === 1 ? "Todavía no: «" + b.textContent + "» no es la minúscula de " + L + ". Fíjese en la forma de la letra e intente otra vez."
          : "La minúscula de " + L + " es «" + L.toLowerCase() + "». Búsquela en la columna de la derecha.";
      }
    });
    caja.querySelector(".emp-otra").addEventListener("click", pinta);
    pinta();
  }

  /* ================= Arma una oración (sujeto + predicado) =================
     <div class="armar" data-suj='["El gato negro",…]' data-pred='["duerme en el sofá.",…]' data-ok='{"0":[0],…}' data-plural='[2]'></div>
     data-ok: para cada sujeto, los predicados que concuerdan. */
  function armar(caja) {
    var S = JSON.parse(caja.getAttribute("data-suj")), P = JSON.parse(caja.getAttribute("data-pred")), OK = JSON.parse(caja.getAttribute("data-ok"));
    var s = null, p = null, intentos = 0, hechas = [];
    var fs = caja.querySelector(".armar-suj"), fp = caja.querySelector(".armar-pred"), out = caja.querySelector(".armar-frase"), fb = caja.querySelector(".fb"), lista = caja.querySelector(".armar-lista");
    fs.innerHTML = S.map(function (x, i) { return '<button type="button" class="opcion armar-b" data-s="' + i + '" aria-pressed="false">' + x + '</button>'; }).join("");
    fp.innerHTML = P.map(function (x, i) { return '<button type="button" class="opcion armar-b" data-p="' + i + '" aria-pressed="false">' + x + '</button>'; }).join("");
    function muestra() {
      out.innerHTML = (s === null ? '<span class="hueco">sujeto</span>' : '<span class="suj">' + S[s] + '</span>') + " " + (p === null ? '<span class="hueco">predicado</span>' : '<span class="pred">' + P[p] + '</span>');
    }
    caja.addEventListener("click", function (ev) {
      var b = ev.target.closest(".armar-b"); if (!b) return;
      var grupo = b.hasAttribute("data-s") ? fs : fp;
      cada(".armar-b", function (x) { x.classList.remove("elegida"); x.setAttribute("aria-pressed", "false"); }, grupo);
      b.classList.add("elegida"); b.setAttribute("aria-pressed", "true");
      if (b.hasAttribute("data-s")) s = +b.getAttribute("data-s"); else p = +b.getAttribute("data-p");
      fb.className = "fb"; fb.innerHTML = ""; muestra();
    });
    caja.querySelector(".armar-comprobar").addEventListener("click", function () {
      if (s === null || p === null) { fb.className = "fb pista"; fb.innerHTML = "Elija un sujeto y un predicado."; return; }
      var bien = OK[s].indexOf(p) >= 0, txt = S[s] + " " + P[p];
      if (bien) {
        intentos = 0; fb.className = "fb bien";
        fb.innerHTML = "✓ <strong>" + txt + "</strong> es una oración completa: dice quién (" + S[s].toLowerCase() + ") y qué hace. Léala en voz alta. " + elogio();
        if (hechas.indexOf(txt) < 0) { hechas.push(txt); lista.innerHTML = hechas.map(function (h) { return "<li>" + h + "</li>"; }).join(""); }
        hablar(txt, 0.85);
      } else {
        intentos++;
        fb.className = intentos === 1 ? "fb pista" : "fb mal";
        fb.innerHTML = intentos === 1 ? "<strong>Todavía no.</strong> Léala en voz alta: «" + txt.replace(/\.$/, "") + "». ¿Suena bien? Fíjese si el sujeto es <em>uno</em> o <em>varios</em> y si el verbo dice lo mismo. Pruebe con otro predicado."
          : "<strong>Así se arregla.</strong> «" + S[s] + "» va con " + OK[s].map(function (k) { return "«" + P[k] + "»"; }).join(" o ") + ": el verbo tiene que concordar con el sujeto (uno → <em>duerme</em>; varios → <em>juegan</em>). En el Tema 3 verá esto a fondo.";
        if (intentos > 1) intentos = 0;
      }
    });
    caja.querySelector(".armar-limpiar").addEventListener("click", function () { s = p = null; cada(".armar-b", function (x) { x.classList.remove("elegida"); x.setAttribute("aria-pressed", "false"); }, caja); fb.className = "fb"; fb.innerHTML = ""; muestra(); });
    muestra();
  }

  /* ================= Guía de lectura: cada palabra se ilumina por turno =================
     <div class="guia" id="g1"><p class="guia-texto">…</p> + botones #g1-empezar, #g1-oir, select #g1-vel */
  function guia(caja) {
    var p = caja.querySelector(".guia-texto"), texto = p.textContent.replace(/\s+/g, " ").trim(), id = caja.id;
    var lineas = Array.prototype.map.call(p.querySelectorAll(".guia-linea"), function (l) { return l.textContent.trim(); });
    if (!lineas.length) lineas = [texto];
    p.innerHTML = lineas.map(function (l) { return '<span class="guia-linea">' + l.split(" ").map(function (w) { return '<span class="guia-p">' + w + '</span>'; }).join(" ") + "</span>"; }).join("");
    var ps = p.querySelectorAll(".guia-p"), t = null, k = 0, bE = $(id + "-empezar");
    function para() { clearInterval(t); t = null; cada(".guia-p", function (x) { x.classList.remove("ahora"); }, p); bE.textContent = "▶ Empezar la guía"; }
    bE.addEventListener("click", function () {
      if (t) return para();
      k = 0; bE.textContent = "⏸ Detener la guía";
      var ms = +($(id + "-vel").value || 700);
      t = setInterval(function () {
        if (k > 0) ps[k - 1].classList.remove("ahora");
        if (k >= ps.length) return para();
        ps[k].classList.add("ahora"); k++;
      }, ms);
    });
    var oir = $(id + "-oir"); if (oir) oir.addEventListener("click", function () { hablar(texto, 0.8); });
  }

  /* ================= Cronómetro de lectura (palabras por minuto) ================= */
  function crono(caja) {
    var id = caja.id, texto = $(caja.getAttribute("data-texto")).textContent.replace(/\s+/g, " ").trim();
    var palabras = texto.split(" ").filter(function (w) { return /[a-záéíóúñü0-9]/i.test(w); }).length;
    var inicio = 0, reloj = null, n = 0, el = $(id + "-tiempo"), res = $(id + "-res"), bE = $(id + "-empezar"), bT = $(id + "-terminar"), tb = caja.querySelector("tbody");
    function fmt(s) { return Math.floor(s / 60) + ":" + ("0" + Math.floor(s % 60)).slice(-2); }
    bE.addEventListener("click", function () {
      callar(); inicio = Date.now(); el.textContent = "0:00"; res.textContent = "Lea en voz alta. Pulse «Terminar» al llegar al final.";
      bE.disabled = true; bT.disabled = false; bT.focus();
      reloj = setInterval(function () { el.textContent = fmt((Date.now() - inicio) / 1000); }, 250);
    });
    bT.addEventListener("click", function () {
      clearInterval(reloj); var s = (Date.now() - inicio) / 1000; bE.disabled = false; bT.disabled = true;
      if (s < 15) { res.textContent = "Fueron solo " + Math.round(s) + " segundos: parece que no leyó el texto completo. Inténtelo otra vez."; return; }
      n++; var ppm = Math.round(palabras / s * 60);
      if (n === 1) tb.innerHTML = "";
      var tr = document.createElement("tr"); tr.innerHTML = '<th scope="row">' + n + "</th><td>" + fmt(s) + "</td><td>" + ppm + "</td>"; tb.appendChild(tr);
      res.textContent = "Pasada " + n + ": " + fmt(s) + ", unas " + ppm + " palabras por minuto (" + palabras + " palabras). " + (n < 3 ? "Prepárese para la siguiente pasada." : "Completó las tres pasadas. Compare sus resultados.");
      bE.textContent = n < 3 ? "Empezar la pasada " + (n + 1) : "Empezar otra pasada";
    });
  }

  /* ================= Teatro leído: la computadora lee un papel y el alumno el otro =================
     <div class="teatro" id="t1" data-lineas='[{"q":"S","t":"…"},…]' data-yo="M" data-nombres='{"S":"Secretaria (la computadora)","M":"Marta (usted)"}'> */
  function teatro(caja) {
    var L = JSON.parse(caja.getAttribute("data-lineas")), yo = caja.getAttribute("data-yo"), N = JSON.parse(caja.getAttribute("data-nombres")), id = caja.id;
    var cont = caja.querySelector(".teatro-lineas"), est = $(id + "-estado"), bS = $(id + "-sigue"), bE = $(id + "-empezar"), i = -1, gen = 0;
    cont.innerHTML = L.map(function (l, k) { return '<p class="linea' + (l.q === yo ? " tu" : "") + '" id="' + id + "-l" + k + '"><span class="quien">' + N[l.q] + "</span>—" + l.t + "</p>"; }).join("");
    function marca() { cada(".linea", function (d, k) { d.classList.toggle("actual", k === i); }, cont); }
    function paso() {
      i++; marca(); var mio = ++gen;
      if (i >= L.length) { est.textContent = "Terminó el diálogo. Repítalo e intente mejorar la entonación."; bS.disabled = true; bE.disabled = false; bE.textContent = "Repetir"; i = -1; marca(); return; }
      if (L[i].q !== yo) {
        bS.disabled = true; est.textContent = "Escuche…";
        hablar(L[i].t, 0.9, function () { if (mio === gen) paso(); });
        setTimeout(function () { if (mio === gen && L[i] && L[i].q !== yo) { bS.disabled = false; est.textContent = "Cuando termine la computadora, pulse «Ya leí mi parte» para seguir."; } }, 9000);
      } else { bS.disabled = false; bS.focus(); est.textContent = "Le toca: lea su línea en voz alta."; }
    }
    bE.addEventListener("click", function () { bE.disabled = true; i = -1; paso(); });
    bS.addEventListener("click", function () { callar(); paso(); });
    $(id + "-reiniciar").addEventListener("click", function () { gen++; callar(); i = -1; marca(); bS.disabled = true; bE.disabled = false; bE.textContent = "Empezar"; est.textContent = ""; });
  }

  /* ================= Dónde empieza cada oración (práctica, dos intentos) =================
     creaLimites(pre, banco): banco = [{titulo, correcto: "Oración uno. Oración dos."}]
     El alumno toca la primera palabra de cada oración; la página pone la mayúscula y el punto. */
  window.creaLimites = function (pre, banco) {
    var pila = [], est = { primero: 0, pista: 0, total: 0 }, it, pals, inicios, intentos, cerrado;
    var enun = $(pre + "-enun"), fb = $(pre + "-fb");
    function saca() { if (!pila.length) pila = baraja(banco); return pila.pop(); }
    function marcador() { $(pre + "-marcador").textContent = est.total ? "Resueltos: " + (est.primero + est.pista) + " de " + est.total + " (" + est.primero + " al primer intento)" : ""; }
    function nuevo() {
      it = saca(); intentos = 0; cerrado = false; pals = []; inicios = {};
      it.correcto.split(/(?<=\.)\s+/).forEach(function (o, k) {
        o.replace(/\.$/, "").split(" ").forEach(function (w, j) { if (j === 0) inicios[pals.length] = 1; pals.push(w); });
      });
      enun.innerHTML = '<p class="lim-tit">' + it.titulo + '</p><p class="lim-texto" role="group" aria-label="Párrafo sin puntos ni mayúsculas. Toque la primera palabra de cada oración.">' +
        pals.map(function (w, i) {
          var base = i === 0 ? w : w.charAt(0).toLowerCase() + w.slice(1);
          if (/^[A-ZÁÉÍÓÚÑ]/.test(w) && !inicios[i]) base = w;   /* nombres propios */
          if (i === 0) return '<span class="lim-p lim-fija">' + w + "</span>";
          return '<button type="button" class="lim-p" data-i="' + i + '" aria-pressed="false" data-w="' + esc(w) + '" data-b="' + esc(base) + '">' + base + "</button>";
        }).join(" ") + '<span class="lim-fin">.</span></p>';
      fb.className = "fb"; fb.innerHTML = ""; $(pre + "-comprobar").disabled = false;
    }
    enun.addEventListener("click", function (ev) {
      var b = ev.target.closest("button.lim-p"); if (!b || cerrado) return;
      var on = b.getAttribute("aria-pressed") !== "true";
      b.setAttribute("aria-pressed", on ? "true" : "false"); b.classList.toggle("marcada", on); b.classList.remove("revisar");
      var w = b.getAttribute("data-w"); b.textContent = on ? w.charAt(0).toUpperCase() + w.slice(1) : b.getAttribute("data-b");
    });
    function comprueba() {
      if (cerrado) return;
      var malos = 0, faltan = 0, sobran = 0;
      cada("button.lim-p", function (b) {
        var i = +b.getAttribute("data-i"), m = b.getAttribute("aria-pressed") === "true", debe = !!inicios[i];
        b.classList.toggle("revisar", m && !debe); if (m !== debe) { malos++; if (debe) faltan++; else sobran++; }
      }, enun);
      intentos++;
      var n = Object.keys(inicios).length;
      if (!malos) {
        cerrado = true; est.total++; if (intentos === 1) est.primero++; else est.pista++;
        fb.className = "fb bien"; fb.innerHTML = "✓ Correcto: el párrafo tiene " + n + " oraciones, cada una con mayúscula al inicio y punto al final. " + elogio();
        $(pre + "-comprobar").disabled = true; hablar(it.correcto, 0.85);
      } else if (intentos === 1) {
        fb.className = "fb pista";
        fb.innerHTML = "<strong>Todavía no.</strong> El párrafo tiene " + n + " oraciones. " + (faltan ? "Falta marcar " + (faltan === 1 ? "1 inicio" : faltan + " inicios") + ". " : "") + (sobran ? "Hay " + (sobran === 1 ? "1 palabra marcada" : sobran + " palabras marcadas") + " que no empiezan oración. " : "") +
          (sobran ? "Las marcas en amarillo no van. " : "") + "Lea en voz alta y pregúntese en cada parada: ¿ya dije quién y qué hace? <strong>Inténtelo de nuevo.</strong>";
      } else {
        cerrado = true; est.total++;
        cada("button.lim-p", function (b) { var i = +b.getAttribute("data-i"), d = !!inicios[i]; b.setAttribute("aria-pressed", d ? "true" : "false"); b.classList.toggle("marcada", d); b.classList.remove("revisar"); var w = b.getAttribute("data-w"); b.textContent = d ? w : b.getAttribute("data-b"); }, enun);
        fb.className = "fb mal"; fb.innerHTML = "<strong>Así queda.</strong> " + it.correcto + " Pulse <em>Otro ejercicio</em> para intentar uno más.";
        $(pre + "-comprobar").disabled = true;
      }
      marcador();
    }
    $(pre + "-comprobar").addEventListener("click", comprueba);
    $(pre + "-nuevo").addEventListener("click", nuevo);
    nuevo(); marcador();
  };

  /* ================= Arranque ================= */
  function inicia() {
    botonesVoz(); sonidos();
    cada(".abc[data-abc]", abecedario);
    cada(".emparejar[data-letras]", emparejar);
    cada(".armar[data-suj]", armar);
    cada(".guia", guia);
    cada(".crono[data-texto]", crono);
    cada(".teatro[data-lineas]", teatro);
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", inicia); else inicia();
})();
