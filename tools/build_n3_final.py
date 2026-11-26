"""Level 3 · Final check (25 questions that cover the eight topics) — builds the page in English and in Spanish.
Imported from GEDparaHispanos (clase_mate3/leccion_8-3.html, «Evaluación final sumativa del Nivel 3»):
the 25 questions A–Y, now with US units, an explanation for each one, and a report by topic with links to the lessons.
One change from the source: question H (x + 4 = 10, the third one-step equation) became a radicals question,
so that every topic of the level, Topic 3 included, is on the final check.
  math/level-3/final-check-level-3.html · es/matematicas/nivel-3/evaluacion-final-nivel-3.html"""
import os, json
import bilingue as B
from bilingue import t

B.NIVEL = 3
ROOT = B.ROOT

def e(base, exp, sr_en, sr_es):
    """A power, shown with a superscript and read aloud in words."""
    return f'<span aria-hidden="true">{base}<sup>{exp}</sup></span><span class="sr-only">{t(sr_en, sr_es)}</span>'

def sci(a, n):
    return f'<span aria-hidden="true">{a} × 10<sup>{n}</sup></span><span class="sr-only">{a} {t("times 10 to the", "por 10 a la")} {n}</span>'

def raiz(c, n):
    return f'<span aria-hidden="true">{c}√{n}</span><span class="sr-only">{c} {t("times the square root of", "por la raíz cuadrada de")} {n}</span>' if c else f'<span aria-hidden="true">√{n}</span><span class="sr-only">{t("the square root of", "la raíz cuadrada de")} {n}</span>'

def fr(a, b):
    return f'<span class="frac" aria-hidden="true"><span>{a}</span><span>{b}</span></span><span class="sr-only">{a} {t("over", "sobre")} {b}</span>'

def preguntas():
    """(topic, lesson, question, options, index of the right one, explanation)"""
    x = lambda n, en, es: e("x", n, "x to the " + en, "x a la " + es)
    return [
     (1, "1-1", t("A. Simplify: ", "A. Simplifique: ") + x(4, "4th", "4") + " · " + x(2, "2nd", "2"), [x(8, "8th", "8"), x(2, "2nd", "2"), x(6, "6th", "6"), x(16, "16th", "16")], 2,
      t("Same base, so the exponents are added: 4 + 2 = 6. Multiplying them (8) is the usual mistake.", "Misma base: los exponentes se suman, 4 + 2 = 6. Multiplicarlos (8) es el error de siempre.")),
     (1, "1-1", t("B. Simplify: ", "B. Simplifique: ") + "(" + x(3, "3rd", "3") + ")<sup aria-hidden=\"true\">2</sup><span class=\"sr-only\">" + t(" squared", " al cuadrado") + "</span>", [x(6, "6th", "6"), x(5, "5th", "5"), x(9, "9th", "9"), "x"], 0,
      t("A power of a power: the exponents are multiplied, 3 · 2 = 6.", "Potencia de una potencia: los exponentes se multiplican, 3 · 2 = 6.")),
     (1, "1-2", t("C. What is the value of ", "C. ¿Cuánto vale ") + x(0, "zero", "cero") + t(" (when x is not 0)?", " (con x distinto de 0)?"), ["0", "x", t("It is not defined", "No está definido"), "1"], 3,
      t("Any number other than zero to the zero power is 1: it is x ÷ x.", "Toda cantidad distinta de cero elevada a la cero vale 1: es x ÷ x.")),
     (2, "2-1", t("D. Write 5,000 in scientific notation.", "D. Escriba 5,000 en notación científica."), [sci(5, 4), sci(5, 3), sci(50, 2), sci("0.5", 4)], 1,
      t("The decimal point moves 3 places to the left to leave a number from 1 to 10: 5 × 10³. 50 × 10² has the right value but is not scientific notation.", "El punto decimal se corre 3 lugares a la izquierda para dejar un número entre 1 y 10: 5 × 10³. 50 × 10² vale lo mismo, pero no está en notación científica.")),
     (2, "2-1", t("E. What is ", "E. ¿Cuánto es ") + sci(3, 2) + "?", ["30", "3,000", "300", "32"], 2,
      t("10² = 100, and 3 × 100 = 300: the point moves 2 places to the right.", "10² = 100 y 3 × 100 = 300: el punto se corre 2 lugares a la derecha.")),
     (4, "4-2", t("F. Solve: 3x = 21.", "F. Resuelva: 3x = 21."), ["x = 7", "x = 18", "x = 24", "x = 63"], 0,
      t("Divide both sides by 3: x = 21 ÷ 3 = 7.", "Se dividen los dos lados entre 3: x = 21 ÷ 3 = 7.")),
     (4, "4-2", t("G. Solve: 2x − 5 = 9.", "G. Resuelva: 2x − 5 = 9."), ["x = 2", "x = −7", "x = 28", "x = 7"], 3,
      t("Add 5 to both sides (2x = 14), then divide by 2: x = 7. Check: 2 · 7 − 5 = 9.", "Se suma 5 a los dos lados (2x = 14) y se divide entre 2: x = 7. Comprobación: 2 · 7 − 5 = 9.")),
     (3, "3-1", t("H. Simplify: ", "H. Simplifique: ") + raiz(None, 50), [raiz(25, 2), raiz(5, 2), raiz(2, 5), raiz(5, 10)], 1,
      t("50 = 25 · 2, and 25 is a perfect square: √50 = √25 · √2 = 5√2.", "50 = 25 · 2 y 25 es un cuadrado perfecto: √50 = √25 · √2 = 5√2.")),
     (5, "5-1", t("I. Solve the inequality: x + 3 > 8.", "I. Resuelva la inecuación: x + 3 > 8."), ["x < 5", "x > 11", "x < 11", "x > 5"], 3,
      t("Subtract 3 from both sides: x > 5. The sign does not flip, because you did not multiply or divide by a negative number.", "Se resta 3 a los dos lados: x > 5. El signo no se invierte, porque no se multiplicó ni dividió entre un número negativo.")),
     (5, "5-3", t("J. Solve d = rt for t.", "J. Despeje t en d = rt."), ["t = dr", "t = " + fr("d", "r"), "t = " + fr("r", "d"), "t = d − r"], 1,
      t("r multiplies t, so divide both sides by r: t = d ÷ r. (Time = distance ÷ rate.)", "r multiplica a t, así que se dividen los dos lados entre r: t = d ÷ r. (Tiempo = distancia ÷ velocidad.)")),
     (6, "6-2", t("K. A right triangle has legs of 3 inches and 4 inches. How long is the hypotenuse?", "K. Un triángulo rectángulo tiene catetos de 3 pulgadas y 4 pulgadas. ¿Cuánto mide la hipotenusa?"), [t("5 inches", "5 pulgadas"), t("7 inches", "7 pulgadas"), t("12 inches", "12 pulgadas"), t("25 inches", "25 pulgadas")], 0,
      t("3² + 4² = 9 + 16 = 25, and √25 = 5. Adding the legs (7) is not the theorem; 25 is c², not c.", "3² + 4² = 9 + 16 = 25 y √25 = 5. Sumar los catetos (7) no es el teorema; 25 es c², no c.")),
     (6, "6-3", t("L. The triangles 2-3-4 and 4-6-x are similar. What is x?", "L. Los triángulos 2-3-4 y 4-6-x son semejantes. ¿Cuánto vale x?"), ["5", "12", "8", "6"], 2,
      t("Each side was multiplied by 2 (2 → 4, 3 → 6), so x = 4 · 2 = 8.", "Cada lado se multiplicó por 2 (2 → 4, 3 → 6), así que x = 4 · 2 = 8.")),
     (7, "7-1", t("M. What is the volume of a box that is 2 feet by 3 feet by 4 feet?", "M. ¿Cuál es el volumen de una caja de 2 pies por 3 pies por 4 pies?"), [t("24 cubic feet", "24 pies cúbicos"), t("9 cubic feet", "9 pies cúbicos"), t("48 cubic feet", "48 pies cúbicos"), t("12 cubic feet", "12 pies cúbicos")], 0,
      t("V = length × width × height = 2 · 3 · 4 = 24 cubic feet. Adding the sides (9) does not give a volume.", "V = largo × ancho × alto = 2 · 3 · 4 = 24 pies cúbicos. Sumar los lados (9) no da un volumen.")),
     (7, "7-1", t("N. What is the volume of a cylinder with a radius of 2 inches and a height of 5 inches? (Use π ≈ 3.14.)", "N. ¿Cuál es el volumen de un cilindro de radio 2 pulgadas y altura 5 pulgadas? (Use π ≈ 3.14.)"), [t("31.4 cubic inches", "31.4 pulgadas cúbicas"), t("20 cubic inches", "20 pulgadas cúbicas"), t("62.8 cubic inches", "62.8 pulgadas cúbicas"), t("125.6 cubic inches", "125.6 pulgadas cúbicas")], 2,
      t("V = πr²h = 3.14 · 2² · 5 = 3.14 · 4 · 5 = 62.8 cubic inches. 31.4 forgets to square the radius.", "V = πr²h = 3.14 · 2² · 5 = 3.14 · 4 · 5 = 62.8 pulgadas cúbicas. 31.4 olvida elevar el radio al cuadrado.")),
     (6, "6-1", t("O. Two supplementary angles add up to…", "O. Dos ángulos suplementarios suman…"), ["90°", "180°", "360°", "45°"], 1,
      t("Supplementary angles add up to 180° (a straight line). Complementary angles add up to 90°.", "Los suplementarios suman 180° (una línea recta). Los complementarios suman 90°.")),
     (7, "7-2", t("P. For the data 2, 4, 6, 8, 10, the median is…", "P. Para los datos 2, 4, 6, 8, 10, la mediana es…"), ["5", "8", "4", "6"], 3,
      t("The data are already in order; the middle value of the five is 6.", "Los datos ya están ordenados; el valor del centro de los cinco es 6.")),
     (7, "7-2", t("Q. If Q1 = 20 and Q3 = 50, the IQR is…", "Q. Si Q1 = 20 y Q3 = 50, el IQR es…"), ["70", "30", "50", "20"], 1,
      t("IQR = Q3 − Q1 = 50 − 20 = 30.", "IQR = Q3 − Q1 = 50 − 20 = 30.")),
     (7, "7-3", t("R. In a histogram, the bars are…", "R. En un histograma, las barras son…"), [t("separated by gaps", "separadas"), t("round", "circulares"), t("side by side, with no gaps", "contiguas, sin espacios"), t("always the same height", "siempre de la misma altura")], 2,
      t("The intervals follow one after another on the number line, so the bars touch. A bar graph of categories is the one with gaps.", "Los intervalos se siguen uno tras otro en la recta numérica, así que las barras se tocan. La gráfica de barras de categorías es la que lleva espacios.")),
     (7, "7-2", t("S. In a box plot, the line inside the box shows…", "S. En un diagrama de caja, la línea dentro de la caja representa…"), [t("the mean", "la media"), t("the maximum", "el máximo"), t("the IQR", "el IQR"), t("the median", "la mediana")], 3,
      t("The line inside the box is the median (Q2). The box plot does not show the mean.", "La línea dentro de la caja es la mediana (Q2). El diagrama de caja no muestra la media.")),
     (7, "7-2", t("T. For the data 3, 5, 7, 9, the mean is…", "T. Para los datos 3, 5, 7, 9, la media es…"), ["6", "7", "5", "24"], 0,
      t("Add them and divide by how many there are: (3 + 5 + 7 + 9) ÷ 4 = 24 ÷ 4 = 6.", "Se suman y se divide entre la cantidad: (3 + 5 + 7 + 9) ÷ 4 = 24 ÷ 4 = 6.")),
     (8, "8-1", t("U. What is 4! ?", "U. ¿Cuánto es 4! ?"), ["12", "4", "16", "24"], 3,
      t("4! = 4 · 3 · 2 · 1 = 24.", "4! = 4 · 3 · 2 · 1 = 24.")),
     (8, "8-1", t("V. What is C(5, 2)?", "V. ¿Cuánto es C(5, 2)?"), ["10", "20", "25", "7"], 0,
      t("C(5, 2) = (5 · 4) ÷ (2 · 1) = 20 ÷ 2 = 10. 20 is P(5, 2), where order matters.", "C(5, 2) = (5 · 4) ÷ (2 · 1) = 20 ÷ 2 = 10. 20 es P(5, 2), donde el orden sí importa.")),
     (8, "8-1", t("W. Choosing a committee of 3 people out of 8 (order does not matter) is a…", "W. Elegir un comité de 3 personas entre 8 (sin importar el orden) es una…"), [t("permutation", "permutación"), t("combination", "combinación"), t("factorial", "factorial"), t("counting principle", "principio del conteo")], 1,
      t("If the order does not matter, it is a combination. If each person had a different job, it would be a permutation.", "Si el orden no importa, es una combinación. Si cada persona tuviera un cargo distinto, sería una permutación.")),
     (8, "8-2", t("X. You toss a coin 2 times. P(heads, then heads) is…", "X. Se lanza una moneda 2 veces. P(cara y luego cara) es…"), [fr(1, 2), fr(3, 4), fr(1, 4), "1"], 2,
      t("The tosses are independent, so multiply: ½ · ½ = ¼.", "Los lanzamientos son independientes, así que se multiplica: ½ · ½ = ¼.")),
     (8, "8-2", t("Y. A bag has 3 red marbles and 2 blue ones (5 in all). P(red on one draw) is…", "Y. Una bolsa tiene 3 canicas rojas y 2 azules (5 en total). P(roja en una extracción) es…"), [fr(2, 5), fr(3, 2), fr(5, 3), fr(3, 5)], 3,
      t("Favorable ÷ total = 3 ÷ 5. A probability is never greater than 1, so 3/2 and 5/3 are impossible.", "Favorables ÷ total = 3 ÷ 5. Una probabilidad nunca pasa de 1, así que 3/2 y 5/3 son imposibles.")),
    ]

TEMAS = [("Rules of exponents", "Reglas de los exponentes"), ("Scientific notation", "Notación científica"), ("Radicals and the real numbers", "Radicales y números reales"),
         ("Linear algebra", "Álgebra lineal"), ("Inequalities and formulas", "Inecuaciones y fórmulas"), ("Geometry: angles, the Pythagorean theorem, and similarity", "Geometría: ángulos, teorema de Pitágoras y semejanza"),
         ("Volume and data analysis", "Volumen y análisis de datos"), ("Counting and probability", "Combinatoria y probabilidad")]

LOGICA = r'''
function T(en, es){ return ES ? es : en; }
var PREG = window.PREG, TEMAS = window.TEMAS, APRUEBA = 18, corregida = false;
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
    d.innerHTML = "<legend><span class=\"num\" aria-hidden=\"true\">" + (i + 1) + "</span> <span class=\"sr-only\">" + T("Question ", "Pregunta ") + (i + 1) + T(" of 25. ", " de 25. ") + "</span>" + q.en + "</legend>";
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
function cuenta(){ var n = PREG.filter(function(q){ return q.elegida !== null; }).length; $("contador").textContent = T("Answered: ", "Respondidas: ") + n + T(" of 25", " de 25"); }
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
  var pct = Math.round(ok / 25 * 100), r = $("resultado");
  r.className = "resultado " + (ok >= APRUEBA ? "aprob" : "repro");
  r.innerHTML = T("Score: ", "Resultado: ") + "<strong>" + ok + T(" of 25", " de 25") + "</strong> (" + pct + " %). " +
    (ok >= APRUEBA ? T("You passed the Level 3 final check. Together with your project, you have finished Level 3.", "Aprobó la evaluación final del Nivel 3. Junto con su proyecto, ha terminado el Nivel 3.")
                   : T("You need 18 right answers (70 %). Review the lessons marked in the report and try again.", "Hacen falta 18 aciertos (70 %). Repase las lecciones señaladas en el informe e inténtelo de nuevo."));
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
    archivo = "math/level-3/final-check-level-3.html" if lang == "en" else "es/matematicas/nivel-3/evaluacion-final-nivel-3.html"
    otro = "/es/matematicas/nivel-3/evaluacion-final-nivel-3.html" if lang == "en" else "/math/level-3/final-check-level-3.html"
    datos = [{"tema": a, "lec": b, "en": c, "ops": d, "ok": k, "ex": x} for a, b, c, d, k, x in preguntas()]
    temas = [t(*x) for x in TEMAS]
    pre = "../" if lang == "en" else "/math/"
    html = f'''<!DOCTYPE html>
<!-- LearnGED · {t("Level 3 · Final check — built by tools/build_n3_final.py", "Nivel 3 · Evaluación final — construida con tools/build_n3_final.py")}
     José M. Fernández · CC BY-NC-SA 4.0 -->
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{t("Level 3 final check · LearnGED", "Evaluación final del Nivel 3 · LearnGED")}</title>
<meta name="license" content="CC BY-NC-SA 4.0"><link rel="license" href="https://creativecommons.org/licenses/by-nc-sa/4.0/">
<link rel="alternate" hreflang="{"es" if lang == "en" else "en"}" href="{otro}">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="{pre}practice.css">
<style>
{ESTILO}
</style>
</head>
<body>
<nav class="lg-bar" aria-label="LearnGED"><a class="lg-logo" href="/"><img src="/img/learnged-logo-horizontal.svg" alt="{t("LearnGED home", "Inicio de LearnGED")}" height="34"></a><a class="lg-link" href="{t("lesson-8-3", "leccion-8-3")}.html">{t("← Back to Lesson 8.3", "← Volver a la Lección 8.3")}</a></nav>
<a class="saltar" href="#preguntas">{t("Skip to the questions", "Saltar a las preguntas")}</a>
<div class="contenedor">
  <header class="principal">
    <div class="ruta">{t("Level 3 · Topic 8 · Lesson 8.3", "Nivel 3 · Tema 8 · Lección 8.3")}</div>
    <h1>{t("Level 3 final check", "Evaluación final del Nivel 3")}</h1>
    <div class="meta">{t("25 questions that cover the eight topics of the level", "25 preguntas que abarcan los ocho temas del nivel")}</div>
  </header>

  <section class="panel no-imp">
    <h2>{t("How it works", "Cómo funciona")}</h2>
    <p>{t("Take it in one sitting, with no interruptions and without looking at the lessons: that way you will really know where you stand before Level 4. Answer the 25 questions, then press <strong>Check my answers</strong>. You will see why each answer is right and a report by topic with the lessons to review. You pass with <strong>18 right answers (70 %)</strong>. You may use the calculator and the GED formula sheet, as on the real test.", "Hágala de una sentada, sin interrupciones y sin consultar las lecciones: así sabrá de verdad dónde está parado antes del Nivel 4. Responda las 25 preguntas y pulse <strong>Revisar mis respuestas</strong>. Verá por qué cada respuesta es la correcta y un informe por tema con las lecciones que conviene repasar. Se aprueba con <strong>18 aciertos (70 %)</strong>. Puede usar la calculadora y la hoja de fórmulas del GED, como en el examen real.")}</p>
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
    <p class="no-imp">{t("Your other piece of the level is the", "La otra pieza del nivel es el")} <a href="{t("project-level-3", "proyecto-nivel-3")}.html">{t("final project «My data analysis»", "proyecto final «Mi análisis de datos»")}</a>.</p>
  </section>

  <footer class="pie">
    <p><strong>{t("Level 3 · Final check · LearnGED", "Nivel 3 · Evaluación final · LearnGED")}</strong><br>
    José M. Fernández, ABE/ASE Math Master Teacher, Harry S. Truman College — City Colleges of Chicago.</p>
    <p>{t("This work is licensed under", "Esta obra está bajo la licencia")} <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/" target="_blank" rel="noopener noreferrer">Creative Commons BY-NC-SA 4.0</a>.</p>
    <p class="tm">GED® is a registered trademark of the American Council on Education (ACE) and administered exclusively by GED Testing Service LLC under license. LearnGED is not affiliated with, endorsed by, or approved by ACE or GED Testing Service.</p>
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
