/* LearnGED · Level 4 · Coordinate plane engine (Topic 1 and the later topics that graph).
   Loaded after practice.js, radicals.js and linear.js (it uses T, aprox, leeDecimal, esCuadrado, simplRad).
   José M. Fernández · CC BY-NC-SA 4.0 */

/* ---------- Numbers and pairs ---------- */
function sg(n){ return String(n).replace("-", "−"); }
function nd(x){ var r = Math.round(x * 1000) / 1000; return sg(r); }                 /* number with at most 3 decimals */
function par(x, y){ return "(" + nd(x) + ", " + nd(y) + ")"; }
function vozN(n){ return (n < 0 ? T("negative ", "menos ") : "") + Math.abs(Math.round(n * 1000) / 1000); }
function parVoz(x, y){ return T("the point ", "el punto ") + vozN(x) + T(" comma ", " coma ") + vozN(y); }
function parHTML(x, y, nombre){ return '<span aria-hidden="true">' + (nombre || "") + par(x, y) + '</span><span class="sr-only">' + (nombre ? nombre + ", " : "") + parVoz(x, y) + "</span>"; }
function cuadrante(x, y){
  if (x === 0 && y === 0) return T("the origin", "el origen");
  if (x === 0) return T("on the y-axis", "sobre el eje y");
  if (y === 0) return T("on the x-axis", "sobre el eje x");
  return T("Quadrant ", "cuadrante ") + (x > 0 ? (y > 0 ? "I" : "IV") : (y > 0 ? "II" : "III"));
}
/* Square root shown simply: √25 = 5; √50 = 5√2 ≈ 7.1; √41 ≈ 6.4 */
function raizTexto(n, dec){
  if (esCuadrado(n)) return "√" + n + " = " + Math.sqrt(n);
  var s = simplRad(n);
  return "√" + n + (s.k > 1 ? " = " + s.k + "√" + s.r : "") + " ≈ " + aprox(Math.sqrt(n), dec === undefined ? 1 : dec);
}

/* ---------- Drawing the plane ----------
   o = {xmin, xmax, ymin, ymax, u (pixels per unit), paso (label every), voz, cuadrantes, sinNumeros}
   Returns P with P.X, P.Y, P.svg(cuerpo) and drawing helpers that return SVG strings. */
var C4 = {azul: "#0d47a1", rojo: "#b71c1c", verde: "#1b5e20", tinta: "#10174f", cateto: "#00695c", morado: "#6a1b9a", gris: "#9e9e9e"};
function Plano(o){
  o = o || {};
  var xmin = o.xmin === undefined ? -10 : o.xmin, xmax = o.xmax === undefined ? 10 : o.xmax, ymin = o.ymin === undefined ? -10 : o.ymin, ymax = o.ymax === undefined ? 10 : o.ymax;
  var u = o.u || Math.min(34, Math.floor(560 / (xmax - xmin))), m = 30, W = (xmax - xmin) * u + 2 * m, H = (ymax - ymin) * u + 2 * m;
  var paso = o.paso || ((xmax - xmin) > 24 ? 5 : ((xmax - xmin) > 14 ? 2 : 1));
  var P = {xmin: xmin, xmax: xmax, ymin: ymin, ymax: ymax, u: u, W: W, H: H};
  P.X = function(x){ return m + (x - xmin) * u; };
  P.Y = function(y){ return m + (ymax - y) * u; };
  P.desdePx = function(px, py){ return [xmin + (px - m) / u, ymax - (py - m) / u]; };
  P.rejilla = function(){
    var s = "", x, y;
    for (x = xmin; x <= xmax; x++) s += '<line x1="' + P.X(x) + '" y1="' + P.Y(ymax) + '" x2="' + P.X(x) + '" y2="' + P.Y(ymin) + '" stroke="' + (x % paso === 0 ? "#cfd8dc" : "#eceff1") + '" stroke-width="1"/>';
    for (y = ymin; y <= ymax; y++) s += '<line x1="' + P.X(xmin) + '" y1="' + P.Y(y) + '" x2="' + P.X(xmax) + '" y2="' + P.Y(y) + '" stroke="' + (y % paso === 0 ? "#cfd8dc" : "#eceff1") + '" stroke-width="1"/>';
    if (o.cuadrantes && xmin < 0 && xmax > 0 && ymin < 0 && ymax > 0){
      [["I", xmax * .62, ymax * .82], ["II", xmin * .62, ymax * .82], ["III", xmin * .62, ymin * .82], ["IV", xmax * .62, ymin * .82]].forEach(function(q){
        s += '<text x="' + f1(P.X(q[1])) + '" y="' + f1(P.Y(q[2])) + '" text-anchor="middle" dominant-baseline="middle" font-size="' + Math.max(20, u * .9) + '" font-weight="700" fill="#cfd8dc" font-family="Georgia, serif">' + q[0] + "</text>";
      });
    }
    var ex = xmin <= 0 && xmax >= 0, ey = ymin <= 0 && ymax >= 0, y0 = ey ? 0 : ymin, x0 = ex ? 0 : xmin;
    s += '<line x1="' + (P.X(xmin) - 8) + '" y1="' + P.Y(y0) + '" x2="' + (P.X(xmax) + 10) + '" y2="' + P.Y(y0) + '" stroke="' + C4.tinta + '" stroke-width="2"/>';
    s += '<line x1="' + P.X(x0) + '" y1="' + (P.Y(ymin) + 8) + '" x2="' + P.X(x0) + '" y2="' + (P.Y(ymax) - 10) + '" stroke="' + C4.tinta + '" stroke-width="2"/>';
    s += '<polygon points="' + (P.X(xmax) + 14) + "," + P.Y(y0) + " " + (P.X(xmax) + 4) + "," + (P.Y(y0) - 5) + " " + (P.X(xmax) + 4) + "," + (P.Y(y0) + 5) + '" fill="' + C4.tinta + '"/>';
    s += '<polygon points="' + P.X(x0) + "," + (P.Y(ymax) - 14) + " " + (P.X(x0) - 5) + "," + (P.Y(ymax) - 4) + " " + (P.X(x0) + 5) + "," + (P.Y(ymax) - 4) + '" fill="' + C4.tinta + '"/>';
    s += '<text x="' + (P.X(xmax) + 14) + '" y="' + (P.Y(y0) - 12) + '" font-size="16" font-style="italic" font-weight="700" fill="' + C4.tinta + '" text-anchor="middle">x</text>';
    s += '<text x="' + (P.X(x0) + 14) + '" y="' + (P.Y(ymax) - 10) + '" font-size="16" font-style="italic" font-weight="700" fill="' + C4.tinta + '">y</text>';
    return s;
  };
  P.numeros = function(){
    var s = "", x, y, ex = xmin <= 0 && xmax >= 0, ey = ymin <= 0 && ymax >= 0, y0 = ey ? 0 : ymin, x0 = ex ? 0 : xmin, h = ' paint-order="stroke" stroke="#fff" stroke-width="3"';
    if (!o.sinNumeros){
      var fs = u < 22 ? 11 : 13;
      for (x = xmin; x <= xmax; x++) if (x !== 0 && x % paso === 0 && x !== xmax) s += '<text x="' + P.X(x) + '" y="' + (P.Y(y0) + fs + 5) + '" font-size="' + fs + '" fill="#455a64" text-anchor="middle"' + h + '>' + sg(x) + "</text>";
      for (y = ymin; y <= ymax; y++) if (y !== 0 && y % paso === 0 && y !== ymax) s += '<text x="' + (P.X(x0) - 6) + '" y="' + (P.Y(y) + 4) + '" font-size="' + fs + '" fill="#455a64" text-anchor="end"' + h + '>' + sg(y) + "</text>";
      if (ex && ey) s += '<text x="' + (P.X(0) - 6) + '" y="' + (P.Y(0) + fs + 4) + '" font-size="' + fs + '" fill="#455a64" text-anchor="end"' + h + '>0</text>';
    }
    return s;
  };
  P.seg = function(a, b, color, ancho, raya){ return '<line x1="' + f1(P.X(a[0])) + '" y1="' + f1(P.Y(a[1])) + '" x2="' + f1(P.X(b[0])) + '" y2="' + f1(P.Y(b[1])) + '" stroke="' + (color || C4.tinta) + '" stroke-width="' + (ancho || 3) + '"' + (raya ? ' stroke-dasharray="' + raya + '"' : "") + ' stroke-linecap="round"/>'; };
  P.poli = function(l, relleno, color, ancho){ return '<polygon points="' + l.map(function(p){ return f1(P.X(p[0])) + "," + f1(P.Y(p[1])); }).join(" ") + '" fill="' + (relleno || "none") + '" stroke="' + (color || C4.tinta) + '" stroke-width="' + (ancho || 3) + '" stroke-linejoin="round"/>'; };
  /* label: text next to the point; lado: "ne", "nw", "se", "sw" or automatic */
  P.punto = function(p, color, etiqueta, lado, r){
    var cx = P.X(p[0]), cy = P.Y(p[1]), s = '<circle cx="' + f1(cx) + '" cy="' + f1(cy) + '" r="' + (r || 6) + '" fill="' + (color || C4.azul) + '" stroke="#fff" stroke-width="2"/>';
    if (etiqueta){
      if (p[0] === 0 && p[1] !== 0) lado = (p[1] > 0 ? "n" : "s") + "e";
      else if (p[1] === 0 && p[0] !== 0) lado = "n" + (p[0] > 0 ? "e" : "w");
      lado = lado || ((p[0] >= (xmin + xmax) / 2 ? "w" : "e") === "w" ? (p[1] >= (ymin + ymax) / 2 ? "sw" : "nw") : (p[1] >= (ymin + ymax) / 2 ? "se" : "ne"));
      var dx = lado.indexOf("e") >= 0 ? 10 : -10, dy = lado.indexOf("n") >= 0 ? -10 : 20;
      s += '<text x="' + f1(cx + dx) + '" y="' + f1(cy + dy) + '" font-size="15" font-weight="700" fill="' + (color || C4.azul) + '" text-anchor="' + (dx > 0 ? "start" : "end") + '" paint-order="stroke" stroke="#fff" stroke-width="4">' + etiqueta + "</text>";
    }
    return s;
  };
  P.texto = function(p, txt, color, tam, ancla, dx, dy){ return '<text x="' + f1(P.X(p[0]) + (dx || 0)) + '" y="' + f1(P.Y(p[1]) + (dy || 0)) + '" font-size="' + (tam || 14) + '" font-weight="700" fill="' + (color || C4.tinta) + '" text-anchor="' + (ancla || "middle") + '" dominant-baseline="middle" paint-order="stroke" stroke="#fff" stroke-width="4">' + txt + "</text>"; };
  P.svg = function(cuerpo, voz, ancho){ return '<svg class="geo-svg plano-svg" viewBox="0 0 ' + W + " " + H + '" role="img" aria-label="' + voz + '" style="max-width:' + (ancho || Math.min(W, 560)) + 'px">' + P.rejilla() + (cuerpo || "") + P.numeros() + "</svg>"; };
  return P;
}

/* Right-triangle legs between two points (for distance): dashed legs with Δx and Δy */
function catetos(P, a, b){
  var c = [b[0], a[1]], s = P.poli([a, c, b], "rgba(26,35,126,.07)", "none", 0);
  s += P.seg(a, c, C4.cateto, 2.5, "7 5") + P.seg(c, b, C4.cateto, 2.5, "7 5");
  var dx = Math.abs(b[0] - a[0]), dy = Math.abs(b[1] - a[1]), arriba = b[1] > a[1];
  if (dx) s += P.texto([(a[0] + b[0]) / 2, a[1]], "Δx = " + dx, C4.cateto, 14, "middle", 0, arriba ? 16 : -14);
  var der = b[0] > a[0] || P.X(b[0]) - 70 < P.X(P.xmin);
  if (P.X(b[0]) + 70 > P.X(P.xmax)) der = false;
  if (dy) s += P.texto([b[0], (a[1] + b[1]) / 2], "Δy = " + dy, C4.cateto, 14, der ? "start" : "end", der ? 10 : -10, 0);
  return s;
}

/* ---------- Clickable plane (place a point with the mouse, finger, or keyboard) ----------
   cont: element; o: options for Plano; cb(x, y) when a point is placed. Returns {pinta(cuerpo), cursor:[x,y], limpia()} */
function PlanoActivo(cont, o, cb, voz){
  var P = Plano(o), cuerpo = "", cur = [0, 0], marcado = null, activo = false;
  cont.innerHTML = "";
  var cap = document.createElement("div"); cont.appendChild(cap);
  var lect = document.createElement("p"); lect.className = "nota lectura-plano"; lect.setAttribute("aria-live", "polite"); cont.appendChild(lect);
  function dibuja(){
    var s = P.svg(cuerpo + (marcado ? P.punto(marcado, C4.rojo, par(marcado[0], marcado[1])) : "") +
      (activo ? '<circle cx="' + P.X(cur[0]) + '" cy="' + P.Y(cur[1]) + '" r="11" fill="none" stroke="' + C4.morado + '" stroke-width="2.5" stroke-dasharray="4 3" class="cursor-plano"/>' : ""), voz);
    cap.innerHTML = s.replace("<svg ", '<svg tabindex="0" ');
    var svg = cap.querySelector("svg");
    svg.setAttribute("aria-label", voz + " " + T("Use the arrow keys to move the cursor and Enter to mark the point.", "Use las flechas para mover el cursor y Enter para marcar el punto."));
    svg.style.cursor = "crosshair";
    svg.addEventListener("click", function(ev){
      var pt = svg.createSVGPoint(); pt.x = ev.clientX; pt.y = ev.clientY;
      var q = pt.matrixTransform(svg.getScreenCTM().inverse()), c = P.desdePx(q.x, q.y);
      var x = Math.max(P.xmin, Math.min(P.xmax, Math.round(c[0]))), y = Math.max(P.ymin, Math.min(P.ymax, Math.round(c[1])));
      cur = [x, y]; activo = true; marca();
    });
    svg.addEventListener("keydown", function(ev){
      var k = ev.key, d = ev.shiftKey ? 5 : 1, mov = true; activo = true;
      if (k === "ArrowLeft") cur[0] -= d; else if (k === "ArrowRight") cur[0] += d; else if (k === "ArrowUp") cur[1] += d; else if (k === "ArrowDown") cur[1] -= d;
      else if (k === "Home") cur = [0, 0]; else if (k === "Enter" || k === " "){ ev.preventDefault(); marca(); return; } else mov = false;
      if (!mov) return;
      ev.preventDefault();
      cur[0] = Math.max(P.xmin, Math.min(P.xmax, cur[0])); cur[1] = Math.max(P.ymin, Math.min(P.ymax, cur[1]));
      dibuja(); cap.querySelector("svg").focus();
      lect.textContent = T("Cursor at ", "Cursor en ") + par(cur[0], cur[1]);
    });
  }
  function marca(){ marcado = cur.slice(); dibuja(); cap.querySelector("svg").focus(); lect.textContent = T("You marked ", "Marcó ") + par(marcado[0], marcado[1]) + "."; if (cb) cb(marcado[0], marcado[1]); }
  dibuja();
  return {
    P: P,
    pinta: function(c){ cuerpo = c || ""; dibuja(); },
    limpia: function(){ marcado = null; cur = [0, 0]; activo = false; cuerpo = ""; lect.textContent = ""; dibuja(); },
    marcado: function(){ return marcado; }
  };
}

/* ---------- Practice with an ordered-pair answer (two boxes, two tries) ----------
   gen() returns {enun, x, y, solucion, diag(xu, yu) → message for the hint} */
function leePar(pre){ return [leeDecimal($(pre + "-x").value), leeDecimal($(pre + "-y").value)]; }
function creaPracticaPar(pre, gen){
  var est = {primero: 0, pista: 0, total: 0, actual: null, resuelta: false, intentos: 0};
  function marcador(){ $(pre + "-marcador").textContent = est.total ? TX.resueltos(est.primero + est.pista, est.primero, est.total) : ""; }
  function pinta(){
    est.actual = gen(); est.resuelta = false; est.intentos = 0;
    $(pre + "-enun").innerHTML = est.actual.enun;
    ["x", "y"].forEach(function(k){ var i = $(pre + "-" + k); i.value = ""; i.disabled = false; i.classList.remove("error"); });
    $(pre + "-comprobar").disabled = false;
    $(pre + "-fb").className = "fb"; $(pre + "-fb").innerHTML = "";
    if (est.actual.despues) est.actual.despues();
  }
  function bloquea(){ $(pre + "-x").disabled = true; $(pre + "-y").disabled = true; $(pre + "-comprobar").disabled = true; }
  function comprueba(){
    if (est.resuelta) return;
    var q = est.actual, fb = $(pre + "-fb"), v = leePar(pre);
    $(pre + "-x").classList.toggle("error", v[0] === null); $(pre + "-y").classList.toggle("error", v[1] === null);
    if (v[0] === null || v[1] === null){ fb.className = "fb pista"; fb.innerHTML = T("Type a number in each box (for example, −3 or 2.5).", "Escriba un número en cada casilla (por ejemplo, −3 o 2.5)."); return; }
    est.intentos++;
    var ok = Math.abs(v[0] - q.x) < 1e-9 && Math.abs(v[1] - q.y) < 1e-9;
    if (ok){
      est.resuelta = true; est.total++; if (est.intentos === 1) est.primero++; else est.pista++;
      fb.className = "fb bien"; fb.innerHTML = TX.bien + q.solucion + " <em>" + (est.intentos === 1 ? elige(ELOGIO) : elige(ELOGIO2)) + "</em>"; bloquea();
      if (q.alFinal) q.alFinal(true);
    } else if (est.intentos >= 2){
      est.resuelta = true; est.total++;
      fb.className = "fb mal"; fb.innerHTML = TX.asi + q.solucion + TX.nuevo; bloquea();
      if (q.alFinal) q.alFinal(false);
    } else {
      fb.className = "fb pista"; fb.innerHTML = TX.todavia + (q.diag ? q.diag(v[0], v[1]) : TX.revise) + TX.unoMas;
      $(pre + "-x").focus();
    }
    marcador();
  }
  $(pre + "-comprobar").addEventListener("click", comprueba);
  [$(pre + "-x"), $(pre + "-y")].forEach(function(i){ i.addEventListener("keydown", function(ev){ if (ev.key === "Enter") comprueba(); }); });
  $(pre + "-nuevo").addEventListener("click", pinta);
  pinta(); marcador();
  return {nuevo: pinta};
}
/* What went wrong with an ordered pair: swapped, a sign, one coordinate */
function diagPar(xu, yu, x, y){
  var igual = function(a, b){ return Math.abs(a - b) < 1e-9; };
  if (igual(xu, y) && igual(yu, x) && !igual(x, y)) return T("You swapped the coordinates. In (x, y), x (left or right) comes first, then y (up or down).", "Invirtió las coordenadas. En (x, y) va primero la x (izquierda o derecha) y después la y (arriba o abajo).");
  if (igual(xu, -x) && igual(yu, -y)) return T("Both signs are wrong. Left of the origin x is negative; below it y is negative.", "Los dos signos están mal. A la izquierda del origen la x es negativa; debajo, la y es negativa.");
  if (igual(xu, -x) && igual(yu, y)) return T("The y-coordinate is right, but check the sign of x: left of the origin it is negative.", "La coordenada y está bien, pero revise el signo de la x: a la izquierda del origen es negativa.");
  if (igual(yu, -y) && igual(xu, x)) return T("The x-coordinate is right, but check the sign of y: below the origin it is negative.", "La coordenada x está bien, pero revise el signo de la y: debajo del origen es negativa.");
  if (igual(xu, x)) return T("The x-coordinate is right. Count the y-coordinate again (up or down).", "La coordenada x está bien. Cuente otra vez la coordenada y (arriba o abajo).");
  if (igual(yu, y)) return T("The y-coordinate is right. Count the x-coordinate again (left or right).", "La coordenada y está bien. Cuente otra vez la coordenada x (izquierda o derecha).");
  return T("Both coordinates are off. Start at the origin: first move left or right (x), then up or down (y).", "Las dos coordenadas están mal. Parta del origen: primero muévase a la izquierda o a la derecha (x) y después arriba o abajo (y).");
}
function azarNZ(a, b){ var n; do { n = aleatorio(a, b); } while (n === 0); return n; }

/* ---------- Plane with draggable points (mouse, finger, or keyboard) ----------
   pts: [{x, y, nombre, color}]; alCambiar(pts) runs after every move and returns the SVG of the dynamic layer
   (lines, triangles…) drawn under the points. Tapping a grid crossing moves the last point used. */
function PlanoArrastre(cont, o, pts, alCambiar, voz){
  var P = Plano(o), ultimo = pts.length - 1, arrastra = -1;
  cont.innerHTML = P.svg('<g class="capa"></g>', voz);
  var svg = cont.querySelector("svg"), capa = svg.querySelector(".capa"), NS = "http://www.w3.org/2000/svg", gs = [];
  svg.style.touchAction = "none";
  function aPlano(ev){ var pt = svg.createSVGPoint(); pt.x = ev.clientX; pt.y = ev.clientY; var q = pt.matrixTransform(svg.getScreenCTM().inverse()), c = P.desdePx(q.x, q.y);
    return [Math.max(P.xmin, Math.min(P.xmax, Math.round(c[0]))), Math.max(P.ymin, Math.min(P.ymax, Math.round(c[1])))]; }
  function voz1(p){ return T("Point ", "Punto ") + p.nombre + " " + par(p.x, p.y) + ". " + T("Move it with the arrow keys.", "Muévalo con las flechas."); }
  pts.forEach(function(p, i){
    var g = document.createElementNS(NS, "g"); g.setAttribute("tabindex", "0"); g.setAttribute("role", "button"); g.setAttribute("class", "punto-mov");
    g.innerHTML = '<circle r="16" fill="' + p.color + '" fill-opacity="0.15"/><circle r="8" fill="' + p.color + '" stroke="#fff" stroke-width="2.5"/><text x="12" y="-12" font-size="16" font-weight="700" fill="' + p.color + '" paint-order="stroke" stroke="#fff" stroke-width="4"></text>';
    g.style.cursor = "grab";
    g.addEventListener("pointerdown", function(ev){ arrastra = i; ultimo = i; g.setPointerCapture(ev.pointerId); ev.preventDefault(); });
    g.addEventListener("pointermove", function(ev){ if (arrastra !== i) return; var c = aPlano(ev); if (c[0] !== p.x || c[1] !== p.y){ p.x = c[0]; p.y = c[1]; pinta(); } });
    g.addEventListener("pointerup", function(){ arrastra = -1; });
    g.addEventListener("keydown", function(ev){
      var d = ev.shiftKey ? 5 : 1, k = ev.key;
      if (k === "ArrowLeft") p.x -= d; else if (k === "ArrowRight") p.x += d; else if (k === "ArrowUp") p.y += d; else if (k === "ArrowDown") p.y -= d; else return;
      ev.preventDefault(); ultimo = i;
      p.x = Math.max(P.xmin, Math.min(P.xmax, p.x)); p.y = Math.max(P.ymin, Math.min(P.ymax, p.y)); pinta();
    });
    svg.appendChild(g); gs.push(g);
  });
  svg.addEventListener("click", function(ev){ if (ev.target.closest && ev.target.closest(".punto-mov")) return; var c = aPlano(ev), p = pts[ultimo]; p.x = c[0]; p.y = c[1]; pinta(); });
  function pinta(){
    capa.innerHTML = alCambiar ? alCambiar(pts, P) : "";
    pts.forEach(function(p, i){
      gs[i].setAttribute("transform", "translate(" + P.X(p.x) + "," + P.Y(p.y) + ")");
      gs[i].querySelector("text").textContent = p.nombre + par(p.x, p.y);
      var izq = P.X(p.x) > P.W - 120; gs[i].querySelector("text").setAttribute("x", izq ? -12 : 12); gs[i].querySelector("text").setAttribute("text-anchor", izq ? "end" : "start");
      gs[i].setAttribute("aria-label", voz1(p));
    });
  }
  pinta();
  return {P: P, pts: pts, pinta: pinta};
}
/* Slope pieces */
function pendiente(a, b){ var dy = b[1] - a[1], dx = b[0] - a[0]; if (dx === 0) return null; return fr(dy, dx); }
function mHTML(m){ return m === null ? T("undefined", "indefinida") : fracHTML(m.n, m.d); }
function tipoM(m){ return m === null ? T("undefined", "indefinida") : (m.n === 0 ? T("zero", "cero") : (m.n > 0 ? T("positive", "positiva") : T("negative", "negativa"))); }
/* The whole line through a and b, clipped to the plane */
function rectaPor(P, a, b, color, ancho){
  if (a[0] === b[0] && a[1] === b[1]) return "";
  if (a[0] === b[0]) return P.seg([a[0], P.ymin], [a[0], P.ymax], color, ancho || 2.5);
  var m = (b[1] - a[1]) / (b[0] - a[0]), c = a[1] - m * a[0], l = [];
  [[P.xmin, m * P.xmin + c], [P.xmax, m * P.xmax + c]].forEach(function(p){ if (p[1] >= P.ymin - 1e-9 && p[1] <= P.ymax + 1e-9) l.push(p); });
  if (m !== 0) [[(P.ymin - c) / m, P.ymin], [(P.ymax - c) / m, P.ymax]].forEach(function(p){ if (p[0] > P.xmin && p[0] < P.xmax) l.push(p); });
  if (l.length < 2) return "";
  l.sort(function(u, v){ return u[0] - v[0]; });
  return P.seg(l[0], l[l.length - 1], color, ancho || 2.5);
}
/* Run (horizontal) and rise (vertical) triangle between a and b */
function trianguloPendiente(P, a, b){
  var c = [b[0], a[1]], s = "", dx = b[0] - a[0], dy = b[1] - a[1];
  if (dx) s += P.seg(a, c, "#1565c0", 3, "7 5") + P.texto([(a[0] + b[0]) / 2, a[1]], T("run ", "avance ") + sg(dx), "#1565c0", 14, "middle", 0, dy > 0 ? 16 : -14);
  if (dy) s += P.seg(c, b, "#c62828", 3, "7 5") + P.texto([b[0], (a[1] + b[1]) / 2], T("rise ", "elevación ") + sg(dy), "#c62828", 14, dx >= 0 ? "start" : "end", dx >= 0 ? 10 : -10, 0);
  return s;
}

/* ---------- Equations of a line (plain text with real minus signs; fractions as (2/3)x) ---------- */
function coefX(m, v){                       /* m is a fraction {n, d}; v the variable name */
  v = v || "x"; if (m.n === 0) return "0";
  var s = m.n < 0 ? "−" : "", a = Math.abs(m.n);
  if (m.d === 1) return s + (a === 1 ? "" : a) + v;
  return s + "(" + a + "/" + m.d + ")" + v;
}
function constTxt(b, primero){              /* + 3, − 3, or 3 when it comes first */
  if (primero) return fTxt(b);
  return (b.n < 0 ? " − " : " + ") + fTxt(fr(Math.abs(b.n), b.d));
}
function eqSI(m, b){ if (m.n === 0) return "y = " + fTxt(b); return "y = " + coefX(m) + (b.n === 0 ? "" : constTxt(b)); }
function restaTxt(v, k){ return k.n === 0 ? v : v + (k.n > 0 ? " − " : " + ") + fTxt(fr(Math.abs(k.n), k.d)); }
function eqPS(m, x1, y1){ var dentro = restaTxt("x", x1); return restaTxt("y", y1) + " = " + (m.d === 1 ? (m.n === 1 ? "" : m.n === -1 ? "−" : fTxt(m)) : "(" + fTxt(m) + ")") + (x1.n === 0 ? "x" : "(" + dentro + ")"); }
/* Standard form Ax + By = C from y = mx + b, with whole numbers and A > 0 (or B > 0 when A = 0) */
function estandar(m, b){
  var L = mcm(m.d, b.d), A = -m.n * L / m.d, B = L, C = b.n * L / b.d;
  if (A < 0 || (A === 0 && B < 0)){ A = -A; B = -B; C = -C; }
  var g = mcd(mcd(Math.abs(A), Math.abs(B)), Math.abs(C)) || 1;
  return {A: A / g, B: B / g, C: C / g};
}
function eqStd(e){
  var t = "";
  if (e.A !== 0) t = (e.A === 1 ? "" : e.A === -1 ? "−" : sg(e.A)) + "x";
  if (e.B !== 0) t += (t ? (e.B < 0 ? " − " : " + ") + (Math.abs(e.B) === 1 ? "" : Math.abs(e.B)) : (e.B === 1 ? "" : e.B === -1 ? "−" : sg(e.B))) + "y";
  return t + " = " + sg(e.C);
}
/* An equation written in plain text, read aloud well */
function eqHTML(txt){ return '<span class="eq" aria-hidden="true">' + txt + '</span><span class="sr-only">' + vozEq(txt) + "</span>"; }
function vozEq(txt){
  return txt.replace(/\((\d+)\/(\d+)\)/g, function(_, a, b){ return a + T(" over ", " sobre ") + b + T(" times ", " por "); }).replace(/(\d+)\/(\d+)/g, function(_, a, b){ return a + T(" over ", " sobre ") + b; })
    .replace(/−/g, T(" minus ", " menos ")).replace(/\+/g, T(" plus ", " más ")).replace(/=/g, T(" equals ", " es igual a ")).replace(/\s+/g, " ").trim();
}

/* Step-by-step widget: gen() returns {enun, pasos: [html], fin()} */
function pasoAPaso4(pre, gen){
  var caso, k;
  function nuevo(){ caso = gen(); k = 0; $(pre + "-enun").innerHTML = caso.enun; $(pre + "-pasos").innerHTML = ""; $(pre + "-sig").hidden = false; $(pre + "-todo").hidden = false; $(pre + "-nuevo").className = "btn-sec"; if (caso.inicio) caso.inicio(); }
  function uno(){ if (k >= caso.pasos.length) return; var d = document.createElement("div"); d.className = "paso4"; d.innerHTML = '<span class="nn" aria-hidden="true">' + (k === caso.pasos.length - 1 ? "✓" : k + 1) + "</span> " + caso.pasos[k]; $(pre + "-pasos").appendChild(d); k++;
    if (k >= caso.pasos.length){ var enfoque = document.activeElement === $(pre + "-sig") || document.activeElement === $(pre + "-todo"); $(pre + "-sig").hidden = true; $(pre + "-todo").hidden = true; $(pre + "-nuevo").className = "btn"; if (enfoque) $(pre + "-nuevo").focus(); if (caso.fin) caso.fin(); } }
  $(pre + "-sig").addEventListener("click", uno);
  $(pre + "-todo").addEventListener("click", function(){ while (k < caso.pasos.length) uno(); });
  $(pre + "-nuevo").addEventListener("click", nuevo);
  nuevo();
}

