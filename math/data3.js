/* LearnGED · Level 3 · Topic 7 · Volume and data engine, data3.js (English and Spanish)
   Loaded after radicals.js, linear.js, inequalities.js, and geometry3.js.
   Quartiles use the lesson's method: the median of each half, leaving out the median when the count is odd.
   José M. Fernández · CC BY-NC-SA 4.0 */
var PI = 3.14;
function r1(x){ return parseFloat(x.toFixed(1)); }
function r2(x){ return parseFloat(x.toFixed(2)); }
/* SVG text with a chosen anchor ("start", "middle", "end") */
function textoA(p, t, tam, color, peso, anc){ return '<text x="' + f1(p[0]) + '" y="' + f1(p[1]) + '" text-anchor="' + (anc || "middle") + '" dominant-baseline="middle" font-size="' + (tam || 16) + '" font-weight="' + (peso || 700) + '" fill="' + (color || "#222") + '">' + t + "</text>"; }
function opN(v){ return {html: nm(v), clave: "n" + v}; }

/* Answer = k·π. Accepts k·3.14 or k·π to the tenth, or the exact form "kπ" (also "k pi"). */
function evaluaPi(txt, k, pistas){
  var s = String(txt).trim().replace(/\s+/g, "").replace(/pi$/i, "π");
  var m = s.match(/^(\d+(?:\.\d+)?)π$/);
  if (m) return Math.abs(parseFloat(m[1]) - k) < 1e-6 ? {estado: "bien", msg: ""} : {estado: "mal", msg: T("The number in front of π is not right.", "El número que acompaña a π no es el correcto.")};
  var v = leeDecimal(s);
  if (v === null) return {estado: "invalido", msg: T("Type a number (for example, 62.8) or the exact answer with π (for example, 20π).", "Escriba un número (por ejemplo, 62.8) o el resultado exacto con π (por ejemplo, 20π).")};
  if (Math.abs(v - k * 3.14) <= 0.051 || Math.abs(v - k * Math.PI) <= 0.051) return {estado: "bien", msg: ""};
  for (var i = 0; i < pistas.length; i++) if (Math.abs(v - pistas[i].v) <= 0.06) return {estado: "mal", msg: pistas[i].msg};
  return {estado: "mal", msg: T("Square the radius, multiply by π, then by the height.", "Eleve el radio al cuadrado, multiplique por π y después por la altura.")};
}

/* ---------- Statistics ---------- */
function ordena(d){ return d.slice().sort(function(a, b){ return a - b; }); }
function mediana(o){ var n = o.length, m = Math.floor(n / 2); return n % 2 ? o[m] : (o[m - 1] + o[m]) / 2; }
function mitades(o){ var n = o.length, m = Math.floor(n / 2); return [o.slice(0, m), o.slice(n % 2 ? m + 1 : m)]; }
function cinco(d){ var o = ordena(d), h = mitades(o); return {min: o[0], q1: mediana(h[0]), med: mediana(o), q3: mediana(h[1]), max: o[o.length - 1], o: o}; }
function datosAzar(n, lo, hi){ var d = []; for (var i = 0; i < n; i++) d.push(aleatorio(lo, hi)); return d; }
function limites(c){ var iqr = c.q3 - c.q1; return {iqr: iqr, inf: c.q1 - 1.5 * iqr, sup: c.q3 + 1.5 * iqr}; }
function listaN(o){ return o.map(nm).join(", "); }
function chips(o, clases){
  return '<div class="datos" aria-hidden="true">' + o.map(function(v, i){ return '<span class="dato' + (clases && clases[i] ? " " + clases[i] : "") + '">' + nm(v) + "</span>"; }).join("") + "</div>" +
         '<span class="sr-only">' + listaN(o) + "</span>";
}
function escalaBonita(lo, hi){
  var r = hi - lo || 1, paso = 1, cand = [1, 2, 5, 10, 20, 25, 50, 100, 200, 500];
  for (var i = 0; i < cand.length; i++){ if (r / cand[i] <= 10){ paso = cand[i]; break; } }
  return {lo: Math.floor(lo / paso) * paso, hi: Math.ceil(hi / paso) * paso, paso: paso};
}
/* Box plot. grupos = [{nombre, c (five values), atip: [], bigMin, bigMax, color, relleno}] */
function cajaSVG(grupos, voz, opc){
  opc = opc || {};
  var lo = Infinity, hi = -Infinity;
  grupos.forEach(function(g){ lo = Math.min(lo, g.c.min); hi = Math.max(hi, g.c.max); });
  if (opc.lo !== undefined){ lo = Math.min(lo, opc.lo); hi = Math.max(hi, opc.hi); }
  var E = escalaBonita(lo, hi), W = 640, x0 = opc.x0 || (grupos.length > 1 ? 90 : 40), x1 = opc.x1 || W - 30, alto = 76, top = opc.rotulos ? 58 : 30, H = top + grupos.length * alto + 34;
  function X(v){ return x0 + (v - E.lo) * (x1 - x0) / (E.hi - E.lo); }
  var s = '<svg class="geo-svg" viewBox="0 0 ' + W + " " + H + '" role="img" aria-label="' + voz + '">', yEje = H - 34;
  s += lineaG([x0, yEje], [x1, yEje], "#424242", 2);
  for (var v = E.lo; v <= E.hi + 1e-9; v += E.paso) s += lineaG([X(v), yEje - 6], [X(v), yEje + 6], "#424242", 2) + textoA([X(v), yEje + 20], nm(v), 16, "#222", 400);
  var rot = [[T("min", "mín"), "min"], ["Q1", "q1"], [T("median", "mediana"), "med"], ["Q3", "q3"], [T("max", "máx"), "max"]];
  grupos.forEach(function(g, i){
    var y = top + 10 + i * alto, c = g.c, col = g.color || "#37474f", bmin = g.bigMin !== undefined ? g.bigMin : c.min, bmax = g.bigMax !== undefined ? g.bigMax : c.max;
    if (grupos.length > 1) s += textoA([x0 - 14, y], g.nombre, 22, col, 700, "end");
    s += lineaG([X(bmin), y], [X(c.q1), y], col, 3) + lineaG([X(c.q3), y], [X(bmax), y], col, 3);
    s += lineaG([X(bmin), y - 12], [X(bmin), y + 12], col, 3) + lineaG([X(bmax), y - 12], [X(bmax), y + 12], col, 3);
    s += '<rect x="' + f1(X(c.q1)) + '" y="' + (y - 20) + '" width="' + f1(Math.max(X(c.q3) - X(c.q1), 1)) + '" height="40" fill="' + (g.relleno || "#cfd8dc") + '" stroke="' + col + '" stroke-width="3"/>';
    s += lineaG([X(c.med), y - 20], [X(c.med), y + 20], "#b71c1c", 4);
    (g.atip || []).forEach(function(a){ s += '<circle cx="' + f1(X(a)) + '" cy="' + y + '" r="7" fill="#fff" stroke="#b71c1c" stroke-width="3"/>'; });
    if (opc.rotulos){
      /* min, median, and max on the lower row; Q1 and Q3 on the upper row, so close labels do not overlap */
      var vals = {min: bmin, q1: c.q1, med: c.med, q3: c.q3, max: bmax};
      rot.forEach(function(p, k){ s += textoA([X(vals[p[1]]), y - 31 - (k % 2) * 17], p[0], 14, p[1] === "med" ? "#b71c1c" : "#424242", 700); });
    }
  });
  return s + "</svg>";
}
/* Histogram. clases = [{a, b, f}] */
function histSVG(clases, voz, opc){
  opc = opc || {};
  var W = 640, H = 300, x0 = 64, x1 = W - 20, yb = H - 48, ytop = 20, fmax = Math.max.apply(null, clases.map(function(c){ return c.f; })) || 1;
  var paso = fmax <= 6 ? 1 : (fmax <= 12 ? 2 : (fmax <= 30 ? 5 : 10)), tope = Math.ceil(fmax / paso) * paso, n = clases.length, w = (x1 - x0) / n;
  function Y(f){ return yb - f * (yb - ytop) / tope; }
  var s = '<svg class="geo-svg" viewBox="0 0 ' + W + " " + H + '" role="img" aria-label="' + voz + '">';
  for (var f = 0; f <= tope; f += paso) s += lineaG([x0, Y(f)], [x1, Y(f)], "#e0e0e0", 1) + textoA([x0 - 8, Y(f)], f, 16, "#424242", 400, "end");
  clases.forEach(function(c, i){
    s += '<rect x="' + f1(x0 + i * w) + '" y="' + f1(Y(c.f)) + '" width="' + f1(w) + '" height="' + f1(yb - Y(c.f)) + '" fill="' + (opc.marcar === i ? "#f9a825" : "#90a4ae") + '" stroke="#37474f" stroke-width="2"/>';
    s += textoA([x0 + i * w, yb + 18], nm(c.a), 16, "#222", 400);
  });
  s += textoA([x1, yb + 18], nm(clases[n - 1].b), 16, "#222", 400);
  s += lineaG([x0, yb], [x1, yb], "#424242", 2) + lineaG([x0, yb], [x0, ytop], "#424242", 2);
  var yc = (yb + ytop) / 2;
  s += '<text x="' + (x0 - 46) + '" y="' + yc + '" transform="rotate(-90 ' + (x0 - 46) + " " + yc + ')" text-anchor="middle" font-size="14" font-weight="700" fill="#424242">' + T("Frequency", "Frecuencia") + "</text>";
  if (opc.eje) s += textoA([(x0 + x1) / 2, H - 8], opc.eje, 15, "#424242", 700);
  return s + "</svg>";
}
