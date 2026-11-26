/* LearnGED · order-of-operations engine (Math Level 2, Topic 3). Load after practice.js and integers.js.
   An expression is a list [term, op, term, …]. Terms: number, grouping symbol, power, square root,
   fraction bar, opposite (−x with no parentheses), and a highlight mark (only for display).
   Ported from algebra/n2-l3-2.html (GEDparaHispanos), now in English and Spanish.
   José M. Fernández · CC BY-NC-SA 4.0 */
var TXP = ES ? {
  etapa: { P: "Agrupadores", E: "Exponentes y raíces", MD: "Multiplicación y división", AS: "Suma y resta" },
  op: { "×": "la multiplicación", "÷": "la división", "+": "la suma", "−": "la resta" },
  agr: { "(": "los paréntesis", "[": "los corchetes", "{": "las llaves" },
  dentro: function(a, lab){ return "Dentro de " + a + ", " + lab.toLowerCase(); }, bajoRaiz: "Bajo la raíz (agrupa como un paréntesis)", enNum: "En el numerador", enDen: "En el denominador",
  exponentes: "Exponentes", raices: "Raíces", barra: "La barra de fracción", seQueda: ", y el signo de afuera se queda: ",
  resultado: "Resultado: ", voz: { mas: " más ", menos: " menos ", por: " por ", entre: " entre ", neg: "menos ", par: "paréntesis ", cierra: " cierra paréntesis", elev: " elevado a ", raiz: "raíz cuadrada de ", finRaiz: " fin de la raíz", frac: "fracción: arriba ", abajo: ", abajo ", opuesto: "el opuesto de " },
  izqder: "Parece que se resolvió de izquierda a derecha sin respetar la prioridad: la multiplicación y la división van antes que la suma y la resta.",
  potmul: "Parece que una potencia se calculó multiplicando la base por el exponente.",
  negcuad: "Cuidado con −a²: sin paréntesis, el exponente no afecta al signo.",
  resuelva: "Resuelva "
} : {
  etapa: { P: "Grouping symbols", E: "Exponents and roots", MD: "Multiplication and division", AS: "Addition and subtraction" },
  op: { "×": "the multiplication", "÷": "the division", "+": "the addition", "−": "the subtraction" },
  agr: { "(": "the parentheses", "[": "the brackets", "{": "the braces" },
  dentro: function(a, lab){ return "Inside " + a + ", " + lab.toLowerCase(); }, bajoRaiz: "Under the radical sign (it groups like parentheses)", enNum: "In the numerator", enDen: "In the denominator",
  exponentes: "Exponents", raices: "Roots", barra: "The fraction bar", seQueda: ", and the sign outside stays: ",
  resultado: "Answer: ", voz: { mas: " plus ", menos: " minus ", por: " times ", entre: " divided by ", neg: "negative ", par: "parenthesis ", cierra: " close parenthesis", elev: " to the power ", raiz: "square root of ", finRaiz: " end of root", frac: "fraction: top ", abajo: ", bottom ", opuesto: "the opposite of " },
  izqder: "It looks like you worked from left to right without the order: multiplication and division come before addition and subtraction.",
  potmul: "It looks like a power was found by multiplying the base by the exponent.",
  negcuad: "Careful with −a²: with no parentheses, the exponent does not apply to the sign.",
  resuelva: "Solve "
};
function N(v){ return { t: "n", v: v }; }
function G(k, e){ return { t: "g", k: k, e: e }; }
function Pw(b, n){ return { t: "p", b: b, n: n }; }
function Rt(e){ return { t: "r", e: e }; }
function Fr(a, b){ return { t: "f", a: a, b: b }; }
function Mn(x){ return { t: "m", x: x }; }
function Hl(html){ return { t: "h", html: html }; }
function listo(e){ return e.length === 1 && e[0].t === "n"; }
var CIERRA = { "(": ")", "[": "]", "{": "}" }, NIVEL_AGR = { "(": "n1", "[": "n2", "{": "n3" };
function numTxt(v){ return Math.round(v) === v ? ent(v) : menos(String(Math.round(v * 1000) / 1000)); }
function envuelve(vis, voz){ return '<span class="ex" aria-hidden="true">' + vis + '</span><span class="sr-only">' + voz + '</span>'; }

/* ---------- Display ---------- */
function vN(v, conPar){ return v < 0 && conPar ? "(" + numTxt(v) + ")" : numTxt(v); }
function rTerm(t, conPar){
  if (t.t === "n") return vN(t.v, conPar);
  if (t.t === "h") return '<mark class="op-act">' + t.html + '</mark>';
  if (t.t === "g") return '<span class="' + NIVEL_AGR[t.k] + '">' + t.k + '</span>' + rLista(t.e) + '<span class="' + NIVEL_AGR[t.k] + '">' + CIERRA[t.k] + '</span>';
  if (t.t === "p") return rTerm(t.b, true) + "<sup>" + t.n + "</sup>";
  if (t.t === "r") return '<span class="rad">√<span class="rc">' + rLista(t.e) + '</span></span>';
  if (t.t === "f") return '<span class="fracc"><span class="fa">' + rLista(t.a) + '</span><span class="fb2">' + rLista(t.b) + '</span></span>';
  if (t.t === "m") return "−" + rTerm(t.x, true);
  return "?";
}
function rLista(e){ return e.map(function(x, i){ return i % 2 ? " " + x + " " : rTerm(x, i > 0); }).join(""); }
function vozTerm(t){
  var V = TXP.voz;
  if (t.t === "n") return numTxt(t.v).replace("−", V.neg);
  if (t.t === "g") return V.par + vozLista(t.e) + V.cierra;
  if (t.t === "p") return vozTerm(t.b) + V.elev + t.n;
  if (t.t === "r") return V.raiz + vozLista(t.e) + V.finRaiz;
  if (t.t === "f") return V.frac + vozLista(t.a) + V.abajo + vozLista(t.b);
  if (t.t === "m") return V.opuesto + vozTerm(t.x);
  return "";
}
function vozLista(e){ var V = TXP.voz; return e.map(function(x, i){ return i % 2 ? { "+": V.mas, "−": V.menos, "×": V.por, "÷": V.entre }[x] : vozTerm(x); }).join(""); }
function exprHTML(e){ return envuelve(rLista(e), vozLista(e)); }

/* ---------- Normalize: a grouping that is already one number becomes the number ---------- */
function norm(e){ return e.map(function(x, i){ return i % 2 ? x : normT(x, false); }); }
function normT(t, esBase){
  if (t.t === "g"){ var e = norm(t.e); if (listo(e) && !(esBase && e[0].v < 0)) return e[0]; return G(t.k, e); }
  if (t.t === "p") return Pw(normT(t.b, true), t.n);
  if (t.t === "r") return Rt(norm(t.e));
  if (t.t === "f") return Fr(norm(t.a), norm(t.b));
  if (t.t === "m"){ var x = normT(t.x, false); return x.t === "n" ? N(-x.v) : Mn(x); }
  return t;
}
function valorBase(b){ return b.t === "n" ? b.v : (b.t === "g" && listo(b.e) ? b.e[0].v : null); }

/* ---------- One step ----------
   Returns { e, hl, lab, cuerpo, etapa, exacto } or null. modo simulates a mistake:
   { tipo: "izqder" | "potmul" | "negcuad", usado, siempre }. */
function desc(r){ return r.lab + ": " + r.cuerpo; }
function paso(e, modo){
  var i, r;
  for (i = 0; i < e.length; i += 2){ r = pasoDentro(e[i], modo); if (r) return armar(e, i, r); }
  for (i = 0; i < e.length; i += 2){ r = pasoE(e[i], modo); if (r) return armar(e, i, r); }
  var ops = []; for (i = 1; i < e.length; i += 2) ops.push(i);
  if (!ops.length) return null;
  var j = null, md = ops.filter(function(k){ return e[k] === "×" || e[k] === "÷"; });
  if (modo && modo.tipo === "izqder" && (!modo.usado || modo.siempre) && md.length && (e[ops[0]] === "+" || e[ops[0]] === "−")){ j = ops[0]; modo.usado = true; modo.paso = modo.cuenta; }
  if (j === null) j = md.length ? md[0] : ops[0];
  var a = e[j - 1].v, b = e[j + 1].v, op = e[j], v = op === "×" ? a * b : (op === "÷" ? a / b : (op === "+" ? a + b : a - b));
  var trozo = vN(a, j - 1 > 0) + " " + op + " " + vN(b, true);
  var nuevo = e.slice(0, j - 1).concat([N(v)], e.slice(j + 2)), hl = e.slice(0, j - 1).concat([Hl(trozo)], e.slice(j + 2));
  var etapa = (op === "×" || op === "÷") ? "MD" : "AS";
  return { e: norm(nuevo), hl: hl, lab: TXP.etapa[etapa], cuerpo: TXP.op[op] + " " + numTxt(a) + " " + op + " " + vN(b, true) + " = " + numTxt(v) + ".", etapa: etapa, exacto: v === Math.round(v) };
}
function armar(e, i, r){ var nuevo = e.slice(), hl = e.slice(); nuevo[i] = r.t; hl[i] = r.hl; return { e: norm(nuevo), hl: hl, lab: r.lab, cuerpo: r.cuerpo, etapa: r.etapa, exacto: r.exacto !== false, dentro: r.dentro }; }
function envolverR(t, campo, r, lab){ var c = {}, h = {}, k; for (k in t){ c[k] = t[k]; h[k] = t[k]; } c[campo] = r.e; h[campo] = r.hl; return { t: c, hl: h, lab: r.dentro ? r.lab : lab, cuerpo: r.cuerpo, etapa: r.etapa, exacto: r.exacto, dentro: true }; }
function pasoDentro(t, modo){
  var r, x;
  if (t.t === "g" && !listo(t.e)){ r = paso(t.e, modo); if (r) return envolverR(t, "e", r, TXP.dentro(TXP.agr[t.k], r.lab)); }
  if (t.t === "p" && t.b.t === "g"){ r = pasoDentro(t.b, modo); if (r) return { t: Pw(r.t, t.n), hl: Pw(r.hl, t.n), lab: r.lab, cuerpo: r.cuerpo, etapa: r.etapa, exacto: r.exacto, dentro: true }; }
  if (t.t === "r" && !listo(t.e)){ r = paso(t.e, modo); if (r) return envolverR(t, "e", r, TXP.bajoRaiz); }
  if (t.t === "f"){
    if (!listo(t.a)){ r = paso(t.a, modo); if (r) return envolverR(t, "a", r, TXP.enNum); }
    if (!listo(t.b)){ r = paso(t.b, modo); if (r) return envolverR(t, "b", r, TXP.enDen); }
  }
  if (t.t === "m"){ r = pasoDentro(t.x, modo); if (r) return { t: Mn(r.t), hl: Mn(r.hl), lab: r.lab, cuerpo: r.cuerpo, etapa: r.etapa, exacto: r.exacto, dentro: true }; }
  return null;
}
function pasoE(t, modo){
  if (t.t === "p"){
    var b = valorBase(t.b); if (b === null) return null;
    var v = Math.pow(b, t.n);
    if (modo && modo.tipo === "potmul" && (!modo.usado || modo.siempre) && b * t.n !== v){ v = b * t.n; modo.usado = true; modo.paso = modo.cuenta; }
    return { t: N(v), hl: Hl(rTerm(t, false)), lab: TXP.exponentes, cuerpo: rTerm(t.b, true) + "<sup>" + t.n + "</sup> = " + numTxt(v) + ".", etapa: "E" };
  }
  if (t.t === "r" && listo(t.e)){ var x = t.e[0].v, s = Math.sqrt(x); return { t: N(s), hl: Hl(rTerm(t, false)), lab: TXP.raices, cuerpo: "√" + numTxt(x) + " = " + numTxt(s) + ".", etapa: "E", exacto: x >= 0 && s === Math.round(s) }; }
  if (t.t === "f" && listo(t.a) && listo(t.b)){ var p = t.a[0].v, q = t.b[0].v, d = p / q; return { t: N(d), hl: Hl(rTerm(t, false)), lab: TXP.barra, cuerpo: numTxt(p) + " ÷ " + vN(q, true) + " = " + numTxt(d) + ".", etapa: "E", exacto: q !== 0 && d === Math.round(d) }; }
  if (t.t === "m"){
    if (modo && modo.tipo === "negcuad" && (!modo.usado || modo.siempre) && t.x.t === "p" && t.x.b.t === "n" && t.x.n % 2 === 0){
      var w = Math.pow(t.x.b.v, t.x.n); modo.usado = true; modo.paso = modo.cuenta;
      return { t: N(w), hl: Hl(rTerm(t, false)), lab: TXP.exponentes, cuerpo: "−" + t.x.b.v + "<sup>" + t.x.n + "</sup> = " + numTxt(w) + ".", etapa: "E" };
    }
    var r = pasoE(t.x, modo); if (!r) return null;
    var nv = normT(Mn(r.t), false);
    return { t: nv, hl: Hl(rTerm(t, false)), lab: r.lab, cuerpo: r.cuerpo.replace(/\.$/, "") + TXP.seQueda + (nv.t === "n" ? numTxt(nv.v) : "") + ".", etapa: "E", exacto: r.exacto };
  }
  return null;
}

/* ---------- Solve the whole expression ---------- */
function resolver(e, modo){
  var pasos = [], cur = norm(e), guard = 0, exacto = true;
  if (modo) modo.cuenta = 0;
  while (!listo(cur) && guard++ < 40){
    if (modo) modo.cuenta = pasos.length;
    var r = paso(cur, modo); if (!r) break;
    if (!r.exacto) exacto = false;
    pasos.push({ antes: cur, hl: r.hl, desc: desc(r), despues: r.e, etapa: r.etapa });
    cur = r.e;
  }
  return { pasos: pasos, res: listo(cur) ? cur[0].v : NaN, exacto: exacto && listo(cur) };
}
function pasosHTML(R){
  return R.pasos.map(function(p){ return p.desc + '<div class="expr-paso">' + envuelve(rLista(p.hl), vozLista(p.antes)) + ' <span aria-hidden="true">→</span> ' + exprHTML(p.despues) + '</div>'; })
    .concat(['<span class="veredicto">' + TXP.resultado + numTxt(R.res) + '</span>']);
}
/* Makes expressions until every division and root is exact and the answer is reasonable */
function generaExacta(fab, max, filtro){
  for (var k = 0; k < 400; k++){ var e = fab(), R = resolver(e); if (R.exacto && Math.abs(R.res) <= (max || 500) && (!filtro || filtro(R))) return { e: e, R: R }; }
  var e2 = [N(2), "+", N(3), "×", N(4)]; return { e: e2, R: resolver(e2) };
}
/* Every operation that "could" be done now (to ask which one comes first) */
function sitios(e){
  var out = [];
  e.forEach(function(t, i){
    if (i % 2){ if (e[i - 1].t === "n" && e[i + 1].t === "n") out.push(vN(e[i - 1].v, i - 1 > 0) + " " + t + " " + vN(e[i + 1].v, true)); return; }
    if (t.t === "g") out = out.concat(sitios(t.e));
    if (t.t === "p"){ if (valorBase(t.b) !== null) out.push(rTerm(t, false)); else if (t.b.t === "g") out = out.concat(sitios(t.b.e)); }
    if (t.t === "r"){ if (listo(t.e)) out.push(rTerm(t, false)); else out = out.concat(sitios(t.e)); }
    if (t.t === "f") out = out.concat(sitios(t.a), sitios(t.b));
    if (t.t === "m" && t.x.t === "p" && valorBase(t.x.b) !== null) out.push(rTerm(t, false));
  });
  return out.filter(function(s, i, a){ return a.indexOf(s) === i; });
}
function primerSitio(e){
  var r = paso(norm(e)); if (!r) return null; var h = null;
  (function busca(l){ l.forEach(function(t, i){ if (i % 2) return; if (t.t === "h") h = t.html; else if (t.t === "g") busca(t.e); else if (t.t === "p" && t.b.t === "g") busca(t.b.e); else if (t.t === "r") busca(t.e); else if (t.t === "f"){ busca(t.a); busca(t.b); } else if (t.t === "m") busca([t.x]); }); })(r.hl);
  return h;
}
/* Common mistakes, simulated, become hints */
function pistasErrores(e, res, tipos){
  var p = [];
  (tipos || ["izqder", "potmul", "negcuad"]).forEach(function(tp){
    var R = resolver(e, { tipo: tp, siempre: true });
    if (R.exacto && R.res !== res && !p.some(function(x){ return x.v === R.res; })) p.push({ v: R.res, msg: TXP[tp] });
  });
  return p;
}
function practicaDe(fab, filtro, tipos){
  return function(){ var x = generaExacta(fab, 400, filtro), R = x.R;
    return { enun: TXP.resuelva + exprHTML(norm(x.e)) + ".", correcta: String(R.res), solucion: R.pasos.map(function(p){ return p.desc; }).join(" "), evalua: numE(R.res, pistasErrores(x.e, R.res, tipos)) }; };
}
function stepper(pre, fab, cola, filtro){
  var S = pasoAPaso(pre, []);
  function nuevo(){ var e = cola.length ? cola.shift() : generaExacta(fab, 400, filtro).e, R = resolver(e); $(pre + "-expr").innerHTML = exprHTML(norm(e)); S.carga(pasosHTML(R)); }
  $(pre + "-nuevo").addEventListener("click", nuevo); nuevo();
}
/* true if any number in the expression is negative (at any depth) */
function hayNeg(e){ return e.some(function(x, i){ if (i % 2) return false; if (x.t === "n") return x.v < 0; if (x.t === "g" || x.t === "r") return hayNeg(x.e); if (x.t === "p") return hayNeg([x.b]); if (x.t === "f") return hayNeg(x.a) || hayNeg(x.b); if (x.t === "m") return true; return false; }); }
function nA(a, b){ return N(aleatorio(a || 1, b || 12)); }
