# -*- coding: utf-8 -*-
"""LearnGED · Artes del lenguaje (español) · Nivel 1 · Lección 2.1 · Conciencia fonológica.
Fuente: clases_leng1/clase_2-1.html (GEDparaHispanos), adaptada al marco de LearnGED.
Los sonidos sueltos (sal, nube, ratón, mesa, sol, luna, foca) son grabaciones del profesor en
es/artes-del-lenguaje/audio/; mientras no existan, el botón queda oculto y se ve la nota «Dígalo en voz alta».
Uso: python3 tools/build_leng1_2_1.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import leng_es as LE
from leng_es import C

LE.nivel(1)
N = "2-1"


def palmas(sil):
    return (f'<p class="bloques">' + " ".join(f'<span class="ficha {"sil" if i % 2 == 0 else "sil2"}">{x}</span>' for i, x in enumerate(sil)) +
            f' <span class="palmas" aria-label="{len(sil)} palmadas">{"👏" * len(sil)}</span></p>')


def grabado(clave, etiqueta, nota):
    b = f'<button type="button" class="btn-voz" data-sonido="{clave}" hidden><span aria-hidden="true">🔊</span> {etiqueta}</button>'
    return b + (f'<p class="nota-audio" data-nota="{clave}">🗣️ <strong>Dígalo usted en voz alta:</strong> {nota}</p>' if nota else "")


def leccion():
    P = C.Practicas()
    s1 = f"""<p>Antes de leer letras en un papel, hay que saber <strong>escuchar</strong> y manejar los sonidos que forman las palabras. A esa capacidad se le llama <strong>conciencia fonológica</strong>, y es la base sobre la que se aprende a leer: permite partir una palabra en sus pedazos.</p>
<ul><li><em>casa</em> son dos golpes de sonido: <strong>ca + sa</strong>.</li><li><em>papá</em> también: <strong>pa + pá</strong>.</li><li><em>chocolate</em> son cuatro: <strong>cho + co + la + te</strong>.</li></ul>
<p>Si usted puede oír esos golpes, después podrá verlos escritos. Por eso esta lección empieza por el oído.</p>
{LE.AVISO_VOZ}
<p>{LE.escuchar("zapato", "«zapato» (entera)", 0.8)} {LE.escuchar("za. pa. to.", "«za - pa - to» (separada)", 0.6)}</p>
{C.caja("tip", "No es cosa de niños", "<p>Hasta los mejores lectores adultos parten en pedazos una palabra larga o desconocida para leerla: <em>in-ter-na-cio-nal</em>. Es una herramienta de lectores adultos, y la va a usar en todo el curso.</p>")}"""

    s2 = f"""<p>Las palabras se separan en <strong>sílabas</strong>: bloques de sonido que se dicen de un solo golpe de voz. Toda sílaba tiene <strong>al menos una vocal</strong> (a, e, i, o, u) y puede tener consonantes antes o después.</p>
<p>La forma más fácil de contarlas es dar <strong>una palmada por cada bloque</strong>:</p>
{palmas(["Ma", "rí", "a"])}
{palmas(["sol"])}
{palmas(["cho", "co", "la", "te"])}
<div class="caja caja-tip"><span class="etiqueta et-verde">Ahora usted</span><p>Diga en voz alta <em>casa</em>, <em>teléfono</em>, <em>pan</em> y <em>Guatemala</em>, y dé una palmada por cada sílaba. Sí, palmadas de verdad. Al principio puede dar pena, pero funciona. (Son 2, 4, 1 y 4.)</p></div>
{C.caja("ojo", "Dos vocales en una sílaba", "<p>A veces dos vocales van juntas en el mismo golpe de voz: <em>pie</em> (1 sílaba), <em>cua-tro</em> (2), <em>bue-no</em> (2). Otras veces se separan: <em>dí-a</em> (2), <em>ma-íz</em> (2). Su oído y las palmadas le dicen cuántos golpes hay.</p>")}
{P("Compruebe", f"¿Cuántas sílabas tiene <strong>pelota</strong>? {LE.escuchar('pelota', '', 0.8)}", ["2", "3", "4"], 1,
   {0: "Dé las palmadas despacio: pe… lo… ¿y?", 2: "Cuente otra vez con palmadas: pe-lo-ta."}, "<strong>pe - lo - ta</strong>: 3 sílabas.")}
<h3>Las rimas: palabras que terminan igual</h3>
<p>Dos palabras <strong>riman</strong> cuando terminan con el mismo sonido, desde la última vocal fuerte de la palabra:</p>
<p>{LE.escuchar("rojo, ojo", "rojo / ojo", 0.8)} {LE.escuchar("luna, cuna", "luna / cuna", 0.8)} {LE.escuchar("gato, pato", "gato / pato", 0.8)}</p>
<ul><li><em>r<strong>ojo</strong></em> rima con <em><strong>ojo</strong></em>.</li><li><em>l<strong>una</strong></em> rima con <em>c<strong>una</strong></em>.</li><li><em>g<strong>ato</strong></em> rima con <em>p<strong>ato</strong></em>.</li></ul>
{P("Compruebe", "¿Qué palabra rima con <strong>luna</strong>?", ["lana", "cuna", "luz"], 1,
   {0: "Lana empieza parecido, pero termina en «ana», no en «una».", 2: "Luz empieza igual, pero la rima se oye al final."}, "<strong>cuna</strong>: las dos terminan en «una».")}"""

    s3 = f"""<p>Dentro de cada sílaba hay sonidos todavía más pequeños: los <strong>fonemas</strong>. La palabra <em>sal</em> tiene tres:</p>
<p class="bloques"><span class="ficha sil">s</span> + <span class="ficha sil2">a</span> + <span class="ficha sil">l</span> = <strong>sal</strong></p>
{grabado("sal", "Escuchar «s - a - l - ¡sal!»", "«sss… a… lll… ¡sal!». Estire cada sonido sin decir el nombre de la letra.")}
{C.caja("ojo", "El nombre de la letra no es su sonido", "<p>La letra <em>s</em> se llama «ese», pero suena «sss». La <em>p</em> se llama «pe», pero suena «p», corto y seco. Cuando trabajamos con fonemas, usamos el <strong>sonido</strong>, nunca el nombre. Esto le va a ayudar mucho en la próxima lección.</p>")}
<p>Casi siempre, cada letra es un sonido. Pero no siempre: la <strong>h</strong> no suena (<em>hola</em> tiene 4 letras y 3 sonidos), y la <strong>ch</strong> y la <strong>ll</strong> son dos letras que dan un solo sonido (<em>chile</em>: ch-i-l-e, 4 sonidos).</p>
<h3>Aislar el primer sonido</h3>
<p>Una técnica muy útil es <strong>estirar el primer sonido</strong> de la palabra para oírlo bien, separado del resto:</p>
<p>{grabado("nube", "«nnn-nube»", "")}{grabado("raton", "«rrr-ratón»", "")}{grabado("mesa", "«mmm-mesa»", "")}{grabado("sol", "«sss-sol»", "")}</p>
<p class="nota-audio" data-nota="nube raton mesa sol">🗣️ <strong>Dígalo usted en voz alta:</strong> estire el primer sonido de cada palabra sin añadirle ninguna vocal: «nnn-nube», «rrr-ratón», «mmm-mesa», «sss-sol».</p>
{C.caja("tip", "Sin pantalla", "<p>Elija cinco objetos de su casa. Diga el nombre de cada uno estirando el primer sonido («mmm-mesa», «sss-silla») y después diga solo ese sonido. El sonido, no el nombre de la letra: si le sale «eme», vuelva a intentarlo con «mmm».</p>")}
{C.caja("ojo", "Letras que suenan igual", "<p>En el español de América, la <strong>b</strong> y la <strong>v</strong> suenan igual, y la <strong>s</strong>, la <strong>z</strong> y la <strong>c</strong> (ante e, i) también. Con el oído no se puede saber cuál se escribe: eso se aprende con la vista, leyendo y escribiendo.</p>")}
{P("Compruebe", "¿Cuál es el primer sonido de <strong>fuego</strong>?", ["«efe»", "«fff»", "«fu»"], 1,
   {0: "Ese es el nombre de la letra, no su sonido.", 2: "Eso ya es la sílaba entera. El primer sonido es solo el de la consonante."}, "<strong>«fff»</strong>: un soplo entre los dientes y el labio, sin vocal.")}
{P("Compruebe", "¿Cuántos sonidos tiene <strong>hola</strong>?", ["3", "4"], 0, {},
   "<strong>3</strong>: o - l - a. La h se escribe, pero no suena.")}"""

    secciones = [("s1", "El sonido de las palabras", s1), ("s2", "Sílabas y rimas", s2), ("s3", "Los fonemas: los sonidos más pequeños", s3)]
    tarea = [("Nombres en sílabas.", "Escriba su nombre y el de cuatro personas de su familia. Sepárelos en sílabas con guiones (<em>Ro-sa-rio</em>) y dé una palmada por cada sílaba mientras los dice."),
             ("Busque la rima.", "Escriba una palabra que rime con cada una de estas: <em>casa, noche, pan, flor, camino</em>."),
             ("El primer sonido.", "Escriba el nombre de cinco cosas de su cocina. Al lado, escriba su primer sonido y dígalo en voz alta, estirándolo."),
             ("Escuche en la calle.", "Cuando oiga una canción o un anuncio, busque dos palabras que rimen y anótelas.")]
    quiz = [
        ("¿Qué es la <strong>conciencia fonológica</strong>?", ["Saber escribir sin faltas", "La capacidad de oír y manejar los sonidos de las palabras", "Leer en voz alta muy rápido"], 1, {0: "Eso es ortografía.", 2: "Eso tiene que ver con la fluidez."}, "Es oír y manejar los sonidos que forman las palabras."),
        (f"¿Cuántas sílabas tiene <strong>mariposa</strong>? {LE.escuchar('mariposa', '', 0.8)}", ["3", "4", "5"], 1, {0: "Cuente con palmadas: ma-ri-po-…", 2: "Cuente otra vez, despacio."}, "<strong>ma-ri-po-sa</strong>: 4."),
        (f"¿Cuántas sílabas tiene <strong>pan</strong>? {LE.escuchar('pan', '', 0.8)}", ["1", "2", "3"], 0, {1: "Pan se dice de un solo golpe.", 2: "Una sílaba puede tener varias letras."}, "<strong>pan</strong>: 1 sílaba."),
        ("¿Cómo se separa <strong>zapato</strong> en sílabas?", ["zap - a - to", "za - pa - to", "z - a - pato"], 1, {0: "Cada sílaba suele empezar con consonante y tener su vocal: za…", 2: "La z sola no es una sílaba: no tiene vocal."}, "<strong>za - pa - to</strong>."),
        ("¿Qué palabra rima con <strong>gato</strong>?", ["gota", "pato", "gallo"], 1, {0: "Empieza igual, pero termina en «ota».", 2: "Empieza igual, pero termina en «allo»."}, "<strong>pato</strong>: las dos terminan en «ato»."),
        ("¿Qué es una <strong>rima</strong>?", ["Dos palabras que empiezan con la misma letra", "Dos palabras que terminan con el mismo sonido", "Una palabra con muchas sílabas"], 1, {0: "La rima se oye al final.", 2: "La rima compara el final de dos palabras."}, "Dos palabras que <strong>terminan con el mismo sonido</strong>."),
        ("¿Qué es un <strong>fonema</strong>?", ["El sonido más pequeño de una palabra", "Una palabra corta", "Un grupo de sílabas"], 0, {1: "Una palabra corta puede tener varios fonemas.", 2: "Es al revés: las sílabas están hechas de fonemas."}, "El <strong>sonido más pequeño</strong>."),
        ("¿Cuántos sonidos tiene <strong>sal</strong>?", ["1", "2", "3"], 2, {0: "Una sílaba, sí; pero ¿cuántos sonidos? s…", 1: "Estírela: sss… a… lll."}, "<strong>3</strong>: s - a - l."),
        ("La letra «s» se llama «ese». ¿Cómo <strong>suena</strong> dentro de una palabra?", ["«ese», igual que su nombre", "«sss», un sonido que se puede estirar", "No suena"], 1, {0: "Ese es el nombre, no el sonido.", 2: "La que no suena es la h."}, "Suena <strong>«sss»</strong>."),
        ("¿Cuál es el primer sonido de <strong>mesa</strong>?", ["«mmm»", "«eme»", "«me»"], 0, {1: "Ese es el nombre de la letra.", 2: "Esa es la primera sílaba completa."}, "<strong>«mmm»</strong>."),
        ("¿Cuántos sonidos tiene <strong>chile</strong>?", ["4", "5"], 0, {}, "<strong>4</strong>: ch - i - l - e. La ch son dos letras y un solo sonido."),
        ("¿Qué par de letras suena igual en el español de América?", ["b y v", "m y n", "p y d"], 0, {1: "Se parecen, pero la m se dice con los labios cerrados.", 2: "Suenan distinto: la p sopla, la d toca los dientes."}, "La <strong>b</strong> y la <strong>v</strong>."),
    ]
    filas = [
        ("Contar sílabas", "Cuento las sílabas de cualquier palabra con palmadas, también las largas.", "Me confundo en palabras con dos vocales juntas.", "No sé dónde termina cada sílaba (<a href=\"#s2\">repase la sección 2</a>)."),
        ("Reconocer rimas", "Digo palabras que riman con otra sin pensarlo mucho.", "Reconozco una rima, pero me cuesta inventarla.", "Confundo rima con empezar igual (<a href=\"#s2\">repase la sección 2</a>)."),
        ("Aislar el primer sonido", "Digo el primer sonido de una palabra sin decir el nombre de la letra.", "A veces digo la sílaba entera en vez del sonido.", "Digo el nombre de la letra (<a href=\"#s3\">repase la sección 3</a>)."),
    ]
    cierre = ("<p>Ya sabe oír las sílabas, las rimas y los sonidos de una palabra. En la próxima lección va a unir esos sonidos con las letras escritas: eso se llama <strong>decodificar</strong>, y es el paso para leer palabras de verdad.</p>")
    glosario = [("Conciencia fonológica", "La capacidad de oír y manejar los sonidos de las palabras."), ("Sílaba", "Bloque de sonido que se dice de un solo golpe de voz; siempre tiene al menos una vocal."),
                ("Rima", "Coincidencia de sonido al final de dos palabras: <em>luna / cuna</em>."), ("Fonema", "El sonido más pequeño de una palabra: <em>sal</em> tiene tres (s, a, l)."),
                ("Vocal", "Las letras a, e, i, o, u; son el centro de cada sílaba.")]
    conexion = ("<p>Empieza el Tema 2. En la Lección 1.2 vio que una oración está hecha de palabras; hoy va a meterse <strong>dentro de las palabras</strong> para ver de qué están hechas. Y esta lección no es de leer todavía: es de <strong>escuchar</strong>.</p>"
                "<p><strong>Lo que necesita:</strong> el cuaderno y, si puede, audífonos: en esta lección va a escuchar mucho.</p>")
    estd = LE.estandares([], fund=["RF.2"])
    return C.pagina_leccion(N, LE.titulo(N), "Antes de leer letras, hay que aprender a escuchar.", ["Fundamentos de lectura", "Conciencia fonológica"],
                            ["<strong>Contar</strong> las sílabas de una palabra con palmadas.", "<strong>Reconocer</strong> y formar rimas.",
                             "<strong>Aislar</strong> el primer sonido de una palabra y contar sus sonidos.", "<strong>Distinguir</strong> el nombre de una letra de su sonido."],
                            estd, conexion, secciones, tarea, quiz, filas, cierre, ("2-2", LE.titulo("2-2")), glosario, P)


# ---------------------------------------------------------------- práctica
SIL = [("casa", "ca-sa"), ("mariposa", "ma-ri-po-sa"), ("pan", "pan"), ("pelota", "pe-lo-ta"), ("sol", "sol"), ("chocolate", "cho-co-la-te"),
       ("teléfono", "te-lé-fo-no"), ("mesa", "me-sa"), ("tomate", "to-ma-te"), ("flor", "flor"), ("ventana", "ven-ta-na"), ("Guatemala", "Gua-te-ma-la"),
       ("tren", "tren"), ("camisa", "ca-mi-sa"), ("árbol", "ár-bol"), ("bicicleta", "bi-ci-cle-ta"), ("leche", "le-che"), ("trabajo", "tra-ba-jo"),
       ("familia", "fa-mi-lia"), ("autobús", "au-to-bús")]


def banco_silabas():
    b = []
    for w, sep in SIL:
        n = sep.count("-") + 1
        ops = [str(x) for x in sorted({n, max(1, n - 1), n + 1, n + 2} - ({0}))][:3]
        if str(n) not in ops:
            ops[-1] = str(n)
        b.append({"enun": f"¿Cuántas sílabas tiene <strong>{w}</strong>? {LE.escuchar(w, '', 0.75)}", "ops": ops, "ok": ops.index(str(n)), "enOrden": True,
                  "pista": "Dígala en voz alta despacio y dé una palmada por cada golpe de voz.", "exp": f"<strong>{sep}</strong>: {n} {'sílaba' if n == 1 else 'sílabas'}."})
    return b


def banco_separa():
    datos = [("zapato", ["za-pa-to", "zap-a-to", "z-a-pa-to"]), ("pelota", ["pe-lo-ta", "pel-o-ta", "pe-l-ota"]), ("ventana", ["ven-ta-na", "ve-nta-na", "vent-a-na"]),
             ("camino", ["ca-mi-no", "cam-i-no", "ca-m-ino"]), ("tomate", ["to-ma-te", "tom-a-te", "to-mat-e"]), ("trabajo", ["tra-ba-jo", "t-ra-ba-jo", "trab-a-jo"]),
             ("escuela", ["es-cue-la", "e-scue-la", "esc-ue-la"]), ("doctora", ["doc-to-ra", "do-cto-ra", "doct-o-ra"])]
    return [{"enun": f"¿Cómo se separa <strong>{w}</strong> en sílabas?", "ops": o, "ok": 0,
             "pista": "Cada sílaba tiene su vocal. Dígala despacio con palmadas.", "exp": f"<strong>{o[0]}</strong>."} for w, o in datos]


def banco_rimas():
    datos = [("luna", "cuna", ["lana", "luz"]), ("gato", "pato", ["gota", "gallo"]), ("casa", "masa", ["cosa", "cama"]), ("noche", "coche", ["nota", "nube"]),
             ("pan", "tan", ["pon", "pie"]), ("flor", "calor", ["flan", "fresa"]), ("camino", "pepino", ["camisa", "cama"]), ("ratón", "botón", ["rato", "rama"]),
             ("mesa", "fresa", ["misa", "mano"]), ("rojo", "ojo", ["roca", "rosa"]), ("canción", "corazón", ["canasta", "cantar"]), ("pelo", "cielo", ["pala", "pila"])]
    return [{"enun": f"¿Qué palabra rima con <strong>{w}</strong>? {LE.escuchar(w, '', 0.8)}", "ops": [r] + d, "ok": 0,
             "pista": "La rima se oye al final de la palabra, no al principio.", "exp": f"<strong>{r}</strong> rima con {w}."} for w, r, d in datos]


def banco_primero():
    datos = [("mesa", "m", ["n", "s"]), ("luna", "l", ["r", "n"]), ("sol", "s", ["m", "l"]), ("foca", "f", ["p", "j"]), ("nube", "n", ["m", "l"]),
             ("ratón", "rr", ["l", "d"]), ("pan", "p", ["b", "t"]), ("taza", "t", ["d", "p"]), ("dedo", "d", ["t", "b"]), ("fuego", "f", ["j", "p"]),
             ("jugo", "j", ["g", "h"]), ("llave", "ll / y", ["l", "ch"]), ("chile", "ch", ["c", "s"]), ("hoja", "o", ["j", "a"])]
    b = []
    for w, s, d in datos:
        exp = f"El primer sonido de <em>{w}</em> es <strong>/{s}/</strong>."
        if w == "hoja":
            exp += " La h no suena: la palabra empieza con el sonido de la o."
        if w == "llave":
            exp += " La ll es un solo sonido; en América suena igual que la y."
        if w == "chile":
            exp += " La ch son dos letras y un solo sonido."
        b.append({"enun": f"¿Cuál es el primer <strong>sonido</strong> de <strong>{w}</strong>? {LE.escuchar(w, '', 0.75)}", "ops": [f"/{s}/"] + [f"/{x}/" for x in d], "ok": 0,
                  "pista": "Estire el principio de la palabra en voz alta, sin decir el nombre de la letra.", "exp": exp})
    return b


def banco_cuantos():
    datos = [("sal", 3, "s-a-l"), ("sol", 3, "s-o-l"), ("pan", 3, "p-a-n"), ("mesa", 4, "m-e-s-a"), ("casa", 4, "c-a-s-a"), ("luz", 3, "l-u-z"),
             ("hola", 3, "o-l-a (la h no suena)"), ("chile", 4, "ch-i-l-e (la ch es un solo sonido)"), ("llave", 4, "ll-a-v-e (la ll es un solo sonido)"),
             ("mar", 3, "m-a-r"), ("flor", 4, "f-l-o-r"), ("hilo", 3, "i-l-o (la h no suena)"), ("pato", 4, "p-a-t-o"), ("leche", 4, "l-e-ch-e")]
    b = []
    for w, n, sep in datos:
        ops = [str(n - 1), str(n), str(n + 1)]
        b.append({"enun": f"¿Cuántos <strong>sonidos</strong> tiene <strong>{w}</strong>?", "ops": ops, "ok": 1, "enOrden": True,
                  "pista": "Estire cada sonido y cuéntelos con los dedos. Recuerde: la h no suena, y la ch y la ll son un solo sonido.",
                  "exp": f"<strong>{n}</strong>: {sep}."})
    return b


def practica():
    mods = [
        ("silabas", "¿Cuántas sílabas?", C.om("m1", "Escuche o lea la palabra en voz alta y dé una palmada por cada sílaba.") + "\n" + LE.AVISO_VOZ),
        ("separar", "¿Cómo se separa?", C.om("m2", "Elija la separación en sílabas correcta.")),
        ("rimas", "¿Qué palabra rima?", C.om("m3", "Busque la palabra que termina con el mismo sonido.")),
        ("primer-sonido", "El primer sonido", C.om("m4", "Estire el principio de la palabra. El sonido, no el nombre de la letra.")),
        ("cuantos-sonidos", "¿Cuántos sonidos?", C.om("m5", "Cuente los fonemas: los sonidos, no las letras.")),
    ]
    js = (C.js_datos("SILB", banco_silabas()) + C.js_datos("SEP", banco_separa()) + C.js_datos("RIM", banco_rimas()) +
          C.js_datos("PRI", banco_primero()) + C.js_datos("CUA", banco_cuantos()) +
          'creaBanco("m1", SILB);\ncreaBanco("m2", SEP);\ncreaBanco("m3", RIM);\ncreaBanco("m4", PRI);\ncreaBanco("m5", CUA);\n')
    return C.pagina_practica(N, LE.titulo(N), "Cinco actividades · los ejercicios cambian cada vez · dos intentos en cada uno", mods, js)


if __name__ == "__main__":
    LE.construye(N, leccion, practica, horas="Unas 3 horas")
