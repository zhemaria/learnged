# -*- coding: utf-8 -*-
"""LearnGED · Artes del lenguaje (español) · Nivel 1 · Lección 4.5 · Claves de contexto.
Fuente: clases_leng1/clase_4-5.html (GEDparaHispanos) y sus prácticas de gramatica, adaptadas al marco de LearnGED.
Uso: python3 tools/build_leng1_4_5.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import leng_es as LE
from leng_es import C

LE.nivel(1)
N = "4-5"
CLAVES = ["Sinónimo", "Antónimo", "Ejemplo", "Definición"]
# (oración con la palabra en <u>, tipo de clave, significado correcto, dos distractores)
ORACIONES = [
    ("Los vecinos estaban <u>furiosos</u>, muy enojados por el ruido de la fiesta.", 0, "muy enojados", ["muy contentos", "muy cansados"]),
    ("No fue una decisión <u>precipitada</u>, sino bien pensada y reflexionada.", 1, "apurada, sin pensar", ["muy lenta", "muy cara"]),
    ("Los <u>cítricos</u>, como la naranja, el limón y la toronja, tienen vitamina C.", 2, "frutas ácidas como la naranja", ["verduras de hoja", "frutas secas"]),
    ("El <u>insomnio</u>, es decir, la dificultad para dormir, afecta a muchos adultos.", 3, "la dificultad para dormir", ["el sueño profundo", "un dolor de cabeza"]),
    ("Después de correr diez millas, el atleta estaba <u>exhausto</u>, agotado, y se sentó a descansar.", 0, "muy cansado", ["muy feliz", "muy rápido"]),
    ("La sopa estaba <u>insípida</u>; no tenía nada de sal ni de sabor.", 3, "sin sabor", ["muy picante", "muy caliente"]),
    ("Mi hermano es muy <u>madrugador</u>: se levanta todos los días a las cinco de la mañana.", 2, "que se levanta muy temprano", ["que duerme mucho", "que trabaja de noche"]),
    ("El examen no fue <u>sencillo</u>, sino muy difícil.", 1, "fácil", ["largo", "aburrido"]),
    ("Los <u>electrodomésticos</u>, como la lavadora, el refrigerador y el microondas, gastan electricidad.", 2, "aparatos eléctricos de la casa", ["muebles de madera", "herramientas del jardín"]),
    ("La <u>gratitud</u>, o sea, el sentimiento de agradecer, hace felices a las personas.", 3, "el sentimiento de agradecer", ["el enojo", "el miedo"]),
    ("Mi abuela era muy <u>ahorrativa</u>, es decir, nunca gastaba de más y guardaba cada moneda.", 3, "que cuida el dinero", ["que gasta mucho", "que trabaja poco"]),
    ("Pensé que la película sería aburrida, pero fue muy <u>entretenida</u>.", 1, "divertida, interesante", ["triste", "corta"]),
    ("Los <u>lácteos</u>, tales como la leche, el queso y el yogur, tienen calcio.", 2, "alimentos hechos de leche", ["alimentos con azúcar", "carnes"]),
    ("Un <u>bilingüe</u> es una persona que habla dos idiomas.", 3, "persona que habla dos idiomas", ["persona que viaja mucho", "persona que lee mucho"]),
    ("El cuarto estaba <u>desordenado</u>, todo revuelto y fuera de lugar.", 0, "sin orden", ["muy limpio", "vacío"]),
    ("Mi jefe no es <u>impaciente</u>; al contrario, espera con calma a que terminemos.", 1, "que no sabe esperar", ["que llega temprano", "que habla poco"]),
]
AVISOS = [("es decir", 3), ("o sea", 3), ("significa", 3), ("como", 2), ("por ejemplo", 2), ("tales como", 2), ("pero", 1), ("sino", 1), ("al contrario", 1), ("también llamado", 0)]


def leccion():
    P = C.Practicas()
    s1 = f"""<p>Hasta los mejores lectores encuentran palabras que no conocen. La diferencia entre el lector que avanza y el que se detiene no está en saberse todo el vocabulario (eso es imposible), sino en saber qué hacer cuando aparece una palabra nueva.</p>
<p>El <strong>contexto</strong> es todo lo que rodea a una palabra: las palabras vecinas, las oraciones de antes y de después, el tema del texto. Casi siempre da pistas.</p>
{C.ejemplo("El lector detective", [("1", "<em>El niño estaba <strong>hambriento</strong> porque no había comido en todo el día.</em>"),
                                   ("2", "No sé qué es <em>hambriento</em>, pero la oración dice «no había comido en todo el día»."),
                                   ("3", "¿Cómo se siente alguien que no come en todo el día? Con mucha hambre.")], "<em>Hambriento</em> = con mucha hambre.")}
{C.caja("tip", "La regla del detective", "<p>Lea la oración completa. Lea también la de antes y la de después. Casi siempre hay una pista. En el examen GED, muchas preguntas de vocabulario son así: <em>¿Qué significa la palabra «…» tal como se usa en el párrafo 3?</em></p>")}"""

    tabla = C.tabla("Las cuatro claves de contexto", ["Clave", "Qué hace el autor", "Ejemplo"],
                    [["🟰 Sinónimo", "Pone cerca una palabra de significado parecido.", ORACIONES[0][0]], ["↔️ Antónimo", "Dice lo contrario.", ORACIONES[1][0]],
                     ["💡 Ejemplo", "Nombra casos concretos.", ORACIONES[2][0]], ["📖 Definición", "Lo explica directamente.", ORACIONES[3][0]]])
    avisos = C.tabla("Palabras que avisan que viene una pista", ["Clave", "Palabras que la avisan"],
                     [["Sinónimo", "también llamado, conocido como, o; una palabra parecida justo al lado"], ["Antónimo", "pero, sin embargo, sino, en cambio, al contrario"],
                      ["Ejemplo", "como, por ejemplo, tales como, incluyendo"], ["Definición", "es decir, o sea, significa, quiere decir"]])
    s2 = f"""<p>Los autores usan cuatro clases de pistas. Aprenda a reconocerlas:</p>
{tabla}
{avisos}
{P("Compruebe", f"<em>{ORACIONES[4][0]}</em><br>¿Qué significa <u>exhausto</u>?", ["muy feliz", "muy cansado", "muy rápido"], 1,
   {0: "¿Por qué se sentaría a descansar alguien feliz?", 2: "Correr rápido no explica que se siente a descansar."}, "<strong>Muy cansado</strong>: el sinónimo <em>agotado</em> está al lado, y además corrió diez millas y se sentó a descansar.")}
{P("Compruebe", f"<em>{ORACIONES[7][0]}</em><br>¿Qué clase de clave ayuda?", CLAVES, 1,
   {0: "No hay una palabra parecida: hay una opuesta.", 2: "No se nombran casos.", 3: "No se explica directamente."}, "Un <strong>antónimo</strong>, avisado por <em>sino</em>: lo contrario de «muy difícil». Sencillo = fácil.")}"""

    s3 = f"""<div class="caja caja-tip"><span class="etiqueta et-verde">Actividad · en voz alta y en su cuaderno</span>
<p>Lea en voz alta cada oración. Escriba qué cree que significa la palabra subrayada y qué pista usó: «Lo sé porque dice…». Lo más importante no es acertar, sino <strong>explicar la pista</strong>.</p>
<ol><li><em>{ORACIONES[5][0]}</em></li><li><em>{ORACIONES[6][0]}</em></li><li><em>{ORACIONES[10][0]}</em></li><li><em>{ORACIONES[11][0]}</em></li></ol></div>
<details class="caja caja-tip"><summary><strong>Ya escribí mis respuestas: ver un modelo</strong></summary>
<ol><li><strong>Insípida:</strong> sin sabor. Pista: «no tenía nada de sal ni de sabor» (casi una definición).</li>
<li><strong>Madrugador:</strong> que se levanta muy temprano. Pista: el ejemplo de las cinco de la mañana.</li>
<li><strong>Ahorrativa:</strong> que cuida el dinero. Pista: la definición que avisa <em>es decir</em>.</li>
<li><strong>Entretenida:</strong> divertida. Pista: lo contrario de «aburrida», avisado por <em>pero</em>.</li></ol></details>
{C.caja("ojo", "Si no hay pista", "<p>A veces el contexto no ayuda. Entonces use las otras estrategias de la Lección 4.2: preguntar o consultar el diccionario. Y en la próxima lección aprenderá una llave más: mirar las partes de la palabra.</p>")}"""

    secciones = [("s1", "¿Qué es el contexto?", s1), ("s2", "Las cuatro claves de contexto", s2), ("s3", "Práctica: explique su pista", s3)]
    tarea = [("Mi palabra del día.", "Durante tres días, busque en un texto de verdad (una noticia, un aviso, una etiqueta) una palabra que no conozca. Copie la oración completa, escriba el significado que deduce y la clave que usó (sinónimo, antónimo, ejemplo, definición o «no había clave»)."),
             ("Compruebe.", "Al final, busque cada palabra en el diccionario. ¿Acertó?"),
             ("Revise su trabajo.", "¿Copió la oración completa? ¿Su significado se conecta con el contexto? ¿Supo qué clave usó?")]
    quiz = [
        ("¿Qué es el <strong>contexto</strong>?", ["Todo lo que rodea a una palabra", "El diccionario", "El título del libro"], 0, {1: "El diccionario es otra estrategia.", 2: "El título es una pista, pero el contexto es más."}, "Todo lo que <strong>rodea</strong> a la palabra."),
        ("¿Cuáles son las cuatro claves de contexto?", ["Sinónimos, antónimos, ejemplos y definiciones", "Sujeto, verbo, adjetivo y punto", "Antes, durante, después y resumen"], 0, {1: "Eso es gramática.", 2: "Eso es el ciclo de lectura."}, "<strong>Sinónimos, antónimos, ejemplos y definiciones.</strong>"),
        ("«No fue rápido, sino lento.» ¿Qué clave es?", CLAVES, 1, {0: "Rápido y lento no significan lo mismo.", 2: "No se nombran casos.", 3: "No hay es decir ni significa."}, "Un <strong>antónimo</strong>, avisado por <em>sino</em>."),
        ("¿Qué palabras avisan una <strong>definición</strong>?", ["es decir, o sea", "pero, sino", "como, por ejemplo"], 0, {1: "Esas avisan un antónimo.", 2: "Esas avisan un ejemplo."}, "<strong>es decir, o sea, significa</strong>."),
        (f"<em>{ORACIONES[2][0]}</em> ¿Qué son los <u>cítricos</u>?", ["frutas ácidas como la naranja", "verduras de hoja", "frutas secas"], 0, {1: "Los ejemplos son frutas, no verduras.", 2: "Naranja y limón son jugosos."}, "<strong>Frutas ácidas</strong> como la naranja: lo dicen los ejemplos."),
        (f"<em>{ORACIONES[3][0]}</em> ¿Qué clave ayuda?", CLAVES, 3, {0: "No hay palabra parecida al lado.", 1: "No hay contrario.", 2: "No se nombran casos."}, "Una <strong>definición</strong>, avisada por <em>es decir</em>."),
        (f"<em>{ORACIONES[0][0]}</em> ¿Qué significa <u>furiosos</u>?", ["muy enojados", "muy contentos", "muy cansados"], 0, {1: "El ruido no pone contentos a los vecinos.", 2: "La oración dice cómo estaban: enojados."}, "<strong>Muy enojados</strong>: el sinónimo está al lado."),
        ("Si no hay ninguna pista en el contexto, ¿qué hace?", ["Pregunta o consulta el diccionario", "Inventa un significado"], 0, {}, "<strong>Pregunta o consulta</strong>."),
        ("¿Qué palabras avisan un <strong>ejemplo</strong>?", ["como, por ejemplo, tales como", "es decir, o sea", "sin embargo, pero"], 0, {1: "Esas avisan una definición.", 2: "Esas avisan un contraste."}, "<strong>como, por ejemplo, tales como</strong>."),
        ("¿Qué es lo más importante al deducir una palabra?", ["Explicar la pista que usó", "Acertar a la primera"], 0, {}, "<strong>Explicar la pista</strong>: así se aprende a leer cualquier texto."),
    ]
    filas = [
        ("Usar el contexto", "Deduzco el significado de palabras nuevas con las palabras vecinas.", "Lo logro solo cuando la pista está muy clara.", "Me detengo y no sigo leyendo (<a href=\"#s1\">repase la sección 1</a>)."),
        ("Reconocer las claves", "Digo si la pista es sinónimo, antónimo, ejemplo o definición.", "Confundo algunas claves.", "No las reconozco (<a href=\"#s2\">repase la sección 2</a>)."),
        ("Explicar la pista", "Escribo «lo sé porque dice…» con la pista exacta.", "Acierto, pero no sé decir por qué.", "Adivino (<a href=\"#s3\">repase la sección 3</a>)."),
    ]
    cierre = "<p>Ya tiene la primera llave para el vocabulario nuevo: el contexto. En la última lección del tema aprenderá la segunda: mirar <strong>dentro</strong> de la palabra, en su raíz, su prefijo y su sufijo.</p>"
    glosario = [("Contexto", "Lo que rodea a una palabra: oraciones, palabras vecinas, tema."), ("Sinónimo", "Palabra de significado parecido: <em>furioso / enojado</em>."),
                ("Antónimo", "Palabra de significado contrario: <em>sencillo / difícil</em>."), ("Inferir", "Deducir algo a partir de pistas.")]
    conexion = ("<p>Ya sabe aclarar dudas mientras lee. Hoy aprenderá a hacerlo con las palabras desconocidas, sin abrir el diccionario: con las pistas que el propio autor deja cerca.</p>"
                "<p><strong>Lo que necesita:</strong> el cuaderno y un texto de verdad (noticia, aviso o etiqueta) para los próximos tres días.</p>")
    estd = LE.estandares(["R.4.1"], base=["L.1.9"])
    return C.pagina_leccion(N, LE.titulo(N), "Las palabras no viven solas: sus vecinas cuentan lo que significan.", ["R.4.1 · Vocabulario en contexto"],
                            ["<strong>Deducir</strong> el significado de palabras desconocidas por el contexto.", "<strong>Reconocer</strong> cuatro claves: sinónimo, antónimo, ejemplo y definición.",
                             "<strong>Usar</strong> las palabras que avisan una pista (es decir, como, pero, sino).", "<strong>Explicar</strong> qué pista usó."],
                            estd, conexion, secciones, tarea, quiz, filas, cierre, ("4-6", LE.titulo("4-6")), glosario, P)


def practica():
    sig = [{"enun": f"<em>{o}</em><br>¿Qué significa la palabra subrayada?", "ops": [ok] + d, "ok": 0, "pista": "Busque la pista: una palabra parecida, una contraria, unos ejemplos o una explicación.",
            "exp": f"<strong>{ok}</strong>. La pista es {['un sinónimo', 'un antónimo', 'un ejemplo', 'una definición'][k]}."} for o, k, ok, d in ORACIONES]
    cla = [{"enun": f"<em>{o}</em><br>¿Qué clave de contexto usó el autor?", "ops": CLAVES, "ok": k, "enOrden": True,
            "pista": "Mire las palabras que avisan: es decir (definición), como (ejemplo), pero o sino (antónimo).", "exp": f"<strong>{CLAVES[k]}</strong>."} for o, k, ok, d in ORACIONES]
    av = [{"enun": f"La palabra <strong>«{w}»</strong> suele avisar…", "ops": ["un sinónimo", "un antónimo", "un ejemplo", "una definición"], "ok": k, "enOrden": True,
           "exp": f"<em>{w}</em> avisa {['un sinónimo', 'un antónimo', 'un ejemplo', 'una definición'][k]}."} for w, k in AVISOS]
    mods = [("significado", "¿Qué significa la palabra?", C.om("m1", "Use la pista del contexto.")),
            ("clave", "¿Qué clave es?", C.om("m2", "Decida qué tipo de pista dejó el autor.")),
            ("avisos", "Palabras que avisan", C.om("m3", "¿Qué clase de pista suele venir después de cada palabra?"))]
    js = C.js_datos("SIG", sig) + C.js_datos("CLA", cla) + C.js_datos("AVI", av) + 'creaBanco("m1", SIG);\ncreaBanco("m2", CLA);\ncreaBanco("m3", AVI);\n'
    return C.pagina_practica(N, LE.titulo(N), "Tres actividades · los ejercicios cambian cada vez · dos intentos en cada uno", mods, js)


if __name__ == "__main__":
    LE.construye(N, leccion, practica, horas="Unas 3 horas")
