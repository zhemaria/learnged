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


  /* ================= Constructor: tocar fichas en orden para formar una palabra o una frase =================
     <div class="constructor" data-grupos='[["ca","sa",…]]' data-sep="" data-max="2" data-reales='["casa",…]' data-titulos='["Sílabas"]'>
     sep "" → sílabas que forman una palabra; sep " " → palabras que forman una frase (mayúscula y punto). */
  function constructor(caja) {
    var G = JSON.parse(caja.getAttribute("data-grupos")), T = JSON.parse(caja.getAttribute("data-titulos") || "[]");
    var sep = caja.getAttribute("data-sep") || "", max = +caja.getAttribute("data-max") || 99;
    var reales = caja.getAttribute("data-reales") ? JSON.parse(caja.getAttribute("data-reales")) : null;
    var elegidas = [], halladas = [];
    var fichas = caja.querySelector(".cons-fichas"), out = caja.querySelector(".cons-frase"), fb = caja.querySelector(".fb"), lista = caja.querySelector(".cons-lista");
    fichas.innerHTML = G.map(function (g, k) {
      return (T[k] ? '<p class="cons-tit">' + T[k] + "</p>" : "") + '<div class="cons-grupo" role="group"' + (T[k] ? ' aria-label="' + esc(T[k]) + '"' : "") + ">" +
        g.map(function (x) { return '<button type="button" class="opcion cons-b" data-f="' + esc(x) + '">' + x + "</button>"; }).join("") + "</div>";
    }).join("");
    function texto() {
      var t = elegidas.join(sep);
      if (sep === " " && t) { t = t.charAt(0).toUpperCase() + t.slice(1); if (!/[.!?]$/.test(t)) t += "."; }
      return t;
    }
    function muestra() { out.textContent = elegidas.length ? texto() : (sep ? "Toque las palabras en orden." : "Toque dos sílabas en orden."); }
    caja.addEventListener("click", function (ev) {
      var b = ev.target.closest(".cons-b"); if (!b) return;
      if (elegidas.length >= max) { fb.className = "fb pista"; fb.innerHTML = "Ya tiene " + max + (sep ? " palabras" : " sílabas") + ". Pulse «Leer» o «Limpiar»."; return; }
      elegidas.push(b.getAttribute("data-f")); fb.className = "fb"; fb.innerHTML = ""; muestra();
    });
    caja.querySelector(".cons-leer").addEventListener("click", function () {
      if (!elegidas.length) return;
      var t = texto(); hablar(t, 0.8);
      if (!reales) { fb.className = "fb bien"; fb.innerHTML = "Lea su frase en voz alta: <strong>" + esc(t) + "</strong>"; return; }
      var w = t.toLowerCase(), k = reales.map(function (r) { return r.replace(/[áéíóú]/g, function (c) { return "aeiou"["áéíóú".indexOf(c)]; }); }).indexOf(w);
      if (k >= 0) {
        fb.className = "fb bien"; fb.innerHTML = "✓ <strong>" + reales[k] + "</strong> es una palabra de verdad. " + elogio();
        if (halladas.indexOf(reales[k]) < 0) { halladas.push(reales[k]); lista.innerHTML = halladas.map(function (h) { return "<li>" + h + "</li>"; }).join(""); }
      } else { fb.className = "fb pista"; fb.innerHTML = "«" + esc(t) + "» se puede leer, pero no es una palabra del español. Pruebe otra combinación."; }
    });
    caja.querySelector(".cons-limpiar").addEventListener("click", function () { elegidas = []; fb.className = "fb"; fb.innerHTML = ""; muestra(); });
    muestra();
  }

  /* ================= Palabras al instante: una palabra cada pocos segundos =================
     <div class="destello" id="d1" data-grupos='[{"n":"Grupo 1","p":["el","la",…]}]'> */
  function destello(caja) {
    var G = JSON.parse(caja.getAttribute("data-grupos")), id = caja.id, sel = $(id + "-grupo"), vel = $(id + "-vel"), tarj = $(id + "-palabra"), est = $(id + "-estado");
    var bP = $(id + "-pasar"), bS = $(id + "-pausa"), lista = $(id + "-todas"), reloj = null, i = 0;
    sel.innerHTML = G.map(function (g, k) { return '<option value="' + k + '">' + g.n + "</option>"; }).join("");
    function grupo() { return G[+sel.value].p; }
    function todas() { lista.innerHTML = grupo().map(function (w) { return '<button type="button" class="btn-voz mini" data-hablar="' + esc(w) + '">' + w + "</button>"; }).join(""); }
    function pinta() { var g = grupo(); tarj.textContent = g[i]; est.textContent = "Palabra " + (i + 1) + " de " + g.length + ". Léala en voz alta."; }
    function para() { clearInterval(reloj); reloj = null; bP.disabled = false; bS.disabled = true; }
    bP.addEventListener("click", function () {
      i = 0; pinta(); bP.disabled = true; bS.disabled = false;
      reloj = setInterval(function () { i++; if (i >= grupo().length) { para(); i = 0; est.textContent = "Terminó el grupo. Repítalo hasta leer cada palabra sin dudar."; return; } pinta(); }, +vel.value);
    });
    bS.addEventListener("click", para);
    sel.addEventListener("change", function () { para(); i = 0; tarj.textContent = grupo()[0]; est.textContent = ""; todas(); });
    tarj.textContent = grupo()[0]; todas();
  }


  /* ================= Lectura en voz alta de la página =================
     Un botón fijo («🔊 Leer en voz alta») pone un altavoz junto a cada párrafo, título, pregunta y
     lista, y un botón «Escuchar las opciones» debajo de cada grupo de opciones. Pensado para quien
     todavía no lee con soltura. Encendido de entrada en el Nivel 1; la elección se recuerda. */
  var L11 = /\/nivel-1\/(leccion|practica)-1-1\.html/.test(location.pathname);
  var CLAVE_VOZ = L11 ? "learnged-voz-1-1" : "learnged-voz", vozOn = false, obs = null;
  var SEL_TXT = ".envoltura h2, .envoltura h3, .envoltura p, .envoltura li, .envoltura dt, .envoltura dd," +
    " .contenedor h1, .contenedor h2, .contenedor h3, .contenedor p, .contenedor li, main h1, main h2, main h3, main p, main li, .enun, .pregunta, .pregunta-int, .etiqueta";
  var EXCLUYE = "nav, footer, .indice, .opciones, button, .abc, .emparejar, .cons-fichas, .cons-frase, .armar-suj, .armar-pred, .armar-frase, .lim-texto, .guia, .destello, .crono, .teatro, .leer-ops, .fb, .marcador, .respuesta-int, .estandares, .chips, .migas, .aviso-voz, .nota-audio, .tabla-rubrica, label, select";
  function guardar(k, v) { try { localStorage.setItem(k, v); } catch (e) {} }
  function leer(k) { try { return localStorage.getItem(k); } catch (e) { return null; } }
  function limpio(el) {
    var c = el.cloneNode(true);
    Array.prototype.forEach.call(c.querySelectorAll(".leer-btn, .leer-ops, button, .cap-oculto, [aria-hidden='true']"), function (x) { x.remove(); });
    return c.textContent.replace(/[\u{1F300}-\u{1FAFF}☀-➿️]/gu, "").replace(/\s+/g, " ").trim();
  }
  function marcaLeyendo(el) {
    cada(".leyendo", function (x) { x.classList.remove("leyendo"); });
    el.classList.add("leyendo");
    hablar(limpio(el), 0.85, function () { el.classList.remove("leyendo"); });
  }
  function decora(raiz) {
    if (!vozOn) return;
    cada(SEL_TXT, function (el) {
      if (el.dataset.leer || el.closest(EXCLUYE) || el.querySelector("p, li, ul, ol, table, div") && !el.matches(".enun, .pregunta, .pregunta-int")) return;
      if (el.matches("li") && el.querySelector(".leer-btn")) return;
      if (el.parentElement && el.parentElement.closest("[data-leer]") && !el.matches(".pregunta, .pregunta-int")) return;
      var txt = limpio(el); if (txt.length < 2) return;
      el.dataset.leer = "1";
      var b = document.createElement("button"); b.type = "button"; b.className = "leer-btn"; b.setAttribute("aria-label", "Leer en voz alta: " + txt.slice(0, 60));
      b.innerHTML = '<span aria-hidden="true">🔊</span>';
      b.addEventListener("click", function (ev) { ev.preventDefault(); ev.stopPropagation(); marcaLeyendo(el); });
      el.insertBefore(b, el.firstChild);
    }, raiz);
    cada(".envoltura tbody tr, .contenedor tbody tr, main tbody tr", function (tr) {
      if (tr.dataset.leer || tr.closest(EXCLUYE) || !tr.firstElementChild) return;
      var txt = limpio(tr); if (txt.length < 2) return;
      tr.dataset.leer = "1";
      var b = document.createElement("button"); b.type = "button"; b.className = "leer-btn"; b.setAttribute("aria-label", "Leer la fila: " + txt.slice(0, 60));
      b.innerHTML = '<span aria-hidden="true">🔊</span>';
      b.addEventListener("click", function (ev) { ev.preventDefault(); ev.stopPropagation(); marcaLeyendo(tr); });
      tr.firstElementChild.insertBefore(b, tr.firstElementChild.firstChild);
    }, raiz);
    cada(".opciones", function (g) {
      var sig = g.nextElementSibling;
      if (sig && sig.classList.contains("leer-ops")) return;
      var b = document.createElement("button"); b.type = "button"; b.className = "leer-ops";
      b.innerHTML = '<span aria-hidden="true">🔊</span> Escuchar las opciones';
      b.addEventListener("click", function () {
        var ops = Array.prototype.map.call(g.querySelectorAll(".opcion"), function (o) { return limpio(o) || (o.querySelector("[aria-label]") ? o.querySelector("[aria-label]").getAttribute("aria-label") : ""); });
        var ord = ["Primera", "Segunda", "Tercera", "Cuarta", "Quinta"];
        hablar(ops.map(function (t, i) { return (ord[i] || "Otra") + " opción: " + t + "."; }).join(" "), 0.85);
      });
      g.parentNode.insertBefore(b, g.nextSibling);
    }, raiz);
    decoraMenus(raiz);
  }
  function decoraMenus(raiz) {
    if (!vozOn) return;
    cada(".frase-huecos", function (f) {
      var sig = f.nextElementSibling;
      if (sig && sig.classList.contains("leer-ops")) return;
      var b = document.createElement("button"); b.type = "button"; b.className = "leer-ops";
      b.innerHTML = '<span aria-hidden="true">🔊</span> Escuchar la oración y las opciones';
      b.addEventListener("click", function () {
        var c = f.cloneNode(true), ops = [];
        Array.prototype.forEach.call(c.querySelectorAll("select"), function (sel, i) {
          ops.push(Array.prototype.slice.call(sel.options, 1).map(function (o) { return o.textContent; }).join(", o "));
          sel.replaceWith(document.createTextNode(" espacio en blanco "));
        });
        Array.prototype.forEach.call(c.querySelectorAll("label"), function (l) { l.remove(); });
        hablar(c.textContent.replace(/\s+/g, " ").trim() + ". Opciones: " + ops.join(". En el siguiente espacio: ") + ".", 0.85);
      });
      f.parentNode.insertBefore(b, f.nextSibling);
    }, raiz);
  }
  function quita() {
    cada(".leer-btn, .leer-ops", function (b) { b.remove(); });
    cada("[data-leer]", function (el) { delete el.dataset.leer; });
    cada(".leyendo", function (x) { x.classList.remove("leyendo"); });
  }
  function botonVozPagina() {
    if (!ES) return;
    var guardado = leer(CLAVE_VOZ);
    vozOn = guardado === null ? L11 : guardado === "1";
    var b = document.createElement("button"); b.type = "button"; b.className = "voz-pagina";
    function pinta() { b.setAttribute("aria-pressed", vozOn ? "true" : "false"); b.innerHTML = '<span aria-hidden="true">🔊</span> Voz: ' + (vozOn ? "sí" : "no"); b.setAttribute("aria-label", vozOn ? "Lectura en voz alta activada. Pulse para desactivarla." : "Activar la lectura en voz alta de la página"); b.title = vozOn ? "Quitar los botones de lectura en voz alta" : "Poner un botón 🔊 junto a cada texto para oírlo"; }
    b.addEventListener("click", function () { vozOn = !vozOn; guardar(CLAVE_VOZ, vozOn ? "1" : "0"); pinta(); if (vozOn) decora(); else { quita(); callar(); } });
    pinta();
    var barra = document.querySelector(".lg-bar") || document.querySelector("header.top .tools");
    if (barra) { b.classList.add("en-barra"); barra.appendChild(b); } else document.body.appendChild(b);
    if (vozOn) decora();
    obs = new MutationObserver(function (m) {
      if (!vozOn) return;
      obs.disconnect(); decora(); obs.observe(document.body, { childList: true, subtree: true });
    });
    obs.observe(document.body, { childList: true, subtree: true });
  }


  /* ================= Tocar en un texto las palabras que se piden (dos intentos) =================
     creaMarcar(pre, banco): banco = [{consigna, texto: "Mi *familia* es pequeña.", mayus: false, exp}]
     Las palabras con * son las que hay que tocar. Con mayus: true el texto se muestra en minúsculas
     y al tocar una palabra se le pone la mayúscula. */
  window.creaMarcar = function (pre, banco) {
    var pila = [], est = { primero: 0, pista: 0, total: 0 }, it, intentos, cerrado;
    var enun = $(pre + "-enun"), fb = $(pre + "-fb");
    function saca() { if (!pila.length) pila = baraja(banco); return pila.pop(); }
    function marcador() { $(pre + "-marcador").textContent = est.total ? "Resueltos: " + (est.primero + est.pista) + " de " + est.total + " (" + est.primero + " al primer intento)" : ""; }
    function partes(tok) { var m = tok.match(/^([«¿¡"(]*)(.*?)([.,;:!?»")]*)$/); return [m[1], m[2], m[3]]; }
    function nuevo() {
      it = saca(); intentos = 0; cerrado = false;
      var html = it.texto.split(/\s+/).map(function (tok, i) {
        var obj = tok.indexOf("*") >= 0; tok = tok.replace(/\*/g, "");
        var p = partes(tok), w = p[1], vis = it.mayus ? w.toLowerCase() : w;
        return p[0] + '<button type="button" class="lim-p" data-ok="' + (obj ? 1 : 0) + '" data-w="' + esc(w) + '" data-b="' + esc(vis) + '" aria-pressed="false">' + vis + "</button>" + p[2];
      }).join(" ");
      enun.innerHTML = '<p class="lim-tit">' + it.consigna + '</p><p class="lim-texto marcar" role="group">' + html + "</p>";
      fb.className = "fb"; fb.innerHTML = ""; $(pre + "-comprobar").disabled = false;
    }
    enun.addEventListener("click", function (ev) {
      var b = ev.target.closest("button.lim-p"); if (!b || cerrado) return;
      var on = b.getAttribute("aria-pressed") !== "true";
      b.setAttribute("aria-pressed", on ? "true" : "false"); b.classList.toggle("marcada", on); b.classList.remove("revisar");
      if (it.mayus) { var w = b.getAttribute("data-b"); b.textContent = on ? w.charAt(0).toUpperCase() + w.slice(1) : w; }
    });
    function comprueba() {
      if (cerrado) return;
      var faltan = 0, sobran = 0, n = 0;
      cada("button.lim-p", function (b) {
        var m = b.getAttribute("aria-pressed") === "true", d = b.getAttribute("data-ok") === "1"; if (d) n++;
        b.classList.toggle("revisar", m && !d); if (d && !m) faltan++; if (m && !d) sobran++;
      }, enun);
      intentos++;
      if (!faltan && !sobran) {
        cerrado = true; est.total++; if (intentos === 1) est.primero++; else est.pista++;
        fb.className = "fb bien"; fb.innerHTML = "✓ Correcto. " + (it.exp || "") + " " + elogio(); $(pre + "-comprobar").disabled = true;
      } else if (intentos === 1) {
        fb.className = "fb pista";
        fb.innerHTML = "<strong>Todavía no.</strong> Hay que marcar " + n + (n === 1 ? " palabra" : " palabras") + ". " + (faltan ? "Le " + (faltan === 1 ? "falta 1" : "faltan " + faltan) + ". " : "") +
          (sobran ? "Las marcas en amarillo no van. " : "") + (it.pista || "") + " <strong>Inténtelo de nuevo.</strong>";
      } else {
        cerrado = true; est.total++;
        cada("button.lim-p", function (b) {
          var d = b.getAttribute("data-ok") === "1"; b.setAttribute("aria-pressed", d ? "true" : "false"); b.classList.toggle("marcada", d); b.classList.remove("revisar");
          if (it.mayus) { var w = b.getAttribute("data-b"); b.textContent = d ? w.charAt(0).toUpperCase() + w.slice(1) : w; }
        }, enun);
        fb.className = "fb mal"; fb.innerHTML = "<strong>Así queda.</strong> " + (it.exp || "") + " Pulse <em>Otro ejercicio</em> para intentar uno más.";
        $(pre + "-comprobar").disabled = true;
      }
      marcador();
    }
    $(pre + "-comprobar").addEventListener("click", comprueba);
    $(pre + "-nuevo").addEventListener("click", nuevo);
    nuevo(); marcador();
  };


  /* creaCortes(pre, banco): banco = [{pal: "ca-mión", exp}]. Se tocan los huecos entre letras para poner o quitar un corte.
     Dos intentos: en el primero se marcan en naranja los cortes que faltan y en rosado los que sobran. */
  window.creaCortes = function (pre, banco) {
    var pila = [], est = { primero: 0, pista: 0, total: 0 }, it, intentos, cerrado, letras, ok;
    var enun = $(pre + "-enun"), fb = $(pre + "-fb");
    function saca() { if (!pila.length) pila = baraja(banco); return pila.pop(); }
    function marcador() { $(pre + "-marcador").textContent = est.total ? "Resueltos: " + (est.primero + est.pista) + " de " + est.total + " (" + est.primero + " al primer intento)" : ""; }
    function nuevo() {
      it = saca(); intentos = 0; cerrado = false;
      letras = it.pal.replace(/-/g, "").split(""); ok = []; var k = 0;
      it.pal.split("").forEach(function (c) { if (c === "-") ok.push(k); else k++; });
      var h = '<p class="lim-tit">Toque los espacios entre las letras para cortar <strong>' + esc(letras.join("")) + '</strong> en sílabas. <button type="button" class="leer-btn" data-hablar="' + esc(letras.join("")) + '" aria-label="Escuchar la palabra">🔊</button></p><p class="cortes" role="group" aria-label="Letras y espacios">';
      letras.forEach(function (c, i) {
        h += '<span class="ct-l">' + esc(c) + '</span>';
        if (i < letras.length - 1) h += '<button type="button" class="ct-g" data-i="' + (i + 1) + '" aria-pressed="false" aria-label="Espacio entre ' + esc(c) + ' y ' + esc(letras[i + 1]) + '"></button>';
      });
      enun.innerHTML = h + "</p>"; fb.className = "fb"; fb.innerHTML = ""; $(pre + "-comprobar").disabled = false;
    }
    enun.addEventListener("click", function (ev) {
      var b = ev.target.closest("button.ct-g"); if (!b || cerrado) return;
      var on = b.getAttribute("aria-pressed") !== "true"; b.setAttribute("aria-pressed", on ? "true" : "false"); b.classList.remove("ct-falta", "ct-sobra");
    });
    function comprueba() {
      if (cerrado) return; intentos++;
      var faltan = 0, sobran = 0;
      cada("button.ct-g", function (b) {
        var i = +b.getAttribute("data-i"), m = b.getAttribute("aria-pressed") === "true", d = ok.indexOf(i) >= 0;
        b.classList.remove("ct-falta", "ct-sobra"); if (d && !m) faltan++; if (m && !d) sobran++;
        if (intentos === 1) { if (m && !d) b.classList.add("ct-sobra"); }
      }, enun);
      var sol = it.pal;
      if (!faltan && !sobran) {
        cerrado = true; est.total++; if (intentos === 1) est.primero++; else est.pista++;
        fb.className = "fb bien"; fb.innerHTML = "✓ Correcto: <strong>" + esc(sol) + "</strong>. " + (it.exp || "") + " " + elogio(); $(pre + "-comprobar").disabled = true;
      } else if (intentos === 1) {
        fb.className = "fb pista"; fb.innerHTML = "<strong>Todavía no.</strong> " + (faltan ? "Falta" + (faltan > 1 ? "n " + faltan + " cortes" : " un corte") + ". " : "") +
          (sobran ? "Los cortes en rosado sobran. " : "") + "Recuerde: no se separan los grupos con l o r, ni ch, ll, rr; los diptongos van juntos. <strong>Inténtelo de nuevo.</strong>";
      } else {
        cerrado = true; est.total++;
        cada("button.ct-g", function (b) { var i = +b.getAttribute("data-i"), m = b.getAttribute("aria-pressed") === "true", d = ok.indexOf(i) >= 0;
          b.setAttribute("aria-pressed", d ? "true" : "false"); if (d && !m) b.classList.add("ct-falta"); }, enun);
        fb.className = "fb mal"; fb.innerHTML = "<strong>Así se separa:</strong> " + esc(sol) + ". Las líneas naranjas son los cortes que faltaban. " + (it.exp || "") + " Pulse <em>Otro ejercicio</em> para intentar uno más.";
        $(pre + "-comprobar").disabled = true;
      }
      marcador();
    }
    $(pre + "-comprobar").addEventListener("click", comprueba);
    $(pre + "-nuevo").addEventListener("click", nuevo);
    nuevo(); marcador();
  };

  /* creaDictado(pre, frases): se escucha una oración, se escribe y se revisa palabra por palabra.
     Verde: bien. Naranja: falta o sobra la tilde. Rosado: palabra distinta o de más. Dos intentos; después se muestra la oración. */
  window.creaDictado = function (pre, frases) {
    var pila = [], est = { primero: 0, pista: 0, total: 0 }, it, intentos, cerrado;
    var enun = $(pre + "-enun"), fb = $(pre + "-fb");
    function saca() { if (!pila.length) pila = baraja(frases); return pila.pop(); }
    function sinTilde(s) { return s.normalize("NFD").replace(/[̀-ͯ]/g, "").normalize("NFC"); }
    function pals(s) { return s.replace(/[¿?¡!.,;:«»"“”()—]/g, " ").split(/\s+/).filter(Boolean); }
    function marcador() { $(pre + "-marcador").textContent = est.total ? "Oraciones resueltas: " + (est.primero + est.pista) + " de " + est.total + " (" + est.primero + " al primer intento)" : ""; }
    function nuevo() {
      it = saca(); intentos = 0; cerrado = false;
      enun.innerHTML = '<p class="dc-botones"><button type="button" class="btn-sec dc-oir">🔊 Escuchar la oración</button> <button type="button" class="btn-sec dc-lento">🐢 Más despacio</button></p>' +
        '<label class="dc-etq" for="' + pre + '-texto">Escriba la oración que oyó:</label><textarea id="' + pre + '-texto" class="dc-texto" rows="2" autocomplete="off" autocapitalize="sentences" spellcheck="false"></textarea>' +
        '<div class="dc-rev" aria-live="polite"></div><p class="dc-sinvoz"><button type="button" class="enlace-btn dc-ver">¿No puede oír la voz? Pida a alguien que le dicte, o pulse aquí para ver la oración unos segundos.</button></p>';
      fb.className = "fb"; fb.innerHTML = ""; $(pre + "-comprobar").disabled = false;
      if (primeraVez) primeraVez = false; else setTimeout(function () { hablar(it, 0.8); }, 300);
    }
    var primeraVez = true;
    enun.addEventListener("click", function (ev) {
      if (ev.target.closest(".dc-oir")) hablar(it, 0.8);
      else if (ev.target.closest(".dc-lento")) hablarPalabras(it);
      else if (ev.target.closest(".dc-ver")) {
        var r = enun.querySelector(".dc-rev"); r.innerHTML = '<p class="dc-flash">' + esc(it) + "</p>";
        setTimeout(function () { if (!cerrado && r.querySelector(".dc-flash")) r.innerHTML = ""; }, 4000);
      }
    });
    function comprueba() {
      if (cerrado) return;
      var area = $(pre + "-texto"), u = area.value.trim();
      if (!u) { fb.className = "fb mal"; fb.textContent = "Primero escriba la oración que oyó."; return; }
      intentos++;
      var E = pals(it), U = pals(u), e = E.map(function (w) { return sinTilde(w.toLowerCase()); }), x = U.map(function (w) { return sinTilde(w.toLowerCase()); });
      var n = e.length, m = x.length, L = [], i, j;
      for (i = 0; i <= n; i++) L.push(new Array(m + 1).fill(0));
      for (i = n - 1; i >= 0; i--) for (j = m - 1; j >= 0; j--) L[i][j] = e[i] === x[j] ? L[i + 1][j + 1] + 1 : Math.max(L[i + 1][j], L[i][j + 1]);
      var marca = new Array(m).fill("w-mal"), usadas = 0, tildes = 0; i = 0; j = 0;
      while (i < n && j < m) {
        if (e[i] === x[j]) { var bien = E[i].toLowerCase() === U[j].toLowerCase(); marca[j] = bien ? "w-ok" : "w-tilde"; if (!bien) tildes++; usadas++; i++; j++; }
        else if (L[i + 1][j] >= L[i][j + 1]) i++; else j++;
      }
      var malas = m - usadas, faltan = n - usadas, mayus = U.length && E.length && U[0].charAt(0) !== E[0].charAt(0) && U[0].charAt(0).toLowerCase() === E[0].charAt(0).toLowerCase();
      enun.querySelector(".dc-rev").innerHTML = '<p class="dc-marcas">' + U.map(function (w, k) { return '<span class="' + marca[k] + '">' + esc(w) + "</span>"; }).join(" ") + "</p>";
      if (!tildes && !malas && !faltan && !mayus) {
        cerrado = true; est.total++; if (intentos === 1) est.primero++; else est.pista++;
        fb.className = "fb bien"; fb.innerHTML = "✓ ¡Sin errores! <strong>" + esc(it) + "</strong> " + elogio(); $(pre + "-comprobar").disabled = true;
      } else if (intentos === 1) {
        var d = [];
        if (tildes) d.push(tildes === 1 ? "una palabra tiene un problema de tilde (en naranja)" : tildes + " palabras tienen un problema de tilde (en naranja)");
        if (malas) d.push(malas === 1 ? "una palabra está mal escrita o sobra (en rosado)" : malas + " palabras están mal escritas o sobran (en rosado)");
        if (faltan > malas) d.push("falta" + (faltan - malas > 1 ? "n " + (faltan - malas) + " palabras" : " una palabra"));
        if (mayus) d.push("la oración empieza con mayúscula");
        var txt = d.join("; "); txt = txt.charAt(0).toUpperCase() + txt.slice(1);
        fb.className = "fb pista"; fb.innerHTML = "<strong>Casi.</strong> " + txt + ". Escúchela otra vez, corrija y pulse <em>Comprobar</em>.";
      } else {
        cerrado = true; est.total++;
        fb.className = "fb mal"; fb.innerHTML = "<strong>La oración es:</strong> " + esc(it) + " Compare con lo que escribió y anote en su cuaderno la regla de cada error. Pulse <em>Otro ejercicio</em> para seguir.";
        $(pre + "-comprobar").disabled = true;
      }
      marcador();
    }
    $(pre + "-comprobar").addEventListener("click", comprueba);
    $(pre + "-nuevo").addEventListener("click", nuevo);
    nuevo(); marcador();
  };

  /* Taller de escritura: <div class="taller" data-clave data-etiqueta data-guia data-oraciones data-palabras data-conectores="a|b" data-lista="x|y">
     Cuenta oraciones y palabras, muestra los conectores usados, lista de revisión, escuchar y copiar. Se guarda en el navegador. */
  function taller(t) {
    var clave = "learnged-taller-" + t.getAttribute("data-clave"), id = "tl-" + t.getAttribute("data-clave");
    var con = (t.getAttribute("data-conectores") || "").split("|").filter(Boolean), lista = (t.getAttribute("data-lista") || "").split("|").filter(Boolean);
    var mO = +t.getAttribute("data-oraciones") || 0, mP = +t.getAttribute("data-palabras") || 0;
    t.innerHTML = '<label class="tl-etq" for="' + id + '">' + esc(t.getAttribute("data-etiqueta") || "Su texto") + '</label>' +
      (t.getAttribute("data-guia") ? '<p class="tl-guia">' + esc(t.getAttribute("data-guia")) + '</p>' : '') +
      '<textarea id="' + id + '" class="tl-texto" rows="9" spellcheck="true" lang="es"></textarea>' +
      '<p class="tl-cuenta" aria-live="polite"></p><p class="tl-con"></p>' +
      '<div class="fila-btn"><button type="button" class="btn-sec tl-oir">🔊 Escuchar mi texto</button><button type="button" class="btn-sec tl-copiar">📋 Copiar mi texto</button><button type="button" class="btn-sec tl-borrar">Borrar</button></div><p class="tl-nota">👂 <strong>Escuche con atención:</strong> la voz lee su texto <strong>exactamente como está escrito</strong>, con sus errores. Si falta una tilde, la palabra suena distinta («papa» no es «papá»; «termino» no es «terminó»). Si falta un punto o una coma, la voz no hace la pausa. Cuando algo no suene como usted quería decirlo, revise esa palabra o esa oración.</p><p class="tl-aviso" aria-live="polite"></p>' +
      (lista.length ? '<fieldset class="tl-lista"><legend>Antes de entregar, revise:</legend>' + lista.map(function (x, i) { return '<label><input type="checkbox" data-i="' + i + '"> ' + esc(x) + '</label>'; }).join("") + '</fieldset>' : '');
    var area = t.querySelector("textarea"), cuenta = t.querySelector(".tl-cuenta"), cn = t.querySelector(".tl-con"), aviso = t.querySelector(".tl-aviso");
    function guarda() { try { localStorage.setItem(clave, JSON.stringify({ t: area.value, c: Array.prototype.map.call(t.querySelectorAll(".tl-lista input"), function (c) { return c.checked; }) })); } catch (e) {} }
    function actualiza() {
      var x = area.value.trim(), pal = x ? x.split(/\s+/).length : 0, ora = (x.match(/[^.!?…]+[.!?…]+/g) || []).length;
      cuenta.innerHTML = "Oraciones: <strong>" + ora + "</strong>" + (mO ? " de " + mO + " o más" : "") + " · Palabras: <strong>" + pal + "</strong>" + (mP ? " de " + mP + " o más" : "") +
        ((mO && ora >= mO && (!mP || pal >= mP)) ? " · <span class=\"tl-ok\">✓ Ya tiene el largo pedido.</span>" : "");
      var low = " " + x.toLowerCase().replace(/[.,;:¿?¡!«»"]/g, " ") + " ", usados = con.filter(function (c) { return low.indexOf(" " + c + " ") >= 0; });
      cn.innerHTML = con.length ? (usados.length ? "Conectores que usó (" + usados.length + "): " + usados.map(function (c) { return '<span class="tl-chip">' + esc(c) + "</span>"; }).join(" ") : "Todavía no usa conectores de la lista.") : "";
    }
    try { var g = JSON.parse(localStorage.getItem(clave) || "null"); if (g) { area.value = g.t || ""; (g.c || []).forEach(function (v, i) { var c = t.querySelector('.tl-lista input[data-i="' + i + '"]'); if (c) c.checked = v; }); } } catch (e) {}
    area.addEventListener("input", function () { actualiza(); guarda(); });
    t.addEventListener("change", function (ev) { if (ev.target.matches(".tl-lista input")) guarda(); });
    t.querySelector(".tl-oir").addEventListener("click", function () {
      if (!area.value.trim()) { aviso.textContent = "Primero escriba su texto."; return; }
      aviso.textContent = "🔊 Escuche si cada palabra suena como usted quería: una tilde o un signo que falta cambian el sonido.";
      hablar(area.value, 0.9);
    });
    t.querySelector(".tl-copiar").addEventListener("click", function () {
      var v = area.value; if (!v.trim()) { aviso.textContent = "Primero escriba su texto."; return; }
      function ok() { aviso.textContent = "✓ Copiado. Péguelo donde le pida su maestro (por ejemplo, en el foro del curso)."; }
      if (navigator.clipboard) navigator.clipboard.writeText(v).then(ok, function () { area.select(); document.execCommand("copy"); ok(); }); else { area.select(); document.execCommand("copy"); ok(); }
    });
    t.querySelector(".tl-borrar").addEventListener("click", function () { if (confirm("¿Borrar su texto? No se puede deshacer.")) { area.value = ""; actualiza(); guarda(); } });
    actualiza();
  }

  /* Audio en dos pasadas: <div class="escucha" data-texto="…" data-titulo="…"></div> (voz del navegador; la transcripción va aparte). */
  function escucha(e) {
    var txt = e.getAttribute("data-texto"), vel = 0.85;
    e.innerHTML = '<p class="es-vel" role="group" aria-label="Velocidad">Velocidad: <button type="button" class="btn-sec es-v" data-v="0.7" aria-pressed="false">🐢 Más lenta</button><button type="button" class="btn-sec es-v" data-v="0.85" aria-pressed="true">Normal</button></p>' +
      '<p><button type="button" class="btn-sec es-p" data-p="1">▶️ Primera pasada: idea general</button><button type="button" class="btn-sec es-p" data-p="2">▶️ Segunda pasada: detalles</button><button type="button" class="btn-sec es-stop">⏹️ Parar</button></p>' +
      '<p class="es-estado" aria-live="polite"></p>';
    var est = e.querySelector(".es-estado");
    e.addEventListener("click", function (ev) {
      var b = ev.target.closest("button"); if (!b) return;
      if (b.classList.contains("es-v")) { vel = +b.getAttribute("data-v"); cada(".es-v", function (x) { x.setAttribute("aria-pressed", x === b ? "true" : "false"); }, e); }
      else if (b.classList.contains("es-p")) {
        var p = b.getAttribute("data-p");
        est.textContent = p === "1" ? "Primera pasada: escuche sin escribir. ¿De qué trata? ¿Quién habla?" : "Segunda pasada: anote números, nombres, fechas y palabras clave.";
        hablar(txt, vel, function () { est.textContent = p === "1" ? "Terminó la primera pasada. Ahora escuche otra vez con papel y lápiz." : "Terminó la segunda pasada. Responda las preguntas y compruebe con la transcripción."; });
      } else if (b.classList.contains("es-stop")) { callar(); est.textContent = "Audio detenido."; }
    });
  }

  /* Grabadora: <div class="grabadora" data-nombre="mi-presentacion"></div>. La grabación queda en el equipo hasta que se descarga. */
  function grabadora(g) {
    var nombre = g.getAttribute("data-nombre") || "mi-grabacion";
    g.innerHTML = '<p class="gr-reloj" aria-live="off">0:00</p><p class="gr-estado" aria-live="polite">Listo para grabar.</p>' +
      '<p><button type="button" class="btn-sec gr-rec">🎙️ Grabar</button><button type="button" class="btn-sec gr-stop" disabled>⏹️ Detener</button></p>' +
      '<audio class="gr-audio" controls hidden></audio><p><a class="gr-bajar btn-sec" hidden>⬇️ Descargar mi grabación</a></p>';
    var rec, trozos = [], t0, int, reloj = g.querySelector(".gr-reloj"), est = g.querySelector(".gr-estado"), bR = g.querySelector(".gr-rec"), bS = g.querySelector(".gr-stop"), au = g.querySelector(".gr-audio"), dl = g.querySelector(".gr-bajar");
    if (!navigator.mediaDevices || !window.MediaRecorder) { est.textContent = "Este navegador no permite grabar. Use la grabadora de voz de su celular."; bR.disabled = true; return; }
    bR.addEventListener("click", function () {
      navigator.mediaDevices.getUserMedia({ audio: true }).then(function (s) {
        trozos = []; rec = new MediaRecorder(s);
        rec.ondataavailable = function (ev) { if (ev.data.size) trozos.push(ev.data); };
        rec.onstop = function () {
          s.getTracks().forEach(function (x) { x.stop(); });
          var tipo = rec.mimeType || "audio/webm", blob = new Blob(trozos, { type: tipo }), url = URL.createObjectURL(blob);
          au.src = url; au.hidden = false; dl.href = url; dl.download = nombre + (tipo.indexOf("mp4") >= 0 ? ".m4a" : tipo.indexOf("ogg") >= 0 ? ".ogg" : ".webm"); dl.hidden = false;
          est.textContent = "Grabación lista. Escúchela y, si le gusta, descárguela para entregarla.";
        };
        rec.start(); t0 = Date.now(); bR.disabled = true; bS.disabled = false; est.textContent = "Grabando… hable con calma.";
        int = setInterval(function () { var s2 = Math.floor((Date.now() - t0) / 1000); reloj.textContent = Math.floor(s2 / 60) + ":" + ("0" + s2 % 60).slice(-2); }, 250);
      }, function () { est.textContent = "No se pudo usar el micrófono. Revise el permiso del navegador o use la grabadora del celular."; });
    });
    bS.addEventListener("click", function () { if (rec && rec.state !== "inactive") rec.stop(); clearInterval(int); bR.disabled = false; bS.disabled = true; });
  }

  /* ================= Arranque ================= */
  function inicia() {
    botonesVoz(); sonidos();
    cada(".abc[data-abc]", abecedario);
    cada(".emparejar[data-letras]", emparejar);
    cada(".armar[data-suj]", armar);
    cada(".guia", guia);
    cada(".crono[data-texto]", crono);
    cada(".teatro[data-lineas]", teatro);
    cada(".constructor[data-grupos]", constructor);
    cada(".destello[data-grupos]", destello);
    cada(".taller[data-clave]", taller);
    cada(".escucha[data-texto]", escucha);
    cada(".grabadora", grabadora);
    botonVozPagina();
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", inicia); else inicia();
})();
