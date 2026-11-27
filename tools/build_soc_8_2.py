"""LearnGED · Estudios sociales · Lección 8.2 · Proyecto final: indagación cívica y acción informada (EN/ES).
Fuente: sociales/soc-8-2.html (la pregunta convincente, el banco de veinte asuntos, el arco de indagación del Marco C3,
dónde están los datos, la conclusión proporcionada, la propuesta de acción, la presentación y la rúbrica de cinco criterios).
Como en Ciencias 8.2, la lección es un cuaderno de trabajo: campos que se guardan como borrador en el navegador, una tabla de
datos con su resumen y su gráfica, el informe para copiar y la impresión. Sin quiz: el proyecto es la evaluación.
Además, una página de práctica: «¿Sirve esta pregunta?», el tamaño de la conclusión y a quién se dirige la propuesta, y el
orden de la presentación.
Uso: python3 tools/build_soc_8_2.py
"""
import os, sys, json, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sociales import C, t

N = "8-2"


def campo(fid, etiqueta, ayuda="", filas=4):
    ay = f'<p class="ayuda" id="{fid}-ayuda">{ayuda}</p>' if ayuda else ""
    desc = f' aria-describedby="{fid}-ayuda"' if ayuda else ""
    return f'<div class="campo"><label for="{fid}">{etiqueta}</label>{ay}<textarea id="{fid}" class="trabajo" rows="{filas}" data-campo="{fid}"{desc}></textarea></div>'


def tipo_fuente(fid, etiqueta):
    ops = [("", t("Choose…", "Elija…")), ("num", t("Numbers (data)", "Números (datos)")), ("voz", t("Human voice (testimony)", "Voz humana (testimonio)")), ("otra", t("Other", "Otra"))]
    o = "".join(f'<option value="{v}">{x}</option>' for v, x in ops)
    return f'<div class="campo"><label for="{fid}">{etiqueta}</label><select id="{fid}" data-campo="{fid}" class="corto">{o}</select></div>'


def etapa(n, sid, tit, cuerpo):
    return f'<section class="etapa"><h2 id="{sid}"><span aria-hidden="true" class="num-seccion">{n}</span>{tit}</h2>\n{cuerpo}\n</section>'


def rubrica():
    return C.tabla(t("Final project rubric: five criteria, four levels, up to 20 points", "Rúbrica analítica del proyecto final, con cinco criterios y cuatro niveles de desempeño cada uno: hasta veinte puntos"),
        [t("Criterion", "Criterio"), t("Beginning (1)", "Inicial (1)"), t("Developing (2)", "En desarrollo (2)"), t("Proficient (3)", "Competente (3)"), t("Advanced (4)", "Destacado (4)")],
        [[t("1 · A compelling question", "1 · Pregunta convincente"), t("It asks for a single fact, or it is so broad that any answer fits.", "Pide un dato, o es tan amplia que cualquier respuesta vale."), t("It is arguable but has no place or period.", "Es discutible pero le falta lugar o periodo."), t("It is arguable, researchable, and bounded.", "Es discutible, investigable y acotada."), t("It also comes broken into supporting questions that build it step by step.", "Además viene desglosada en preguntas de apoyo que la construyen paso a paso.")],
         [t("2 · Sources and credibility", "2 · Fuentes y credibilidad"), t("Uses one or two sources without saying where they come from.", "Usa una o dos fuentes sin decir de dónde salen."), t("Gathers several but evaluates none.", "Reúne varias pero no evalúa ninguna."), t("Four sources, each with its card: who, when, and for what purpose.", "Cuatro fuentes con su ficha: quién, cuándo y con qué propósito."), t("Names the least reliable one and why, and says how to check it.", "Señala cuál es la menos fiable y por qué, y explica qué haría para verificarla.")],
         [t("3 · Putting evidence together", "3 · Integración de evidencia"), t("Only numbers, or only testimony.", "Solo números, o solo testimonios."), t("Has both kinds, but in separate sections with no link.", "Trae las dos clases pero en secciones separadas, sin relacionarlas."), t("Builds a table or graph of their own and joins it to the testimony.", "Construye una representación cuantitativa propia y la une a los testimonios."), t("Says what the numbers show that the testimony cannot, and the other way around.", "Dice qué sabe por los números que no sabría por los testimonios, y al revés.")],
         [t("4 · A conclusion that fits the evidence", "4 · Conclusión proporcionada"), t("Claims more than the evidence allows, or concludes nothing.", "Afirma más de lo que la evidencia permite, o no concluye nada."), t("Concludes reasonably but names no limit.", "Concluye razonablemente pero no menciona ningún límite."), t("The conclusion is the size of the evidence and names what is still uncertain.", "La conclusión es del tamaño de la evidencia y nombra lo que queda incierto."), t("Separates what the data show from what they only suggest, and says what data are missing.", "Distingue lo que los datos muestran de lo que solo sugieren, y dice qué dato faltaría.")],
         [t("5 · Action and presentation", "5 · Acción y presentación"), t("The proposal is a general wish, or there is none.", "La propuesta es un deseo general, o no la hay."), t("It is concrete but does not say to whom it is directed.", "Es concreta pero no dice a quién se dirige."), t("Concrete, directed at whoever has the power to decide, and within reach of one person or a small group.", "Concreta, dirigida a quien tiene la potestad, y al alcance de una persona o un grupo pequeño."), t("The presentation also fits in five minutes and answers the two required questions well.", "Además la presentación cabe en cinco minutos y responde con solvencia a las dos preguntas.")]])


def banco_asuntos():
    return C.tabla(t("Twenty local subjects you can research with public data, by area", "Banco de veinte asuntos locales investigables con datos públicos, agrupados por ámbito"),
        [t("Area", "Ámbito"), t("Subjects", "Asuntos")],
        [[t("Transportation", "Transporte"), t("Bus frequency by neighborhood · Commute time depending on where you live · Station accessibility · Traffic safety at specific intersections · Cost of a monthly pass compared with the minimum wage", "Frecuencia de autobuses por barrio · Tiempo de trayecto al trabajo según dónde se viva · Accesibilidad de las estaciones · Seguridad vial en cruces concretos · Coste del pase mensual frente al salario mínimo")],
         [t("Housing", "Vivienda"), t("How rent has changed in your ZIP code · Share of income that goes to housing · Affordable housing built in the last ten years · Evictions by neighborhood", "Evolución del alquiler en su código postal · Proporción del ingreso que se va en vivienda · Vivienda asequible construida en los últimos diez años · Desalojos por barrio")],
         [t("Schools", "Escuelas"), t("Budget per student across districts · Adult English classes offered · After-school programs · Condition of the buildings", "Presupuesto por estudiante entre distritos · Oferta de clases de inglés para adultos · Programas después del horario escolar · Estado de los edificios")],
         [t("Health and surroundings", "Salud y entorno"), t("Air quality by area · Distance to the nearest clinic · Green space per person · Access to fresh food", "Calidad del aire por zona · Distancia a la clínica más cercana · Espacios verdes por habitante · Acceso a alimentos frescos")],
         [t("Services and participation", "Servicios y participación"), t("City service response time by neighborhood · Local voter turnout · Services in Spanish at public offices", "Tiempo de respuesta de los servicios municipales por barrio · Participación electoral local · Servicios en español en las oficinas públicas")]])


def pagina():
    L = C.L
    tn = 8
    rub = rubrica()
    banco = banco_asuntos()
    filas_datos = "\n".join(
        f'<tr><th scope="row">{i}</th>'
        f'<td><input type="text" id="d{i}-c" data-campo="d{i}-c" aria-label="{t("Row", "Fila")} {i}: {t("place, group, or year", "lugar, grupo o año")}"></td>'
        f'<td><input type="text" inputmode="decimal" id="d{i}-v" data-campo="d{i}-v" aria-label="{t("Row", "Fila")} {i}: {t("value", "valor")}"></td>'
        f'<td><input type="text" id="d{i}-u" data-campo="d{i}-u" aria-label="{t("Row", "Fila")} {i}: {t("unit", "unidad")}"></td>'
        f'<td><input type="text" id="d{i}-o" data-campo="d{i}-o" aria-label="{t("Row", "Fila")} {i}: {t("source and year", "fuente y año")}"></td></tr>' for i in range(1, 13))

    e1 = (f'<p>{t("Write your compelling question and, under it, three smaller supporting questions you must answer to get there. Check it against the three conditions: arguable, researchable, bounded.", "Escriba su pregunta convincente y, debajo, tres preguntas de apoyo más pequeñas que hay que responder para llegar a ella. Compruébela con las tres condiciones: discutible, investigable y acotada.")}</p>'
          f'<div class="campo"><label for="nombre">{t("Name and start date", "Nombre y fecha de inicio")}</label><input type="text" id="nombre" data-campo="nombre" class="corto"></div>'
          + campo("pregunta", t("My compelling question", "Mi pregunta convincente"), t("A comparison you can measure plus a “what would explain it” usually works. Example: “Does my neighborhood have worse access to public transit than other neighborhoods of the city, and what would explain the difference?”", "Suele funcionar una comparación medible más un «qué lo explicaría». Ejemplo: «¿Tiene mi barrio peor acceso al transporte público que otros barrios de la ciudad, y qué explicaría la diferencia?»"), 3)
          + campo("apoyo", t("Three supporting questions", "Tres preguntas de apoyo"), t("Smaller questions, often with one answer each, that build the big one. Example: How many buses an hour stop in my neighborhood? And in the city as a whole? How long do my neighbors take to get to work?", "Preguntas más pequeñas, a menudo con una sola respuesta, que construyen la grande. Ejemplo: ¿Cuántos autobuses por hora paran en mi barrio? ¿Y en el conjunto de la ciudad? ¿Cuánto tardan mis vecinos en llegar al trabajo?"), 4)
          + campo("interes", t("Why it matters to me", "Por qué me importa"), t("Two or three lines. You will say this in the first minute of your presentation.", "Dos o tres líneas. Lo dirá en el primer minuto de su presentación."), 3)
          + C.caja("tip", t("The test of a good question", "La prueba de una buena pregunta"), "<p>" + t("Read your question to someone and ask them to answer it from memory. If they give a quick, sure answer, the question was not arguable: change it now, not in week 3.", "Lea su pregunta a alguien y pídale que la responda de memoria. Si le da una respuesta segura y rápida, la pregunta no era discutible: cámbiela ahora, no en la semana 3.") + "</p>"))
    fuentes = "".join(campo(f"f{i}", t(f"Source {i}: what it is, who produced it, when, and for what purpose", f"Fuente {i}: qué es, quién la produjo, cuándo y con qué propósito"), "", 3) + tipo_fuente(f"f{i}t", t(f"Kind of source {i}", f"Tipo de la fuente {i}")) for i in range(1, 5))
    e2 = (f'<p>{t("Gather at least four sources: <strong>two with numbers and two with a human voice</strong>. For each one, write down three things before you use it: who produced it, when the data are from, and for what purpose it was published. It is the same card you have seen on every document in this course, and for the same reason: a source with no origin cannot be judged, and one that cannot be judged cannot be used.", "Reúna al menos cuatro fuentes: <strong>dos con números y dos con voz humana</strong>. De cada una anote tres cosas antes de usarla: quién la produjo, de cuándo son los datos y con qué propósito se publicaron. Es la misma ficha que ha visto en cada documento de este curso, y por la misma razón: una fuente sin procedencia no se puede evaluar, y una que no se puede evaluar no se puede usar.")}</p>'
          + C.caja("ojo", t("Two with numbers and two with a voice is not decoration", "«Dos con números y dos con voz» no es un adorno"), "<p>" + t("An eviction statistic says how many there were and does not say what it is like to be evicted; a family’s testimony says the second and does not prove the first. A project with only numbers convinces no one, and one with only testimony proves nothing. It is what you practiced in Lesson 6.2.", "Una estadística de desalojos dice cuántos hubo y no dice qué es que lo desalojen a uno; el testimonio de una familia dice lo segundo y no prueba lo primero. Un proyecto con solo números no convence a nadie y uno con solo testimonios no demuestra nada. Es lo que practicó en la Lección 6.2.") + "</p>")
          + fuentes
          + campo("menosfiable", t("My least reliable source, and how I would check it", "Mi fuente menos fiable, y cómo la verificaría"), t("Required, and it earns points (criterion 2).", "Obligatorio, y suma puntos (criterio 2)."), 3))
    e3 = (f'<p>{t("Build <strong>your own</strong> table or graph with the data you gathered. Do not copy one from the internet: make yours, even by hand. Write one value per row and the place, group, or year it belongs to, always written the same way (for example, always “My neighborhood” and “City”), so the page can group the rows.", "Construya <strong>su propia</strong> tabla o gráfica con los datos que reunió. No copie una de internet: haga la suya, aunque sea a mano. Escriba un valor por fila y el lugar, grupo o año al que corresponde, escrito siempre igual (por ejemplo, siempre «Mi barrio» y «Ciudad»), para que la página pueda agrupar las filas.")}</p>'
          f'<div aria-label="{t("Data table (you can scroll sideways)", "Tabla de datos (desplazable horizontalmente)")}" class="tabla-scroll" role="region" tabindex="0"><table class="tabla-trad tabla-datos"><caption class="cap-oculto">{t("Table to record up to twelve values: row number, place or group, value, unit, and source", "Tabla para registrar hasta doce valores: número, lugar o grupo, valor, unidad y fuente")}</caption>'
          f'<thead><tr><th scope="col">{t("No.", "N.º")}</th><th scope="col">{t("Place, group, or year", "Lugar, grupo o año")}</th><th scope="col">{t("Value", "Valor")}</th><th scope="col">{t("Unit", "Unidad")}</th><th scope="col">{t("Source and year", "Fuente y año")}</th></tr></thead><tbody>{filas_datos}</tbody></table></div>'
          f'<p class="aviso-desliza"><span aria-hidden="true">↔</span> {t("Slide the table sideways to see all the columns.", "Deslice la tabla horizontalmente para ver todas las columnas.")}</p>'
          f'<p><button class="btn btn-sec" type="button" id="b-resumen">{t("Summarize my data", "Resumir mis datos")}</button></p>'
          f'<div id="resumen" aria-live="polite"></div>'
          + C.caja("tip", t("Same unit, or no comparison", "La misma unidad, o no hay comparación"), "<p>" + t("Compare only values in the same unit and the same period (Lesson 8.1). A total for your neighborhood next to a percent for the city is not a comparison. If the units differ, divide first: per person, per household, per 1,000 people (Lesson 2.3).", "Compare solo valores en la misma unidad y del mismo periodo (Lección 8.1). Un total de su barrio junto a un porcentaje de la ciudad no es una comparación. Si las unidades no coinciden, divida primero: por habitante, por hogar, por cada 1,000 personas (Lección 2.3).") + "</p>")
          + campo("describe", t("Paragraph 1 · What my data show", "Párrafo 1 · Lo que muestran mis datos"), t("Describe only. The word “because” cannot appear in this paragraph: describing and explaining are two different things (Lesson 6.2).", "Solo describa. La palabra «porque» no puede aparecer en este párrafo: describir y explicar son dos cosas distintas (Lección 6.2)."), 4)
          + campo("testimonios", t("Paragraph 2 · What the testimony adds", "Párrafo 2 · Lo que aportan los testimonios"), t("What do the voices tell you that the numbers cannot, and what do the numbers show that the voices cannot?", "¿Qué le dicen las voces que no dicen los números, y qué muestran los números que no muestran las voces?"), 4))
    e4 = (f'<p>{t("The last two steps separate a good project from an excellent one, and both are about not overreaching.", "Los dos últimos pasos separan un buen proyecto de uno excelente, y los dos consisten en no pasarse.")}</p>'
          + C.tabla(t("Three conclusions about the same investigation, with the same evidence behind them", "Tres conclusiones sobre la misma investigación, con la misma evidencia detrás"), [t("Conclusion", "Conclusión"), t("What is wrong with it", "Qué le pasa")],
             [[t("“Transit is worse in my neighborhood.”", "«En mi barrio el transporte es peor.»"), t("Too vague. Worse than where, measured how? It cannot be checked, so it cannot be discussed either.", "Demasiado vaga. ¿Peor que dónde, medido cómo? No se puede comprobar, así que tampoco se puede discutir.")],
              [t("“The city deliberately discriminates against my neighborhood in transit.”", "«La ciudad discrimina deliberadamente a mi barrio en el transporte.»"), t("Too big. Frequency data do not prove intention, and you have no sources on how the decisions were made. It is the absolute of Lesson 8.1.", "Demasiado grande. Los datos de frecuencia no prueban intención, y usted no tiene fuentes sobre cómo se tomaron las decisiones. Es el error del absoluto de la Lección 8.1.")],
              [t("“Between 2015 and 2025, bus frequency in my neighborhood fell by X%, while in the city as a whole it fell by Y%. The testimony I gathered describes longer trips to work. The data do not show why it was decided this way.”", "«Entre 2015 y 2025 la frecuencia de autobuses en mi barrio bajó un X %, mientras que en el conjunto de la ciudad bajó un Y %. Los testimonios recogidos describen trayectos más largos al trabajo. Los datos no permiten decir por qué se decidió así.»"), t("<strong>The right size.</strong> It says what it measures, against what comparison, with what human voice, and where what it can claim stops.", "<strong>Del tamaño correcto.</strong> Dice qué mide, con qué comparación, con qué voz humana, y dónde se detiene lo que puede afirmar.")]])
          + campo("conclusion", t("My conclusion", "Mi conclusión"), t("Answer your question, and cite right away the data point behind it.", "Responda a su pregunta y cite enseguida el dato que la sostiene."), 4)
          + campo("incierto", t("What is still unresolved", "Lo que queda sin resolver"), t("Required, and it earns points (criterion 4). Saying it out loud is not a weakness: it shows you understood.", "Obligatorio, y suma puntos (criterio 4). Decirlo en voz alta no es una debilidad: demuestra que lo entendió."), 3)
          + f'<h3>{t("A proposal someone can really carry out", "Una propuesta que se pueda hacer de verdad")}</h3>'
          + C.tabla(t("Three conditions of an informed action", "Tres condiciones de una acción informada"), [t("Condition", "Condición"), t("What it means", "Qué significa")],
             [[t("Concrete", "Concreta"), t("It says exactly what is done. “Raise awareness” is not an action; “present a petition with signatures at the March school board meeting” is.", "Dice qué se hace exactamente. «Concienciar» no es una acción; «presentar una petición con firmas en la reunión de marzo de la junta escolar» sí lo es.")],
              [t("Directed", "Dirigida"), t("It names whoever has the power to decide it. Everything you learned in Topics 4 and 5 about who does what applies here.", "Nombra a quien tiene la potestad de decidirlo. Aquí sirve todo lo que aprendió en los Temas 4 y 5 sobre quién hace qué.")],
              [t("Within reach", "A su alcance"), t("You or a small group can start it without permission or a budget. If it needs a federal law, it is not your proposal: it is your wish.", "Usted o un grupo pequeño puede empezarla sin permiso ni presupuesto. Si necesita una ley federal, no es su propuesta: es su deseo.")]])
          + C.caja("tip", t("The question that organizes this part", "La pregunta que ordena esta parte"), "<p>" + t("<strong>Who has the power to change this?</strong> A matter decided by your city council member is not the same as one decided by the school board or by the state. Sending a proposal to someone who cannot grant it is the most common way for nothing to happen.", "<strong>¿Quién tiene la potestad de cambiar esto?</strong> No es lo mismo un asunto que decide el concejal de su distrito, uno que decide la junta escolar y uno que decide el estado. Dirigir una propuesta a quien no puede concederla es la manera más común de que no pase nada.") + "</p>")
          + campo("accion", t("My proposal: what exactly will be done", "Mi propuesta: qué se hace exactamente"), "", 3)
          + campo("quien", t("To whom: who has the power to decide it", "A quién: quién tiene la potestad de decidirlo"), "", 2)
          + campo("cuando", t("When, and the first step", "Cuándo, y el primer paso"), "", 2))
    e5 = (f'<p>{t("The presentation lasts five minutes and has five parts, about one a minute, in this order: <strong>the question</strong> and why it matters to you; <strong>the sources</strong>, where they come from and which one seemed least reliable; <strong>the evidence</strong>, your graph and what the testimony says; <strong>the conclusion</strong>, the size of the evidence, and what is still unresolved; <strong>the proposal</strong>: what, to whom, and when.", "La presentación dura cinco minutos y tiene cinco partes, más o menos una por minuto, en este orden: <strong>la pregunta</strong> y por qué le importa; <strong>las fuentes</strong>, de dónde salen y cuál le pareció menos fiable; <strong>la evidencia</strong>, su gráfica y lo que dicen los testimonios; <strong>la conclusión</strong>, del tamaño de la evidencia, y lo que queda sin resolver; <strong>la propuesta</strong>: qué, a quién y cuándo.")}</p>'
          + campo("guion", t("My presentation script", "Guion de mi presentación"), t("One or two sentences per minute. If you go over five minutes when you rehearse, do not talk faster: cut. And if what you cut is “what is still unresolved,” put it back and cut something else.", "Una o dos frases por minuto. Si al ensayar se pasa de cinco minutos, no hable más rápido: quite. Y si lo que quita es «lo que queda sin resolver», póngalo de nuevo y quite otra cosa."), 6)
          + C.caja("ojo", t("The two required questions", "Las dos preguntas obligatorias"), "<p>" + t("After the presentation, whoever listens asks you two questions. If you work alone, write them yourself and answer them in writing: these two, whatever the others are.", "Después de la presentación, quien le escucha le hace dos preguntas. Si trabaja solo, escríbaselas usted mismo y respóndalas por escrito: estas dos, sean cuales sean las otras.") + "</p>")
          + campo("preg1", t("1 · Does your conclusion hold up with the evidence you presented, or is one more piece of data needed?", "1 · ¿Se sostiene su conclusión con la evidencia que ha presentado, o hace falta un dato más?"), "", 3)
          + campo("preg2", t("2 · Is your proposal really doable, and is it directed at whoever can grant it?", "2 · ¿Es su propuesta realmente viable, y va dirigida a quien puede concederla?"), "", 3)
          + C.caja("tip", t("If someone listens to you", "Si alguien le escucha"), "<p>" + t("This is what the course asks of the listener: point out one specific strength in the use of evidence and one source worth checking. Not an opinion on the subject, and not general advice. It is the rule of Lesson 7.3: comment on the work, not on the position.", "Esto es lo que el curso pide a quien escucha: señalar una fortaleza concreta en el uso de la evidencia y una fuente que convendría verificar. No una opinión sobre el tema, ni un consejo general. Es la regla de la Lección 7.3: se comenta el trabajo, no la postura.") + "</p>"))

    etapas = [("e1", t("Step 1 · Ask", "Paso 1 · Preguntar"), e1), ("e2", t("Step 2 · Find and evaluate sources", "Paso 2 · Buscar y evaluar fuentes"), e2), ("e3", t("Step 3 · Put the evidence together", "Paso 3 · Integrar la evidencia"), e3),
              ("e4", t("Step 4 · Conclude and propose", "Paso 4 · Concluir y proponer"), e4), ("e5", t("Five minutes and two questions", "Cinco minutos y dos preguntas"), e5)]
    cuerpo_etapas = "\n".join(etapa(i + 1, sid, tit, c) for i, (sid, tit, c) in enumerate(etapas))
    idx = "".join(f'<li><a href="#{s}">{x}</a></li>' for s, x in [("s-plantilla", t("How to use this workbook", "Cómo trabajar con este cuaderno")), ("s-rubrica", t("The rubric, from day one", "La rúbrica, desde el primer día")), ("s-pregunta", t("The question decides everything", "La pregunta lo decide todo")), ("s-datos", t("Where the data are", "Dónde están los datos"))] + [(s, x) for s, x, _ in etapas] + [("s-plan", t("How to spread out the work", "Cómo repartir el trabajo")), ("s-evaluar", t("How to grade it", "Cómo evaluarlo")), ("s-sigue", t("Coming next", "Lo que viene"))])
    titulos = {sid: tit for sid, tit, _ in etapas}
    etiquetas = {}
    for m in re.finditer(r'<label for="([^"]+)">([^<]+)</label>', "".join(c for _, _, c in etapas)):
        etiquetas[m.group(1)] = m.group(2)
    orden = [("e1", ["nombre", "pregunta", "apoyo", "interes"]), ("e2", ["f1", "f1t", "f2", "f2t", "f3", "f3t", "f4", "f4t", "menosfiable"]), ("e3", ["DATOS", "describe", "testimonios"]),
             ("e4", ["conclusion", "incierto", "accion", "quien", "cuando"]), ("e5", ["guion", "preg1", "preg2"])]
    info = {"clave": "learnged-sociales-proyecto-" + L, "orden": [[titulos[s], [[f, etiquetas.get(f, "")] for f in fs]] for s, fs in orden],
            "tipos": {"num": t("Numbers (data)", "Números (datos)"), "voz": t("Human voice (testimony)", "Voz humana (testimonio)"), "otra": t("Other", "Otra")},
            "txt": {"guardado": t("Draft saved in this browser at ", "Borrador guardado en este navegador a las "), "cargado": t("Your saved draft was loaded.", "Se cargó su borrador guardado."),
                    "borrar": t("Press again within 5 seconds to erase everything. This cannot be undone.", "Pulse otra vez en menos de 5 segundos para borrar todo. No se puede deshacer."), "borrado": t("Everything was erased.", "Se borró todo."),
                    "sin": t("(not filled in)", "(sin completar)"), "datos": t("Data", "Datos"), "media": t("value", "valor"), "n": t("rows", "filas"), "cond": t("Place, group, or year", "Lugar, grupo o año"), "ncab": t("Rows", "Filas"), "mcab": t("Value (average if more than one row)", "Valor (media si hay más de una fila)"),
                    "nodatos": t("Type at least one place or group with a numeric value to see the summary.", "Escriba al menos un lugar o grupo con un valor numérico para ver el resumen."),
                    "resumen": t("Summary of your data: the value of each place, group, or year.", "Resumen de sus datos: el valor de cada lugar, grupo o año."),
                    "aviso1": "", "aviso2": "", "yeje": t("Value", "Valor"), "unid": t("Careful: your rows use different units (", "Cuidado: sus filas usan unidades distintas ("), "unid2": t("). Compare only values in the same unit.", "). Compare solo valores en la misma unidad."),
                    "graf": t("Bar graph of the value of each place, group, or year", "Gráfica de barras del valor de cada lugar, grupo o año"), "titulo": t("FINAL PROJECT · CIVIC INQUIRY AND INFORMED ACTION", "PROYECTO FINAL · INDAGACIÓN CÍVICA Y ACCIÓN INFORMADA"),
                    "copiado": t("Report copied. You can paste it into an email or a document.", "Informe copiado. Puede pegarlo en un correo o en un documento."), "nocopia": t("Select the text and copy it with Ctrl+C (Cmd+C on a Mac).", "Seleccione el texto y cópielo con Ctrl+C (Cmd+C en Mac).")}}
    logica = r'''
var INFO = window.INFO, X = INFO.txt;
function $(id){ return document.getElementById(id); }
function campos(){ return [].slice.call(document.querySelectorAll("[data-campo]")); }
function lee(){ var o = {}; campos().forEach(function(c){ o[c.dataset.campo] = c.value; }); return o; }
function escribe(o){ campos().forEach(function(c){ if (o[c.dataset.campo] != null) c.value = o[c.dataset.campo]; }); }
function aviso(m){ $("estado").textContent = m; }
function guarda(silencio){ try { localStorage.setItem(INFO.clave, JSON.stringify(lee())); if (!silencio){ var d = new Date(); aviso(X.guardado + d.toLocaleTimeString()); } } catch(e){} }
function num(s){ s = String(s || "").trim().replace(/\s/g, ""); if (!s) return null; if (/^-?\d{1,3}(,\d{3})+(\.\d+)?$/.test(s)) s = s.replace(/,/g, ""); else s = s.replace(",", "."); var v = Number(s); return isFinite(v) ? v : null; }
function filas(){ var out = []; for (var i = 1; i <= 12; i++){ var c = $("d" + i + "-c").value.trim(), v = $("d" + i + "-v").value.trim(), u = $("d" + i + "-u").value.trim(), o = $("d" + i + "-o").value.trim(); if (c || v || u || o) out.push({i: i, c: c, v: v, u: u, o: o}); } return out; }
function grupos(){ var g = {}, ord = []; filas().forEach(function(f){ var v = num(f.v); if (!f.c || v === null) return; var k = f.c.toLowerCase(); if (!g[k]){ g[k] = {nom: f.c, vals: [], u: f.u}; ord.push(k); } g[k].vals.push(v); if (!g[k].u && f.u) g[k].u = f.u; }); return ord.map(function(k){ var x = g[k]; x.media = x.vals.reduce(function(a, b){ return a + b; }, 0) / x.vals.length; return x; }); }
function fmt(v){ return (Math.round(v * 100) / 100).toLocaleString("en-US"); }
function esc(s){ return String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;"); }
function resumen(){
  var gs = grupos(), r = $("resumen");
  if (!gs.length){ r.innerHTML = "<p>" + X.nodatos + "</p>"; return; }
  var una = gs.filter(function(g){ return g.vals.length < 2; }).map(function(g){ return esc(g.nom); });
  var h = "<p><strong>" + X.resumen + "</strong></p><table class=\"tabla-trad\"><caption class=\"cap-oculto\">" + X.resumen + "</caption><thead><tr><th scope=\"col\">" + X.cond + "</th><th scope=\"col\">" + X.ncab + "</th><th scope=\"col\">" + X.mcab + "</th></tr></thead><tbody>" +
    gs.map(function(g){ return "<tr><th scope=\"row\">" + esc(g.nom) + "</th><td>" + g.vals.length + "</td><td>" + fmt(g.media) + (g.u ? " " + esc(g.u) : "") + "</td></tr>"; }).join("") + "</tbody></table>";
  var mx = Math.max.apply(null, gs.map(function(g){ return g.media; })), mn = Math.min(0, Math.min.apply(null, gs.map(function(g){ return g.media; })));
  var W = 520, H = 260, x0 = 60, y0 = 20, ah = 180, bw = Math.min(90, (W - x0 - 20) / gs.length - 20), rango = (mx - mn) || 1;
  var y = function(v){ return y0 + ah - (v - mn) / rango * ah; };
  var s = "<svg viewBox=\"0 0 " + W + " " + H + "\" style=\"width:100%;max-width:" + W + "px;height:auto\" role=\"img\" aria-label=\"" + X.graf + ": " + gs.map(function(g){ return esc(g.nom) + " " + fmt(g.media); }).join(", ") + "\">";
  s += "<line x1=\"" + x0 + "\" y1=\"" + y(mn) + "\" x2=\"" + (W - 10) + "\" y2=\"" + y(mn) + "\" stroke=\"#222\" stroke-width=\"2\"/><line x1=\"" + x0 + "\" y1=\"" + y0 + "\" x2=\"" + x0 + "\" y2=\"" + (y0 + ah) + "\" stroke=\"#222\" stroke-width=\"2\"/>";
  gs.forEach(function(g, k){ var bx = x0 + 20 + k * (bw + 20), top = y(Math.max(g.media, 0)), bot = y(Math.min(g.media, 0));
    s += "<rect x=\"" + bx + "\" y=\"" + top + "\" width=\"" + bw + "\" height=\"" + Math.max(bot - top, 1) + "\" fill=\"#5b8def\" stroke=\"#1e3a8a\"/>";
    s += "<text x=\"" + (bx + bw / 2) + "\" y=\"" + (top - 6) + "\" font-size=\"13\" font-weight=\"700\" text-anchor=\"middle\" fill=\"#1e3a8a\">" + fmt(g.media) + "</text>";
    s += "<text x=\"" + (bx + bw / 2) + "\" y=\"" + (y0 + ah + 20) + "\" font-size=\"13\" text-anchor=\"middle\" fill=\"#222\">" + esc(g.nom.length > 14 ? g.nom.slice(0, 13) + "…" : g.nom) + "</text>"; });
  s += "<text x=\"16\" y=\"" + (y0 + ah / 2) + "\" font-size=\"12\" text-anchor=\"middle\" fill=\"#222\" transform=\"rotate(-90 16 " + (y0 + ah / 2) + ")\">" + (X.yeje || X.mcab) + (gs[0].u ? " (" + esc(gs[0].u) + ")" : "") + "</text></svg>";
  h += s;
  var us = []; gs.forEach(function(g){ var u = (g.u || "").trim().toLowerCase(); if (u && us.indexOf(u) < 0) us.push(u); });
  if (X.unid && us.length > 1) h += "<p class=\"aviso-corto\">" + X.unid + us.map(esc).join(", ") + X.unid2 + "</p>";
  if (X.aviso1 && una.length) h += "<p class=\"aviso-corto\">" + X.aviso1 + una.join(", ") + X.aviso2 + "</p>";
  r.innerHTML = h;
}
function informe(){
  var o = lee(), L = [X.titulo, ""];
  INFO.orden.forEach(function(e){
    L.push("== " + e[0].toUpperCase() + " ==");
    e[1].forEach(function(p){
      if (p[0] === "DATOS"){ L.push(X.datos + ":"); var fs = filas(); if (!fs.length) L.push("  " + X.sin); fs.forEach(function(f){ L.push("  " + f.i + ". " + [f.c, f.v + (f.u ? " " + f.u : ""), f.o].filter(Boolean).join(" · ")); });
        var gs = grupos(); if (gs.length){ L.push("  " + X.resumen); gs.forEach(function(g){ L.push("  - " + g.nom + ": " + X.media + " " + fmt(g.media) + (g.u ? " " + g.u : "") + " (" + g.vals.length + " " + X.n + ")"); }); }
        return; }
      var v = (o[p[0]] || "").trim(); if (INFO.tipos && INFO.tipos[v]) v = INFO.tipos[v]; L.push(p[1] + ":"); L.push(v || X.sin); L.push("");
    });
    L.push("");
  });
  $("informe-txt").value = L.join("\n"); $("informe-caja").hidden = false; $("informe-txt").focus();
}
$("b-guardar").addEventListener("click", function(){ guarda(false); });
$("b-informe").addEventListener("click", function(){ guarda(true); informe(); });
$("b-copiar").addEventListener("click", function(){ var tx = $("informe-txt"); tx.select(); var ok = false; try { ok = document.execCommand("copy"); } catch(e){} if (navigator.clipboard){ navigator.clipboard.writeText(tx.value).then(function(){ aviso(X.copiado); }, function(){ aviso(X.nocopia); }); } else aviso(ok ? X.copiado : X.nocopia); });
$("b-imprimir").addEventListener("click", function(){ guarda(true); resumen(); window.print(); });
$("b-resumen").addEventListener("click", resumen);
var armado = 0;
$("b-borrar").addEventListener("click", function(){ var ahora = Date.now(); if (ahora - armado > 5000){ armado = ahora; aviso(X.borrar); return; } armado = 0; try { localStorage.removeItem(INFO.clave); } catch(e){} campos().forEach(function(c){ c.value = ""; }); $("resumen").innerHTML = ""; $("informe-caja").hidden = true; aviso(X.borrado); });
var t0; document.addEventListener("input", function(){ clearTimeout(t0); t0 = setTimeout(function(){ guarda(true); }, 1500); });
try { var g = localStorage.getItem(INFO.clave); if (g){ escribe(JSON.parse(g)); aviso(X.cargado); if (grupos().length) resumen(); } } catch(e){}
'''
    estilo = """
  [hidden]{display:none !important;}
  .campo{margin:14px 0;}
  .campo label{display:block;font-weight:700;color:var(--azul-osc,#14265e);margin-bottom:4px;font-size:17px;}
  .campo .ayuda{margin:0 0 6px;font-size:15px;color:#4a5568;}
  textarea.trabajo,input.corto,select.corto{width:100%;font:inherit;font-size:17px;padding:10px;border:2px solid #b0bec5;border-radius:8px;background:#fff;box-sizing:border-box;}
  input.corto{max-width:520px;}
  select.corto{max-width:420px;}
  textarea.trabajo:focus,input.corto:focus,select.corto:focus,.tabla-datos input:focus{outline:3px solid #1e3a8a;outline-offset:1px;border-color:#1e3a8a;}
  .tabla-datos input{width:100%;min-width:110px;font:inherit;font-size:16px;padding:6px 8px;border:1px solid #b0bec5;border-radius:6px;box-sizing:border-box;}
  .tabla-datos td{padding:6px !important;}
  .fila-botones{display:flex;flex-wrap:wrap;gap:10px;margin:12px 0;}
  #estado{font-weight:600;color:#14265e;min-height:1.4em;}
  #informe-txt{width:100%;min-height:320px;font-family:Consolas,'Courier New',monospace;font-size:14px;padding:10px;border:2px solid #b0bec5;border-radius:8px;box-sizing:border-box;}
  .aviso-corto{background:#fdf3df;border-left:4px solid #5C3900;padding:8px 12px;border-radius:5px;color:#5C3900;font-weight:600;}
  section.etapa{border-top:3px solid #e6e9f2;padding-top:6px;}
  @media print{
    .lg-bar,.saltar,.fila-botones,#informe-caja,.indice,.aviso-desliza,#estado{display:none !important;}
    textarea.trabajo{border:1px solid #000;min-height:0;height:auto;}
    section.etapa{break-inside:auto;}
    body{background:#fff;}
  }"""
    otro = "es" if L == "en" else "en"
    return f'''<!DOCTYPE html>
<!-- LearnGED · {t("Social studies · Lesson 8.2 · Final project workbook", "Estudios sociales · Lección 8.2 · Cuaderno del proyecto final")} — {t("built by", "construida con")} tools/build_soc_8_2.py
     José M. Fernández · CC BY-NC-SA 4.0 -->
<html lang="{L}">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>{t("Lesson 8.2 · Final project: civic inquiry and informed action · LearnGED", "Lección 8.2 · Proyecto final: indagación cívica y acción informada · LearnGED")}</title>
<meta content="CC BY-NC-SA 4.0" name="license"/><link href="https://creativecommons.org/licenses/by-nc-sa/4.0/" rel="license"/>
<link rel="icon" href="/favicon.svg" type="image/svg+xml"/>
<link rel="alternate" hreflang="{otro}" href="/{C.carpeta(otro)}/{C.lec(N, otro)}"/>
<link rel="stylesheet" href="/math/lesson.css">
<link rel="stylesheet" href="/science/science.css">
<link rel="stylesheet" href="/social-studies/social.css">
<style>{estilo}
</style>
</head>
<body data-area="ged">
{C.barra()}
<a class="saltar" href="#indice">{t("Skip to the workbook contents", "Saltar al contenido del cuaderno")}</a>
<header class="principal">
<div class="envoltura-header">
<p class="ruta">{t("Social studies · Topic", "Estudios sociales · Tema")} {tn} — {C.tema(tn)}</p>
<h1>{t("Lesson 8.2 · Final project: civic inquiry and informed action", "Lección 8.2 · Proyecto final: indagación cívica y acción informada")}</h1>
<p class="lema">{t("Choose a question from your own community, find and judge the sources yourself, and propose an action someone can really carry out.", "Elija una pregunta de su propia comunidad, busque y evalúe usted las fuentes, y proponga una acción que alguien pueda llevar a cabo de verdad.")}</p>
<div class="chips">
<span class="chip"><span aria-hidden="true">⏱️</span> {t("About 8 hours, spread over two or three weeks", "Unas 8 horas, repartidas en dos o tres semanas")}</span>
<span class="chip chip-sp">SSP.1 – SSP.11 · {t("All the practices of the course", "Todas las prácticas del curso")}</span>
<span class="chip chip-sp">{t("C3 Framework · Dimension 4: informed action", "Marco C3 · Dimensión 4: acción informada")}</span>
<span class="chip chip-sp">{t("No quiz · the project is the assessment", "Sin quiz · el proyecto es la evaluación")}</span>
</div>
</div>
</header>
<div class="envoltura">
<section>
<div class="caja caja-objetivo">
<h2><span aria-hidden="true" class="num-seccion">🎯</span>{t("What you will do", "Lo que va a hacer")}</h2>
<ul>
<li>{t("<strong>Ask</strong> a question worth researching that allows more than one reasonable answer.", "<strong>Formular</strong> una pregunta que valga la pena investigar y que admita más de una respuesta razonable.")}</li>
<li>{t("<strong>Gather</strong> relevant sources and judge the credibility of each one.", "<strong>Reunir</strong> fuentes pertinentes y evaluar la credibilidad de cada una.")}</li>
<li>{t("<strong>Join</strong> numerical evidence and testimony in one argument.", "<strong>Integrar</strong> en un mismo argumento evidencia numérica y evidencia de testimonio.")}</li>
<li>{t("<strong>Reach</strong> a conclusion the size of the evidence and propose a civic action that can be done.", "<strong>Llegar</strong> a una conclusión proporcionada a la evidencia y proponer una acción cívica viable.")}</li>
</ul>
</div>
</section>
<nav aria-labelledby="indice-titulo" class="indice" id="indice"><h2 id="indice-titulo">{t("Workbook contents", "Contenido del cuaderno")}</h2><ol>{idx}</ol></nav>

<div class="caja caja-tip"><span class="etiqueta et-verde">{t("Before you start", "Antes de empezar")}</span>
<p>{t("<strong>Where we are.</strong> In the twenty-one earlier lessons you analyzed the sources you were given. Here you choose them, find them, and judge them yourself, on a subject that really matters to you.", "<strong>Dónde quedamos.</strong> En las veintiuna lecciones anteriores usted analizó las fuentes que le dieron. Aquí las elige, las busca y las evalúa por su cuenta, sobre un asunto que le importe de verdad.")}</p>
<p>{t("<strong>This page is your workbook.</strong> It is not a lesson to read: it is a template you fill in over two or three weeks. This project has no quiz: the project is the assessment, and its rubric is on this page from day one. Read it before you start, not after you finish.", "<strong>Esta página es su cuaderno de trabajo.</strong> No es una lección para leer: es una plantilla que se va completando a lo largo de dos o tres semanas. Este proyecto no tiene quiz: el proyecto es la evaluación, y su rúbrica está en esta página desde el primer día. Léala antes de empezar, no después de terminar.")}</p>
<p>{t("<strong>What you need:</strong> a subject from your community that matters to you (there are twenty below if none comes to mind), internet access to look for public data, and someone to listen to you for five minutes at the end. One person is enough.", "<strong>Lo que necesita:</strong> un asunto de su comunidad que le importe (abajo hay veinte si no se le ocurre ninguno), acceso a internet para buscar datos públicos y alguien que le escuche cinco minutos al final. Basta con una persona.")}</p>
</div>

<section>
<h2 id="s-plantilla"><span aria-hidden="true" class="num-seccion">💾</span>{t("How to use this workbook", "Cómo trabajar con este cuaderno")}</h2>
<p>{t("Type straight into the fields. The page saves a draft in this browser by itself every few seconds, and you can also press <strong>Save draft</strong>. When you come back to this page on the same device, you will find your work where you left it.", "Escriba directamente en los campos. La página guarda sola un borrador en este navegador cada pocos segundos, y también puede pulsar <strong>Guardar borrador</strong>. Al volver a esta página en el mismo equipo, encontrará su trabajo donde lo dejó.")}</p>
{C.caja("ojo", t("A saved draft is not a backup", "El borrador guardado no es una copia de seguridad"), "<p>" + t("It is only on this device and is lost if the browser’s data are cleared or if you use another device. To keep your work, press <strong>Make the report</strong> and copy the text, or use <strong>Print or save as PDF</strong>.", "Solo está en este equipo y se pierde si se borran los datos del navegador o si se usa otro dispositivo. Para conservar su trabajo, pulse <strong>Generar informe</strong> y copie el texto, o use <strong>Imprimir o guardar en PDF</strong>.") + "</p>")}
<div class="fila-botones">
<button class="btn" type="button" id="b-guardar">{t("Save draft", "Guardar borrador")}</button>
<button class="btn" type="button" id="b-informe">{t("Make the report", "Generar informe")}</button>
<button class="btn btn-sec" type="button" id="b-imprimir">{t("Print or save as PDF", "Imprimir o guardar en PDF")}</button>
<button class="btn btn-sec" type="button" id="b-borrar">{t("Erase everything and start over", "Borrar todo y empezar de nuevo")}</button>
</div>
<p id="estado" role="status" aria-live="polite"></p>
<div id="informe-caja" hidden>
<label for="informe-txt"><strong>{t("Full report, ready to copy", "Informe completo, listo para copiar")}</strong></label>
<textarea id="informe-txt" readonly></textarea>
<p><button class="btn btn-sec" type="button" id="b-copiar">{t("Copy the report", "Copiar el informe")}</button></p>
</div>
</section>

<section>
<h2 id="s-rubrica"><span aria-hidden="true" class="num-seccion">📊</span>{t("The rubric, from day one", "La rúbrica, desde el primer día")}</h2>
<p>{t("This rubric does not appear at the end to grade you: you get it now, at the start, because <strong>it is the guide for the work</strong>. Five criteria with four levels each: 20 points in all. It takes the place of the lesson quiz.", "Esta rúbrica no aparece al final para calificarle: se le da ahora, al principio, porque <strong>es la guía del trabajo</strong>. Cinco criterios de cuatro niveles: veinte puntos en total. Sustituye al quiz de la lección.")}</p>
{C.caja("tip", t("Look at criteria 2 and 4", "Fíjese en los criterios 2 y 4"), "<p>" + t("<strong>Naming your least reliable source and what is still unresolved adds points; it does not take them away.</strong> A project that admits what its evidence cannot show is better done, not worse.", "<strong>Señalar su fuente menos fiable y lo que queda sin resolver suma puntos; no los resta.</strong> Un proyecto que reconoce lo que su evidencia no puede mostrar está mejor hecho, no peor.") + "</p>")}
{rub}
</section>

<section>
<h2 id="s-pregunta"><span aria-hidden="true" class="num-seccion">❓</span>{t("The question decides everything", "La pregunta lo decide todo")}</h2>
<p>{t("The most important step of the project is the first one, and it is where most people go wrong. A compelling question must meet three conditions at once.", "El paso más importante del proyecto es el primero, y es donde más gente se equivoca. Una pregunta convincente tiene que cumplir tres condiciones a la vez.")}</p>
{C.tabla(t("The three conditions of a compelling question", "Las tres condiciones de una pregunta convincente"), [t("Condition", "Condición"), t("What it means", "Qué significa"), t("Does not work", "No sirve")],
  [[t("Arguable", "Discutible"), t("It allows more than one reasonable answer. If there is only one, it is not research: it is a lookup.", "Admite más de una respuesta razonable. Si solo hay una, no es una investigación: es una consulta."), t("“How many schools are in my district?”", "«¿Cuántas escuelas hay en mi distrito?»")],
   [t("Researchable", "Investigable"), t("There are data and testimony you can reach to answer it. If there are not, it cannot be done.", "Existen datos y testimonios accesibles que permiten responderla. Si no los hay, no se puede hacer."), t("“What would my neighbors have thought in 1950?”", "«¿Qué pensarían los vecinos en 1950?»")],
   [t("Bounded", "Acotada"), t("It has a specific place and period. Without them, any answer fits and none holds up.", "Tiene un lugar y un periodo concretos. Sin eso, cualquier respuesta cabe y ninguna se sostiene."), t("“Is housing fair?”", "«¿Es justa la vivienda?»")]])}
{C.tabla(t("The same concern, asked three ways, and only one works", "La misma inquietud, formulada de tres maneras, y solo una sirve"), [t("Wording", "Formulación"), t("What happens", "Qué le pasa")],
  [[t("“How many bus lines run through my neighborhood?”", "«¿Cuántas líneas de autobús pasan por mi barrio?»"), t("Researchable and bounded, but not arguable: it has one answer and you can find it in a minute. It is a fact, not a question.", "Investigable y acotada, pero no es discutible: tiene una sola respuesta y se busca en un minuto. Es un dato, no una pregunta.")],
   [t("“Is public transit unfair?”", "«¿Es injusto el transporte público?»"), t("Arguable, but neither researchable nor bounded: it does not say where, when, or compared with what. Any answer is worth the same, which means none is worth anything.", "Discutible, pero no es investigable ni está acotada: no dice dónde, ni cuándo, ni respecto de qué. Cualquier respuesta valdrá igual, y eso significa que no vale nada.")],
   [t("“Does my neighborhood have worse access to public transit than other neighborhoods of the city, and what would explain the difference?”", "«¿Tiene mi barrio peor acceso al transporte público que otros barrios de la ciudad, y qué explicaría la diferencia?»"), t("<strong>It works.</strong> It allows more than one answer, there are public data to answer it, and it has a place and a comparison.", "<strong>Sirve.</strong> Admite más de una respuesta, hay datos públicos para responderla, y tiene lugar y comparación.")]])}
{C.caja("tip", t("The test of a good question", "La prueba de una buena pregunta"), "<p>" + t("If you can imagine two reasonable, informed people answering it differently, you are on track. If the answer seems obvious before you start, change it: research whose result you already know is not research, and the rubric notices.", "Si puede imaginar a dos personas razonables e informadas respondiéndola de manera distinta, va bien. Si la respuesta le parece obvia antes de empezar, cámbiela: una investigación cuyo resultado ya se conoce no es una investigación, y la rúbrica lo nota.") + "</p>")}
<h3>{t("Twenty subjects to choose from", "Veinte asuntos para elegir")}</h3>
<p>{t("All of them can be researched with public data, and all allow more than one answer. They are written as subjects, not questions: you write the question.", "Todos son investigables con datos públicos y todos admiten más de una respuesta. Están redactados como temas, no como preguntas: la pregunta la escribe usted.")}</p>
{banco}
{C.enlace(N, t("does-it-work", "sirve"), t("Does this question work?", "¿Sirve esta pregunta?"), t("Eight project questions: do they work, or which condition is missing?", "Ocho preguntas de proyecto: ¿sirven, o qué condición les falta?"))}
</section>

<section>
<h2 id="s-datos"><span aria-hidden="true" class="num-seccion">🔎</span>{t("Where the data are", "Dónde están los datos")}</h2>
<p>{t("More public data are available, for free, than people imagine. These are the places to look, ordered by how close they are to your neighborhood.", "Hay más datos públicos disponibles, y gratis, de lo que uno imagina. Estos son los sitios donde buscar, ordenados por lo cerca que están de su barrio.")}</p>
{C.tabla(t("Public data sources, from local to national", "Fuentes públicas de datos, de lo local a lo nacional"), [t("Where", "Dónde"), t("What you find", "Qué se encuentra"), t("How to get there", "Cómo llegar")],
  [[t("Your city’s data portal", "El portal de datos de su ciudad"), t("Almost every big city publishes one: calls to city services, building permits, crime, inspections, budget. Chicago has its own.", "Casi todas las ciudades grandes publican uno: llamadas a servicios municipales, permisos de obra, delitos, inspecciones, presupuesto. Chicago tiene el suyo."), t("Search for “open data portal” and the name of your city.", "Busque «portal de datos abiertos» (open data portal) y el nombre de su ciudad.")],
   [t("U.S. Census Bureau", "La Oficina del Censo de los Estados Unidos"), t("Population, income, housing, commuting, language spoken at home. With detail by census tract, which is almost block by block.", "Población, ingresos, vivienda, transporte al trabajo, idioma hablado en casa. Con detalle por sector censal, es decir, casi por manzanas."), t("Search for “American Community Survey” and your neighborhood or ZIP code.", "Busque «American Community Survey» y el nombre de su barrio o su código postal.")],
   [t("Your area’s transit agency", "La agencia de transporte de su área"), t("Routes, frequency, on-time performance, riders per stop.", "Rutas, frecuencias, puntualidad, número de pasajeros por parada."), t("Its website usually has a data or reports section.", "Su página suele tener una sección de datos o de informes.")],
   [t("The school district", "El distrito escolar"), t("Budget, enrollment, staff, results, and building condition, school by school.", "Presupuesto, matrícula, personal, resultados y estado de los edificios, escuela por escuela."), t("Districts publish yearly reports for each school.", "Los distritos publican informes anuales por escuela.")],
   [t("Your public library", "Su biblioteca pública"), t("Access to paid databases, old newspapers and, above all, librarians who know how to search.", "Acceso a bases de datos de pago, periódicos antiguos y, sobre todo, bibliotecarios que saben buscar."), t("Ask at the reference desk. It is free, and it is the fastest shortcut on this list.", "Pregunte en el mostrador de referencia. Es gratis y es el atajo más rápido de esta tabla.")]])}
{C.caja("ojo", t("Why this table has no links", "Por qué esta tabla no lleva enlaces"), "<p>" + t("On purpose. Addresses change, portals are redesigned, and a broken link in a course is worse than none. And there is a better reason: knowing how to find the source is part of what this project assesses.", "A propósito. Las direcciones cambian, los portales se rediseñan y un enlace roto en un curso es peor que ninguno. Y hay una razón mejor: saber encontrar la fuente es parte de lo que este proyecto evalúa.") + "</p>")}
</section>

{cuerpo_etapas}

<section>
<h2 id="s-plan"><span aria-hidden="true" class="num-seccion">🗓️</span>{t("How to spread out the work", "Cómo repartir el trabajo")}</h2>
{C.tabla(t("A three-week plan", "Un plan de tres semanas"), [t("Week", "Semana"), t("What you do", "Qué hace"), t("Check yourself", "Compruebe usted mismo")],
  [[t("1 · The question and the sources · 3 hours", "1 · La pregunta y las fuentes · 3 horas"), t("Choose the subject, write the compelling question and the three supporting ones. Then go looking: gather the four minimum sources, two with numbers and two with a voice, and fill in the card for each one.", "Elija el asunto, escriba la pregunta convincente y las tres de apoyo. Después salga a buscar: reúna las cuatro fuentes mínimas, dos con números y dos con voz humana, y haga la ficha de cada una."), t("Read your question to someone and ask them to answer it from memory. If the answer is quick and sure, redo the question now.", "Lea su pregunta a alguien y pídale que la responda de memoria. Si la respuesta es segura y rápida, rehaga la pregunta ahora.")],
   [t("2 · The evidence · 3 hours", "2 · La evidencia · 3 horas"), t("Build your graph or table with the data you gathered, and write the two paragraphs.", "Construya su gráfica o su tabla con los datos que reunió, y escriba los dos párrafos."), t("The word “because” cannot appear in the paragraph that describes.", "En el párrafo que describe no puede aparecer la palabra «porque».")],
   [t("3 · The conclusion, the proposal, and your voice · 2 hours", "3 · La conclusión, la propuesta y la voz · 2 horas"), t("Write the conclusion and the proposal, and rehearse the presentation out loud with a clock. Five minutes are less than they seem.", "Escriba la conclusión y la propuesta, y ensaye la presentación en voz alta con un reloj. Cinco minutos son menos de lo que parecen."), t("If you go over five minutes, cut, but never “what is still unresolved”: that part is worth a full level of the rubric.", "Si se pasa de cinco minutos, quite, pero nunca «lo que queda sin resolver»: esa parte vale un nivel entero de la rúbrica.")]])}
</section>

<section>
<h2 id="s-evaluar"><span aria-hidden="true" class="num-seccion">✅</span>{t("How to grade it", "Cómo evaluarlo")}</h2>
<p>{t("Press <strong>Make the report</strong>, copy the text, and give it to your teacher to grade with the rubric, criterion by criterion. Before you hand it in, grade it yourself with the same rubric, and apply the rule of Lesson 8.1 to your own work: does your conclusion hold up with the evidence you presented?", "Pulse <strong>Generar informe</strong>, copie el texto y entrégueselo a su docente para que lo evalúe con la rúbrica, criterio por criterio. Antes de entregarlo, evalúelo usted con la misma rúbrica y aplíquele a su propio trabajo el criterio de la Lección 8.1: ¿se sostiene su conclusión con la evidencia que presentó?")}</p>
</section>

<section class="cierre">
<h2 id="s-sigue"><span aria-hidden="true" class="num-seccion">➡️</span>{t("Coming next", "Lo que viene")}</h2>
<p>{t("Three ideas to take away. Research whose result you already know is not research, so if your question seems obvious before you start, change it. Numbers and voices need each other: an eviction statistic says how many there were and not what it is like to be evicted. And a proposal goes to whoever has the power to grant it, which is the first thing to find out.", "Tres ideas se llevan de aquí. Una investigación cuyo resultado ya se conoce no es una investigación, así que si su pregunta le parece obvia antes de empezar, cámbiela. Los números y las voces se necesitan: una estadística de desalojos dice cuántos hubo y no qué es que lo desalojen a uno. Y una propuesta se dirige a quien tiene la potestad de concederla, que es lo primero que hay que averiguar.")}</p>
<p>{t("This project is the only work in the course where nobody tells you the right answer in advance, and that is on purpose. Everything else was training for this: reading a source, doubting an average, telling describing from explaining, spotting an absolute, and knowing who decides what. Lesson 8.3 closes the course with the item types of the test, managing your time, a timed practice test, and the Illinois Constitution requirement.", "Este proyecto es el único trabajo del curso en el que nadie le dice de antemano cuál es la respuesta correcta, y eso es a propósito. Todo lo demás ha sido entrenamiento para esto: leer una fuente, dudar de un promedio, distinguir describir de explicar, reconocer un absoluto y saber quién decide qué. La Lección 8.3 cierra el curso con los tipos de pregunta del examen, la gestión del tiempo, un simulacro cronometrado y el requisito de la Constitución de Illinois.")}</p>
<p class="flecha-sig"><span aria-hidden="true">➡️</span> {t("Next", "Siguiente")}: <a href="{C.lec("8-3")}">{t("Lesson 8.3 · Timed practice test, item types, and the Illinois Constitution", "Lección 8.3 · Simulacro cronometrado, tipos de pregunta y Constitución de Illinois")}</a></p>
</section>
</div>
<footer><p>LearnGED · {t("Social studies · Topic 8 · Lesson 8.2", "Estudios sociales · Tema 8 · Lección 8.2")}</p>{C.PIE[L]}</footer>
<script>
window.INFO = {json.dumps(info, ensure_ascii=False)};
{logica}
</script>
</body>
</html>
'''


# ---------------------------------------------------------------- la práctica
def casos_sirve():
    G = [t("It works", "Sirve"), t("Not arguable", "No es discutible"), t("Not researchable", "No es investigable"), t("Not bounded", "No está acotada")]
    PI = [t("Arguable, researchable, and bounded all at once?", "¿Discutible, investigable y acotada a la vez?"), t("Does it have just one answer you could look up in a minute?", "¿Tiene una sola respuesta que se busca en un minuto?"),
          t("Are there data or testimony you could actually reach?", "¿Existen datos o testimonios a los que de verdad pueda llegar?"), t("Does it say where, when, and compared with what?", "¿Dice dónde, cuándo y respecto de qué?")]
    def caso(tit, piezas):
        return {"titulo": tit, "intro": t("Does each project question work? If not, which condition is missing?", "¿Sirve cada pregunta de proyecto? Si no, ¿qué condición le falta?"), "grupos": G, "etiqueta": t("This question…", "Esta pregunta…"),
                "piezas": [{"t": a, "v": v, "pista": PI[v]} for a, v in piezas]}
    return [
        caso(t("Set 1", "Serie 1"), [
            (t("How many elementary schools are in my district?", "¿Cuántas escuelas primarias hay en mi distrito?"), 1),
            (t("Is the housing system fair?", "¿Es justo el sistema de vivienda?"), 3),
            (t("What would the people of my neighborhood have thought about transit in 1930?", "¿Qué habrían opinado los vecinos de mi barrio en 1930 sobre el transporte?"), 2),
            (t("Has average rent in my ZIP code risen faster than in the city as a whole over the last ten years, and what would explain it?", "¿Ha aumentado el alquiler medio en mi código postal más deprisa que en el conjunto de la ciudad en los últimos diez años, y qué lo explicaría?"), 0)]),
        caso(t("Set 2", "Serie 2"), [
            (t("Should there be more parks?", "¿Debería haber más parques?"), 3),
            (t("Which bus line in the city has the most riders?", "¿Cuál es la línea de autobús con más pasajeros de la ciudad?"), 1),
            (t("Do the schools in my district get less money per student than those in neighboring districts, and what would explain the difference?", "¿Reciben las escuelas de mi distrito menos presupuesto por estudiante que las de distritos vecinos, y qué explicaría la diferencia?"), 0),
            (t("Is my city a good place to live?", "¿Es mi ciudad un buen lugar para vivir?"), 3)]),
    ]


def banco_proyecto():
    D = [(t("A student’s data show that bus frequency in her neighborhood fell more than in the rest of the city. Which conclusion is the right size?", "Los datos de una estudiante muestran que la frecuencia de autobuses en su barrio bajó más que en el resto de la ciudad. ¿Qué conclusión es del tamaño correcto?"),
          [t("Frequency fell more in her neighborhood; the data do not show why", "La frecuencia bajó más en su barrio; los datos no muestran por qué"), t("The city discriminates against her neighborhood on purpose", "La ciudad discrimina a propósito a su barrio"), t("Transit is worse in her neighborhood", "En su barrio el transporte es peor")], t("Frequency data do not prove intention, and “worse” is too vague.", "Los datos de frecuencia no prueban intención, y «peor» es demasiado vago.")),
         (t("Which proposal is an informed action?", "¿Qué propuesta es una acción informada?"),
          [t("Present a petition with 60 signatures at the school board meeting in March", "Presentar una petición con 60 firmas en la reunión de marzo de la junta escolar"), t("Raise awareness about the schools", "Concienciar sobre las escuelas"), t("Ask Congress to pass a federal law for my school", "Pedir al Congreso una ley federal para mi escuela")], t("Concrete, directed at whoever decides, and within reach.", "Concreta, dirigida a quien decide y a su alcance.")),
         (t("A project wants more frequent buses on a city route. To whom should the proposal be directed first?", "Un proyecto quiere más frecuencia en una ruta de autobús de la ciudad. ¿A quién debe dirigirse primero la propuesta?"),
          [t("The transit agency that sets the schedules", "A la agencia de transporte que fija los horarios"), t("The Supreme Court", "Al Tribunal Supremo"), t("The President", "Al presidente")], t("Who has the power to change it? Topics 4 and 5.", "¿Quién tiene la potestad de cambiarlo? Temas 4 y 5.")),
         (t("A project has two tables of eviction numbers and nothing else. What is missing?", "Un proyecto tiene dos tablas de cifras de desalojos y nada más. ¿Qué le falta?"),
          [t("Human voice: testimony of what being evicted is like", "La voz humana: testimonios de qué es ser desalojado"), t("More tables", "Más tablas"), t("Nothing", "Nada")], t("Two with numbers and two with a voice.", "Dos con números y dos con voz.")),
         (t("A student’s paragraph describing her graph says: “Rent rose because new buildings came in.” What is wrong?", "El párrafo en que una estudiante describe su gráfica dice: «El alquiler subió porque llegaron edificios nuevos». ¿Qué falla?"),
          [t("It explains instead of describing: “because” does not belong in that paragraph", "Explica en vez de describir: el «porque» no va en ese párrafo"), t("Nothing", "Nada"), t("It should use bigger numbers", "Debería usar cifras más grandes")], t("Describing and explaining are two different things (Lesson 6.2).", "Describir y explicar son dos cosas distintas (Lección 6.2).")),
         (t("In the presentation, a listener says: “I think the city is right to cut buses.” What should the listener do instead?", "En la presentación, quien escucha dice: «Creo que la ciudad hace bien en recortar autobuses». ¿Qué debería hacer en su lugar?"),
          [t("Name one strength in the use of evidence and one source worth checking", "Señalar una fortaleza en el uso de la evidencia y una fuente que convendría verificar"), t("Give a longer opinion", "Dar una opinión más larga"), t("Say nothing", "No decir nada")], t("Comment on the work, not on the position (Lesson 7.3).", "Se comenta el trabajo, no la postura (Lección 7.3).")),
         (t("A student’s conclusion names nothing that is still unresolved. Under the rubric, that…", "La conclusión de un estudiante no nombra nada que quede sin resolver. Según la rúbrica, eso…"),
          [t("keeps criterion 4 at level 2 at most", "deja el criterio 4 en el nivel 2 como mucho"), t("earns the top level", "gana el nivel más alto"), t("does not matter", "no importa")], t("Naming the limit is what earns level 3.", "Nombrar el límite es lo que da el nivel 3."))]
    return [{"enun": "<strong>" + s + "</strong>", "ops": ops, "ok": 0, "exp": e} for s, ops, e in D]


def casos_orden():
    return [{"titulo": t("The five-minute presentation", "La presentación de cinco minutos"), "intro": t("Put the five parts in order with ▲ and ▼.", "Ordene las cinco partes con ▲ y ▼."),
             "pasos": [t("The question, and why it matters to you", "La pregunta, y por qué le importa"), t("The sources, and which one seemed least reliable", "Las fuentes, y cuál le pareció menos fiable"), t("The evidence: your graph and the testimony", "La evidencia: su gráfica y los testimonios"),
                       t("The conclusion, and what is still unresolved", "La conclusión, y lo que queda sin resolver"), t("The proposal: what, to whom, and when", "La propuesta: qué, a quién y cuándo")],
             "inicio": [3, 0, 4, 2, 1], "cons": {"4>3": t("The proposal comes out of the conclusion, so it goes after it.", "La propuesta sale de la conclusión, así que va después."), "3>2": t("You conclude after showing the evidence.", "Se concluye después de enseñar la evidencia.")},
             "general": t("Question, sources, evidence, conclusion, proposal: about one minute each.", "Pregunta, fuentes, evidencia, conclusión, propuesta: más o menos un minuto cada una.")},
            {"titulo": t("The inquiry arc", "El arco de indagación"), "intro": t("Put the four steps of the project in order.", "Ordene los cuatro pasos del proyecto."),
             "pasos": [t("Ask: a compelling question and three supporting ones", "Preguntar: una pregunta convincente y tres de apoyo"), t("Find and evaluate at least four sources", "Buscar y evaluar al menos cuatro fuentes"), t("Put together your own graph and the testimony", "Integrar su propia gráfica y los testimonios"), t("Conclude and propose an action", "Concluir y proponer una acción")],
             "inicio": [2, 3, 0, 1], "cons": {"1>0": t("You cannot look for sources before you know your question.", "No se pueden buscar fuentes sin saber la pregunta."), "3>2": t("The conclusion comes from the evidence.", "La conclusión sale de la evidencia.")},
             "general": t("Ask, find, put together, conclude: the C3 Framework.", "Preguntar, buscar, integrar, concluir: el Marco C3.")}]


def titulo():
    return t("Final project: civic inquiry and informed action", "Proyecto final: indagación cívica y acción informada")


def practica():
    A = {"en": ["does-it-work", "size-and-action", "order"], "es": ["sirve", "tamano-y-accion", "orden"]}[C.L]
    mods = [
        (A[0], t("Does this question work?", "¿Sirve esta pregunta?"), C.clasifica("m1", t("Eight project questions. Decide whether each one works or which of the three conditions it is missing: arguable, researchable, or bounded. If something is not right, the questions marked in yellow get a hint.", "Ocho preguntas de proyecto. Diga si sirven, o cuál de las tres condiciones les falta: ser discutible, ser investigable o estar acotada. Si algo no está bien, las preguntas marcadas en amarillo reciben una pista."))),
        (A[1], t("The size of the conclusion and the address of the action", "El tamaño de la conclusión y la dirección de la acción"), C.om("m2", t("Choose the answer the rubric would reward.", "Elija la respuesta que premiaría la rúbrica."))),
        (A[2], t("Put it in order", "Póngalo en orden"), C.orden("m3")),
    ]
    js = C.js_datos("SIR", casos_sirve()) + C.js_datos("PRO", banco_proyecto()) + C.js_datos("ORD", casos_orden()) + 'creaClasifica("m1", SIR);\ncreaBanco("m2", PRO);\ncreaOrden("m3", ORD);\n'
    return C.pagina_practica(N, titulo(), t("Three activities · two tries in each one", "Tres actividades · dos intentos en cada una"), mods, js)


if __name__ == "__main__":
    for lang in ("en", "es"):
        C.L = lang
        for nombre, f in ((C.lec(N), pagina), (C.prac(N), practica)):
            ruta = os.path.join(C.ROOT, C.carpeta(), nombre)
            open(ruta, "w", encoding="utf-8").write(f())
            print("ok", os.path.relpath(ruta, C.ROOT))
    C.L = "en"
