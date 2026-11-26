/* LearnGED · helpers for signed numbers (Math Level 2). Load after practice.js.
   The texts follow the language of the page, like practice.js.
   José M. Fernández · CC BY-NC-SA 4.0 */
var TXE = ES ? {
  entSigno: "Escriba un número entero, con el signo menos si es negativo (por ejemplo, −7 o -7).",
  signoValor: "Elija el signo del resultado (paso 1) y escriba su valor sin signo (paso 2).",
  soloSigno: "El valor está bien, pero el signo no.",
  soloValor: "El signo está bien; revise el valor.",
  ambos: "Revise el signo y el valor.",
  laRespuesta: "La respuesta es ",
  primerPaso: "Mostrar el primer paso", sigPaso: "Mostrar el paso siguiente", yaTodos: "Ya se ven todos los pasos",
  signoRes: "Revise el signo: ¿el resultado queda por encima o por debajo del cero?"
} : {
  entSigno: "Type an integer, with a minus sign if it is negative (for example, −7 or -7).",
  signoValor: "Choose the sign of the answer (step 1) and type its value without a sign (step 2).",
  soloSigno: "The value is right, but the sign is not.",
  soloValor: "The sign is right; check the value.",
  ambos: "Check the sign and the value.",
  laRespuesta: "The answer is ",
  primerPaso: "Show the first step", sigPaso: "Show the next step", yaTodos: "All the steps are showing",
  signoRes: "Check the sign: is the answer above or below zero?"
};

/* Numbers with a true minus sign (−) and commas for thousands */
function menos(t){ return String(t).replace(/-/g, "−"); }
function ent(n){ return (n < 0 ? "−" : "") + com(Math.abs(n)); }
function par(n){ return n < 0 ? "(" + ent(n) + ")" : ent(n); }
function azarEnt(a, b, sinCero){ var n; do { n = aleatorio(a, b); } while (sinCero && n === 0); return n; }
/* Reads "-7", "−7", "+7", "7", "1,250" → integer, or null */
function leeEnt(t){
  var s = String(t).trim().replace(/[−–—]/g, "-").replace(/\s+/g, "").replace(/^\+/, "");
  if (/^-?\d{1,3}(,\d{3})+$/.test(s)) s = s.replace(/,/g, "");
  return /^-?\d+$/.test(s) ? parseInt(s, 10) : null;
}
/* Evaluator for creaPracticaLibre: res = right answer; pistas = [{v, msg}] for common mistakes */
function numE(res, pistas, general){
  return function(t){
    var v = leeEnt(t);
    if (v === null) return { estado: "invalido", msg: TXE.entSigno };
    if (v === res) return { estado: "bien" };
    for (var i = 0; i < (pistas || []).length; i++) if (pistas[i].v === v) return { estado: "mal", msg: pistas[i].msg };
    if (v === -res) return { estado: "mal", msg: TXE.signoRes };
    return { estado: "mal", msg: general || TX.revise };
  };
}

/* Number line from lo to hi. marcas = [{ v, txt, color, abajo }], saltos = [{ de, a, txt, color }], tramo = { de, a, color } */
function rectaEnt(lo, hi, marcas, saltos, voz, tramo){
  var W = 660, H = 170, x0 = 26, x1 = W - 26, y = 112;
  function X(v){ return x0 + (v - lo) * (x1 - x0) / (hi - lo); }
  var s = '<svg class="figura" viewBox="0 0 ' + W + ' ' + H + '" role="img" aria-label="' + voz + '">';
  s += linea([x0 - 12, y], [x1 + 12, y], "#424242", 2) + '<path d="M' + (x0 - 18) + ' ' + y + ' l10 -6 v12 z" fill="#424242"/><path d="M' + (x1 + 18) + ' ' + y + ' l-10 -6 v12 z" fill="#424242"/>';
  if (tramo) s += linea([X(tramo.de), y], [X(tramo.a), y], tramo.color || "#b71c1c", 7);
  var paso = (hi - lo) > 24 ? 5 : ((hi - lo) > 14 ? 2 : 1);
  for (var v = lo; v <= hi; v++){
    s += linea([X(v), y - (v === 0 ? 11 : 7)], [X(v), y + (v === 0 ? 11 : 7)], "#424242", v === 0 ? 3 : 1.5);
    if (v % paso === 0 || v === 0) s += texto([X(v), y + 28], ent(v), v === 0 ? 17 : 15, "#222", v === 0 ? 700 : 400);
  }
  (saltos || []).forEach(function(sl, i){
    var xa = X(sl.de), xb = X(sl.a), alto = 34 + 10 * (i % 2), col = sl.color || "#b71c1c", mx = (xa + xb) / 2;
    s += '<path d="M' + f1(xa) + ' ' + (y - 6) + ' Q' + f1(mx) + ' ' + (y - 6 - 2 * alto) + ' ' + f1(xb) + ' ' + (y - 6) + '" fill="none" stroke="' + col + '" stroke-width="3"/>';
    var dir = xb > xa ? -1 : 1;
    s += '<path d="M' + f1(xb) + ' ' + (y - 6) + ' l' + (dir * 9) + ' -12 l' + (-dir * 3) + ' 0 z" fill="' + col + '" stroke="' + col + '" stroke-width="2"/>';
    if (sl.txt) s += texto([mx, y - 10 - alto], sl.txt, 17, col);
  });
  (marcas || []).forEach(function(m){
    s += '<circle cx="' + f1(X(m.v)) + '" cy="' + y + '" r="8" fill="' + (m.color || "#b71c1c") + '"/>';
    if (m.txt) s += texto([X(m.v), m.abajo ? y + 50 : y - 22], m.txt, 16, m.color || "#b71c1c");
  });
  return s + '</svg>';
}

/* Two-color counters: a row for a and a row for b. Yellow (+) is +1, red (−) is −1.
   empareja = true crosses out the zero pairs. */
function fichasSVG(a, b, empareja, voz){
  var W = 660, r = 15, dx = 36, H = 150, s = "";
  var pos = Math.max(a, 0) + Math.max(b, 0), neg = Math.max(-a, 0) + Math.max(-b, 0), pares = Math.min(pos, neg);
  s += '<svg class="figura" viewBox="0 0 ' + W + ' ' + H + '" role="img" aria-label="' + voz + '">';
  var usadosP = 0, usadosN = 0;
  [a, b].forEach(function(v, fi){
    var y = 40 + fi * 64, n = Math.abs(v);
    s += texto([30, y], ent(v), 18, "#222", 700);
    for (var i = 0; i < n; i++){
      var x = 80 + i * dx, posit = v > 0, cero = false;
      if (empareja){ if (posit && usadosP < pares){ cero = true; usadosP++; } else if (!posit && usadosN < pares){ cero = true; usadosN++; } }
      var fill = posit ? "#fbc02d" : "#c62828", col = posit ? "#3e2723" : "#fff";
      s += '<circle cx="' + x + '" cy="' + y + '" r="' + r + '" fill="' + (cero ? "#eeeeee" : fill) + '" stroke="' + (cero ? "#9e9e9e" : "#424242") + '" stroke-width="2"/>';
      s += texto([x, y + 1], posit ? "+" : "−", 20, cero ? "#9e9e9e" : col);
      if (cero) s += linea([x - 12, y + 12], [x + 12, y - 12], "#757575", 2);
    }
  });
  return s + '</svg>';
}

/* Two-step practice: first the sign, then the value. gen() → { enun, res, explica }.
   Same feedback as the other practices: a hint and another try, then the solution. */
function creaSignoValor(pre, gen){
  var est = { primero: 0, pista: 0, total: 0, actual: null, resuelta: false, intentos: 0, signo: null };
  function marcador(){ $(pre + "-marcador").textContent = est.total ? TX.resueltos(est.primero + est.pista, est.primero, est.total) : ""; }
  function marca(sg){ est.signo = sg; $(pre + "-mas").setAttribute("aria-pressed", sg === "+" ? "true" : "false"); $(pre + "-menos").setAttribute("aria-pressed", sg === "−" ? "true" : "false"); }
  function pinta(){
    est.actual = gen(); est.resuelta = false; est.intentos = 0; marca(null);
    $(pre + "-enun").innerHTML = est.actual.enun;
    $(pre + "-v").value = ""; $(pre + "-v").disabled = false; $(pre + "-comprobar").disabled = false;
    $(pre + "-mas").disabled = false; $(pre + "-menos").disabled = false;
    $(pre + "-fb").className = "fb"; $(pre + "-fb").innerHTML = "";
  }
  function bloquea(){ $(pre + "-v").disabled = true; $(pre + "-comprobar").disabled = true; $(pre + "-mas").disabled = true; $(pre + "-menos").disabled = true; }
  function comprueba(){
    if (est.resuelta) return;
    var q = est.actual, fb = $(pre + "-fb"), v = leeEnt($(pre + "-v").value);
    if (v !== null) v = Math.abs(v);
    if (v === null || (!est.signo && q.res !== 0)){ fb.className = "fb pista"; fb.innerHTML = TXE.signoValor; return; }
    est.intentos++;
    var okS = q.res === 0 || est.signo === (q.res > 0 ? "+" : "−"), okV = v === Math.abs(q.res);
    if (okS && okV){
      est.resuelta = true; est.total++; if (est.intentos === 1) est.primero++; else est.pista++;
      fb.className = "fb bien"; fb.innerHTML = TX.bien + "<strong>" + ent(q.res) + "</strong>. " + (q.explica || "") + " <em>" + (est.intentos === 1 ? elige(ELOGIO) : elige(ELOGIO2)) + "</em>";
      bloquea();
    } else {
      var msg = !okS && okV ? TXE.soloSigno : (okS && !okV ? TXE.soloValor : TXE.ambos);
      if (est.intentos >= 2){
        est.resuelta = true; est.total++;
        fb.className = "fb mal"; fb.innerHTML = TX.asi + TXE.laRespuesta + "<strong>" + ent(q.res) + "</strong>. " + (q.explica || "") + TX.nuevo;
        bloquea();
      } else {
        fb.className = "fb pista"; fb.innerHTML = TX.todavia + msg + (q.pista && !okS ? " " + q.pista : "") + TX.unoMas;
      }
    }
    marcador();
  }
  $(pre + "-mas").addEventListener("click", function(){ if (!est.resuelta) marca("+"); });
  $(pre + "-menos").addEventListener("click", function(){ if (!est.resuelta) marca("−"); });
  $(pre + "-comprobar").addEventListener("click", comprueba);
  $(pre + "-v").addEventListener("keydown", function(ev){ if (ev.key === "Enter") comprueba(); });
  $(pre + "-nuevo").addEventListener("click", pinta);
  pinta(); marcador();
}

/* Step-by-step viewer: buttons pre-sig and pre-todo, steps in pre-pasos */
function pasoAPaso(pre, pasos){
  var S = { pasos: pasos, visto: 0 };
  function pinta(){
    var h = "";
    for (var i = 0; i < S.visto; i++) h += '<div class="paso"><span class="n" aria-hidden="true">' + (i === S.pasos.length - 1 ? "✓" : i + 1) + '</span>' + S.pasos[i] + '</div>';
    $(pre + "-pasos").innerHTML = h;
    var b = $(pre + "-sig"); b.disabled = S.visto >= S.pasos.length; $(pre + "-todo").disabled = b.disabled;
    b.textContent = S.visto === 0 ? TXE.primerPaso : (b.disabled ? TXE.yaTodos : TXE.sigPaso);
  }
  S.pinta = pinta;
  S.carga = function(p){ S.pasos = p; S.visto = 0; pinta(); };
  $(pre + "-sig").addEventListener("click", function(){ if (S.visto < S.pasos.length){ S.visto++; pinta(); } });
  $(pre + "-todo").addEventListener("click", function(){ S.visto = S.pasos.length; pinta(); });
  pinta();
  return S;
}

/* ---------- Signed fractions ---------- */
var TXF = ES ? {
  escriba: "Escriba una fracción con la barra, como −3/4 (con el signo menos delante si es negativa), un entero o un número mixto como −2 3/4.",
  simplifique: "El valor está bien, pero todavía se puede simplificar.",
  cero: "Una fracción nunca tiene 0 en el denominador.",
  signo: "El valor está bien, pero revise el signo con la regla de los signos.",
  mixtoMal: "En un número mixto, la parte de fracción tiene que ser menor que 1."
} : {
  escriba: "Type a fraction with a slash, like −3/4 (with the minus sign in front if it is negative), an integer, or a mixed number like −2 3/4.",
  simplifique: "The value is right, but you can still simplify it.",
  cero: "A fraction never has 0 in the denominator.",
  signo: "The value is right, but check the sign with the sign rule.",
  mixtoMal: "In a mixed number, the fraction part must be less than 1."
};
function mcdE(a, b){ a = Math.abs(a); b = Math.abs(b); while (b){ var x = a % b; a = b; b = x; } return a; }
function mcmE(a, b){ return a / mcdE(a, b) * b; }
/* fraction in simplest form, sign in the numerator */
function q(n, d){ if (d === undefined) d = 1; if (d < 0){ n = -n; d = -d; } var g = mcdE(n, d) || 1; return { n: n / g, d: d / g }; }
function qsum(a, b){ return q(a.n * b.d + b.n * a.d, a.d * b.d); }
function qres(a, b){ return q(a.n * b.d - b.n * a.d, a.d * b.d); }
function qmul(a, b){ return q(a.n * b.n, a.d * b.d); }
function qdiv(a, b){ return q(a.n * b.d, a.d * b.n); }
function qneg(a){ return q(-a.n, a.d); }
function qigual(a, b){ return a && b && a.n === b.n && a.d === b.d; }
/* HTML: stacked fraction, read correctly by screen readers. numerador and denominador may be negative (written as typed). */
function frH(n, d){ return '<span aria-hidden="true"><span class="fracc"><span class="fa">' + ent(n) + '</span><span class="fb2">' + ent(d) + '</span></span></span><span class="sr-only">' + ent(n) + '/' + ent(d) + '</span>'; }
/* a value {n, d}: integer, or fraction with the sign in front */
function qH(v){
  if (v.d === 1) return ent(v.n);
  return '<span aria-hidden="true">' + (v.n < 0 ? "−" : "") + '<span class="fracc"><span class="fa">' + Math.abs(v.n) + '</span><span class="fb2">' + v.d + '</span></span></span><span class="sr-only">' + (v.n < 0 ? "−" : "") + Math.abs(v.n) + '/' + v.d + '</span>';
}
function qP(v){ return v.n < 0 ? "(" + qH(v) + ")" : qH(v); }
function qTxt(v){ return v.d === 1 ? ent(v.n) : ent(v.n) + "/" + v.d; }
function qMixto(v){ if (v.d === 1 || Math.abs(v.n) < v.d) return ""; var e = Math.floor(Math.abs(v.n) / v.d), r = Math.abs(v.n) % v.d;
  return '<span aria-hidden="true">' + (v.n < 0 ? "−" : "") + e + '&nbsp;<span class="fracc"><span class="fa">' + r + '</span><span class="fb2">' + v.d + '</span></span></span><span class="sr-only">' + (v.n < 0 ? "−" : "") + e + ' ' + r + '/' + v.d + '</span>'; }
/* Reads "−3/4", "-3/4", "3/-4", "-2 3/4", "5" → { v: value, simple: written in simplest form } or { cero } or null */
function leeQ(t){
  var s = String(t).trim().replace(/[−–—]/g, "-").replace(/\s*\/\s*/g, "/").replace(/\s+/g, " "), x;
  if ((x = s.match(/^(-?\d+)$/))) return { v: q(+x[1]), simple: true };
  if ((x = s.match(/^(-?\d+)\/(-?\d+)$/))){ if (+x[2] === 0) return { cero: true }; return { v: q(+x[1], +x[2]), simple: mcdE(+x[1], +x[2]) === 1 }; }
  if ((x = s.match(/^(-?)(\d+) (\d+)\/(\d+)$/))){ if (+x[4] === 0) return { cero: true }; var nn = +x[2] * +x[4] + +x[3]; return { v: q(x[1] ? -nn : nn, +x[4]), simple: mcdE(+x[3], +x[4]) === 1, mixtoMal: +x[3] >= +x[4] }; }
  return null;
}
/* Evaluator: obj = right value; pistas = [{ v, msg }] */
function evQ(obj, pistas){
  return function(t){
    var r = leeQ(t);
    if (r && r.cero) return { estado: "invalido", msg: TXF.cero };
    if (!r) return { estado: "invalido", msg: TXF.escriba };
    if (qigual(r.v, obj)){
      if (r.mixtoMal) return { estado: "mal", msg: TXF.mixtoMal };
      if (!r.simple) return { estado: "mal", msg: TXF.simplifique };
      return { estado: "bien" };
    }
    for (var i = 0; i < (pistas || []).length; i++) if (qigual(r.v, pistas[i].v)) return { estado: "mal", msg: pistas[i].msg };
    if (qigual(r.v, qneg(obj))) return { estado: "mal", msg: TXF.signo };
    return { estado: "mal", msg: TX.revise };
  };
}
/* Powers */
function potH(b, e, parentesis){ return (parentesis && b < 0 ? "(" + ent(b) + ")" : ent(b)) + "<sup>" + e + "</sup>"; }
function pw(b, e){ var r = 1; for (var i = 0; i < e; i++) r *= b; return r; }
/* Square root sign with the radicand under the bar */
function rz(n){ return '<span class="rad" aria-hidden="true">√<span class="rc">' + n + '</span></span><span class="sr-only">' + (ES ? "raíz cuadrada de " : "square root of ") + n + '</span>'; }
