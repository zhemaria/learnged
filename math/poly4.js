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

/* ---------- Factored forms ----------
   A factored form is {k: whole number, m: power of x outside, f: [polynomials]} meaning k · x^m · f1 · f2 … */
function mcdLista(l){ return l.reduce(function(a, b){ return mcd(a, Math.abs(b)); }, 0); }
function contenido(p){ return mcdLista(p) || 1; }
function fProducto(F){ var r = pMono(F.k, F.m || 0); F.f.forEach(function(q){ r = pMul(r, q); }); return r; }
/* (x + 3), (2x − 5), (x + 3)² written with plain text */
function factorVis(q){ return "(" + pVis(q) + ")"; }
function fVis(F){
  var pre = "", k = F.k, m = F.m || 0;
  if (m) pre = (k === 1 ? "" : k === -1 ? "−" : sg(k)) + "x" + (m > 1 ? "<sup>" + m + "</sup>" : "");
  else if (k !== 1 || !F.f.length) pre = k === -1 && F.f.length ? "−" : sg(k);
  var partes = [], i = 0;
  while (i < F.f.length){ var j = i; while (j + 1 < F.f.length && pIgual(F.f[j + 1], F.f[i])) j++; partes.push(factorVis(F.f[i]) + (j > i ? "<sup>" + (j - i + 1) + "</sup>" : "")); i = j + 1; }
  return pre + partes.join("");
}
function fVoz(F){
  var k = F.k, m = F.m || 0, s = [];
  if (k !== 1 || m) s.push((k === -1 ? T("negative ", "menos ") : (k !== 1 ? sg(k).replace("−", T("negative ", "menos ")) + " " : "")) + (m ? (m === 1 ? "x" : "x " + T("to the ", "a la ") + m) : ""));
  F.f.forEach(function(q){ s.push(T("the quantity ", "la cantidad ") + pVoz(q)); });
  return s.join(T(" times ", " por "));
}
function fHTML(F){ return envuelve(fVis(F), fVoz(F)); }
function opF(F){ return {clave: fClave(F), html: fHTML(F)}; }
function fClave(F){ return F.k + "|" + (F.m || 0) + "|" + F.f.map(pClave).sort().join(";"); }
/* Reads a typed factored form: 2(x+5)(x-5), 4x(2x+3), (x+3)^2, -3(x-1)(x+2), x^2(x+4). Returns {F, prod} or null. */
function fLee(txt){
  var s = String(txt).replace(/\s+/g, "").replace(/[−–]/g, "-").replace(/[·*×]/g, "").replace(/[⁰¹²³⁴⁵⁶⁷⁸⁹]+/g, function(m){ return "^" + m.split("").map(function(ch){ for (var k in SUPS) if (SUPS[k] === ch) return k; return ""; }).join(""); });
  if (!s) return null;
  var letras = s.match(/[a-z]/gi); if (letras && letras.some(function(l){ return l.toLowerCase() !== letras[0].toLowerCase(); })) return null;
  if (letras) s = s.replace(new RegExp(letras[0], "gi"), "x");
  var m0 = s.match(/^([-+]?\d*)(x(?:\^(\d+))?)?(?=\(|$)/);
  if (!m0) return null;
  var resto = s.slice(m0[0].length), k = m0[1] === "" || m0[1] === "+" ? 1 : (m0[1] === "-" ? -1 : parseInt(m0[1], 10)), m = m0[2] ? (m0[3] ? +m0[3] : 1) : 0, f = [];
  if (!resto && !m0[0]) return null;
  var re = /^\(([^()]+)\)(?:\^(\d+))?/;
  while (resto){ var mm = resto.match(re); if (!mm) return null; var q = pLee(mm[1]); if (!q) return null; var e = mm[2] ? +mm[2] : 1; for (var i = 0; i < e; i++) f.push(q); resto = resto.slice(mm[0].length); }
  var F = {k: k, m: m, f: f};
  return {F: F, prod: fProducto(F)};
}
/* Is a polynomial factor "finished"? (degree 1 with no common number, or a quadratic with no whole-number roots and no common number) */
function primo(q){ var g = pGrado(q); if (g === 0) return true; if (contenido(q) !== 1) return false; if (g === 1) return true; if (g === 2){ var a = q[2], b = q[1], c = q[0], d = b * b - 4 * a * c; return !(d >= 0 && esCuadrado(d)) || false; } return false; }
/* Checks a typed factored answer against the polynomial ok. trampas: [{p (product) or F, msg}] */
function evaluaF(txt, ok, trampas){
  var r = fLee(txt);
  if (!r) return {estado: "invalido", msg: T("Type the factors with parentheses, like 3(x + 2) or (x − 4)(x + 4). Use ^ for exponents.", "Escriba los factores con paréntesis, como 3(x + 2) o (x − 4)(x + 4). Use ^ para los exponentes.")};
  var F = r.F;
  for (var i = 0; i < (trampas || []).length; i++){ var tp = trampas[i]; if (tp.F ? fClave(tp.F) === fClave(F) : pIgual(r.prod, tp.p) && !pIgual(r.prod, ok)) return {estado: "mal", msg: tp.msg}; }
  if (!pIgual(r.prod, ok)) return {estado: "mal", msg: T("Multiply your factors to check: they do not give back the polynomial. Look at the signs and the numbers.", "Multiplique sus factores para comprobar: no devuelven el polinomio. Revise los signos y los números.")};
  if (!F.f.length || (F.f.length === 1 && pGrado(F.f[0]) === pGrado(ok) && F.k === 1 && !F.m)) return {estado: "mal", msg: T("That is the same polynomial. Write it as a product of factors.", "Ese es el mismo polinomio. Escríbalo como un producto de factores.")};
  var gx = 0; F.f.forEach(function(q){ if (!q[0]) gx++; });
  var fin = F.f.every(primo) && !gx;
  if (!fin) return {estado: "mal", msg: F.f.some(function(q){ return contenido(q) !== 1 || !q[0]; }) ? T("The product is right, but a factor still has a common factor inside. Take it out.", "El producto está bien, pero dentro de un factor todavía queda un factor común. Sáquelo.") : T("The product is right, but it can be factored further: look at what is left inside the parentheses.", "El producto está bien, pero todavía se puede factorizar más: mire lo que queda dentro del paréntesis.")};
  return {estado: "bien"};
}
