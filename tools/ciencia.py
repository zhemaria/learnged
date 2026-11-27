"""Herramientas para construir las lecciones de Ciencias de LearnGED en inglés y en español a la vez.

Cada constructor (tools/build_sci_T_N.py) escribe los textos una sola vez, lado a lado, con
t("inglés", "español"), y llama a construye(): salen cuatro páginas

  science/lesson-T-N.html     science/practice-T-N.html        (inglés)
  es/ciencias/leccion-T-N.html es/ciencias/practica-T-N.html    (español)

A diferencia de Matemáticas, aquí no hay traductor del marco: todo el texto, también el marco,
pasa por t(). Las páginas usan el diseño de Matemáticas (/math/lesson.css y /math/practice.css,
/math/lesson.js y /math/practice.js) más /science/science.css (color del área) y
/science/sci.js (actividades de ciencias: ordenar, clasificar, el invernadero, huecos).

Después de construir, ejecute tools/build_planes.py (índice del curso) y tools/build_indices.py
(botón de Inicio en todas las páginas).
"""
import html as H, json, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
L = "en"


def t(en, es):
    """El texto en el idioma que se está construyendo."""
    return en if L == "en" else es


# ---------------------------------------------------------------- la materia (Ciencias; tools/sociales.py la cambia)
MAT = {"nombre": ("Science", "Ciencias"), "carpeta": ("science", "es/ciencias"), "builder": "build_sci_",
       "css": ["/science/science.css"], "icono": "🔬"}


def materia():
    return t(*MAT["nombre"])


# ---------------------------------------------------------------- temas y áreas
TEMAS = {
    1: (("The scientific method and research design", "El método científico y el diseño de investigación"), "skills"),
    2: (("Quantitative reasoning in science", "Razonamiento cuantitativo en ciencias"), "skills"),
    3: (("Life science I: the cell, energy, and the human body", "Ciencias de la vida I: célula, energía y cuerpo humano"), "life"),
    4: (("Life science II: heredity, evolution, and ecosystems", "Ciencias de la vida II: herencia, evolución y ecosistemas"), "life"),
    5: (("Physical science I: matter, atoms, and chemical reactions", "Ciencias físicas I: materia, átomo y reacciones químicas"), "physical"),
    6: (("Physical science II: force, motion, energy, and waves", "Ciencias físicas II: fuerza, movimiento, energía y ondas"), "physical"),
    7: (("Earth and space science", "Ciencias de la Tierra y el espacio"), "earth"),
    8: (("Putting it together: evaluating conclusions and GED preparation", "Integración, evaluación de conclusiones y preparación para el GED"), "ged"),
}
COLOR = {"skills": "#1f6066", "life": "#1b5e20", "physical": "#1e3a8a", "earth": "#5b21b6", "ged": "#8f3f1f"}


def tema(n):
    return t(*TEMAS[n][0])


# ---------------------------------------------------------------- estándares
# GED Testing Service, Assessment Guide for Educators: Science (2016; Science Practices updated 2020).
SP = {
    "SP.1.a": ("Understand and explain textual scientific presentations.", "Comprender y explicar presentaciones científicas escritas."),
    "SP.1.b": ("Determine the meaning of symbols, terms and phrases as they are used in scientific presentations.", "Determinar el significado de símbolos, términos y frases tal como se usan en las presentaciones científicas."),
    "SP.1.c": ("Understand and explain a non-textual scientific presentation.", "Comprender y explicar una presentación científica no textual (tablas, gráficas, diagramas)."),
    "SP.2.a": ("Identify possible sources of error and alter the design of an investigation to ameliorate that error.", "Identificar posibles fuentes de error y modificar el diseño de una investigación para corregirlas."),
    "SP.2.b": ("Identify and refine hypotheses for scientific investigations.", "Identificar y precisar hipótesis para investigaciones científicas."),
    "SP.2.c": ("Identify the strengths and weaknesses of one or more scientific investigation (i.e., experimental or observational) designs.", "Identificar los puntos fuertes y débiles de uno o más diseños de investigación científica (experimentales o de observación)."),
    "SP.2.d": ("Design a scientific investigation.", "Diseñar una investigación científica."),
    "SP.2.e": ("Identify and interpret independent and dependent variables in scientific investigations.", "Identificar e interpretar las variables independiente y dependiente en las investigaciones científicas."),
    "SP.3.a": ("Cite specific textual evidence to support a finding or conclusion.", "Citar evidencia específica del texto que apoye un hallazgo o una conclusión."),
    "SP.3.b": ("Reason from data or evidence to a conclusion.", "Razonar a partir de datos o evidencia hasta llegar a una conclusión."),
    "SP.3.c": ("Make a prediction based upon data or evidence.", "Hacer una predicción a partir de datos o evidencia."),
    "SP.3.d": ("Use sampling techniques to answer scientific questions.", "Usar técnicas de muestreo para responder preguntas científicas."),
    "SP.4.a": ("Evaluate whether a conclusion or theory is supported or challenged by particular data or evidence.", "Evaluar si unos datos o una evidencia concretos apoyan o contradicen una conclusión o teoría."),
    "SP.5.a": ("Reconcile multiple findings, conclusions, or theories.", "Conciliar varios hallazgos, conclusiones o teorías."),
    "SP.6.a": ("Express scientific information or findings visually.", "Expresar información o hallazgos científicos de forma visual."),
    "SP.6.b": ("Express scientific information or findings numerically or symbolically.", "Expresar información o hallazgos científicos con números o símbolos."),
    "SP.6.c": ("Express scientific information or findings verbally.", "Expresar información o hallazgos científicos con palabras."),
    "SP.7.a": ("Understand and apply scientific models, theories, and processes.", "Comprender y aplicar modelos, teorías y procesos científicos."),
    "SP.7.b": ("Apply formulas from scientific theories.", "Aplicar fórmulas de las teorías científicas."),
    "SP.8.a": ("Describe a data set statistically.", "Describir un conjunto de datos con estadística."),
    "SP.8.b": ("Use counting and permutations to solve scientific problems.", "Usar el conteo y las permutaciones para resolver problemas científicos."),
    "SP.8.c": ("Determine the probability of events.", "Determinar la probabilidad de un suceso."),
}
# Content topics (same guide). Only the ones the lessons use are written out.
CT = {
    "L.a": ("Human body and health", "Cuerpo humano y salud"),
    "L.b": ("Relationship between life functions and energy intake", "Relación entre las funciones vitales y la energía que se obtiene"),
    "L.c": ("Energy flows in ecologic networks (ecosystems)", "Flujo de energía en las redes ecológicas (ecosistemas)"),
    "L.d": ("Organization of life (structure and function of life)", "Organización de la vida (estructura y función)"),
    "L.e": ("Molecular basis for heredity", "Base molecular de la herencia"),
    "L.f": ("Evolution", "Evolución"),
    "P.a": ("Conservation, transformation, and flow of energy", "Conservación, transformación y flujo de la energía"),
    "P.b": ("Work, motion, and forces", "Trabajo, movimiento y fuerzas"),
    "P.c": ("Chemical properties and reactions related to living systems", "Propiedades químicas y reacciones relacionadas con los seres vivos"),
    "ES.a": ("Interactions between Earth's systems and living things", "Interacciones entre los sistemas de la Tierra y los seres vivos"),
    "ES.b": ("Earth and its system components and interactions", "La Tierra: componentes de su sistema e interacciones"),
    "ES.c": ("Structures and organization of the cosmos", "Estructura y organización del cosmos"),
}
# Alineación oficial de cada subpráctica (misma guía, tabla de las prácticas científicas):
# (categoría de informe, DOK, estándares alineados). La guía escribe los códigos sin punto (R2, M4).
# En SP.2.b la guía trae además una «M» sin número (errata); se omite.
# Categorías de informe: 1 = analizar argumentos, evidencia y textos (30 %); 2 = aplicar procesos
# científicos y conceptos de procedimiento (40 %); 3 = razonar con cantidades e interpretar datos (30 %).
ALIN = {
    "SP.1.a": (1, "1–3", ["R2", "R8", "P8", "M2", "M6"]),
    "SP.1.b": (1, "2", ["R4", "L4", "P8", "M2", "M4", "M6"]),
    "SP.1.c": (3, "2", ["S-ID", "8.SP", "P8", "M2", "M4", "M6"]),
    "SP.2.a": (2, "2–3", ["R8", "P3", "P4", "M4"]),
    "SP.2.b": (2, "2–3", ["R2", "R5", "W5", "P1", "P8", "M4", "M8"]),
    "SP.2.c": (2, "2–3", ["R8", "R9", "P2", "P5", "M3", "M4"]),
    "SP.2.d": (2, "1–3", ["W7", "3.MD", "P3", "P5", "M4", "M8"]),
    "SP.2.e": (2, "2–3", ["R5", "P2", "P4", "M4"]),
    "SP.3.a": (1, "2–3", ["R1", "P7"]),
    "SP.3.b": (2, "2–3", ["R1", "R2", "R3", "P1", "P6", "P7", "M3", "M4", "M7", "M8"]),
    "SP.3.c": (2, "2–3", ["R1", "R3", "P4", "M3", "M4", "M7", "M8"]),
    "SP.3.d": (3, "2–3", ["S-CP", "7.SP", "P4", "P5", "M4", "M7", "M8"]),
    "SP.4.a": (2, "2–3", ["R8", "P4", "P6", "M3", "M7", "M8"]),
    "SP.5.a": (1, "2–3", ["R9", "P2", "P4", "P6", "M3", "M7"]),
    "SP.6.a": (3, "2", ["R7", "W2", "P8", "M2", "M4", "M6"]),
    "SP.6.b": (3, "1–2", ["R7", "W2", "P5", "P8", "M2", "M4", "M6"]),
    "SP.6.c": (1, "2–3", ["R7", "W2", "P8", "M2", "M6"]),
    "SP.7.a": (2, "2–3", ["R3", "R5", "L3", "P1", "P2", "P7", "M2", "M4"]),
    "SP.7.b": (3, "2", ["P2", "P5", "M2", "M4", "M8"]),
    "SP.8.a": (3, "1–2", ["S-MD", "S-ID", "P4", "P5", "M4", "M6"]),
    "SP.8.b": (3, "1–2", ["7.SP", "P5", "M4", "M6"]),
    "SP.8.c": (3, "2", ["7.SP", "S-CP", "P5", "M4", "M6"]),
}
CATEGORIA = {
    1: ("Category 1 · Analyzing scientific and technical arguments, evidence, and text-based information (30% of the test)", "Categoría 1 · Analizar argumentos científicos y técnicos, evidencia e información de textos (30 % del examen)"),
    2: ("Category 2 · Applying scientific processes and procedural concepts (40% of the test)", "Categoría 2 · Aplicar procesos científicos y conceptos de procedimiento (40 % del examen)"),
    3: ("Category 3 · Reasoning quantitatively and interpreting data in scientific contexts (30% of the test)", "Categoría 3 · Razonar con cantidades e interpretar datos en contextos científicos (30 % del examen)"),
}
# Qué significa cada código alineado (resumen breve, no el texto completo del estándar).
CODIGO = {
    "R1": ("CCR Reading 1: read closely and cite specific evidence from the text.", "Lectura CCR 1: leer con atención y citar evidencia concreta del texto."),
    "R2": ("CCR Reading 2: find the central ideas and summarize them.", "Lectura CCR 2: determinar las ideas centrales y resumirlas."),
    "R3": ("CCR Reading 3: analyze how ideas, events, or steps develop and interact.", "Lectura CCR 3: analizar cómo se desarrollan y relacionan las ideas, los hechos o los pasos."),
    "R4": ("CCR Reading 4: interpret words and phrases, including technical meanings.", "Lectura CCR 4: interpretar palabras y frases, incluidos los significados técnicos."),
    "R5": ("CCR Reading 5: analyze how a text is structured.", "Lectura CCR 5: analizar la estructura de un texto."),
    "R7": ("CCR Reading 7: combine information from text, visuals, and numbers.", "Lectura CCR 7: integrar información de textos, imágenes y números."),
    "R8": ("CCR Reading 8: evaluate the claims in a text and the evidence behind them.", "Lectura CCR 8: evaluar las afirmaciones de un texto y la evidencia que las sostiene."),
    "R9": ("CCR Reading 9: compare how two texts treat the same topic.", "Lectura CCR 9: comparar cómo tratan dos textos el mismo tema."),
    "W2": ("CCR Writing 2: write to inform and explain.", "Escritura CCR 2: escribir para informar y explicar."),
    "W5": ("CCR Writing 5: plan, revise, and improve a piece of writing.", "Escritura CCR 5: planificar, revisar y mejorar un escrito."),
    "W7": ("CCR Writing 7: carry out short research projects.", "Escritura CCR 7: hacer proyectos breves de investigación."),
    "L3": ("CCR Language 3: use knowledge of language to understand how it works in context.", "Lenguaje CCR 3: usar el conocimiento de la lengua para comprender cómo funciona en contexto."),
    "L4": ("CCR Language 4: work out the meaning of unknown words (context, roots).", "Lenguaje CCR 4: deducir el significado de palabras desconocidas (contexto, raíces)."),
    "P1": ("NRC practice 1: ask questions.", "Práctica NRC 1: hacer preguntas."),
    "P2": ("NRC practice 2: develop and use models.", "Práctica NRC 2: desarrollar y usar modelos."),
    "P3": ("NRC practice 3: plan and carry out investigations.", "Práctica NRC 3: planificar y llevar a cabo investigaciones."),
    "P4": ("NRC practice 4: analyze and interpret data.", "Práctica NRC 4: analizar e interpretar datos."),
    "P5": ("NRC practice 5: use mathematics and computational thinking.", "Práctica NRC 5: usar las matemáticas y el pensamiento computacional."),
    "P6": ("NRC practice 6: construct explanations.", "Práctica NRC 6: construir explicaciones."),
    "P7": ("NRC practice 7: argue from evidence.", "Práctica NRC 7: argumentar con evidencia."),
    "P8": ("NRC practice 8: obtain, evaluate, and communicate information.", "Práctica NRC 8: obtener, evaluar y comunicar información."),
    "M2": ("Math practice 2: reason abstractly and quantitatively.", "Práctica matemática 2: razonar de forma abstracta y cuantitativa."),
    "M3": ("Math practice 3: build arguments and critique the reasoning of others.", "Práctica matemática 3: construir argumentos y criticar el razonamiento ajeno."),
    "M4": ("Math practice 4: model with mathematics.", "Práctica matemática 4: modelar con matemáticas."),
    "M6": ("Math practice 6: attend to precision.", "Práctica matemática 6: atender a la precisión."),
    "M7": ("Math practice 7: look for and use structure.", "Práctica matemática 7: buscar y usar la estructura."),
    "M8": ("Math practice 8: look for patterns in repeated reasoning.", "Práctica matemática 8: buscar regularidades en el razonamiento repetido."),
    "3.MD": ("Math, measurement and data (grade 3): measure and choose units.", "Matemáticas, medición y datos (3.er grado): medir y elegir unidades."),
    "7.SP": ("Math, statistics and probability (grade 7): samples and probability.", "Matemáticas, estadística y probabilidad (7.º grado): muestras y probabilidad."),
    "8.SP": ("Math, statistics and probability (grade 8): patterns in two-variable data.", "Matemáticas, estadística y probabilidad (8.º grado): patrones en datos de dos variables."),
    "S-ID": ("Statistics: interpret categorical and quantitative data.", "Estadística: interpretar datos categóricos y cuantitativos."),
    "S-CP": ("Statistics: conditional probability and compound events.", "Estadística: probabilidad condicional y sucesos compuestos."),
    "S-MD": ("Statistics: use probability to make decisions.", "Estadística: usar la probabilidad para tomar decisiones."),
}


def estandares(sp, ct, base=()):
    """sp: prácticas que trabaja; base: prácticas que prepara; ct: temas de contenido.
    Cada práctica muestra su categoría de informe, su DOK y los estándares alineados según la guía."""
    def fam(cods):
        g = {"CCR": [c for c in cods if c[0] in "RWL"], "NRC": [c for c in cods if c[0] == "P"],
             t("Math", "Mat."): [c for c in cods if c[0] == "M" or c[0].isdigit() or c.startswith("S-")]}
        return " · ".join(f"{k} {', '.join(v)}" for k, v in g.items() if v)
    def li(cls, cod):
        cat, dok, cods = ALIN[cod]
        return (f'<li><span class="std-cod {cls}">{cod}</span> {t(*SP[cod])}<br><span class="std-meta">'
                f'{t("Category", "Categoría")} {cat} · DOK {dok} · {fam(cods)}</span></li>')
    usados = []
    for c in list(sp) + list(base):
        for k in ALIN[c][2]:
            if k not in usados:
                usados.append(k)
    cats = sorted({ALIN[c][0] for c in sp})
    s = [f'<details class="estandares" id="{t("ged-standards", "estandares-ged")}">',
         f'<summary><span aria-hidden="true">🎓</span> {t("Standards for this lesson (GED® and CCR)", "Estándares de esta lección (GED® y CCR)")}</summary>',
         '<div class="std-cuerpo">',
         f'<p class="std-tit">{t("Science Practices of the GED® test that this lesson works on:", "Prácticas científicas del examen GED® que trabaja esta lección:")}</p><ul>' +
         "".join(li("std-dir", c) for c in sp) + "</ul>"]
    if base:
        s.append(f'<p class="std-tit">{t("It also builds the base for:", "También prepara la base para:")}</p><ul>' + "".join(li("std-base", c) for c in base) + "</ul>")
    s.append(f'<p class="std-tit">{t("Reporting categories of the GED® Science test:", "Categorías de informe del examen de Ciencias del GED®:")}</p><ul>' +
             "".join(f"<li>{t(*CATEGORIA[k])}</li>" for k in cats) + "</ul>")
    s.append(f'<p class="std-tit">{t("GED® Science content topics:", "Temas de contenido de Ciencias del GED®:")}</p>')
    if ct:
        s.append("<ul>" + "".join(f'<li><span class="std-cod std-mp">{c}</span> {t(*CT[c])}</li>' for c in ct) + "</ul>")
    else:
        s.append("<p>" + t("The skills in this lesson are used with every content topic of the test: life science, physical science, and Earth and space science.",
                           "Las destrezas de esta lección se aplican a todos los temas de contenido del examen: ciencias de la vida, ciencias físicas y ciencias de la Tierra y el espacio.") + "</p>")
    s.append(f'<p class="std-tit">{t("What the aligned codes mean (CCR, NRC, and math):", "Qué significan los códigos alineados (CCR, NRC y matemáticas):")}</p><ul class="std-clave">' +
             "".join(f'<li><span class="std-cod std-ccr">{k}</span> {t(*CODIGO[k])}</li>' for k in usados) + "</ul>")
    s.append('<p class="std-fuente">' + t(
        "DOK (depth of knowledge): 1 = recall, 2 = use a skill or concept, 3 = reason with evidence. Source of the practices, categories, DOK ranges, and alignment: GED Testing Service, <cite>Assessment Guide for Educators: Science</cite> (2016; Science Practices updated in 2020). The CCR anchor standards are in Pimentel, S. (2013), <cite>College and Career Readiness Standards for Adult Education</cite>; the NRC practices are in <cite>A Framework for K-12 Science Education</cite> (National Research Council, 2012).",
        "DOK (profundidad de conocimiento): 1 = recordar, 2 = aplicar una destreza o un concepto, 3 = razonar con evidencia. Fuente de las prácticas, las categorías, los rangos de DOK y la alineación: GED Testing Service, <cite>Assessment Guide for Educators: Science</cite> (2016; prácticas científicas actualizadas en 2020). Los estándares ancla CCR están en Pimentel, S. (2013), <cite>College and Career Readiness Standards for Adult Education</cite>; las prácticas NRC, en <cite>A Framework for K-12 Science Education</cite> (National Research Council, 2012).") + "</p>")
    s.append("</div>\n</details>")
    return "\n".join(s)


def ged_item(practicas, num, sp, dok, pregunta, ops, ok, pistas, solucion):
    """Pregunta tipo GED: un estímulo, cuatro opciones, la práctica y el DOK a la vista."""
    tit = f'{t("GED-style question", "Pregunta tipo GED")} {num} · {sp} · DOK {dok}'
    return practicas(tit, pregunta, ops, ok, pistas, solucion)


# ---------------------------------------------------------------- rutas
def lec(n, lang=None):
    return f"lesson-{n}.html" if (lang or L) == "en" else f"leccion-{n}.html"


def prac(n, lang=None):
    return f"practice-{n}.html" if (lang or L) == "en" else f"practica-{n}.html"


def carpeta(lang=None):
    return MAT["carpeta"][0] if (lang or L) == "en" else MAT["carpeta"][1]


def existe(n):
    return os.path.exists(os.path.join(ROOT, carpeta(), lec(n)))


# ---------------------------------------------------------------- piezas de la lección
def caja(tipo, etiqueta, cuerpo):
    """tipo: 'tip' (verde) u 'ojo' (ámbar)."""
    cls, et = ("caja-tip", "et-verde") if tipo == "tip" else ("caja-ojo", "et-ambar")
    return f'<div class="caja {cls}">\n<span class="etiqueta {et}">{etiqueta}</span>\n{cuerpo}\n</div>'


def ejemplo(titulo, pasos, cierre=None):
    """pasos: lista de (marca, texto)."""
    p = "\n".join(f'<p class="paso"><span aria-hidden="true" class="n">{m}</span>{x}</p>' for m, x in pasos)
    c = f'\n<p class="paso"><span aria-hidden="true" class="n">✓</span>{cierre}</p>' if cierre else ""
    return f'<div class="ejemplo">\n<p class="titulo-ej">{titulo}</p>\n{p}{c}\n</div>'


def tabla(caption, cabeza, filas, fila_th=True):
    th = "".join(f'<th scope="col">{c}</th>' for c in cabeza)
    def fila(f):
        return "<tr>" + "".join((f'<th scope="row">{c}</th>' if i == 0 and fila_th else f"<td>{c}</td>") for i, c in enumerate(f)) + "</tr>"
    return (f'<div aria-label="{H.escape(caption)} {t("(table you can scroll sideways)", "(tabla desplazable horizontalmente)")}" class="tabla-scroll" role="region" tabindex="0"><table class="tabla-trad"><caption class="cap-oculto">{caption}</caption>\n'
            f'<thead><tr>{th}</tr></thead>\n<tbody>\n' + "\n".join(fila(f) for f in filas) + '\n</tbody>\n</table></div>\n'
            f'<p class="aviso-desliza"><span aria-hidden="true">↔</span> {t("Slide the table sideways to see all the columns.", "Deslice la tabla horizontalmente para ver todas las columnas.")}</p>')


def calc(titulo, cuerpo):
    """Recuadro de la calculadora con el botón que la abre (js/calculator.js o js/calculadora.js)."""
    return (f'<div class="caja-calc">\n<span class="et-calc"><span aria-hidden="true">🧮</span> {titulo}</span>\n{cuerpo}\n'
            f'<button type="button" class="btn-calc" data-gph-calculadora><span aria-hidden="true">🧮</span> {t("Open the calculator", "Abrir la calculadora")}</button>\n</div>')


def sci_campos(pid):
    """Respuesta escrita en notación científica (creaPracticaSci de /math/scinot.js)."""
    return f'''      <div class="practica" id="{pid}">
        <div class="enun" id="{pid}-enun"></div>
        <div class="campos campos-sci">
          <div class="campo"><label for="{pid}-c">{t("Coefficient", "Coeficiente")}</label><input type="text" inputmode="decimal" autocomplete="off" class="corto" id="{pid}-c"></div>
          <div class="campo" aria-hidden="true" style="font-size:20px;font-weight:700;padding-bottom:8px;white-space:nowrap;">× 10</div>
          <div class="campo"><label for="{pid}-e">{t("Exponent", "Exponente")}</label><input type="text" autocomplete="off" class="corto" id="{pid}-e"></div>
        </div>
        <p class="nota">{t("Use a decimal point (4.5). For a negative exponent, type the minus sign: −3 or -3.", "Use punto decimal (4.5). Para un exponente negativo, escriba el signo menos: −3 o -3.")}</p>
        <div class="fila-btn">
          <button type="button" class="btn" id="{pid}-comprobar">{t("Check", "Comprobar")}</button>
          <button type="button" class="btn-sec" id="{pid}-nuevo">{t("New exercise", "Otro ejercicio")}</button>
        </div>
        <div class="fb" id="{pid}-fb" role="status"></div>
        <p class="marcador" id="{pid}-marcador"></p>
      </div>'''


def dec_campo(pid, etiqueta):
    """Respuesta escrita con un número decimal (creaPracticaDec de /math/scinot.js)."""
    return f'''      <div class="practica" id="{pid}">
        <div class="enun" id="{pid}-enun"></div>
        <div class="campos"><div class="campo"><label for="{pid}-r">{etiqueta}</label><input type="text" inputmode="decimal" autocomplete="off" class="ancho" id="{pid}-r"></div></div>
        <div class="fila-btn">
          <button type="button" class="btn" id="{pid}-comprobar">{t("Check", "Comprobar")}</button>
          <button type="button" class="btn-sec" id="{pid}-nuevo">{t("New exercise", "Otro ejercicio")}</button>
        </div>
        <div class="fb" id="{pid}-fb" role="status"></div>
        <p class="marcador" id="{pid}-marcador"></p>
      </div>'''


def lectura(titulo, parrafos, nota=None):
    ps = "\n".join(f"<p>{p}</p>" for p in parrafos)
    n = f'<p class="fuente">{nota}</p>' if nota else ""
    return f'<div class="lectura"><h3><span aria-hidden="true">📖</span> {titulo}</h3><div class="texto">\n{ps}\n</div>{n}</div>'


def enlace(n, ancla, titulo, sub):
    return f'''<a class="enlace-interactivo" href="{prac(n)}#{ancla}" target="_blank" rel="noopener noreferrer" aria-label="{t("Open the practice activity", "Abrir la actividad de práctica")}: {H.escape(re.sub("<[^>]+>", "", titulo))} {t("(opens in a new tab)", "(se abre en una pestaña nueva)")}">
<span class="ei-icono" aria-hidden="true">{MAT["icono"]}</span>
<span class="ei-cuerpo"><span class="ei-titulo">{t("Practice more", "Practique más")}: {titulo}</span><span class="ei-sub">{sub}</span><span class="ei-cta">{t("Open the activity", "Abrir la actividad")} <span aria-hidden="true">›</span></span></span>
</a>'''


class Practicas:
    """Reúne las preguntas de práctica de la lección (window.LESSON.practice)."""
    def __init__(self):
        self.datos = {}
        self.k = 0

    def __call__(self, titulo, pregunta, ops, ok, pistas, solucion, right=None):
        """ops: lista de textos; ok: índice de la correcta; pistas: {índice: pista}."""
        self.k += 1
        pid = f"p{self.k}"
        letras = "abcdefgh"
        self.datos[pid] = {"ok": letras[ok], "hints": {letras[i]: h for i, h in pistas.items()}, "right": right or solucion, "solution": solucion}
        btn = "\n".join(f'<button class="opcion" data-k="{letras[i]}" type="button">{x}</button>' for i, x in enumerate(ops))
        return (f'<div class="practica">\n<div class="cabe"><span aria-hidden="true" class="ico">✏️</span><h3>{titulo}</h3></div>\n'
                f'<p class="pregunta-int" id="t-{pid}">{pregunta}</p>\n<div aria-labelledby="t-{pid}" class="opciones" data-practica="{pid}" role="group">\n{btn}\n</div>\n'
                f'<div aria-live="polite" class="respuesta-int" id="r-{pid}" role="status"></div>\n</div>')


def seccion(sid, num, titulo, cuerpo):
    return f'<section>\n<h2 id="{sid}"><span aria-hidden="true" class="num-seccion">{num}</span>{titulo}</h2>\n{cuerpo}\n</section>'


def quiz_html(items):
    letras = "abcdefgh"
    out, datos = [], {}
    for q, (preg, ops, ok, pistas, sol) in enumerate(items, 1):
        datos[str(q)] = {"ok": letras[ok], "hints": {letras[i]: h for i, h in pistas.items()}, "solution": sol}
        btn = "".join(f'<button class="opcion" data-k="{letras[i]}" type="button">{x}</button>' for i, x in enumerate(ops))
        out.append(f'<div class="quiz-bloque" data-q="{q}"><p class="qnum">{t("Question", "Pregunta")} {q}</p>\n<p class="pregunta" id="t-q{q}">{preg}</p>\n'
                   f'<div aria-labelledby="t-q{q}" class="opciones" role="group">\n{btn}\n</div><div aria-live="polite" class="respuesta-int" role="status"></div></div>')
    return "\n".join(out), datos


PIE = {
    "en": '<p>José M. Fernández, ABE/ASE Math Master Teacher, Harry S. Truman College — City Colleges of Chicago</p><p class="licencia">© 2026. This work is licensed under <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/" rel="license" target="_blank">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)</a>.</p><p class="licencia">GED® is a registered trademark of the American Council on Education (ACE) and administered exclusively by GED Testing Service LLC under license. LearnGED is not affiliated with, endorsed by, or approved by ACE or GED Testing Service.</p>',
    "es": '<p>José M. Fernández, ABE/ASE Math Master Teacher, Harry S. Truman College — City Colleges of Chicago</p><p class="licencia">© 2026. Esta obra está bajo una licencia <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/deed.es" rel="license" target="_blank">Creative Commons Atribución-NoComercial-CompartirIgual 4.0 Internacional (CC BY-NC-SA 4.0)</a>.</p><p class="licencia">GED® es una marca registrada del American Council on Education (ACE), administrada exclusivamente por GED Testing Service LLC bajo licencia. LearnGED no está afiliado a ACE ni a GED Testing Service, ni cuenta con su respaldo o aprobación.</p>',
}


def barra():
    return (f'<nav class="lg-bar" aria-label="LearnGED"><a class="lg-logo" href="{t("/", "/es/")}"><img src="/img/learnged-logo-horizontal.svg" alt="{t("LearnGED home", "Inicio de LearnGED")}" height="34"></a>'
            f'<a class="lg-link" href="./">{materia()} · {t("all lessons", "todas las lecciones")}</a></nav>')


# ---------------------------------------------------------------- la página de la lección
def pagina_leccion(n, titulo, lema, sp_chips, objetivos, estd, conexion, secciones, tarea, quiz_items, lista_filas,
                   cierre, siguiente, glosario, practicas, calculadora=False):
    """secciones: lista de (id, título, html). tarea: lista de (negrita, texto). siguiente: (n, título) o (None, texto)."""
    tn = int(n.split("-")[0])
    area = TEMAS[tn][1]
    num = n.replace("-", ".")
    idx = "\n".join(f'<li><a href="#{sid}">{tt}</a></li>' for sid, tt, _ in secciones)
    cuerpo = "\n\n".join(seccion(sid, i + 1, tt, h) for i, (sid, tt, h) in enumerate(secciones))
    k = len(secciones)
    ns, ntxt = siguiente
    if ns:
        nom = f'{t("Lesson", "Lección")} {ns.replace("-", ".")} · {ntxt}'
        sig = f'{t("Next", "Siguiente")}: <a href="{lec(ns)}">{nom}</a>' if existe(ns) else f'{t("Next", "Siguiente")}: {nom}'
    else:
        sig = ntxt
    objs = "\n".join(f"<li>{o}</li>" for o in objetivos)
    filas = "\n".join(f'<tr><th scope="row">{a}</th><td>{b}</td><td>{c}</td><td>{d}</td></tr>' for a, b, c, d in lista_filas)
    glos = "\n".join(f"<dt>{a}</dt><dd>{b}</dd>" for a, b in glosario)
    qh, qd = quiz_html(quiz_items)
    nq = len(quiz_items)
    tareas = "\n".join(f"<li><strong>{a}</strong> {b}</li>" for a, b in tarea)
    chips = "".join(f'<span class="chip chip-sp">{c}</span>' for c in sp_chips)
    lesson = {"practice": practicas.datos, "quiz": qd, "next": (f'{t("Lesson", "Lección")} {ns.replace("-", ".")}' if ns else ""),
              "review": t("the lesson", "la lección")}
    calc = '\n<script src="%s" data-color="%s" defer></script>' % (t("/js/calculator.js", "/js/calculadora.js"), COLOR[area]) if calculadora else ""
    return f'''<!DOCTYPE html>
<!-- LearnGED · {materia()} · {t("Lesson", "Lección")} {num} ({t("English", "español")}) — {t("built by", "construida con")} tools/{MAT["builder"]}{n.replace("-", "_")}.py
     José M. Fernández · CC BY-NC-SA 4.0 -->
<html lang="{L}">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>{t("Lesson", "Lección")} {num} · {re.sub("<[^>]+>", "", titulo)} · LearnGED</title>
<meta content="CC BY-NC-SA 4.0" name="license"/><link href="https://creativecommons.org/licenses/by-nc-sa/4.0/" rel="license"/>
<link rel="icon" href="/favicon.svg" type="image/svg+xml"/>
<link rel="alternate" hreflang="{t("es", "en")}" href="/{carpeta("es" if L == "en" else "en")}/{lec(n, "es" if L == "en" else "en")}"/>
<link rel="stylesheet" href="/math/lesson.css">
{"".join('<link rel="stylesheet" href="' + x + '">' for x in MAT["css"])}
</head>
<body data-area="{area}">
{barra()}
<a class="saltar" href="#indice">{t("Skip to the lesson contents", "Saltar al contenido de la lección")}</a>
<header class="principal">
<div class="envoltura-header">
<p class="ruta">{materia()} · {t("Topic", "Tema")} {tn} — {tema(tn)}</p>
<h1>{t("Lesson", "Lección")} {num} · {titulo}</h1>
<p class="lema">{lema}</p>
<div class="chips">
<span class="chip"><span aria-hidden="true">⏱️</span> {t("About 4 hours with practice and homework · take breaks", "Unas 4 horas con la práctica y la tarea · tome descansos")}</span>
{chips}
</div>
</div>
</header>
<div class="envoltura">
<section>
<div class="caja caja-objetivo">
<h2><span aria-hidden="true" class="num-seccion">🎯</span>{t("What you will learn", "Lo que va a aprender")}</h2>
<p>{t("When you finish this lesson, you will be able to:", "Al terminar esta lección, usted podrá:")}</p>
<ul>
{objs}
</ul>
</div>
{estd}
</section>
<nav aria-labelledby="indice-titulo" class="indice" id="indice"><h2 id="indice-titulo">{t("Lesson contents", "Contenido de la lección")}</h2><ol>
{idx}
<li><a href="#s-tarea">{t("Homework", "Tarea")}</a></li>
<li><a href="#s-quiz">{t("Practice quiz", "Quiz de práctica")}</a></li>
<li><a href="#s-lista">{t("Self-check checklist", "Lista de autoevaluación")}</a></li>
<li><a href="#s-sigue">{t("Coming next", "Lo que viene")}</a></li>
<li><a href="#s-palabras">{t("Key words", "Palabras clave")}</a></li>
</ol></nav>

<div class="caja caja-tip"><span class="etiqueta et-verde">{t("Before you start", "Antes de empezar")}</span>
{conexion}
</div>

{cuerpo}

<section>
<h2 id="s-tarea"><span aria-hidden="true" class="num-seccion">{k + 1}</span>{t("Homework", "Tarea")}</h2>
<p>{t("This is independent practice. Plan for about one hour, with your notebook open.", "Es práctica independiente. Calcule una hora, con el cuaderno abierto.")}</p>
<ul class="lista-tarea">
<li><strong>{t("The practice page.", "La página de práctica.")}</strong> {t(f'Open the <a href="{prac(n)}">practice page for this lesson</a> and do each activity. The exercises come in a new order every time. Keep going until you get 8 out of 10 right on the first try. The score under each activity keeps count for you.', f'Abra la <a href="{prac(n)}">página de práctica de esta lección</a> y haga cada actividad. Los ejercicios salen en un orden distinto cada vez. Siga hasta acertar 8 de cada 10 al primer intento. El marcador de cada actividad lleva la cuenta.')}</li>
{tareas}
</ul>
</section>

<section>
<h2 id="s-quiz"><span aria-hidden="true" class="num-seccion">{k + 2}</span>{t("Practice quiz", "Quiz de práctica")}</h2>
<p>{t(f"Answer the <strong>{nq} questions</strong> and press <strong>Check my answers</strong>. If an answer is not right, you will get a hint and a second try. After the second try, you will see the solution. You can take the quiz as many times as you want.", f"Responda las <strong>{nq} preguntas</strong> y pulse <strong>Revisar mis respuestas</strong>. Si una respuesta no es correcta, recibirá una pista y un segundo intento. Después del segundo intento verá la solución. Puede hacer el quiz las veces que quiera.")}</p>
<div id="quiz">
{qh}
</div>
<p style="text-align:center;margin-top:18px;">
<button class="btn" id="btn-calificar" type="button">{t("Check my answers", "Revisar mis respuestas")}</button>
<button class="btn btn-sec" id="btn-reintentar" style="display:none;" type="button">{t("Start the quiz again", "Empezar el quiz otra vez")}</button>
</p>
<div aria-live="polite" class="marcador" id="marcador" role="status">
<div aria-hidden="true" class="barra-prog"><span id="barra"></span></div>
<p class="puntaje" id="puntaje"></p>
<p class="mensaje" id="mensaje"></p>
</div>
</section>

<section>
<h2 id="s-lista"><span aria-hidden="true" class="num-seccion">{k + 3}</span>{t("Self-check checklist", "Lista de autoevaluación")}</h2>
<p>{t("Use this checklist to see how you are doing. For each skill, choose <strong>Got it</strong>, <strong>Getting there</strong>, or <strong>Needs more practice</strong>. Read it <strong>before</strong> you start the homework. Use it <strong>after</strong> to check your own work honestly.", "Use esta lista para ver cómo va. En cada destreza, elija <strong>Lo domino</strong>, <strong>Voy avanzando</strong> o <strong>Necesito más práctica</strong>. Léala <strong>antes</strong> de empezar la tarea y úsela <strong>después</strong> para revisar su trabajo con honestidad.")}</p>
<div aria-label="{t("Self-check checklist (table you can scroll sideways)", "Lista de autoevaluación (tabla desplazable horizontalmente)")}" class="tabla-scroll" role="region" tabindex="0">
<table class="tabla-rubrica">
<caption class="cap-oculto">{t("Skills of this lesson and what Got it, Getting there, and Needs more practice look like", "Destrezas de la lección y cómo se ve cada nivel: lo domino, voy avanzando y necesito más práctica")}</caption>
<thead><tr><th scope="col">{t("Skill", "Destreza")}</th><th class="nivel-cab" scope="col">{t("Got it", "Lo domino")}</th><th class="nivel-cab" scope="col">{t("Getting there", "Voy avanzando")}</th><th class="nivel-cab" scope="col">{t("Needs more practice", "Necesito más práctica")}</th></tr></thead>
<tbody>
{filas}
</tbody>
</table>
</div>
<p class="aviso-desliza"><span aria-hidden="true">↔</span> {t("Slide the table sideways to see all the columns.", "Deslice la tabla horizontalmente para ver todas las columnas.")}</p>
</section>

<section class="cierre">
<h2 id="s-sigue"><span aria-hidden="true" class="num-seccion">➡️</span>{t("Coming next", "Lo que viene")}</h2>
{cierre}
<p class="flecha-sig"><span aria-hidden="true">➡️</span> {sig}</p>
</section>

<section>
<h2 id="s-palabras"><span aria-hidden="true" class="num-seccion">📘</span>{t("Key words", "Palabras clave")}</h2>
<dl class="glosario">
{glos}
</dl>
</section>
</div>
<footer><p>LearnGED · {materia()} · {t("Topic", "Tema")} {tn} · {t("Lesson", "Lección")} {num}</p>{PIE[L]}</footer>
<script>
window.LESSON = {json.dumps(lesson, ensure_ascii=False, indent=1)};
</script>
<script src="/math/lesson.js"></script>{calc}
</body>
</html>
'''


# ---------------------------------------------------------------- la página de práctica
def modulo(mid, num, titulo, cuerpo, abierto=False):
    return f'''  <details class="modulo" id="{mid}"{" open" if abierto else ""}>
    <summary><span class="num" aria-hidden="true">{num}</span><h2>{titulo}</h2><span class="chev" aria-hidden="true">›</span></summary>
    <div class="cuerpo">
{cuerpo}
      <a class="volver" href="#titulo-indice">↑ {t("Back to contents", "Volver al índice")}</a>
    </div>
  </details>'''


def _botones(pid, comprobar=None):
    c = f'<button type="button" class="btn" id="{pid}-comprobar">{comprobar or t("Check", "Comprobar")}</button>\n          ' if comprobar is not False else ""
    return f'''        <div class="fila-btn">
          {c}<button type="button" class="btn-sec" id="{pid}-nuevo">{t("New exercise", "Otro ejercicio")}</button>
        </div>
        <div class="fb" id="{pid}-fb" role="status"></div>
        <p class="marcador" id="{pid}-marcador"></p>'''


def om(pid, intro=""):
    """Opción múltiple de un banco (creaBanco)."""
    i = f"      <p>{intro}</p>\n" if intro else ""
    return f'''{i}      <div class="practica" id="{pid}">
        <div class="enun" id="{pid}-enun"></div>
        <div class="opciones" id="{pid}-opciones"></div>
{_botones(pid, False)}
      </div>'''


def orden(pid, intro=""):
    i = f"      <p>{intro}</p>\n" if intro else ""
    return f'''{i}      <div class="practica" id="{pid}">
        <div class="enun" id="{pid}-enun"></div>
        <ol class="lista-orden" id="{pid}-lista"></ol>
        <p class="cap-oculto" aria-live="polite" id="{pid}-voz"></p>
{_botones(pid, t("Check the order", "Comprobar el orden"))}
      </div>'''


def clasifica(pid, intro=""):
    i = f"      <p>{intro}</p>\n" if intro else ""
    return f'''{i}      <div class="practica" id="{pid}">
        <div class="enun" id="{pid}-enun"></div>
        <div id="{pid}-piezas"></div>
{_botones(pid)}
      </div>'''


def huecos(pid, intro=""):
    i = f"      <p>{intro}</p>\n" if intro else ""
    return f'''{i}      <div class="practica" id="{pid}">
        <div class="enun" id="{pid}-enun"></div>
{_botones(pid)}
      </div>'''


def pagina_practica(n, titulo, meta, modulos, js, scripts=(), calculadora=False):
    """modulos: lista de (id, título, html). js: el código de la página (después de practice.js y sci.js)."""
    tn = int(n.split("-")[0])
    area = TEMAS[tn][1]
    num = n.replace("-", ".")
    idx = "\n".join(f'      <li><a href="#{mid}">{tt}</a></li>' for mid, tt, _ in modulos)
    mods = "\n\n".join(modulo(mid, i + 1, tt, h, i == 0) for i, (mid, tt, h) in enumerate(modulos))
    ruta = f'{materia()} · {t("Topic", "Tema")} {tn} · {tema(tn)}'
    otra = "es" if L == "en" else "en"
    calc = '\n<script src="%s" data-color="%s" defer></script>' % (t("/js/calculator.js", "/js/calculadora.js"), COLOR[area]) if calculadora else ""
    return f'''<!DOCTYPE html>
<!-- LearnGED · {materia()} · {t("Lesson", "Lección")} {num} · {t("practice", "práctica")} ({t("English", "español")}) — {t("built by", "construida con")} tools/{MAT["builder"]}{n.replace("-", "_")}.py
     José M. Fernández · CC BY-NC-SA 4.0 -->
<html lang="{L}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{t("Practice · Lesson", "Práctica · Lección")} {num} · {re.sub("<[^>]+>", "", titulo)} · LearnGED</title>
<meta name="license" content="CC BY-NC-SA 4.0"><link rel="license" href="https://creativecommons.org/licenses/by-nc-sa/4.0/">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="alternate" hreflang="{otra}" href="/{carpeta(otra)}/{prac(n, otra)}">
<link rel="stylesheet" href="/math/practice.css">
{"".join('<link rel="stylesheet" href="' + x + '">' for x in MAT["css"])}
</head>
<body data-area="{area}">
{barra()}
<a class="saltar" href="#titulo-indice">{t("Skip to contents", "Saltar al índice")}</a>
<div class="contenedor">
  <header class="principal">
    <div class="ruta">{ruta}</div>
    <h1>{t("Practice", "Práctica")} · {t("Lesson", "Lección")} {num} · {titulo}</h1>
    <div class="meta">{meta}</div>
  </header>
  <nav class="indice" aria-labelledby="titulo-indice">
    <h2 id="titulo-indice">{t("On this page", "En esta página")}</h2>
    <ol>
{idx}
    </ol>
    <div class="controles-todo">
      <button type="button" class="btn-sec" id="abrir-todo">{t("Open all", "Abrir todo")}</button>
      <button type="button" class="btn-sec" id="cerrar-todo">{t("Close all", "Cerrar todo")}</button>
    </div>
  </nav>

{mods}

  <footer class="pie">
    <p><strong>{ruta} · LearnGED</strong><br>
    <a href="{lec(n)}">{t("Back to the lesson", "Volver a la lección")} {num}</a></p>
    {PIE[L]}
  </footer>
</div>
<script src="/math/practice.js"></script>
<script src="/science/sci.js"></script>{"".join(chr(10) + '<script src="' + x + '"></script>' for x in scripts)}
<script>
{js.strip()}
iniciaNavegacion();
</script>{calc}
</body>
</html>
'''


def js_datos(nombre, valor):
    return f"var {nombre} = {json.dumps(valor, ensure_ascii=False, indent=1)};\n"


# ---------------------------------------------------------------- escribir las cuatro páginas
def construye(n, hacer_leccion, hacer_practica):
    global L
    for lang in ("en", "es"):
        L = lang
        os.makedirs(os.path.join(ROOT, carpeta()), exist_ok=True)
        for nombre, f in ((lec(n), hacer_leccion), (prac(n), hacer_practica)):
            ruta = os.path.join(ROOT, carpeta(), nombre)
            open(ruta, "w", encoding="utf-8").write(f())
            print("ok", os.path.relpath(ruta, ROOT))
    L = "en"


# ---------------------------------------------------------------- gráficas en SVG (líneas, barras, tablas)
PALETA = ["#1f6066", "#c0582f", "#5b21b6", "#2e7d32"]


def _paso(rango):
    """Un paso «bonito» (1, 2, 2.5, 5 × 10^k) para unas 5 divisiones."""
    import math
    if rango <= 0:
        return 1
    bruto = rango / 5
    k = 10 ** math.floor(math.log10(bruto))
    for m in (1, 2, 2.5, 5, 10):
        if bruto <= m * k:
            return m * k
    return 10 * k


def _fmt(v):
    v = round(v, 6)
    s = (f"{v:,.6f}" if abs(v) >= 10000 else f"{v:.6f}").rstrip("0").rstrip(".")
    return s.replace("-", "−")


def grafica(spec, aria, ancho=560, alto=320, y0=None, y1=None):
    """spec: {"tipo": "linea", "xEtq", "yEtq", "series": [{"nombre", "puntos": [[x, y], ...]}]}
             {"tipo": "barras", "xEtq", "yEtq", "barras": [{"etq", "valor"}]}
             {"tipo": "tabla", "encabezados": [...], "filas": [[...]]}
    aria: descripción completa para lectores de pantalla (con los datos)."""
    import math
    if spec["tipo"] == "tabla":
        th = "".join(f'<th scope="col">{c}</th>' for c in spec["encabezados"])
        tr = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in f) + "</tr>" for f in spec["filas"])
        return f'<table class="cuaderno"><caption class="cap-oculto">{aria}</caption><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table>'
    ml, mr, mt, mb = 66, 18, 16, 58
    W, Hh = ancho - ml - mr, alto - mt - mb
    if spec["tipo"] in ("linea", "puntos"):
        xs = [p[0] for s in spec["series"] for p in s["puntos"]]
        ys = [p[1] for s in spec["series"] for p in s["puntos"]]
        xmin, xmax = min(xs), max(xs)
    else:
        ys = [b["valor"] for b in spec["barras"]]
    ymin = min(0, min(ys)) if y0 is None else y0
    ymax = max(ys) if y1 is None else y1
    py = spec.get("py") or _paso(ymax - ymin)
    ymin = math.floor(ymin / py) * py
    ymax = math.ceil(ymax / py) * py
    if ymax == ymin:
        ymax = ymin + py
    Y = lambda v: mt + Hh - (v - ymin) / (ymax - ymin) * Hh
    g = []
    v = ymin
    while v <= ymax + 1e-9:
        g.append(f'<line x1="{ml}" y1="{Y(v):.1f}" x2="{ml + W}" y2="{Y(v):.1f}" stroke="#e1e6ea"/>'
                 f'<text x="{ml - 8}" y="{Y(v) + 5:.1f}" text-anchor="end" font-size="13" fill="#3d4753">{_fmt(v)}</text>')
        v += py
    g.append(f'<line x1="{ml}" y1="{mt}" x2="{ml}" y2="{mt + Hh}" stroke="#1a2330" stroke-width="1.5"/>')
    base = Y(max(ymin, min(0, ymax))) if ymin <= 0 <= ymax else mt + Hh
    g.append(f'<line x1="{ml}" y1="{base:.1f}" x2="{ml + W}" y2="{base:.1f}" stroke="#1a2330" stroke-width="1.5"/>')
    if spec["tipo"] in ("linea", "puntos"):
        px = spec.get("px") or _paso(xmax - xmin)
        xa, xb = math.floor(xmin / px) * px, math.ceil(xmax / px) * px
        X = lambda v: ml + (v - xa) / (xb - xa) * W
        v = xa
        while v <= xb + 1e-9:
            g.append(f'<text x="{X(v):.1f}" y="{mt + Hh + 20}" text-anchor="middle" font-size="13" fill="#3d4753">{_fmt(v)}</text>'
                     f'<line x1="{X(v):.1f}" y1="{mt + Hh}" x2="{X(v):.1f}" y2="{mt + Hh + 5}" stroke="#1a2330"/>')
            v += px
        for i, s in enumerate(spec["series"]):
            c = PALETA[i % len(PALETA)]
            pts = " ".join(f"{X(x):.1f},{Y(y):.1f}" for x, y in s["puntos"])
            dash = ' stroke-dasharray="7 4"' if i == 1 else (' stroke-dasharray="2 4"' if i == 2 else "")
            if spec["tipo"] == "linea":
                g.append(f'<polyline points="{pts}" fill="none" stroke="{c}" stroke-width="3"{dash}/>')
            forma = ["circle", "rect", "diamond"][i % 3]
            for x, y in s["puntos"]:
                if forma == "circle":
                    g.append(f'<circle cx="{X(x):.1f}" cy="{Y(y):.1f}" r="4.5" fill="{c}"/>')
                elif forma == "rect":
                    g.append(f'<rect x="{X(x) - 4.5:.1f}" y="{Y(y) - 4.5:.1f}" width="9" height="9" fill="{c}"/>')
                else:
                    g.append(f'<path d="M{X(x):.1f} {Y(y) - 6:.1f} l6 6 l-6 6 l-6 -6z" fill="{c}"/>')
        if len(spec["series"]) > 1:
            for i, s in enumerate(spec["series"]):
                c = PALETA[i % len(PALETA)]
                yy = mt + 8 + i * 20
                g.append(f'<line x1="{ml + 14}" y1="{yy}" x2="{ml + 40}" y2="{yy}" stroke="{c}" stroke-width="3"{" stroke-dasharray=\"7 4\"" if i == 1 else (" stroke-dasharray=\"2 4\"" if i == 2 else "")}/>'
                         f'<text x="{ml + 46}" y="{yy + 5}" font-size="13" font-weight="700" fill="{c}">{s["nombre"]}</text>')
    else:
        n = len(spec["barras"])
        bw = W / n
        for i, b in enumerate(spec["barras"]):
            x = ml + i * bw + bw * 0.18
            g.append(f'<rect x="{x:.1f}" y="{Y(b["valor"]):.1f}" width="{bw * 0.64:.1f}" height="{Y(ymin) - Y(b["valor"]):.1f}" fill="{PALETA[0]}"/>'
                     f'<text x="{x + bw * 0.32:.1f}" y="{Y(b["valor"]) - 6:.1f}" text-anchor="middle" font-size="12" font-weight="700" fill="#1a2330">{_fmt(b["valor"])}</text>'
                     f'<text x="{x + bw * 0.32:.1f}" y="{mt + Hh + 18}" text-anchor="middle" font-size="{12 if n > 6 else 13}" fill="#3d4753">{b["etq"]}</text>')
    g.append(f'<text x="{ml + W / 2:.1f}" y="{alto - 8}" text-anchor="middle" font-size="14" font-weight="700" fill="#1a2330">{spec["xEtq"]}</text>'
             f'<text x="16" y="{mt + Hh / 2:.1f}" text-anchor="middle" font-size="14" font-weight="700" fill="#1a2330" transform="rotate(-90 16 {mt + Hh / 2:.1f})">{spec["yEtq"]}</text>')
    return f'<svg viewBox="0 0 {ancho} {alto}" role="img" aria-label="{H.escape(aria)}" style="width:100%;max-width:{ancho}px;height:auto;display:block;margin:10px auto;">{"".join(g)}</svg>'


def describe(spec):
    """Texto alternativo automático: tipo, ejes y todos los datos."""
    if spec["tipo"] == "puntos":
        return t(f'Scatter plot. Horizontal axis: {spec["xEtq"]}. Vertical axis: {spec["yEtq"]}. ', f'Gráfica de dispersión. Eje horizontal: {spec["xEtq"]}. Eje vertical: {spec["yEtq"]}. ') + spec.get("patron", "")
    if spec["tipo"] == "linea":
        partes = []
        for s in spec["series"]:
            partes.append(f'{s["nombre"]}: ' + "; ".join(f"{_fmt(x)}, {_fmt(y)}" for x, y in s["puntos"]))
        return t(f'Line graph. Horizontal axis: {spec["xEtq"]}. Vertical axis: {spec["yEtq"]}. Data points (x, y): ', f'Gráfica de líneas. Eje horizontal: {spec["xEtq"]}. Eje vertical: {spec["yEtq"]}. Puntos (x, y): ') + ". ".join(partes) + "."
    if spec["tipo"] == "barras":
        return t(f'Bar graph. Horizontal axis: {spec["xEtq"]}. Vertical axis: {spec["yEtq"]}. Values: ', f'Gráfica de barras. Eje horizontal: {spec["xEtq"]}. Eje vertical: {spec["yEtq"]}. Valores: ') + "; ".join(f'{b["etq"]}, {_fmt(b["valor"])}' for b in spec["barras"]) + "."
    return t("Data table.", "Tabla de datos.")


def svg_orig(nombre, trad, aria_en, ancho=700):
    """Diagrama SVG tomado de clases_ciencias (copiado en tools/svg). En inglés se traducen los rótulos
    (trad: {"texto en español": "English text"}) y la descripción para lectores de pantalla."""
    import re as _re
    s = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg", nombre + ".svg"), encoding="utf-8").read()
    s = _re.sub(r'<svg([^>]*?) width="\d+" height="\d+"', r'<svg\1', s, count=1)
    s = s.replace("<svg", f'<svg style="width:100%;max-width:{ancho}px;height:auto;display:block;margin:12px auto;"', 1)
    if L == "en":
        s = _re.sub(r'aria-label="[^"]*"', 'aria-label="' + aria_en.replace('"', "&quot;") + '"', s, count=1)
        def rep(m):
            txt = m.group(2)
            if txt.strip() not in trad:
                raise KeyError("svg " + nombre + ": falta traducir «" + txt.strip() + "»")
            return m.group(1) + txt.replace(txt.strip(), trad[txt.strip()]) + m.group(3)
        s = _re.sub(r'(<(?:text|tspan)[^>]*>)([^<]*[^\s<0-9][^<]*)(</(?:text|tspan)>)', rep, s)
    return s
