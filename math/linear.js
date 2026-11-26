/* LearnGED · math/linear.js — shared engine for Level 3 · Topic 4 (linear algebra).
   Exact fractions {n, d}, linear equations ax + b = cx + d, and polynomials with terms in x², x, y and constants.
   Works in English and Spanish. Load after practice.js and radicals.js (it uses T, mcd, envuelve, fracVis, fracVoz,
   fracHTML, leeFraccion and leeDecimal from radicals.js).
   Ported from GEDparaHispanos (algebra/n3-l4-*.html). José M. Fernández · CC BY-NC-SA 4.0 */

function fr(n, d){ if (d === undefined) d = 1; if (d < 0){ n = -n; d = -d; } var g = mcd(n, d) || 1; return {n: n / g, d: d / g}; }
function fsum(a, b){ return fr(a.n * b.d + b.n * a.d, a.d * b.d); }
function fres(a, b){ return fr(a.n * b.d - b.n * a.d, a.d * b.d); }
function fmul(a, b){ return fr(a.n * b.n, a.d * b.d); }
function fdiv(a, b){ return fr(a.n * b.d, a.d * b.n); }
function fneg(a){ return fr(-a.n, a.d); }
function figual(a, b){ return a.n === b.n && a.d === b.d; }
function fcero(a){ return a.n === 0; }
function fent(a){ return a.d === 1; }
function fval(a){ return a.n / a.d; }
function mcm(a, b){ return a / mcd(a, b) * b; }
/* Visual minus sign: −3 instead of -3 */
function menosV(t){ return String(t).replace(/-/g, "−"); }
function fTxt(a){ return a.d === 1 ? menosV(a.n) : menosV(a.n) + "/" + a.d; }
/* Exact decimal of a fraction, or null if it does not end */
function fDecimal(a){
  var d = a.d; while (d % 2 === 0) d /= 2; while (d % 5 === 0) d /= 5;
  if (d !== 1) return null;
  for (var k = 0; k <= 6; k++){ var p = Math.pow(10, k); if ((p * a.n) % a.d === 0) return menosV((a.n / a.d).toFixed(k)); }
  return null;
}
function fHTML(a, modo){ if (modo === "dec"){ var s = fDecimal(a); if (s !== null) return s; } return fracHTML(a.n, a.d); }
function numVoz(a){ return a.d === 1 ? String(a.n).replace("-", T("negative ", "menos ")) : fracVoz(a.n, a.d); }

/* One side of an equation: {x: fr, k: fr}. Mode "frac" writes x/2 or 3x/4; mode "dec" writes 0.25x */
function L(x, k){ return {x: x.n !== undefined ? x : fr(x), k: k.n !== undefined ? k : fr(k)}; }
var MAS = T(" plus ", " más "), MENOS = T(" minus ", " menos "), NEG = T("negative ", "menos ");
function termXVis(c, modo, primero){
  var neg = c.n < 0, a = fr(Math.abs(c.n), c.d), cuerpo;
  if (modo === "dec" && a.d !== 1 && fDecimal(a) !== null) cuerpo = fDecimal(a) + "x";
  else if (a.d === 1) cuerpo = (a.n === 1 ? "" : a.n) + "x";
  else cuerpo = '<span class="fracc"><span class="fa">' + (a.n === 1 ? "" : a.n) + 'x</span><span class="fb2">' + a.d + "</span></span>";
  return (neg ? (primero ? "−" : " − ") : (primero ? "" : " + ")) + cuerpo;
}
function termXVoz(c, primero){
  var neg = c.n < 0, a = fr(Math.abs(c.n), c.d), cuerpo;
  if (a.d === 1) cuerpo = (a.n === 1 ? "" : a.n + " ") + "x";
  else cuerpo = (a.n === 1 ? "" : a.n + " ") + T("x over ", "x sobre ") + a.d;
  return (neg ? (primero ? NEG : MENOS) : (primero ? "" : MAS)) + cuerpo;
}
function constVis(c, modo, primero){
  var neg = c.n < 0, a = fr(Math.abs(c.n), c.d);
  var cuerpo = (modo === "dec" && fDecimal(a) !== null) ? fDecimal(a) : (a.d === 1 ? String(a.n) : fracVis(a.n, a.d));
  return (neg ? (primero ? "−" : " − ") : (primero ? "" : " + ")) + cuerpo;
}
function constVoz(c, primero){
  var neg = c.n < 0, a = fr(Math.abs(c.n), c.d), cuerpo = a.d === 1 ? String(a.n) : fracVoz(a.n, a.d);
  return (neg ? (primero ? NEG : MENOS) : (primero ? "" : MAS)) + cuerpo;
}
function ladoVis(l, modo){ var s = ""; if (!fcero(l.x)) s += termXVis(l.x, modo, true); if (!fcero(l.k) || s === "") s += constVis(l.k, modo, s === ""); return s; }
function ladoVoz(l){ var s = ""; if (!fcero(l.x)) s += termXVoz(l.x, true); if (!fcero(l.k) || s === "") s += constVoz(l.k, s === ""); return s; }
function ecHTML(izq, der, modo){ return envuelve(ladoVis(izq, modo) + " = " + ladoVis(der, modo), ladoVoz(izq) + T(" equals ", " es igual a ") + ladoVoz(der)); }
function ladoHTML(l, modo){ return envuelve(ladoVis(l, modo), ladoVoz(l)); }
function evalLado(l, v){ return fsum(fmul(l.x, v), l.k); }
/* Solution: {tipo: "una"|"ninguna"|"infinitas", x} */
function resuelve(izq, der){
  var a = fres(izq.x, der.x), b = fres(der.k, izq.k);
  if (fcero(a)) return {tipo: fcero(b) ? "infinitas" : "ninguna"};
  return {tipo: "una", x: fdiv(b, a)};
}
function numVis(v, modo){ return (modo === "dec" && fDecimal(v) !== null) ? fDecimal(v) : fracVis(v.n, v.d); }
function xIgual(v, modo){ return envuelve("x = " + numVis(v, modo), T("x equals ", "x igual a ") + numVoz(v)); }
function numHTML(v, modo){ return envuelve(numVis(v, modo), numVoz(v)); }
function opX(v, modo){ return {html: xIgual(v, modo), clave: "x" + v.n + "/" + v.d}; }

/* Polynomials of Lesson 4.1: a list of terms {c, v} with v in "x2", "x", "y", "" (constant) */
var VAR_VIS = {x2: "x<sup>2</sup>", x: "x", y: "y", "": ""};
var VAR_VOZ = {x2: T("x squared", "x al cuadrado"), x: "x", y: "y", "": ""};
function termVis(t, primero){
  var neg = t.c < 0, a = Math.abs(t.c), cuerpo = t.v === "" ? String(a) : (a === 1 ? "" : a) + VAR_VIS[t.v];
  return (neg ? (primero ? "−" : " − ") : (primero ? "" : " + ")) + cuerpo;
}
function termVoz(t, primero){
  var neg = t.c < 0, a = Math.abs(t.c), cuerpo = t.v === "" ? String(a) : (a === 1 ? "" : a + " ") + VAR_VOZ[t.v];
  return (neg ? (primero ? NEG : MENOS) : (primero ? "" : MAS)) + cuerpo;
}
function polVis(p){ if (!p.length) return "0"; return p.map(function(t, i){ return termVis(t, i === 0); }).join(""); }
function polVoz(p){ if (!p.length) return "0"; return p.map(function(t, i){ return termVoz(t, i === 0); }).join(""); }
function polHTML(p){ return envuelve(polVis(p), polVoz(p)); }
function polClave(p){ return p.map(function(t){ return t.c + t.v; }).join("|") || "0"; }
function opPol(p){ return {html: polHTML(p), clave: polClave(p)}; }
var ORDEN_VAR = ["x2", "x", "y", ""];
/* Combines like terms and orders them: x², x, y, constant */
function reducePol(p){
  var s = {}; p.forEach(function(t){ s[t.v] = (s[t.v] || 0) + t.c; });
  return ORDEN_VAR.filter(function(v){ return s[v]; }).map(function(v){ return {c: s[v], v: v}; });
}
function tm(c, v){ return {c: c, v: v || ""}; }

/* Typed numeric answer (for creaPracticaLibre) */
function evaluaNumero(txt, esperado, pistas){
  var f = leeFraccion(txt), dcm = leeDecimal(txt);
  if (!f && dcm === null) return {estado: "invalido", msg: T("Type a whole number, a decimal, or a fraction like 3/4.", "Escriba un número entero, un decimal o una fracción como 3/4.")};
  var v = f ? fr(f.p, f.q) : null;
  var ok = v ? figual(v, esperado) : Math.abs(dcm - fval(esperado)) < 1e-9;
  if (ok) return {estado: "bien", msg: ""};
  if (pistas){ for (var i = 0; i < pistas.length; i++){ var pv = pistas[i]; if ((v && figual(v, pv.v)) || (!v && Math.abs(dcm - fval(pv.v)) < 1e-9)) return {estado: "mal", msg: pv.msg}; } }
  return {estado: "mal", msg: T("Check the steps again.", "Revise los pasos otra vez.")};
}
/* Typed whole number (accepts −, – or -) */
function leeEntero(txt){ var s = String(txt).trim().replace(/\s+/g, "").replace(/[−–]/g, "-"); return /^-?\d+$/.test(s) ? parseInt(s, 10) : null; }

/* Screen-reader text made from the visual HTML */
function vozAuto(vis){
  return vis.replace(/<sup>2<\/sup>/g, T(" squared", " al cuadrado")).replace(/<span class="fracc"><span class="fa">(.*?)<\/span><span class="fb2">(.*?)<\/span><\/span>/g, "$1" + T(" over ", " sobre ") + "$2")
            .replace(/<[^>]+>/g, "").replace(/−/g, T(" minus ", " menos ")).replace(/·/g, T(" times ", " por ")).replace(/\s+/g, " ").replace(/\(\s+/g, "(").trim();
}
function auto(vis){ return envuelve(vis, vozAuto(vis)); }
function nz(){ var n = aleatorio(1, 9); return Math.random() < 0.5 ? -n : n; }
