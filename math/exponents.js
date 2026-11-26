/* LearnGED · math/exponents.js — shared engine for Level 3 · Topic 1 (rules of exponents).
   Works in English and Spanish: practice.js sets ES from <html lang>.
   Load after practice.js. Ported from GEDparaHispanos (algebra/n3-l1-*.html), with two tries per exercise.
   José M. Fernández · CC BY-NC-SA 4.0 */

function T(en, es){ return ES ? es : en; }
function mezcla(a){ return baraja(a); }
var ale = aleatorio;
function mcd(a, b){ a = Math.abs(a); b = Math.abs(b); while (b){ var t = a % b; a = b; b = t; } return a || 1; }
var MENOS = "−";
function numTxt(n){ return n < 0 ? MENOS + Math.abs(n) : String(n); }
function numVoz(n){ return n < 0 ? T("minus ", "menos ") + Math.abs(n) : String(n); }
function fmt(n){ return (n < 0 ? MENOS : "") + Math.abs(n).toLocaleString("en-US"); }
var VZ = ES ? { pot: " elevado a la ", por: " por ", entre: " entre ", igual: " igual a ", sobre: " sobre ", abre: "abre paréntesis ", cierra: " cierra paréntesis", cuanto: " elevado a la cuánto" }
            : { pot: " to the power of ", por: " times ", entre: " divided by ", igual: " equals ", sobre: " over ", abre: "open parenthesis ", cierra: " close parenthesis", cuanto: " to what power" };

/* ---------- Visual expression: {h: visible HTML, s: spoken text} ---------- */
function X(h, s){ return {h: h, s: s}; }
function ver(x){ return '<span class="ex"><span aria-hidden="true">' + x.h + '</span><span class="sr-only">' + x.s + '</span></span>'; }
function supH(e){ return "<sup>" + numTxt(e) + "</sup>"; }
function potX(baseH, baseS, e){ if (e === 1) return X(baseH, baseS); return X(baseH + supH(e), baseS + VZ.pot + numVoz(e)); }
function parX(x, e){
  var d = X("(" + x.h + ")", VZ.abre + x.s + VZ.cierra);
  if (e === undefined || e === null) return d;
  return X(d.h + supH(e), d.s + VZ.pot + numVoz(e));
}
function porX(a, b){ return X(a.h + ' <span class="signo">·</span> ' + b.h, a.s + VZ.por + b.s); }
function entreX(a, b){ return X(a.h + ' <span class="signo">÷</span> ' + b.h, a.s + VZ.entre + b.s); }
function igualX(a, b){ return X(a.h + ' <span class="signo">=</span> ' + b.h, a.s + VZ.igual + b.s); }
function fracX(n, d){ return X('<span class="frac"><span class="arriba">' + n.h + '</span><span class="abajo">' + d.h + '</span></span>', n.s + VZ.sobre + d.s); }
function txtX(t){ return X(t, t); }
function xp(v, e){ return potX(v, v, e); }
function preg(v){ return X(v + "<sup>?</sup>", v + VZ.cuanto); }

/* ---------- Monomials: coefficient n/d and an exponent for each variable ---------- */
function M(n, d, e, orden){
  e = e || {};
  if (d < 0){ n = -n; d = -d; }
  var g = mcd(n, d), o = [];
  (orden || []).concat(Object.keys(e)).forEach(function(k){ if (o.indexOf(k) < 0) o.push(k); });
  return {n: n / g, d: d / g, e: e, o: o};
}
function mono(c, e){ return M(c, 1, e || {}); }
function e1(v, k){ var o = {}; o[v] = k; return o; }
function xv(v, e){ return mono(1, e1(v, e)); }
function copiaE(e){ var r = {}; for (var k in e) r[k] = e[k]; return r; }
function mMul(A, B){ var e = copiaE(A.e); for (var k in B.e) e[k] = (e[k] || 0) + B.e[k]; return M(A.n * B.n, A.d * B.d, e, A.o.concat(B.o)); }
function mPow(A, k){ var e = {}; for (var v in A.e) e[v] = A.e[v] * k; return M(Math.pow(A.n, k), Math.pow(A.d, k), e, A.o); }
function mDiv(A, B){ var e = copiaE(A.e); for (var k in B.e) e[k] = (e[k] || 0) - B.e[k]; return M(A.n * B.d, A.d * B.n, e, A.o.concat(B.o)); }
function mIgual(A, B){
  if (A.n !== B.n || A.d !== B.d) return false;
  var ks = {}, k;
  for (k in A.e) if (A.e[k] !== 0) ks[k] = 1;
  for (k in B.e) if (B.e[k] !== 0) ks[k] = 1;
  for (k in ks) if ((A.e[k] || 0) !== (B.e[k] || 0)) return false;
  return true;
}
/* Exact value (a fraction) when the variables are replaced by numbers */
function mValor(A, env){
  var n = A.n, d = A.d;
  A.o.forEach(function(v){ var e = A.e[v] || 0, x = env[v]; if (e > 0) n *= Math.pow(x, e); else if (e < 0) d *= Math.pow(x, -e); });
  if (d < 0){ n = -n; d = -d; }
  var g = mcd(n, d);
  return {n: n / g, d: d / g};
}
function ratX(r){
  if (r.d === 1) return X(numTxt(r.n), numVoz(r.n));
  return X((r.n < 0 ? MENOS : "") + Math.abs(r.n) + "/" + r.d, (r.n < 0 ? T("minus ", "menos ") : "") + Math.abs(r.n) + VZ.sobre + r.d);
}
function valX(r){
  if (r.d === 1) return X(fmt(r.n), numVoz(r.n));
  return X((r.n < 0 ? MENOS : "") + fmt(Math.abs(r.n)) + "/" + fmt(r.d), (r.n < 0 ? T("minus ", "menos ") : "") + Math.abs(r.n) + VZ.sobre + r.d);
}
function ratIgual(a, b){ return a.n === b.n && a.d === b.d; }

/* Parts of a monomial: coefficient and variables with exponents */
function partesX(coef, vars, uno){
  var h = "", s = [], hay = vars.length > 0;
  if (coef === -1 && hay){ h += MENOS; s.push(T("minus", "menos")); }
  else if (coef !== 1 || !hay || uno){ h += numTxt(coef); s.push(numVoz(coef)); }
  vars.forEach(function(p){ var x = potX(p[0], p[0], p[1]); h += x.h; s.push(x.s); });
  return X(h, s.join(" "));
}
/* In-line form: allows negative exponents (a middle step) */
function mLinea(A, verCero){
  var vars = [];
  A.o.forEach(function(v){ var e = A.e[v]; if (e === undefined) return; if (e !== 0 || verCero) vars.push([v, e]); });
  if (A.d !== 1){
    var f = fracX(partesX(Math.abs(A.n), [], false), X(String(A.d), String(A.d))), resto = partesX(1, vars, false);
    return X((A.n < 0 ? MENOS : "") + f.h + (vars.length ? resto.h : ""), (A.n < 0 ? T("minus ", "menos ") : "") + f.s + (vars.length ? VZ.por + resto.s : ""));
  }
  return partesX(A.n, vars, false);
}
/* Final form: positive exponents only, as a fraction when needed */
function mFinal(A){
  var arriba = [], abajo = [];
  A.o.forEach(function(v){ var e = A.e[v] || 0; if (e > 0) arriba.push([v, e]); else if (e < 0) abajo.push([v, -e]); });
  if (A.d === 1 && abajo.length === 0) return partesX(A.n, arriba, false);
  var f = fracX(partesX(Math.abs(A.n), arriba, false), partesX(A.d, abajo, false));
  return A.n < 0 ? X(MENOS + f.h, T("minus ", "menos ") + f.s) : f;
}

/* ---------- Chips: each factor of the base as a visible chip ---------- */
function fichas(base, cuantas, clase, tachadas){
  var h = "";
  for (var i = 0; i < cuantas; i++) h += '<span class="ficha' + (clase ? " " + clase : "") + (tachadas && i < tachadas ? " tachada" : "") + '">' + base + "</span>";
  return h;
}

/* ---------- Answer choices with no repeats ---------- */
function opcionesMono(correcto, distractores, fbBien, forma){
  var pinta = forma === "linea" ? mLinea : mFinal;
  var lista = [{x: pinta(correcto), ok: true, fb: fbBien || ""}], vistos = [correcto];
  distractores.forEach(function(d){
    if (lista.length >= 4) return;
    for (var i = 0; i < vistos.length; i++) if (mIgual(vistos[i], d[0])) return;
    vistos.push(d[0]); lista.push({x: pinta(d[0]), ok: false, fb: d[1] || ""});
  });
  var v0 = correcto.o.filter(function(v){ return (correcto.e[v] || 0) !== 0; })[0], cambios = [1, -1, 2, 3, -2];
  for (var i = 0; i < cambios.length && lista.length < 4; i++){
    var e = copiaE(correcto.e), m;
    if (v0){ e[v0] = e[v0] + cambios[i]; m = M(correcto.n, correcto.d, e, correcto.o); } else m = M(correcto.n + cambios[i], correcto.d, e, correcto.o);
    var rep = false;
    for (var j = 0; j < vistos.length; j++) if (mIgual(vistos[j], m)) rep = true;
    if (!rep){ vistos.push(m); lista.push({x: pinta(m), ok: false, fb: ""}); }
  }
  return lista;
}
function unicas(lista){
  var vistos = {}, r = [];
  lista.forEach(function(o){ var c = o.x ? o.x.h : o.html; if (vistos[c] || r.length >= 4) return; vistos[c] = true; r.push(o); });
  return r;
}
function numOp(v, ok, fb){ return {x: X(numTxt(v), numVoz(v)), ok: ok, fb: fb || ""}; }
function htmlOp(h, ok, fb){ return {html: h, ok: ok, fb: fb || ""}; }
function pasosHTML(lista){
  return '<div class="pasos">' + lista.map(function(p, i){ return '<div class="paso"><span class="n" aria-hidden="true">' + (i + 1) + "</span>" + p + "</div>"; }).join("") + "</div>";
}
function R_(t){ return ' <span class="regla">' + t + "</span>"; }

/* ---------- Number boxes in the explorers ---------- */
function leeEntero(id, min, max, aviso, nombre){
  var v = parseInt($(id).value, 10);
  if (isNaN(v) || v < min || v > max){
    $(id).classList.add("error");
    $(aviso).className = "caja-aviso visible";
    $(aviso).textContent = T("The " + nombre + " must be a whole number from " + min + " to " + max + ".", "El " + nombre + " debe ser un número entero entre " + min + " y " + max + ".");
    return null;
  }
  $(id).classList.remove("error");
  return v;
}
function limpiaAviso(aviso){ $(aviso).className = "caja-aviso"; $(aviso).textContent = ""; }
function leeEnt(t){ t = String(t).trim().replace(/−|–|—/g, "-").replace(/\s+/g, ""); return /^-?\d+$/.test(t) ? parseInt(t, 10) : NaN; }

/* ---------- Practice adapters: the generators of each module → practice.js (two tries) ----------
   Multiple choice: gen() returns {enun, opciones: [{x | html, ok, fb}], sol, regla?}.
   The fb of a wrong choice is its hint; the fb of the right choice goes with the explanation. */
function OM(pre, gen, reglas){
  var actual = null;
  creaPracticaOM(pre, function(){
    var q = gen(), ops = q.opciones.map(function(o, i){ return {html: o.x ? ver(o.x) : o.html, clave: "k" + i, ok: o.ok, fb: o.fb || ""}; });
    var cor = ops.filter(function(o){ return o.ok; })[0] || ops[0], pistas = {};
    ops.forEach(function(o){ if (!o.ok && o.fb) pistas[o.clave] = o.fb; });
    var expl = (cor.fb ? cor.fb + " " : "") + (q.sol || "");
    actual = q;
    return {enun: q.enun, opciones: ops.map(function(o){ return {html: o.html, clave: o.clave}; }), correcta: cor.clave, pistas: pistas,
            pista: q.pista || T("Check which rule fits and try again.", "Revise qué regla corresponde y vuelva a intentarlo."), bien: expl, mal: expl, enOrden: q.enOrden};
  });
  if (!reglas) return;
  /* Score by rule: tells the student which rule to review */
  var est = {}, caja = document.createElement("div");
  reglas.forEach(function(r){ est[r[0]] = {nombre: r[1], a: 0, t: 0}; });
  caja.className = "marcador-regla"; $(pre).appendChild(caja);
  function pinta(){
    caja.innerHTML = "<table><caption>" + T("Right answers by rule", "Aciertos por regla") + '</caption><thead><tr><th scope="col">' + T("Rule", "Regla") + '</th><th scope="col">' + T("Right", "Aciertos") + "</th></tr></thead><tbody>" +
      reglas.map(function(r){ var x = est[r[0]]; return "<tr><td>" + x.nombre + "</td><td>" + x.a + T(" of ", " de ") + x.t + "</td></tr>"; }).join("") + "</tbody></table>";
  }
  var fb = $(pre + "-fb"), contado = null;
  new MutationObserver(function(){
    var c = fb.className, q = actual;
    if (!q || contado === q || !q.regla || !est[q.regla]) return;
    if (c.indexOf("bien") >= 0 || c.indexOf("mal") >= 0){ contado = q; est[q.regla].t++; if (c.indexOf("bien") >= 0) est[q.regla].a++; pinta(); }
  }).observe(fb, {attributes: true, attributeFilter: ["class"]});
  pinta();
}
/* Typed integer: gen() returns {enun, etiqueta, resp, pista(v) → HTML | null, sol} */
function ESCRITA(pre, gen){
  creaPracticaLibre(pre, function(){
    var q = gen(), lab = document.querySelector('label[for="' + pre + '-r"]');
    if (lab && q.etiqueta) lab.textContent = q.etiqueta;
    return {enun: q.enun, solucion: q.sol,
      evalua: function(t){
        var v = leeEnt(t);
        if (isNaN(v)) return {estado: "invalido", msg: T("Type a whole number (it can start with a minus sign).", "Escriba un número entero (puede empezar con el signo menos).")};
        if (v === q.resp) return {estado: "bien"};
        return {estado: "mal", msg: (q.pista && q.pista(v)) || T("Check the rule.", "Revise la regla.")};
      }};
  });
}
