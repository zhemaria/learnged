"""Level 3 · Topic 8 · Explore pages, imported from the repository interactivos and rebuilt for LearnGED
(English and Spanish, LearnGED styles, screen-reader text, 1 / 10 / 100 trials at a time):
  interactivos/prob_dados + prob_barajas + prob_rueda → math/level-3/explore-chance.html · es/matematicas/nivel-3/explorar-azar.html
  interactivos/caja_arbol                             → math/level-3/explore-tree.html   · es/matematicas/nivel-3/explorar-arbol.html
Run it before the lesson builders of Topic 8 (the lessons link to these pages)."""
import os
import bilingue as B
from bilingue import t
from es.traduce import Traductor
from build_n3_lesson_7_1 import ESTILO

B.NIVEL = 3
ROOT = B.ROOT
TEMA = ("Counting and probability", "Combinatoria y probabilidad")
SCRIPTS = ("/math/radicals.js", "/math/linear.js", "/math/inequalities.js", "/math/geometry3.js", "/math/data3.js", "/math/prob3.js")
ESTILO8 = ESTILO + """
  .sim-res{font-size:1.25rem;font-weight:700;text-align:center;min-height:1.6em;margin:8px 0;color:var(--tema-d);}
  .dados{display:flex;gap:18px;justify-content:center;margin:8px 0;}
  .tabla-sim{border-collapse:collapse;margin:10px auto;font-size:16px;}
  .tabla-sim caption{font-size:14px;color:var(--gris);padding-bottom:6px;}
  .tabla-sim th,.tabla-sim td{border:1px solid #c8c8c8;padding:5px 12px;text-align:center;}
  .tabla-sim th{background:var(--tema-bg);color:var(--tema-d);}
  .arbol-tabla{border-collapse:collapse;margin:10px auto;font-size:17px;}
  .arbol-tabla th,.arbol-tabla td{border:1px solid #c8c8c8;padding:8px 14px;text-align:center;}
  .arbol-tabla th{background:var(--tema-bg);color:var(--tema-d);}
  .arbol-tabla td.marca{background:#fff8e1;outline:3px solid #f9a825;}
  .arbol-tabla td[tabindex]{cursor:pointer;}
  .pasos-arbol{font-weight:700;color:var(--tema-d);}"""

# =====================================================================
# 1 · Chance experiments: two dice, a deck of cards, a spinner
# =====================================================================
JS_AZAR = r'''
/* Each experiment: outcome names, theoretical probabilities, a draw function, and a picture */
function barras(nombres, teo, exp, voz){
  var W = 640, H = 230, x0 = 46, x1 = 620, yb = 190, n = nombres.length, w = (x1 - x0) / n, mx = Math.max.apply(null, teo.concat(exp).concat([0.05])), tope = Math.ceil(mx * 20) / 20;
  function Y(p){ return yb - p * (yb - 16) / tope; }
  var s = '<svg class="geo-svg" viewBox="0 0 ' + W + " " + H + '" role="img" aria-label="' + voz + '">';
  for (var k = 0; k <= tope + 1e-9; k += 0.05) s += lineaG([x0, Y(k)], [x1, Y(k)], "#e0e0e0", 1) + textoA([x0 - 6, Y(k)], Math.round(k * 100) + "%", 12, "#424242", 400, "end");
  nombres.forEach(function(nm_, i){
    var x = x0 + i * w;
    s += '<rect x="' + f1(x + w * 0.12) + '" y="' + f1(Y(teo[i])) + '" width="' + f1(w * 0.36) + '" height="' + f1(yb - Y(teo[i])) + '" fill="#90a4ae"/>';
    s += '<rect x="' + f1(x + w * 0.5) + '" y="' + f1(Y(exp[i])) + '" width="' + f1(w * 0.36) + '" height="' + f1(yb - Y(exp[i])) + '" fill="#f9a825"/>';
    s += textoA([x + w / 2, yb + 16], nm_, 13, "#222", 700);
  });
  return s + lineaG([x0, yb], [x1, yb], "#424242", 2) + "</svg>";
}
function creaSim(pre, cfg){
  var E = {f: cfg.nombres.map(function(){ return 0; }), n: 0};
  function pinta(ultimo){
    var h = "<caption>" + T("Theoretical and experimental probability", "Probabilidad teórica y experimental") + '</caption><thead><tr><th scope="col">' + cfg.col + '</th><th scope="col">' + T("Times", "Veces") + '</th><th scope="col">' + T("Theoretical", "Teórica") + '</th><th scope="col">' + T("Experimental", "Experimental") + "</th></tr></thead><tbody>";
    var exp = E.f.map(function(x){ return E.n ? x / E.n : 0; });
    cfg.nombres.forEach(function(nm_, i){ h += "<tr><td>" + nm_ + "</td><td>" + E.f[i] + "</td><td>" + cfg.teoTxt[i] + " ≈ " + (cfg.teo[i] * 100).toFixed(1) + "%</td><td>" + (exp[i] * 100).toFixed(1) + "%</td></tr>"; });
    $(pre + "-tabla").innerHTML = h + "</tbody>";
    $(pre + "-graf").innerHTML = barras(cfg.corto || cfg.nombres, cfg.teo, exp, T("Bar graph: gray bars are the theoretical probabilities and yellow bars the experimental ones after " + E.n + " trials.", "Gráfica de barras: las grises son las probabilidades teóricas y las amarillas las experimentales después de " + E.n + " intentos."));
    $(pre + "-total").textContent = T("Total trials: ", "Total de intentos: ") + E.n;
    if (ultimo) $(pre + "-dibujo").innerHTML = cfg.dibujo(ultimo);
  }
  function corre(veces){
    var ult = null;
    for (var i = 0; i < veces; i++){ ult = cfg.saca(); E.f[ult.i]++; E.n++; }
    pinta(ult);
    $(pre + "-res").textContent = veces === 1 ? cfg.texto(ult) : T(veces + " more trials. The last one: ", veces + " intentos más. El último: ") + cfg.texto(ult);
  }
  [1, 10, 100].forEach(function(v){ $(pre + "-x" + v).addEventListener("click", function(){ corre(v); }); });
  $(pre + "-borrar").addEventListener("click", function(){ E.f = E.f.map(function(){ return 0; }); E.n = 0; $(pre + "-res").textContent = ""; pinta(null); });
  $(pre + "-dibujo").innerHTML = cfg.dibujo(null);
  pinta(null);
}
/* Two dice */
var PUNTOS = {1: [[0, 0]], 2: [[-1, -1], [1, 1]], 3: [[-1, -1], [0, 0], [1, 1]], 4: [[-1, -1], [1, -1], [-1, 1], [1, 1]], 5: [[-1, -1], [1, -1], [0, 0], [-1, 1], [1, 1]], 6: [[-1, -1], [1, -1], [-1, 0], [1, 0], [-1, 1], [1, 1]]};
function dado(v){ var s = '<svg width="90" height="90" viewBox="0 0 90 90" aria-hidden="true"><rect x="4" y="4" width="82" height="82" rx="14" fill="#fff" stroke="#37474f" stroke-width="3"/>'; (PUNTOS[v] || []).forEach(function(p){ s += '<circle cx="' + (45 + p[0] * 22) + '" cy="' + (45 + p[1] * 22) + '" r="7.5" fill="#263238"/>'; }); return s + "</svg>"; }
var SUMAS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], FORMAS = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1];
creaSim("dd", {col: T("Sum", "Suma"), nombres: SUMAS.map(String), teo: FORMAS.map(function(k){ return k / 36; }), teoTxt: FORMAS.map(function(k){ return k + "/36"; }),
  saca: function(){ var a = aleatorio(1, 6), b = aleatorio(1, 6); return {i: a + b - 2, a: a, b: b}; },
  texto: function(u){ return u.a + " + " + u.b + " = " + (u.a + u.b) + "."; },
  dibujo: function(u){ return '<div class="dados">' + dado(u ? u.a : 1) + dado(u ? u.b : 1) + "</div>"; }});
/* A deck of cards */
var PALOS = [{s: "♥", n: T("hearts", "corazones"), r: true}, {s: "♦", n: T("diamonds", "diamantes"), r: true}, {s: "♣", n: T("clubs", "tréboles"), r: false}, {s: "♠", n: T("spades", "picas"), r: false}];
var VALORES = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"];
function carta(u){
  if (!u) return '<svg width="110" height="150" viewBox="0 0 110 150" aria-hidden="true"><rect x="4" y="4" width="102" height="142" rx="10" fill="#1565c0" stroke="#0d47a1" stroke-width="3"/><rect x="16" y="16" width="78" height="118" rx="6" fill="none" stroke="#bbdefb" stroke-width="2"/></svg>';
  var p = PALOS[u.i], col = p.r ? "#c62828" : "#212121";
  return '<svg width="110" height="150" viewBox="0 0 110 150" aria-hidden="true"><rect x="4" y="4" width="102" height="142" rx="10" fill="#fff" stroke="#37474f" stroke-width="3"/><text x="16" y="30" font-size="20" font-weight="700" fill="' + col + '">' + u.v + '</text><text x="16" y="50" font-size="18" fill="' + col + '">' + p.s + '</text><text x="55" y="95" font-size="48" text-anchor="middle" fill="' + col + '">' + p.s + "</text></svg>";
}
creaSim("cb", {col: T("Suit", "Palo"), nombres: PALOS.map(function(p){ return p.s + " " + p.n; }), corto: PALOS.map(function(p){ return p.s; }), teo: [0.25, 0.25, 0.25, 0.25], teoTxt: ["13/52", "13/52", "13/52", "13/52"],
  saca: function(){ return {i: aleatorio(0, 3), v: elige(VALORES)}; },
  texto: function(u){ return T(u.v + " of " + PALOS[u.i].n + " (a " + (PALOS[u.i].r ? "red" : "black") + " card).", u.v + " de " + PALOS[u.i].n + " (carta " + (PALOS[u.i].r ? "roja" : "negra") + ")."); },
  dibujo: function(u){ return '<div class="dados">' + carta(u) + "</div>"; }});
/* A spinner with 6 equal parts */
var SECTORES = [{n: T("Red", "Rojo"), c: "#e53935"}, {n: T("Yellow", "Amarillo"), c: "#fdd835"}, {n: T("Green", "Verde"), c: "#43a047"}, {n: T("Teal", "Turquesa"), c: "#00acc1"}, {n: T("Blue", "Azul"), c: "#1e88e5"}, {n: T("Purple", "Morado"), c: "#8e24aa"}];
function ruleta(u){
  var s = '<svg width="200" height="200" viewBox="-100 -100 200 200" aria-hidden="true">', giro = u ? u.i * 60 + 30 : 30;
  SECTORES.forEach(function(sc, i){ var a1 = rad(90 - i * 60 + giro), a0 = a1 - rad(60); var p = [Math.cos(a1) * 88, -Math.sin(a1) * 88], q = [Math.cos(a0) * 88, -Math.sin(a0) * 88];
    s += '<path d="M0 0 L' + f1(p[0]) + " " + f1(p[1]) + " A88 88 0 0 1 " + f1(q[0]) + " " + f1(q[1]) + ' Z" fill="' + sc.c + '" stroke="#fff" stroke-width="2"/>'; });
  return s + '<circle r="8" fill="#263238"/><path d="M0 -98 L-10 -76 L10 -76 Z" fill="#263238"/></svg>';
}
creaSim("rl", {col: T("Color", "Color"), nombres: SECTORES.map(function(sc){ return sc.n; }), teo: [1, 1, 1, 1, 1, 1].map(function(){ return 1 / 6; }), teoTxt: ["1/6", "1/6", "1/6", "1/6", "1/6", "1/6"],
  saca: function(){ return {i: aleatorio(0, 5)}; },
  texto: function(u){ return T("The arrow landed on ", "La flecha cayó en ") + SECTORES[u.i].n.toLowerCase() + ".";},
  dibujo: function(u){ return '<div class="dados">' + ruleta(u) + "</div>"; }});
'''

def bloque_sim(pre, intro):
    return f'''      <p>{intro}</p>
      <div class="panel">
        <div id="{pre}-dibujo"></div>
        <p class="sim-res" id="{pre}-res" role="status" aria-live="polite"></p>
        <div class="fila-btn" style="justify-content:center;"><button type="button" class="btn" id="{pre}-x1">{t("1 time", "1 vez")}</button><button type="button" class="btn-sec" id="{pre}-x10">{t("10 times", "10 veces")}</button><button type="button" class="btn-sec" id="{pre}-x100">{t("100 times", "100 veces")}</button><button type="button" class="btn-sec" id="{pre}-borrar">{t("Start over", "Empezar de nuevo")}</button></div>
        <p class="nota" id="{pre}-total" style="text-align:center;"></p>
      </div>
      <div class="leyenda-geo" aria-hidden="true"><span><i style="background:#90a4ae"></i>{t("theoretical", "teórica")}</span><span><i style="background:#f9a825"></i>{t("experimental", "experimental")}</span></div>
      <div id="{pre}-graf"></div>
      <div class="tabla-scroll"><table class="tabla-sim" id="{pre}-tabla"></table></div>'''

def pagina_azar():
    mods = [
     (t("dice", "dados"), t("Two dice", "Dos dados"),
      bloque_sim("dd", t("Roll two dice and add them. There are 6 × 6 = 36 equally likely results, but the sums are not equally likely: 7 can happen in 6 ways (1 + 6, 2 + 5, …), while 2 can only happen as 1 + 1. Roll many times and watch the yellow bars get close to the gray ones.", "Se lanzan dos dados y se suman. Hay 6 × 6 = 36 resultados igual de probables, pero las sumas no lo son: el 7 sale de 6 formas (1 + 6, 2 + 5, …), mientras que el 2 solo sale con 1 + 1. Lance muchas veces y observe cómo las barras amarillas se acercan a las grises."))
      + f'''
      <div class="caja-tip">{t("<strong>Theoretical probability</strong> comes from the formula: favorable cases ÷ possible cases, such as P(7) = 6/36. <strong>Experimental probability</strong> comes from repeating the experiment: times it happened ÷ total trials. With more trials, the two get closer.", "La <strong>probabilidad teórica</strong> sale de la fórmula: casos favorables ÷ casos posibles, como P(7) = 6/36. La <strong>probabilidad experimental</strong> sale de repetir el experimento: veces que ocurrió ÷ total de intentos. Con más intentos, las dos se acercan.")}</div>'''),
     (t("cards", "baraja"), t("A deck of cards", "Una baraja"),
      bloque_sim("cb", t("Draw a card from a full deck of 52, look at it, and put it back. Each suit has 13 cards, so each one has a probability of 13/52 = 1/4. Half the cards (hearts and diamonds) are red.", "Se saca una carta de una baraja completa de 52, se mira y se devuelve. Cada palo tiene 13 cartas, así que cada uno tiene probabilidad 13/52 = 1/4. La mitad de las cartas (corazones y diamantes) son rojas."))),
     (t("spinner", "ruleta"), t("A spinner", "Una ruleta"),
      bloque_sim("rl", t("The spinner has 6 equal parts, so each color has a probability of 1/6. With only a few spins the results can look very uneven; with hundreds, they even out.", "La ruleta tiene 6 partes iguales, así que cada color tiene probabilidad 1/6. Con pocos giros los resultados pueden verse muy disparejos; con cientos, se emparejan.")))]
    return mods, JS_AZAR

# =====================================================================
# 2 · From the tree to the table (caja_arbol)
# =====================================================================
JS_ARBOL = r'''
var AR = {paso: 4};
var NOMBRE_C = {R: T("red", "roja"), A: T("blue", "azul")};
function fq(n, d){ var r = reduce(n, d); return r.q === 1 ? String(r.p) : r.p + "/" + r.q; }
function fqH(n, d){ var r = reduce(n, d); return fracHTML(r.p, r.q); }
function modelo(){
  var r = Math.max(1, Math.min(10, +$("ar-r").value || 1)), a = Math.max(1, Math.min(10, +$("ar-a").value || 1)), con = $("ar-con").checked, T0 = r + a, T2 = con ? T0 : T0 - 1;
  var c = {RR: [con ? r : r - 1, T2], RA: [a, T2], AR: [r, T2], AA: [con ? a : a - 1, T2]};
  var D = T0 * T2, num = {RR: r * c.RR[0], RA: r * a, AR: a * r, AA: a * c.AA[0]};
  return {r: r, a: a, con: con, T0: T0, T2: T2, c: c, D: D, num: num};
}
function svgFr(x, y, n, d, col){ return '<text x="' + x + '" y="' + (y - 3) + '" text-anchor="middle" font-size="15" font-weight="700" fill="' + col + '">' + n + '</text><line x1="' + (x - 14) + '" y1="' + y + '" x2="' + (x + 14) + '" y2="' + y + '" stroke="' + col + '" stroke-width="1.5"/><text x="' + x + '" y="' + (y + 15) + '" text-anchor="middle" font-size="15" font-weight="700" fill="' + col + '">' + d + "</text>"; }
function pintaAR(marca){
  var M = modelo(), p = AR.paso, CR = "#c62828", CA = "#1565c0", s = "";
  $("ar-modo").textContent = M.con ? T("With replacement: the ball goes back.", "Con reemplazo: la bola se devuelve.") : T("Without replacement: the ball stays out.", "Sin reemplazo: la bola no se devuelve.");
  var narr = [T("The jar has " + M.r + " red and " + M.a + " blue balls (" + M.T0 + " in all). We take out two, one after the other, and write down the colors.", "La urna tiene " + M.r + " bolas rojas y " + M.a + " azules (" + M.T0 + " en total). Se sacan dos, una tras otra, y se anotan los colores."),
    T("First draw. Each branch shows its probability: the balls of that color out of the total.", "Primera extracción. Cada rama muestra su probabilidad: las bolas de ese color entre el total."),
    M.con ? T("Second draw, with replacement: the ball goes back, the total stays " + M.T0 + ", and the draws are independent.", "Segunda extracción, con reemplazo: la bola se devuelve, el total sigue en " + M.T0 + " y las extracciones son independientes.") : T("Second draw, without replacement: the ball stays out, so the total drops to " + M.T2 + ", and the second draw depends on the first (dependent events).", "Segunda extracción, sin reemplazo: la bola no se devuelve, el total baja a " + M.T2 + " y la segunda depende de la primera (eventos dependientes)."),
    T("Multiplication rule: the probability of each path is the product of its two branches.", "Regla del producto: la probabilidad de cada camino es el producto de sus dos ramas."),
    T("Two-way table: the four results organized; together they add up to 1.", "Tabla de doble entrada: los cuatro resultados organizados; juntos suman 1.")];
  $("ar-paso").textContent = T("Step ", "Paso ") + (p + 1) + T(" of 5", " de 5");
  $("ar-narr").textContent = narr[p];
  /* jar */
  s += '<path d="M30 160 L110 160 L104 270 Q70 284 36 270 Z" fill="#fff8e1" stroke="#8d6e63" stroke-width="3"/>';
  for (var i = 0; i < M.T0; i++) s += '<circle cx="' + (46 + (i % 4) * 16) + '" cy="' + (180 + Math.floor(i / 4) * 17) + '" r="7" fill="' + (i < M.r ? CR : CA) + '"/>';
  var lados = {RR: [80, "R", "R"], RA: [175, "R", "A"], AR: [300, "A", "R"], AA: [395, "A", "A"]}, marcado = function(k){ return marca === k ? 6 : 3; };
  if (p >= 1){
    s += lineaG([130, 230], [300, 128], CR, marca && marca[0] === "R" ? 6 : 3) + lineaG([130, 230], [300, 348], CA, marca && marca[0] === "A" ? 6 : 3);
    s += svgFr(200, 160, M.r, M.T0, CR) + svgFr(200, 318, M.a, M.T0, CA);
    s += '<circle cx="315" cy="128" r="16" fill="' + CR + '"/><text x="315" y="134" text-anchor="middle" font-size="16" font-weight="700" fill="#fff">R</text><circle cx="315" cy="348" r="16" fill="' + CA + '"/><text x="315" y="354" text-anchor="middle" font-size="16" font-weight="700" fill="#fff">' + T("B", "A") + "</text>";
  }
  if (p >= 2){
    ["RR", "RA", "AR", "AA"].forEach(function(k){
      var y0 = k[0] === "R" ? 128 : 348, y = lados[k][0], col = k[1] === "R" ? CR : CA, mid = [(331 + 530) / 2, (y0 + y) / 2];
      s += lineaG([331, y0], [530, y], col, marcado(k)) + svgFr(mid[0], mid[1] + (y < y0 ? -22 : 30), M.c[k][0], M.c[k][1], col);
      s += '<circle cx="545" cy="' + y + '" r="15" fill="' + col + '"/><text x="545" y="' + (y + 6) + '" text-anchor="middle" font-size="15" font-weight="700" fill="#fff">' + (k[1] === "R" ? "R" : T("B", "A")) + "</text>";
    });
  }
  if (p >= 3){
    ["RR", "RA", "AR", "AA"].forEach(function(k){ var y = lados[k][0], r = reduce(M.num[k], M.D);
      s += textoA([640, y - 18], (k[0] === "R" ? "R" : T("B", "A")) + (k[1] === "R" ? "R" : T("B", "A")), 13, "#424242", 700) + svgFr(640, y + 2, r.p, r.q, "#1b5e20") + textoA([640, y + 30], "≈ " + (M.num[k] / M.D).toFixed(3), 12, "#424242", 400); });
  }
  var voz = T("Tree diagram. Jar with " + M.r + " red and " + M.a + " blue balls. ", "Diagrama de árbol. Urna con " + M.r + " rojas y " + M.a + " azules. ") + (p >= 1 ? T("First draw: red " + M.r + "/" + M.T0 + ", blue " + M.a + "/" + M.T0 + ". ", "Primera: roja " + M.r + "/" + M.T0 + ", azul " + M.a + "/" + M.T0 + ". ") : "") +
    (p >= 2 ? T("Second draw after red: red " + M.c.RR[0] + "/" + M.T2 + ", blue " + M.c.RA[0] + "/" + M.T2 + "; after blue: red " + M.c.AR[0] + "/" + M.T2 + ", blue " + M.c.AA[0] + "/" + M.T2 + ". ", "Segunda después de roja: roja " + M.c.RR[0] + "/" + M.T2 + ", azul " + M.c.RA[0] + "/" + M.T2 + "; después de azul: roja " + M.c.AR[0] + "/" + M.T2 + ", azul " + M.c.AA[0] + "/" + M.T2 + ". ") : "");
  $("ar-svg").innerHTML = '<svg class="geo-svg" viewBox="0 0 700 440" role="img" aria-label="' + voz + '">' + s + "</svg>";
  /* table */
  if (p >= 4){
    var celda = function(k){ return '<td tabindex="0" role="button" data-k="' + k + '"' + (marca === k ? ' class="marca"' : "") + ' aria-label="' + T("First " + NOMBRE_C[k[0]] + ", second " + NOMBRE_C[k[1]] + ": ", "Primera " + NOMBRE_C[k[0]] + ", segunda " + NOMBRE_C[k[1]] + ": ") + fq(M.num[k], M.D) + '">' + fqH(M.num[k], M.D) + "</td>"; };
    $("ar-tabla").innerHTML = '<table class="arbol-tabla"><caption class="sr-only">' + T("Two-way table of the two draws", "Tabla de doble entrada de las dos extracciones") + '</caption><thead><tr><th scope="col"></th><th scope="col">' + T("2nd red", "2.ª roja") + '</th><th scope="col">' + T("2nd blue", "2.ª azul") + '</th><th scope="col">Total</th></tr></thead><tbody>' +
      '<tr><th scope="row">' + T("1st red", "1.ª roja") + "</th>" + celda("RR") + celda("RA") + "<td>" + fqH(M.r, M.T0) + "</td></tr>" +
      '<tr><th scope="row">' + T("1st blue", "1.ª azul") + "</th>" + celda("AR") + celda("AA") + "<td>" + fqH(M.a, M.T0) + "</td></tr>" +
      '<tr><th scope="row">Total</th><td>' + fqH(M.num.RR + M.num.AR, M.D) + "</td><td>" + fqH(M.num.RA + M.num.AA, M.D) + "</td><td>1</td></tr></tbody></table>";
    Array.prototype.forEach.call($("ar-tabla").querySelectorAll("td[data-k]"), function(td){
      function elige_(){ pintaAR(td.getAttribute("data-k")); var f = $("ar-tabla").querySelector('td[data-k="' + td.getAttribute("data-k") + '"]'); if (f) f.focus(); }
      td.addEventListener("click", elige_); td.addEventListener("keydown", function(ev){ if (ev.key === "Enter" || ev.key === " "){ ev.preventDefault(); elige_(); } });
    });
    var mismo = M.num.RR + M.num.AA, dist = M.num.RA + M.num.AR, alMenos = M.D - M.num.AA;
    $("ar-deriv").innerHTML = '<div class="linea">' + T("Same color (RR or BB): ", "Mismo color (RR o AA): ") + fqH(mismo, M.D) + " ≈ " + (mismo / M.D).toFixed(3) + "</div>" +
      '<div class="linea">' + T("Different colors (RB or BR): ", "Colores distintos (RA o AR): ") + fqH(dist, M.D) + " ≈ " + (dist / M.D).toFixed(3) + "</div>" +
      '<div class="linea">' + T("At least one red (1 − P(BB)): ", "Al menos una roja (1 − P(AA)): ") + fqH(alMenos, M.D) + " ≈ " + (alMenos / M.D).toFixed(3) + "</div>" +
      '<div class="linea veredicto">' + T("Check: the four paths add up to ", "Comprobación: los cuatro caminos suman ") + M.num.RR + " + " + M.num.RA + " + " + M.num.AR + " + " + M.num.AA + " = " + M.D + "/" + M.D + " = 1 ✓</div>" +
      (marca ? '<div class="linea">' + T("Path ", "Camino ") + NOMBRE_C[marca[0]] + " → " + NOMBRE_C[marca[1]] + ": " + fqH(marca[0] === "R" ? M.r : M.a, M.T0) + " × " + fqH(M.c[marca][0], M.c[marca][1]) + " = " + fqH(M.num[marca], M.D) + "</div>" : "");
  } else { $("ar-tabla").innerHTML = '<p class="nota">' + T("The table fills in at step 5. Go through the steps or press “Show all”.", "La tabla se completa en el paso 5. Avance los pasos o pulse «Ver todo».") + "</p>"; $("ar-deriv").innerHTML = ""; }
  $("ar-ant").disabled = p === 0; $("ar-sig").disabled = p === 4;
}
$("ar-ant").addEventListener("click", function(){ if (AR.paso > 0){ AR.paso--; pintaAR(); } });
$("ar-sig").addEventListener("click", function(){ if (AR.paso < 4){ AR.paso++; pintaAR(); } });
$("ar-todo").addEventListener("click", function(){ AR.paso = 4; pintaAR(); });
$("ar-cero").addEventListener("click", function(){ AR.paso = 0; pintaAR(); });
["ar-r", "ar-a"].forEach(function(id){ $(id).addEventListener("input", function(){ pintaAR(); }); });
$("ar-con").addEventListener("change", function(){ pintaAR(); });
pintaAR();
'''

def pagina_arbol():
    mods = [
     (t("tree", "arbol"), t("From the tree to the table", "Del árbol a la tabla"),
      f'''      <p>{t("Two balls are taken out of a jar, one after the other. Build the tree diagram step by step and see how each path becomes a cell of the two-way table. Choose a cell of the table to highlight its path on the tree.", "Se sacan dos bolas de una urna, una tras otra. Construya el diagrama de árbol paso a paso y vea cómo cada camino pasa a una celda de la tabla de doble entrada. Elija una celda de la tabla para resaltar su camino en el árbol.")}</p>
      <div class="panel"><div class="campos">
        <div class="campo"><label for="ar-r">{t("Red balls", "Bolas rojas")}</label><input type="number" id="ar-r" min="1" max="10" value="4"></div>
        <div class="campo"><label for="ar-a">{t("Blue balls", "Bolas azules")}</label><input type="number" id="ar-a" min="1" max="10" value="3"></div>
        <label class="casilla" style="align-self:flex-end;"><input type="checkbox" id="ar-con"> {t("With replacement", "Con reemplazo")}</label></div>
        <p class="nota" id="ar-modo"></p>
        <div class="fila-btn"><button type="button" class="btn-sec" id="ar-ant">{t("◀ Back", "◀ Anterior")}</button><button type="button" class="btn" id="ar-sig">{t("Next step ▶", "Siguiente paso ▶")}</button><button type="button" class="btn-sec" id="ar-todo">{t("Show all", "Ver todo")}</button><button type="button" class="btn-sec" id="ar-cero">{t("↺ Start over", "↺ Empezar de nuevo")}</button></div>
        <p class="pasos-arbol" id="ar-paso"></p>
        <p id="ar-narr" aria-live="polite"></p></div>
      <div class="leyenda-geo" aria-hidden="true"><span><i style="background:#c62828"></i>{t("R = red ball", "R = bola roja")}</span><span><i style="background:#1565c0"></i>{t("B = blue ball", "A = bola azul")}</span></div>
      <div class="tabla-scroll" id="ar-svg"></div>
      <h3>{t("Two-way table", "Tabla de doble entrada")}</h3>
      <div class="tabla-scroll" id="ar-tabla"></div>
      <h3>{t("Results and check", "Resultados derivados y comprobación")}</h3>
      <div class="salida" id="ar-deriv" aria-live="polite"></div>
      <div class="caja-tip">{t("<strong>To check a tree:</strong> add the probabilities of all the paths. If they do not add up to 1, a branch is wrong.", "<strong>Para comprobar un árbol:</strong> sume las probabilidades de todos los caminos. Si no da 1, hay una rama mal calculada.")}</div>''')]
    return mods, JS_ARBOL

PAGINAS = [
 ("8-2", "explore-chance", "explorar-azar", pagina_azar, ("Explore: chance experiments", "Explorar: experimentos de azar"), ("Chance experiments: dice, cards, and a spinner", "Experimentos de azar: dados, baraja y ruleta")),
 ("8-2", "explore-tree", "explorar-arbol", pagina_arbol, ("Explore: from the tree to the table", "Explorar: del árbol a la tabla"), ("From the tree to the table", "Del árbol a la tabla")),
]

def construye():
    for n, en, es, hacer, tit, corto in PAGINAS:
        num = n.replace("-", ".")
        html = {}
        for lang in ("en", "es"):
            B.L = lang
            mods, js = hacer()
            meta = t("An interactive activity to explore what you learned in Lesson " + num + ". It goes with the lesson and its practice page.", "Una actividad interactiva para explorar lo aprendido en la Lección " + num + ". Acompaña a la lección y a su página de práctica.")
            s = B.pagina_practica(n, 8, t(*TEMA), t(*corto), meta, mods, js, estilo=ESTILO8, scripts=SCRIPTS)
            s = s.replace(f'<h1>{t("Lesson", "Lección")} {num} · {t(*corto)}</h1>', f'<h1>{t(*tit)}</h1>')
            s = s.replace(f'<title>{t("Practice · Lesson", "Práctica · Lección")} {num} · ', f'<title>{t("Explore", "Explorar")} · {t("Lesson", "Lección")} {num} · ')
            s = s.replace('<a class="lg-link" href="./">Math · Level 3 lessons</a>', f'<a class="lg-link" href="{t("lesson-" + n, "leccion-" + n)}.html">{t("← Back to Lesson " + num, "← Volver a la Lección " + num)}</a>')
            s = s.replace("practice (English) — built by", "explore page (English) — built by")
            html[lang] = s
        B.L = "en"
        ruta_en = f"math/level-3/{en}.html"
        open(os.path.join(ROOT, ruta_en), "w", encoding="utf-8").write(html["en"]); print("ok", ruta_en)
        tr = Traductor(ruta_en, texto=html["es"], nivel=3); tr.frecuentes()
        tr.cabecera(f"<!-- LearnGED · Nivel 3 · Lección {num} · {corto[1]} — página para explorar (español) — construida con tools/build_n3_explora_8.py\n     José M. Fernández · CC BY-NC-SA 4.0 -->")
        ruta_es = f"es/matematicas/nivel-3/{es}.html"
        tr.guarda(ruta_es)
        s = open(os.path.join(ROOT, ruta_es), encoding="utf-8").read()
        for frase in ["New exercise", "Back to contents", "On this page", "Open all", "Check<"]:
            if frase in s: print("  ¡OJO! queda en inglés en", ruta_es, ":", frase)

if __name__ == "__main__":
    construye()
