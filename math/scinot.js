/* LearnGED · math/scinot.js — shared engine for Level 3 · Topic 2 (scientific notation).
   Numbers are kept as m × 10^e with m a whole number (BigInt), so every calculation is exact:
   no rounding errors like 0.1 + 0.2 = 0.30000000000000004.
   Works in English and Spanish (practice.js sets ES from <html lang>). Load after practice.js.
   Ported from GEDparaHispanos (algebra/n3-l2-*.html). José M. Fernández · CC BY-NC-SA 4.0 */

function T(en, es){ return ES ? es : en; }
var DIEZ = BigInt(10), CERO = BigInt(0), UNO = BigInt(1);
function pot10(k){ var r = UNO; for (var i = 0; i < k; i++) r *= DIEZ; return r; }
function N(m, e){ return normaliza({m: BigInt(m), e: e || 0}); }
function normaliza(n){
  var m = n.m, e = n.e;
  if (m === CERO) return {m: CERO, e: 0};
  while (m % DIEZ === CERO){ m /= DIEZ; e++; }
  return {m: m, e: e};
}
/* "4.5" → 45 × 10^-1. Accepts a sign; a comma is a decimal point only if there is no point and it is not a thousands comma */
function leeNumero(txt){
  if (txt === null || txt === undefined) return null;
  var s = String(txt).trim().replace(/\s+/g, "").replace(/[−–]/g, "-");
  if (s.indexOf(".") < 0 && /^-?\d+,\d+$/.test(s) && !/^-?\d{1,3}(,\d{3})+$/.test(s)) s = s.replace(",", ".");
  s = s.replace(/,/g, "");
  if (!/^-?(\d+\.?\d*|\.\d+)$/.test(s)) return null;
  var neg = s.charAt(0) === "-"; if (neg) s = s.slice(1);
  var p = s.indexOf("."), dec = 0;
  if (p >= 0){ dec = s.length - p - 1; s = s.slice(0, p) + s.slice(p + 1); }
  if (s === "") return null;
  var m = BigInt(s); if (neg) m = -m;
  return normaliza({m: m, e: -dec});
}
function sci(c, k){ var n = leeNumero(String(c)); return normaliza({m: n.m, e: n.e + k}); }
function mul(a, b){ return normaliza({m: a.m * b.m, e: a.e + b.e}); }
function alinea(a, b){ var e = Math.min(a.e, b.e); return [a.m * pot10(a.e - e), b.m * pot10(b.e - e), e]; }
function suma(a, b){ var t = alinea(a, b); return normaliza({m: t[0] + t[1], e: t[2]}); }
function resta(a, b){ var t = alinea(a, b); return normaliza({m: t[0] - t[1], e: t[2]}); }
function compara(a, b){ var t = alinea(a, b); return t[0] < t[1] ? -1 : (t[0] > t[1] ? 1 : 0); }
function igual(a, b){ return compara(a, b) === 0; }
function porPot(n, k){ return normaliza({m: n.m, e: n.e + k}); }
function abs(m){ return m < 0 ? -m : m; }
/* Exact division when it has few digits; otherwise rounded to 4 significant digits */
function divide(a, b){
  for (var k = 0; k <= 12; k++){ var num = a.m * pot10(k); if (num % b.m === CERO) return {n: normaliza({m: num / b.m, e: a.e - b.e - k}), exacta: true}; }
  var esc = 30, n = normaliza({m: (a.m * pot10(esc)) / b.m, e: a.e - b.e - esc}), s = abs(n.m).toString();
  if (s.length > 4){ var corte = s.length - 4, base = pot10(corte), m = abs(n.m), r = m / base; if ((m % base) * BigInt(2) >= base) r += UNO; n = normaliza({m: n.m < 0 ? -r : r, e: n.e + corte}); }
  return {n: n, exacta: false};
}
function esCero(n){ return n.m === CERO; }
function exponenteSci(n){ return n.e + abs(n.m).toString().length - 1; }
function coefCon(n, k){ return plano(porPot(n, -k)); }
function aSci(n){ if (esCero(n)) return {c: "0", e: 0}; var k = exponenteSci(n); return {c: coefCon(n, k), e: k}; }
function plano(n){
  var neg = n.m < 0, s = abs(n.m).toString(), r;
  if (n.e >= 0) r = s + "0".repeat(n.e);
  else { var d = -n.e; if (s.length <= d) s = "0".repeat(d - s.length + 1) + s; r = s.slice(0, s.length - d) + "." + s.slice(s.length - d); }
  return (neg ? "-" : "") + r;
}
/* Decimal with thousands commas, as on the GED test */
function conComas(n){
  var s = plano(n), neg = s.charAt(0) === "-"; if (neg) s = s.slice(1);
  var p = s.indexOf("."), ent = p < 0 ? s : s.slice(0, p), dec = p < 0 ? "" : s.slice(p);
  return (neg ? "−" : "") + ent.replace(/\B(?=(\d{3})+(?!\d))/g, ",") + dec;
}
function signo(txt){ return String(txt).replace(/^-/, "−"); }
function expTexto(k){ return k < 0 ? "−" + (-k) : String(k); }
function par(k){ return k < 0 ? "(" + expTexto(k) + ")" : expTexto(k); }
function expVoz(k){ return k < 0 ? T("negative ", "menos ") + (-k) : String(k); }
var SUP = {"0": "⁰", "1": "¹", "2": "²", "3": "³", "4": "⁴", "5": "⁵", "6": "⁶", "7": "⁷", "8": "⁸", "9": "⁹", "-": "⁻", "−": "⁻"};
function supTexto(k){ return String(k).split("").map(function(ch){ return SUP[ch] || ch; }).join(""); }
function sciTexto(c, k){ return signo(c) + " × 10" + supTexto(k); }
function sciHTML(c, k){
  return '<span class="ex" aria-hidden="true">' + signo(c) + " × 10<sup>" + expTexto(k) + "</sup></span>" +
         '<span class="sr-only">' + signo(c).replace("−", T("negative ", "menos ")) + T(" times 10 to the power of ", " por 10 elevado a ") + expVoz(k) + "</span>";
}
function potHTML(k){ return '<span class="ex" aria-hidden="true">10<sup>' + expTexto(k) + '</sup></span><span class="sr-only">' + T("10 to the power of ", "10 elevado a ") + expVoz(k) + "</span>"; }
function numSciHTML(n){ var s = aSci(n); return sciHTML(s.c, s.e); }
function esValida(c){ var n = leeNumero(c); if (!n || n.m === CERO) return false; var x = normaliza({m: abs(n.m), e: n.e}); return compara(x, N(1)) >= 0 && compara(x, N(10)) < 0; }
/* A random coefficient with 1 to 3 significant digits, from 1 to 9.99 */
function coefAzar(cifras){
  cifras = cifras || aleatorio(1, 3);
  var d = String(aleatorio(1, 9));
  for (var i = 1; i < cifras; i++) d += String(i === cifras - 1 ? aleatorio(1, 9) : aleatorio(0, 9));
  return plano(normaliza({m: BigInt(d), e: -(cifras - 1)}));
}
function lugares(k){ return k === 1 ? T(" place", " lugar") : T(" places", " lugares"); }

/* ---------- Answer choices ---------- */
function op(c, k){ return {html: sciHTML(c, k), clave: signo(c) + "e" + k}; }
function opNum(n){ var s = aSci(n); return op(s.c, s.e); }

/* Multiple choice with two tries (practice.js). gen() returns {enun, opciones: [{html, clave}], correcta, porClave, bien, mal} */
function OMS(pre, gen){
  creaPracticaOM(pre, function(){
    var q = gen();
    q.pistas = q.porClave || {};
    q.pista = q.pista || T("Check the coefficient and the exponent, and try again.", "Revise el coeficiente y el exponente, y vuelva a intentarlo.");
    return q;
  });
}

/* Typed answer in scientific notation, with two tries.
   gen() returns {enun, resp (number), explica, diagnostico(value, coef, exp)?, operacion?, porQueOp?, previo()?, alPintar()?} */
function creaPracticaSci(pre, gen){
  var est = {primero: 0, pista: 0, total: 0, actual: null, resuelta: false, intentos: 0};
  function marcador(){ $(pre + "-marcador").textContent = est.total ? TX.resueltos(est.primero + est.pista, est.primero, est.total) : ""; }
  function pinta(){
    est.actual = gen(); est.resuelta = false; est.intentos = 0;
    $(pre + "-enun").innerHTML = est.actual.enun;
    $(pre + "-c").value = ""; $(pre + "-e").value = "";
    $(pre + "-c").disabled = false; $(pre + "-e").disabled = false; $(pre + "-comprobar").disabled = false;
    $(pre + "-c").classList.remove("error"); $(pre + "-e").classList.remove("error");
    if ($(pre + "-op")){ $(pre + "-op").value = ""; $(pre + "-op").disabled = false; }
    if ($(pre + "-r")){ $(pre + "-r").value = ""; $(pre + "-r").disabled = false; $(pre + "-r").classList.remove("error"); }
    if (est.actual.alPintar) est.actual.alPintar();
    $(pre + "-fb").className = "fb"; $(pre + "-fb").innerHTML = "";
  }
  function bloquea(){
    $(pre + "-c").disabled = true; $(pre + "-e").disabled = true; $(pre + "-comprobar").disabled = true;
    if ($(pre + "-op")) $(pre + "-op").disabled = true;
    if ($(pre + "-r")) $(pre + "-r").disabled = true;
  }
  function comprueba(){
    if (est.resuelta) return;
    var q = est.actual, fb = $(pre + "-fb"), ctxt = $(pre + "-c").value, etxt = $(pre + "-e").value.trim().replace(/[−–]/g, "-");
    var c = leeNumero(ctxt), okE = /^-?\d+$/.test(etxt);
    $(pre + "-c").classList.toggle("error", !c); $(pre + "-e").classList.toggle("error", !okE);
    if ($(pre + "-op") && q.operacion && !$(pre + "-op").value){ fb.className = "fb pista"; fb.innerHTML = T("First choose the operation that solves the problem.", "Elija primero la operación que resuelve el problema."); return; }
    if (!c || !okE){ fb.className = "fb pista"; fb.innerHTML = T("Type the coefficient with a decimal point (for example, 4.5) and the exponent as a whole number (for example, 6 or −3).", "Escriba el coeficiente con punto decimal (por ejemplo, 4.5) y el exponente como un número entero (por ejemplo, 6 o −3)."); return; }
    var k = parseInt(etxt, 10), valor = porPot(c, k), bien = igual(valor, q.resp), valido = esValida(ctxt);
    var fallaPrevio = q.previo ? q.previo() : null, opOk = !($(pre + "-op") && q.operacion) || $(pre + "-op").value === q.operacion;
    est.intentos++;
    if (bien && valido && opOk && !fallaPrevio){
      est.resuelta = true; est.total++; if (est.intentos === 1) est.primero++; else est.pista++;
      fb.className = "fb bien"; fb.innerHTML = TX.bien + numSciHTML(q.resp) + ". " + (q.explica || "") + " <em>" + (est.intentos === 1 ? elige(ELOGIO) : elige(ELOGIO2)) + "</em>";
      bloquea();
    } else {
      var msg;
      if (fallaPrevio) msg = fallaPrevio;
      else if (!opOk) msg = T("Check the operation: ", "Revise la operación: ") + (q.porQueOp || T("read again what the question asks.", "vuelva a leer qué pide la pregunta."));
      else if (bien && !valido) msg = T("The value is right, but it is not yet valid scientific notation: the coefficient must be from 1 up to, but not including, 10 (1 ≤ a < 10).", "El valor es correcto, pero todavía no está en notación científica válida: el coeficiente tiene que quedar entre 1 y 10 (1 ≤ a < 10).");
      else if (q.diagnostico && q.diagnostico(valor, c, k)) msg = q.diagnostico(valor, c, k);
      else if (igual(valor, porPot(q.resp, 1)) || igual(valor, porPot(q.resp, -1))) msg = T("Almost: the value is 10 times too big or too small. Check the exponent.", "Casi: el valor queda 10 veces más grande o más pequeño. Revise el exponente.");
      else if (valido && k === aSci(q.resp).e) msg = T("The exponent is right; check the coefficient.", "El exponente está bien; revise el coeficiente.");
      else if (valido && igual(c, leeNumero(aSci(q.resp).c))) msg = T("The coefficient is right; check the exponent.", "El coeficiente está bien; revise el exponente.");
      else msg = T("Check the coefficient and the exponent.", "Revise el coeficiente y el exponente.");
      if (est.intentos >= 2){
        est.resuelta = true; est.total++;
        fb.className = "fb mal"; fb.innerHTML = TX.asi + msg + " " + T("The answer is ", "La respuesta es ") + numSciHTML(q.resp) + ". " + (q.explica || "") + TX.nuevo;
        bloquea();
      } else { fb.className = "fb pista"; fb.innerHTML = TX.todavia + msg + TX.unoMas; }
    }
    marcador();
  }
  $(pre + "-comprobar").addEventListener("click", comprueba);
  [pre + "-c", pre + "-e"].forEach(function(id){ $(id).addEventListener("keydown", function(ev){ if (ev.key === "Enter") comprueba(); }); });
  $(pre + "-nuevo").addEventListener("click", pinta);
  pinta(); marcador();
}

/* ---------- Typed decimal answer with two tries: gen() returns {enun, resp, explica, pista(v)?} ---------- */
function creaPracticaDec(pre, gen){
  creaPracticaLibre(pre, function(){
    var q = gen();
    return {enun: q.enun, solucion: q.explica,
      evalua: function(t){
        var v = leeNumero(t);
        if (!v) return {estado: "invalido", msg: T("Type a number with digits, for example 370000 or 0.0056.", "Escriba un número con cifras, por ejemplo 370000 o 0.0056.")};
        if (igual(v, q.resp)) return {estado: "bien"};
        return {estado: "mal", msg: (q.pista && q.pista(v)) || T("Check how many places and in which direction the point moves.", "Revise cuántos lugares y hacia dónde se mueve el punto.")};
      }};
  });
}
