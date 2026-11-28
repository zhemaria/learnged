# -*- coding: utf-8 -*-
"""LearnGED · Artes del lenguaje (español) · Nivel 1 · Lección 3.2 · La concordancia.
Fuente: clases_leng1/clase_3-2.html (GEDparaHispanos) y sus prácticas de gramatica/n1-l3-2.html, adaptadas al marco de LearnGED.
Uso: python3 tools/build_leng1_3_2.py
"""
import os, random, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import leng_es as LE
from leng_es import C

LE.nivel(1)
N = "3-2"

# sustantivo: (singular, plural, género)
SUS = [("casa", "casas", "f"), ("carro", "carros", "m"), ("mesa", "mesas", "f"), ("libro", "libros", "m"), ("niña", "niñas", "f"), ("perro", "perros", "m"),
       ("flor", "flores", "f"), ("árbol", "árboles", "m"), ("camisa", "camisas", "f"), ("zapato", "zapatos", "m"), ("ventana", "ventanas", "f"), ("vaso", "vasos", "m"),
       ("día", "días", "m"), ("mano", "manos", "f"), ("mapa", "mapas", "m"), ("problema", "problemas", "m"), ("canción", "canciones", "f"), ("pared", "paredes", "f"),
       ("lápiz", "lápices", "m"), ("ciudad", "ciudades", "f"), ("tren", "trenes", "m"), ("foto", "fotos", "f"), ("radio", "radios", "f"), ("idioma", "idiomas", "m")]
# adjetivo: forma masculina singular; los que no terminan en -o no cambian de género
ADJ = ["rojo", "nuevo", "bonito", "viejo", "limpio", "pequeño", "blanco", "largo", "grande", "feliz", "azul", "verde", "amable", "fácil", "difícil", "importante"]
PAREJA = {"casa": "bonito", "carro": "rojo", "mesa": "redondo", "libro": "nuevo", "niña": "feliz", "perro": "pequeño", "flor": "amarillo", "árbol": "alto",
          "camisa": "blanco", "zapato": "negro", "ventana": "limpio", "vaso": "lleno", "día": "largo", "mano": "frío", "mapa": "viejo", "problema": "difícil",
          "canción": "alegre", "pared": "blanco", "lápiz": "azul", "ciudad": "grande", "tren": "rápido", "foto": "bonito", "radio": "viejo", "idioma": "fácil"}
PLURAL = {"feliz": "felices", "azul": "azules", "fácil": "fáciles", "difícil": "difíciles"}


def forma(adj, g, n):
    if adj.endswith("o"):
        base = adj[:-1] + ("o" if g == "m" else "a")
        return base + ("s" if n == "p" else "")
    if n == "s":
        return adj
    return PLURAL.get(adj, adj + "s")


def art(g, n, det="el"):
    if det == "el":
        return {"ms": "el", "fs": "la", "mp": "los", "fp": "las"}[g + n]
    return {"ms": "un", "fs": "una", "mp": "unos", "fp": "unas"}[g + n]


def leccion():
    P = C.Practicas()
    s1 = f"""<p>En español, todos los sustantivos tienen <strong>género</strong>: son masculinos o femeninos. No tiene nada que ver con que la cosa sea macho o hembra: es una etiqueta de la gramática. La mesa no es mujer ni el libro es hombre.</p>
<ul><li><strong>Masculinos:</strong> van con <em>el, un, los, unos</em>: <em>el carro, un libro, el árbol</em>.</li>
<li><strong>Femeninos:</strong> van con <em>la, una, las, unas</em>: <em>la casa, una flor, la mesa</em>.</li></ul>
{C.caja("tip", "Pista útil, con excepciones", "<p>La mayoría de las palabras que terminan en <strong>-o</strong> son masculinas (<em>libro, carro</em>) y la mayoría de las que terminan en <strong>-a</strong>, femeninas (<em>casa, mesa</em>). Pero hay excepciones muy usadas: <em>la mano, la foto, la radio</em> (femeninas), y <em>el día, el mapa, el problema, el idioma</em> (masculinas). El artículo le dice la verdad: fíjese siempre en él.</p>")}
<p>Los sustantivos también tienen <strong>número</strong>: <strong>singular</strong> (uno) o <strong>plural</strong> (varios). El plural se forma con <strong>-s</strong> si la palabra termina en vocal (<em>casa → casas</em>) y con <strong>-es</strong> si termina en consonante (<em>flor → flores, pared → paredes</em>). Ojo: la z cambia a c (<em>lápiz → lápices, feliz → felices</em>).</p>
{C.tabla("Artículos según el género y el número", ["Género", "Singular", "Plural"], [["Masculino", "el gato, un carro", "los gatos, unos carros"], ["Femenino", "la gata, una casa", "las gatas, unas casas"]])}
{P("Compruebe", "¿Qué artículo va con <strong>problema</strong>?", ["la", "el"], 1, {}, "<strong>el problema</strong>: es masculino aunque termina en -a.")}"""

    s2 = f"""<p>La <strong>regla de oro</strong>: cuando un adjetivo acompaña a un sustantivo, los dos van en el <strong>mismo género</strong> y en el <strong>mismo número</strong>. Y el artículo también. Todo cambia <strong>en bloque</strong>:</p>
{C.tabla("Las cuatro formas de «gato negro»", ["Género", "Singular", "Plural"], [["Masculino", "el gat<strong>o</strong> negr<strong>o</strong>", "los gat<strong>os</strong> negr<strong>os</strong>"], ["Femenino", "la gat<strong>a</strong> negr<strong>a</strong>", "las gat<strong>as</strong> negr<strong>as</strong>"]])}
{C.tabla("Las cuatro formas con «rojo»", ["Género", "Singular", "Plural"], [["Masculino", "el carro rojo", "los carros rojos"], ["Femenino", "la flor roja", "las flores rojas"]])}
{C.caja("ojo", "Adjetivos que no cambian de género", "<p>Los adjetivos que no terminan en -o sirven igual para masculino y femenino; solo cambian en plural: <em>el niño feliz / la niña feliz / los niños felices</em>; <em>un carro grande / una casa grande</em>; <em>el cielo azul / la camisa azul</em>.</p>")}
{C.caja("ojo", "«El agua fría»", "<p>Algunas palabras femeninas que empiezan con <em>a</em> tónica llevan <em>el</em> en singular para que suene mejor: <em>el agua, el águila, el hacha</em>. Pero siguen siendo femeninas: <em>el agua <strong>fría</strong></em>, <em>las aguas <strong>frías</strong></em>.</p>")}
{P("Compruebe", "¿Cuál está bien?", ["las mesas roja", "las mesas rojas", "la mesas rojas"], 1, {0: "Mesas es plural: el adjetivo también.", 2: "Con mesas va las, no la."}, "<strong>las mesas rojas</strong>: todo en femenino plural.")}
{P("Compruebe", "¿Cuál está bien?", ["el día soleado", "la día soleada"], 0, {}, "<strong>el día soleado</strong>: <em>día</em> es masculino aunque termine en -a.")}"""

    pares = [("La camisa", ["blanco", "blanca", "blancas"], 1), ("Los zapatos", ["nuevo", "nuevos", "nuevas"], 1), ("Mi hermana es", ["alto", "alta", "altas"], 1),
             ("Las ventanas están", ["sucio", "sucias", "sucios"], 1), ("El mapa es", ["viejo", "vieja", "viejos"], 0), ("Los niños están", ["feliz", "felices", "felizes"], 1)]
    s3 = f"""<p>Elija en cada menú la forma que concuerda. Así son las preguntas de corrección del examen GED: un menú dentro de la oración.</p>
{"".join(P("Elija la forma correcta", f"{a} ___ .", o, k, {i: "Mire el sustantivo: ¿es masculino o femenino?, ¿uno o varios?" for i in range(3) if i != k}, f"<strong>{a} {o[k]}.</strong>") for a, o, k in pares)}"""

    secciones = [("s1", "El género y el número", s1), ("s2", "La regla de oro: todo en bloque", s2), ("s3", "Práctica: elija la forma correcta", s3)]
    tarea = [("Las cuatro formas.", "Escriba las cuatro formas de <em>perro grande</em>, <em>casa bonita</em> y <em>niño feliz</em>, como en la tabla de la sección 2."),
             ("Mi objeto, en plural.", "Vuelva a las oraciones de la tarea de la Lección 3.1 sobre un objeto de su casa y escríbalas en plural (<em>Mis mesas de cocina son redondas y viejas.</em>). Revise que todo concuerde."),
             ("Atento a la calle.", "En carteles, anuncios o mensajes, busque dos frases con un error de concordancia y escríbalas corregidas.")]
    quiz = [
        ("¿Qué artículo va con <strong>mano</strong>?", ["el", "la"], 1, {}, "<strong>la mano</strong>: femenina aunque termina en -o."),
        ("¿Qué artículo va con <strong>mapa</strong>?", ["el", "la"], 0, {}, "<strong>el mapa</strong>: masculino aunque termina en -a."),
        ("¿Cuál es el plural de <strong>flor</strong>?", ["flors", "flores", "floras"], 1, {0: "Termina en consonante: se añade -es.", 2: "No se cambia la palabra: solo se añade -es."}, "<strong>flores</strong>."),
        ("¿Cuál es el plural de <strong>lápiz</strong>?", ["lápizes", "lápices", "lápiz"], 1, {0: "La z cambia a c antes de -es.", 2: "En plural hay que cambiarla."}, "<strong>lápices</strong>."),
        ("¿Cuál está bien?", ["la casa blanco", "la casa blanca", "la casas blanca"], 1, {0: "Casa es femenina: el adjetivo también.", 2: "Con casas va las, y el adjetivo en plural."}, "<strong>la casa blanca</strong>."),
        ("¿Cuál está bien?", ["los carros rojos", "los carros rojo", "las carros rojos"], 0, {1: "Carros es plural: rojos.", 2: "Carro es masculino: los."}, "<strong>los carros rojos</strong>."),
        ("¿Cuál está bien?", ["las flores bonitas", "las flores bonito"], 0, {}, "<strong>las flores bonitas</strong>."),
        ("¿Cuál está bien?", ["el niño feliz", "el niño feliza", "el niño felices"], 0, {1: "Feliz no cambia de género.", 2: "Niño es singular."}, "<strong>el niño feliz</strong>."),
        ("¿Cuál está bien?", ["las niñas felices", "las niñas feliz", "las niñas felizes"], 0, {1: "Niñas es plural: el adjetivo también.", 2: "La z cambia a c: felices."}, "<strong>las niñas felices</strong>."),
        ("¿Cuál está bien?", ["el agua frío", "el agua fría"], 1, {}, "<strong>el agua fría</strong>: agua es femenina aunque lleve <em>el</em>."),
        ("En <em>Las ventanas están limpias</em>, ¿qué tienen en común <em>ventanas</em> y <em>limpias</em>?", ["Son femeninas y plurales", "Son masculinas y singulares", "Nada"], 0, {1: "Mire las terminaciones: -as.", 2: "Concuerdan: ese es el punto."}, "Las dos son <strong>femeninas y plurales</strong>."),
        ("¿Por qué importa la concordancia?", ["Porque el lector entiende de qué y de cuántas cosas se habla", "Porque así las oraciones son más largas"], 0, {}, "Sin concordancia el lector tropieza: <em>«las mesas roja»</em>, ¿una o varias?"),
    ]
    filas = [
        ("Género y número", "Sé si un sustantivo es masculino o femenino, singular o plural, también en las excepciones (el día, la mano).", "Me confundo con las excepciones.", "No sé qué artículo va (<a href=\"#s1\">repase la sección 1</a>)."),
        ("Concordancia", "Hago concordar artículo, sustantivo y adjetivo en todas mis oraciones.", "Se me escapa el plural del adjetivo.", "Mezclo géneros y números (<a href=\"#s2\">repase la sección 2</a>)."),
        ("Plurales", "Formo bien los plurales con -s, -es y z → c.", "Dudo con los que terminan en z.", "No sé formarlos (<a href=\"#s1\">repase la sección 1</a>)."),
    ]
    cierre = "<p>La concordancia evita que el lector tropiece, y el examen GED la evalúa en sus preguntas de corrección. En la próxima lección conocerá al corazón de la oración: el <strong>verbo</strong>. Sin verbo no hay acción, y sin acción no hay oración completa.</p>"
    glosario = [("Género", "Masculino o femenino; lo muestra el artículo."), ("Número", "Singular (uno) o plural (varios)."), ("Concordancia", "Acuerdo en género y número entre el artículo, el sustantivo y el adjetivo."),
                ("Adjetivo invariable", "El que no cambia de género: <em>feliz, grande, azul</em>.")]
    conexion = ("<p>En la Lección 3.1 conoció a los sustantivos y a los adjetivos. Hoy va a ver la regla que los hace funcionar juntos. El español es un idioma de parejas: no podemos decir <em>«el casa blancos»</em>; suena raro porque las palabras no concuerdan. Lo correcto es <em>la casa blanca</em>.</p>"
                "<p><strong>Lo que necesita:</strong> el cuaderno y las oraciones de la tarea de la Lección 3.1.</p>")
    estd = LE.estandares(["L.1.2"], base=["L.1.7"])
    return C.pagina_leccion(N, LE.titulo(N), "Artículo, sustantivo y adjetivo: siempre en bloque.", ["L.1.2 · Concordancia"],
                            ["<strong>Reconocer</strong> el género y el número de un sustantivo, también en las excepciones comunes.", "<strong>Formar</strong> plurales con -s, -es y z → c.",
                             "<strong>Hacer concordar</strong> el artículo, el sustantivo y el adjetivo.", "<strong>Corregir</strong> errores de concordancia, como en el examen GED."],
                            estd, conexion, secciones, tarea, quiz, filas, cierre, ("3-3", LE.titulo("3-3")), glosario, P)


# ---------------------------------------------------------------- práctica
def banco_genero():
    b = []
    for s, p, g in SUS:
        b.append({"enun": f"¿Qué artículo va con <strong class=\"grande\">{s}</strong>?", "ops": ["el", "la"], "ok": 0 if g == "m" else 1, "enOrden": True,
                  "exp": f"<strong>{'el' if g == 'm' else 'la'} {s}</strong>." + (" ¡Es una excepción!" if (s.endswith("a") and g == "m") or (s.endswith("o") and g == "f") else "")})
    return b


def banco_menu():
    r = random.Random(7)
    b = []
    for s, p, g in SUS:
        for n in ("s", "p"):
            a = PAREJA[s]
            ok = forma(a, g, n)
            cand = []
            for gg in ("m", "f"):
                for nn in ("s", "p"):
                    f = forma(a, gg, nn)
                    if f != ok and f not in cand:
                        cand.append(f)
            if a == "feliz":
                cand.append("felizes")
            ops = [ok] + cand[:2] if len(cand) >= 2 else [ok] + cand + [a + "es"]
            sus = s if n == "s" else p
            b.append({"partes": [f"{art(g, n).capitalize()} {sus} ", {"ops": sorted(ops[:3]), "ok": sorted(ops[:3]).index(ok)}, "."],
                      "pista": f"«{sus}» es {'masculino' if g == 'm' else 'femenino'} y {'singular' if n == 's' else 'plural'}.",
                      "exp": f"<strong>{art(g, n).capitalize()} {sus} {ok}</strong>: {'masculino' if g == 'm' else 'femenino'} {'singular' if n == 's' else 'plural'}."})
    return b


def banco_error():
    datos = [(["La casa es bonita.", "Las casas son bonita.", "Las casas son bonitas."], 1), (["El perro está cansado.", "Los perros están cansado.", "Los perros están cansados."], 1),
             (["La mano está fría.", "La mano está frío.", "Las manos están frías."], 1), (["El día fue largo.", "El día fue larga.", "Los días fueron largos."], 1),
             (["Compré unos zapatos negros.", "Compré unos zapatos negras.", "Compré unas botas negras."], 1), (["Las canciones son alegres.", "Las canciones son alegre.", "La canción es alegre."], 1),
             (["El agua está fría.", "El agua está frío.", "Las aguas están frías."], 1), (["Mis hijas son altas.", "Mis hijas son altos.", "Mi hija es alta."], 1)]
    return [{"enun": "¿Cuál tiene un <strong>error</strong> de concordancia?", "ops": o, "ok": k, "pista": "Revise en cada una si el adjetivo va igual que el sustantivo: género y número.",
             "exp": f"<em>{o[k]}</em> tiene el error."} for o, k in datos]


def practica():
    mods = [
        ("genero", "¿El o la?", C.om("m1", "Elija el artículo. Cuidado con las excepciones.")),
        ("menu", "Elija la forma que concuerda", C.huecos("m2", "Abra el menú y elija el adjetivo que concuerda con el sustantivo. Así son las preguntas de corrección del examen GED.")),
        ("error", "Encuentre el error", C.om("m3", "Una de las tres oraciones tiene un error de concordancia.")),
    ]
    js = (C.js_datos("GEN", banco_genero()) + C.js_datos("MEN", banco_menu()) + C.js_datos("ERR", banco_error()) +
          'creaBanco("m1", GEN);\ncreaHuecos("m2", MEN);\ncreaBanco("m3", ERR);\n')
    return C.pagina_practica(N, LE.titulo(N), "Tres actividades · los ejercicios cambian cada vez · dos intentos en cada uno", mods, js)


if __name__ == "__main__":
    LE.construye(N, leccion, practica, horas="Unas 3 horas")
