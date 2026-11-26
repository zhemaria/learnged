/* LearnGED · Level 3 · Topic 8 · Counting and probability engine, prob3.js (English and Spanish)
   Loaded after radicals.js, linear.js, inequalities.js, geometry3.js, and data3.js.
   José M. Fernández · CC BY-NC-SA 4.0 */
function fact(n){ var r = 1; for (var i = 2; i <= n; i++) r *= i; return r; }
function perm(n, r){ var p = 1; for (var i = 0; i < r; i++) p *= (n - i); return p; }
function comb(n, r){ return perm(n, r) / fact(r); }
function factores(n, r){ var a = []; for (var i = 0; i < r; i++) a.push(n - i); return a.join(" × "); }
var LETRAS = "ABCDEFGH".split("");
/* All the ordered lists (permutations) and all the groups (combinations) of r items taken from elem */
function permutaciones(elem, r){
  if (r === 0) return [[]];
  var out = [];
  elem.forEach(function(e, i){ var resto = elem.slice(0, i).concat(elem.slice(i + 1)); permutaciones(resto, r - 1).forEach(function(p){ out.push([e].concat(p)); }); });
  return out;
}
function combinaciones(elem, r){
  if (r === 0) return [[]]; if (elem.length < r) return [];
  var out = [];
  combinaciones(elem.slice(1), r - 1).forEach(function(c){ out.push([elem[0]].concat(c)); });
  return out.concat(combinaciones(elem.slice(1), r));
}
/* Whole-number answer with hints */
function evaluaEntero(txt, esperado, pistas, otro){
  var v = leeDecimal(String(txt).replace(/,/g, ""));
  if (v === null) return {estado: "invalido", msg: T("Type a whole number, for example 120.", "Escriba un número entero, por ejemplo 120.")};
  if (Math.abs(v - esperado) < 1e-9) return {estado: "bien", msg: ""};
  for (var i = 0; i < (pistas || []).length; i++) if (Math.abs(v - pistas[i].v) < 1e-9) return {estado: "mal", msg: pistas[i].msg};
  return {estado: "mal", msg: otro || T("Check how many choices there are at each step.", "Revise cuántas opciones hay en cada paso.")};
}

/* ---------- Probability ---------- */
/* Reads 3/8, 0.375, or 37.5% → a number; null if it cannot */
function leeProb(txt){
  var s = String(txt).trim().replace(/\s+/g, "").replace(/−/g, "-");
  var pc = s.match(/^(\d+(?:\.\d+)?)%$/); if (pc) return parseFloat(pc[1]) / 100;
  var f = leeFraccion(s); if (f) return f.p / f.q;
  return leeDecimal(s);
}
/* p is a fraction {n, d} from linear.js; pistas = [{v: {n, d}, msg}] */
function evaluaProb(txt, p, pistas, otro){
  var v = leeProb(txt);
  if (v === null) return {estado: "invalido", msg: T("Write the probability as a fraction (3/8), a decimal (0.375), or a percent (37.5%).", "Escriba la probabilidad como fracción (3/8), decimal (0.375) o porcentaje (37.5%).")};
  if (Math.abs(v - fval(p)) < 0.0006) return {estado: "bien", msg: ""};
  if (v > 1) return {estado: "mal", msg: T("A probability is never more than 1 (100%): you probably added when you needed to multiply.", "Una probabilidad nunca pasa de 1 (100%): probablemente se sumó cuando había que multiplicar.")};
  for (var i = 0; i < (pistas || []).length; i++) if (Math.abs(v - fval(pistas[i].v)) < 0.0006) return {estado: "mal", msg: pistas[i].msg};
  return {estado: "mal", msg: otro || T("Multiply the probability of the first event by the probability of the second.", "Multiplique la probabilidad del primer evento por la del segundo.")};
}
function frSimpl(p, q){ var r = reduce(p, q); return fracHTML(r.p, r.q); }
/* p/q = simplified ≈ decimal ≈ percent */
function tresFormas(p, q){ var v = p / q; return fracHTML(p, q) + (mcd(p, q) > 1 ? " = " + frSimpl(p, q) : "") + " ≈ " + nm(Math.round(v * 10000) / 10000) + " ≈ " + nm(Math.round(v * 1000) / 10) + "%"; }
