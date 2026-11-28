# -*- coding: utf-8 -*-
"""LearnGED · Artes del lenguaje (español) · Nivel 1 · Lección 7.3 · Tres tipos de texto: narrativo e informativo.
Fuente: clases_leng1/clase_7-3.html (GEDparaHispanos), adaptada al marco de LearnGED (esta lección no tenía práctica en gramatica:
la práctica se escribió aquí).
Uso: python3 tools/build_leng1_7_3.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import leng_es as LE
from leng_es import C

LE.nivel(1)
N = "7-3"
TIPOS = ["Narrativo", "Informativo", "De opinión"]
TEXTOS = [("Ayer fui al mercado con mi hija. Primero compramos frutas. Luego tomamos un café. Al final volvimos a casa en autobús.", 0, "cuenta lo que pasó, en orden y en pasado"),
          ("El mango es una fruta tropical. Contiene vitamina C y vitamina A. Se cultiva en México, la India y el Caribe.", 1, "da datos que se pueden comprobar, en presente"),
          ("Creo que el mango es la fruta más sabrosa. Me encanta su olor y su dulzura. Para mí, no hay nada mejor en verano.", 2, "dice lo que piensa la persona: creo, me encanta, para mí"),
          ("El sábado se fue la luz en todo el barrio. Primero buscamos las velas. Después mi hijo sacó la radio de pilas. Finalmente volvió la luz a medianoche.", 0, "cuenta sucesos en orden"),
          ("El lago Michigan es uno de los cinco Grandes Lagos. Es el único que está completamente dentro de los Estados Unidos.", 1, "presenta hechos de geografía"),
          ("Pienso que todos los barrios deberían tener un huerto comunitario, porque une a los vecinos.", 2, "expresa un punto de vista: pienso que, deberían"),
          ("La biblioteca pública presta libros gratis. También ofrece computadoras con internet y clases de inglés.", 1, "explica qué ofrece la biblioteca, sin opinar"),
          ("Cuando llegué a Chicago, no conocía a nadie. Un día entré a la biblioteca y me inscribí en una clase. Allí conocí a mi mejor amiga.", 0, "cuenta una experiencia personal en orden"),
          ("El corazón es un músculo que bombea la sangre a todo el cuerpo. Late unas 100,000 veces al día.", 1, "da datos científicos"),
          ("En mi opinión, el invierno de Chicago es demasiado largo. Prefiero mil veces el calor.", 2, "en mi opinión y prefiero marcan una opinión"),
          ("Mi abuelo llegó de Puerto Rico en 1965. Primero trabajó en una fábrica. Años después abrió su propia bodega.", 0, "cuenta la vida del abuelo en orden"),
          ("Las abejas llevan el polen de una flor a otra. Gracias a ellas crecen muchas frutas y verduras.", 1, "explica un hecho de la naturaleza")]
# (oración, True si es hecho)
HECHO = [("El plátano contiene potasio.", True), ("El plátano es la fruta más rica.", False), ("Cuba es la isla más grande del Caribe.", True), ("Cuba es un país hermoso.", False),
         ("El agua hierve a 100 °C al nivel del mar.", True), ("El agua caliente es más agradable que la fría.", False), ("Chicago está en el estado de Illinois.", True),
         ("Chicago es la ciudad más bonita del país.", False), ("La semana tiene siete días.", True), ("El lunes es el peor día de la semana.", False),
         ("El examen GED tiene cuatro materias.", True), ("La materia más fácil del GED es Estudios Sociales.", False), ("Los perros son mamíferos.", True), ("Los gatos son mejores mascotas que los perros.", False)]
NARR = [("La mañana del domingo", ["Primero, me levanté tarde y preparé café.", "Luego, salimos a caminar por el parque.", "Después, almorzamos arroz con pollo en familia.", "Finalmente, vimos una película antes de dormir."]),
        ("La mudanza", ["El año pasado nos mudamos a un apartamento nuevo.", "Primero, empacamos todo en cajas.", "Luego, unos amigos nos ayudaron a cargar el camión.", "Al final, dormimos la primera noche en el piso, entre las cajas."]),
        ("El primer día de clase", ["El lunes fue mi primer día en la clase del GED.", "Al llegar, la maestra me dio la bienvenida.", "Después, cada uno se presentó ante el grupo.", "Al final, salí contento y con muchas ganas de volver."])]
MISMO = [("📖 Narrativo", "Ayer comí lechón. Primero, mi tía sacó el cerdo del horno. Luego, pusimos la mesa con arroz blanco, frijoles negros y yuca. Finalmente, todos nos sentamos a comer y disfrutamos un almuerzo familiar inolvidable.", "Palabras de secuencia y verbos en pasado."),
         ("📊 Informativo", "La comida cubana es una mezcla de tradiciones. Combina ingredientes españoles, africanos e indígenas. Sus platos más conocidos son el lechón asado, los frijoles negros y el arroz congrí. Casi siempre se acompaña con plátano frito o yuca.", "Datos que se pueden comprobar, en presente."),
         ("💭 De opinión", "Me gusta mucho la comida cubana. Creo que es la más sabrosa del Caribe porque combina sabores fuertes y dulces a la vez. Además, los platos son abundantes y se comparten en familia. Por eso, siempre la elijo cuando salgo a comer.", "Marcas de opinión: me gusta, creo que.")]


def leccion():
    P = C.Practicas()
    s1 = f"""<p>No todos los párrafos tienen el mismo propósito: unos cuentan una historia, otros explican un tema y otros dan una opinión. Antes de escribir, pregúntese: <strong>¿para qué escribo?</strong> La respuesta decide el tipo de texto.</p>
{C.tabla("Tres tipos de texto", ["Tipo", "Pregunta", "Qué hace"],
         [["📖 Narrativo", "¿Qué pasó?", "Cuenta sucesos en orden."], ["📊 Informativo", "¿Qué es? ¿Cómo es?", "Da datos y hechos sobre un tema."], ["💭 De opinión", "¿Qué pienso?", "Expresa un punto de vista."]])}
<h3>Un mismo tema, tres textos</h3>
{C.tabla("La comida cubana, de tres maneras", ["Tipo", "Texto", "Cómo se nota"], [[a, f"<em>{b}</em>", c] for a, b, c in MISMO])}
{C.caja("tip", "Idea central", "<p>El <strong>propósito</strong> distingue un tipo de texto de otro. En esta lección estudiará los dos primeros; el de opinión, en la próxima.</p>")}"""

    s2 = f"""<p>Un texto <strong>narrativo</strong> cuenta algo que pasó: una experiencia real (un viaje, una anécdota familiar) o una historia inventada (un cuento).</p>
<ul><li>Responde a <strong>¿qué pasó?</strong></li><li>Tiene al menos dos sucesos ordenados en el tiempo.</li><li>Usa <strong>palabras de secuencia</strong> (Lección 5.3): primero, luego, después, finalmente.</li>
<li>Suele ir en <strong>pasado</strong>: comí, fui, vimos.</li><li>Tiene un protagonista. En las narraciones personales, es quien escribe: «yo».</li></ul>
<div class="texto-lectura"><p><strong>Mi mañana de domingo.</strong> El domingo pasado fue un día muy tranquilo en mi casa. <strong>Primero</strong>, me levanté tarde y preparé café para todos. <strong>Luego</strong>, mi esposa y yo salimos a caminar por el parque del barrio. <strong>Después</strong>, almorzamos arroz con pollo en familia. <strong>Finalmente</strong>, vimos una película juntos antes de acostarnos.</p></div>
{C.caja("tip", "Antes de escribir una narración", "<p>Haga una <strong>línea de tiempo</strong>: anote los sucesos en el orden en que pasaron (1. me levanté, 2. caminamos, 3. almorzamos, 4. vimos una película). Después escriba una oración para cada uno y únalas con palabras de secuencia.</p>")}
{P("Compruebe", "¿Qué señal muestra que «Mi mañana de domingo» es narrativo?", ["Las palabras de secuencia y los verbos en pasado", "Los datos con números", "Las palabras «creo que»"], 0,
   {1: "No tiene datos para comprobar.", 2: "No da una opinión."}, "<strong>Palabras de secuencia y verbos en pasado.</strong>")}"""

    s3 = f"""<p>Un texto <strong>informativo</strong> presenta hechos, datos o explicaciones sobre un tema, de forma objetiva. Está en los libros de texto, los periódicos, los manuales y casi todos los textos del GED de Ciencias y Estudios Sociales.</p>
<ul><li>Responde a <strong>¿qué es?</strong> o <strong>¿cómo es?</strong></li><li>Presenta datos que se pueden comprobar.</li><li>Evita las opiniones personales; usa un tono neutro.</li><li>Suele ir en <strong>presente</strong>: es, tiene, contiene.</li></ul>
{C.tabla("La regla de oro: hechos, no opiniones", ["Hecho ✅ (va en un texto informativo)", "Opinión ❌ (no va aquí)"],
         [["El plátano contiene potasio.", "El plátano es la fruta más rica."], ["Cuba es la isla más grande del Caribe.", "Cuba es un país hermoso."], ["El agua hierve a 100 °C al nivel del mar.", "El agua caliente es más agradable que la fría."]])}
{C.caja("tip", "Pruebe sus oraciones", "<p>Pregúntese: <strong>¿se puede comprobar?</strong> Si la respuesta es sí, es un hecho. Si es «depende de quién» o «depende del gusto», es una opinión: guárdela para otro tipo de texto.</p>")}
{P("Compruebe", "<em>Chicago está en el estado de Illinois.</em>", ["Es un hecho", "Es una opinión"], 0, {}, "Es un <strong>hecho</strong>: se puede comprobar en un mapa.")}
<div class="caja caja-tip"><span class="etiqueta et-verde">Actividad · en su cuaderno</span>
<p>Elija un tema que conozca: su país, su comida favorita o su trabajo. Escriba dos párrafos cortos: uno <strong>narrativo</strong> (algo que le pasó, con palabras de secuencia) y otro <strong>informativo</strong> (cuatro hechos que se puedan comprobar). Antes, haga la línea de tiempo y la lista de hechos.</p></div>"""

    secciones = [("s1", "Los tres tipos de texto", s1), ("s2", "El texto narrativo", s2), ("s3", "El texto informativo", s3)]
    tarea = [("Dos textos, un tema.", "Pase en limpio los dos párrafos de la sección 3."),
             ("Revise el narrativo.", "¿Tiene al menos tres sucesos en orden? ¿Usó palabras de secuencia? ¿Está en pasado?"),
             ("Revise el informativo.", "Lea cada oración y pregúntese: ¿se puede comprobar? Si alguna es opinión, cámbiela o quítela.")]
    quiz = [
        ("¿Qué decide el tipo de texto?", ["El propósito: para qué se escribe", "El largo", "El tema"], 0, {1: "No.", 2: "Un mismo tema da tres tipos de texto."}, "El <strong>propósito</strong>."),
        ("¿Qué pregunta responde el texto narrativo?", ["¿Qué pasó?", "¿Qué es?", "¿Qué pienso?"], 0, {1: "Esa es del informativo.", 2: "Esa es de la opinión."}, "<strong>¿Qué pasó?</strong>"),
        ("¿Qué pregunta responde el texto informativo?", ["¿Qué es? ¿Cómo es?", "¿Qué pasó?", "¿Qué pienso?"], 0, {1: "Esa es del narrativo.", 2: "Esa es de la opinión."}, "<strong>¿Qué es? ¿Cómo es?</strong>"),
        ("¿En qué tiempo suele estar un texto narrativo?", ["En pasado", "En presente", "En futuro"], 0, {1: "El presente es típico del informativo.", 2: "No."}, "En <strong>pasado</strong>."),
        ("¿Qué palabras son el motor del texto narrativo?", ["Las de secuencia", "Las de opinión", "Los números"], 0, {1: "Esas son de la opinión.", 2: "Esos son del informativo."}, "Las <strong>de secuencia</strong>."),
        ("<em>El corazón late unas 100,000 veces al día.</em>", ["Es un hecho", "Es una opinión"], 0, {}, "Un <strong>hecho</strong>: se puede comprobar."),
        ("<em>El lunes es el peor día de la semana.</em>", ["Es una opinión", "Es un hecho"], 0, {}, "Una <strong>opinión</strong>: depende de quién."),
        ("<em>El mango contiene vitamina C. Se cultiva en México y el Caribe.</em> ¿Qué tipo de texto es?", TIPOS, 1, {0: "No cuenta sucesos.", 2: "No dice qué piensa nadie."}, "<strong>Informativo.</strong>"),
        ("¿Qué conviene hacer antes de escribir una narración?", ["Una línea de tiempo con los sucesos", "Una lista de opiniones"], 0, {}, "Una <strong>línea de tiempo</strong>."),
        ("¿Qué tono usa el texto informativo?", ["Neutro y objetivo", "Emocionado y personal"], 0, {}, "<strong>Neutro y objetivo.</strong>"),
    ]
    filas = [
        ("Distinguir los tipos", "Digo si un texto es narrativo, informativo o de opinión y por qué.", "Distingo el narrativo, pero confundo los otros.", "No los distingo (<a href=\"#s1\">repase la sección 1</a>)."),
        ("Hecho u opinión", "Separo los hechos de las opiniones.", "A veces dudo.", "No veo la diferencia (<a href=\"#s3\">repase la sección 3</a>)."),
        ("Escribir", "Escribo un párrafo narrativo y uno informativo sobre el mismo tema.", "Escribo uno, pero el otro mezcla opiniones.", "No sé empezar (<a href=\"#s2\">repase la sección 2</a>)."),
    ]
    cierre = "<p>Ya sabe escribir para contar y para informar. En la próxima lección verá el tercer tipo: <strong>el texto de opinión</strong>, y comparará los tres.</p>"
    glosario = [("Texto narrativo", "Cuenta sucesos en orden."), ("Texto informativo", "Da hechos y datos sobre un tema."), ("Texto de opinión", "Expresa lo que alguien piensa."),
                ("Hecho", "Algo que se puede comprobar."), ("Opinión", "Lo que alguien piensa o siente."), ("Propósito", "Para qué se escribe un texto.")]
    conexion = ("<p>Ya conoce la estructura del párrafo y sus tres cualidades. Pero no todos los párrafos sirven para lo mismo. Un mismo tema —por ejemplo, la comida cubana— puede dar tres textos muy distintos, según para qué se escriba.</p>"
                "<p><strong>Lo que necesita:</strong> el cuaderno.</p>")
    estd = LE.estandares(["R.6.1", "W.1"], base=["R.3.1"])
    return C.pagina_leccion(N, LE.titulo(N), "Contar lo que pasó o explicar lo que es: dos propósitos, dos textos.", ["Tipos de texto", "Hecho y opinión"],
                            ["<strong>Distinguir</strong> el texto narrativo, el informativo y el de opinión por su propósito.", "<strong>Reconocer</strong> las señales del texto narrativo y del informativo.",
                             "<strong>Separar</strong> los hechos de las opiniones.", "<strong>Escribir</strong> un párrafo narrativo y uno informativo sobre el mismo tema."],
                            estd, conexion, secciones, tarea, quiz, filas, cierre, ("7-4", LE.titulo("7-4")), glosario, P)


def practica():
    tip = [{"enun": f"<div class=\"texto-lectura\"><p>{t}</p></div>¿Qué tipo de texto es?", "ops": TIPOS, "ok": k, "enOrden": True, "pista": "¿Cuenta lo que pasó, da datos o dice lo que alguien piensa?",
            "exp": f"Es <strong>{TIPOS[k].lower()}</strong>: {e}."} for t, k, e in TEXTOS]
    hec = [{"enun": f"<strong>{o}</strong><br>¿Es un hecho o una opinión?", "ops": ["Es un hecho", "Es una opinión"], "ok": 0 if h else 1, "enOrden": True, "pista": "",
            "exp": "Es un <strong>hecho</strong>: se puede comprobar." if h else "Es una <strong>opinión</strong>: depende de quién lo diga."} for o, h in HECHO]
    ini = [[2, 0, 3, 1], [3, 1, 0, 2], [1, 3, 2, 0]]
    ordn = [{"titulo": t, "intro": "Ordene los sucesos de la narración con los botones ▲ y ▼.", "pasos": p, "inicio": ini[i], "cons": {}, "general": "En una narración, los sucesos van en el orden en que pasaron, y las palabras de secuencia lo marcan."}
            for i, (t, p) in enumerate(NARR)]
    mods = [("tipo", "¿Qué tipo de texto es?", C.om("m1", "Lea el texto y decida su tipo.")),
            ("hecho", "¿Hecho u opinión?", C.om("m2", "¿Se puede comprobar o depende de quién lo diga?")),
            ("ordenar", "Ordene la narración", C.orden("m3"))]
    js = C.js_datos("TIP", tip) + C.js_datos("HEC", hec) + C.js_datos("ORD", ordn) + 'creaBanco("m1", TIP);\ncreaBanco("m2", HEC);\ncreaOrden("m3", ORD);\n'
    return C.pagina_practica(N, LE.titulo(N), "Tres actividades · los ejercicios cambian cada vez · dos intentos en cada uno", mods, js)


if __name__ == "__main__":
    LE.construye(N, leccion, practica, horas="Unas 3 horas")
