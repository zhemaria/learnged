# -*- coding: utf-8 -*-
"""LearnGED · Artes del lenguaje (español) · Nivel 1 · Lección 8.6 · Evaluación final y camino al GED.
Fuente: clases_leng1/clase_8-6.html (GEDparaHispanos), adaptada al marco de LearnGED.
La página de práctica de esta lección es la evaluación final del Nivel 1: 32 preguntas (4 de cada tema), sorteadas en cada
intento entre las preguntas de los cuestionarios de todas las lecciones (se recogen ejecutando sus builders y se descartan las
que remiten a un texto, una gráfica o un mapa de su lección). Hay que volver a correr este builder cuando cambie un cuestionario.
Datos del GED (tiempos y puntaje para aprobar): GED Testing Service, ged.com. Consultado en noviembre de 2026.
Uso: python3 tools/build_leng1_8_6.py
"""
import os, sys, importlib, json, html
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import leng_es as LE
from leng_es import C

LE.nivel(1)
N = "8-6"
MALO = ["En el cuento", "En el texto", "del texto", "En la gráfica", "la gráfica de", "En el mapa", "Las Flores", "En la tabla", "del autobús", "desafío", "modelo", "En «",
        "Según la", "artículo", "lección", "sección", "data-", "Marta", "Roberto", "abuela", "Ana", "Lucía", "¿Qué hacía", "cuaderno del proyecto", "la rúbrica"]
EXAMENES = [("📖 Razonamiento a través de las Artes del Lenguaje", "Lectura, gramática y un ensayo escrito. Es el área que prepara este curso.", "150 minutos"),
            ("🔢 Razonamiento Matemático", "Números, álgebra, geometría y datos. Se puede usar calculadora en la mayor parte del examen.", "115 minutos"),
            ("🔬 Ciencia", "Ciencias de la vida, física y química, y la Tierra y el espacio. Mucha lectura de experimentos y datos.", "90 minutos"),
            ("🌎 Estudios Sociales", "Educación cívica, historia de los EE. UU., economía y geografía. Muchos mapas, tablas y gráficas.", "70 minutos")]


def leccion():
    P = C.Practicas()
    s1 = f"""<p>Ya tiene su texto, su gráfica y su guion de la Lección 8.5. Ahora toca presentarlo: grábese con el teléfono o preséntelo ante alguien de su casa.</p>
{C.tabla("Los tiempos de su presentación", ["Tiempo", "Qué hacer"],
         [["0:00 – 0:30", "<strong>Apertura:</strong> preséntese, diga el título del proyecto y conecte con quien escucha."],
          ["0:30 – 2:30", "<strong>Desarrollo:</strong> tres ideas (mi historia, dónde estoy, mis metas). Muestre su gráfica aquí."],
          ["2:30 – 3:00", "<strong>Cierre:</strong> un mensaje que se recuerde y un agradecimiento."],
          ["3:00 – 4:00", "<strong>Preguntas:</strong> pida a quien le escucha dos preguntas. Si se graba solo, piense qué le preguntarían y respóndalo en voz alta."]])}
{C.caja("tip", "No busque la grabación perfecta", "<p>Haga una toma completa y mírela. Si quiere, haga una segunda. Lo importante es <strong>terminarla</strong>.</p>")}
{C.tabla("Mírese con ojos de evaluador (de 1 a 5 estrellas)", ["Criterio", "Pregúntese"],
         [["🎤 Claridad", "¿Se entiende lo que digo? ¿Tengo buen volumen y pocas muletillas?"], ["📊 Apoyo visual", "¿Mi gráfica es clara? ¿Apoya lo que digo o solo adorna?"],
          ["💡 Mensaje", "¿Mi presentación deja una idea que alguien recordaría mañana?"]])}
{C.caja("ojo", "Evalúe la presentación, no a la persona", "<p>Sea honesto y amable, como lo sería con un amigo: anote una cosa que hizo bien y una que mejoraría. Presentar ya es un esfuerzo.</p>")}"""

    temas = "".join(f"<li><strong>Tema {k}</strong> · {v}</li>" for k, v in LE.NIVELES[1][1].items())
    s2 = f"""<p>Antes de la evaluación, mire el camino recorrido:</p>
<ol class="sin-num">{temas}</ol>
<p>La <a href="practica-8-6.html"><strong>evaluación final del Nivel 1</strong></a> está en la página de práctica de esta lección:</p>
<ul><li>Tiene <strong>32 preguntas</strong>, cuatro de cada tema, sin límite de tiempo. Las preguntas cambian en cada intento.</li>
<li>Al corregir, verá su puntaje <strong>por tema</strong>: sabrá qué domina y qué necesita repasar.</li>
<li>Cada pregunta que falle trae un enlace a la lección que la explica.</li>
<li>Puede imprimir el resumen (o guardarlo en PDF) y usarlo como guía de estudio. Después, repita la evaluación.</li></ul>
{C.caja("tip", "La meta es el 80 %", "<p>Si acierta <strong>26 preguntas o más</strong>, domina el Nivel 1. Si no, no pasa nada: el resumen le dice exactamente qué repasar. Un error bien estudiado vale más que un acierto por suerte.</p>")}"""

    s3 = f"""<p><strong>GED</strong> son las siglas de <em>General Educational Development</em>. Es una credencial que demuestra las destrezas de una persona graduada de la escuela secundaria (<em>high school</em>) de los EE. UU. Tiene cuatro exámenes independientes, que se pueden tomar en español o en inglés:</p>
{C.tabla("Los cuatro exámenes del GED", ["Examen", "Qué evalúa", "Tiempo"], [list(x) for x in EXAMENES])}
{C.caja("tip", "Datos prácticos", "<p>Los cuatro exámenes se toman por separado y en el orden que usted quiera. Para aprobar cada uno se necesitan <strong>145 puntos de 200</strong>. Al aprobar los cuatro, recibe su credencial. Los precios, las reglas y las fechas cambian según el estado y con el tiempo: consulte siempre la información oficial en <strong>ged.com</strong>.</p>")}
<p class="nota-fina">Fuente de los tiempos y del puntaje: GED Testing Service (ged.com). Consultado en noviembre de 2026.</p>
<h3>Por qué este nivel importa</h3>
<p>El Nivel 1 es el primer escalón hacia el examen de Artes del Lenguaje: aquí construyó la base (leer con comprensión, escribir oraciones y párrafos, leer una gráfica, dar una opinión con razones). En los niveles siguientes lo profundizará hasta llegar al ensayo del examen. Y lo que aprendió en el Tema 6 (mapas, tablas y gráficas) y en el Tema 7 (tipos de texto) le sirve también para Ciencia y Estudios Sociales.</p>
<p><strong>El siguiente paso:</strong> el Nivel 2 de Artes del Lenguaje. ¡Felicidades por llegar hasta aquí!</p>"""

    secciones = [("s1", "Mi presentación final", s1), ("s2", "La evaluación final del Nivel 1", s2), ("s3", "¿Qué es el GED?", s3)]
    tarea = [("Mi presentación.", "Grábese presentando su proyecto (de 3 a 4 minutos) y califíquese con las estrellas de la sección 1."),
             ("La evaluación.", "Haga la evaluación final. Imprima o guarde el resumen."),
             ("Mi plan de repaso.", "Para cada tema por debajo del 75 %, escriba qué lección va a repasar y cuándo. Después, repita la evaluación."),
             ("Mi cuenta GED.", "Si todavía no la tiene, cree su cuenta en ged.com (Lección 8.3) y explore los exámenes de práctica.")]
    quiz = [
        ("¿Cuántos exámenes tiene el GED?", ["Cuatro", "Dos", "Ocho"], 0, {1: "Son cuatro materias.", 2: "No."}, "<strong>Cuatro.</strong>"),
        ("¿Cuánto dura el examen de Artes del Lenguaje?", ["150 minutos", "70 minutos", "30 minutos"], 0, {1: "Ese es Estudios Sociales.", 2: "No."}, "<strong>150 minutos.</strong>"),
        ("¿Cuántos puntos se necesitan para aprobar cada examen?", ["145 de 200", "100 de 200", "200 de 200"], 0, {1: "Es más.", 2: "No hace falta la perfección."}, "<strong>145 de 200.</strong>"),
        ("¿Se pueden tomar los exámenes por separado?", ["Sí, en el orden que quiera", "No, todos el mismo día"], 0, {}, "<strong>Sí.</strong>"),
        ("¿En qué idiomas se puede tomar el GED?", ["En español o en inglés", "Solo en inglés"], 0, {}, "<strong>En español o en inglés.</strong>"),
        ("¿Dónde se consulta la información oficial del GED?", ["En ged.com", "En cualquier anuncio de internet"], 0, {}, "En <strong>ged.com</strong>."),
        ("¿Cuántas preguntas tiene la evaluación final del Nivel 1?", ["32, cuatro de cada tema", "10"], 0, {}, "<strong>32.</strong>"),
        ("¿Qué porcentaje indica que domina el Nivel 1?", ["80 % (26 preguntas o más)", "50 %"], 0, {}, "<strong>80 %.</strong>"),
        ("¿Qué conviene hacer con los temas que salgan bajos?", ["Repasar sus lecciones y repetir la evaluación", "Olvidarlos"], 0, {}, "<strong>Repasar y repetir.</strong>"),
        ("¿Qué se evalúa en su presentación, según la sección 1?", ["La presentación, no a la persona", "La persona, no la presentación"], 0, {}, "La <strong>presentación</strong>."),
    ]
    filas = [
        ("Presentación", "Me grabé, me califiqué y anoté qué mejorar.", "Me grabé, pero no me califiqué.", "No me grabé todavía (<a href=\"#s1\">repase la sección 1</a>)."),
        ("Evaluación", "Llegué al 80 % o hice mi plan de repaso.", "Hice la evaluación, pero sin plan.", "No la he hecho (<a href=\"#s2\">vea la sección 2</a>)."),
        ("El GED", "Sé cuáles son los cuatro exámenes y dónde informarme.", "Conozco algunos datos.", "No lo tengo claro (<a href=\"#s3\">repase la sección 3</a>)."),
    ]
    cierre = "<p>¡Terminó el Nivel 1 de Artes del Lenguaje! Siga con el Nivel 2, a su ritmo.</p>"
    glosario = [("GED", "General Educational Development: credencial equivalente a la secundaria de los EE. UU."), ("Credencial", "Documento que certifica lo que alguien sabe hacer."),
                ("Autoevaluación", "Calificar el propio trabajo con criterios claros.")]
    conexion = ("<p>Cuando empezó este nivel, quizá se preguntaba qué es el GED y si podría prepararlo. Hoy va a presentar un proyecto que reúne todo lo aprendido, hacer una evaluación de los ocho temas y ver con claridad el camino que sigue.</p>"
                "<p><strong>Lo que necesita:</strong> su proyecto de la Lección 8.5, un teléfono para grabarse y unos 40 minutos tranquilos para la evaluación.</p>")
    estd = LE.estandares(["R.2.1"], base=["W.1"], fund=["SL.4"])
    return C.pagina_leccion(N, LE.titulo(N), "Mirar lo recorrido y el camino que sigue.", ["Evaluación final", "Camino al GED"],
                            ["<strong>Presentar</strong> el proyecto final y evaluarse.", "<strong>Medir</strong> lo aprendido en los ocho temas con la evaluación final.",
                             "<strong>Conocer</strong> los cuatro exámenes del GED y dónde informarse."],
                            estd, conexion, secciones, tarea, quiz, filas, cierre, (None, "Siguiente: Nivel 2 de Artes del Lenguaje (en preparación)."), glosario, P)


def banco():
    """Recoge las preguntas de los cuestionarios de todas las lecciones del Nivel 1."""
    cap, orig = [], LE._quiz_original

    def captura(items):
        cap.extend(items)
        return orig(items)
    salida = []
    for t in range(1, 9):
        for n in range(1, 7):
            try:
                m = sys.modules[__name__] if (t, n) == (8, 6) else importlib.import_module(f"build_leng1_{t}_{n}")
            except ModuleNotFoundError:
                continue
            LE.nivel(1)
            cap.clear()
            antes = C.quiz_html
            C.quiz_html = captura
            try:
                m.leccion()
            finally:
                C.quiz_html = antes
            for preg, ops, ok, pistas, sol in cap:
                if any(x in preg for x in MALO):
                    continue
                salida.append({"t": t, "l": f"{t}-{n}", "q": preg, "o": list(ops), "c": ok, "s": sol})
    LE.nivel(1)
    return salida


def practica():
    B = banco()
    temas = {str(k): v for k, v in LE.NIVELES[1][1].items()}
    titulos = {f"{t}-{n}": LE.titulo(f"{t}-{n}") for t in range(1, 9) for n in range(1, 7) if f"{t}-{n}" in LE.LECCIONES[1]}
    cont = """<div id="evf" class="evaluacion">
<p>Responda las 32 preguntas y pulse <strong>Corregir</strong> al final. Las preguntas cambian en cada intento.</p>
<ol id="evf-lista" class="evf-lista"></ol>
<p><button type="button" class="btn" id="evf-corregir">✅ Corregir</button> <button type="button" class="btn-sec" id="evf-otra">🔄 Otra evaluación</button> <button type="button" class="btn-sec" id="evf-imp" hidden>🖨️ Imprimir o guardar en PDF</button></p>
<div id="evf-res" aria-live="polite"></div></div>"""
    js = (f"var EVB = {json.dumps(B, ensure_ascii=False)};\nvar EVT = {json.dumps(temas, ensure_ascii=False)};\nvar EVL = {json.dumps(titulos, ensure_ascii=False)};\n" + r"""
(function () {
  var lista = document.getElementById("evf-lista"), res = document.getElementById("evf-res"), sel = [], cor = false;
  function baraja(a) { a = a.slice(); for (var i = a.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)), x = a[i]; a[i] = a[j]; a[j] = x; } return a; }
  function nueva() {
    sel = []; cor = false;
    for (var t = 1; t <= 8; t++) { var p = baraja(EVB.filter(function (q) { return q.t === t; })).slice(0, 4); sel = sel.concat(p); }
    lista.innerHTML = "";
    sel.forEach(function (q, i) {
      var orden = baraja(q.o.map(function (o, k) { return k; }));
      q._orden = orden; q._elegida = null;
      var li = document.createElement("li"); li.className = "evf-p";
      li.innerHTML = '<p class="evf-tema">Tema ' + q.t + '</p><p class="evf-q" id="evf-q' + i + '">' + q.q + '</p><div class="opciones" role="radiogroup" aria-labelledby="evf-q' + i + '">' +
        orden.map(function (k) { return '<button type="button" class="opcion" role="radio" aria-checked="false" data-k="' + k + '">' + q.o[k] + '</button>'; }).join("") + '</div><div class="evf-fb"></div>';
      li.querySelectorAll(".opcion").forEach(function (b) {
        b.addEventListener("click", function () { if (cor) return; li.querySelectorAll(".opcion").forEach(function (x) { x.classList.remove("elegida"); x.setAttribute("aria-checked", "false"); });
          b.classList.add("elegida"); b.setAttribute("aria-checked", "true"); q._elegida = +b.getAttribute("data-k"); li.classList.remove("evf-falta"); });
      });
      lista.appendChild(li);
    });
    res.innerHTML = ""; document.getElementById("evf-imp").hidden = true; document.getElementById("evf-corregir").disabled = false;
  }
  function corregir() {
    var faltan = sel.filter(function (q) { return q._elegida === null; }).length;
    if (faltan && !cor) {
      lista.querySelectorAll(".evf-p").forEach(function (li, i) { li.classList.toggle("evf-falta", sel[i]._elegida === null); });
      res.innerHTML = '<p class="fb pista">Faltan ' + faltan + ' pregunta' + (faltan > 1 ? 's' : '') + ' por responder (marcadas en amarillo).</p>'; return;
    }
    cor = true; document.getElementById("evf-corregir").disabled = true;
    var porTema = {}, total = 0, malas = [];
    sel.forEach(function (q, i) {
      var li = lista.children[i], bien = q._elegida === q.c;
      porTema[q.t] = porTema[q.t] || [0, 0]; porTema[q.t][1]++; if (bien) { porTema[q.t][0]++; total++; } else malas.push(q);
      li.classList.add(bien ? "evf-bien" : "evf-mal");
      li.querySelectorAll(".opcion").forEach(function (b) { var k = +b.getAttribute("data-k"); if (k === q.c) b.classList.add("correcta"); else if (k === q._elegida) b.classList.add("incorrecta"); b.disabled = true; });
      li.querySelector(".evf-fb").innerHTML = (bien ? "✅ " : "❌ ") + q.s + (bien ? "" : ' <a href="leccion-' + q.l + '.html">Repase la Lección ' + q.l.replace("-", ".") + '</a>');
    });
    var pct = Math.round(total / sel.length * 100), filas = "";
    for (var t = 1; t <= 8; t++) { var p = porTema[t] || [0, 0], v = p[1] ? Math.round(p[0] / p[1] * 100) : 0;
      filas += '<tr><th scope="row">Tema ' + t + ' · ' + EVT[t] + '</th><td>' + p[0] + ' de ' + p[1] + '</td><td>' + (v >= 75 ? "✅ Lo domina" : "📚 Repasar") + '</td></tr>'; }
    var rep = {}; malas.forEach(function (q) { rep[q.l] = 1; });
    var links = Object.keys(rep).sort(function (a, b) { var x = a.split("-"), y = b.split("-"); return x[0] - y[0] || x[1] - y[1]; })
      .map(function (l) { return '<li><a href="leccion-' + l + '.html">Lección ' + l.replace("-", ".") + ' · ' + (EVL[l] || "") + '</a></li>'; }).join("");
    res.innerHTML = '<div class="evf-resumen"><p class="evf-total">' + total + ' de ' + sel.length + ' (' + pct + ' %)</p><p>' +
      (pct >= 80 ? "🎉 <strong>¡Domina el Nivel 1!</strong> Está listo para el Nivel 2." : "Va por buen camino. Repase los temas marcados y repita la evaluación: la meta es el 80 % (26 preguntas).") +
      '</p><table class="tabla-ej"><caption>Resultado por tema</caption><thead><tr><th scope="col">Tema</th><th scope="col">Aciertos</th><th scope="col">Estado</th></tr></thead><tbody>' + filas + '</tbody></table>' +
      (links ? '<p><strong>Lecciones para repasar:</strong></p><ul>' + links + '</ul>' : '') + '</div>';
    document.getElementById("evf-imp").hidden = false; res.scrollIntoView({ behavior: "smooth", block: "start" });
  }
  document.getElementById("evf-corregir").addEventListener("click", corregir);
  document.getElementById("evf-otra").addEventListener("click", function () { nueva(); window.scrollTo({ top: lista.getBoundingClientRect().top + window.scrollY - 90 }); });
  document.getElementById("evf-imp").addEventListener("click", function () { window.print(); });
  nueva();
})();
""")
    mods = [("evaluacion", "Evaluación final del Nivel 1", cont)]
    return C.pagina_practica(N, "Evaluación final del Nivel 1", f"32 preguntas · 4 de cada tema · sorteadas entre {len(B)} · meta: 80 %", mods, js)


if __name__ == "__main__":
    LE.construye(N, leccion, practica, horas="Unas 3 horas")
