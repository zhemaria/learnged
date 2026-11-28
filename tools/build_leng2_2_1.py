# -*- coding: utf-8 -*-
"""LearnGED · Artes del lenguaje (español) · Nivel 2 · Lección 2.1 · Sustantivos y adverbios.
Fuente: clases_leng2/clase_2-1.html (GEDparaHispanos) y gramatica/n2-l2-1.html, adaptadas al marco de LearnGED.
Uso: python3 tools/build_leng2_2_1.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import leng_es as LE
from leng_es import C

LE.nivel(2)
N = "2-1"
TIPOS = ["Concreto", "Abstracto", "Colectivo"]
SUST = [("silla", 0, "se ve y se toca"), ("manzana", 0, "se ve, se toca y se come"), ("carro", 0, "se ve y se toca"), ("perfume", 0, "se huele"), ("trueno", 0, "se oye"),
        ("camisa", 0, "se ve y se toca"), ("río", 0, "se ve y se toca"), ("teléfono", 0, "se ve y se toca"),
        ("paciencia", 1, "es una cualidad"), ("tristeza", 1, "es un sentimiento"), ("amistad", 1, "es una relación, una idea"), ("justicia", 1, "es una idea"),
        ("belleza", 1, "es una cualidad"), ("esperanza", 1, "es un sentimiento"), ("honestidad", 1, "es una cualidad"), ("cansancio", 1, "es un estado que se siente, pero no se toca"),
        ("público", 2, "grupo de personas que asisten a algo"), ("orquesta", 2, "grupo de músicos"), ("enjambre", 2, "grupo de abejas"), ("arboleda", 2, "grupo de árboles"),
        ("familia", 2, "grupo de parientes"), ("jauría", 2, "grupo de perros"), ("alumnado", 2, "grupo de alumnos"), ("ejército", 2, "grupo de soldados")]
PLURAL = [("luz", "luces", ["luzes", "luz"], "z → ces."), ("rey", "reyes", ["reys", "reis"], "Termina en y, que aquí suena como consonante: -es."),
          ("mes", "meses", ["mes", "mesis"], "Una sola sílaba: -es."), ("autobús", "autobuses", ["autobúses", "autobús"], "Lleva fuerza al final: -es, y la tilde desaparece."),
          ("nariz", "narices", ["narizes", "nariz"], "z → ces."), ("árbol", "árboles", ["arboles", "árbols"], "Consonante: -es. La tilde se mantiene."),
          ("ciudad", "ciudades", ["ciudads", "ciudáds"], "Consonante: -es."), ("sofá", "sofás", ["sofaes", "sofases"], "Vocal con tilde: -s."),
          ("canción", "canciones", ["canciónes", "cancions"], "-es, y la tilde desaparece."), ("crisis", "crisis", ["crisises", "crisi"], "Termina en -s sin fuerza: no cambia."),
          ("actriz", "actrices", ["actrizes", "actriz"], "z → ces."), ("corazón", "corazones", ["corazónes", "corazóns"], "-es, y la tilde desaparece."),
          ("martes", "martes", ["marteses", "martés"], "Termina en -s sin fuerza: no cambia."), ("mujer", "mujeres", ["mujers", "mujéres"], "Consonante: -es."),
          ("ley", "leyes", ["leys", "leis"], "Termina en y: -es."), ("joven", "jóvenes", ["jovenes", "jóvens"], "-es, y aparece la tilde.")]
ADV = [("La tienda abre *temprano*.", "temprano", "tiempo (¿cuándo?)"), ("Mis vecinos viven *arriba*.", "arriba", "lugar (¿dónde?)"),
       ("El niño leyó *rápidamente* el cuento.", "rápidamente", "modo (¿cómo?)"), ("Mi esposa trabaja *bastante*.", "bastante", "cantidad (¿cuánto?)"),
       ("*Hoy* cocina mi hermano.", "Hoy", "tiempo (¿cuándo?)"), ("Pon las llaves *allí*.", "allí", "lugar (¿dónde?)"), ("Los gatos duermen *afuera*.", "afuera", "lugar (¿dónde?)"),
       ("Mi hijo estudia *poco*.", "poco", "cantidad (¿cuánto?)"), ("*Siempre* desayuno en casa.", "Siempre", "tiempo (¿cuándo?)"), ("El médico habló *claramente*.", "claramente", "modo (¿cómo?)"),
       ("Mi abuela *ya* llegó.", "ya", "tiempo (¿cuándo?)"), ("La farmacia queda *cerca*.", "cerca", "lugar (¿dónde?)"), ("Los precios subieron *demasiado*.", "demasiado", "cantidad (¿cuánto?)"),
       ("Camina *despacio*, por favor.", "despacio", "modo (¿cómo?)"), ("Mi tío vive *lejos*.", "lejos", "lugar (¿dónde?)"), ("*Mañana* empieza mi curso.", "Mañana", "tiempo (¿cuándo?)")]
COMPL = [("¿Cuándo?", "Mi hermana llega ___ del trabajo.", "tarde", ["allí", "mucho"]), ("¿Dónde?", "Los niños juegan ___.", "afuera", ["ayer", "poco"]),
         ("¿Cómo?", "El médico explicó todo ___.", "claramente", ["temprano", "afuera"]), ("¿Cuánto?", "Este mes llovió ___.", "bastante", ["aquí", "bien"]),
         ("¿Cuándo?", "___ voy a la biblioteca.", "Mañana", ["Lejos", "Despacio"]), ("¿Dónde?", "Deje los zapatos ___.", "abajo", ["pronto", "mucho"]),
         ("¿Cómo?", "Mi abuelo maneja ___.", "despacio", ["temprano", "dentro"]), ("¿Cuánto?", "Mis hijos duermen ___ los domingos.", "mucho", ["allí", "ya"]),
         ("¿Cuándo?", "La reunión empezó ___.", "temprano", ["arriba", "bien"]), ("¿Dónde?", "La parada del autobús está ___.", "cerca", ["nunca", "poco"]),
         ("¿Cómo?", "Cierre la puerta ___, que el bebé duerme.", "suavemente", ["mañana", "adentro"]), ("¿Cuánto?", "Ese carro cuesta ___.", "demasiado", ["afuera", "ayer"])]
PARQUE = ["Los domingos voy temprano al parque de mi barrio. Allí siempre hay mucha gente: familias con niños, parejas de ancianos y un equipo de fútbol que entrena cerca de la fuente.",
          "Me siento tranquilamente en un banco y observo. Un grupo de palomas camina despacio entre los árboles. Más allá, una banda toca música alegre. Los niños corren rápidamente detrás de un balón, y sus padres los miran con orgullo.",
          "En el parque se respira paz. Cuando el sol calienta demasiado, regreso a casa con alegría y con ganas de volver pronto."]


def leccion():
    P = C.Practicas()
    s1 = f"""<p>En el Nivel 1 aprendió que el <strong>sustantivo</strong> nombra personas, lugares, objetos e ideas. Hoy conocerá más tipos de sustantivos y una palabra nueva: el <strong>adverbio</strong>. Si el adjetivo describe a las cosas, el adverbio describe a las acciones: no es lo mismo <em>hablar</em> que <em>hablar despacio</em>.</p>
{C.tabla("Sustantivos concretos, abstractos y colectivos", ["Tipo", "Qué nombra", "Ejemplos"],
         [["Concreto", "Algo que se puede ver, tocar, oír u oler.", "mesa, pan, perro, lluvia, música"], ["Abstracto", "Una idea, un sentimiento o una cualidad: existe, pero no se toca.", "alegría, miedo, libertad, paciencia, belleza"],
          ["Colectivo", "En singular, un grupo de muchos seres o cosas.", "gente, familia, equipo, rebaño, enjambre, orquesta"]])}
{C.caja("tip", "La prueba de la caja", "<p>¿Lo podría guardar en una caja? Una taza, sí: es concreto. La paciencia, no: es abstracto. Muchos abstractos se forman con sufijos que ya conoce: educa<strong>ción</strong>, triste<strong>za</strong>, bon<strong>dad</strong>.</p>")}
{C.caja("ojo", "Error muy común", "<p>Aunque nombra a muchos, el colectivo es <strong>singular</strong>, y el verbo también: <em>La gente <strong>está</strong> contenta</em> (no «la gente están»); <em>El equipo <strong>ganó</strong></em> (no «el equipo ganaron»).</p>")}
{P("Compruebe", "<strong>esperanza</strong> es un sustantivo…", TIPOS, 1, {0: "No se puede tocar.", 2: "No nombra un grupo."}, "<strong>Abstracto</strong>: es un sentimiento.")}
{P("Compruebe", "¿Cuál está bien escrita?", ["La gente está contenta.", "La gente están contentos."], 0, {}, "<strong>La gente está</strong>: el colectivo es singular.")}"""

    s2 = f"""{C.tabla("Reglas del plural", ["Si la palabra termina en…", "El plural", "Ejemplos"],
         [["Vocal sin tilde", "añade -s", "casa → casas · niño → niños"], ["Vocal con tilde (á, é, ó)", "añade -s", "café → cafés · sofá → sofás"],
          ["Consonante", "añade -es", "papel → papeles · ciudad → ciudades"], ["-z", "cambia la z por c y añade -es", "lápiz → lápices · voz → voces"],
          ["-s en sílaba sin fuerza", "no cambia", "el lunes → los lunes · la crisis → las crisis"]])}
{C.caja("tip", "La tilde puede moverse", "<p>Al añadir una sílaba, a veces la tilde desaparece (<em>camión → camiones</em>) y a veces aparece (<em>joven → jóvenes</em>, <em>examen → exámenes</em>). La fuerza de la voz se queda en la misma sílaba; lo que cambia es la regla de la tilde, que verá en el Tema 3.</p>")}
{P("Compruebe", "¿Cuál es el plural de <strong>lápiz</strong>?", ["lápices", "lápizes", "lápiz"], 0, {1: "La z cambia a c delante de e.", 2: "Sí cambia."}, "<strong>lápices</strong>: z → ces.")}"""

    s3 = f"""<p>El <strong>adverbio</strong> acompaña sobre todo al verbo y da más información sobre la acción. Para encontrarlo, hágale una pregunta al verbo:</p>
{C.tabla("Tipos de adverbios", ["Tipo", "Responde a…", "Ejemplos"],
         [["De modo", "¿Cómo?", "bien, mal, despacio, así, y muchos en -mente: tranquilamente"], ["De tiempo", "¿Cuándo?", "hoy, ayer, mañana, ahora, siempre, nunca, ya, pronto, tarde, temprano"],
          ["De lugar", "¿Dónde?", "aquí, allí, cerca, lejos, arriba, abajo, dentro, fuera"], ["De cantidad", "¿Cuánto?", "mucho, poco, muy, bastante, demasiado, más, menos"]])}
<p><em>Mi hijo estudia</em> → ¿cuándo? <strong>siempre</strong> · ¿cuánto? <strong>mucho</strong> · ¿dónde? <strong>aquí</strong> → <em>Mi hijo siempre estudia mucho aquí.</em></p>
{C.caja("tip", "El adverbio no cambia", "<p>No tiene masculino ni femenino, ni singular ni plural: <em>Ella está <strong>medio</strong> cansada</em> (no «media cansada»); <em>Ellas llegaron <strong>temprano</strong></em> (no «tempranas»).</p>")}
{C.caja("ojo", "Mucho y poco", "<p>Con un verbo son adverbios y no cambian: <em>Ellas comen <strong>mucho</strong></em>. Con un sustantivo funcionan como adjetivos y sí concuerdan: <em><strong>mucha</strong> gente, <strong>pocas</strong> sillas</em>.</p>")}
<h3>Lectura: «El parque de mi barrio»</h3>
{LE.escuchar(" ".join(PARQUE), "Escuchar el texto")}
<div class="texto-lectura">{"".join(f"<p>{p}</p>" for p in PARQUE)}</div>
<p>Anote en su cuaderno cuatro sustantivos colectivos, tres abstractos y seis adverbios con la pregunta que responden.</p>
<details class="caja caja-tip"><summary><strong>Ver las respuestas</strong></summary>
<p><strong>Colectivos:</strong> gente, familias, equipo, grupo, banda. <strong>Abstractos:</strong> orgullo, paz, alegría, ganas. <strong>Adverbios:</strong> temprano (¿cuándo?), allí (¿dónde?), siempre (¿cuándo?), cerca (¿dónde?), tranquilamente (¿cómo?), despacio (¿cómo?), rápidamente (¿cómo?), demasiado (¿cuánto?), pronto (¿cuándo?).</p>
<p>En <em>mucha gente</em>, <em>mucha</em> no es adverbio: acompaña a un sustantivo y concuerda con él.</p></details>
<div class="caja caja-tip"><span class="etiqueta et-verde">Actividad · enriquezca la oración</span>
<p>Copie cada oración y añádale dos adverbios que respondan a las preguntas: <em>Mi vecina cocina</em> (¿cómo? ¿cuándo?) · <em>Los niños juegan</em> (¿dónde? ¿cuánto?) · <em>El autobús avanza</em> (¿cuándo? ¿cómo?) · <em>Mi equipo entrena</em> (¿dónde? ¿cuándo?).</p>
<p>Ejemplo: <em>Mi vecina siempre cocina muy bien.</em></p></div>"""

    secciones = [("s1", "Tres clases de sustantivos", s1), ("s2", "El plural de los sustantivos", s2), ("s3", "Los adverbios", s3)]
    tarea = [("Mis sustantivos.", "Escriba cinco sustantivos concretos, cinco abstractos y cinco colectivos de su vida diaria."),
             ("Mis plurales.", "Escriba el plural de: voz, examen, jueves, café, pared, canción. Diga qué regla usó."),
             ("Mi día con adverbios.", "Escriba un párrafo de cinco oraciones sobre su día con al menos un adverbio de modo, uno de tiempo, uno de lugar y uno de cantidad. Subráyelos.")]
    quiz = [
        ("¿Qué nombra un sustantivo abstracto?", ["Una idea, un sentimiento o una cualidad", "Algo que se ve, se toca o se oye", "Un grupo de seres o de cosas"], 0, {1: "Eso es concreto.", 2: "Eso es colectivo."}, "<strong>Una idea, un sentimiento o una cualidad.</strong>"),
        ("<strong>enjambre</strong> es un sustantivo…", TIPOS, 2, {0: "No es una sola cosa.", 1: "Sí se puede ver."}, "<strong>Colectivo</strong>: grupo de abejas."),
        ("¿Cuál está bien?", ["El equipo ganó.", "El equipo ganaron."], 0, {}, "<strong>El equipo ganó</strong>: singular."),
        ("Plural de <strong>canción</strong>:", ["canciones", "canciónes", "cancions"], 0, {1: "La tilde desaparece.", 2: "Termina en consonante: -es."}, "<strong>canciones.</strong>"),
        ("Plural de <strong>el lunes</strong>:", ["los lunes", "los luneses"], 0, {}, "<strong>los lunes</strong>: no cambia."),
        ("¿Qué pregunta responde un adverbio de lugar?", ["¿Dónde?", "¿Cuándo?", "¿Cómo?"], 0, {1: "Eso es de tiempo.", 2: "Eso es de modo."}, "<strong>¿Dónde?</strong>"),
        ("<em>El médico habló claramente.</em> ¿Cuál es el adverbio?", ["claramente", "médico", "habló"], 0, {1: "Es un sustantivo.", 2: "Es el verbo."}, "<strong>claramente</strong> (¿cómo?)."),
        ("¿Cuál está bien?", ["Ella está medio cansada.", "Ella está media cansada."], 0, {}, "<strong>medio</strong>: el adverbio no cambia."),
        ("En <em>Había mucha gente</em>, <strong>mucha</strong> es…", ["un adjetivo", "un adverbio"], 0, {1: "Acompaña a un sustantivo, no a un verbo."}, "Es un <strong>adjetivo</strong>: acompaña a un sustantivo: <strong>concuerda</strong>."),
        ("<em>Siempre desayuno en casa.</em> <strong>Siempre</strong> es un adverbio de…", ["tiempo", "lugar", "cantidad"], 0, {1: "No dice dónde.", 2: "No dice cuánto."}, "<strong>Tiempo</strong> (¿cuándo?)."),
    ]
    filas = [
        ("Sustantivos", "Distingo concretos, abstractos y colectivos, y uso el colectivo en singular.", "Distingo dos de los tres.", "No los distingo (<a href=\"#s1\">repase la sección 1</a>)."),
        ("Plural", "Formo el plural con todas las reglas, también con z y con tilde.", "Me equivoco con la z o la tilde.", "No sé las reglas (<a href=\"#s2\">repase la sección 2</a>)."),
        ("Adverbios", "Encuentro el adverbio y digo qué pregunta responde.", "Lo encuentro, pero dudo del tipo.", "No lo encuentro (<a href=\"#s3\">repase la sección 3</a>)."),
    ]
    cierre = "<p>Ya conoce más clases de sustantivos y sabe usar los adverbios. En la próxima lección verá los <strong>pronombres reflexivos y la concordancia</strong>.</p>"
    glosario = [("Sustantivo concreto", "Nombra algo que se percibe con los sentidos."), ("Sustantivo abstracto", "Nombra una idea, un sentimiento o una cualidad."),
                ("Sustantivo colectivo", "Nombra en singular a un grupo."), ("Adverbio", "Palabra que dice cómo, cuándo, dónde o cuánto ocurre una acción; no cambia de forma.")]
    conexion = ("<p>Con el Tema 2 entra en la gramática de la oración. Partirá de lo que ya sabe del sustantivo y conocerá una palabra que da precisión a lo que hacemos: el adverbio.</p>"
                "<p><strong>Lo que necesita:</strong> el cuaderno.</p>")
    estd = LE.estandares(["L.1.7"], base=["L.1.2"])
    return C.pagina_leccion(N, LE.titulo(N), "Lo que nombramos y cómo lo hacemos.", ["Gramática", "Sustantivo y adverbio"],
                            ["<strong>Distinguir</strong> sustantivos concretos, abstractos y colectivos.", "<strong>Formar</strong> el plural de los sustantivos.",
                             "<strong>Reconocer</strong> los adverbios de modo, tiempo, lugar y cantidad.", "<strong>Enriquecer</strong> oraciones con adverbios."],
                            estd, conexion, secciones, tarea, quiz, filas, cierre, ("2-2", LE.titulo("2-2")), glosario, P)


def practica():
    su = [{"enun": f"<strong class=\"grande\">{w}</strong><br>¿Qué tipo de sustantivo es?", "ops": TIPOS, "ok": k, "enOrden": True, "pista": "¿Lo podría guardar en una caja? ¿Nombra a muchos a la vez?",
           "exp": f"<strong>{TIPOS[k]}</strong>: {e}."} for w, k, e in SUST]
    pl = [{"enun": f"<strong class=\"grande\">{w}</strong><br>¿Cuál es su plural?", "ops": [ok] + d, "ok": 0, "pista": "¿En qué letra termina la palabra? Repase la tabla del plural.", "exp": f"<strong>{ok}</strong>. {e}"} for w, ok, d, e in PLURAL]
    ad = [{"consigna": "Toque el adverbio de la oración.", "texto": t, "exp": f"«<strong>{a}</strong>» es un adverbio de {e}."} for t, a, e in ADV]
    co = [{"enun": f"<strong>{q}</strong><br><span class=\"grande\">{o.replace('___', '_____')}</span>", "ops": [ok] + d, "ok": 0, "pista": "Elija el adverbio que responde a la pregunta de arriba.",
           "exp": f"«{o.replace('___', ok)}»"} for q, o, ok, d in COMPL]
    mods = [("sustantivos", "Tipos de sustantivo", C.om("m1", "¿Concreto, abstracto o colectivo?")),
            ("plural", "El plural", C.om("m2", "Elija el plural correcto.")),
            ("adverbio", "Encuentre el adverbio", LE.marcar("m3", "Toque el adverbio. Después pulse <strong>Comprobar</strong>.")),
            ("completar", "Complete con un adverbio", C.om("m4", "Elija el adverbio que responde a la pregunta."))]
    js = (C.js_datos("SU", su) + C.js_datos("PL", pl) + C.js_datos("AD", ad) + C.js_datos("CO", co) +
          'creaBanco("m1", SU);\ncreaBanco("m2", PL);\ncreaMarcar("m3", AD);\ncreaBanco("m4", CO);\n')
    return C.pagina_practica(N, LE.titulo(N), "Cuatro actividades · los ejercicios cambian cada vez · dos intentos en cada uno", mods, js)


if __name__ == "__main__":
    LE.construye(N, leccion, practica, horas="Unas 3 horas")
