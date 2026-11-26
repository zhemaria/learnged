"""Level 4 · Final check (30 questions that cover the eight topics) — builds the page in English and in Spanish.
Imported from GEDparaHispanos (clase_mate4/leccion_8-3.html, «Evaluación final · 30 preguntas»): the 30 questions A–AD (5 for each block),
now with an explanation for each one and a report by topic with links to the lessons.
  math/level-4/final-check-level-4.html · es/matematicas/nivel-4/evaluacion-final-nivel-4.html"""
import os, json
import bilingue as B
from bilingue import t

B.NIVEL = 4
ROOT = B.ROOT

def fr(a, b):
    return f'<span class="frac" aria-hidden="true"><span>{a}</span><span>{b}</span></span><span class="sr-only">{a} {t("over", "sobre")} {b}</span>'

def preguntas():
    """(topic, lesson, question, options, index of the right one, explanation)"""
    Y = lambda a, b: t(f"x = {a} and x = {b}", f"x = {a} y x = {b}")
    return [
     (1, "1-1", t("A. The distance between (0, 0) and (3, 4) is:", "A. La distancia entre (0, 0) y (3, 4) es:"), ["7", "25", "12", "5"], 3,
      t("d = √(3² + 4²) = √25 = 5. Adding the differences (7) is not the formula; 25 is d², not d.", "d = √(3² + 4²) = √25 = 5. Sumar las diferencias (7) no es la fórmula; 25 es d², no d.")),
     (1, "1-1", t("B. The midpoint of (2, 4) and (6, 8) is:", "B. El punto medio de (2, 4) y (6, 8) es:"), ["(4, 6)", "(8, 12)", "(2, 2)", "(4, 4)"], 0,
      t("Average each coordinate: ((2 + 6)/2, (4 + 8)/2) = (4, 6).", "Se promedia cada coordenada: ((2 + 6)/2, (4 + 8)/2) = (4, 6).")),
     (1, "1-2", t("C. The slope between (1, 2) and (3, 8) is:", "C. La pendiente entre (1, 2) y (3, 8) es:"), ["2", fr(1, 3), "3", "4"], 2,
      t("m = (8 − 2) / (3 − 1) = 6/2 = 3. 1/3 is the fraction upside down.", "m = (8 − 2) / (3 − 1) = 6/2 = 3. 1/3 es la fracción al revés.")),
     (2, "2-1", t("D. The volume of a sphere with radius 3 inches (V = ⁴⁄₃πr³) is:", "D. El volumen de una esfera de radio 3 pulgadas (V = ⁴⁄₃πr³) es:"), [t("27π in³", "27π pulg³"), t("36π in³", "36π pulg³"), t("12π in³", "12π pulg³"), t("9π in³", "9π pulg³")], 1,
      t("⁴⁄₃ · π · 3³ = ⁴⁄₃ · 27π = 36π cubic inches.", "⁴⁄₃ · π · 3³ = ⁴⁄₃ · 27π = 36π pulgadas cúbicas.")),
     (2, "2-1", t("E. The volume of a cone with r = 3 ft and h = 4 ft (V = ⅓πr²h) is:", "E. El volumen de un cono con r = 3 pies y h = 4 pies (V = ⅓πr²h) es:"), [t("12π ft³", "12π pies³"), t("36π ft³", "36π pies³"), t("9π ft³", "9π pies³"), t("24π ft³", "24π pies³")], 0,
      t("⅓ · π · 3² · 4 = ⅓ · 36π = 12π cubic feet. 36π is the cylinder; the cone is one third.", "⅓ · π · 3² · 4 = ⅓ · 36π = 12π pies cúbicos. 36π es el cilindro; el cono es un tercio.")),
     (3, "3-1", "F. (x + 3)(x − 3) =", ["x² + 9", "x² − 6x + 9", "x² − 3", "x² − 9"], 3,
      t("A sum times a difference: x² − 3² = x² − 9. The middle terms cancel.", "Suma por diferencia: x² − 3² = x² − 9. Los términos del medio se cancelan.")),
     (3, "3-3", t("G. Factor x² − 5x + 6.", "G. Factorice x² − 5x + 6."), ["(x + 2)(x + 3)", "(x − 1)(x − 6)", "(x − 2)(x − 3)", "(x − 2)(x + 3)"], 2,
      t("Two numbers with product 6 and sum −5: −2 and −3.", "Dos números de producto 6 y suma −5: −2 y −3.")),
     (3, "3-1", "H. (x + 4)² =", ["x² + 16", "x² + 8x + 16", "x² + 4x + 16", "x² + 8x + 8"], 1,
      t("(x + 4)(x + 4) = x² + 2 · 4 · x + 16 = x² + 8x + 16. x² + 16 forgets the middle term.", "(x + 4)(x + 4) = x² + 2 · 4 · x + 16 = x² + 8x + 16. x² + 16 olvida el término del medio.")),
     (3, "3-2", t("I. The greatest common factor of 6x² + 9x gives:", "I. Sacar el factor común de 6x² + 9x da:"), ["x(6x + 9)", "3(2x² + 3x)", "3x(2x + 3)", "6x(x + 3)"], 2,
      t("The greatest common factor is 3x: 6x² ÷ 3x = 2x and 9x ÷ 3x = 3. The other choices are not completely factored, or are wrong.", "El máximo factor común es 3x: 6x² ÷ 3x = 2x y 9x ÷ 3x = 3. Las demás opciones no están factorizadas por completo o son incorrectas.")),
     (3, "3-2", t("J. Factor x² − 16.", "J. Factorice x² − 16."), ["(x − 16)(x + 1)", "(x + 4)(x − 4)", "(x + 8)(x − 2)", "(x − 4)²"], 1,
      t("A difference of squares: x² − 4² = (x + 4)(x − 4).", "Diferencia de cuadrados: x² − 4² = (x + 4)(x − 4).")),
     (4, "4-1", t("K. Solve x² − 9 = 0.", "K. Resuelva x² − 9 = 0."), [Y(3, "−3"), "x = 9", "x = 3", "x = ±81"], 0,
      t("x² = 9, so x = 3 or x = −3. Do not forget the negative root.", "x² = 9, así que x = 3 o x = −3. No olvide la raíz negativa.")),
     (4, "4-1", t("L. Solve (x − 2)(x + 5) = 0.", "L. Resuelva (x − 2)(x + 5) = 0."), [Y("−2", 5), Y(2, 5), "x = 10", Y(2, "−5")], 3,
      t("Each factor equal to 0: x − 2 = 0 → x = 2; x + 5 = 0 → x = −5.", "Cada factor igual a 0: x − 2 = 0 → x = 2; x + 5 = 0 → x = −5.")),
     (4, "4-3", t("M. The discriminant of x² + 2x + 1 is b² − 4ac = 0. That means there is:", "M. El discriminante de x² + 2x + 1 es b² − 4ac = 0. Eso indica que hay:"), [t("two different real roots", "dos raíces reales distintas"), t("no real root", "ninguna raíz real"), t("one double root", "una raíz doble"), t("three roots", "tres raíces")], 2,
      t("Discriminant 0: one double root (x = −1). Positive would be two; negative, none.", "Discriminante 0: una raíz doble (x = −1). Positivo serían dos; negativo, ninguna.")),
     (4, "4-1", t("N. Solve x² − 7x + 12 = 0.", "N. Resuelva x² − 7x + 12 = 0."), ["−3 " + t("and", "y") + " −4", "7 " + t("and", "y") + " 12", "3 " + t("and", "y") + " 4", "1 " + t("and", "y") + " 12"], 2,
      t("(x − 3)(x − 4) = 0, so x = 3 and x = 4. Check: 9 − 21 + 12 = 0.", "(x − 3)(x − 4) = 0, así que x = 3 y x = 4. Comprobación: 9 − 21 + 12 = 0.")),
     (4, "4-3", t("O. The quadratic formula is x =", "O. La fórmula cuadrática es x ="), ["−b / (2a)", "(b ± √(b² − 4ac)) / (2a)", "b² − 4ac", "(−b ± √(b² − 4ac)) / (2a)"], 3,
      t("x = (−b ± √(b² − 4ac)) / (2a). −b/(2a) is only the x of the vertex, and b² − 4ac is the discriminant.", "x = (−b ± √(b² − 4ac)) / (2a). −b/(2a) es solo la x del vértice, y b² − 4ac es el discriminante.")),
     (5, "5-1", t("P. Simplify (x² − 9) / (x − 3), with x ≠ 3.", "P. Simplifique (x² − 9) / (x − 3), con x ≠ 3."), ["x − 3", "x + 3", "x + 9", "3"], 1,
      t("(x + 3)(x − 3) / (x − 3) = x + 3. You cancel factors, never terms.", "(x + 3)(x − 3) / (x − 3) = x + 3. Se cancelan factores, nunca términos.")),
     (5, "5-1", t("Q. For which value is 1 / (x − 2) NOT defined?", "Q. ¿Para qué valor NO está definida 1 / (x − 2)?"), ["x = 2", "x = 0", "x = −2", "x = 1"], 0,
      t("The denominator is 0 when x = 2, and you cannot divide by zero.", "El denominador vale 0 cuando x = 2, y no se puede dividir entre cero.")),
     (5, "5-2", "R. " + fr(2, "x") + " · " + fr("x", 5) + " =", [fr("2x", 5), fr(10, "x"), fr(2, "5x"), fr(2, 5)], 3,
      t("Multiply: 2x / 5x, and the x cancels: 2/5.", "Se multiplica: 2x / 5x, y la x se cancela: 2/5.")),
     (5, "5-2", "S. " + fr(1, "x") + " + " + fr(2, "x") + " =", [fr(3, "x"), fr(3, "2x"), fr(2, "x²"), fr(3, "x²")], 0,
      t("Same denominator: add the numerators and keep the denominator: 3/x.", "Mismo denominador: se suman los numeradores y se conserva el denominador: 3/x.")),
     (5, "5-2", t("T. Dividing by a fraction is multiplying by its:", "T. Dividir entre una fracción es multiplicar por su:"), [t("opposite", "opuesto"), t("reciprocal", "recíproco"), t("square", "cuadrado"), t("square root", "raíz")], 1,
      t("Dividing by a/b is multiplying by b/a, its reciprocal.", "Dividir entre a/b es multiplicar por b/a, su recíproco.")),
     (6, "6-1", t("U. Solve y = 2x and x + y = 9.", "U. Resuelva y = 2x ; x + y = 9."), ["(6, 3)", "(3, 3)", "(3, 6)", "(9, 0)"], 2,
      t("Substitute: x + 2x = 9, x = 3, y = 6. Check: 6 = 2(3) and 3 + 6 = 9.", "Se sustituye: x + 2x = 9, x = 3, y = 6. Comprobación: 6 = 2(3) y 3 + 6 = 9.")),
     (6, "6-2", t("V. Solve by elimination x + y = 10 and x − y = 4.", "V. Resuelva por eliminación x + y = 10 ; x − y = 4."), ["(3, 7)", "(7, 3)", "(5, 5)", "(10, 4)"], 1,
      t("Add the equations: 2x = 14, x = 7; then y = 10 − 7 = 3.", "Se suman las ecuaciones: 2x = 14, x = 7; luego y = 10 − 7 = 3.")),
     (6, "6-2", t("W. Solving a system, you get 0 = 5. The system:", "W. Al resolver un sistema se obtiene 0 = 5. El sistema:"), [t("has one solution", "tiene una solución"), t("has infinitely many solutions", "tiene infinitas soluciones"), t("has no solution", "no tiene solución"), t("has two solutions", "tiene dos soluciones")], 2,
      t("A false statement means the lines are parallel: no solution. 0 = 0 would mean infinitely many.", "Una igualdad falsa significa rectas paralelas: no hay solución. 0 = 0 significaría infinitas.")),
     (6, "6-3", t("X. Two parallel lines make a system:", "X. Dos rectas paralelas forman un sistema:"), [t("with one solution", "con una solución"), t("with infinitely many solutions", "con infinitas soluciones"), t("that is dependent", "dependiente"), t("with no solution", "sin solución")], 3,
      t("Parallel lines never cross, so no point is on both: no solution (inconsistent).", "Las rectas paralelas nunca se cruzan: ningún punto está en las dos, así que no hay solución (inconsistente).")),
     (6, "6-3", t("Y. Two adult tickets and one child ticket cost $25; one adult and one child cost $15. What is the price of the adult ticket?", "Y. Dos boletos de adulto y uno de niño cuestan $25; un adulto y un niño cuestan $15. ¿Precio del adulto?"), ["$10", "$5", "$15", "$12"], 0,
      t("Subtract the equations: (2a + c) − (a + c) = 25 − 15, so a = $10 (and the child ticket is $5).", "Se restan las ecuaciones: (2a + n) − (a + n) = 25 − 15, así que a = $10 (y el de niño, $5).")),
     (7, "7-2", t("Z. If f(x) = 2x² − 3x + 1, what is f(2)?", "Z. Si f(x) = 2x² − 3x + 1, ¿cuánto vale f(2)?"), ["1", "0", "11", "3"], 3,
      t("f(2) = 2(4) − 3(2) + 1 = 8 − 6 + 1 = 3.", "f(2) = 2(4) − 3(2) + 1 = 8 − 6 + 1 = 3.")),
     (8, "8-1", t("AA. The vertex of f(x) = x² − 4x + 3 is:", "AA. El vértice de f(x) = x² − 4x + 3 es:"), ["(−2, −1)", "(2, −1)", "(2, 1)", "(4, 3)"], 1,
      t("x = −(−4)/(2 · 1) = 2; f(2) = 4 − 8 + 3 = −1.", "x = −(−4)/(2 · 1) = 2; f(2) = 4 − 8 + 3 = −1.")),
     (8, "8-2", t("AB. f(x) = 3ˣ is a function that is:", "AB. f(x) = 3ˣ es una función:"), [t("exponential", "exponencial"), t("linear", "lineal"), t("quadratic", "cuadrática"), t("rational", "racional")], 0,
      t("x is in the exponent: exponential (it grows, because the base 3 is greater than 1).", "La x está en el exponente: exponencial (crece, porque la base 3 es mayor que 1).")),
     (7, "7-3", t("AC. The average rate of change if f(1) = 4 and f(5) = 20 is:", "AC. Tasa de cambio promedio si f(1) = 4 y f(5) = 20:"), ["16", "5", "4", "24"], 2,
      t("(20 − 4) / (5 − 1) = 16/4 = 4. 16 is only the change in y.", "(20 − 4) / (5 − 1) = 16/4 = 4. 16 es solo el cambio en y.")),
     (7, "7-3", t("AD. The outputs 2, 4, 8, 16 (multiplied by 2 each time) belong to a function that is:", "AD. Las salidas 2, 4, 8, 16 (se multiplican por 2) corresponden a una función:"), [t("linear", "lineal"), t("quadratic", "cuadrática"), t("constant", "constante"), t("exponential", "exponencial")], 3,
      t("A constant ratio (×2) is the pattern of an exponential function. A linear one would add the same.", "Una razón constante (×2) es el patrón de una función exponencial. Una lineal sumaría lo mismo.")),
    ]

TEMAS = [("Analytic geometry", "Geometría analítica"), ("3D volume and polynomials", "Volumen 3D y polinomios"), ("Multiplying and factoring", "Multiplicación y factorización"),
         ("Quadratic equations", "Ecuaciones cuadráticas"), ("Rational expressions", "Expresiones racionales"), ("Systems of linear equations", "Sistemas de ecuaciones lineales"),
         ("Systems of inequalities and functions", "Sistemas de desigualdades y funciones"), ("Modeling with functions", "Modelado de funciones")]

LOGICA = r'''
function T(en, es){ return ES ? es : en; }
var PREG = window.PREG, TEMAS = window.TEMAS, APRUEBA = 21, corregida = false;
var LEC = function(l){ return (ES ? "leccion-" : "lesson-") + l + ".html"; };
function fechaHoy(){
  var d = new Date(), m = ES ? ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
                            : ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
  return ES ? d.getDate() + " de " + m[d.getMonth()] + " de " + d.getFullYear() : m[d.getMonth()] + " " + d.getDate() + ", " + d.getFullYear();
}
function pinta(){
  var c = $("preguntas"); c.innerHTML = "";
  PREG.forEach(function(q, i){
    q.orden = baraja(q.ops.map(function(_, j){ return j; })); q.elegida = null;
    var d = document.createElement("fieldset"); d.className = "pregunta-c"; d.id = "p-" + (i + 1);
    d.innerHTML = "<legend><span class=\"num\" aria-hidden=\"true\">" + (i + 1) + "</span> <span class=\"sr-only\">" + T("Question ", "Pregunta ") + (i + 1) + T(" of 30. ", " de 30. ") + "</span>" + q.en + "</legend>";
    var o = document.createElement("div"); o.className = "opciones";
    q.orden.forEach(function(j){
      var b = document.createElement("button"); b.type = "button"; b.className = "opcion"; b.setAttribute("aria-pressed", "false"); b.innerHTML = q.ops[j];
      b.addEventListener("click", function(){
        if (corregida) return;
        q.elegida = j;
        [].forEach.call(o.children, function(x){ x.setAttribute("aria-pressed", "false"); x.classList.remove("elegida"); });
        b.setAttribute("aria-pressed", "true"); b.classList.add("elegida"); cuenta();
      });
      o.appendChild(b);
    });
    d.appendChild(o);
    var fb = document.createElement("div"); fb.className = "fb"; fb.setAttribute("role", "status"); d.appendChild(fb);
    c.appendChild(d);
  });
  cuenta();
}
function cuenta(){ var n = PREG.filter(function(q){ return q.elegida !== null; }).length; $("contador").textContent = T("Answered: ", "Respondidas: ") + n + T(" of 30", " de 30"); }
function comprueba(){
  var sin = PREG.filter(function(q){ return q.elegida === null; }).length;
  if (sin && !$("b-comprobar").dataset.aviso){ $("b-comprobar").dataset.aviso = "1"; $("aviso").className = "caja-aviso visible"; $("aviso").innerHTML = T("You have " + sin + " questions with no answer. A blank answer counts as wrong. Press the button again to check anyway.", "Le quedan " + sin + " preguntas sin responder. Una pregunta en blanco cuenta como incorrecta. Pulse el botón otra vez para revisar de todos modos."); return; }
  $("aviso").className = "caja-aviso"; $("aviso").textContent = "";
  corregida = true;
  var ok = 0, por = TEMAS.map(function(){ return {c: 0, t: 0, mal: []}; });
  var fs = $("preguntas").querySelectorAll("fieldset");
  PREG.forEach(function(q, i){
    var bs = fs[i].querySelectorAll(".opcion"), fb = fs[i].querySelector(".fb"), bien = q.elegida === q.ok, m = por[q.tema - 1];
    m.t++; if (bien){ ok++; m.c++; } else if (m.mal.indexOf(q.lec) < 0) m.mal.push(q.lec);
    q.orden.forEach(function(j, k){ bs[k].disabled = true; if (j === q.ok) bs[k].classList.add("correcta"); if (j === q.elegida && !bien) bs[k].classList.add("incorrecta"); });
    fb.className = "fb " + (bien ? "bien" : "mal");
    fb.innerHTML = "<strong>" + (bien ? T("Correct.", "Correcto.") : (q.elegida === null ? T("Not answered.", "Sin responder.") : T("Not correct.", "Incorrecto.")) + T(" The right answer is ", " La respuesta correcta es ") + q.ops[q.ok] + ".") + "</strong> " + q.ex +
      (bien ? "" : ' <a href="' + LEC(q.lec) + '">' + T("Lesson ", "Lección ") + q.lec.replace("-", ".") + "</a>");
  });
  var pct = Math.round(ok / 30 * 100), r = $("resultado");
  r.className = "resultado " + (ok >= APRUEBA ? "aprob" : "repro");
  r.innerHTML = T("Score: ", "Resultado: ") + "<strong>" + ok + T(" of 30", " de 30") + "</strong> (" + pct + " %). " +
    (ok >= APRUEBA ? T("You passed the Level 4 final check. Together with your project, you have finished Level 4: you are ready for the GED Mathematical Reasoning test.", "Aprobó la evaluación final del Nivel 4. Junto con su proyecto, ha terminado el Nivel 4: está listo para el GED Mathematical Reasoning.")
                   : T("You need 21 right answers (70 %). Review the lessons marked in the report and try again.", "Hacen falta 21 aciertos (70 %). Repase las lecciones señaladas en el informe e inténtelo de nuevo."));
  $("informe-cuerpo").innerHTML = TEMAS.map(function(nom, k){
    var m = por[k], p = Math.round(m.c / m.t * 100), j = m.c === m.t ? T("Mastered", "Dominado") : (p >= 50 ? T("Getting there", "En desarrollo") : T("Needs review", "Requiere repaso"));
    return '<tr><th scope="row">' + T("Topic ", "Tema ") + (k + 1) + " · " + nom + "</th><td>" + m.c + T(" of ", " de ") + m.t + "</td><td>" + p + " %</td><td>" + j +
      (m.mal.length ? " · " + T("Review: ", "Repase: ") + m.mal.map(function(l){ return '<a href="' + LEC(l) + '">' + T("Lesson ", "Lección ") + l.replace("-", ".") + "</a>"; }).join(", ") : "") + "</td></tr>";
  }).join("");
  $("informe").hidden = false; $("b-comprobar").hidden = true; $("b-nueva").hidden = false; $("b-imprimir").hidden = false;
  $("nombre-imp").textContent = $("nombre").value.trim() ? T("Student: ", "Estudiante: ") + $("nombre").value.trim() + " · " + fechaHoy() : fechaHoy();
  r.focus();
}
function nueva(){
  corregida = false; delete $("b-comprobar").dataset.aviso; $("resultado").className = "resultado"; $("resultado").textContent = "";
  $("informe").hidden = true; $("b-comprobar").hidden = false; $("b-nueva").hidden = true; $("b-imprimir").hidden = true;
  pinta(); window.scrollTo({top: $("preguntas").offsetTop - 20, behavior: "smooth"});
}
$("fecha").textContent = fechaHoy();
$("b-comprobar").addEventListener("click", comprueba);
$("b-nueva").addEventListener("click", nueva);
$("b-imprimir").addEventListener("click", function(){ window.print(); });
pinta();
'''

ESTILO = """
  [hidden]{display:none !important;}
  fieldset.pregunta-c{border:2px solid var(--tema-bg2);border-radius:12px;padding:14px 18px;margin:16px 0;background:#fff;}
  fieldset.pregunta-c legend{font-weight:700;color:var(--tema-d);padding:0 6px;font-size:17px;}
  fieldset.pregunta-c legend .num{display:inline-flex;width:28px;height:28px;font-size:14px;margin-right:4px;vertical-align:middle;}
  .opciones{display:flex;flex-wrap:wrap;gap:10px;margin-top:8px;}
  .opcion{font-size:18px;min-width:90px;}
  .opcion.elegida{border-color:var(--tema);background:var(--tema-bg);font-weight:700;}
  .frac{display:inline-flex;flex-direction:column;vertical-align:middle;text-align:center;line-height:1.1;font-size:.9em;}
  .frac span:first-child{border-bottom:2px solid currentColor;padding:0 3px;}
  .resultado{font-size:18px;margin:16px 0;padding:14px 18px;border-radius:10px;}
  .resultado:empty{display:none;}
  .resultado.aprob{background:var(--ok-bg);border-left:6px solid var(--ok);}
  .resultado.repro{background:#fff8e1;border-left:6px solid #f9a825;}
  .datos-est{display:flex;flex-wrap:wrap;gap:16px;align-items:flex-end;}
  #contador{font-weight:700;color:var(--tema-d);}
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
    lang = B.L
    archivo = "math/level-4/final-check-level-4.html" if lang == "en" else "es/matematicas/nivel-4/evaluacion-final-nivel-4.html"
    otro = "/es/matematicas/nivel-4/evaluacion-final-nivel-4.html" if lang == "en" else "/math/level-4/final-check-level-4.html"
    datos = [{"tema": a, "lec": b, "en": c, "ops": d, "ok": k, "ex": x} for a, b, c, d, k, x in preguntas()]
    temas = [t(*x) for x in TEMAS]
    pre = "../" if lang == "en" else "/math/"
    html = f'''<!DOCTYPE html>
<!-- LearnGED · {t("Level 4 · Final check — built by tools/build_n4_final.py", "Nivel 4 · Evaluación final — construida con tools/build_n4_final.py")}
     José M. Fernández · CC BY-NC-SA 4.0 -->
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{t("Level 4 final check · LearnGED", "Evaluación final del Nivel 4 · LearnGED")}</title>
<meta name="license" content="CC BY-NC-SA 4.0"><link rel="license" href="https://creativecommons.org/licenses/by-nc-sa/4.0/">
<link rel="alternate" hreflang="{"es" if lang == "en" else "en"}" href="{otro}">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="{pre}practice.css">
<style>
{ESTILO}
</style>
</head>
<body>
<nav class="lg-bar" aria-label="LearnGED"><a class="lg-logo" href="{"/" if lang == "en" else "/es/"}"><img src="/img/learnged-logo-horizontal.svg" alt="{t("LearnGED home", "Inicio de LearnGED")}" height="34"></a><a class="lg-link" href="{t("lesson-8-3", "leccion-8-3")}.html">{t("← Back to Lesson 8.3", "← Volver a la Lección 8.3")}</a></nav>
<a class="saltar" href="#preguntas">{t("Skip to the questions", "Saltar a las preguntas")}</a>
<div class="contenedor">
  <header class="principal">
    <div class="ruta">{t("Level 4 · Topic 8 · Lesson 8.3", "Nivel 4 · Tema 8 · Lección 8.3")}</div>
    <h1>{t("Level 4 final check", "Evaluación final del Nivel 4")}</h1>
    <div class="meta">{t("30 questions that cover the eight topics of the level", "30 preguntas que abarcan los ocho temas del nivel")}</div>
  </header>

  <section class="panel no-imp">
    <h2>{t("How it works", "Cómo funciona")}</h2>
    <p>{t("Take it in one sitting, with no interruptions and without looking at the lessons: that way you will really know whether you are ready for the GED test. Answer the 30 questions, then press <strong>Check my answers</strong>. You will see why each answer is right and a report by topic with the lessons to review. You pass with <strong>21 right answers (70 %)</strong>. You may use the calculator and the GED formula sheet, as on the real test.", "Hágala de una sentada, sin interrupciones y sin consultar las lecciones: así sabrá de verdad si está listo para el examen GED. Responda las 30 preguntas y pulse <strong>Revisar mis respuestas</strong>. Verá por qué cada respuesta es la correcta y un informe por tema con las lecciones que conviene repasar. Se aprueba con <strong>21 aciertos (70 %)</strong>. Puede usar la calculadora y la hoja de fórmulas del GED, como en el examen real.")}</p>
    <div class="datos-est">
      <div class="campo"><label for="nombre">{t("Your name (for the printed report)", "Su nombre (para el informe impreso)")}</label><input type="text" id="nombre" autocomplete="name" style="min-width:260px"></div>
      <p>{t("Date:", "Fecha:")} <span id="fecha"></span></p>
    </div>
  </section>
  <p class="solo-imp" id="nombre-imp"></p>

  <div id="preguntas"></div>

  <p id="contador" aria-live="polite"></p>
  <p class="caja-aviso" id="aviso" role="alert"></p>
  <div class="resultado" id="resultado" tabindex="-1" aria-live="polite"></div>
  <div class="fila-btn">
    <button type="button" class="btn" id="b-comprobar">{t("Check my answers", "Revisar mis respuestas")}</button>
    <button type="button" class="btn" id="b-nueva" hidden>{t("Try again", "Intentarlo de nuevo")}</button>
    <button type="button" class="btn-sec" id="b-imprimir" hidden>{t("Print the report", "Imprimir el informe")}</button>
  </div>

  <section id="informe" hidden>
    <h2>{t("Report by topic", "Informe por tema")}</h2>
    <p>{t("For each topic, the lessons of the questions you missed. Go back to them and to their practice pages before you take the check again.", "En cada tema aparecen las lecciones de las preguntas que falló. Vuelva a ellas y a sus prácticas antes de repetir la evaluación.")}</p>
    <div class="tabla-scroll" role="region" tabindex="0" aria-label="{t("Report by topic (table you can scroll sideways)", "Informe por tema (tabla desplazable horizontalmente)")}">
    <table class="informe"><caption class="cap-oculto">{t("Right answers, percent, and level for each topic", "Aciertos, porcentaje y nivel de cada tema")}</caption>
    <thead><tr><th scope="col">{t("Topic", "Tema")}</th><th scope="col">{t("Right", "Aciertos")}</th><th scope="col">{t("Percent", "Porcentaje")}</th><th scope="col">{t("Level", "Nivel")}</th></tr></thead>
    <tbody id="informe-cuerpo"></tbody></table></div>
    <p class="no-imp">{t("Your other piece of the level is the", "La otra pieza del nivel es el")} <a href="{t("project-level-4", "proyecto-nivel-4")}.html">{t("final project «My mathematical model»", "proyecto final «Mi modelo matemático»")}</a>.</p>
  </section>

  <footer class="pie">
    <p><strong>{t("Level 4 · Final check · LearnGED", "Nivel 4 · Evaluación final · LearnGED")}</strong><br>
    José M. Fernández, ABE/ASE Math Master Teacher, Harry S. Truman College — City Colleges of Chicago.</p>
    <p>{t("This work is licensed under", "Esta obra está bajo la licencia")} <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/" target="_blank" rel="noopener noreferrer">Creative Commons BY-NC-SA 4.0</a>.</p>
    <p class="tm">{t("GED® is a registered trademark of the American Council on Education (ACE) and administered exclusively by GED Testing Service LLC under license. LearnGED is not affiliated with, endorsed by, or approved by ACE or GED Testing Service.", "GED® es una marca registrada del American Council on Education (ACE), administrada exclusivamente por GED Testing Service LLC bajo licencia. LearnGED no está afiliado a ACE ni a GED Testing Service, ni cuenta con su respaldo o aprobación.")}</p>
  </footer>
</div>
<script src="{pre}practice.js"></script>
<script>
window.PREG = {json.dumps(datos, ensure_ascii=False)};
window.TEMAS = {json.dumps(temas, ensure_ascii=False)};
{LOGICA.strip()}
</script>
</body>
</html>
'''
    open(os.path.join(ROOT, archivo), "w", encoding="utf-8").write(html)
    print("ok", archivo)

if __name__ == "__main__":
    for L in ("en", "es"):
        B.L = L
        pagina()
    B.L = "en"
