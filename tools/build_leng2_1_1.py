# -*- coding: utf-8 -*-
"""LearnGED · Artes del lenguaje (español) · Nivel 2 · Lección 1.1 · Vocales, diptongos y sílabas complejas.
Fuente: clases_leng2/clase_1-1.html (GEDparaHispanos) y gramatica/n2-l1-1.html, adaptadas al marco de LearnGED.
Usa creaCortes (/rla/leng.js): cortar palabras en sílabas tocando los huecos entre letras.
Uso: python3 tools/build_leng2_1_1.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import leng_es as LE
from leng_es import C

LE.nivel(2)
N = "1-1"
DIP = ["ai-re", "pei-ne", "cui-da-do", "ciu-dad", "a-gua", "cau-sa", "puer-ta", "nue-vo", "fa-mi-lia", "his-to-ria", "ca-mión", "can-ción", "seis", "vien-to", "sue-lo", "deu-da",
       "rui-do", "tie-rra", "cua-der-no", "siem-pre", "a-cei-te", "es-cue-la", "pue-blo", "true-no"]
HIA = ["dí-a", "po-e-ta", "le-er", "pa-ís", "rí-o", "ma-es-tro", "ba-úl", "ma-íz", "o-í-do", "tí-o", "ca-ca-o", "o-cé-a-no", "mu-se-o", "fe-o", "bú-ho", "re-ír", "frí-o", "ca-er", "pe-or", "ra-íz"]
CORTES = ["tra-ba-jo", "ha-blar", "li-bro", "a-pren-der", "cla-se", "bra-zo", "plá-ta-no", "nom-bre", "a-zú-car", "cui-da-do", "ciu-dad", "ai-re", "a-gua", "puer-ta", "fa-mi-lia",
          "his-to-ria", "pa-ís", "po-e-ta", "ma-es-tro", "ba-úl", "es-cue-la", "true-no", "pro-gra-ma", "can-ción", "ca-mión", "hom-bre", "pe-rro", "ca-lle", "co-che", "gui-ta-rra",
          "que-so", "ins-truc-ción", "cua-der-no", "siem-pre", "pro-ble-ma", "es-tu-dian-te", "bú-ho", "re-ír", "pue-blo", "i-gle-sia", "fá-bri-ca", "ma-íz", "pá-ja-ro", "mu-cha-cho",
          "des-pués", "ár-bol", "ven-ta-na", "tran-qui-lo"]
GRUPOS = [("libro", "br", ["bl", "dr"]), ("clase", "cl", ["cr", "gl"]), ("tren", "tr", ["dr", "pr"]), ("hablar", "bl", ["br", "pl"]), ("plato", "pl", ["pr", "bl"]), ("frío", "fr", ["fl", "pr"]),
          ("grande", "gr", ["gl", "cr"]), ("crema", "cr", ["cl", "gr"]), ("madre", "dr", ["tr", "br"]), ("flor", "fl", ["fr", "pl"]), ("iglesia", "gl", ["gr", "cl"]), ("primo", "pr", ["pl", "br"]),
          ("blanco", "bl", ["br", "pl"]), ("fruta", "fr", ["fl", "tr"]), ("triste", "tr", ["dr", "cr"]), ("cobre", "br", ["bl", "pr"]), ("tabla", "bl", ["br", "pl"]), ("pluma", "pl", ["pr", "fl"]),
          ("grupo", "gr", ["cr", "gl"]), ("cruz", "cr", ["cl", "gr"]), ("sobre", "br", ["bl", "dr"]), ("nublado", "bl", ["br", "pl"]), ("claro", "cl", ["cr", "pl"]), ("globo", "gl", ["gr", "bl"])]
TREN = ["Cada día, a las seis y media, Julia sale de su casa con prisa. Camina tres cuadras bajo el viento frío hasta la estación. Allí espera el tren junto a un grupo de trabajadores.",
        "En el vagón, Julia lee un libro sobre la historia de su ciudad. Le gusta aprender palabras nuevas. A veces el tren se detiene y se oye un ruido fuerte, pero ella sigue leyendo tranquila.",
        "Cuando llega a la fábrica, guarda el libro en su bolsa azul. Por la tarde, en el camino de regreso, piensa en el día en que podrá enseñar a sus hijos todo lo que aprendió."]
VOCALES = [("a", 0), ("e", 0), ("o", 0), ("i", 1), ("u", 1)]


def leccion():
    P = C.Practicas()
    s1 = f"""<p>En el Nivel 1 separó en sílabas palabras sencillas como <em>ca-sa</em> o <em>ga-to</em>. Pero muchas palabras de la vida diaria no son tan simples: <em>cuidado, tren, estudiante, país</em>. Tienen dos vocales juntas o dos consonantes seguidas. Las reglas de esta lección le dirán cómo se agrupan esas letras, para leer palabras largas sin trabarse y, más adelante, poner bien las tildes.</p>
{C.tabla("Vocales fuertes y débiles", ["Grupo", "Vocales", "Cómo se pronuncian"],
         [["Fuertes (abiertas)", "<strong>a · e · o</strong>", "La boca se abre más."], ["Débiles (cerradas)", "<strong>i · u</strong>", "La boca queda casi cerrada."]])}
{C.caja("tip", "Para recordarlas", "<p>Las débiles son solo dos: la <strong>i</strong> y la <strong>u</strong>. Piense en «<strong>tú y yo</strong>»: una u y una y, que suena como i. Al final de palabra, la <em>y</em> funciona como vocal débil: <em>hoy, muy, rey</em>.</p>")}
{P("Compruebe", "¿Qué vocales son débiles?", ["la i y la u", "la a y la e", "la o y la u"], 0, {1: "Son fuertes.", 2: "La o es fuerte."}, "La <strong>i</strong> y la <strong>u</strong>.")}"""

    s2 = f"""<h3>El diptongo: dos vocales en una sílaba</h3>
{C.tabla("Combinaciones que forman diptongo", ["Combinación", "Ejemplos"],
         [["Débil + fuerte", "a-<strong>gua</strong> · <strong>puer</strong>-ta · fa-mi-<strong>lia</strong> · <strong>vien</strong>-to"], ["Fuerte + débil", "<strong>ai</strong>-re · <strong>pei</strong>-ne · <strong>cau</strong>-sa · <strong>hoy</strong>"],
          ["Dos débiles distintas", "<strong>ciu</strong>-dad · <strong>cui</strong>-da-do · <strong>rui</strong>-do"]])}
<h3>El hiato: dos vocales que se separan</h3>
<ul><li><strong>Dos vocales fuertes juntas:</strong> po-e-ta, le-er, ma-es-tro, ca-ca-o.</li>
<li><strong>Una débil con tilde:</strong> dí-a, rí-o, pa-ís, ba-úl. La tilde sobre la í o la ú avisa que el diptongo se rompe.</li></ul>
{C.caja("tip", "Compare con el oído", "<p>En <em>causa</em>, la a y la u salen de un solo golpe de voz (cau-sa). En <em>baúl</em>, la voz se detiene un instante entre ellas (ba-úl).</p>" + LE.escuchar("causa… baúl", "Escuchar causa y baúl"))}
{C.caja("ojo", "Dos trampas", "<ul><li><strong>La h no separa:</strong> en <em>búho</em>, la ú y la o forman hiato (bú-ho), como si la h no estuviera.</li><li><strong>La u muda:</strong> en <em>que, qui, gue, gui</em> la u no suena y no forma diptongo: <em>que-so</em>, <em>gui-ta-rra</em>. Cuando sí debe sonar, lleva diéresis: <em>pingüino, vergüenza</em>.</li></ul>")}
{P("Compruebe", "<strong>país</strong>: ¿diptongo o hiato?", ["Hiato", "Diptongo"], 0, {}, "<strong>Hiato</strong>: pa-ís. La í con tilde forma su propia sílaba.")}
{P("Compruebe", "<strong>ciudad</strong>: ¿diptongo o hiato?", ["Diptongo", "Hiato"], 0, {}, "<strong>Diptongo</strong>: ciu-dad. Dos débiles distintas van juntas.")}"""

    s3 = f"""<h3>Grupos que nunca se separan</h3>
<p>Algunas consonantes se juntan con una <strong>l</strong> o una <strong>r</strong> y forman un <strong>grupo</strong> que se lee de un solo golpe y va siempre al comienzo de la misma sílaba.</p>
{C.tabla("Grupos consonánticos", ["Con l", "Con r"],
         [["<strong>bl</strong>: ha-blar", "<strong>br</strong>: li-bro"], ["<strong>cl</strong>: cla-se", "<strong>cr</strong>: cre-ma"], ["<strong>fl</strong>: flor", "<strong>dr</strong>: ma-dre"],
          ["<strong>gl</strong>: i-gle-sia", "<strong>fr</strong>: frí-o"], ["<strong>pl</strong>: pla-to", "<strong>gr</strong>: gran-de"], ["", "<strong>pr</strong>: pri-mo · <strong>tr</strong>: tren"]])}
{C.caja("tip", "La regla en una frase", "<p>Si ve una consonante seguida de <strong>l</strong> o <strong>r</strong>, no las separe: <em>a-pren-der</em>, no <em>ap-ren-der</em>; <em>nom-bre</em>, no <em>nomb-re</em>.</p>")}
<h3>Letras dobles: ch, ll, rr</h3>
<p>Se escriben con dos letras, pero suenan como un solo sonido. Tampoco se separan: <em>co-che, ca-lle, pe-rro</em>.</p>
<h3>Dos consonantes que no forman grupo</h3>
<p>Si no son un grupo ni una letra doble, se reparten: la primera cierra una sílaba y la segunda abre la siguiente: <em>can-ción, par-que, es-cue-la, al-to</em>.</p>
{P("Compruebe", "¿Cuál es la separación correcta de <strong>aprender</strong>?", ["a-pren-der", "ap-ren-der", "apr-en-der"], 0, {1: "La p y la r forman grupo: no se separan.", 2: "El grupo pr va al comienzo de la sílaba."}, "<strong>a-pren-der</strong>.")}"""

    s4 = f"""<p>Lea el texto tres veces: la primera, escuchándolo y siguiendo las palabras con el dedo; la segunda, despacio, marcando las sílabas de las palabras largas; la tercera, a su ritmo normal.</p>
{LE.escuchar(" ".join(TREN), "Escuchar el texto")}
<div class="texto-lectura"><p><strong>El tren de la mañana</strong></p>{"".join(f"<p>{p}</p>" for p in TREN)}</div>
{C.caja("tip", "Fíjese en tres detalles", "<ul><li><em>Julia</em> tiene dos sílabas (Ju-lia), y <em>día</em> también (dí-a): en la primera hay diptongo; en la segunda, la tilde lo rompe.</li><li>En <em>sigue</em> y <em>tranquila</em> la u no suena; en <em>guarda</em> sí suena: por eso <em>guar-da</em> tiene diptongo.</li><li>En <em>se oye</em>, la y está entre dos vocales y suena como consonante: <em>o-ye</em>.</li></ul>")}
{P("Comprensión", "¿Qué lee Julia en el tren?", ["Un libro sobre la historia de su ciudad", "El periódico", "Una carta de sus hijos"], 0, {1: "Relea el segundo párrafo.", 2: "Relea el segundo párrafo."}, "<strong>Un libro sobre la historia de su ciudad.</strong>")}
{P("Comprensión", "¿Qué quiere hacer Julia con lo que aprende?", ["Enseñárselo a sus hijos", "Dar clases en la fábrica", "Escribir un libro"], 0, {1: "No lo dice el texto.", 2: "No lo dice el texto."}, "<strong>Enseñárselo a sus hijos.</strong>")}
<div class="caja caja-tip"><span class="etiqueta et-verde">Actividad · en su cuaderno</span>
<p>Separe en sílabas y marque con un color los diptongos y con otro los grupos de consonantes: <em>trabajo · nuevo · problema · escuela · país · blanco · siempre · maíz · cuaderno · flores</em>. Después léalas dando una palmada en cada sílaba.</p></div>
<details class="caja caja-tip"><summary><strong>Ver las respuestas</strong></summary><p>tra-ba-jo · nue-vo · pro-ble-ma · es-cue-la · pa-ís (hiato) · blan-co · siem-pre · ma-íz (hiato) · cua-der-no · flo-res</p></details>"""

    secciones = [("s1", "Vocales fuertes y débiles", s1), ("s2", "Diptongos e hiatos", s2), ("s3", "Grupos de consonantes y letras dobles", s3), ("s4", "Lectura: «El tren de la mañana»", s4)]
    tarea = [("Cazador de diptongos.", "Busque en un periódico, una etiqueta o un anuncio cinco palabras con diptongo y tres con hiato. Cópielas separadas en sílabas."),
             ("Mi lista de grupos.", "Escriba una palabra de su vida diaria para cada grupo: br, cl, dr, fr, gr, pl, pr, tr."),
             ("Lectura grabada.", "Lea en voz alta «El tren de la mañana» y grábese. ¿Se trabó en alguna palabra? Sepárela en sílabas, practíquela y grábese otra vez.")]
    quiz = [
        ("¿Cuáles son las vocales fuertes?", ["a, e, o", "i, u", "a, i, u"], 0, {1: "Esas son las débiles.", 2: "La i y la u son débiles."}, "<strong>a, e, o.</strong>"),
        ("¿Qué es un diptongo?", ["Dos vocales en una misma sílaba", "Dos vocales en sílabas distintas", "Dos consonantes juntas"], 0, {1: "Eso es un hiato.", 2: "Eso es un grupo de consonantes."}, "Dos vocales en <strong>una sílaba</strong>."),
        ("<strong>poeta</strong> tiene…", ["hiato: po-e-ta", "diptongo: poe-ta"], 0, {}, "<strong>Hiato</strong>: dos fuertes juntas."),
        ("<strong>familia</strong> se separa…", ["fa-mi-lia", "fa-mi-li-a", "fam-i-lia"], 0, {1: "La i y la a forman diptongo.", 2: "La m abre la sílaba: mi."}, "<strong>fa-mi-lia.</strong>"),
        ("¿Por qué <strong>río</strong> tiene hiato?", ["Porque la í lleva tilde", "Porque tiene dos fuertes"], 0, {}, "La <strong>tilde</strong> en la í rompe el diptongo."),
        ("¿En cuál la u no suena?", ["queso", "cuaderno", "guarda"], 0, {1: "En cuaderno suena: cua.", 2: "En guarda suena: guar."}, "<strong>queso</strong>: que, qui."),
        ("¿Cuál es un grupo de consonantes que no se separa?", ["pl", "rt", "nc"], 0, {1: "Se separa: par-te.", 2: "Se separa: blan-co."}, "<strong>pl</strong>: pla-to."),
        ("<strong>perro</strong> se separa…", ["pe-rro", "per-ro"], 0, {}, "<strong>pe-rro</strong>: la rr no se separa."),
        ("<strong>canción</strong> se separa…", ["can-ción", "ca-nción", "canc-ión"], 0, {1: "La n cierra la primera sílaba.", 2: "No."}, "<strong>can-ción</strong>."),
        ("¿Qué indica la diéresis en <strong>pingüino</strong>?", ["Que la u sí suena", "Que la u no suena"], 0, {}, "Que la <strong>u sí suena</strong>."),
    ]
    filas = [
        ("Diptongo e hiato", "Distingo diptongos de hiatos, también con tilde y con h.", "Me confundo con la tilde.", "No los distingo (<a href=\"#s2\">repase la sección 2</a>)."),
        ("Grupos y letras dobles", "No separo bl, br, cl… ni ch, ll, rr.", "A veces separo un grupo.", "Separo mal (<a href=\"#s3\">repase la sección 3</a>)."),
        ("Leer palabras largas", "Leo palabras largas sin trabarme.", "Me trabo en algunas.", "Me trabo mucho (<a href=\"#s4\">repase la lectura</a>)."),
    ]
    cierre = "<p>Ya sabe cómo se agrupan las letras en sílabas. En la próxima lección usará los <strong>prefijos y sufijos</strong> para leer palabras nuevas.</p>"
    glosario = [("Vocal fuerte", "a, e, o."), ("Vocal débil", "i, u (y la y al final de palabra)."), ("Diptongo", "Dos vocales en una misma sílaba."),
                ("Hiato", "Dos vocales juntas en sílabas distintas."), ("Grupo consonántico", "Consonante + l o r que no se separa: bl, br, cl, cr…"), ("Diéresis", "Los dos puntos sobre la ü: indican que la u suena.")]
    conexion = ("<p>Bienvenido al Nivel 2, «Conectando ideas y textos». En el Nivel 1 separó en sílabas palabras sencillas; ahora verá cómo se agrupan las letras en las palabras largas de la vida diaria.</p>"
                "<p><strong>Lo que necesita:</strong> el cuaderno y lápices de dos colores.</p>")
    estd = LE.estandares([], base=["L.2.1"], fund=["RF.3", "RF.4"])
    return C.pagina_leccion(N, LE.titulo(N), "Dos vocales juntas, dos consonantes seguidas: así se agrupan.", ["Fundamentos de lectura", "Sílabas"],
                            ["<strong>Distinguir</strong> las vocales fuertes y débiles.", "<strong>Reconocer</strong> diptongos e hiatos.",
                             "<strong>Separar</strong> en sílabas palabras con grupos de consonantes y letras dobles.", "<strong>Leer</strong> en voz alta un texto con palabras largas."],
                            estd, conexion, secciones, tarea, quiz, filas, cierre, ("1-2", LE.titulo("1-2")), glosario, P)


def practica():
    dh = [{"enun": f"<strong class=\"grande\">{s.replace('-', '')}</strong> {LE.escuchar(s.replace('-', ''), '')}<br>¿Diptongo o hiato?", "ops": ["Diptongo", "Hiato"], "ok": 1 if h else 0, "enOrden": True, "pista": "",
           "exp": (f"Hiato: <strong>{s}</strong>. " + ("La vocal débil lleva tilde y forma su propia sílaba." if any(c in s for c in "íú") else "Son dos vocales fuertes, así que se separan.")) if h
           else f"Diptongo: <strong>{s}</strong>. Las dos vocales van juntas en la misma sílaba."} for lista, h in ((DIP, False), (HIA, True)) for s in lista]
    cor = [{"pal": s} for s in CORTES]
    gru = [{"enun": f"<strong class=\"grande\">{w.replace(g, '__', 1)}</strong> {LE.escuchar(w, '')}<br>¿Qué grupo falta?", "ops": [g] + d, "ok": 0, "pista": "Escuche la palabra: ¿suena con l o con r?",
            "exp": f"<strong>{w}</strong>: lleva <strong>{g}</strong>."} for w, g, d in GRUPOS]
    mods = [("diptongo", "¿Diptongo o hiato?", C.om("m1", "Escuche la palabra si quiere y decida.")),
            ("cortes", "Corte en sílabas", LE.marcar("m2", "Toque los espacios entre las letras para poner o quitar un corte. Después pulse <strong>Comprobar</strong>. Tiene dos intentos.")),
            ("grupos", "Escuche y complete el grupo", C.om("m3", "Elija el grupo de consonantes que falta."))]
    js = C.js_datos("DH", dh) + C.js_datos("COR", cor) + C.js_datos("GRU", gru) + 'creaBanco("m1", DH);\ncreaCortes("m2", COR);\ncreaBanco("m3", GRU);\n'
    return C.pagina_practica(N, LE.titulo(N), "Tres actividades · los ejercicios cambian cada vez · dos intentos en cada uno", mods, js)


if __name__ == "__main__":
    LE.construye(N, leccion, practica, horas="Unas 3 horas")
