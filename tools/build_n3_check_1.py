"""Level 3 · Topic 1 check (the five rules of exponents) — builds the page in English and in Spanish.
Twelve questions (four from each lesson), answered all at once, with a report by lesson that can be printed.
Ported from GEDparaHispanos (interactivos/exponentes_comprobacion)."""
import os
import bilingue as B
from bilingue import t
import n3

B.NIVEL = 3
ROOT = B.ROOT

LOGICA = r'''
function con(c, x){ return c === 1 ? x : X(c + x.h, c + " " + x.s); }
function une(a, b){ return X(a.h + b.h, a.s + " " + b.s); }
function neg(x){ return X(MENOS + x.h, T("minus ", "menos ") + x.s); }
function num(n){ return X(String(n), String(n)); }
var LEC = ES ? ["leccion-1-1.html", "leccion-1-2.html", "leccion-1-3.html"] : ["lesson-1-1.html", "lesson-1-2.html", "lesson-1-3.html"];

/* ---------- Lesson 1.1 ---------- */
var V11 = ["x", "y", "a", "m", "n", "b"];
var B11 = [
 function(){ var v = elige(V11), a = ale(2, 7), b = ale(2, 7), dif = a === b ? a + b + 1 : Math.abs(a - b);
   return {en: T("Simplify with the product rule:", "Simplifique aplicando la regla del producto:"), ex: porX(xp(v, a), xp(v, b)), ans: xp(v, a + b), dis: [xp(v, a * b), xp(v, dif), con(2, xp(v, a + b))],
     expl: T("The bases are the same, so the exponents are <strong>added</strong>: ", "Las bases son iguales, así que los exponentes se <strong>suman</strong>: ") + a + " + " + b + " = " + (a + b) + T(". Multiplying them is the most common mistake with this rule.", ". Multiplicarlos es el error más frecuente en esta regla.")}; },
 function(){ var v = elige(V11), a = ale(2, 5), b = ale(2, 5), c1 = ale(2, 6), c2 = ale(2, 6);
   return {en: T("Simplify the product of these two terms:", "Simplifique el producto de estos dos términos:"), ex: porX(con(c1, xp(v, a)), con(c2, xp(v, b))), ans: con(c1 * c2, xp(v, a + b)), dis: [con(c1 * c2, xp(v, a * b)), con(c1 + c2, xp(v, a + b)), con(c1 + c2, xp(v, a * b))],
     expl: T("The numbers are <strong>multiplied</strong> (", "Los coeficientes se <strong>multiplican</strong> (") + c1 + " · " + c2 + " = " + (c1 * c2) + T(") and the exponents are <strong>added</strong> (", ") y los exponentes se <strong>suman</strong> (") + a + " + " + b + " = " + (a + b) + ")."}; },
 function(){ var v = elige(V11), a = ale(2, 6), b = ale(2, 5); if (a + b === a * b) b = 3;
   return {en: T("Simplify with the power of a power rule:", "Simplifique aplicando la potencia de una potencia:"), ex: parX(xp(v, a), b), ans: xp(v, a * b), dis: [xp(v, a + b), con(b, xp(v, a)), xp(v, a)],
     expl: T("When a power is raised to a power, the exponents are <strong>multiplied</strong>: ", "Cuando una potencia se eleva a otra, los exponentes se <strong>multiplican</strong>: ") + a + " · " + b + " = " + (a * b) + T(". Adding them belongs to the product rule.", ". Sumarlos corresponde a la regla del producto.")}; },
 function(){ var v = elige(V11), c = ale(2, 5), a = ale(2, 3); if (c === a) c = a + 1;
   return {en: T("Simplify with the power of a product rule:", "Simplifique aplicando la potencia de un producto:"), ex: parX(con(c, X(v, v)), a), ans: con(Math.pow(c, a), xp(v, a)), dis: [con(c, xp(v, a)), con(c * a, xp(v, a)), con(Math.pow(c, a), X(v, v))],
     expl: T("The outside exponent reaches <strong>every</strong> factor in the parentheses, the number too: ", "El exponente de fuera alcanza a <strong>todos</strong> los factores del paréntesis, también al coeficiente: ") + c + "<sup>" + a + "</sup> = " + Math.pow(c, a) + "."}; },
 function(){ var v = elige(["x", "a", "m"]), w = elige(["y", "b", "n"]), a = ale(2, 4), b = ale(2, 4), c = ale(2, 3);
   return {en: T("Share out the outside exponent to both factors:", "Reparta el exponente de fuera a los dos factores:"), ex: parX(une(xp(v, a), xp(w, b)), c), ans: une(xp(v, a * c), xp(w, b * c)), dis: [une(xp(v, a + c), xp(w, b + c)), une(xp(v, a * c), xp(w, b)), une(xp(v, a), xp(w, b))],
     expl: T("The outside exponent goes to each factor, and the exponents are multiplied: ", "El exponente de fuera llega a cada factor y los exponentes se multiplican: ") + a + " · " + c + " = " + (a * c) + T(" and ", " y ") + b + " · " + c + " = " + (b * c) + "."}; }];

/* ---------- Lesson 1.2 ---------- */
var V12 = ["m", "n", "p", "z", "x", "y"];
var B12 = [
 function(){ var v = elige(V12), a = ale(6, 10), b = ale(1, 4);
   return {en: T("Simplify with the quotient rule:", "Simplifique aplicando la regla del cociente:"), ex: fracX(xp(v, a), xp(v, b)), ans: xp(v, a - b), dis: [xp(v, a + b), xp(v, a * b), fracX(num(1), xp(v, a - b))],
     expl: T("When you divide powers with the same base, the exponents are <strong>subtracted</strong>: ", "Al dividir potencias de la misma base, los exponentes se <strong>restan</strong>: ") + a + " − " + b + " = " + (a - b) + "."}; },
 function(){ var v = elige(V12), a = ale(5, 9), b = ale(1, 4), c2 = ale(2, 5), k = ale(2, 5), c1 = c2 * k;
   return {en: T("Simplify the whole quotient, number and letter:", "Simplifique el cociente completo, coeficiente y variable:"), ex: fracX(con(c1, xp(v, a)), con(c2, xp(v, b))), ans: con(k, xp(v, a - b)), dis: [con(k, xp(v, a + b)), con(c1 - c2, xp(v, a - b)), con(c1 * c2, xp(v, a - b))],
     expl: T("The numbers are <strong>divided</strong> (", "Los coeficientes se <strong>dividen</strong> (") + c1 + " ÷ " + c2 + " = " + k + T(") and the exponents are <strong>subtracted</strong> (", ") y los exponentes se <strong>restan</strong> (") + a + " − " + b + " = " + (a - b) + ")."}; },
 function(){ var v = elige(V12), a = ale(3, 8);
   return {en: T("Use the quotient rule and write the final answer:", "Aplique la regla del cociente y escriba el resultado final:"), ex: fracX(xp(v, a), xp(v, a)), ans: num(1), dis: [num(0), X(v, v), xp(v, 2 * a)],
     expl: a + " − " + a + T(" = 0, that is ", " = 0, es decir ") + v + "<sup>0</sup>" + T(". Any amount other than zero to the power zero is <strong>1</strong>, because anything divided by itself is 1.", ". Toda cantidad distinta de cero elevada a la cero vale <strong>1</strong>, porque cualquier expresión dividida entre sí misma da 1.")}; },
 function(){ var v = elige(["x", "a", "m"]), w = elige(["y", "b", "n"]), c = ale(2, 9), a = ale(2, 5), b = ale(2, 5), d = con(c, une(xp(v, a), xp(w, b)));
   return {en: T("What is the value of this expression?", "Calcule el valor de esta expresión:"), ex: parX(d, 0), ans: num(1), dis: [num(0), num(c), d],
     expl: T("The whole parentheses are raised to the zero power. If the base is not zero, the answer is <strong>1</strong>. A zero exponent is not the same as multiplying by zero.", "Todo el paréntesis está elevado a la cero. Si la base no es cero, el resultado es <strong>1</strong>. El exponente cero no es lo mismo que multiplicar por cero.")}; },
 function(){ var v = elige(V12), a = ale(2, 6);
   return {en: T("Rewrite with a positive exponent:", "Reescriba con exponente positivo:"), ex: xp(v, -a), ans: fracX(num(1), xp(v, a)), dis: [neg(xp(v, a)), fracX(num(1), xp(v, -a)), neg(fracX(num(1), xp(v, a)))],
     expl: T("A negative exponent means <strong>reciprocal</strong>, not a negative number: ", "Un exponente negativo indica <strong>recíproco</strong>, no un número negativo: ") + v + "<sup>−" + a + "</sup> = 1 ÷ " + v + "<sup>" + a + "</sup>."}; },
 function(){ var v = elige(V12), a = ale(2, 6);
   return {en: T("Rewrite this fraction with one negative exponent:", "Reescriba esta fracción usando un solo exponente negativo:"), ex: fracX(num(1), xp(v, a)), ans: xp(v, -a), dis: [xp(v, a), neg(xp(v, a)), neg(xp(v, -a))],
     expl: T("Moving a power from the bottom to the top <strong>changes the sign of its exponent</strong>: 1 ÷ ", "Pasar una potencia del denominador al numerador <strong>cambia el signo del exponente</strong>: 1 ÷ ") + v + "<sup>" + a + "</sup> = " + v + "<sup>−" + a + "</sup>."}; },
 function(){ var v = elige(V12), a = ale(2, 4), b = ale(6, 9);
   return {en: T("Simplify and give the answer with a positive exponent:", "Simplifique y exprese el resultado con exponente positivo:"), ex: fracX(xp(v, a), xp(v, b)), ans: fracX(num(1), xp(v, b - a)), dis: [xp(v, b - a), fracX(num(1), xp(v, a + b)), neg(xp(v, b - a))],
     expl: a + " − " + b + " = −" + (b - a) + T(", that is ", ", es decir ") + v + "<sup>−" + (b - a) + "</sup>" + T(". With a positive exponent: 1 ÷ ", ". Con exponente positivo: 1 ÷ ") + v + "<sup>" + (b - a) + "</sup>."}; }];

/* ---------- Lesson 1.3 ---------- */
var V13 = ["x", "y", "a", "m"];
var B13 = [
 function(){ var v = elige(V13), a = ale(2, 5), b = ale(2, 5), c = ale(2, 4);
   return {en: T("Simplify in order: parentheses first.", "Simplifique respetando el orden: primero el paréntesis."), ex: parX(porX(xp(v, a), xp(v, b)), c), ans: xp(v, (a + b) * c), dis: [xp(v, a * b * c), xp(v, a + b + c), xp(v, a * b + c)],
     expl: T("Inside the parentheses, <strong>add</strong> (", "Dentro del paréntesis se <strong>suman</strong> (") + a + " + " + b + " = " + (a + b) + T("), then <strong>multiply</strong> by the outside exponent (", ") y después se <strong>multiplica</strong> por el exponente de fuera (") + (a + b) + " · " + c + " = " + ((a + b) * c) + ")."}; },
 function(){ var v = elige(V13), a = ale(2, 4), b = ale(2, 4), ar = a * b, c = ale(1, ar - 1);
   return {en: T("Simplify the whole expression:", "Simplifique la expresión completa:"), ex: fracX(parX(xp(v, a), b), xp(v, c)), ans: xp(v, ar - c), dis: [xp(v, a + b - c), xp(v, ar + c), fracX(num(1), xp(v, ar - c))],
     expl: T("First the power of a power: ", "Primero la potencia de una potencia: ") + a + " · " + b + " = " + ar + T(". Then the quotient: ", ". Después el cociente: ") + ar + " − " + c + " = " + (ar - c) + "."}; },
 function(){ var v = elige(V13), c = ale(2, 4), a = ale(2, 3), n = ale(2, 3), b = ale(2, 5), cn = Math.pow(c, n);
   return {en: T("Simplify: raise the parentheses, then multiply.", "Simplifique: eleve el paréntesis y después multiplique."), ex: porX(parX(con(c, xp(v, a)), n), xp(v, b)), ans: con(cn, xp(v, a * n + b)), dis: [con(c * n, xp(v, a * n + b)), con(cn, xp(v, a * n * b)), con(cn, xp(v, a + n + b))],
     expl: T("The outside exponent raises the number too (", "El exponente de fuera eleva también al coeficiente (") + c + "<sup>" + n + "</sup> = " + cn + T(") and multiplies the exponent of the letter (", ") y multiplica el exponente de la variable (") + a + " · " + n + " = " + (a * n) + T("). Last, the product rule adds: ", "). Por último, la regla del producto suma: ") + (a * n) + " + " + b + " = " + (a * n + b) + "."}; },
 function(){ var v = elige(["x", "a"]), w = elige(["y", "b"]), a = ale(2, 4), b = ale(2, 4), c = ale(2, 3), d = ale(1, a * c - 1), e = ale(1, b * c - 1);
   return {en: T("Simplify the expression with two letters:", "Simplifique la expresión con las dos variables:"), ex: fracX(parX(une(xp(v, a), xp(w, b)), c), une(xp(v, d), xp(w, e))), ans: une(xp(v, a * c - d), xp(w, b * c - e)),
     dis: [une(xp(v, a + c - d), xp(w, b + c - e)), une(xp(v, a * c + d), xp(w, b * c + e)), une(xp(v, a * c - d), xp(w, b * c + e))],
     expl: T("Share out the outside exponent (", "Se reparte el exponente de fuera (") + a + " · " + c + " = " + (a * c) + T(" and ", " y ") + b + " · " + c + " = " + (b * c) + T("), then subtract the bottom one letter at a time: ", ") y después se resta el denominador letra por letra: ") + (a * c) + " − " + d + " = " + (a * c - d) + T(" and ", " y ") + (b * c) + " − " + e + " = " + (b * c - e) + "."}; },
 function(){ var v = elige(V13), a = ale(2, 3), b = ale(2, 3), ar = a * b, c = ar + ale(1, 4);
   return {en: T("Simplify and give the answer with positive exponents:", "Simplifique y exprese el resultado con exponentes positivos:"), ex: fracX(parX(xp(v, a), b), xp(v, c)), ans: fracX(num(1), xp(v, c - ar)), dis: [xp(v, c - ar), fracX(num(1), xp(v, ar + c)), fracX(num(1), xp(v, ar * c))],
     expl: T("On top: ", "Arriba queda ") + a + " · " + b + " = " + ar + T(". Subtracting: ", ". Al restar: ") + ar + " − " + c + " = −" + (c - ar) + T(". A negative exponent is rewritten as a fraction: 1 ÷ ", ". Un exponente negativo se reescribe como fracción: 1 ÷ ") + v + "<sup>" + (c - ar) + "</sup>."}; },
 function(){ var v = elige(V13), a = ale(2, 5), b = ale(2, 5), c = ale(2, 4);
   return {en: T("Simplify the whole expression:", "Simplifique la expresión completa:"), ex: porX(parX(con(c, xp(v, a)), 0), xp(v, b)), ans: xp(v, b), dis: [con(c, xp(v, a + b)), num(0), con(c, xp(v, b))],
     expl: T("The first factor is raised to the zero power, so it is <strong>1</strong>. Multiplying by 1 changes nothing, so only ", "El primer factor está elevado a la cero, así que vale <strong>1</strong>. Multiplicar por 1 no cambia nada, de modo que solo queda ") + v + "<sup>" + b + "</sup>" + T(" is left.", ".")}; }];

var BLOQUES = [{nombre: T("Rules for multiplying (Lesson 1.1)", "Reglas de la multiplicación (Lección 1.1)"), gens: B11, lec: 0},
               {nombre: T("Quotient, zero, and negative exponents (Lesson 1.2)", "Cociente, exponente cero y negativos (Lección 1.2)"), gens: B12, lec: 1},
               {nombre: T("Several rules combined (Lesson 1.3)", "Varias reglas combinadas (Lección 1.3)"), gens: B13, lec: 2}];
var POR_BLOQUE = 4, APRUEBA = 9, ronda = [], corregida = false;

function opciones(q){
  var lista = [q.ans], vistos = {}; vistos[q.ans.h] = 1;
  q.dis.forEach(function(d){ if (lista.length < 4 && !vistos[d.h]){ vistos[d.h] = 1; lista.push(d); } });
  [con(2, q.ans), X(q.ans.h + "<sup>2</sup>", q.ans.s + T(" squared", " al cuadrado"))].forEach(function(d){ if (lista.length < 4 && !vistos[d.h]){ vistos[d.h] = 1; lista.push(d); } });
  return baraja(lista);
}
function fechaHoy(){
  var d = new Date(), m = ES ? ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
                            : ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
  return ES ? d.getDate() + " de " + m[d.getMonth()] + " de " + d.getFullYear() : m[d.getMonth()] + " " + d.getDate() + ", " + d.getFullYear();
}
function genera(){
  ronda = [];
  BLOQUES.forEach(function(bl){ var g = baraja(bl.gens); for (var i = 0; i < POR_BLOQUE; i++){ var q = g[i % g.length](); q.bloque = bl; q.ops = opciones(q); q.elegida = null; ronda.push(q); } });
  ronda = baraja(ronda);
}
function pinta(){
  var c = $("preguntas"); c.innerHTML = "";
  ronda.forEach(function(q, i){
    var d = document.createElement("fieldset"); d.className = "pregunta-c";
    d.innerHTML = "<legend><span class=\"num\" aria-hidden=\"true\">" + (i + 1) + "</span> " + T("Question ", "Pregunta ") + (i + 1) + T(" of ", " de ") + ronda.length + ": " + q.en + "</legend>" +
      '<div class="expr-grande">' + ver(q.ex) + "</div>";
    var o = document.createElement("div"); o.className = "opciones";
    q.ops.forEach(function(op, j){
      var b = document.createElement("button"); b.type = "button"; b.className = "opcion"; b.setAttribute("aria-pressed", "false"); b.innerHTML = ver(op);
      b.addEventListener("click", function(){
        if (corregida) return;
        q.elegida = j;
        Array.prototype.forEach.call(o.children, function(x){ x.setAttribute("aria-pressed", "false"); x.classList.remove("elegida"); });
        b.setAttribute("aria-pressed", "true"); b.classList.add("elegida");
      });
      o.appendChild(b);
    });
    d.appendChild(o);
    var fb = document.createElement("div"); fb.className = "fb"; fb.setAttribute("role", "status"); d.appendChild(fb);
    c.appendChild(d);
  });
}
function comprueba(){
  corregida = true;
  var ok = 0, por = {};
  BLOQUES.forEach(function(bl){ por[bl.nombre] = {c: 0, t: 0, lec: bl.lec}; });
  var fs = $("preguntas").querySelectorAll("fieldset");
  ronda.forEach(function(q, i){
    var bs = fs[i].querySelectorAll(".opcion"), fb = fs[i].querySelector(".fb"), bien = q.elegida !== null && q.ops[q.elegida].h === q.ans.h;
    por[q.bloque.nombre].t++;
    if (bien){ ok++; por[q.bloque.nombre].c++; }
    Array.prototype.forEach.call(bs, function(b, j){ b.disabled = true; if (q.ops[j].h === q.ans.h) b.classList.add("correcta"); });
    if (q.elegida !== null && !bien) bs[q.elegida].classList.add("incorrecta");
    fb.className = "fb " + (bien ? "bien" : "mal");
    fb.innerHTML = "<strong>" + (bien ? T("Correct.", "Correcto.") : (q.elegida === null ? T("Not answered.", "Sin responder.") : T("Not correct.", "Incorrecto.")) + (bien ? "" : T(" The right answer is ", " La respuesta correcta es ") + ver(q.ans) + ".")) + "</strong> " + q.expl;
  });
  var pct = Math.round(ok / ronda.length * 100), r = $("resultado");
  r.className = "resultado " + (ok >= APRUEBA ? "aprob" : "repro");
  r.innerHTML = T("Score: ", "Resultado: ") + "<strong>" + ok + T(" of ", " de ") + ronda.length + "</strong> (" + pct + " %). " +
    (ok >= APRUEBA ? T("You have shown you know Topic 1. You can go on to Topic 2.", "Demostró que domina el Tema 1. Puede continuar al Tema 2.")
                   : T("You need 9 right answers. Review the lessons marked below and try again.", "Hacen falta 9 aciertos. Repase las lecciones señaladas abajo e inténtelo de nuevo."));
  $("informe-cuerpo").innerHTML = BLOQUES.map(function(bl){
    var m = por[bl.nombre], p = Math.round(m.c / m.t * 100), j = p >= 75 ? T("Mastered", "Dominado") : (p >= 50 ? T("Getting there", "En desarrollo") : T("Needs review", "Requiere repaso"));
    return '<tr><th scope="row">' + bl.nombre + "</th><td>" + m.c + T(" of ", " de ") + m.t + "</td><td>" + p + " %</td><td>" + j + (p < 75 ? ' · <a href="' + LEC[bl.lec] + '">' + T("Review the lesson", "Repasar la lección") + "</a>" : "") + "</td></tr>";
  }).join("");
  $("informe").hidden = false; $("b-comprobar").hidden = true; $("b-nueva").hidden = false; $("b-imprimir").hidden = false;
  $("nombre-imp").textContent = $("nombre").value.trim() ? T("Student: ", "Estudiante: ") + $("nombre").value.trim() : "";
  r.focus();
}
function nueva(){
  corregida = false; $("resultado").className = "resultado"; $("resultado").textContent = "";
  $("informe").hidden = true; $("b-comprobar").hidden = false; $("b-nueva").hidden = true; $("b-imprimir").hidden = true;
  genera(); pinta(); window.scrollTo({top: $("preguntas").offsetTop - 20, behavior: "smooth"});
}
$("fecha").textContent = fechaHoy();
$("b-comprobar").addEventListener("click", comprueba);
$("b-nueva").addEventListener("click", nueva);
$("b-imprimir").addEventListener("click", function(){ window.print(); });
genera(); pinta();
'''

ESTILO = n3.ESTILO_EXP + """
  fieldset.pregunta-c{border:2px solid var(--tema-bg2);border-radius:12px;padding:14px 18px;margin:16px 0;background:#fff;}
  fieldset.pregunta-c legend{font-weight:700;color:var(--tema-d);padding:0 6px;font-size:16px;}
  fieldset.pregunta-c legend .num{display:inline-flex;width:28px;height:28px;font-size:14px;margin-right:4px;vertical-align:middle;}
  .opcion.elegida{border-color:var(--tema);background:var(--tema-bg);font-weight:700;}
  .resultado{font-size:18px;margin:16px 0;padding:14px 18px;border-radius:10px;}
  .resultado:empty{display:none;}
  .resultado.aprob{background:var(--ok-bg);border-left:6px solid var(--ok);}
  .resultado.repro{background:#fff8e1;border-left:6px solid #f9a825;}
  .datos-est{display:flex;flex-wrap:wrap;gap:16px;align-items:flex-end;}
  table.informe{border-collapse:collapse;width:100%;margin:10px 0;font-size:15px;}
  table.informe th,table.informe td{border:1px solid #c8c8c8;padding:8px 12px;text-align:left;}
  table.informe thead th{background:var(--tema-bg);color:var(--tema-d);}
  .solo-imp{display:none;}
  @media print{
    .lg-bar,.saltar,.fila-btn,.no-imp,footer.pie .tm,#gph-calc-btn,.gph-calc,[data-gph-calculadora]{display:none !important;}
    .solo-imp{display:block;}
    header.principal{background:#fff !important;color:#000 !important;border:2px solid #000;}
    fieldset.pregunta-c{break-inside:avoid;}
    body{background:#fff;}
  }"""

def pagina():
    filas = "".join(f"<tr><td>{a}</td><td>{b}</td><td>{d}</td></tr>" for a, b, c, d in n3.tabla_reglas(True))
    lang = B.L
    archivo = "math/level-3/topic-1-check.html" if lang == "en" else "es/matematicas/nivel-3/comprobacion-tema-1.html"
    otro = "/es/matematicas/nivel-3/comprobacion-tema-1.html" if lang == "en" else "/math/level-3/topic-1-check.html"
    js = LOGICA
    html = f'''<!DOCTYPE html>
<!-- LearnGED · Level 3 · Topic 1 check — built by tools/build_n3_check_1.py
     José M. Fernández · CC BY-NC-SA 4.0 -->
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{t("Topic 1 check · The five rules of exponents · LearnGED", "Comprobación del Tema 1 · Las cinco reglas de los exponentes · LearnGED")}</title>
<meta name="license" content="CC BY-NC-SA 4.0"><link rel="license" href="https://creativecommons.org/licenses/by-nc-sa/4.0/">
<link rel="alternate" hreflang="{"es" if lang == "en" else "en"}" href="{otro}">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="../practice.css">
<link rel="stylesheet" href="{"../" if lang == "en" else "../../../math/"}practice.css" media="not all">
<style>
{ESTILO}
</style>
</head>
<body>
<nav class="lg-bar" aria-label="LearnGED"><a class="lg-logo" href="/"><img src="/img/learnged-logo-horizontal.svg" alt="{t("LearnGED home", "Inicio de LearnGED")}" height="34"></a><a class="lg-link" href="./">{t("Math · Level 3 lessons", "Matemáticas · Lecciones del Nivel 3")}</a></nav>
<a class="saltar" href="#preguntas">{t("Skip to the questions", "Saltar a las preguntas")}</a>
<div class="contenedor">
  <header class="principal">
    <div class="ruta">{t("Level 3 · Topic 1 · Rules of exponents", "Nivel 3 · Tema 1 · Reglas de los exponentes")}</div>
    <h1>{t("Topic 1 check · The five rules of exponents", "Comprobación del Tema 1 · Las cinco reglas de los exponentes")}</h1>
    <div class="meta">{t("12 questions made at random · a review of Lessons 1.1, 1.2, and 1.3", "12 preguntas generadas al azar · repaso de las lecciones 1.1, 1.2 y 1.3")}</div>
  </header>

  <section class="panel no-imp">
    <h2>{t("How it works", "Cómo funciona")}</h2>
    <p>{t("There are twelve questions: four from each lesson. Answer all of them, then press <strong>Check my answers</strong>. You will see the explanation of each exercise and a report by lesson that tells you what to review. You pass with <strong>9 right answers out of 12</strong>. Here there are no hints: it is a check, like a small test.", "Son doce preguntas: cuatro de cada lección. Responda todas y después pulse <strong>Revisar mis respuestas</strong>. Verá la explicación de cada ejercicio y un informe por lección que le dice qué repasar. Se aprueba con <strong>9 aciertos de 12</strong>. Aquí no hay pistas: es una comprobación, como un pequeño examen.")}</p>
    <div class="datos-est">
      <div class="campo"><label for="nombre">{t("Your name (for the printed report)", "Su nombre (para el informe impreso)")}</label><input type="text" id="nombre" autocomplete="name" style="min-width:260px"></div>
      <p>{t("Date:", "Fecha:")} <span id="fecha"></span></p>
    </div>
  </section>
  <p class="solo-imp" id="nombre-imp"></p>

  <div id="preguntas"></div>

  <div class="resultado" id="resultado" tabindex="-1" aria-live="polite"></div>
  <div class="fila-btn">
    <button type="button" class="btn" id="b-comprobar">{t("Check my answers", "Revisar mis respuestas")}</button>
    <button type="button" class="btn" id="b-nueva" hidden>{t("Make a new check", "Generar otra comprobación")}</button>
    <button type="button" class="btn-sec" id="b-imprimir" hidden>{t("Print the report", "Imprimir el informe")}</button>
  </div>

  <section id="informe" hidden>
    <h2>{t("Report by lesson", "Informe por lección")}</h2>
    <p>{t("A lesson counts as mastered from 75 % on. If a lesson needs review, go back to it and to its practice page before you take the check again.", "Una lección se considera dominada a partir del 75 %. Si una lección requiere repaso, vuelva a ella y a su página de práctica antes de repetir la comprobación.")}</p>
    <div class="tabla-scroll" role="region" tabindex="0" aria-label="{t("Report by lesson (table you can scroll sideways)", "Informe por lección (tabla desplazable horizontalmente)")}">
    <table class="informe"><caption class="cap-oculto">{t("Right answers, percent, and level for each lesson", "Aciertos, porcentaje y nivel de cada lección")}</caption>
    <thead><tr><th scope="col">{t("Lesson", "Lección")}</th><th scope="col">{t("Right", "Aciertos")}</th><th scope="col">{t("Percent", "Porcentaje")}</th><th scope="col">{t("Level", "Nivel")}</th></tr></thead>
    <tbody id="informe-cuerpo"></tbody></table></div>
  </section>

  <section class="panel">
    <h2>{t("Reminder: the five rules of exponents", "Recordatorio: las cinco reglas de los exponentes")}</h2>
    <div class="tabla-scroll" role="region" tabindex="0" aria-label="{t("The five rules (table you can scroll sideways)", "Las cinco reglas (tabla desplazable horizontalmente)")}"><table class="reglas"><caption>{t("Each rule, its pattern, and an example.", "Cada regla, su patrón y un ejemplo.")}</caption>
    <thead><tr><th scope="col">{t("Rule", "Regla")}</th><th scope="col">{t("Pattern", "Patrón")}</th><th scope="col">{t("Example", "Ejemplo")}</th></tr></thead><tbody>{filas}</tbody></table></div>
    <p>{t("In every rule, the base cannot be zero when it is in a denominator.", "En todas las reglas, la base debe ser distinta de cero cuando aparece en un denominador.")}</p>
  </section>

  <footer class="pie">
    <p><strong>{t("Level 3 · Topic 1 · Rules of exponents · LearnGED", "Nivel 3 · Tema 1 · Reglas de los exponentes · LearnGED")}</strong><br>
    José M. Fernández, ABE/ASE Math Master Teacher, Harry S. Truman College — City Colleges of Chicago.</p>
    <p>{t("This work is licensed under", "Esta obra está bajo la licencia")} <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/" target="_blank" rel="noopener noreferrer">Creative Commons BY-NC-SA 4.0</a>.</p>
    <p class="tm">GED® is a registered trademark of the American Council on Education (ACE) and administered exclusively by GED Testing Service LLC under license. LearnGED is not affiliated with, endorsed by, or approved by ACE or GED Testing Service.</p>
  </footer>
</div>
<script src="../practice.js"></script>
<script src="/math/exponents.js"></script>
<script>
{js.strip()}
</script>
</body>
</html>
'''
    if lang == "es":
        html = html.replace('href="../practice.css"', 'href="/math/practice.css"').replace('src="../practice.js"', 'src="/math/practice.js"')
    html = html.replace('\n<link rel="stylesheet" href="../practice.css" media="not all">', "").replace('\n<link rel="stylesheet" href="../../../math/practice.css" media="not all">', "")
    open(os.path.join(ROOT, archivo), "w", encoding="utf-8").write(html)
    print("ok", archivo)

if __name__ == "__main__":
    for L in ("en", "es"):
        B.L = L
        pagina()
    B.L = "en"
