"""Herramientas para construir las lecciones de Estudios Sociales de LearnGED (EN/ES).

Usa el mismo marco que Ciencias (tools/ciencia.py): t("inglés", "español"), Practicas, tabla, caja,
ejemplo, pagina_leccion, pagina_practica, om, clasifica, orden, huecos, grafica... Este módulo solo
cambia la materia (carpetas, nombres, colores), los temas del curso y los estándares (prácticas de
estudios sociales SSP y temas de contenido del GED), y añade las piezas propias de la materia:
el documento con su ficha y su original plegado.

Cada constructor (tools/build_soc_T_N.py) hace:
    from sociales import C, t
y llama a C.construye(N, leccion, practica). Salen cuatro páginas:

  social-studies/lesson-T-N.html        social-studies/practice-T-N.html     (inglés)
  es/estudios-sociales/leccion-T-N.html es/estudios-sociales/practica-T-N.html (español)

Después de construir, ejecute tools/build_planes.py (índice del curso) y tools/build_portada.py.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ciencia as C
from ciencia import t

C.MAT.update({"nombre": ("Social studies", "Estudios sociales"), "carpeta": ("social-studies", "es/estudios-sociales"),
              "builder": "build_soc_", "css": ["/science/science.css", "/social-studies/social.css"], "icono": "🗂️"})

# ---------------------------------------------------------------- temas y áreas
C.TEMAS = {
    1: (("Inquiry, sources, and analytical literacy", "Indagación, fuentes y alfabetización analítica"), "tools"),
    2: (("Quantitative reasoning in social studies", "Razonamiento cuantitativo en estudios sociales"), "tools"),
    3: (("Civics I: founding documents and constitutional principles", "Cívica I: documentos fundacionales y principios constitucionales"), "civics"),
    4: (("Civics II: the three branches and policymaking", "Cívica II: las tres ramas y la formación de políticas"), "civics"),
    5: (("Citizenship in action: rights, elections, and public finance", "Ciudadanía en acción: derechos, elecciones y finanzas públicas"), "civics"),
    6: (("U.S. history: cause and change", "Historia de los Estados Unidos: causalidad y cambio"), "history"),
    7: (("Economics and geography of a connected world", "Economía y geografía del mundo conectado"), "economics"),
    8: (("Putting it together: multiple-source scenarios and GED preparation", "Integración, escenarios de varias fuentes y preparación para el GED"), "ged"),
}
C.COLOR = {"tools": "#7a4a2e", "civics": "#283593", "history": "#9c3d1c", "economics": "#2e6b30", "ged": "#5e3591"}

# ---------------------------------------------------------------- estándares
# GED Testing Service, Assessment Guide for Educators: Social Studies (prácticas de estudios sociales).
SSP = {
    "SSP.1.a": ("Determine the details of what is explicitly stated in primary and secondary sources and make logical inferences or valid claims based on evidence.",
                "Determinar los detalles de lo que dicen explícitamente las fuentes primarias y secundarias, y hacer inferencias lógicas o afirmaciones válidas basadas en la evidencia."),
    "SSP.1.b": ("Cite or identify specific evidence to support inferences or analyses of primary and secondary sources, attending to the precise details of explanations or descriptions of a process, event, or concept.",
                "Citar o identificar evidencia concreta que apoye las inferencias o los análisis de fuentes primarias y secundarias, atendiendo a los detalles precisos de un proceso, un hecho o un concepto."),
    "SSP.2.a": ("Determine the central ideas or information of a primary or secondary source document, corroborating or challenging conclusions with evidence.",
                "Determinar las ideas centrales o la información esencial de una fuente primaria o secundaria, y confirmar o refutar conclusiones con evidencia."),
    "SSP.2.b": ("Describe people, places, environments, processes, and events, and the connections between and among them.",
                "Describir personas, lugares, entornos, procesos y hechos, y las conexiones que hay entre ellos."),
    "SSP.3.a": ("Identify the chronological structure of a historical narrative and sequence steps in a process.",
                "Identificar la estructura cronológica de un relato histórico y ordenar los pasos de un proceso."),
    "SSP.3.b": ("Analyze in detail how events, processes, and ideas develop and interact in a written document; determine whether earlier events caused later ones or simply preceded them.",
                "Analizar en detalle cómo se desarrollan y se relacionan los hechos, los procesos y las ideas en un documento; decidir si un hecho anterior causó otro posterior o solo lo precedió."),
    "SSP.3.c": ("Analyze cause and effect relationships and multiple causation, including action by individuals, natural and societal processes, and the influence of ideas.",
                "Analizar relaciones de causa y efecto y la causalidad múltiple: la acción de las personas, los procesos naturales y sociales, y la influencia de las ideas."),
    "SSP.3.d": ("Compare differing sets of ideas related to political, historical, economic, geographic, or societal contexts; evaluate the assumptions and implications inherent in differing positions.",
                "Comparar ideas distintas sobre un contexto político, histórico, económico, geográfico o social; evaluar los supuestos y las consecuencias de cada posición."),
    "SSP.4.a": ("Determine the meaning of words and phrases as they are used in a text, including vocabulary describing political, social, geographic, and economic aspects of social studies.",
                "Determinar el significado de palabras y frases tal como se usan en un texto, incluido el vocabulario político, social, geográfico y económico."),
    "SSP.5.a": ("Identify aspects of a historical document that reveal the author's point of view or purpose (e.g., loaded language, inclusion or avoidance of particular facts).",
                "Identificar los rasgos de un documento histórico que revelan el punto de vista o el propósito del autor (por ejemplo, el lenguaje cargado o los hechos que incluye u omite)."),
    "SSP.5.b": ("Identify instances of bias or propagandizing.", "Identificar casos de sesgo o de propaganda."),
    "SSP.5.c": ("Analyze how a historical context shapes an author's point of view.", "Analizar cómo el contexto histórico da forma al punto de vista de un autor."),
    "SSP.5.d": ("Evaluate the credibility of an author in historical and contemporary political discourse.", "Evaluar la credibilidad de un autor en el discurso político, histórico y actual."),
    "SSP.6.a": ("Integrate quantitative or technical analysis (e.g., charts, research data) with qualitative analysis in print or digital text.",
                "Integrar el análisis cuantitativo o técnico (gráficas, datos de investigación) con el análisis cualitativo de un texto impreso o digital."),
    "SSP.6.b": ("Analyze information presented in a variety of maps, graphic organizers, tables, and charts, and in a variety of visual sources such as artifacts, photographs, and political cartoons.",
                "Analizar la información de mapas, organizadores gráficos, tablas y gráficas, y de fuentes visuales como objetos, fotografías y caricaturas políticas."),
    "SSP.6.c": ("Translate quantitative information expressed in words in a text into visual form (e.g., table or chart); translate information expressed visually or mathematically into words.",
                "Pasar a forma visual (tabla o gráfica) la información numérica que un texto da con palabras, y pasar a palabras la información que se da de forma visual o matemática."),
    "SSP.7.a": ("Distinguish among fact, opinion, and reasoned judgment in a primary or secondary source.", "Distinguir entre hecho, opinión y juicio razonado en una fuente primaria o secundaria."),
    "SSP.7.b": ("Distinguish between unsupported claims and informed hypotheses grounded in social studies evidence.", "Distinguir entre las afirmaciones sin respaldo y las hipótesis informadas que se apoyan en evidencia de los estudios sociales."),
    "SSP.8.a": ("Compare treatment of the same social studies topic in various primary and secondary sources, noting discrepancies between and among the sources.",
                "Comparar cómo tratan el mismo tema varias fuentes primarias y secundarias, y señalar en qué no coinciden."),
    "SSP.10.a": ("Interpret, use, and create graphs (e.g., scatterplot, line, bar, circle), including predicting trends within reasonable limits.",
                 "Interpretar, usar y elaborar gráficas (de dispersión, de líneas, de barras, circulares), incluida la predicción de tendencias dentro de límites razonables."),
    "SSP.10.b": ("Represent data on two variables (dependent and independent) on a graph; analyze and communicate how the variables are related.",
                 "Representar en una gráfica datos de dos variables (dependiente e independiente); analizar y explicar cómo se relacionan."),
    "SSP.10.c": ("Distinguish between correlation and causation.", "Distinguir entre correlación y causalidad."),
    "SSP.11.a": ("Use mean, median, mode, and range to describe a set of data.", "Usar la media, la mediana, la moda y el rango para describir un conjunto de datos."),
}
# Rango de DOK y estándares alineados de cada indicador (misma guía).
ALIN = {
    "SSP.1.a": ("2–3", ["R1", "R8"]), "SSP.1.b": ("1–3", ["R1", "R8"]),
    "SSP.2.a": ("1–3", ["R2"]), "SSP.2.b": ("2–3", ["R2"]),
    "SSP.3.a": ("1–2", ["R3"]), "SSP.3.b": ("2–3", ["R3", "R8"]), "SSP.3.c": ("2–3", ["R3", "R8"]), "SSP.3.d": ("2–3", ["R3", "R8"]),
    "SSP.4.a": ("1–3", ["R4", "L4"]),
    "SSP.5.a": ("2", ["R6", "NSH"]), "SSP.5.b": ("2–3", ["R6", "NSH"]), "SSP.5.c": ("2–3", ["R6", "NSH"]), "SSP.5.d": ("2–3", ["R6", "NSH"]),
    "SSP.6.a": ("2–3", ["R7", "R9", "S-ID"]), "SSP.6.b": ("2–3", ["R7", "R9"]), "SSP.6.c": ("1–3", ["R7", "7.RP", "3.MD"]),
    "SSP.7.a": ("2–3", ["R8", "NSH"]), "SSP.7.b": ("2–3", ["R8", "NSH"]),
    "SSP.8.a": ("2–3", ["R9", "R7"]),
    "SSP.10.a": ("2–3", ["7.RP", "3.MD", "8.SP", "S-ID"]), "SSP.10.b": ("2–3", ["8.SP", "S-ID"]), "SSP.10.c": ("1–3", ["S-ID"]),
    "SSP.11.a": ("1", ["6.SP", "S-ID"]),
}
NOMBRE_SSP = {
    "SSP.1": ("Drawing conclusions and making inferences", "Sacar conclusiones y hacer inferencias"),
    "SSP.2": ("Determining central ideas, hypotheses, and conclusions", "Determinar ideas centrales, hipótesis y conclusiones"),
    "SSP.3": ("Analyzing events and ideas", "Analizar hechos e ideas"),
    "SSP.4": ("Interpreting meaning of symbols, words, and phrases", "Interpretar el significado de símbolos, palabras y frases"),
    "SSP.5": ("Analyzing purpose and point of view", "Analizar el propósito y el punto de vista"),
    "SSP.6": ("Integrating content presented in different ways", "Integrar contenido presentado de distintas formas"),
    "SSP.7": ("Evaluating reasoning and evidence", "Evaluar el razonamiento y la evidencia"),
    "SSP.8": ("Analyzing relationships between texts", "Analizar las relaciones entre textos"),
    "SSP.10": ("Reading and interpreting graphs and charts", "Leer e interpretar gráficas y tablas"),
    "SSP.11": ("Measuring the center of a statistical data set", "Medir el centro de un conjunto de datos"),
}
# Temas de contenido de la misma guía. Cada pregunta del examen combina una práctica y uno de estos temas.
CT = {
    "CG.a": ("Types of modern and historical governments", "Tipos de gobierno, modernos e históricos"),
    "CG.b": ("Principles that have contributed to the development of American constitutional democracy", "Principios que dieron forma a la democracia constitucional estadounidense"),
    "CG.c": ("Structure and design of the United States government", "Estructura y diseño del gobierno de los Estados Unidos"),
    "CG.d": ("Individual rights and civic responsibilities", "Derechos individuales y responsabilidades cívicas"),
    "CG.e": ("Political parties, campaigns, and elections in American politics", "Partidos políticos, campañas y elecciones"),
    "CG.f": ("Contemporary public policy", "Políticas públicas actuales"),
    "USH.a": ("Key historical documents that have shaped American constitutional government", "Documentos históricos clave del gobierno constitucional estadounidense"),
    "USH.b": ("Revolutionary and Early Republic periods", "La Revolución y los primeros años de la república"),
    "USH.c": ("Civil War and Reconstruction", "La Guerra Civil y la Reconstrucción"),
    "USH.d": ("Civil rights", "Los derechos civiles"),
    "USH.e": ("European settlement and population of the Americas", "El asentamiento europeo y la población de las Américas"),
    "USH.f": ("World War I and World War II", "La Primera y la Segunda Guerra Mundial"),
    "USH.g": ("The Cold War", "La Guerra Fría"),
    "USH.h": ("American foreign policy since 9/11", "La política exterior estadounidense desde el 11 de septiembre"),
    "E.a": ("Key economic events that have shaped American government and policies", "Hechos económicos clave que dieron forma al gobierno y a las políticas de los EE. UU."),
    "E.b": ("Relationship between political and economic freedoms", "Relación entre las libertades políticas y las económicas"),
    "E.c": ("Fundamental economic concepts", "Conceptos económicos fundamentales"),
    "E.d": ("Microeconomics", "Microeconomía"),
    "E.e": ("Macroeconomics", "Macroeconomía"),
    "E.f": ("Consumer economics", "Economía del consumidor"),
    "E.g": ("Economic causes and impacts of wars", "Causas y efectos económicos de las guerras"),
    "E.h": ("Economic drivers of exploration and colonization", "Motores económicos de la exploración y la colonización"),
    "E.i": ("Scientific and industrial revolutions", "Las revoluciones científica e industrial"),
    "G.a": ("Development of classical civilizations", "El desarrollo de las civilizaciones clásicas"),
    "G.b": ("Relationship between the environment and societal development", "Relación entre el medio ambiente y el desarrollo de las sociedades"),
    "G.c": ("Borders between peoples and nations", "Fronteras entre pueblos y naciones"),
    "G.d": ("Human migration", "La migración humana"),
}
AREA_CT = {"CG": ("Civics and government · about 50% of the test", "Educación cívica y gobierno · cerca del 50 % del examen"),
           "USH": ("United States history · about 20%", "Historia de los Estados Unidos · cerca del 20 %"),
           "E": ("Economics · about 15%", "Economía · cerca del 15 %"),
           "G": ("Geography and the world · about 15%", "Geografía y el mundo · cerca del 15 %")}
CODIGO = {
    "R1": ("CCR Reading 1: read closely and cite specific evidence from the text.", "Lectura CCR 1: leer con atención y citar evidencia concreta del texto."),
    "R2": ("CCR Reading 2: find the central ideas and summarize them.", "Lectura CCR 2: determinar las ideas centrales y resumirlas."),
    "R3": ("CCR Reading 3: analyze how people, events, and ideas develop and interact.", "Lectura CCR 3: analizar cómo se desarrollan y se relacionan las personas, los hechos y las ideas."),
    "R4": ("CCR Reading 4: interpret words and phrases, including technical meanings.", "Lectura CCR 4: interpretar palabras y frases, incluidos los significados técnicos."),
    "R6": ("CCR Reading 6: determine the author's point of view or purpose.", "Lectura CCR 6: determinar el punto de vista o el propósito del autor."),
    "R7": ("CCR Reading 7: combine information from text, visuals, and numbers.", "Lectura CCR 7: integrar información de textos, imágenes y números."),
    "R8": ("CCR Reading 8: evaluate the claims in a text and the evidence behind them.", "Lectura CCR 8: evaluar las afirmaciones de un texto y la evidencia que las sostiene."),
    "R9": ("CCR Reading 9: compare how two texts treat the same topic.", "Lectura CCR 9: comparar cómo tratan dos textos el mismo tema."),
    "L4": ("CCR Language 4: work out the meaning of unknown words (context, roots).", "Lenguaje CCR 4: deducir el significado de palabras desconocidas (contexto, raíces)."),
    "NSH": ("National Standards for History: historical analysis and interpretation (context, credibility, evidence).", "Estándares Nacionales de Historia: análisis e interpretación histórica (contexto, credibilidad, evidencia)."),
    "3.MD": ("Math, measurement and data (grade 3): picture and bar graphs.", "Matemáticas, medición y datos (3.er grado): pictogramas y gráficas de barras."),
    "6.SP": ("Math, statistics (grade 6): center and spread of a data set.", "Matemáticas, estadística (6.º grado): centro y dispersión de un conjunto de datos."),
    "7.RP": ("Math, ratios and proportions (grade 7): rates, percents, and proportional relationships.", "Matemáticas, razones y proporciones (7.º grado): tasas, porcentajes y relaciones proporcionales."),
    "8.SP": ("Math, statistics (grade 8): patterns in two-variable data.", "Matemáticas, estadística (8.º grado): patrones en datos de dos variables."),
    "S-ID": ("Statistics: interpret categorical and quantitative data.", "Estadística: interpretar datos categóricos y cuantitativos."),
}


def estandares(sp, ct, base=()):
    """sp: indicadores SSP que trabaja; base: los que prepara; ct: temas de contenido (CG.b, USH.c…)."""
    def li(cls, cod):
        dok, cods = ALIN[cod]
        prac = cod.rsplit(".", 1)[0]
        return (f'<li><span class="std-cod {cls}">{cod}</span> <strong>{t(*NOMBRE_SSP[prac])}.</strong> {t(*SSP[cod])}<br><span class="std-meta">'
                f'DOK {dok} · {t("Aligned with", "Alineado con")} {", ".join(cods)}</span></li>')
    usados = []
    for c in list(sp) + list(base):
        for k in ALIN[c][1]:
            if k not in usados:
                usados.append(k)
    s = [f'<details class="estandares" id="{t("ged-standards", "estandares-ged")}">',
         f'<summary><span aria-hidden="true">🎓</span> {t("Standards for this lesson (GED® and CCR)", "Estándares de esta lección (GED® y CCR)")}</summary>',
         '<div class="std-cuerpo">',
         f'<p class="std-tit">{t("Social Studies Practices of the GED® test that this lesson works on:", "Prácticas de estudios sociales del examen GED® que trabaja esta lección:")}</p><ul>' +
         "".join(li("std-dir", c) for c in sp) + "</ul>"]
    if base:
        s.append(f'<p class="std-tit">{t("It also builds the base for:", "También prepara la base para:")}</p><ul>' + "".join(li("std-base", c) for c in base) + "</ul>")
    s.append(f'<p class="std-tit">{t("GED® Social Studies content topics:", "Temas de contenido de Estudios Sociales del GED®:")}</p>')
    if ct:
        s.append("<ul>" + "".join(f'<li><span class="std-cod std-mp">{c}</span> {t(*CT[c])} <span class="std-meta">({t(*AREA_CT[c.split(".")[0]])})</span></li>' for c in ct) + "</ul>")
    else:
        s.append("<p>" + t("The skills in this lesson are used with every content area of the test: civics and government (about 50% of the questions), U.S. history (20%), economics (15%), and geography and the world (15%). On the test, every question joins one practice with one content topic.",
                           "Las destrezas de esta lección se aplican a todas las áreas de contenido del examen: educación cívica y gobierno (cerca del 50 % de las preguntas), historia de los Estados Unidos (20 %), economía (15 %) y geografía y el mundo (15 %). En el examen, cada pregunta une una práctica con un tema de contenido.") + "</p>")
    s.append(f'<p class="std-tit">{t("What the aligned codes mean:", "Qué significan los códigos alineados:")}</p><ul class="std-clave">' +
             "".join(f'<li><span class="std-cod std-ccr">{k}</span> {t(*CODIGO[k])}</li>' for k in usados) + "</ul>")
    s.append('<p class="std-fuente">' + t(
        "DOK (depth of knowledge): 1 = recall, 2 = use a skill or concept, 3 = reason with evidence. Source of the practices, the content topics, the DOK ranges, and the alignment: GED Testing Service, <cite>Assessment Guide for Educators: Social Studies</cite>. The CCR anchor standards are in Pimentel, S. (2013), <cite>College and Career Readiness Standards for Adult Education</cite>.",
        "DOK (profundidad de conocimiento): 1 = recordar, 2 = aplicar una destreza o un concepto, 3 = razonar con evidencia. Fuente de las prácticas, los temas de contenido, los rangos de DOK y la alineación: GED Testing Service, <cite>Assessment Guide for Educators: Social Studies</cite>. Los estándares ancla CCR están en Pimentel, S. (2013), <cite>College and Career Readiness Standards for Adult Education</cite>.") + "</p>")
    s.append("</div>\n</details>")
    return "\n".join(s)


C.estandares = estandares


# ---------------------------------------------------------------- el documento
def documento(titulo, ficha, partes, nota=None):
    """Un documento real para analizar.
    ficha: lista de (campo, valor) — ya en el idioma de la página.
    partes: lista de (subtítulo, [párrafos en inglés], [párrafos en español]). En inglés se muestra el
    original; en español, la traducción, con el original plegado debajo."""
    f = "".join(f"<dt>{a}</dt><dd>{b}</dd>" for a, b in ficha)
    cuerpo = []
    for sub, en, es in partes:
        h = f"<h4>{sub}</h4>" if sub else ""
        if C.L == "en":
            cuerpo.append(h + "".join(f"<p>{p}</p>" for p in en))
        else:
            cuerpo.append(h + "".join(f"<p>{p}</p>" for p in es) +
                          '<details class="original"><summary>Ver el original en inglés</summary><div lang="en">' +
                          "".join(f"<p>{p}</p>" for p in en) + "</div></details>")
    n = f'<p class="doc-nota">{nota}</p>' if nota else ""
    return (f'<div class="documento"><p class="doc-tit"><span aria-hidden="true">📜</span> {titulo}</p>'
            f'<dl class="ficha">{f}</dl>{n}<div class="doc-texto">' + "".join(f'<div class="doc-parte">{x}</div>' for x in cuerpo) + "</div></div>")


def cita(texto, autor):
    """Un fragmento breve de una fuente (estímulo de una pregunta tipo GED)."""
    return f'<blockquote class="cita-doc"><p>{texto}</p><footer>— {autor}</footer></blockquote>'


# ---------------------------------------------------------------- el escenario de varias fuentes
def fuente(etiqueta, cuerpo):
    """Una fuente dentro de un escenario: etiqueta («Source 1 · Text») y su contenido en HTML."""
    return f'<div class="fuente"><p class="f-tit">{etiqueta}</p>{cuerpo}</div>'


def escenario(titulo, fuentes, nota=None):
    """Un escenario del examen: varias fuentes sobre un mismo asunto, en una caja."""
    n = f'<p class="esc-nota">{nota}</p>' if nota else ""
    return f'<div class="escenario" role="group" aria-label="{titulo}"><p class="esc-tit"><span aria-hidden="true">🧩</span> {titulo}</p>{"".join(fuentes)}{n}</div>'
