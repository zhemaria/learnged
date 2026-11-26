/* LearnGED · Level 2 · shared helpers for statistics, circle graphs, and probability (Topic 8).
   Needs practice.js and rates.js first. */
var TXS = ES ? {
  prob: "Escriba la probabilidad como fracción (3/8), decimal (0.375) o porcentaje (37.5%).",
  mayor1: "Una probabilidad nunca pasa de 1 (100%). Revise los casos favorables y los totales.",
  sobre: " sobre ", sinModa: "no hay moda", y: " y "
} : {
  prob: "Write the probability as a fraction (3/8), a decimal (0.375), or a percent (37.5%).",
  mayor1: "A probability is never more than 1 (100%). Check the favorable and the total outcomes.",
  sobre: " over ", sinModa: "no mode", y: " and "
};
/* ---------- Basic statistics ---------- */
function ordenaN(d){ return d.slice().sort(function(a, b){ return a - b; }); }
function sumaDe(d){ return d.reduce(function(s, x){ return s + x; }, 0); }
function mediaDe(d){ return sumaDe(d) / d.length; }
function medianaDe(d){ var o = ordenaN(d), n = o.length, m = Math.floor(n / 2); return n % 2 ? o[m] : (o[m - 1] + o[m]) / 2; }
function modasDe(d){
  var c = {}, mx = 0; d.forEach(function(x){ c[x] = (c[x] || 0) + 1; mx = Math.max(mx, c[x]); });
  if (mx === 1) return [];
  var m = Object.keys(c).filter(function(k){ return c[k] === mx; }).map(Number);
  if (m.length === Object.keys(c).length) return [];
  return ordenaN(m);
}
function modaTxt(m){ return m.length === 0 ? TXS.sinModa : m.map(nd).join(TXS.y); }
function lista(d){ return d.map(nd).join(", "); }
/* "78, 85, 90" or "78 85 90" → [78, 85, 90]; null if something is not a number */
function leeLista(t){
  var p = String(t).trim().replace(/,\s+/g, " ").split(/[;\s]+/).filter(function(x){ return x !== ""; });
  if (p.length === 1 && !/^-?\d{1,3}(,\d{3})+(\.\d+)?$/.test(p[0])) p = p[0].split(",").filter(function(x){ return x !== ""; });
  p = p.map(function(x){ return leeD(x); });
  return p.length && p.every(function(x){ return x !== null; }) ? p : null;
}
/* Data shown as chips; clases[i] = "med", "moda", "ext", "fav" */
function chipsN(o, clases, txt){
  return '<div class="datos" aria-hidden="true">' + o.map(function(v, i){ return '<span class="dato' + (clases && clases[i] ? " " + clases[i] : "") + '">' + (txt ? txt[i] : nd(v)) + '</span>'; }).join("") + '</div><span class="sr-only">' + (txt ? txt.join(", ") : o.map(nd).join(", ")) + '</span>';
}

/* ---------- Circle graphs ---------- */
var COLS = ["#c62828", "#1565c0", "#2e7d32", "#8a5a00", "#6a1b9a", "#00695c", "#bf360c", "#4e342e"];
function punto(cx, cy, R, gr){ var a = gr * Math.PI / 180; return [cx + R * Math.cos(a), cy - R * Math.sin(a)]; }
/* items: [{nombre, pct, color}] · opc.sinPct: no percent labels */
function pieSVG(items, voz, opc){
  opc = opc || {};
  var cx = 160, cy = 150, R = 120, a0 = 90, s = '<svg class="figura" viewBox="0 0 640 300" role="img" aria-label="' + voz + '">';
  items.forEach(function(it, i){
    var ang = 360 * it.pct / 100, a1 = a0 - ang, col = it.color || COLS[i % COLS.length];
    if (ang >= 359.99) s += '<circle cx="' + cx + '" cy="' + cy + '" r="' + R + '" fill="' + col + '"/>';
    else if (ang > 0){ var p0 = punto(cx, cy, R, a0), p1 = punto(cx, cy, R, a1); s += '<path d="M' + cx + ' ' + cy + ' L' + f1(p0[0]) + ' ' + f1(p0[1]) + ' A' + R + ' ' + R + ' 0 ' + (ang > 180 ? 1 : 0) + ' 1 ' + f1(p1[0]) + ' ' + f1(p1[1]) + ' Z" fill="' + col + '" stroke="#fff" stroke-width="2"/>'; }
    if (it.pct >= 6 && !opc.sinPct){ var pm = punto(cx, cy, R * 0.64, a0 - ang / 2); s += texto(pm, it.etq !== undefined ? it.etq : nd(it.pct) + "%", 17, "#fff"); }
    a0 = a1;
    var ly = 40 + i * 32;
    s += '<rect x="320" y="' + (ly - 10) + '" width="20" height="20" rx="3" fill="' + col + '"/><text x="350" y="' + ly + '" dominant-baseline="middle" font-size="19" fill="#222">' + it.nombre + (opc.sinPct ? "" : " — " + (it.etq !== undefined ? it.etq : nd(it.pct) + "%")) + '</text>';
  });
  return s + '</svg>';
}
/* n percents, multiples of 5, that add to 100 */
function repartoAzar(n){
  for (var k = 0; k < 300; k++){
    var p = [], rest = 100;
    for (var i = 0; i < n - 1; i++){ var v = 5 * aleatorio(1, Math.min(10, Math.floor((rest - 5 * (n - 1 - i)) / 5))); p.push(v); rest -= v; }
    if (rest >= 5 && rest <= 60){ p.push(rest); if (p.every(function(x, j, a){ return a.indexOf(x) === j; }) || Math.random() < 0.3) return baraja(p); }
  }
  return [40, 30, 20, 10].slice(0, n);
}
function items(nombres, pcts){ return nombres.map(function(n, i){ return { nombre: n, pct: pcts[i] }; }); }

/* ---------- Fractions and probability ---------- */
function mcdS(a, b){ a = Math.abs(a); b = Math.abs(b); while (b){ var x = a % b; a = b; b = x; } return a; }
function reduce(p, q){ var g = mcdS(p, q) || 1; return { p: p / g, q: q / g }; }
function fracHTML(p, q){
  if (q === 1) return String(p);
  return '<span aria-hidden="true"><span class="fracc"><span class="fa">' + p + '</span><span class="fb2">' + q + '</span></span></span><span class="sr-only">' + p + TXS.sobre + q + '</span>';
}
/* "3/8", "0.375", "37.5%" → number, or null */
function leeProb(t){
  var s = String(t).trim().replace(/\s+/g, "");
  var pc = s.match(/^(\d+(?:\.\d+)?)%$/); if (pc) return parseFloat(pc[1]) / 100;
  var f = s.match(/^(\d+)\/(\d+)$/); if (f) return +f[2] ? +f[1] / +f[2] : null;
  return leeD(s);
}
/* Evaluator: correct value v (number); pistas [{v, msg}] */
function evaluaProb(v, pistas){
  return function(t){
    var x = leeProb(t);
    if (x === null) return { estado: "invalido", msg: TXS.prob };
    if (Math.abs(x - v) < 0.0006) return { estado: "bien" };
    for (var i = 0; i < (pistas || []).length; i++) if (Math.abs(x - pistas[i].v) < 0.0006) return { estado: "mal", msg: pistas[i].msg };
    if (x > 1) return { estado: "mal", msg: TXS.mayor1 };
    return { estado: "mal", msg: TXR.revise };
  };
}
/* 3/6 = 1/2 = 0.5 = 50% */
function tresF(a, b){
  var v = a / b, ex = Math.abs(Math.round(v * 1000) / 1000 - v) < 1e-12, s = ex ? " = " : " ≈ ", r = reduce(a, b);
  return fracHTML(a, b) + (r.q !== b && a ? " = " + fracHTML(r.p, r.q) : "") + s + nd(Math.round(v * 1000) / 1000) + s + nd(Math.round(v * 1000) / 10) + "%";
}
