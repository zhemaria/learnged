# -*- coding: utf-8 -*-
"""LearnGED · Artes del lenguaje (español) · Nivel 2 · Lección 5.1 · Comparar y contrastar dos textos.
Fuente: clases_leng2/clase_5-1.html (GEDparaHispanos) y gramatica/n2-l5-1.html, adaptadas al marco de LearnGED.
Uso: python3 tools/build_leng2_5_1.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import leng_es as LE
from leng_es import C

LE.nivel(2)
N = "5-1"
VENN_OPS = ["Solo A", "Los dos", "Solo B"]
PARES = [
    ("Vivir en la ciudad tiene muchas ventajas. Hay trabajo, hospitales cerca y transporte público. Los niños tienen escuelas a pocas cuadras. Eso sí, los alquileres son caros.",
     "Vivir en el campo es más tranquilo. Hay aire limpio, menos tráfico y los vecinos se conocen. Eso sí, los hospitales y las escuelas quedan lejos, y no hay transporte público.",
     [("Hay transporte público.", 0), ("Hay aire limpio y menos tráfico.", 2), ("Menciona una desventaja del lugar.", 1), ("Las escuelas están cerca.", 0), ("Los vecinos se conocen.", 2), ("Habla de dónde quedan los hospitales.", 1)]),
    ("El perro es el mejor compañero: es fiel, cuida la casa y obliga a salir a caminar. Necesita paseos todos los días y mucha atención.",
     "El gato es ideal para quien trabaja muchas horas: es independiente y no necesita paseos. Igual que el perro, da cariño y compañía.",
     [("Da cariño y compañía.", 1), ("Necesita paseos diarios.", 0), ("Es independiente.", 2), ("Cuida la casa.", 0), ("Es bueno para quien trabaja mucho.", 2), ("Presenta a una mascota como buena opción.", 1)]),
    ("Pagar en efectivo ayuda a controlar los gastos: cuando el dinero se acaba, uno deja de comprar. Además, no hay intereses.",
     "Pagar con tarjeta de débito es más seguro que llevar efectivo, porque si se pierde se puede bloquear. Como con el efectivo, se gasta solo el dinero que se tiene y no se pagan intereses.",
     [("No se pagan intereses.", 1), ("Se puede bloquear si se pierde.", 2), ("Cuando el dinero se acaba, uno deja de comprar.", 0), ("Se gasta solo el dinero que se tiene.", 1), ("Es más seguro que llevar efectivo.", 2)]),
    ("Leer libros en papel es un placer: se puede subrayar, se descansa la vista y no se necesita batería. Además, un libro bonito se puede regalar.",
     "Leer en el celular es práctico: se lleva una biblioteca entera en el bolsillo y muchos libros son gratis. Pero cansa la vista y depende de la batería.",
     [("No necesita batería.", 0), ("Muchos libros son gratis.", 2), ("Habla de la vista.", 1), ("Se lleva una biblioteca en el bolsillo.", 2), ("Se puede regalar.", 0)])]
SD = [("El ejercicio", "«Caminar media hora al día mejora la salud del corazón.»", "«Un paseo diario de treinta minutos protege el corazón.»", 0, "Dicen lo mismo con otras palabras."),
      ("La comida rápida", "«La comida rápida es barata y práctica para quien trabaja.»", "«La comida rápida parece barata, pero a la larga daña la salud.»", 1, "El primero la defiende; el segundo, no."),
      ("El teléfono en clase", "«El celular distrae a los estudiantes.»", "«El celular puede ser una buena herramienta para aprender.»", 1, "Ven el celular de manera opuesta."),
      ("El reciclaje", "«Reciclar reduce la basura que llega a los vertederos.»", "«Gracias al reciclaje, hay menos desechos en los basureros.»", 0, "Es la misma idea."),
      ("El invierno", "«El invierno en Chicago es duro por el viento y la nieve.»", "«Los inviernos de Chicago son difíciles: el viento helado y la nieve no perdonan.»", 0, "Coinciden en que es duro y en las razones."),
      ("El trabajo nocturno", "«Trabajar de noche paga mejor.»", "«El turno de noche afecta el sueño y la salud.»", 1, "Uno ve una ventaja; el otro, un problema."),
      ("Las bibliotecas", "«Las bibliotecas son un servicio gratuito para todos.»", "«Cualquier persona puede usar la biblioteca sin pagar.»", 0, "Dicen lo mismo."),
      ("Comprar en línea", "«Comprar en línea ahorra tiempo.»", "«Comprar en la tienda permite ver y tocar el producto antes de pagar.»", 1, "Cada uno defiende una forma distinta de comprar."),
      ("Los abuelos", "«Los abuelos transmiten la lengua y las tradiciones.»", "«Gracias a los abuelos, muchos niños aprenden el español y las costumbres de la familia.»", 0, "La misma idea, con un ejemplo."),
      ("El transporte", "«El autobús es lento y casi siempre llega tarde.»", "«El autobús es una forma cómoda y puntual de moverse.»", 1, "Opiniones opuestas sobre el mismo servicio.")]
CONEC = [("___ textos hablan del mismo tema.", ["Ambos", "En cambio", "Mientras que"]), ("Ana prefiere el campo; Luis, ___, prefiere la ciudad.", ["en cambio", "también", "al igual que"]),
         ("___ su madre, Rosa es enfermera.", ["Al igual que", "A diferencia de", "Sin embargo"]), ("El texto A da datos, ___ el texto B cuenta una historia.", ["mientras que", "ambos", "también"]),
         ("___ el perro, el gato no necesita paseos.", ["A diferencia de", "Al igual que", "Tanto"]), ("Los dos autores hablan del dinero. ___, sus opiniones son distintas.", ["Sin embargo", "Además", "Ambos"]),
         ("Pedro trabaja de noche, y su esposa ___.", ["también", "en cambio", "mientras que"]), ("___ mi hijo como mi hija terminaron la escuela.", ["Tanto", "Ambos", "Mientras"]),
         ("El primer anuncio exagera; el segundo, ___, da datos reales.", ["por el contrario", "también", "al igual que"]), ("___ autores reconocen que el problema es grave.", ["Los dos", "A diferencia de", "En cambio"])]
TA = "Desde hace un año trabajo desde casa tres días por semana, y mi vida cambió. Antes pasaba casi dos horas al día en el tren; ahora uso ese tiempo para desayunar con mis hijos. Ahorro unos ochenta dólares al mes en transporte y en comida. Además, en casa me concentro mejor: no hay ruido ni interrupciones. Creo que todas las empresas que puedan deberían ofrecer esta opción."
TB = "En mi oficina, la mitad del equipo trabaja desde casa tres días por semana. Reconozco que así se ahorra tiempo de transporte. Pero he notado algunos problemas: varios empleados se sienten solos, y es más difícil resolver una duda rápida cuando no se tiene a un compañero al lado. Además, no todos tienen en casa un espacio tranquilo para trabajar. Pienso que el trabajo desde casa funciona, pero solo si la empresa ayuda a cada empleado a organizarse."
VENN = [("Se trabaja desde casa tres días por semana.", 1), ("Se ahorra tiempo de transporte.", 1), ("Se ahorra dinero en transporte y en comida.", 0), ("En casa hay menos ruido y uno se concentra mejor.", 0),
        ("Algunos empleados se sienten solos.", 2), ("No todos tienen en casa un espacio tranquilo.", 2), ("Todas las empresas que puedan deberían ofrecerlo.", 0), ("Funciona solo si la empresa ayuda a organizarse.", 2)]
U = ('<div class="dos-textos"><div class="texto-lectura"><p><strong>Texto 1:</strong> «Los uniformes escolares ahorran dinero a las familias: no hay que comprar tanta ropa. Además, los niños no compiten por quién tiene la ropa más cara. Las escuelas deberían exigirlos.»</p></div>'
     '<div class="texto-lectura tb"><p><strong>Texto 2:</strong> «Los uniformes escolares pueden ahorrar algo de dinero, pero no dejan que los niños expresen su personalidad. Prefiero que cada familia decida cómo vestir a sus hijos.»</p></div></div>')


def dos(a, b, ta="Texto A", tb="Texto B"):
    return f'<div class="dos-textos"><div class="texto-lectura"><p><strong>{ta}:</strong> {a}</p></div><div class="texto-lectura tb"><p><strong>{tb}:</strong> {b}</p></div></div>'


def venn_svg(lleno):
    """Diagrama de Venn: vacío (lleno=False) o con las ideas de la lectura."""
    col = {0: [], 1: [], 2: []}
    if lleno:
        for t, k in VENN:
            col[k].append(t)
    def textos(x, lista, ancho=18):
        out = ""
        y = 120 - 14 * len(lista)
        for t in lista:
            pal = t.rstrip(".").split(); lineas = []; cur = ""
            for w in pal:
                if len(cur + " " + w) > ancho: lineas.append(cur); cur = w
                else: cur = (cur + " " + w).strip()
            lineas.append(cur)
            for ln in lineas:
                out += f'<text x="{x}" y="{y}" text-anchor="middle" font-size="11.5">{ln}</text>'; y += 14
            y += 8
        return out
    desc = ("Dos círculos que se cruzan. El izquierdo dice Solo el texto A, el derecho dice Solo el texto B y la zona del centro dice Los dos." if not lleno else
            "Solo A: " + "; ".join(col[0]) + ". Los dos: " + "; ".join(col[1]) + ". Solo B: " + "; ".join(col[2]) + ".")
    return f"""<svg viewBox="0 0 560 270" role="img" aria-label="Diagrama de Venn. {desc}" style="max-width:560px;width:100%">
<circle cx="205" cy="140" r="125" fill="#dbeafe" fill-opacity=".75" stroke="#1e40af" stroke-width="2"/><circle cx="355" cy="140" r="125" fill="#fce7f3" fill-opacity=".7" stroke="#9d174d" stroke-width="2"/>
<text x="130" y="22" text-anchor="middle" font-weight="800" font-size="14" fill="#1e40af">Solo A</text><text x="280" y="22" text-anchor="middle" font-weight="800" font-size="14">Los dos</text><text x="430" y="22" text-anchor="middle" font-weight="800" font-size="14" fill="#9d174d">Solo B</text>
{textos(140, col[0])}{textos(280, col[1], 13)}{textos(420, col[2])}</svg>"""


def leccion():
    P = C.Practicas()
    s1 = f"""<p>Comparamos todo el tiempo: dos ofertas de trabajo, dos apartamentos, dos médicos. Con los textos pasa lo mismo. Dos personas pueden escribir sobre el mismo tema y decir cosas muy distintas, o decir lo mismo con otras palabras. En el GED, varias preguntas de Artes del Lenguaje y la respuesta extendida trabajan con <strong>dos textos a la vez</strong>, así que esta destreza es clave.</p>
{C.tabla("Comparar y contrastar", ["Verbo", "Significa", "Pregunta"], [["Comparar", "Buscar las semejanzas: en qué se parecen.", "¿Qué tienen en común?"], ["Contrastar", "Buscar las diferencias: en qué no se parecen.", "¿En qué se distinguen?"]])}
{C.caja("tip", "En la vida diaria", "<p>Se dice «comparar» para las dos cosas. Cuando un examen pide «comparar y contrastar», espera que hable de las semejanzas <strong>y</strong> de las diferencias.</p>")}
<p>Dos textos sobre el mismo tema pueden parecerse o diferenciarse en cinco aspectos:</p>
{C.tabla("Aspectos para comparar dos textos", ["Aspecto", "Pregunta"],
         [["Tema", "¿Hablan de lo mismo?"], ["Información", "¿Qué datos, ejemplos o razones da cada uno? ¿Cuáles da uno y no el otro?"], ["Punto de vista", "¿Qué piensa cada autor? ¿Está a favor, en contra o con dudas?"],
          ["Propósito", "¿Para qué escribió cada uno: informar, entretener o persuadir?"], ["Tipo de texto", "¿Es una noticia, una opinión, un cuento, una carta?"]])}
{C.caja("tip", "El punto de vista", "<p>Es la posición del autor frente al tema. Se descubre en las palabras que muestran su opinión: <em>creo, pienso, debería, por desgracia, por suerte, lo mejor, el problema es…</em> Dos autores pueden dar los mismos datos y llegar a opiniones distintas.</p>")}
{P("Compruebe", "<strong>Contrastar</strong> dos textos es…", ["buscar sus diferencias", "buscar sus semejanzas", "resumir los dos en una oración"], 0, {1: "Eso es comparar.", 2: "Eso es resumir."}, "Buscar sus <strong>diferencias</strong>.")}"""

    cx = [("«Ambos autores viven en Chicago.»", 0, "<em>Ambos</em> señala algo en común."), ("«Ana prefiere el tren; Luis, en cambio, maneja.»", 1, "<em>en cambio</em> marca una diferencia."),
          ("«Al igual que su hermana, Marta estudia de noche.»", 0, "<em>al igual que</em>: semejanza."), ("«El primer texto da datos, mientras que el segundo cuenta una historia.»", 1, "<em>mientras que</em>: diferencia.")]
    s2 = f"""{C.tabla("Conectores para comparar y contrastar", ["Para señalar semejanzas", "Para señalar diferencias"],
         [["<strong>ambos, los dos:</strong> Ambos textos hablan del trabajo.", "<strong>en cambio:</strong> Gloria está contenta; Raúl, en cambio, ve problemas."],
          ["<strong>al igual que:</strong> Al igual que Gloria, Raúl reconoce el ahorro de tiempo.", "<strong>mientras que:</strong> Gloria lo ve fácil, mientras que Raúl ve dificultades."],
          ["<strong>también:</strong> Raúl también menciona el transporte.", "<strong>a diferencia de:</strong> A diferencia de Gloria, Raúl es supervisor."],
          ["<strong>tanto… como…:</strong> Tanto Gloria como Raúl trabajan en oficinas.", "<strong>sin embargo, por el contrario:</strong> Sin embargo, sus opiniones son distintas."]], fila_th=False)}
{C.caja("ojo", "Repaso de concordancia", "<p><em>Tanto Gloria como Raúl</em> son dos personas: el verbo va en plural, <em>Tanto Gloria como Raúl <strong>trabajan</strong></em>. Y recuerde la coma después de <em>sin embargo</em> al comienzo.</p>")}
{"".join(P("¿Semejanza o diferencia?", t, ["Semejanza", "Diferencia"], k, {1 - k: "Mire el conector."}, f"<strong>{['Semejanza', 'Diferencia'][k]}</strong>: {e}") for t, k, e in cx)}"""

    s3 = f"""<p>Lea los dos textos. Mientras lee, haga dos columnas en su cuaderno, una para cada autora o autor, y anote en una palabra o frase cada idea que encuentre. Después marque con una estrella las ideas que aparecen en los dos.</p>
<div class="dos-textos"><div class="texto-lectura"><p><strong>Texto A · Trabajar desde casa: una bendición</strong><br><em>Gloria, asistente administrativa</em></p><p>{TA}</p>{LE.escuchar(TA, "Escuchar el texto A")}</div>
<div class="texto-lectura tb"><p><strong>Texto B · Trabajar desde casa: no es para todos</strong><br><em>Raúl, supervisor</em></p><p>{TB}</p>{LE.escuchar(TB, "Escuchar el texto B")}</div></div>
<p class="fuente">Gloria y Raúl son personajes creados para esta lección; sus cifras no son datos reales.</p>
{P("Pregunta 1", "¿Cuál es el punto de vista de Gloria?", ["Está completamente a favor", "Está en contra", "No da su opinión"], 0, {1: "Habla de una bendición.", 2: "Dice «creo que…»."}, "«Una bendición», «mi vida cambió», «todas las empresas deberían».")}
{P("Pregunta 2", "¿Cuál es el punto de vista de Raúl?", ["Está completamente en contra", "Está a favor, pero con condiciones", "Está completamente a favor"], 1, {0: "Dice que funciona.", 2: "Pone una condición."}, "«Funciona, pero solo si la empresa ayuda».")}
{P("Pregunta 3", "¿Qué palabras muestran la opinión de Raúl?", ["«En mi oficina» y «tres días»", "«Pienso que» y «solo si»", "«La mitad del equipo»"], 1, {0: "Son datos.", 2: "Es un dato."}, "<em>Pienso que</em> anuncia una opinión; <em>solo si</em> pone una condición.")}
{P("Pregunta 4", "¿Por qué los dos ven el tema de manera distinta?", ["Porque viven en ciudades diferentes", "Porque ella es empleada y él supervisa a todo un equipo", "Porque Raúl no sabe usar la computadora"], 1, {0: "El texto no lo dice.", 2: "El texto no lo dice."}, "Gloria habla de su propia vida; Raúl, de lo que observa en todo su equipo.")}
<h3>El diagrama de Venn</h3>
<p>Un diagrama de Venn son dos círculos que se cruzan. En cada círculo van las ideas de un solo texto; en el centro, donde se juntan, van las que comparten.</p>
<figure class="venn">{venn_svg(False)}</figure>
<p>Copie el diagrama en su cuaderno y coloque cada idea de la lectura en su lugar:</p>
<ol>{"".join(f"<li>{t}</li>" for t, _ in VENN)}</ol>
<details class="caja caja-tip"><summary><strong>Ver el diagrama completo</strong></summary><figure class="venn">{venn_svg(True)}</figure></details>
{C.caja("ojo", "Cuidado con lo parecido", "<p>Los dos hablan del transporte, pero Gloria habla de dinero y de tiempo, y Raúl solo de tiempo. Por eso el ahorro de tiempo va en el centro y el ahorro de dinero, solo en A. Comparar bien exige leer con precisión.</p>")}
<div class="caja caja-tip"><span class="etiqueta et-verde">Actividad · escriba la comparación</span>
<p>Use su diagrama de Venn para escribir un párrafo que compare los dos textos. Puede seguir esta plantilla:</p>
<p class="formula">Los dos textos hablan de <em>tema</em>. Ambos <em>semejanza</em>. Sin embargo, sus puntos de vista son distintos. <em>Autor A</em> piensa que <em>opinión A</em>, porque <em>razón</em>. En cambio, <em>autor B</em> <em>opinión B</em>, ya que <em>razón</em>.</p>
<details><summary><strong>Ver un párrafo modelo</strong></summary><p>Los dos textos hablan de trabajar desde casa tres días por semana, y ambos reconocen que así se ahorra tiempo de transporte. Sin embargo, sus puntos de vista son distintos. Gloria piensa que es una bendición, porque ahorra dinero, pasa más tiempo con sus hijos y se concentra mejor. En cambio, Raúl ve algunos problemas, como la soledad de los empleados y la falta de un espacio tranquilo en casa. Mientras que Gloria quiere que todas las empresas lo ofrezcan, Raúl cree que solo funciona si la empresa ayuda a cada persona a organizarse.</p></details>
<p>Si tiene con quién practicar, pregúntele a alguien de su casa qué piensa de trabajar desde casa. Compare su opinión con la de Gloria y la de Raúl: ¿a cuál se parece más?</p></div>"""

    secciones = [("s1", "Comparar, contrastar y qué se compara", s1), ("s2", "Las palabras de la comparación", s2), ("s3", "Lectura paralela: trabajar desde casa", s3)]
    tarea = [("Dos noticias.", "Busque la misma noticia en dos periódicos o sitios distintos. Haga un diagrama de Venn: ¿qué dicen los dos? ¿Qué dato da uno y el otro no?"),
             ("Dos lugares.", "Escriba un párrafo que compare su país de origen (o el de su familia) con la ciudad donde vive ahora. Use al menos cuatro conectores de la sección 2."),
             ("Dos opiniones.", "Escriba dos opiniones cortas sobre un mismo tema (por ejemplo, el uso del celular en la escuela): una a favor y otra con dudas. Luego compárelas en tres oraciones.")]
    quiz = [
        ("El <strong>punto de vista</strong> de un autor es…", ["su posición u opinión frente al tema", "el lugar donde escribió el texto", "la cantidad de datos que da"], 0, {1: "No es un lugar.", 2: "Los datos no son la opinión."}, "Su <strong>posición</strong> frente al tema."),
        ("¿Qué palabras suelen mostrar la opinión del autor?", ["creo, pienso, debería", "ayer, hoy, mañana", "aquí, allí, cerca"], 0, {1: "Indican tiempo.", 2: "Indican lugar."}, "<strong>creo, pienso, debería.</strong>"),
        ("¿Qué conector señala una <strong>semejanza</strong>?", ["al igual que", "en cambio", "mientras que"], 0, {1: "Señala diferencia.", 2: "Señala diferencia."}, "<strong>al igual que.</strong>"),
        ("¿Qué conector señala una <strong>diferencia</strong>?", ["a diferencia de", "ambos", "también"], 0, {1: "Señala semejanza.", 2: "Señala semejanza."}, "<strong>a diferencia de.</strong>"),
        ("En un diagrama de Venn, en el centro van…", ["las ideas que comparten los dos textos", "las ideas que solo tiene el primer texto", "los títulos de los dos textos"], 0, {1: "Esas van en el círculo de A.", 2: "Los títulos no van en el diagrama."}, "Las ideas <strong>compartidas</strong>."),
        (U + "¿En qué coinciden los dos textos?", ["En que los uniformes pueden ahorrar dinero", "En que los uniformes deben ser obligatorios", "En que los niños compiten por la ropa"], 0, {1: "Solo lo dice el texto 1.", 2: "Solo lo dice el texto 1."}, "Los dos hablan del <strong>ahorro</strong>."),
        (U + "¿Cuál es el punto de vista del texto 1?", ["A favor de exigir uniformes", "En contra de los uniformes", "No da ninguna opinión"], 0, {1: "Dice que deberían exigirlos.", 2: "Dice «deberían»."}, "<strong>A favor.</strong>"),
        (U + "¿Qué idea aparece solo en el texto 2?", ["Los uniformes no dejan expresar la personalidad", "Los uniformes ahorran algo de dinero", "Las escuelas deberían exigirlos"], 0, {1: "Lo dicen los dos.", 2: "Lo dice el texto 1."}, "La <strong>personalidad</strong>."),
        (U + "¿Qué oración compara bien los dos textos?", ["El texto 1 quiere uniformes obligatorios, mientras que el texto 2 prefiere que decida cada familia.", "Los dos textos están completamente de acuerdo sobre los uniformes escolares.", "El texto 2 dice que los uniformes son demasiado caros para las familias."], 0,
         {1: "Tienen opiniones distintas.", 2: "El texto 2 no dice eso."}, "Usa <strong>mientras que</strong> y resume bien las dos posturas."),
        ("Complete: «Tanto Gloria como Raúl ___ en una oficina.»", ["trabajan", "trabaja", "trabajamos"], 0, {1: "Son dos personas.", 2: "No incluye a «nosotros»."}, "<strong>trabajan</strong>: plural."),
    ]
    filas = [
        ("Aspectos", "Comparo tema, información, punto de vista, propósito y tipo de texto.", "Comparo el tema y la información.", "Solo resumo cada texto por separado (<a href=\"#s1\">repase la sección 1</a>)."),
        ("Conectores", "Uso conectores de semejanza y de diferencia, con buena concordancia.", "Uso pocos conectores.", "No uso conectores (<a href=\"#s2\">repase la sección 2</a>)."),
        ("Diagrama de Venn", "Coloco con precisión las ideas propias y las compartidas.", "Me confundo con ideas parecidas.", "No sé usar el diagrama (<a href=\"#s3\">repase la sección 3</a>)."),
    ]
    cierre = "<p>Ya sabe poner dos textos uno junto al otro. En la próxima lección verá cómo descubrir el significado de una palabra con <strong>pistas, afijos y raíces</strong>.</p>"
    glosario = [("Comparar", "Buscar las semejanzas."), ("Contrastar", "Buscar las diferencias."), ("Punto de vista", "La posición del autor frente al tema."),
                ("Diagrama de Venn", "Dos círculos que se cruzan para ordenar lo propio de cada texto y lo que comparten.")]
    conexion = ("<p>En el Nivel 1 comparó personajes y objetos con un diagrama de Venn. Ahora comparará dos textos enteros: sus datos, sus opiniones y sus propósitos. Es la base de la respuesta extendida del GED.</p>"
                "<p><strong>Lo que necesita:</strong> el cuaderno y lápices de dos colores.</p>")
    estd = LE.estandares(["R.9.1/R.7.1", "R.9.2"], base=["R.6.1", "R.5.3"])
    return C.pagina_leccion(N, LE.titulo(N), "Dos autores, un mismo tema: dónde coinciden y dónde no.", ["Lectura", "Comparar textos"],
                            ["<strong>Distinguir</strong> comparar de contrastar.", "<strong>Reconocer</strong> el punto de vista de cada autor.",
                             "<strong>Ordenar</strong> las ideas de dos textos en un diagrama de Venn.", "<strong>Escribir</strong> una comparación con conectores."],
                            estd, conexion, secciones, tarea, quiz, filas, cierre, ("5-2", LE.titulo("5-2")), glosario, P)


def practica():
    ve = []
    for a, b, ideas in PARES:
        for t, k in ideas:
            ve.append({"enun": dos(a, b) + f"<p class=\"formula\">{t}</p><strong>¿Dónde va esta idea en el diagrama de Venn?</strong>", "ops": VENN_OPS, "ok": k, "enOrden": True,
                       "pista": "Vuelva a buscar esa idea en los dos textos.", "exp": f"<strong>{VENN_OPS[k]}</strong>."})
    sd = [{"enun": f"<p>Tema: <strong>{t}</strong></p>" + dos(a, b, "A", "B") + "<strong>¿Se parecen o se oponen?</strong>", "ops": ["Semejanza", "Diferencia"], "ok": k, "enOrden": True,
           "pista": "Fíjese en la opinión de cada autor: ¿piensan lo mismo o lo contrario?", "exp": f"<strong>{['Semejanza', 'Diferencia'][k]}</strong>. {e}"} for t, a, b, k, e in SD]
    def may(s): return s[0].upper() + s[1:]
    co = [{"enun": f"<span class=\"grande\">{o.replace('___', '_____')}</span>", "ops": ops, "ok": 0, "pista": "¿La oración señala algo en común o una diferencia?",
           "exp": f"«{may(o.replace('___', ops[0]))}»"} for o, ops in CONEC]
    mods = [("venn", "Diagrama de Venn", C.om("m1", "Lea los dos textos y decida si la idea está solo en A, en los dos o solo en B.")),
            ("semejanza", "¿Semejanza o diferencia?", C.om("m2", "Decida si dos afirmaciones sobre el mismo tema se parecen o se oponen.")),
            ("conectores", "Conectores de comparación", C.om("m3", "Elija el conector que completa la oración."))]
    js = C.js_datos("VE", ve) + C.js_datos("SD", sd) + C.js_datos("CO", co) + 'creaBanco("m1", VE);\ncreaBanco("m2", SD);\ncreaBanco("m3", CO);\n'
    return C.pagina_practica(N, LE.titulo(N), "Tres actividades · los ejercicios cambian cada vez · dos intentos en cada uno", mods, js)


if __name__ == "__main__":
    LE.construye(N, leccion, practica, horas="Unas 3 horas")
