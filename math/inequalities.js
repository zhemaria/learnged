/* LearnGED · math/inequalities.js — shared engine for Level 3 · Topic 5 (inequalities and formulas).
   Inequalities ax + b r cx + d with exact fractions, the sign-flip rule, the number-line graph,
   and the typed practice "sign + boundary number" with two tries.
   Works in English and Spanish. Load after practice.js, radicals.js and linear.js.
   Ported from GEDparaHispanos (algebra/n3-l5-*.html). José M. Fernández · CC BY-NC-SA 4.0 */

var REL_VOZ = {"<": T("is less than", "es menor que"), ">": T("is greater than", "es mayor que"), "≤": T("is less than or equal to", "es menor o igual que"), "≥": T("is greater than or equal to", "es mayor o igual que")};
var REL_INV = {"<": ">", ">": "<", "≤": "≥", "≥": "≤"};
var REL_ESTRICTO = {"<": true, ">": true, "≤": false, "≥": false};
var RELS = ["<", ">", "≤", "≥"];
function relVis(r){ return r === "<" ? "&lt;" : (r === ">" ? "&gt;" : r); }
function ineqHTML(izq, r, der, modo){ return envuelve(ladoVis(izq, modo) + " " + relVis(r) + " " + ladoVis(der, modo), ladoVoz(izq) + " " + REL_VOZ[r] + " " + ladoVoz(der)); }
function solHTML(r, v){ return envuelve("x " + relVis(r) + " " + numVis(v), "x " + REL_VOZ[r] + " " + numVoz(v)); }
function opSol(r, v){ return {html: solHTML(r, v), clave: r + v.n + "/" + v.d}; }
function cumple(a, r, b){ var d = fval(a) - fval(b); return r === "<" ? d < -1e-12 : (r === ">" ? d > 1e-12 : (r === "≤" ? d <= 1e-12 : d >= -1e-12)); }
function derecha(r){ return r === ">" || r === "≥"; }
/* Solves izq r der: returns {r, v, invierte} or a special case */
function resuelveIneq(izq, r, der){
  var A = fres(izq.x, der.x), K = fres(der.k, izq.k);
  if (fcero(A)) return {especial: true, siempre: cumple(fr(0), r, K)};
  var inv = A.n < 0;
  return {r: inv ? REL_INV[r] : r, v: fdiv(K, A), invierte: inv, A: A, K: K};
}

/* Number line with the solution: open or closed point and a ray */
function ineqSVG(v, r, opciones){
  opciones = opciones || {};
  var c = fval(v), lo = Math.floor(c) - 5, hi = Math.floor(c) + 5;
  var W = 640, H = 110, x0 = 30, x1 = W - 30, y = 52, col = opciones.color || "#0d47a1";
  function X(tt){ return x0 + (tt - lo) * (x1 - x0) / (hi - lo); }
  var voz = opciones.voz || (r ? T("Number line: x ", "Recta numérica: x ") + REL_VOZ[r] + " " + numVoz(v) : T("Number line", "Recta numérica"));
  var s = '<svg class="recta-svg" viewBox="0 0 ' + W + " " + H + '" role="img" aria-label="' + voz + '">';
  s += '<line x1="' + (x0 - 14) + '" y1="' + y + '" x2="' + (x1 + 14) + '" y2="' + y + '" stroke="#424242" stroke-width="2"/>';
  s += '<path d="M' + (x0 - 22) + " " + y + ' l12 -7 v14 z" fill="#424242"/><path d="M' + (x1 + 22) + " " + y + ' l-12 -7 v14 z" fill="#424242"/>';
  for (var tt = lo; tt <= hi; tt++){
    s += '<line x1="' + X(tt) + '" y1="' + (y - 9) + '" x2="' + X(tt) + '" y2="' + (y + 9) + '" stroke="#424242" stroke-width="2"/>';
    s += '<text x="' + X(tt) + '" y="' + (y + 36) + '" text-anchor="middle" font-size="22" fill="#222">' + menosV(tt) + "</text>";
  }
  if (r){
    var der = derecha(r), xc = X(c), fin = der ? x1 + 18 : x0 - 18;
    s += '<line x1="' + xc + '" y1="' + y + '" x2="' + fin + '" y2="' + y + '" stroke="' + col + '" stroke-width="8"/>';
    s += '<path d="M' + (der ? fin + 12 : fin - 12) + " " + y + " l" + (der ? -18 : 18) + ' -12 v24 z" fill="' + col + '"/>';
    s += '<circle cx="' + xc + '" cy="' + y + '" r="11" fill="' + (REL_ESTRICTO[r] ? "#ffffff" : col) + '" stroke="' + col + '" stroke-width="4"/>';
  }
  if (opciones.marca !== undefined){ var xm = X(opciones.marca); s += '<path d="M' + xm + " " + (y - 16) + ' l-9 -16 h18 z" fill="#b71c1c"/>'; }
  return s + "</svg>";
}

/* Typed practice for an inequality: sign + number, two tries.
   gen() returns {enun, r, v (fr), explica, invierte} */
function creaPracticaDesig(pre, gen){
  var est = {primero: 0, pista: 0, total: 0, actual: null, resuelta: false, intentos: 0};
  function marcador(){ $(pre + "-marcador").textContent = est.total ? TX.resueltos(est.primero + est.pista, est.primero, est.total) : ""; }
  function pinta(){
    est.actual = gen(); est.resuelta = false; est.intentos = 0;
    $(pre + "-enun").innerHTML = est.actual.enun;
    $(pre + "-s").value = ""; $(pre + "-v").value = "";
    [pre + "-s", pre + "-v", pre + "-comprobar"].forEach(function(id){ $(id).disabled = false; });
    $(pre + "-v").classList.remove("error");
    $(pre + "-fb").className = "fb"; $(pre + "-fb").innerHTML = "";
  }
  function comprueba(){
    if (est.resuelta) return;
    var q = est.actual, fb = $(pre + "-fb"), r = $(pre + "-s").value, tx = $(pre + "-v").value;
    var f = leeFraccion(tx), dcm = leeDecimal(tx), v = f ? fr(f.p, f.q) : (dcm !== null ? fr(Math.round(dcm * 1000), 1000) : null);
    $(pre + "-v").classList.toggle("error", !v);
    if (!r || !v){ fb.className = "fb pista"; fb.innerHTML = T("Choose the sign and type the boundary number.", "Elija el signo y escriba el número límite."); return; }
    est.intentos++;
    var okV = figual(v, q.v), okR = r === q.r, msg;
    if (okV && okR){
      est.resuelta = true; est.total++; if (est.intentos === 1) est.primero++; else est.pista++;
      fb.className = "fb bien"; fb.innerHTML = TX.bien + solHTML(q.r, q.v) + ". " + (q.explica || "") + " <em>" + elige(est.intentos === 1 ? ELOGIO : ELOGIO2) + "</em>";
    } else {
      if (okV && r === REL_INV[q.r]) msg = q.invierte ? T("The number is right, but you multiplied or divided by a negative number: the sign has to flip.", "El número está bien, pero se dividió o multiplicó por un negativo: el signo tiene que invertirse.") : T("The number is right, but here the sign does not flip: you did not multiply or divide by a negative number.", "El número está bien, pero aquí el signo no se invierte: no se multiplicó ni se dividió por un negativo.");
      else if (okV) msg = T("The number is right; check whether the boundary is included (≤, ≥) or not (<, >).", "El número está bien; revise si el límite se incluye (≤, ≥) o no (<, >).");
      else if (okR) msg = T("The sign is right; check the boundary number.", "El signo está bien; revise el número límite.");
      else msg = T("Solve it like an equation and watch the sign at the end.", "Resuélvala como una ecuación y fíjese en el signo al final.");
      if (est.intentos >= 2){ est.resuelta = true; est.total++; fb.className = "fb mal"; fb.innerHTML = TX.asi + T("The answer is ", "La respuesta es ") + solHTML(q.r, q.v) + ". " + (q.explica || "") + TX.nuevo; }
      else { fb.className = "fb pista"; fb.innerHTML = TX.todavia + msg + TX.unoMas; }
    }
    if (est.resuelta) [pre + "-s", pre + "-v", pre + "-comprobar"].forEach(function(id){ $(id).disabled = true; });
    marcador();
  }
  $(pre + "-comprobar").addEventListener("click", comprueba);
  $(pre + "-v").addEventListener("keydown", function(ev){ if (ev.key === "Enter") comprueba(); });
  $(pre + "-nuevo").addEventListener("click", pinta);
  pinta();
  var obj = {pinta: pinta, estado: est};
  (window.__desig = window.__desig || {})[pre] = obj;
  return obj;
}
function P(){ return polVis(Array.prototype.slice.call(arguments)); }

/* Steps to solve izq r der, with the sign rule */
function pasosIneq(izq, r, der){
  var pasos = [], li = izq, ld = der, rel = r;
  if (!fcero(ld.x)){
    var nx = fres(li.x, ld.x);
    pasos.push(T("Subtract ", "Se resta ") + ladoHTML(L(ld.x, 0)) + T(" from both sides to gather the x terms: ", " en ambos lados para reunir las x: ") + ineqHTML(L(nx, li.k), rel, L(0, ld.k)) + ".");
    li = L(nx, li.k); ld = L(0, ld.k);
  }
  if (!fcero(li.k)){
    var nk = fres(ld.k, li.k);
    pasos.push((li.k.n > 0 ? T("Subtract " + fTxt(li.k) + " from both sides", "Se resta " + fTxt(li.k) + " en ambos lados") : T("Add " + fTxt(fneg(li.k)) + " to both sides", "Se suma " + fTxt(fneg(li.k)) + " en ambos lados")) + T(" (adding or subtracting never flips the sign): ", " (sumar o restar nunca invierte el signo): ") + ineqHTML(L(li.x, 0), rel, L(0, nk)) + ".");
    li = L(li.x, 0); ld = L(0, nk);
  }
  var v = fdiv(ld.k, li.x);
  if (!figual(li.x, fr(1))){
    if (li.x.n < 0){ rel = REL_INV[rel]; pasos.push(T("Divide by " + fTxt(li.x) + ". <strong>It is a negative number, so the sign flips</strong>: ", "Se divide entre " + fTxt(li.x) + ". <strong>Es un número negativo, así que el signo se invierte</strong>: ") + solHTML(rel, v) + "."); }
    else pasos.push(T("Divide by " + fTxt(li.x) + " (positive: the sign does not change): ", "Se divide entre " + fTxt(li.x) + " (positivo: el signo no cambia): ") + solHTML(rel, v) + ".");
  }
  return {pasos: pasos, r: rel, v: v, invierte: li.x.n < 0};
}

