# -*- coding: utf-8 -*-
"""LearnGED · Artes del lenguaje (español) · Nivel 1 · Lección 2.3 · Palabras de uso frecuente y fluidez inicial.
Fuentes: clases_leng1/clase_2-3.html y gramatica/n1-l2-3.html (entrenador: palabras a simple vista,
señales y lectura repetida), adaptadas al marco de LearnGED. Las señales y las palabras parecidas
están en tools/leng/senales.json y tools/leng/parecidas.json.
Uso: python3 tools/build_leng1_2_3.py
"""
import json, os, random, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import leng_es as LE
from leng_es import C

LE.nivel(1)
N = "2-3"
DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "leng")
SENALES = json.load(open(os.path.join(DIR, "senales.json"), encoding="utf-8"))
PARECIDAS = {k: [x for x in v if x != k] for k, v in json.load(open(os.path.join(DIR, "parecidas.json"), encoding="utf-8")).items()}
GRUPOS = [("Grupo 1 · artículos y enlaces", ["el", "la", "los", "las", "un", "una", "de", "del", "en", "y"]),
          ("Grupo 2 · preguntas y respuestas", ["a", "que", "es", "son", "no", "sí", "por", "para", "con", "sin"]),
          ("Grupo 3 · las personas", ["mi", "tu", "su", "yo", "tú", "él", "ella", "me", "te", "se"]),
          ("Grupo 4 · comparar y unir", ["al", "lo", "le", "más", "pero", "como", "cuando", "muy", "también", "hay"]),
          ("Grupo 5 · lugar y tiempo", ["aquí", "allí", "hoy", "ahora", "todo", "nada", "bien", "está", "ver", "ir"])]
LECTURAS = [
    ("Un cartel en la puerta", ["Hoy yo voy a la tienda con mi mamá.", "La tienda está aquí, muy cerca de mi casa.", "En la puerta hay un cartel que dice «Empuje».",
                                "Yo leo el cartel y empujo la puerta.", "Mi mamá me dice: «Por favor, busca la leche».", "La leche está allí, al lado de los huevos."],
     [("¿Con quién va a la tienda?", ["Con su mamá", "Con su hermano", "Sola"], 0), ("¿Qué dice el cartel de la puerta?", ["Salida", "Empuje", "Cerrado"], 1),
      ("¿Dónde está la leche?", ["Al lado de los huevos", "En la puerta", "En la casa"], 0)]),
    ("En la esquina", ["Tú y yo caminamos por la calle.", "En la esquina hay una señal que dice «Alto».", "Nosotros no cruzamos ahora.",
                       "Cuando el semáforo está en verde, sí podemos pasar.", "Al final de la calle está la salida del parque.", "Todo el mundo sale por esa puerta."],
     [("¿Qué dice la señal de la esquina?", ["Alto", "Salida", "No fumar"], 0), ("¿Cuándo pueden pasar?", ["Cuando el semáforo está en verde", "Cuando no hay nadie", "Nunca"], 0),
      ("¿Qué hay al final de la calle?", ["Una tienda", "La salida del parque", "Un hospital"], 1)]),
    ("Mi casa", ["Mi casa es pequeña, pero es muy bonita.", "En la sala hay una mesa y dos sillas.", "Yo estudio aquí todos los días.",
                 "Mi hermano lee un libro y mi papá ve la televisión.", "Hoy no hay nadie más en la casa.", "Todo está muy tranquilo."],
     [("¿Cómo es la casa?", ["Grande y fea", "Pequeña, pero bonita", "Nueva y grande"], 1), ("¿Qué hay en la sala?", ["Una mesa y dos sillas", "Una cama", "Tres mesas"], 0),
      ("¿Qué hace el hermano?", ["Ve la televisión", "Lee un libro", "Estudia"], 1)]),
    ("El primer día de trabajo", ["Hoy es mi primer día en el trabajo nuevo.", "En la entrada hay un cartel que dice «Solo personal autorizado».", "Yo tengo mi tarjeta y sí puedo pasar.",
                                  "Mi jefe me dice: «Por favor, ven aquí».", "Él me explica todo con mucha calma.", "Al final del día, yo salgo por la puerta que dice «Salida»."],
     [("¿Qué dice el cartel de la entrada?", ["Salida", "No fumar", "Solo personal autorizado"], 2), ("¿Por qué puede pasar?", ["Porque tiene su tarjeta", "Porque llegó temprano", "Porque conoce al jefe"], 0),
      ("¿Cómo le explica el jefe?", ["Con mucha calma", "Con mucha prisa", "No le explica nada"], 0)]),
]


def crono(cid, tid):
    return f'''<div class="crono" id="{cid}" data-texto="{tid}">
<p class="crono-reloj" id="{cid}-tiempo" aria-live="off">0:00</p>
<p><button type="button" class="btn" id="{cid}-empezar">Empezar</button> <button type="button" class="btn-sec" id="{cid}-terminar" disabled>Terminar</button></p>
<p class="fb" id="{cid}-res" role="status" aria-live="polite"></p>
{C.tabla("Resultados de mis pasadas", ["Pasada", "Tiempo", "Palabras por minuto"], [["—", "Todavía no hay pasadas.", ""]])}
</div>'''


def frase(partes):
    """partes: lista de (palabra, 'f' frecuente | 'b' bisílaba | '' otra)."""
    txt = " ".join(p for p, _ in partes)
    return ('<p class="oracion-ej">' + " ".join(f'<span class="fr fr-{k}">{p}</span>' if k else p for p, k in partes) + " " + LE.escuchar(txt, "", 0.85) + "</p>")


def leccion():
    P = C.Practicas()
    tarjetas = ["el", "la", "de", "un", "una", "para", "tú", "yo", "con", "en", "que", "por", "mi", "muy", "hay", "está"]
    destello = f'''<div class="destello" id="d1" data-grupos='{json.dumps([{"n": n, "p": p} for n, p in GRUPOS], ensure_ascii=False)}'>
<p><label for="d1-grupo">Grupo de palabras:</label> <select id="d1-grupo"></select>
<label for="d1-vel">Tiempo por palabra:</label> <select id="d1-vel"><option value="4000">Muy despacio · 4 segundos</option><option value="3000" selected>Despacio · 3 segundos</option><option value="2000">Normal · 2 segundos</option><option value="1000">Rápido · 1 segundo</option></select></p>
<p class="destello-tarjeta" id="d1-palabra" aria-live="polite"></p>
<p><button type="button" class="btn" id="d1-pasar">Pasar palabras</button> <button type="button" class="btn-sec" id="d1-pausa" disabled>Pausar</button></p>
<p class="fb" id="d1-estado" role="status"></p>
<p><strong>Todas las palabras del grupo</strong> (toque una para oírla):</p><div class="destello-todas" id="d1-todas"></div>
</div>'''
    s1 = f"""<p>Hay un puñado de palabras que aparecen en casi todo lo que se lee: <em>el, la, de, que, en, y, un, por, con</em>… Si cada vez se detiene a decodificarlas sonido por sonido, la lectura se vuelve lenta y cansada. Lo mejor es <strong>reconocerlas de un vistazo</strong>, como cuando ve la cara de un amigo y sabe quién es sin pensarlo. Se llaman <strong>palabras de uso frecuente</strong>.</p>
{LE.AVISO_VOZ}
<p>Toque cada tarjeta para oírla. Léalas varias veces hasta que su vista las reconozca de un golpe:</p>
<p class="frecuentes">{" ".join(LE.escuchar(w, w, 0.8) for w in tarjetas)}</p>
<h3>Palabras al instante</h3>
<p>Las cincuenta palabras más frecuentes, en cinco grupos. Pulse <strong>Pasar palabras</strong> y lea en voz alta cada una cuando aparezca. Empiece despacio; cuando no dude con ninguna, suba la velocidad.</p>
{destello}
{C.caja("ojo", "Parecidas, pero distintas", "<p>Algunas palabras frecuentes se diferencian solo por una tilde, y cambian de significado: <em>el</em> (el libro) y <em>él</em> (él trabaja); <em>tu</em> (tu casa) y <em>tú</em> (tú estudias); <em>si</em> (si llueve) y <em>sí</em> (sí, quiero); <em>mi</em> (mi hijo) y <em>mí</em> (para mí). Mírelas bien: la tilde también se lee.</p>")}
{P("Compruebe", "¿En qué oración <strong>tú</strong> lleva tilde porque es una persona?", ["Tú estudias de noche.", "Tu casa es bonita."], 0, {},
   "<strong>Tú estudias</strong>: <em>tú</em> es la persona que estudia. En <em>tu casa</em>, <em>tu</em> dice de quién es la casa y no lleva tilde.")}"""

    s2 = f"""<p>En la Lección 1.3 vio que la fluidez tiene tres partes: <strong>precisión</strong> (leer bien cada palabra), <strong>ritmo</strong> (una velocidad cómoda) y <strong>expresión</strong> (pausas y entonación; los especialistas la llaman <em>prosodia</em>). Hoy va a practicar dos técnicas para ganarla.</p>
<h3>Lectura en eco</h3>
<p>La voz lee una frase con buena entonación y usted la repite exactamente igual, como un eco.</p>
<p class="oracion-ej">Hoy es un día bonito. {LE.escuchar("Hoy es un día bonito.", "Escuchar el modelo", 0.85)}</p>
<p class="oracion-ej">¿Tú quieres un café? {LE.escuchar("¿Tú quieres un café?", "Escuchar el modelo", 0.85)}</p>
<p class="oracion-ej">¡Qué buena pelota tira ese jugador! {LE.escuchar("¡Qué buena pelota tira ese jugador!", "Escuchar el modelo", 0.85)}</p>
<h3>Lectura acompañada</h3>
<p>Usted lee en voz alta <strong>al mismo tiempo</strong> que la voz, como quien canta junto con la radio: si va más despacio, la voz lo jala; si va más rápido, lo frena. Si se queda atrás, alcáncela en la frase siguiente.</p>
<div class="texto-lectura"><p>El sol sale por el este.</p><p>Mi mamá hace un café muy rico.</p><p>Los niños juegan en el parque del barrio.</p></div>
<p>{LE.escuchar("El sol sale por el este. Mi mamá hace un café muy rico. Los niños juegan en el parque del barrio.", "Escuchar las tres seguidas", 0.8)}</p>
{P("Compruebe", "En la <strong>lectura en eco</strong>, usted…", ["lee al mismo tiempo que la voz", "escucha la frase y después la repite igual", "lee en silencio"], 1,
   {0: "Eso es la lectura acompañada.", 2: "Las dos técnicas son en voz alta."}, "Primero escucha y <strong>después repite</strong>, imitando la entonación.")}"""

    s3 = f"""<p>Ahora junte todo: las <span class="fr fr-f">palabras frecuentes</span>, que lee de un vistazo, y las <span class="fr fr-b">palabras de dos sílabas</span> que aprendió a decodificar. Con ellas se arman <strong>frases de apoyo</strong>: oraciones sencillas, siempre parecidas, que dejan la cabeza libre para leer con entonación.</p>
{frase([("Yo", "f"), ("veo", "b"), ("un", "f"), ("perro.", "b")])}
{frase([("Yo", "f"), ("quiero", "b"), ("la", "f"), ("leche.", "b")])}
{frase([("Tú", "f"), ("tienes", "b"), ("una", "f"), ("bota.", "b")])}
{frase([("El", "f"), ("bebé", "b"), ("toma", "b"), ("la", "f"), ("leche.", "b")])}
<p>Y fíjese: estas frases también tienen sujeto y predicado, como vio en la Lección 1.2.</p>
<p class="oracion-ej"><span class="suj">El bebé</span> <span class="pred">toma la leche.</span></p>
<h3>Arme sus frases de apoyo</h3>
<p>Toque palabras <strong>en orden</strong>, de izquierda a derecha, y pulse <strong>Leer mi frase</strong>. La página le pone la mayúscula y el punto.</p>
<div class="constructor" data-grupos='{json.dumps([["yo", "tú", "el", "la", "un", "una", "mi", "con", "muy"], ["veo", "quiero", "tomo", "leche", "perro", "bota", "casa", "bebé", "taxi", "mesa", "sopa"]], ensure_ascii=False)}' data-sep=" " data-max="7" data-titulos='["Palabras frecuentes", "Palabras de dos sílabas"]'>
<div class="cons-fichas"></div>
<p><strong>Su frase:</strong></p><p class="cons-frase" aria-live="polite"></p>
<p><button type="button" class="btn cons-leer"><span aria-hidden="true">🔊</span> Leer mi frase</button> <button type="button" class="btn-sec cons-limpiar">Limpiar</button></p>
<div class="fb" role="status" aria-live="polite"></div><ul class="cons-lista" hidden></ul>
</div>
{C.caja("tip", "Versión en papel", "<p>Escriba en papelitos cinco palabras frecuentes (<em>yo, tú, el, la, un</em>) y cinco de dos sílabas (<em>mesa, casa, perro, leche, bota</em>). Combínelas, lea en voz alta las frases y copie las tres que más le gusten.</p>")}"""

    ej = SENALES[:4]
    s4 = f"""<p>Hay palabras que se leen todos los días en la calle, en la tienda y en el trabajo. Muchas van en mayúsculas y en carteles de colores; conviene reconocerlas de un vistazo, como las palabras frecuentes.</p>
<div class="materias">{"".join(f'<div><span class="placa {t}">{x}</span>{l}</div>' for x, t, l, o, k in ej)}</div>
<p>En la <a href="{C.prac(N)}#senales">página de práctica</a> hay dieciséis señales para leer y entender, y textos cortos para la lectura repetida.</p>
{P("Compruebe", '<span class="placa placa-ambar">PISO MOJADO</span>¿Qué quiere decir?', ["El piso está seco y limpio.", "Camine con cuidado: puede resbalar.", "No se puede caminar nunca más."], 1,
   {0: "Mojado es lo contrario de seco.", 2: "Es un aviso para tener cuidado, no una prohibición."}, "<strong>Camine con cuidado</strong>: el piso está mojado y puede resbalar.")}"""

    secciones = [("s1", "Las palabras que aparecen todo el tiempo", s1), ("s2", "Dos técnicas para ganar fluidez", s2),
                 ("s3", "De palabras a frases", s3), ("s4", "Señales y carteles de todos los días", s4)]
    tarea = [("Mis palabras frecuentes.", "Copie en su cuaderno las dieciséis tarjetas de la sección 1. Léalas en voz alta todos los días de esta semana."),
             ("Palabras al instante.", "Pase los cinco grupos de la sección 1 hasta que pueda leerlos a «Normal · 2 segundos» sin dudar."),
             ("Cinco frases de apoyo.", "Arme cinco frases con el constructor de la sección 3 y cópielas. Subraye el sujeto con una raya recta y el predicado con una ondulada."),
             ("Las señales de la calle.", "Camino a casa o al trabajo, busque tres señales y léalas en voz alta. Anótelas.")]
    quiz = [
        ("¿Qué son las <strong>palabras de uso frecuente</strong>?", ["Palabras largas y difíciles", "Palabras que aparecen muchísimo y conviene reconocer de un vistazo", "Palabras en inglés"], 1, {0: "Al contrario: suelen ser cortas.", 2: "Son del español."}, "Las que aparecen en casi todo y se leen <strong>de un vistazo</strong>."),
        ("¿Por qué conviene reconocerlas de un vistazo?", ["Para leer más rápido y con menos cansancio", "Porque no se pueden decodificar"], 0, {}, "Para leer <strong>con más soltura</strong>: se ahorra el trabajo de decodificarlas cada vez."),
        ("¿Cuál de estas es una palabra frecuente?", ["que", "murciélago", "helicóptero"], 0, {1: "Esa es larga y no aparece tanto.", 2: "Esa es larga y no aparece tanto."}, "<strong>que</strong>."),
        ("¿En qué oración <strong>él</strong> lleva tilde porque es una persona?", ["Él trabaja de noche.", "El trabajo es de noche."], 0, {}, "<strong>Él trabaja</strong>: él es la persona."),
        ("¿Cuáles son las tres partes de la fluidez?", ["Precisión, ritmo y expresión", "Letras, sílabas y palabras", "Volumen, prisa y memoria"], 0, {1: "Eso son partes de las palabras.", 2: "Ninguna de esas es parte de la fluidez."}, "<strong>Precisión, ritmo y expresión</strong>."),
        ("En la <strong>lectura acompañada</strong>, usted…", ["lee al mismo tiempo que la voz", "repite la frase después de oírla", "lee solo en silencio"], 0, {1: "Esa es la lectura en eco.", 2: "Es en voz alta."}, "Lee <strong>al mismo tiempo</strong> que la voz."),
        ("¿Qué es una <strong>frase de apoyo</strong>?", ["Una oración sencilla con palabras frecuentes y palabras conocidas", "Una lista de palabras sueltas", "Una oración muy larga"], 0, {1: "Las palabras sueltas no forman frase.", 2: "Al contrario: son cortas."}, "Una <strong>oración sencilla</strong> que ayuda a leer con soltura."),
        ("¿Cuál es el sujeto de <em>El bebé toma la leche</em>?", ["El bebé", "toma la leche", "la leche"], 0, {1: "Ese es el predicado.", 2: "La leche es lo que toma, no quién."}, "<span class=\"suj\">El bebé</span>."),
        ('<span class="placa placa-roja">ALTO</span>¿Qué quiere decir?', ["Siga sin parar", "Pare completamente antes de seguir", "Doble a la derecha"], 1, {0: "Es lo contrario.", 2: "No indica dirección."}, "<strong>Pare</strong> completamente antes de seguir."),
        ('<span class="placa placa-verde">SALIDA</span>¿Qué quiere decir?', ["Por aquí se entra", "Por aquí se sale", "Aquí se paga"], 1, {0: "Eso diría «Entrada».", 2: "Eso diría «Caja»."}, "Por aquí <strong>se sale</strong>."),
    ]
    filas = [
        ("Palabras frecuentes", "Leo las cincuenta palabras frecuentes sin dudar, a velocidad normal.", "Dudo con algunas, sobre todo las que llevan tilde.", "Todavía las decodifico (<a href=\"#s1\">repase la sección 1</a>)."),
        ("Leer frases con fluidez", "Leo frases de apoyo con entonación, sin pausas entre palabras.", "Leo bien, pero con voz plana.", "Me detengo en cada palabra (<a href=\"#s2\">repase la sección 2</a>)."),
        ("Señales", "Reconozco las señales de la calle y sé qué piden.", "Las leo, pero dudo de su significado.", "No las reconozco (<a href=\"#s4\">repase la sección 4</a>)."),
    ]
    cierre = ("<p>Terminó el Tema 2. Mire el camino: <strong>sonidos</strong> (2.1) → <strong>decodificación</strong> (2.2) → <strong>fluidez</strong> (2.3). Ese es el motor de la lectura: sin él, leer es un esfuerzo enorme; con él, la cabeza queda libre para <em>entender</em>, que es lo que pide el GED en los artículos, los textos de ciencias y las instrucciones.</p>"
              "<p>En el Tema 3 mirará por dentro las oraciones que ya sabe leer: qué palabras nombran las cosas, cuáles dicen cómo son y cuáles dicen qué pasa.</p>")
    glosario = [("Palabras de uso frecuente", "Las que aparecen en casi todos los textos: <em>el, de, que, en, y</em>… Se leen de un vistazo."),
                ("Lectura en eco", "Escuchar una frase y repetirla imitando la entonación."), ("Lectura acompañada", "Leer en voz alta al mismo tiempo que un modelo."),
                ("Prosodia", "La expresión al leer: pausas, entonación y énfasis."), ("Frase de apoyo", "Oración sencilla con palabras frecuentes y palabras conocidas.")]
    conexion = ("<p>Con esta lección cierra el Tema 2. En la 2.1 entrenó el oído y en la 2.2 aprendió a decodificar. Hoy le pone velocidad y naturalidad a esa lectura.</p>"
                "<p><strong>Lo que necesita:</strong> el cuaderno, unos papelitos y el volumen activado.</p>")
    estd = LE.estandares([], base=["L.1.1"], fund=["RF.3", "RF.4"])
    return C.pagina_leccion(N, LE.titulo(N), "Hay palabras que no se leen: se reconocen.", ["Fundamentos de lectura", "Fluidez"],
                            ["<strong>Reconocer de un vistazo</strong> las cincuenta palabras de uso más frecuente.", "<strong>Distinguir</strong> palabras frecuentes que solo se diferencian por la tilde (el/él, tu/tú).",
                             "<strong>Leer</strong> frases sencillas con fluidez, con lectura en eco y acompañada.", "<strong>Entender</strong> las señales y los carteles más comunes."],
                            estd, conexion, secciones, tarea, quiz, filas, cierre, ("3-1", LE.titulo("3-1")), glosario, P)


# ---------------------------------------------------------------- práctica
def banco_vista():
    b = []
    for _, ws in GRUPOS:
        for w in ws:
            dis = PARECIDAS.get(w, [])[:2]
            r = random.Random(w)
            while len(dis) < 2:
                x = r.choice([y for _, g in GRUPOS for y in g])
                if x != w and x not in dis:
                    dis.append(x)
            b.append({"enun": f"Toque la palabra <strong class=\"grande\">{w}</strong> {LE.escuchar(w, '', 0.8)}", "ops": [f'<span class="grande">{x}</span>' for x in [w] + dis], "ok": 0,
                      "pista": "Mírela letra por letra, y fíjese también en la tilde.", "exp": f"<strong>{w}</strong>."})
    return b


def banco_senales():
    return [{"enun": f'<span class="placa {t}">{x}</span><em>{l}</em><br>¿Qué quiere decir?', "ops": o, "ok": k,
             "pista": "Lea la señal en voz alta y piense en el lugar donde se ve.", "exp": f"<strong>{x}</strong>: {o[k][0].lower() + o[k][1:]}"} for x, t, l, o, k in SENALES]


def banco_comprension():
    b = []
    for tit, _, qs in LECTURAS:
        for q, o, k in qs:
            b.append({"enun": f"<em>{tit}</em> · {q}", "ops": o, "ok": k, "pista": f"Vuelva a leer «{tit}» y busque la oración que lo dice.", "exp": f"<strong>{o[k]}</strong>."})
    return b


def practica():
    textos = "".join(f'<h3>{tit}</h3>\n<p>{LE.escuchar(" ".join(o), "Escuchar el modelo", 0.85)}</p>\n<div class="texto-lectura" id="lec{i}">' + "".join(f"<p>{x}</p>" for x in o) +
                     f'</div>\n{crono("cr" + str(i), "lec" + str(i))}\n' for i, (tit, o, _) in enumerate(LECTURAS, 1))
    mods = [
        ("vista", "Palabras a simple vista", C.om("m1", "Busque la palabra entre otras parecidas. Si tiene voz, también puede escucharla.") + "\n" + LE.AVISO_VOZ),
        ("senales", "Señales y carteles", C.om("m2", "Lea la señal en voz alta y elija lo que significa.")),
        ("lectura-repetida", "Lectura repetida", f"      <p>Lea cada texto tres veces en voz alta con el cronómetro. La primera cuesta un poco; la tercera sale mucho mejor. El reloj es solo para ver su propio avance.</p>\n{textos}"),
        ("comprension", "¿Qué dice el texto?", C.om("m4", "Preguntas sobre los cuatro textos de la lectura repetida. Léalos antes.")),
    ]
    js = (C.js_datos("VIS", banco_vista()) + C.js_datos("SEN", banco_senales()) + C.js_datos("COM", banco_comprension()) +
          'creaBanco("m1", VIS);\ncreaBanco("m2", SEN);\ncreaBanco("m4", COM);\n')
    return C.pagina_practica(N, LE.titulo(N), "Cuatro actividades · los ejercicios cambian cada vez · dos intentos en cada uno", mods, js)


if __name__ == "__main__":
    LE.construye(N, leccion, practica, horas="Unas 3 horas")
