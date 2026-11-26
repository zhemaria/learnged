/* LearnGED · Level 4 · Topic 7, Lessons 7.2 and 7.3 — functions: graphs, evaluating f(x) step by step, domain and range,
   composition, and the average rate of change. Loaded after coord4.js (Plano, sg, par) and poly4.js (polynomials as coefficient
   lists: pVis, pEval, pMul, pSuma, pEsc). */

var COL_F = ["#1565c0", "#c62828", "#6a1b9a", "#ef6c00"];
function nf(v){ var r = Math.round(v * 100) / 100; return sg(Object.is(r, -0) ? 0 : r); }   /* number with at most 2 decimals */

/* Samples a curve x → y on [x0, x1]; returns a list of pieces (breaks where y is not a number or jumps off the plane) */
function muestrea(f, x0, x1, y0, y1, n){
  n = n || 240; var piezas = [], cur = [], lim = (y1 - y0) * 3;
  for (var i = 0; i <= n; i++){ var x = x0 + (x1 - x0) * i / n, y = f(x);
    if (typeof y !== "number" || !isFinite(y) || y < y0 - lim || y > y1 + lim || (cur.length && Math.abs(y - cur[cur.length - 1][1]) > (y1 - y0))){ if (cur.length > 1) piezas.push(cur); cur = []; if (typeof y === "number" && isFinite(y) && y >= y0 - lim && y <= y1 + lim) cur.push([x, y]); continue; }
    cur.push([x, y]); }
  if (cur.length > 1) piezas.push(cur);
  return piezas;
}
/* Graph: o.rango {x0, x1, y0, y1}; o.curvas [{f | piezas, color, raya}]; o.puntos [[x, y, color, label]];
   o.vertical x (a dashed vertical line); o.segmentos [[a, b, color, raya]]; o.dominio [a, b] / o.rangoY [c, d] (bands on the axes);
   o.voz (spoken text); o.ancho; o.paso */
function grafFun(o){
  var R = o.rango || {x0: -7, x1: 7, y0: -7, y1: 7}, sx = R.x1 - R.x0, sy = R.y1 - R.y0, span = Math.max(sx, sy), P;
  if (sy > 1.3 * sx){ /* a tall graph: its own scale on the y-axis */
    var u = Math.floor(440 / sx), uy = Math.min(u, 380 / sy), py = sy > 60 ? 10 : sy > 24 ? 5 : 2;
    P = Plano({xmin: R.x0, xmax: R.x1, ymin: R.y0, ymax: R.y1, u: u, uy: uy, paso: o.paso || (sx > 14 ? 2 : 1), pasoY: py});
  } else P = Plano({xmin: R.x0, xmax: R.x1, ymin: R.y0, ymax: R.y1, u: o.u || Math.floor(440 / span), paso: o.paso || (span > 30 ? 5 : span > 14 ? 2 : 1)});
  var s = "";
  var clip = "cf" + Math.floor(Math.random() * 1e9);
  s += '<defs><clipPath id="' + clip + '"><rect x="' + P.X(R.x0) + '" y="' + P.Y(R.y1) + '" width="' + (P.X(R.x1) - P.X(R.x0)) + '" height="' + (P.Y(R.y0) - P.Y(R.y1)) + '"/></clipPath></defs>';
  var cuerpo = "";
  var lista = function(v){ return v ? (typeof v[0] === "number" ? [v] : v) : []; };
  lista(o.dominio).forEach(function(d){ cuerpo += '<rect x="' + P.X(d[0]).toFixed(1) + '" y="' + (P.Y(Math.max(R.y0, Math.min(0, R.y1))) - 5).toFixed(1) + '" width="' + (P.X(d[1]) - P.X(d[0])).toFixed(1) + '" height="10" rx="5" fill="#ef6c00" fill-opacity=".45"/>'; });
  lista(o.rangoY).forEach(function(d){ cuerpo += '<rect x="' + (P.X(Math.max(R.x0, Math.min(0, R.x1))) - 5).toFixed(1) + '" y="' + P.Y(d[1]).toFixed(1) + '" width="10" height="' + (P.Y(d[0]) - P.Y(d[1])).toFixed(1) + '" rx="5" fill="#6a1b9a" fill-opacity=".45"/>'; });
  (o.curvas || []).forEach(function(c, i){
    var piezas = c.piezas || muestrea(c.f, R.x0, R.x1, R.y0, R.y1);
    piezas.forEach(function(pz){ cuerpo += '<polyline points="' + pz.map(function(p){ return P.X(p[0]).toFixed(1) + "," + P.Y(p[1]).toFixed(1); }).join(" ") + '" fill="none" stroke="' + (c.color || COL_F[i % 4]) + '" stroke-width="3.5" stroke-linejoin="round" stroke-linecap="round"' + (c.raya ? ' stroke-dasharray="' + c.raya + '"' : "") + "/>"; });
  });
  (o.segmentos || []).forEach(function(g){ cuerpo += P.seg(g[0], g[1], g[2] || "#455a64", g[4] || 2.5, g[3] || null); });
  if (o.vertical !== undefined && o.vertical !== null) cuerpo += P.seg([o.vertical, R.y0], [o.vertical, R.y1], "#ef6c00", 3, "8 6");
  s += '<g clip-path="url(#' + clip + ')">' + cuerpo + "</g>";
  (o.puntos || []).forEach(function(p){
    s += '<circle cx="' + P.X(p[0]).toFixed(1) + '" cy="' + P.Y(p[1]).toFixed(1) + '" r="' + (p[4] || 6.5) + '" fill="' + (p[2] || "#2e7d32") + '" stroke="#fff" stroke-width="2"/>';
    if (p[3]){ var der = p[6] !== undefined ? p[6] : p[0] < (R.x0 + R.x1) / 2 + (R.x1 - R.x0) * .2, arr = p[5] !== undefined ? p[5] : true;
      s += '<text x="' + (P.X(p[0]) + (der ? 11 : -11)).toFixed(1) + '" y="' + (P.Y(p[1]) + (arr ? -11 : 21)).toFixed(1) + '" font-size="14" font-weight="700" fill="' + (p[2] || "#2e7d32") + '" text-anchor="' + (der ? "start" : "end") + '" paint-order="stroke" stroke="#fff" stroke-width="4">' + p[3] + "</text>"; }
  });
  (o.textos || []).forEach(function(tx){ s += P.texto([tx[0], tx[1]], tx[2], tx[3] || "#263238", tx[4] || 14, tx[5] || "middle", tx[6] || 0, tx[7] || 0); });
  return P.svg(s, o.voz || T("Graph on the coordinate plane.", "Gráfica en el plano cartesiano."), o.ancho || 460);
}

/* ---------- Evaluating a polynomial step by step ---------- */
var SUPF = {2: "²", 3: "³"};
/* substitution text: 2(−3)² − 3(−3) + 1 */
function sustP(p, a){
  var l = []; for (var g = p.length - 1; g >= 0; g--) if (p[g]) l.push([p[g], g]);
  if (!l.length) return "0";
  return l.map(function(t, i){ var c = t[0], g = t[1], ab = Math.abs(c), cuerpo;
    cuerpo = g === 0 ? String(ab) : (ab === 1 ? "" : ab) + "(" + sg(a) + ")" + (g > 1 ? SUPF[g] : "");
    return (i === 0 ? (c < 0 ? "−" : "") : (c < 0 ? " − " : " + ")) + cuerpo; }).join("");
}
/* the terms already worked out: 2(9) − 3(−3) + 1 → 18 + 9 + 1 */
function terminosP(p, a){
  var l = []; for (var g = p.length - 1; g >= 0; g--) if (p[g] && p[g] * Math.pow(a, g)) l.push(p[g] * Math.pow(a, g));
  if (!l.length) return "0";
  return l.map(function(v, i){ return i === 0 ? nf(v) : (v < 0 ? " − " + nf(-v) : " + " + nf(v)); }).join("");
}
/* Steps to evaluate f(a) for a polynomial f */
function pasosEval(p, a, nombre){
  nombre = nombre || "f"; var res = pEval(p, a), st = [], s1 = sustP(p, a), cuad = p.length > 2;
  st.push(T("Put the input in parentheses in place of x: ", "Se sustituye la entrada entre paréntesis en lugar de x: ") + nombre + "(" + sg(a) + ") = " + s1 + ".");
  if (cuad){ var potencias = []; for (var g = p.length - 1; g >= 2; g--) if (p[g]) potencias.push("(" + sg(a) + ")" + SUPF[g] + " = " + nf(Math.pow(a, g)));
    st.push(T("Powers first (PEMDAS): ", "Primero las potencias (PEMDAS): ") + potencias.join("; ") + "." + (a < 0 ? T(" The square of a negative number is positive.", " El cuadrado de un número negativo es positivo.") : "")); }
  var tt = terminosP(p, a);
  if (tt !== s1 && tt !== nf(res)) st.push(T("Multiply: ", "Se multiplica: ") + tt + ".");
  st.push("<strong>" + nombre + "(" + sg(a) + ") = " + nf(res) + "</strong>.");
  return st;
}
function fDef(p, nombre){ return (nombre || "f") + "(x) = " + pVis(p); }

/* ---------- Average rate of change ---------- */
function tasaTxt(fa, fb, a, b){ return "(" + nf(fb) + " − " + (fa < 0 ? "(" + nf(fa) + ")" : nf(fa)) + ") / (" + nf(b) + " − " + (a < 0 ? "(" + nf(a) + ")" : nf(a)) + ")"; }
/* a fraction p/q in lowest terms, or a decimal */
function fracTxt(n, d){ if (d < 0){ n = -n; d = -d; } if (n === Math.round(n) && d === Math.round(d)){ var a = Math.abs(n), b = d; while (b){ var t = a % b; a = b; b = t; } a = a || 1; n /= a; d /= a; return d === 1 ? sg(n) : (n < 0 ? "−" : "") + Math.abs(n) + "/" + d; } return nf(n / d); }

/* ---------- Kind of function from a table (equally spaced inputs) ---------- */
function difs(l){ var r = []; for (var i = 1; i < l.length; i++) r.push(Math.round((l[i] - l[i - 1]) * 1e6) / 1e6); return r; }
function razones(l){ var r = []; for (var i = 1; i < l.length; i++) r.push(l[i - 1] ? Math.round(l[i] / l[i - 1] * 1e6) / 1e6 : NaN); return r; }
function constante(l){ return l.length > 0 && l.every(function(v){ return isFinite(v) && Math.abs(v - l[0]) < 1e-9; }); }
function tipoTabla(ys){ var d1 = difs(ys), d2 = difs(d1), q = razones(ys);
  if (constante(d1)) return "lin"; if (constante(d2) && d2[0] !== 0) return "cuad"; if (constante(q) && q[0] !== 1 && q[0] > 0) return "exp"; return "otra"; }
var NOM_TIPO = {lin: ["linear", "lineal"], cuad: ["quadratic", "cuadrática"], exp: ["exponential", "exponencial"], otra: ["none of the three", "ninguna de las tres"], rac: ["rational", "racional"]};
function nomTipo(k){ return T(NOM_TIPO[k][0], NOM_TIPO[k][1]); }
