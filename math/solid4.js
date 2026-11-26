/* LearnGED · Level 4 · Solids in 3D: drawings, volume, and surface area (Topic 2).
   Loaded after practice.js, radicals.js, linear.js and coord4.js (it uses T, f1, nd, sg, aprox, fr, fTxt).
   José M. Fernández · CC BY-NC-SA 4.0 */

/* ---------- Numbers with π ---------- */
/* k is a fraction {n, d}: kπ → "36π", "(4/3)π", "π", "0" */
function piTxt(k){ if (k.n === 0) return "0"; var a = Math.abs(k.n), s = k.n < 0 ? "−" : ""; if (k.d === 1) return s + (a === 1 ? "" : a) + "π"; return s + a + "/" + k.d + " π"; }
function piVal(k){ return k.n / k.d * Math.PI; }
function redondea(x, d){ var p = Math.pow(10, d === undefined ? 1 : d); return Math.round(x * p) / p; }
function n1(x, d){ return nd(redondea(x, d === undefined ? 1 : d)); }
/* Units in both languages: [singular, plural, cubic, square] */
var UNID = {
  "in": ES ? ["pulgada", "pulgadas", "pulgadas cúbicas", "pulgadas cuadradas", "pulg"] : ["inch", "inches", "cubic inches", "square inches", "in"],
  "ft": ES ? ["pie", "pies", "pies cúbicos", "pies cuadrados", "pies"] : ["foot", "feet", "cubic feet", "square feet", "ft"],
  "yd": ES ? ["yarda", "yardas", "yardas cúbicas", "yardas cuadradas", "yd"] : ["yard", "yards", "cubic yards", "square yards", "yd"]};
/* Reads "36π", "36 pi", "36", "113.1": returns {pi: number in front of π or null, val: decimal value or null} */
function leePi(txt){
  var s = String(txt).trim().toLowerCase().replace(/\s+/g, "").replace(/[−–]/g, "-");
  var tienePi = /π|pi$/.test(s); s = s.replace(/π|pi$/, "");
  if (s === "" && tienePi) s = "1";
  var f = s.match(/^\(?(-?\d+)\/(\d+)\)?$/), v = f ? +f[1] / +f[2] : leeDecimal(s.replace(/,(?=\d{3}\b)/g, ""));
  if (v === null || isNaN(v)) return null;
  return tienePi ? {pi: v, val: v * Math.PI} : {pi: null, val: v};
}
/* Checks a volume or area that has π in it: exact (kπ) or approximate (with π ≈ 3.14 or the π key, 1 % margin) */
function evaluaPi(txt, k, pistas){
  var r = leePi(txt);
  if (!r) return {estado: "invalido", msg: T("Type the number in front of π (for example, 36π) or the decimal value (for example, 113.1).", "Escriba el número que acompaña a π (por ejemplo, 36π) o el valor decimal (por ejemplo, 113.1).")};
  var exacto = k.n / k.d, ok = r.pi !== null ? Math.abs(r.pi - exacto) < 1e-6 : (Math.abs(r.val - exacto * Math.PI) <= Math.max(0.051, exacto * Math.PI * 0.01) || Math.abs(r.val - exacto * 3.14) <= Math.max(0.051, exacto * 3.14 * 0.005));
  if (ok) return {estado: "bien"};
  if (r.pi === null && Math.abs(r.val - exacto) < 1e-6) return {estado: "mal", msg: T("That is the number in front of π. Write it with π (" + nd(exacto) + "π) or multiply it by π.", "Ese es el número que acompaña a π. Escríbalo con π (" + nd(exacto) + "π) o multiplíquelo por π.")};
  var x = r.pi !== null ? r.pi : r.val / Math.PI;
  for (var i = 0; i < (pistas || []).length; i++) if (Math.abs(x - pistas[i].k) < 0.02 * Math.max(1, Math.abs(pistas[i].k))) return {estado: "mal", msg: pistas[i].msg};
  return {estado: "mal", msg: T("Check the formula and the substitution, one step at a time.", "Revise la fórmula y la sustitución, un paso a la vez.")};
}
/* Plain number answer with a margin (for volumes without π, and lengths) */
function evaluaNum(txt, v, tol, pistas){
  var x = leeDecimal(String(txt).replace(/,(?=\d{3}\b)/g, "").replace(/\s/g, ""));
  if (x === null) return {estado: "invalido", msg: T("Type a number, like 120 or 7.5.", "Escriba un número, como 120 o 7.5.")};
  if (Math.abs(x - v) <= (tol || 1e-6)) return {estado: "bien"};
  for (var i = 0; i < (pistas || []).length; i++) if (Math.abs(x - pistas[i].v) <= Math.max(tol || 0, 1e-6)) return {estado: "mal", msg: pistas[i].msg};
  return {estado: "mal", msg: T("Check the formula and the substitution, one step at a time.", "Revise la fórmula y la sustitución, un paso a la vez.")};
}

/* ---------- Drawings (SVG, a front view with an ellipse for depth) ---------- */
var S4 = {linea: "#37474f", rell: "#e3f2fd", radio: "#c62828", alto: "#1565c0", base: "#2e7d32", oculto: "#90a4ae"};
function etq(x, y, txt, color, ancla, tam){ return '<text x="' + f1(x) + '" y="' + f1(y) + '" font-size="' + (tam || 16) + '" font-weight="700" fill="' + (color || S4.linea) + '" text-anchor="' + (ancla || "middle") + '" paint-order="stroke" stroke="#fff" stroke-width="4">' + txt + "</text>"; }
function lin(x1, y1, x2, y2, color, ancho, raya){ return '<line x1="' + f1(x1) + '" y1="' + f1(y1) + '" x2="' + f1(x2) + '" y2="' + f1(y2) + '" stroke="' + (color || S4.linea) + '" stroke-width="' + (ancho || 2.5) + '"' + (raya ? ' stroke-dasharray="' + raya + '"' : "") + ' stroke-linecap="round"/>'; }
function elip(cx, cy, rx, ry, relleno, color, mitad){
  if (mitad === "atras") return '<path d="M' + f1(cx - rx) + " " + f1(cy) + " A" + f1(rx) + " " + f1(ry) + " 0 0 1 " + f1(cx + rx) + " " + f1(cy) + '" fill="none" stroke="' + (color || S4.linea) + '" stroke-width="2" stroke-dasharray="6 5"/>';
  if (mitad === "frente") return '<path d="M' + f1(cx - rx) + " " + f1(cy) + " A" + f1(rx) + " " + f1(ry) + " 0 0 0 " + f1(cx + rx) + " " + f1(cy) + '" fill="none" stroke="' + (color || S4.linea) + '" stroke-width="2.5"/>';
  return '<ellipse cx="' + f1(cx) + '" cy="' + f1(cy) + '" rx="' + f1(rx) + '" ry="' + f1(ry) + '" fill="' + (relleno || "none") + '" stroke="' + (color || S4.linea) + '" stroke-width="2.5"/>';
}
function marco(W, H, voz, cuerpo, ancho){ return '<svg class="geo-svg" viewBox="0 0 ' + W + " " + H + '" role="img" aria-label="' + voz + '" style="max-width:' + (ancho || W) + 'px">' + cuerpo + "</svg>"; }
/* o: {r, u, diam, cil, voz}; sizes in px are scaled to fit */
function esferaSVG(o){
  var W = 360, H = 300, cx = 180, cy = 150, R = 110, s = "";
  if (o.cil) s += '<rect x="' + (cx - R) + '" y="' + (cy - R) + '" width="' + 2 * R + '" height="' + 2 * R + '" fill="#fff8e1" stroke="#f9a825" stroke-width="2" stroke-dasharray="7 5"/>' + elip(cx, cy - R, R, R * .22, "none", "#f9a825") + elip(cx, cy + R, R, R * .22, "none", "#f9a825", "frente");
  s += '<circle cx="' + cx + '" cy="' + cy + '" r="' + R + '" fill="' + S4.rell + '" stroke="' + S4.linea + '" stroke-width="2.5"/>';
  s += elip(cx, cy, R, R * .25, "none", S4.oculto, "atras") + elip(cx, cy, R, R * .25, "none", S4.linea, "frente");
  s += '<circle cx="' + cx + '" cy="' + cy + '" r="4" fill="' + S4.linea + '"/>' + lin(cx, cy, cx + R, cy, S4.radio, 3.5) + etq(cx + R + 8, cy + 6, isNaN(+o.r) ? "r" : "r = " + o.r, S4.radio, "start");
  if (o.diam) s += lin(cx - R, cy + 36, cx + R, cy + 36, "#6a1b9a", 2.5, "6 4") + etq(cx, cy + 58, isNaN(+o.r) ? "d" : "d = " + nd(2 * o.r), "#6a1b9a");
  return marco(W, H, o.voz, s, o.ancho || 340);
}
function conoSVG(o){
  var W = 360, H = 320, cx = 180, base = 270, R = Math.max(30, Math.min(140, o.r * o.esc)), h = Math.max(40, Math.min(230, o.h * o.esc)), ap = base - h, s = "";
  if (o.cil) s += '<rect x="' + (cx - R) + '" y="' + ap + '" width="' + 2 * R + '" height="' + h + '" fill="#fff8e1" stroke="#f9a825" stroke-width="2" stroke-dasharray="7 5"/>' + elip(cx, ap, R, R * .25, "none", "#f9a825");
  s += '<path d="M' + f1(cx - R) + " " + base + " L" + cx + " " + f1(ap) + " L" + f1(cx + R) + " " + base + ' A' + f1(R) + " " + f1(R * .25) + " 0 0 1 " + f1(cx - R) + " " + base + 'Z" fill="' + S4.rell + '" stroke="' + S4.linea + '" stroke-width="2.5"/>';
  s += elip(cx, base, R, R * .25, "none", S4.oculto, "atras");
  s += lin(cx, ap, cx, base, S4.alto, 3, "7 5") + lin(cx, base, cx + R, base, S4.radio, 3.5) + '<path d="M' + cx + " " + (base - 12) + " h12 v12" + '" fill="none" stroke="' + S4.alto + '" stroke-width="2"/>';
  s += etq(R < 80 ? cx - R / 2 - 8 : cx - 10, (ap + base) / 2, "h = " + o.h, S4.alto, "end") + etq(cx + R / 2, Math.min(base + R * .25 + 19, H - 3), "r = " + o.r, S4.radio);
  return marco(W, H, o.voz, s, o.ancho || 340);
}
function cilindroSVG(o){
  var W = 360, H = 320, cx = 180, base = 270, R = Math.max(30, Math.min(140, o.r * o.esc)), h = Math.max(40, Math.min(220, o.h * o.esc)), top = base - h, s = "";
  s += '<path d="M' + f1(cx - R) + " " + f1(top) + " L" + f1(cx - R) + " " + base + " A" + f1(R) + " " + f1(R * .25) + " 0 0 0 " + f1(cx + R) + " " + base + " L" + f1(cx + R) + " " + f1(top) + '" fill="' + S4.rell + '" stroke="' + S4.linea + '" stroke-width="2.5"/>';
  s += elip(cx, top, R, R * .25, "#bbdefb") + elip(cx, base, R, R * .25, "none", S4.oculto, "atras");
  s += lin(cx + R + 18, top, cx + R + 18, base, S4.alto, 3, "7 5") + etq(cx + R + 24, (top + base) / 2, "h = " + o.h, S4.alto, "start") + lin(cx, top, cx + R, top, S4.radio, 3.5) + etq(cx + R / 2, top - 12, "r = " + o.r, S4.radio);
  return marco(W, H, o.voz, s, o.ancho || 340);
}
/* Pyramid or prism with a rectangular base L × b (oblique view) */
function caja3(L, b, esc){ var w = Math.max(60, Math.min(220, L * esc)), d = Math.max(30, Math.min(120, b * esc)) * .5; return {w: w, dx: d * .8, dy: d * .55}; }
function piramideSVG(o){
  var W = 380, H = 330, k = caja3(o.L, o.b, o.esc), x0 = 190 - (k.w + k.dx) / 2, y0 = 290, h = Math.max(50, Math.min(220, o.h * o.esc)), s = "";
  var A = [x0, y0], B = [x0 + k.w, y0], C = [x0 + k.w + k.dx, y0 - k.dy], D = [x0 + k.dx, y0 - k.dy], cen = [x0 + (k.w + k.dx) / 2, y0 - k.dy / 2], V = [cen[0], cen[1] - h];
  if (o.prisma) s += '<polygon points="' + [A, B, [B[0], B[1] - h], [A[0], A[1] - h]].map(function(p){ return f1(p[0]) + "," + f1(p[1]); }).join(" ") + '" fill="#fff8e1" stroke="#f9a825" stroke-width="2" stroke-dasharray="7 5"/>' + '<polygon points="' + [[A[0], A[1] - h], [B[0], B[1] - h], [C[0], C[1] - h], [D[0], D[1] - h]].map(function(p){ return f1(p[0]) + "," + f1(p[1]); }).join(" ") + '" fill="none" stroke="#f9a825" stroke-width="2" stroke-dasharray="7 5"/>';
  s += lin(A[0], A[1], D[0], D[1], S4.oculto, 2, "6 5") + lin(D[0], D[1], C[0], C[1], S4.oculto, 2, "6 5") + lin(D[0], D[1], V[0], V[1], S4.oculto, 2, "6 5");
  s += '<polygon points="' + [A, B, V].map(function(p){ return f1(p[0]) + "," + f1(p[1]); }).join(" ") + '" fill="' + S4.rell + '" stroke="' + S4.linea + '" stroke-width="2.5"/>';
  s += '<polygon points="' + [B, C, V].map(function(p){ return f1(p[0]) + "," + f1(p[1]); }).join(" ") + '" fill="#bbdefb" stroke="' + S4.linea + '" stroke-width="2.5"/>';
  var ym = (V[1] + cen[1]) / 2;
  s += lin(V[0], V[1], cen[0], cen[1], S4.alto, 3, "7 5");
  if (o.prisma) s += lin(A[0] - 6, ym, cen[0] - 4, ym, S4.alto, 1.5, "2 4") + etq(A[0] - 10, ym + 5, "h = " + o.h, S4.alto, "end");
  else s += etq(cen[0] - 10, ym, "h = " + o.h, S4.alto, "end");
  s += etq((A[0] + B[0]) / 2, y0 + 26, (o.cuadrada ? "L = " : "L = ") + o.L, S4.base) + etq((B[0] + C[0]) / 2 + 14, (B[1] + C[1]) / 2 + 6, (o.cuadrada ? "L = " : T("w = ", "a = ")) + o.b, S4.base, "start");
  return marco(W, H, o.voz, s, o.ancho || 360);
}
function prismaSVG(o){
  var W = 380, H = 320, k = caja3(o.L, o.b, o.esc), x0 = 190 - (k.w + k.dx) / 2, y0 = 290, h = Math.max(40, Math.min(200, o.h * o.esc)), s = "";
  var A = [x0, y0], B = [x0 + k.w, y0], C = [x0 + k.w + k.dx, y0 - k.dy], D = [x0 + k.dx, y0 - k.dy], up = function(p){ return [p[0], p[1] - h]; };
  s += lin(A[0], A[1], D[0], D[1], S4.oculto, 2, "6 5") + lin(D[0], D[1], C[0], C[1], S4.oculto, 2, "6 5") + lin(D[0], D[1], D[0], D[1] - h, S4.oculto, 2, "6 5");
  [[A, B, up(B), up(A), S4.rell], [B, C, up(C), up(B), "#bbdefb"], [up(A), up(B), up(C), up(D), "#e1f5fe"]].forEach(function(c){ s += '<polygon points="' + c.slice(0, 4).map(function(p){ return f1(p[0]) + "," + f1(p[1]); }).join(" ") + '" fill="' + c[4] + '" stroke="' + S4.linea + '" stroke-width="2.5"/>'; });
  s += etq((A[0] + B[0]) / 2, y0 + 26, "L = " + o.L, S4.base) + etq((B[0] + C[0]) / 2 + 14, (B[1] + C[1]) / 2 + 6, T("w = ", "a = ") + o.b, S4.base, "start") + etq(A[0] - 10, y0 - h / 2, "h = " + o.h, S4.alto, "end");
  var dims = [o.L, o.b, o.h].map(Number);
  if (Math.max.apply(null, dims) / Math.min.apply(null, dims) > 6) s += etq(W / 2, 22, T("(drawing not to scale)", "(dibujo sin escala)"), "#607d8b", "middle", 13);
  return marco(W, H, o.voz, s, o.ancho || 360);
}
