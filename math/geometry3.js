/* LearnGED · Level 3 · Topic 6 · Geometry engine, geometry3.js (English and Spanish; not the Level 2 geometry.js)
   Loaded after radicals.js and linear.js. Angles are in degrees, measured counterclockwise with the y axis up.
   José M. Fernández · CC BY-NC-SA 4.0 */
function rad(g){ return g * Math.PI / 180; }
function punto(cx, cy, r, g){ return [cx + r * Math.cos(rad(g)), cy - r * Math.sin(rad(g))]; }
function lineaG(p, q, color, ancho, extra){ return '<line x1="' + f1(p[0]) + '" y1="' + f1(p[1]) + '" x2="' + f1(q[0]) + '" y2="' + f1(q[1]) + '" stroke="' + (color || "#424242") + '" stroke-width="' + (ancho || 2) + '"' + (extra || "") + "/>"; }
/* Sector of the angle from g1 to g2 (counterclockwise) */
function arco(cx, cy, r, g1, g2, color, relleno){
  var a = punto(cx, cy, r, g1), b = punto(cx, cy, r, g2), grande = ((g2 - g1 + 360) % 360) > 180 ? 1 : 0;
  return '<path d="M' + f1(cx) + " " + f1(cy) + " L" + f1(a[0]) + " " + f1(a[1]) + " A" + r + " " + r + " 0 " + grande + " 0 " + f1(b[0]) + " " + f1(b[1]) + ' Z" fill="' + (relleno || "none") + '" stroke="' + (color || "#424242") + '" stroke-width="2"/>';
}
function marcaRecta(p, g, t, color){
  var a = punto(p[0], p[1], t, g), b = punto(a[0], a[1], t, g + 90), c = punto(p[0], p[1], t, g + 90);
  return '<path d="M' + f1(a[0]) + " " + f1(a[1]) + " L" + f1(b[0]) + " " + f1(b[1]) + " L" + f1(c[0]) + " " + f1(c[1]) + '" fill="none" stroke="' + (color || "#424242") + '" stroke-width="2"/>';
}
function gr(n){ return String(n).replace("-", "−") + "°"; }
function opG(n){ return {html: gr(n), clave: "g" + n}; }
var COL_SEL = "#0d47a1", COL_IG = "#1b5e20", COL_SUP = "#b71c1c";

/* ---------- Two parallel lines r and s cut by a transversal ----------
   Angles 1–4 at line r, 5–8 at line s. Position: 0 top left, 1 top right, 2 bottom left, 3 bottom right.
   alfa is the angle of the transversal with the parallels (the measure of angles 2, 3, 6, and 7). */
function posDe(i){ return (i - 1) % 4; }
function interDe(i){ return i <= 4 ? 0 : 1; }
function medida(i, alfa){ var p = posDe(i); return (p === 1 || p === 2) ? alfa : 180 - alfa; }
var REL = {
  vert: T("vertical angles", "opuestos por el vértice"), lin: T("a linear pair", "adyacentes"),
  corr: T("corresponding angles", "correspondientes"), aint: T("alternate interior angles", "alternos internos"), aext: T("alternate exterior angles", "alternos externos"),
  sint: T("same-side interior angles", "internos del mismo lado"), sext: T("same-side exterior angles", "externos del mismo lado")};
var REL_OP = {
  vert: T("Vertical angles", "Opuestos por el vértice"), lin: T("Linear pair", "Adyacentes (forman una recta)"),
  corr: T("Corresponding", "Correspondientes"), aint: T("Alternate interior", "Alternos internos"), aext: T("Alternate exterior", "Alternos externos"),
  sint: T("Same-side interior", "Internos del mismo lado"), sext: T("Same-side exterior", "Externos del mismo lado")};
function relacion(i, j){
  var pi = posDe(i), pj = posDe(j);
  if (interDe(i) === interDe(j)) return pi + pj === 3 ? "vert" : "lin";
  if (i > j){ var x = i; i = j; j = x; x = pi; pi = pj; pj = x; }
  if (pi === pj) return "corr";
  var intI = pi >= 2, intJ = pj <= 1, izq = function(p){ return p === 0 || p === 2; };
  if (intI && intJ) return izq(pi) === izq(pj) ? "sint" : "aint";
  if (!intI && !intJ) return izq(pi) === izq(pj) ? "sext" : "aext";
  return null;
}
function dibujaTransversal(alfa, opc){
  opc = opc || {};
  var yA = 95, yB = 235, tn = Math.tan(rad(alfa)), dx = Math.abs(tn) < 1e-6 ? 0 : 70 / tn;
  var cA = [320 + dx, yA], cB = [320 - dx, yB];
  var s = '<svg class="geo-svg" viewBox="0 0 640 330" role="img" aria-label="' + (opc.voz || T("Two parallel lines r and s cut by a transversal, with eight numbered angles.", "Dos rectas paralelas r y s cortadas por una transversal, con ocho ángulos numerados.")) + '">';
  s += lineaG([30, yA], [610, yA], "#424242", 3) + lineaG([30, yB], [610, yB], "#424242", 3);
  s += lineaG(punto(cB[0], cB[1], 95, alfa + 180), punto(cA[0], cA[1], 95, alfa), "#6a1b9a", 3);
  s += texto([600, yA - 16], "r", 18, "#555") + texto([600, yB - 16], "s", 18, "#555");
  for (var i = 1; i <= 8; i++){
    var c = interDe(i) === 0 ? cA : cB, p = posDe(i), g = [(alfa + 180) / 2, alfa / 2, 180 + alfa / 2, (alfa + 540) / 2][p];
    var et = opc.etiquetas && opc.etiquetas[i], q = punto(c[0], c[1], et ? 46 : 40, g), col = opc.colores && opc.colores[i];
    if (col) s += '<circle cx="' + f1(q[0]) + '" cy="' + f1(q[1]) + '" r="' + (et ? 22 : 16) + '" fill="' + col + '"/>';
    s += texto(q, et || String(i), et ? 15 : 17, col ? "#fff" : "#222");
  }
  return s + "</svg>";
}

/* ---------- Typed number with two tries: answer in whole degrees or a value of x ---------- */
function evaluaGrados(txt, esperado, pistas){ return evaluaNumero(String(txt).replace(/°/g, ""), fr(esperado), (pistas || []).map(function(p){ return {v: fr(p.v), msg: p.msg}; })); }

/* ---------- Step-by-step viewer: buttons pre-sig and pre-todo, list pre-pasos ---------- */
function pasoAPaso(pre, pasos){
  var S = {pasos: pasos, visto: 0};
  function pinta(){
    var h = "";
    for (var i = 0; i < S.visto; i++) h += '<div class="paso"><span class="n" aria-hidden="true">' + (i === S.pasos.length - 1 ? "✓" : i + 1) + "</span>" + S.pasos[i] + "</div>";
    $(pre + "-pasos").innerHTML = h;
    var b = $(pre + "-sig"); b.disabled = S.visto >= S.pasos.length; $(pre + "-todo").disabled = b.disabled;
    b.textContent = S.visto === 0 ? T("Show the first step", "Mostrar el primer paso") : (b.disabled ? T("All the steps are showing", "Ya se ven todos los pasos") : T("Show the next step", "Mostrar el siguiente paso"));
  }
  S.pinta = pinta;
  S.carga = function(p){ S.pasos = p; S.visto = 0; pinta(); };
  $(pre + "-sig").addEventListener("click", function(){ if (S.visto < S.pasos.length){ S.visto++; pinta(); } });
  $(pre + "-todo").addEventListener("click", function(){ S.visto = S.pasos.length; pinta(); });
  pinta();
  return S;
}

/* ---------- Pythagorean theorem ---------- */
var TRIPLES = [[3, 4, 5], [5, 12, 13], [8, 15, 17], [7, 24, 25]];
function tripleAzar(max){ var t, k; do { t = elige(TRIPLES); k = aleatorio(1, 4); } while (t[2] * k > (max || 60)); return [t[0] * k, t[1] * k, t[2] * k]; }
/* √n, simplified when it can be, and rounded to the tenth when it is not exact */
function raizTxt(n){ var s = simplRad(n); return s.r === 1 ? String(s.k) : radHTML(1, n) + (s.k > 1 ? " = " + radHTML(s.k, s.r) : "") + " ≈ " + aprox(Math.sqrt(n), 1); }
/* Typed answer √n: exact, or rounded to the tenth */
function evaluaRaiz(txt, n, pistas){
  var v = leeDecimal(txt), exacto = esCuadrado(n), r = Math.sqrt(n);
  if (v === null){ var f = leeFraccion(txt); if (f) v = f.p / f.q; }
  if (v === null) return {estado: "invalido", msg: T("Type a number, for example 13 or 7.8.", "Escriba un número, por ejemplo 13 o 7.8.")};
  if (exacto ? Math.abs(v - r) < 1e-9 : Math.abs(v - parseFloat(aprox(r, 1))) < 1e-9) return {estado: "bien", msg: ""};
  if (!exacto && Math.abs(v - r) < 0.1) return {estado: "mal", msg: T("Almost: round to the nearest tenth.", "Casi: redondee a la décima.")};
  for (var i = 0; i < pistas.length; i++) if (Math.abs(v - pistas[i].v) < 0.051) return {estado: "mal", msg: pistas[i].msg};
  return {estado: "mal", msg: T("Check the squares and the square root.", "Revise los cuadrados y la raíz cuadrada.")};
}

/* ---------- Similarity and scale ---------- */
/* A number for display: up to 4 decimals, no trailing zeros, visual minus sign */
function nm(x){ return String(parseFloat(x.toFixed(4))).replace("-", "−"); }
function Qf(a, b){ return '<span class="fracc"><span class="fa">' + a + '</span><span class="fb2">' + b + "</span></span>"; }
/* Typed decimal answer with optional hints for known mistakes; tol is the accepted difference (default: exact) */
function evaluaDec(txt, esperado, pistas, tol){
  var v = leeDecimal(txt); if (v === null){ var f = leeFraccion(txt); if (f) v = f.p / f.q; }
  if (v === null) return {estado: "invalido", msg: T("Type a number, for example 8 or 7.5.", "Escriba un número, por ejemplo 8 o 7.5.")};
  if (Math.abs(v - esperado) <= (tol || 1e-6)) return {estado: "bien", msg: ""};
  for (var i = 0; i < (pistas || []).length; i++) if (Math.abs(v - pistas[i].v) <= (pistas[i].tol || tol || 1e-6)) return {estado: "mal", msg: pistas[i].msg};
  return {estado: "mal", msg: T("Check the proportion and the cross multiplication.", "Revise la proporción y la multiplicación cruzada.")};
}
/* Triangle with sides a = BC, b = CA, c = AB: vertices A, B, C */
function verticesDe(a, b, c){ var x = (b * b + c * c - a * a) / (2 * c), y = Math.sqrt(Math.max(b * b - x * x, 0)); return [[0, 0], [c, 0], [x, y]]; }
function angulosDe(a, b, c){ function g(o, p, q){ return Math.acos((p * p + q * q - o * o) / (2 * p * q)) * 180 / Math.PI; } return [g(a, b, c), g(b, a, c), g(c, a, b)]; }
