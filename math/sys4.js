/* LearnGED · Level 4 · Topic 6 — systems of two linear equations.
   Loaded after coord4.js (Plano, rectaPor, sg, par). A line is {a, b, c}: ax + by = c, with whole numbers.
   Optional vis: how the equation is shown (for example "y = 2x + 1"). */

function L3(a, b, c, vis){ return {a: a, b: b, c: c, vis: vis}; }
function terminoXY(k, v, primero){ if (!k) return ""; var a = Math.abs(k), cuerpo = (a === 1 ? "" : a) + v; return (k < 0 ? (primero ? "−" : " − ") : (primero ? "" : " + ")) + cuerpo; }
/* ax + by = c as text (vx, vy: names of the variables) */
function ecTxt(L, vx, vy){ if (L.vis) return L.vis; vx = vx || "x"; vy = vy || "y"; var s = terminoXY(L.a, vx, true); s += terminoXY(L.b, vy, !s); return (s || "0") + " = " + sg(L.c); }
function ecVozXY(txt){ return txt.replace(/−/g, T(" minus ", " menos ")).replace(/\+/g, T(" plus ", " más ")).replace(/=/g, T(" equals ", " es igual a ")).replace(/·/g, T(" times ", " por ")); }
function ecH(L, vx, vy){ var s = ecTxt(L, vx, vy); return envuelve(s, ecVozXY(s)); }
/* The system with a brace, one equation per line */
function sisHTML(L1, L2, vx, vy){ var a = ecTxt(L1, vx, vy), b = ecTxt(L2, vx, vy);
  return '<span class="sistema" aria-hidden="true"><span class="llave">{</span><span class="ecs"><span>' + a + "</span><span>" + b + '</span></span></span><span class="sr-only">' + T("The system: ", "El sistema: ") + ecVozXY(a) + T("; and ", "; y ") + ecVozXY(b) + "</span>"; }
function valL(L, x, y){ return L.a * x + L.b * y; }
function cumple(L, x, y){ return Math.abs(valL(L, x, y) - L.c) < 1e-9; }
/* Solve: {tipo: "uno" | "ninguna" | "infinitas", x, y} */
function resuelveSis(L1, L2){
  var D = L1.a * L2.b - L2.a * L1.b;
  if (D !== 0) return {tipo: "uno", x: (L1.c * L2.b - L2.c * L1.b) / D, y: (L1.a * L2.c - L2.a * L1.c) / D};
  var prop = (L1.a * L2.c - L2.a * L1.c === 0) && (L1.b * L2.c - L2.b * L1.c === 0);
  return {tipo: prop ? "infinitas" : "ninguna"};
}
/* A system with a chosen whole-number solution (x0, y0); coefficients from -lim..lim. forma: "std" | "y" (y = mx + b) | "x" (x = y + k) */
function sisCon(x0, y0, opciones){
  opciones = opciones || {}; var lim = opciones.lim || 5, L1, L2, k = 0;
  function una(forma){ var a, b;
    if (forma === "y"){ var m = elige([-3, -2, -1, 1, 2, 3, 4]), bb = y0 - m * x0; return L3(-m, 1, bb, "y = " + terminoXY(m, "x", true) + (bb ? (bb < 0 ? " − " + -bb : " + " + bb) : "")); }
    if (forma === "x"){ var mm = elige([-2, -1, 1, 2, 3]), kk = x0 - mm * y0; return L3(1, -mm, kk, "x = " + terminoXY(mm, "y", true) + (kk ? (kk < 0 ? " − " + -kk : " + " + kk) : "")); }
    if (forma === "uno"){ a = elige([1, 1, 2, 3, -1]); b = elige([1, -1]); if (Math.random() < .5){ var tmp = a; a = b; b = tmp; } return L3(a, b, a * x0 + b * y0); }
    var g0 = function(u, v){ u = Math.abs(u); v = Math.abs(v); while (v){ var w = u % v; u = v; v = w; } return u; };
    do { a = aleatorio(-lim, lim); b = aleatorio(-lim, lim); } while (!a || !b || g0(g0(a, b), a * x0 + b * y0) > 1 || (a < 0 && b < 0)); return L3(a, b, a * x0 + b * y0); }
  do { L1 = una(opciones.f1 || "std"); L2 = una(opciones.f2 || "std"); k++; } while ((L1.a * L2.b - L2.a * L1.b === 0 || (L1.a === L2.a && L1.b === L2.b)) && k < 200);
  return [L1, L2];
}
/* Two points on the line, for drawing */
function puntosL(L){ if (!L.b) return [[L.c / L.a, -50], [L.c / L.a, 50]]; return [[-50, (L.c + 50 * L.a) / L.b], [50, (L.c - 50 * L.a) / L.b]]; }
/* The graph of the system: two lines, their names, and the crossing point. o: {rango, u, sinPunto, punto: [x, y] to mark, etiquetas: [t1, t2]} */
var COL_SIS = ["#1565c0", "#c62828"];
function grafSis(L1, L2, o){
  o = o || {}; var r = o.rango || 8, P = Plano({xmin: -r, xmax: r, ymin: -r, ymax: r, u: o.u || Math.floor(440 / (2 * r)), paso: r > 10 ? 5 : 2}), s = "";
  [L1, L2].forEach(function(L, i){ var p = puntosL(L); s += rectaPor(P, p[0], p[1], COL_SIS[i], 3.5); });
  /* names of the lines, near the right edge where each one is inside the plane */
  var sol0 = resuelveSis(L1, L2), usados = [];
  [L1, L2].forEach(function(L, i){ var x, y, ok = false, otra = i ? L1 : L2, largo = ecTxt(L).length * .32, m0 = L.b ? -L.a / L.b : 0,
    lejos = function(px, py){ var ly = py + (m0 >= 0 ? .55 : -.75), libre = true;
      for (var xs = px - largo; xs <= px; xs += .25){ var yo = otra.b ? (otra.c - otra.a * xs) / otra.b : null; if (yo === null ? Math.abs(xs - otra.c / otra.a) < .3 : Math.abs(yo - ly) < .7) libre = false; }
      if (px - largo < .4 && px > -.4) libre = false;
      return libre && (sol0.tipo !== "uno" || Math.hypot(px - sol0.x, py - sol0.y) > 2.5) && usados.every(function(u){ return Math.abs(u[1] - py) > 1.4 || Math.abs(u[0] - px) > 5; }); };
    for (var pasada = 0; pasada < 2 && !ok; pasada++) for (x = r - 1.2; x > -r + 3; x -= .5){ y = L.b ? (L.c - L.a * x) / L.b : null; if (y !== null && y > -r + .8 && y < r - .8 && (pasada || (Math.abs(y) > 1.3 && Math.abs(x) > 1 && lejos(x, y)))){ ok = true; break; } }
    if (ok) usados.push([x, y]);
    if (!L.b){ x = L.c / L.a; y = r - 1.5 - i * 1.2; ok = Math.abs(x) < r; }
    var m = L.b ? -L.a / L.b : 0, dy = !L.b ? 0 : m >= 0 ? -10 : 20, dx = L.b ? -6 : 8;
    if (ok) s += '<text x="' + (P.X(x) + dx).toFixed(1) + '" y="' + (P.Y(y) + dy).toFixed(1) + '" font-size="14" font-weight="700" fill="' + COL_SIS[i] + '" text-anchor="' + (L.b ? "end" : "start") + '" paint-order="stroke" stroke="#fff" stroke-width="4">' + (o.etiquetas ? o.etiquetas[i] : ecTxt(L)) + "</text>"; });
  var sol = resuelveSis(L1, L2);
  /* a point with its label on the side farthest from both lines */
  function puntoLibre(p, color){
    var best = null, bd = -1, txt = par(p[0], p[1]), w = txt.length * 8.6 / P.u, h = 13 / P.u, g = 11 / P.u;
    /* candidate centres of the label box: right, left, above, below and the four diagonals */
    [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, 1], [1, -1], [-1, -1]].forEach(function(d){
      var cx = p[0] + d[0] * (w / 2 + g), cy = p[1] + d[1] * (h / 2 + g), dmin = 99;
      if (Math.abs(cx) + w / 2 > r - .2 || Math.abs(cy) + h / 2 > r - .2) return;
      for (var ix = -1; ix <= 1; ix += .5) for (var iy = -1; iy <= 1; iy++){ var xx = cx + ix * w / 2, yy = cy + iy * h / 2;
        [L1, L2].forEach(function(L){ dmin = Math.min(dmin, Math.abs(L.a * xx + L.b * yy - L.c) / Math.hypot(L.a, L.b)); });
        dmin = Math.min(dmin, Math.abs(yy) + .15, Math.abs(xx) + .15); }
      if (dmin > bd + 1e-9){ bd = dmin; best = [cx, cy]; } });
    var q = '<circle cx="' + P.X(p[0]).toFixed(1) + '" cy="' + P.Y(p[1]).toFixed(1) + '" r="7" fill="' + color + '" stroke="#fff" stroke-width="2"/>';
    if (best) q += '<text x="' + P.X(best[0]).toFixed(1) + '" y="' + (P.Y(best[1]) + 5).toFixed(1) + '" font-size="15" font-weight="700" fill="' + color + '" text-anchor="middle" paint-order="stroke" stroke="#fff" stroke-width="4">' + txt + "</text>";
    return q; }
  if (!o.sinPunto && sol.tipo === "uno" && Math.abs(sol.x) <= r && Math.abs(sol.y) <= r) s += puntoLibre([sol.x, sol.y], "#2e7d32");
  if (o.punto && Math.abs(o.punto[0]) <= r && Math.abs(o.punto[1]) <= r) s += puntoLibre(o.punto, "#6a1b9a");
  var voz = T("Graph of the lines ", "Gráfica de las rectas ") + ecVozXY(ecTxt(L1)) + T(" and ", " y ") + ecVozXY(ecTxt(L2)) + ". " + (sol.tipo === "uno" ? T("They cross at ", "Se cruzan en ") + parVoz(sol.x, sol.y) : sol.tipo === "ninguna" ? T("They are parallel.", "Son paralelas.") : T("They are the same line.", "Son la misma recta.")) + (o.punto ? ". " + T("The point checked is ", "El punto que se verifica es ") + parVoz(o.punto[0], o.punto[1]) : "") + ".";
  return P.svg(s, voz, o.ancho || 460);
}
/* What a wrong pair tells: swapped, solves only one equation, or neither */
function diagSis(L1, L2, sol){ return function(x, y){
  if (x === sol.y && y === sol.x && x !== y) return T("You swapped x and y: write the x value first.", "Intercambió x e y: escriba primero el valor de x.");
  var c1 = cumple(L1, x, y), c2 = cumple(L2, x, y);
  if (c1 && !c2) return T("Your pair works in the first equation but not in the second. Check it in both.", "Su par cumple la primera ecuación pero no la segunda. Verifíquelo en las dos.");
  if (c2 && !c1) return T("Your pair works in the second equation but not in the first. Check it in both.", "Su par cumple la segunda ecuación pero no la primera. Verifíquelo en las dos.");
  return T("Your pair does not work in either equation. Substitute carefully, with parentheses.", "Su par no cumple ninguna de las dos ecuaciones. Sustituya con cuidado, usando paréntesis.");
}; }
/* A substitution written out: 3(2) + (5) = 11 */
function sustTxt(L, x, y, vx, vy){ var s = "", primero = true;
  [[L.a, x], [L.b, y]].forEach(function(p){ if (!p[0]) return; var k = p[0], v = "(" + sg(p[1]) + ")"; s += (primero ? (k < 0 ? "−" : "") : (k < 0 ? " − " : " + ")) + (Math.abs(k) === 1 ? "" : Math.abs(k)) + v; primero = false; });
  return s + " = " + sg(valL(L, x, y)); }
var ESTILO_SIS = "";
