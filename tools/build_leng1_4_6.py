# -*- coding: utf-8 -*-
"""LearnGED · Artes del lenguaje (español) · Nivel 1 · Lección 4.6 · Raíces y afijos.
Fuente: clases_leng1/clase_4-6.html (GEDparaHispanos) y sus prácticas de gramatica, adaptadas al marco de LearnGED.
Uso: python3 tools/build_leng1_4_6.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import leng_es as LE
from leng_es import C

LE.nivel(1)
N = "4-6"
PREFIJOS = [("in- / im-", "no, lo contrario", "infeliz, imposible, inútil, incorrecto"), ("des-", "lo contrario, deshacer", "deshacer, desconocido, destapar, desconfiar"),
            ("re-", "otra vez", "rehacer, releer, revivir, recalentar"), ("pre-", "antes de", "prehistoria, prevenir, precalentar, preparar"),
            ("sub-", "debajo de", "submarino, subsuelo, subterráneo, subrayar"), ("auto-", "por uno mismo", "autoservicio, autorretrato, autoestima")]
SUFIJOS = [("-ito / -ita", "pequeño, con cariño", "casita, perrito, mesita"), ("-ón / -ona", "grande", "casona, sillón, cabezón"),
           ("-mente", "de manera… (forma adverbios)", "felizmente, rápidamente, fácilmente"), ("-dor / -dora", "persona o cosa que hace algo", "trabajador, lavadora, vendedor"),
           ("-ero / -era", "oficio, o lugar donde se guarda algo", "zapatero, panadero, florero"), ("-able / -ible", "que se puede", "lavable, reciclable, comestible")]
# (palabra con la parte en <b>, qué es la parte: 0 prefijo, 1 raíz, 2 sufijo)
PARTES = [("<b>in</b>feliz", 0), ("<b>des</b>conocido", 0), ("<b>re</b>leer", 0), ("<b>sub</b>marino", 0), ("<b>pre</b>venir", 0), ("<b>auto</b>servicio", 0),
          ("cas<b>ita</b>", 2), ("rápida<b>mente</b>", 2), ("trabaja<b>dor</b>", 2), ("lav<b>able</b>", 2), ("sill<b>ón</b>", 2), ("zapat<b>ero</b>", 2),
          ("des<b>hacer</b>", 1), ("in<b>útil</b>", 1), ("re<b>leer</b>", 1), ("<b>pan</b>adero", 1), ("<b>flor</b>ero", 1), ("<b>cas</b>ona", 1)]
# (palabra, significado, dos distractores)
SIGNIF = [("rehacer", "hacer otra vez", ["no hacer", "hacer antes"]), ("deshacer", "lo contrario de hacer", ["hacer otra vez", "hacer rápido"]),
          ("incorrecto", "que no es correcto", ["muy correcto", "correcto otra vez"]), ("prehistoria", "el tiempo antes de la historia escrita", ["la historia de hoy", "una historia corta"]),
          ("submarino", "que va debajo del mar", ["que vuela sobre el mar", "un marino importante"]), ("perrito", "un perro pequeño", ["un perro grande", "muchos perros"]),
          ("casona", "una casa grande", ["una casa pequeña", "una casa vieja"]), ("vendedor", "persona que vende", ["cosa vendida", "lugar donde se vende"]),
          ("lavable", "que se puede lavar", ["que está sucio", "que lava"]), ("felizmente", "de manera feliz", ["muy triste", "persona feliz"]),
          ("inquieto", "que no está quieto", ["muy quieto", "quieto otra vez"]), ("releer", "leer otra vez", ["no leer", "leer antes"]),
          ("panadero", "persona que hace pan", ["pan pequeño", "pan grande"]), ("incomprensible", "que no se puede comprender", ["muy fácil de entender", "que entiende mucho"])]
FAMILIAS = [("pan", ["panadero", "panadería", "empanada"], "pantalón"), ("flor", ["florero", "florista", "florecer"], "flojo"),
            ("libro", ["librería", "librero", "libreta"], "libre"), ("sol", ["soleado", "solar", "girasol"], "soldado"),
            ("zapato", ["zapatero", "zapatería", "zapatilla"], "zapallo"), ("agua", ["aguacero", "aguado", "paraguas"], "águila"),
            ("casa", ["casita", "casero", "casona"], "casco"), ("mesa", ["mesero", "mesita", "sobremesa"], "mes"),
            ("tierra", ["terreno", "terremoto", "aterrizar"], "tierno"), ("mar", ["marinero", "marea", "submarino"], "martes")]


def leccion():
    P = C.Practicas()
    s1 = f"""<p>En la Lección 4.5 usó las palabras vecinas para descubrir un significado. Ahora va a mirar <strong>dentro</strong> de la palabra. Las palabras del español se forman con piezas, como cubos.</p>
<p>La <strong>raíz</strong> es la parte que carga el significado principal, como el tronco de un árbol: de ella nacen muchas palabras. De la raíz <strong>cas-</strong> salen <em>casa, casita, casona, casero</em>: todas tienen que ver con la vivienda.</p>
<p>Los <strong>afijos</strong> son piezas pequeñas que se pegan a la raíz:</p>
<p class="bloques"><span class="ficha sil2">in-</span> + <span class="ficha sil">feliz</span> = <strong>infeliz</strong> &nbsp;·&nbsp; <span class="ficha sil">feliz</span> + <span class="ficha sil2">-mente</span> = <strong>felizmente</strong></p>
{C.tabla("Las piezas de una palabra", ["Pieza", "Dónde va", "Qué hace"],
         [["Prefijo", "Antes de la raíz", "Cambia el significado: niega, repite, dice antes o debajo…"], ["Raíz", "En el centro", "Carga el significado principal"],
          ["Sufijo", "Después de la raíz", "Cambia el tamaño o la función: diminutivo, persona que hace algo, de qué manera…"]])}
{P("Compruebe", "En <strong>infeliz</strong>, ¿qué es <em>in-</em>?", ["Un prefijo", "La raíz", "Un sufijo"], 0,
   {1: "La raíz es feliz: el significado principal.", 2: "El sufijo va al final."}, "Un <strong>prefijo</strong>: va antes y significa «no».")}"""

    s2 = f"""<h3>Prefijos comunes</h3>
{C.tabla("Prefijos comunes del español", ["Prefijo", "Significado", "Ejemplos"], [list(x) for x in PREFIJOS])}
{C.caja("tip", "Descifre sin diccionario", "<p>Si sabe que <em>quieto</em> significa «tranquilo, sin moverse», y que <em>in-</em> significa «no», entonces <em>inquieto</em> es «que no está tranquilo». Acaba de descifrar una palabra sin diccionario.</p>")}
<h3>Sufijos comunes</h3>
{C.tabla("Sufijos comunes del español", ["Sufijo", "Significado", "Ejemplos"], [list(x) for x in SUFIJOS])}
{C.caja("ojo", "Dos pistas rápidas", "<p>Si una palabra termina en <strong>-mente</strong>, casi siempre dice <em>de qué manera</em> se hace algo (<em>rápidamente</em>). Si termina en <strong>-dor / -dora</strong>, suele ser una persona o una cosa que hace una acción (<em>trabajador, lavadora</em>).</p>")}
{P("Compruebe", "¿Qué significa <strong>releer</strong>?", ["no leer", "leer otra vez", "leer antes"], 1, {0: "El prefijo de «no» es in- o des-.", 2: "El prefijo de «antes» es pre-."}, "<strong>re-</strong> = otra vez: leer otra vez.")}
{P("Compruebe", "¿Qué significa <strong>lavable</strong>?", ["que se puede lavar", "persona que lava", "que está limpio"], 0, {1: "Persona que lava sería lavador o lavadora.", 2: "-able no significa limpio."}, "<strong>-able</strong> = que se puede: que se puede lavar.")}"""

    s3 = f"""<p>Una <strong>familia de palabras</strong> es un grupo de palabras que comparten la raíz y el significado: <em>pan, panadero, panadería, empanada</em>. Cuidado: algunas palabras se parecen por fuera pero no tienen nada que ver. <em>Pantalón</em> empieza con «pan», pero no es de la familia: no tiene nada que ver con el pan.</p>
{P("Compruebe", "¿Qué palabra <strong>no</strong> es de la familia de <em>libro</em>?", ["librería", "libreta", "libre"], 2,
   {0: "Librería es donde venden libros: sí es de la familia.", 1: "Libreta es un cuaderno pequeño, de la familia de libro."}, "<strong>libre</strong> se parece, pero significa «que no está preso u ocupado»: no tiene que ver con libros.")}
<div class="caja caja-tip"><span class="etiqueta et-verde">Actividad · en su cuaderno</span>
<p>Elija una raíz: <em>hacer, casa, feliz, hablar</em> o <em>vivir</em>. En 5 minutos, escriba todas las palabras que pueda formar con prefijos (<em>re-, des-, in-, pre-</em>) y sufijos (<em>-ito, -ón, -mente, -dor, -ble</em>). Ponga la raíz en el centro de la página y las palabras alrededor, con su significado.</p></div>
<details class="caja caja-tip"><summary><strong>Ver un ejemplo con «hablar»</strong></summary>
<p><em>hablador</em> (persona que habla mucho), <em>habladuría</em> (chisme), <em>hablante</em> (persona que habla un idioma), <em>habla</em> (la forma de hablar). Fíjese que <em>«deshablar»</em> no existe: no todas las combinaciones forman palabras reales.</p></details>
{C.caja("tip", "Sus dos llaves para el vocabulario", "<p>Cuando encuentre una palabra que no conoce: primero, el <strong>contexto</strong> (¿qué dicen las palabras de alrededor?); después, la <strong>anatomía</strong> (¿reconozco la raíz o algún afijo?). Las dos juntas abren casi cualquier palabra del examen.</p>")}"""

    secciones = [("s1", "Las palabras tienen partes", s1), ("s2", "Prefijos y sufijos comunes", s2), ("s3", "Familias de palabras", s3)]
    tarea = [("Descomponga las palabras.", "Separe la raíz y los afijos y escriba qué significan: <em>trabajadora, incomprensible, releí, rápidamente</em>."),
             ("Compruebe.", "trabaja + dora: mujer que trabaja · in + comprens + ible: que no se puede comprender · re + leí: leí otra vez · rápida + mente: de manera rápida."),
             ("Mi familia de palabras.", "Pase en limpio la familia de la sección 3, con al menos 3 palabras que existan y lo que significa cada una."),
             ("A la caza de afijos.", "En un periódico, un empaque o un aviso, busque 5 palabras con prefijo o sufijo y sepárelas en sus partes.")]
    quiz = [
        ("¿Qué es la <strong>raíz</strong> de una palabra?", ["La parte que carga el significado principal", "La primera letra", "El acento"], 0, {1: "La raíz es una parte con significado.", 2: "El acento no es una pieza."}, "La parte con el <strong>significado principal</strong>."),
        ("¿Dónde va el <strong>prefijo</strong>?", ["Antes de la raíz", "Después de la raíz", "En medio de la raíz"], 0, {1: "Eso es el sufijo.", 2: "Los afijos van antes o después."}, "<strong>Antes</strong> de la raíz."),
        ("¿Qué significa <em>des-</em> en <strong>destapar</strong>?", ["lo contrario", "otra vez", "debajo"], 0, {1: "Otra vez es re-.", 2: "Debajo es sub-."}, "<strong>Lo contrario</strong>: quitar la tapa."),
        ("¿Qué significa <strong>imposible</strong>?", ["que no es posible", "muy posible", "posible otra vez"], 0, {1: "im- niega.", 2: "Otra vez sería re-."}, "<strong>Que no es posible</strong>."),
        ("¿Qué significa <strong>casita</strong>?", ["una casa pequeña", "una casa grande", "muchas casas"], 0, {1: "Grande sería casona.", 2: "Muchas sería casas."}, "<strong>Una casa pequeña</strong> (-ita)."),
        ("¿Qué tipo de palabra suele terminar en <strong>-mente</strong>?", ["Una que dice de qué manera", "Un sustantivo de persona", "Un lugar"], 0, {1: "Las personas suelen terminar en -dor, -ero.", 2: "No."}, "Dice <strong>de qué manera</strong>: rápidamente, fácilmente."),
        ("¿Qué es un <strong>vendedor</strong>?", ["persona que vende", "lo que se vende", "el lugar de venta"], 0, {1: "Eso es la mercancía.", 2: "Eso sería la tienda."}, "<strong>Persona que vende</strong> (-dor)."),
        ("¿Qué palabra <strong>no</strong> es de la familia de <em>pan</em>?", ["panadero", "pantalón", "empanada"], 1, {0: "El panadero hace pan.", 2: "La empanada tiene masa de pan."}, "<strong>pantalón</strong>: se parece por fuera, pero no tiene que ver con el pan."),
        ("¿Qué significa <strong>subterráneo</strong>?", ["debajo de la tierra", "sobre la tierra", "sin tierra"], 0, {1: "sub- significa debajo.", 2: "Sin sería in- o des-."}, "<strong>Debajo de la tierra</strong>."),
        ("¿Cuáles son las dos llaves para descifrar palabras nuevas?", ["El contexto y las partes de la palabra", "La suerte y la memoria"], 0, {}, "<strong>El contexto</strong> y <strong>la anatomía</strong> de la palabra."),
    ]
    filas = [
        ("Partes de la palabra", "Separo raíz, prefijo y sufijo en palabras nuevas.", "Encuentro la raíz, pero dudo con los afijos.", "No veo las partes (<a href=\"#s1\">repase la sección 1</a>)."),
        ("Significado de los afijos", "Sé qué significan in-, des-, re-, pre-, sub-, -ito, -ón, -mente, -dor, -able.", "Sé algunos.", "No los recuerdo (<a href=\"#s2\">repase la sección 2</a>)."),
        ("Familias de palabras", "Formo familias y encuentro la palabra que solo se parece por fuera.", "Me engañan las que se parecen.", "No sé qué es una familia (<a href=\"#s3\">repase la sección 3</a>)."),
    ]
    cierre = ("<p>Terminó el Tema 4. Ya tiene las cuatro estrategias del buen lector (predecir, preguntar, aclarar y resumir), sabe encontrar la idea principal y sus detalles, y tiene dos llaves para el vocabulario: el contexto y las partes de la palabra. Son exactamente las destrezas que pide la parte de lectura del examen GED.</p>"
              "<p>En el Tema 5 va a leer cuentos y a fijarse en quién hace qué y por qué: los <strong>personajes y sus conflictos</strong>.</p>")
    glosario = [("Raíz", "Parte de la palabra que carga el significado principal."), ("Prefijo", "Pieza que va antes de la raíz: <em>re-, des-, in-</em>."),
                ("Sufijo", "Pieza que va después de la raíz: <em>-ito, -mente, -dor</em>."), ("Afijo", "Nombre común de prefijos y sufijos."),
                ("Familia de palabras", "Grupo de palabras con la misma raíz y significado relacionado.")]
    conexion = ("<p>En la Lección 4.5 usó las palabras vecinas para descubrir un significado. Ahora va a aprender la segunda herramienta: mirar dentro de la palabra y separarla en sus piezas.</p>"
                "<p><strong>Lo que necesita:</strong> el cuaderno y un periódico, un empaque o un aviso.</p>")
    estd = LE.estandares(["R.4.1"], fund=["RF.3"])
    return C.pagina_leccion(N, LE.titulo(N), "Dentro de cada palabra hay piezas que cuentan lo que significa.", ["R.4.1 · Vocabulario", "Raíces y afijos"],
                            ["<strong>Separar</strong> una palabra en raíz, prefijo y sufijo.", "<strong>Usar</strong> los prefijos y sufijos más comunes para descifrar palabras.",
                             "<strong>Formar</strong> familias de palabras a partir de una raíz.", "<strong>Distinguir</strong> las palabras de una familia de las que solo se parecen por fuera."],
                            estd, conexion, secciones, tarea, quiz, filas, cierre, ("5-1", LE.titulo("5-1")), glosario, P)


def practica():
    Q = ["Prefijo", "Raíz", "Sufijo"]
    par = [{"enun": f"En <strong class=\"grande\">{w}</strong>, la parte en negrita es…", "ops": Q, "ok": k, "enOrden": True,
            "pista": "Prefijo: va antes y cambia el significado. Raíz: el significado principal. Sufijo: va al final.", "exp": f"Es <strong>{Q[k].lower()}</strong>."} for w, k in PARTES]
    sig = [{"enun": f"¿Qué significa <strong class=\"grande\">{w}</strong>?", "ops": [ok] + d, "ok": 0, "pista": "Separe la palabra en sus piezas y piense qué significa cada una.", "exp": f"<strong>{w}</strong>: {ok}."} for w, ok, d in SIGNIF]
    fam = [{"enun": f"¿Qué palabra <strong>no</strong> es de la familia de <strong>{r}</strong>?", "ops": a + [x], "ok": 3, "pista": "Busque la que se parece por fuera pero no comparte el significado.",
            "exp": f"<strong>{x}</strong> solo se parece por fuera: no tiene que ver con «{r}»."} for r, a, x in FAMILIAS]
    mods = [("partes", "¿Prefijo, raíz o sufijo?", C.om("m1", "Decida qué es la parte en negrita.")),
            ("significado", "Descifre la palabra", C.om("m2", "Use lo que sabe de los afijos.")),
            ("familias", "La palabra intrusa de la familia", C.om("m3", "Una palabra solo se parece por fuera."))]
    js = C.js_datos("PAR", par) + C.js_datos("SIG", sig) + C.js_datos("FAM", fam) + 'creaBanco("m1", PAR);\ncreaBanco("m2", SIG);\ncreaBanco("m3", FAM);\n'
    return C.pagina_practica(N, LE.titulo(N), "Tres actividades · los ejercicios cambian cada vez · dos intentos en cada uno", mods, js)


if __name__ == "__main__":
    LE.construye(N, leccion, practica, horas="Unas 3 horas")
