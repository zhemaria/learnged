/* LearnGED · Science practice activities (load after /math/practice.js)
   Same feedback as the rest of LearnGED: first mistake → a hint and another try;
   second mistake → the answer, explained. Two-option questions explain right away.
   The language comes from <html lang>: ES (from practice.js) is true on Spanish pages.
   José M. Fernández · CC BY-NC-SA 4.0 */

var SX = ES ? {
  paso: "Paso", sube: "Subir", baja: "Bajar", compruebe: "Comprobar el orden", otro: "Otro ejercicio",
  bienOrden: "El orden es correcto.", faltan: "Elija una opción en cada lista antes de comprobar.",
  malOrden: function (n) { return n === 1 ? "Hay 1 lugar marcado en amarillo que no está bien." : "Hay " + n + " lugares marcados en amarillo que no están bien."; },
  ordenCorrecto: "La lista ya muestra el orden correcto.", queHabria: "Qué habría pasado en el laboratorio: ",
  movido: function (t, i, n) { return "«" + t + "» está ahora en el lugar " + i + " de " + n + "."; },
  elija: "Elija…", noPertenece: "No pertenece al informe",
  ensayo: "Ensayo", cambio: "Qué cambió entre A y B", altA: "Altura A (cm)", altB: "Altura B (cm)", interp: "¿Se puede concluir?",
  nada: "Nada", si: "Sí", no: "No", ninguno: "Todavía no ha hecho ningún ensayo."
} : {
  paso: "Step", sube: "Move up", baja: "Move down", compruebe: "Check the order", otro: "New exercise",
  bienOrden: "The order is correct.", faltan: "Choose an option in every list before you check.",
  malOrden: function (n) { return n === 1 ? "1 place marked in yellow is not right yet." : n + " places marked in yellow are not right yet."; },
  ordenCorrecto: "The list now shows the correct order.", queHabria: "What would have happened in the lab: ",
  movido: function (t, i, n) { return "“" + t + "” is now in place " + i + " of " + n + "."; },
  elija: "Choose…", noPertenece: "Does not belong in the report",
  ensayo: "Trial", cambio: "What changed between A and B", altA: "Height A (cm)", altB: "Height B (cm)", interp: "Can you conclude anything?",
  nada: "Nothing", si: "Yes", no: "No", ninguno: "You have not run any trials yet."
};

/* A shuffled deck: items do not repeat until all have been used */
function mazo(lista) {
  var pila = [];
  return function () { if (!pila.length) pila = baraja(lista.slice()); return pila.pop(); };
}

/* Multiple choice from a bank. Each item: {enun, ops:[...], ok, pistas:{i: text}, pista, exp}
   (ops in their natural order; they are shuffled on screen) */
function creaBanco(pre, banco, prep) {
  var saca = mazo(banco);
  creaPracticaOM(pre, function () {
    var it = saca();
    if (prep) it = prep(it);
    var pistas = {};
    Object.keys(it.pistas || {}).forEach(function (k) { pistas["o" + k] = it.pistas[k]; });
    return {
      enun: it.enun,
      opciones: it.ops.map(function (o, i) { return { clave: "o" + i, html: o }; }),
      correcta: "o" + it.ok, pistas: pistas, pista: it.pista || "", bien: it.exp || "", mal: it.exp || "", enOrden: !!it.enOrden
    };
  });
}

function marcador(pre, est) { $(pre + "-marcador").textContent = est.total ? TX.resueltos(est.primero + est.pista, est.primero, est.total) : ""; }
function cuenta(est, intentos, ok) { est.total++; if (ok) { if (intentos === 1) est.primero++; else est.pista++; } }

/* ---------- Put the steps in order (up/down buttons: works with keyboard and touch) ----------
   item: {titulo, intro, pasos:[in the right order], inicio:[starting order], cons:{"a>b": text}, libres:[[a,b]], general}
   "a>b" = step a was placed before step b (a comes later in the right order). libres: pairs that can go in either order. */
function creaOrden(pre, banco) {
  var saca = mazo(banco), est = { primero: 0, pista: 0, total: 0 }, it, orden, intentos, cerrado;
  var lista = $(pre + "-lista"), fb = $(pre + "-fb"), voz = $(pre + "-voz");
  function libre(a, b) { return (it.libres || []).some(function (p) { return (p[0] === a && p[1] === b) || (p[0] === b && p[1] === a); }); }
  function pinta(marcas) {
    lista.innerHTML = "";
    orden.forEach(function (k, i) {
      var li = document.createElement("li");
      li.className = "paso-orden" + (marcas ? (marcas[i] ? " ok" : " revisar") : "");
      li.innerHTML = '<span class="po-num" aria-hidden="true">' + (i + 1) + '</span><span class="po-txt">' + it.pasos[k] + '</span>' +
        '<span class="po-btn"><button type="button" class="btn-sec" data-m="-1" aria-label="' + SX.sube + ': ' + it.pasos[k].replace(/"/g, "&quot;") + '"' + (i === 0 || cerrado ? " disabled" : "") + '>▲</button>' +
        '<button type="button" class="btn-sec" data-m="1" aria-label="' + SX.baja + ': ' + it.pasos[k].replace(/"/g, "&quot;") + '"' + (i === orden.length - 1 || cerrado ? " disabled" : "") + '>▼</button></span>';
      li.querySelectorAll("button").forEach(function (b) {
        b.addEventListener("click", function () {
          var d = parseInt(b.getAttribute("data-m"), 10), j = i + d, t = orden[i];
          orden[i] = orden[j]; orden[j] = t; pinta();
          voz.textContent = SX.movido(it.pasos[t], j + 1, orden.length);
          var bt = lista.children[j].querySelector('button[data-m="' + d + '"]') || lista.children[j].querySelector("button:not([disabled])");
          if (bt) bt.focus();
        });
      });
      lista.appendChild(li);
    });
  }
  function nuevo() {
    it = saca(); orden = it.inicio.slice(); intentos = 0; cerrado = false;
    $(pre + "-enun").innerHTML = "<p><strong>" + it.titulo + "</strong></p><p>" + it.intro + "</p>";
    fb.className = "fb"; fb.innerHTML = ""; $(pre + "-comprobar").disabled = false; pinta();
  }
  function correcto(i) {
    if (orden[i] === i) return true;
    return libre(orden[i], i) && Math.abs(orden[i] - i) === 1 && orden[orden[i]] === i;
  }
  function comprueba() {
    if (cerrado) return;
    intentos++;
    var marcas = orden.map(function (k, i) { return correcto(i); }), malos = marcas.filter(function (m) { return !m; }).length;
    if (!malos) {
      cerrado = true; cuenta(est, intentos, true); pinta(marcas);
      fb.className = "fb bien"; fb.innerHTML = TX.bien + SX.bienOrden + " " + it.general + " <em>" + (intentos === 1 ? elige(ELOGIO) : elige(ELOGIO2)) + "</em>";
      $(pre + "-comprobar").disabled = true;
    } else {
      var avisos = [];
      for (var a = 0; a < orden.length; a++) for (var b = a + 1; b < orden.length; b++)
        if (orden[a] > orden[b] && !libre(orden[a], orden[b])) { var c = it.cons[orden[a] + ">" + orden[b]]; if (c && avisos.indexOf(c) < 0) avisos.push(c); }
      if (intentos === 1) {
        pinta(marcas);
        fb.className = "fb pista";
        fb.innerHTML = TX.todavia + SX.malOrden(malos) + (avisos.length ? " " + SX.queHabria + avisos[0] : "") + TX.otraVez;
      } else {
        cerrado = true; cuenta(est, intentos, false); orden = it.pasos.map(function (p, i) { return i; }); pinta(orden.map(function () { return true; }));
        fb.className = "fb mal";
        fb.innerHTML = TX.asi + SX.ordenCorrecto + " " + it.general + (avisos.length ? "<br>" + SX.queHabria + avisos.join(" ") : "") + TX.nuevo;
        $(pre + "-comprobar").disabled = true;
      }
    }
    marcador(pre, est);
  }
  $(pre + "-comprobar").addEventListener("click", comprueba);
  $(pre + "-nuevo").addEventListener("click", nuevo);
  nuevo(); marcador(pre, est);
}

/* ---------- Sort each piece into a group with a list (e.g., each paragraph into its stage) ----------
   item: {titulo, intro, piezas:[{t, v}], grupos:[names], extra:"text after solving"}; v = index in grupos */
function creaClasifica(pre, banco) {
  var saca = mazo(banco), est = { primero: 0, pista: 0, total: 0 }, it, piezas, intentos, cerrado;
  var cont = $(pre + "-piezas"), fb = $(pre + "-fb");
  function nuevo() {
    it = saca(); piezas = baraja(it.piezas.slice()); intentos = 0; cerrado = false;
    $(pre + "-enun").innerHTML = "<p><strong>" + it.titulo + "</strong></p><p>" + it.intro + "</p>";
    cont.innerHTML = "";
    piezas.forEach(function (p, i) {
      var id = pre + "-s" + i, d = document.createElement("div");
      d.className = "pieza";
      d.innerHTML = '<p class="pz-txt" id="' + id + '-t">' + p.t + '</p><label class="pz-lab" for="' + id + '">' + (it.etiqueta || SX.elija) + '</label> <select id="' + id + '" aria-describedby="' + id + '-t"><option value="">' + SX.elija + '</option>' +
        it.grupos.map(function (g, k) { return '<option value="' + k + '">' + g + '</option>'; }).join("") + '</select><p class="pz-fb" aria-live="polite"></p>';
      cont.appendChild(d);
    });
    fb.className = "fb"; fb.innerHTML = ""; $(pre + "-comprobar").disabled = false;
  }
  function comprueba() {
    if (cerrado) return;
    var sel = cont.querySelectorAll("select"), vacio = false;
    sel.forEach(function (s) { if (s.value === "") vacio = true; });
    if (vacio) { fb.className = "fb pista"; fb.innerHTML = SX.faltan; return; }
    intentos++;
    var malos = 0;
    sel.forEach(function (s, i) {
      var p = piezas[i], ok = parseInt(s.value, 10) === p.v, caja = s.parentNode;
      caja.classList.remove("ok", "revisar");
      caja.querySelector(".pz-fb").innerHTML = "";
      if (ok) { caja.classList.add("ok"); s.disabled = true; }
      else {
        malos++; caja.classList.add("revisar");
        if (intentos === 1 && p.pista) caja.querySelector(".pz-fb").innerHTML = p.pista;
      }
    });
    if (!malos) {
      cerrado = true; cuenta(est, intentos, true);
      fb.className = "fb bien"; fb.innerHTML = TX.bien + (it.extra || "") + " <em>" + (intentos === 1 ? elige(ELOGIO) : elige(ELOGIO2)) + "</em>";
      $(pre + "-comprobar").disabled = true;
    } else if (intentos === 1) {
      fb.className = "fb pista"; fb.innerHTML = TX.todavia + SX.malOrden(malos) + TX.otraVez;
    } else {
      cerrado = true; cuenta(est, intentos, false);
      sel.forEach(function (s, i) {
        var p = piezas[i], caja = s.parentNode;
        if (parseInt(s.value, 10) !== p.v) { s.value = String(p.v); caja.classList.remove("revisar"); caja.classList.add("corregida"); caja.querySelector(".pz-fb").innerHTML = "✓ " + it.grupos[p.v] + (p.por ? ". " + p.por : ""); }
        s.disabled = true;
      });
      fb.className = "fb mal"; fb.innerHTML = TX.asi + (it.extra || "") + TX.nuevo;
      $(pre + "-comprobar").disabled = true;
    }
    marcador(pre, est);
  }
  $(pre + "-comprobar").addEventListener("click", comprueba);
  $(pre + "-nuevo").addEventListener("click", nuevo);
  nuevo(); marcador(pre, est);
}

/* ---------- The greenhouse: isolate the variable ----------
   Two groups of plants, four factors. Deterministic model: the same setup always gives the same result.
   F: [{id, t, base, ops:[[value, label]], f:{value: factor}}], BASE: height in centimeters with every factor at its usual value. */
function creaInvernadero(pre, F, BASE, TXI) {
  var A = {}, B = {}, n = 0;
  F.forEach(function (f) { A[f.id] = f.base; B[f.id] = f.base; });
  function sel(g, f) {
    return '<label for="' + pre + g + f.id + '">' + f.t + '</label><select id="' + pre + g + f.id + '" data-g="' + g + '" data-f="' + f.id + '">' +
      f.ops.map(function (o) { return '<option value="' + o[0] + '"' + (o[0] === f.base ? " selected" : "") + '>' + o[1] + '</option>'; }).join("") + '</select>';
  }
  $(pre + "-mesa").innerHTML = ["A", "B"].map(function (g) {
    return '<fieldset class="grupo-inv"><legend>' + TXI.grupo + ' ' + g + '</legend>' + F.map(function (f) { return '<div class="campo-inv">' + sel(g, f) + '</div>'; }).join("") + '</fieldset>';
  }).join("");
  $(pre + "-mesa").querySelectorAll("select").forEach(function (s) {
    s.addEventListener("change", function () { (s.getAttribute("data-g") === "A" ? A : B)[s.getAttribute("data-f")] = s.value; });
  });
  function altura(g) { var h = BASE; F.forEach(function (f) { h *= f.f[g[f.id]]; }); return Math.round(h * 10) / 10; }
  $(pre + "-ensayar").addEventListener("click", function () {
    var cambia = F.filter(function (f) { return A[f.id] !== B[f.id]; }), hA = altura(A), hB = altura(B), fb = $(pre + "-fb"), msg, clase;
    n++;
    var nombres = cambia.map(function (f) { return f.t.toLowerCase(); });
    if (!cambia.length) { clase = "pista"; msg = TXI.igual(hA); }
    else if (cambia.length === 1) {
      clase = "bien";
      msg = TXI.uno(nombres[0], hA, hB, Math.round(Math.abs(hA - hB) * 10) / 10);
    } else { clase = "mal"; msg = TXI.varios(nombres, hA, hB); }
    fb.className = "fb " + clase; fb.innerHTML = msg;
    var tb = $(pre + "-cuaderno");
    if (n === 1) tb.innerHTML = "";
    var tr = document.createElement("tr");
    tr.innerHTML = '<th scope="row">' + n + '</th><td>' + (cambia.length ? nombres.join(", ") : SX.nada) + '</td><td>' + hA.toFixed(1) + '</td><td>' + hB.toFixed(1) + '</td><td>' + (cambia.length === 1 ? SX.si : SX.no) + '</td>';
    tb.appendChild(tr);
  });
  $(pre + "-reinicia").addEventListener("click", function () {
    F.forEach(function (f) { A[f.id] = f.base; B[f.id] = f.base; ["A", "B"].forEach(function (g) { $(pre + g + f.id).value = f.base; }); });
    $(pre + "-fb").className = "fb"; $(pre + "-fb").innerHTML = "";
  });
}

/* ---------- Fill in the blanks of a sentence with lists ----------
   item: {partes:["text", {ops:[...], ok}, "text", ...], exp, pista} */
function creaHuecos(pre, banco) {
  var saca = mazo(banco), est = { primero: 0, pista: 0, total: 0 }, it, intentos, cerrado, fb = $(pre + "-fb");
  function nuevo() {
    it = saca(); intentos = 0; cerrado = false; var k = 0;
    $(pre + "-enun").innerHTML = '<p class="frase-huecos">' + it.partes.map(function (p) {
      if (typeof p === "string") return p;
      var id = pre + "-h" + (k++);
      return '<label class="cap-oculto" for="' + id + '">' + (ES ? "Hueco " : "Blank ") + k + '</label><select id="' + id + '"><option value="">…</option>' + p.ops.map(function (o, i) { return '<option value="' + i + '">' + o + '</option>'; }).join("") + '</select>';
    }).join("") + '</p>';
    fb.className = "fb"; fb.innerHTML = ""; $(pre + "-comprobar").disabled = false;
  }
  function comprueba() {
    if (cerrado) return;
    var huecos = it.partes.filter(function (p) { return typeof p !== "string"; }), sel = $(pre + "-enun").querySelectorAll("select"), vacio = false, malos = 0;
    sel.forEach(function (s) { if (s.value === "") vacio = true; });
    if (vacio) { fb.className = "fb pista"; fb.innerHTML = SX.faltan; return; }
    intentos++;
    sel.forEach(function (s, i) { var ok = parseInt(s.value, 10) === huecos[i].ok; s.classList.toggle("revisar", !ok); if (ok) s.disabled = true; else malos++; });
    if (!malos) {
      cerrado = true; cuenta(est, intentos, true);
      fb.className = "fb bien"; fb.innerHTML = TX.bien + it.exp + " <em>" + (intentos === 1 ? elige(ELOGIO) : elige(ELOGIO2)) + "</em>";
      $(pre + "-comprobar").disabled = true;
    } else if (intentos === 1) {
      fb.className = "fb pista"; fb.innerHTML = TX.todavia + (it.pista || SX.malOrden(malos)) + TX.otraVez;
    } else {
      cerrado = true; cuenta(est, intentos, false);
      sel.forEach(function (s, i) { s.value = String(huecos[i].ok); s.classList.remove("revisar"); s.disabled = true; });
      fb.className = "fb mal"; fb.innerHTML = TX.asi + it.exp + TX.nuevo;
      $(pre + "-comprobar").disabled = true;
    }
    marcador(pre, est);
  }
  $(pre + "-comprobar").addEventListener("click", comprueba);
  $(pre + "-nuevo").addEventListener("click", nuevo);
  nuevo(); marcador(pre, est);
}
