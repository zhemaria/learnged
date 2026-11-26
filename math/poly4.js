/* LearnGED · Level 4 · Polynomials in one variable (Topics 2 to 5).
   A polynomial is an array of whole-number coefficients by degree: [5, −2, 3] is 3x² − 2x + 5.
   Loaded after practice.js and radicals.js (it uses T, envuelve, aleatorio).
   José M. Fernández · CC BY-NC-SA 4.0 */
function pLimpia(p){ var q = p.slice(); while (q.length > 1 && !q[q.length - 1]) q.pop(); if (!q.length) q = [0]; return q; }
function pDe(o){ var p = []; Object.keys(o).forEach(function(k){ p[+k] = (p[+k] || 0) + o[k]; }); for (var i = 0; i < p.length; i++) p[i] = p[i] || 0; return pLimpia(p); }
function pSuma(a, b){ var n = Math.max(a.length, b.length), r = []; for (var i = 0; i < n; i++) r.push((a[i] || 0) + (b[i] || 0)); return pLimpia(r); }
function pEsc(a, k){ return pLimpia(a.map(function(c){ return c * k; })); }
function pResta(a, b){ return pSuma(a, pEsc(b, -1)); }
function pMul(a, b){ var r = []; for (var i = 0; i < a.length + b.length - 1; i++) r.push(0); a.forEach(function(x, i){ b.forEach(function(y, j){ r[i + j] += x * y; }); }); return pLimpia(r); }
function pMono(c, g){ var r = []; for (var i = 0; i < g; i++) r.push(0); r.push(c); return pLimpia(r); }
function pGrado(p){ p = pLimpia(p); return p.length === 1 && !p[0] ? 0 : p.length - 1; }
function pTerminos(p){ return p.filter(function(c){ return c; }).length; }
function pEval(p, x){ return p.reduce(function(s, c, i){ return s + c * Math.pow(x, i); }, 0); }
function pIgual(a, b){ a = pLimpia(a); b = pLimpia(b); return a.length === b.length && a.every(function(c, i){ return c === b[i]; }); }
function pClave(p){ return pLimpia(p).join(","); }
var SUPS = {"0": "⁰", "1": "¹", "2": "²", "3": "³", "4": "⁴", "5": "⁵", "6": "⁶", "7": "⁷", "8": "⁸", "9": "⁹"};
/* One term: c·x^g. orden: list of [c, g] in the order they are written (standard form unless given) */
function tVis(c, g, primero, v){
  v = v || "x"; var a = Math.abs(c), cuerpo = g === 0 ? String(a) : (a === 1 ? "" : a) + v + (g > 1 ? "<sup>" + g + "</sup>" : "");
  return (c < 0 ? (primero ? "−" : " − ") : (primero ? "" : " + ")) + cuerpo;
}
function tVoz(c, g, primero, v){
  v = v || "x"; var a = Math.abs(c), pot = g === 0 ? "" : (g === 1 ? v : g === 2 ? v + T(" squared", " al cuadrado") : g === 3 ? v + T(" cubed", " al cubo") : v + T(" to the ", " a la ") + g), cuerpo = g === 0 ? String(a) : (a === 1 ? "" : a + " ") + pot;
  return (c < 0 ? (primero ? T("negative ", "menos ") : T(" minus ", " menos ")) : (primero ? "" : T(" plus ", " más "))) + cuerpo;
}
function listaTerm(p, orden){ if (orden) return orden; var l = []; for (var g = p.length - 1; g >= 0; g--) if (p[g]) l.push([p[g], g]); return l; }
function pVis(p, orden, v){ var l = listaTerm(p, orden); if (!l.length) return "0"; return l.map(function(t, i){ return tVis(t[0], t[1], i === 0, v); }).join(""); }
function pVoz(p, orden, v){ var l = listaTerm(p, orden); if (!l.length) return "0"; return l.map(function(t, i){ return tVoz(t[0], t[1], i === 0, v); }).join(""); }
function pHTML(p, orden, v){ return envuelve(pVis(p, orden, v), pVoz(p, orden, v)); }
function opP(p){ return {clave: pClave(p), html: pHTML(p)}; }
/* Reads a typed polynomial: 3x^2 - 2x + 5, 3x² − 2x + 5, -x^3+x. Any single letter is taken as the variable. Returns an array or null. */
function pLee(txt){
  var s = String(txt).replace(/\s+/g, "").replace(/[−–]/g, "-").replace(/[⁰¹²³⁴⁵⁶⁷⁸⁹]+/g, function(m){ return "^" + m.split("").map(function(ch){ for (var k in SUPS) if (SUPS[k] === ch) return k; return ""; }).join(""); }).replace(/\*\*/g, "^").replace(/·|\*/g, "");
  if (!s) return null;
  var letras = s.match(/[a-z]/gi); if (letras && letras.some(function(l){ return l.toLowerCase() !== letras[0].toLowerCase(); })) return null;
  if (letras) s = s.replace(new RegExp(letras[0], "gi"), "x");
  if (!/^[-+]?[\dx.^]/.test(s)) return null;
  var partes = s.match(/[-+]?[^-+]+/g), p = {}, vistos = {}, rep = false;
  if (!partes || partes.join("") !== s.replace(/^\+/, "") && partes.join("") !== s) return null;
  for (var i = 0; i < partes.length; i++){
    var m = partes[i].match(/^([-+]?)(\d*\.?\d*)(x(?:\^(\d+))?)?$/);
    if (!m || (!m[2] && !m[3])) return null;
    var c = m[2] === "" ? 1 : parseFloat(m[2]); if (isNaN(c)) return null; if (m[1] === "-") c = -c;
    var g = m[3] ? (m[4] ? parseInt(m[4], 10) : 1) : 0;
    if (vistos[g]) rep = true; vistos[g] = 1;
    p[g] = (p[g] || 0) + c;
  }
  var r = pDe(p); r.repetidos = rep; return r;
}
/* Checks a typed polynomial. trampas: [{p, msg}] known wrong answers with their hint */
function evaluaP(txt, ok, trampas, extra){
  var p = pLee(txt);
  if (!p) return {estado: "invalido", msg: T("Type a polynomial like 3x^2 − 2x + 5 (use ^ for the exponent: x^2).", "Escriba un polinomio como 3x^2 − 2x + 5 (use ^ para el exponente: x^2).")};
  if (pIgual(p, ok)) return p.repetidos ? {estado: "invalido", msg: T("The value is right, but combine the like terms: write each power of x only once.", "El valor está bien, pero combine los términos semejantes: escriba cada potencia de x una sola vez.")} : {estado: "bien"};
  for (var i = 0; i < (trampas || []).length; i++) if (pIgual(p, trampas[i].p)) return {estado: "mal", msg: trampas[i].msg};
  if (extra){ var m = extra(p); if (m) return {estado: "mal", msg: m}; }
  return {estado: "mal", msg: T("Check each term again: its coefficient, its sign, and its exponent.", "Revise cada término otra vez: su coeficiente, su signo y su exponente.")};
}
function azarP(grado, nterm, max){
  var gs = []; for (var g = 0; g <= grado; g++) gs.push(g);
  var elegidos = [grado].concat(baraja(gs.slice(0, grado)).slice(0, Math.max(0, nterm - 1))), o = {};
  elegidos.forEach(function(g){ var c; do { c = aleatorio(-(max || 9), max || 9); } while (!c); o[g] = c; });
  return pDe(o);
}
