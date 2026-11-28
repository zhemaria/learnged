# -*- coding: utf-8 -*-
"""LearnGED · Artes del lenguaje (español) · Nivel 1 · Lección 1.1 · El alfabeto.
Fuente: clases_leng1/clase_1-1.html (GEDparaHispanos), adaptada al marco de LearnGED.
Uso: python3 tools/build_leng1_1_1.py
"""
import json, os, random, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import leng_es as LE
from leng_es import C

LE.nivel(1)
N = "1-1"

# Letra, minúscula, palabra, emoji, nombre, cómo debe decirlo la voz (si la voz lo dice mal)
ABC = [("A", "a", "árbol", "🌳", "a", ""), ("B", "b", "barco", "⛵", "be", "beh"), ("C", "c", "casa", "🏠", "ce", ""),
       ("D", "d", "dedo", "👆", "de", ""), ("E", "e", "estrella", "⭐", "e", ""), ("F", "f", "flor", "🌸", "efe", ""),
       ("G", "g", "gato", "🐱", "ge", ""), ("H", "h", "hoja", "🍃", "hache", ""), ("I", "i", "isla", "🏝️", "i", ""),
       ("J", "j", "jugo", "🥤", "jota", ""), ("K", "k", "kilo", "⚖️", "ka", ""), ("L", "l", "luna", "🌙", "ele", ""),
       ("M", "m", "manzana", "🍎", "eme", ""), ("N", "n", "nube", "☁️", "ene", ""), ("Ñ", "ñ", "ñame", "🍠", "eñe", ""),
       ("O", "o", "oso", "🐻", "o", ""), ("P", "p", "pan", "🍞", "pe", "la pe"), ("Q", "q", "queso", "🧀", "cu", "ku"),
       ("R", "r", "ratón", "🐭", "erre", ""), ("S", "s", "sol", "☀️", "ese", ""), ("T", "t", "taza", "🍵", "te", ""),
       ("U", "u", "uva", "🍇", "u", ""), ("V", "v", "vaca", "🐄", "uve", ""), ("W", "w", "wifi", "📶", "doble uve", ""),
       ("X", "x", "xilófono", "🎵", "equis", ""), ("Y", "y", "yate", "🛥️", "ye", "lle"), ("Z", "z", "zapato", "👞", "zeta", "")]
LETRAS = "".join(x[0] for x in ABC)
# Letras que se confunden por su forma (para los distractores)
PARECIDAS = {"b": "dpqh", "d": "bpqa", "p": "qbdg", "q": "pgbd", "n": "mñuh", "m": "nñw", "ñ": "nmu", "u": "nvñ", "g": "qjy", "j": "igy",
             "i": "jlt", "l": "ift", "h": "bnk", "r": "nvt", "v": "uwy", "w": "vmu", "y": "vgj", "e": "aco", "a": "eod", "o": "aec",
             "c": "eoz", "f": "tlk", "t": "fli", "k": "hxl", "x": "kyz", "z": "sxc", "s": "zcx"}


def abc_json():
    return json.dumps([{"M": M, "m": m, "p": p, "e": e, "n": n, "v": v} for M, m, p, e, n, v in ABC], ensure_ascii=False)


def leccion():
    P = C.Practicas()
    s1 = f"""<p>El alfabeto del español tiene <strong>27 letras</strong>. Cada letra tiene dos formas: la <strong>mayúscula</strong>, grande, y la <strong>minúscula</strong>, pequeña. Casi todo lo que usted lee está en minúsculas; las mayúsculas aparecen en lugares concretos, que verá en la sección 2.</p>
{C.tabla("Las dos formas de las letras", ["Forma", "Cómo es", "Ejemplo"],
         [["Mayúscula", "Grande. Todas las mayúsculas tienen la misma altura.", "M A R Í A"],
          ["Minúscula", "Pequeña. Algunas suben (b, d, h, l…) y otras bajan (g, j, p, q, y).", "m a r í a"]])}
<h3>El abecedario ilustrado</h3>
<p>Toque cualquier letra para oír su nombre y una palabra que empieza con ella. Haga tres pasadas:</p>
<ol>
<li><strong>Primera:</strong> toque las letras una por una y escuche.</li>
<li><strong>Segunda:</strong> pulse «Escuchar todo el abecedario» y repita en voz alta junto con la voz.</li>
<li><strong>Tercera:</strong> diga usted solo el abecedario y compruebe con la pantalla las letras en que dude.</li>
</ol>
{LE.AVISO_VOZ}
<p><button type="button" class="btn-voz" id="abc1-todo"><span aria-hidden="true">🔊</span> Escuchar todo el abecedario</button>
<button type="button" class="btn-voz" id="abc1-parar"><span aria-hidden="true">⏹</span> Detener</button></p>
<div class="abc" id="abc1" data-abc='{abc_json()}'></div>
{C.caja("tip", "El nombre y el sonido", "<p>Cada letra tiene un <strong>nombre</strong> (lo que dice al deletrear) y un <strong>sonido</strong> (cómo suena dentro de una palabra). La B se llama «be», pero en <em>barco</em> suena «b». La H se llama «hache», pero en español no suena: <em>hola</em> se pronuncia «ola». En el Tema 2 trabajará los sonidos con calma.</p>")}
{C.caja("ojo", "Letras con dos nombres", "<p>La <strong>Y</strong> se llama <em>ye</em>; también se le dice <em>i griega</em>. La <strong>V</strong> se llama <em>uve</em>, y en América es muy común decirle <em>ve</em> o <em>ve corta</em>; la <strong>W</strong>, <em>doble uve</em> o <em>doble ve</em>. Va a oír los dos nombres y los dos son correctos.</p><p>La <strong>ch</strong> y la <strong>ll</strong> ya no se cuentan como letras: son dos letras juntas que forman un solo sonido (<em>chile</em>, <em>lluvia</em>). Por eso el alfabeto tiene 27 letras y no 29.</p>")}
{P("Compruebe", "¿Cuántas letras tiene el alfabeto del español?", ["26", "27", "29"], 1,
   {0: "26 son las del inglés. El español tiene una más, que el inglés no tiene: ¿cuál?", 2: "Antes se contaban la ch y la ll, pero hoy son dos letras juntas, no letras aparte."},
   "Son <strong>27</strong>: las 26 del inglés más la <strong>ñ</strong>.")}"""

    s2 = f"""<p>Se escribe con <strong>mayúscula</strong> la primera letra de:</p>
<ul>
<li><strong>Cada oración:</strong> <em>Hoy empiezo a estudiar.</em></li>
<li><strong>Los nombres propios</strong> de personas, ciudades, países, calles, escuelas y empresas: <em>María, Chicago, Guatemala, Truman College</em>.</li>
<li>Y van <strong>todas en mayúscula</strong> las siglas: <em>GED, EE. UU., ONU</em>.</li>
</ul>
<p>Todo lo demás va en minúscula. En español, a diferencia del inglés, van con minúscula los <strong>días de la semana</strong>, los <strong>meses</strong>, los <strong>idiomas</strong> y las <strong>nacionalidades</strong>: <em>el lunes 3 de marzo; hablo español; soy mexicano</em>.</p>
{C.ejemplo("Ejemplo · Un recado bien escrito", [
    ("1", "<em>el martes llamó la señora ruiz desde chicago.</em> → Esta oración tiene tres errores de mayúscula."),
    ("2", "La primera palabra de la oración va con mayúscula: <strong>El</strong>."),
    ("3", "<em>Ruiz</em> es un apellido y <em>Chicago</em> una ciudad: los dos son nombres propios, con mayúscula."),
    ("4", "<em>martes</em> es un día de la semana: en español se queda en minúscula.")],
    "<strong>El</strong> martes llamó la señora <strong>Ruiz</strong> desde <strong>Chicago</strong>.")}
{C.caja("ojo", "Un error que viene del inglés", "<p>En inglés se escribe <em>Monday</em>, <em>March</em>, <em>Spanish</em> con mayúscula. En español no: <em>lunes</em>, <em>marzo</em>, <em>español</em>. El examen GED en español sigue la norma del español.</p>")}
{P("Compruebe", "¿Cuál está bien escrita?", ["Mi cita es el Lunes en Houston.", "Mi cita es el lunes en Houston.", "mi cita es el lunes en houston."], 1,
   {0: "En español, los días de la semana van con minúscula.", 2: "La oración empieza con mayúscula, y Houston es el nombre de una ciudad."},
   "<em>Mi</em> empieza la oración y <em>Houston</em> es un nombre propio; <em>lunes</em> va en minúscula.")}"""

    s3 = f"""<p>Algunas letras se confunden porque se parecen mucho. Fíjese en hacia dónde mira la «barriga» de la letra y si el palito sube o baja:</p>
{C.tabla("Letras que se confunden por su forma", ["Letras", "Cómo distinguirlas", "Ejemplos"],
         [["b · d", "La <strong>b</strong> tiene el palito a la izquierda y la barriga a la derecha; la <strong>d</strong>, al revés.", "<em>boca · dedo</em>"],
          ["p · q", "Las dos tienen el palito hacia abajo. La <strong>p</strong> lleva la barriga a la derecha; la <strong>q</strong>, a la izquierda, y siempre va con <em>u</em> (<em>que, qui</em>).", "<em>pan · queso</em>"],
          ["n · ñ", "La <strong>ñ</strong> lleva una rayita ondulada encima (la tilde de la eñe).", "<em>pena · peña</em>"],
          ["m · n", "La <strong>m</strong> tiene dos jorobas; la <strong>n</strong>, una.", "<em>mesa · nube</em>"]])}
<p>Otras se confunden porque <strong>suenan igual</strong>, aunque se escriben distinto:</p>
<ul>
<li><strong>b</strong> y <strong>v</strong> suenan igual: <em>barco, vaca</em>.</li>
<li><strong>c</strong> (ante a, o, u), <strong>k</strong> y <strong>qu</strong> suenan igual: <em>casa, kilo, queso</em>.</li>
<li>En casi toda América, <strong>s</strong>, <strong>z</strong> y <strong>c</strong> (ante e, i) suenan igual: <em>sol, zapato, cena</em>.</li>
<li>La <strong>h</strong> no suena: <em>hoja</em> se dice «oja».</li>
</ul>
<p>Por eso, para escribir bien no basta con oír la palabra: hay que recordar cómo se ve. Su diccionario personal (sección 4) le ayudará.</p>
{P("Compruebe", "¿Con qué letra empieza <strong>vaca</strong>? <span aria-hidden=\"true\">🐄</span>", ["B", "V", "F"], 1,
   {0: "La b y la v suenan igual, pero esta palabra se escribe con la letra de la «ve corta».", 2: "La f suena distinto: se dice soplando entre los dientes y el labio."},
   "<em>Vaca</em> se escribe con <strong>V</strong>. Suena igual que la b: hay que recordar cómo se ve la palabra.")}"""

    s4 = f"""<div class="caja caja-tip"><span class="etiqueta et-verde">Actividad · en voz alta y en su cuaderno</span>
<p>Elija una letra y escriba en su cuaderno <strong>tres palabras</strong> que empiecen con ella. Después dígalas en voz alta. Repita hasta completar <strong>diez letras</strong>.</p>
<ul><li>Letra M: <em>mesa, mamá, mango</em>.</li><li>Letra C: <em>carro, casa, café</em>.</li><li>Letra P: <em>perro, pan, paz</em>.</li></ul>
<p>No repita palabras. Si duda con una letra difícil (K, W, X, Y, Ñ), vuelva al abecedario de la sección 1 y escuche la palabra de ejemplo. Guarde la lista: es el comienzo de su <strong>diccionario personal</strong>, que seguirá llenando en las próximas lecciones.</p></div>
{C.caja("tip", "Si tiene con quién practicar", "<p>Conviértalo en un juego: por turnos, uno dice una letra y el otro nombra tres cosas que empiecen con ella. No se vale repetir.</p>")}"""

    s5 = f"""<p>Toque primero una <strong>mayúscula</strong> (columna de la izquierda) y después su <strong>minúscula</strong> (columna de la derecha). Si son pareja, se ponen verdes. Cuando termine, pida otra tanda: salen letras distintas cada vez.</p>
<div class="emparejar" id="emp1" data-letras="{LETRAS}" data-n="7">
<div class="emp-cols"></div>
<p class="fb emp-estado" role="status" aria-live="polite"></p>
<p><button type="button" class="btn-sec emp-otra">Otra tanda de letras</button></p>
</div>
<p>En la <a href="{C.prac(N)}">página de práctica</a> tiene más ejercicios de mayúsculas, minúsculas y primeras letras.</p>"""

    secciones = [("s1", "El abecedario del español", s1), ("s2", "¿Cuándo se usa la mayúscula?", s2), ("s3", "Letras que se confunden", s3),
                 ("s4", "Actividad: palabras que empiezan con mi letra", s4), ("s5", "Práctica: emparejar mayúscula y minúscula", s5)]
    tarea = [("Mi nombre con mayúscula.", "Escriba su nombre completo, el de tres personas de su familia y el de la ciudad donde vive. Revise que cada uno empiece con mayúscula."),
             ("El abecedario de memoria.", "Escriba las 27 letras en orden, primero en mayúscula y después en minúscula. Compruébelas con el abecedario de la sección 1."),
             ("Mi diccionario personal.", "Complete la lista de la sección 4 hasta tener tres palabras para cada una de las 27 letras. Para K, W, X e Y puede usar <em>kilo, wifi, xilófono, yate</em>."),
             ("En la calle.", "Copie una palabra de tres letreros que vea (en la tienda, en el autobús, en el trabajo). ¿Está en mayúsculas o en minúsculas?")]
    quiz = [
        ("¿Cuál es la minúscula de <strong>G</strong>?", ["g", "q", "j"], 0, {1: "La q también baja, pero su barriga mira hacia la izquierda y siempre va con u.", 2: "La j tiene un punto arriba."}, "La minúscula de G es <strong>g</strong>."),
        ("¿Cuál es la minúscula de <strong>B</strong>?", ["d", "p", "b"], 2, {0: "En la d, la barriga está a la izquierda del palito.", 1: "En la p, el palito baja."}, "La minúscula de B es <strong>b</strong>: palito arriba y barriga a la derecha."),
        ("¿Cuál es la minúscula de <strong>Ñ</strong>?", ["ñ", "n", "m"], 0, {1: "Le falta la rayita ondulada de encima.", 2: "La m tiene dos jorobas."}, "La minúscula de Ñ es <strong>ñ</strong>, con su tilde encima."),
        ("¿Cuál es la mayúscula de <strong>d</strong>?", ["B", "P", "D"], 2, {0: "La B es la mayúscula de b.", 1: "La P es la mayúscula de p."}, "La mayúscula de d es <strong>D</strong>."),
        ("¿Cuál es la mayúscula de <strong>h</strong>?", ["H", "N", "K"], 0, {1: "La N es la mayúscula de n.", 2: "La K es la mayúscula de k."}, "La mayúscula de h es <strong>H</strong>."),
        ("¿Con qué letra empieza <strong>queso</strong>? <span aria-hidden=\"true\">🧀</span>", ["K", "Q", "C"], 1, {0: "Suena igual, pero queso no se escribe con k.", 2: "La c no puede ir delante de «ue» con ese sonido: se escribe qu."}, "<em>Queso</em> empieza con <strong>Q</strong> (que, qui)."),
        ("¿Con qué letra empieza <strong>hoja</strong>? <span aria-hidden=\"true\">🍃</span>", ["O", "J", "H"], 2, {0: "Se oye «oja», pero hay una letra muda antes de la o.", 1: "La j está en medio de la palabra, no al principio."}, "<em>Hoja</em> empieza con <strong>H</strong>, que no suena."),
        ("¿Con qué letra empieza <strong>zapato</strong>? <span aria-hidden=\"true\">👞</span>", ["Z", "S", "C"], 0, {1: "En América suenan igual, pero zapato no se escribe con s.", 2: "La c solo suena así delante de e o i."}, "<em>Zapato</em> empieza con <strong>Z</strong>."),
        ("¿Cuántas letras tiene el alfabeto del español?", ["26", "27", "29"], 1, {0: "Esas son las del inglés. Falta una.", 2: "La ch y la ll ya no se cuentan como letras."}, "Son <strong>27</strong>."),
        ("¿Qué letra tiene el español que el inglés <strong>no</strong> tiene?", ["la W", "la K", "la Ñ"], 2, {0: "La w está en los dos alfabetos.", 1: "La k está en los dos alfabetos."}, "La <strong>Ñ</strong>."),
        ("¿Qué letra se escribe pero <strong>no suena</strong> en «hola»?", ["la O", "la L", "la H"], 2, {0: "La o sí suena.", 1: "La l sí suena."}, "La <strong>H</strong> es muda en español."),
        ("¿Cuál está bien escrita?", ["Vivo en Chicago desde Enero.", "vivo en Chicago desde enero.", "Vivo en Chicago desde enero."], 2, {0: "Los meses van con minúscula en español.", 1: "La oración tiene que empezar con mayúscula."}, "<strong>Vivo en Chicago desde enero.</strong> Mayúscula al principio y en el nombre de la ciudad; el mes, en minúscula."),
        ("¿Cuál de estas palabras debe ir siempre con mayúscula?", ["martes", "Guatemala", "español"], 1, {0: "Los días de la semana van con minúscula.", 2: "Los idiomas van con minúscula."}, "<strong>Guatemala</strong> es el nombre de un país: es un nombre propio."),
    ]
    filas = [
        ("Reconocer las 27 letras", "Digo el abecedario completo y reconozco cada letra en mayúscula y minúscula.", "Dudo con algunas letras (b/d, p/q, Ñ).", "Me salto letras o las confundo seguido (<a href=\"#s1\">repase la sección 1</a>)."),
        ("Usar la mayúscula", "Pongo mayúscula al inicio de la oración y en los nombres propios, y no en días ni meses.", "A veces olvido la mayúscula en un nombre propio.", "No sé cuándo va (<a href=\"#s2\">repase la sección 2</a>)."),
        ("Distinguir letras parecidas", "Distingo b/d, p/q, n/ñ y sé que b y v suenan igual.", "Me confundo cuando leo rápido.", "Las confundo casi siempre (<a href=\"#s3\">repase la sección 3</a>)."),
    ]
    cierre = "<p>Ya conoce las 27 letras, sus dos formas y cuándo va la mayúscula. En la próxima lección verá hacia dónde se mueven los ojos al leer y de qué partes está hecha una oración.</p>"
    glosario = [("Alfabeto (abecedario)", "Las 27 letras del español en su orden."), ("Mayúscula", "La forma grande de una letra: A, B, C."),
                ("Minúscula", "La forma pequeña de una letra: a, b, c."), ("Nombre propio", "El nombre de una persona, un lugar o una institución concreta; va con mayúscula: <em>Ana, Texas</em>."),
                ("Sigla", "Palabra formada por las iniciales de otras, toda en mayúscula: <em>GED</em>."), ("Letra muda", "Letra que se escribe pero no suena, como la h.")]
    conexion = ("<p>Bienvenido al primer tema. Antes de leer y escribir oraciones, vamos a repasar lo más básico: las letras. Algunas las recuerda perfectamente y otras quizás se le confunden, sobre todo si ha aprendido inglés y español al mismo tiempo. Esta lección es la base de todo lo que viene.</p>"
                "<p><strong>Lo que necesita:</strong> un cuaderno, un lápiz y el volumen activado (o audífonos): esta lección tiene sonido.</p>")
    estd = LE.estandares([], base=["L.2.1"], fund=["RF.1", "RF.3"])
    return C.pagina_leccion(N, LE.titulo(N), "Veintisiete letras, dos formas cada una. Aquí empieza todo.",
                            ["Fundamentos de lectura", "L.2.1 · Mayúsculas"],
                            ["<strong>Reconocer y nombrar</strong> las 27 letras del alfabeto en mayúscula y en minúscula.",
                             "<strong>Usar la mayúscula</strong> al inicio de la oración y en los nombres propios, y no en días, meses ni idiomas.",
                             "<strong>Distinguir</strong> las letras que se confunden por su forma (b/d, p/q, n/ñ) o por su sonido (b/v, c/k/q).",
                             "<strong>Relacionar</strong> cada letra con palabras que empiezan con ella."],
                            estd, conexion, secciones, tarea, quiz, filas, cierre, ("1-2", LE.titulo("1-2")), glosario, P)


# ---------------------------------------------------------------- práctica
def banco_minus():
    b = []
    for M, m, *_ in ABC:
        dis = [x for x in PARECIDAS.get(m, "") if x != m][:2]
        while len(dis) < 2:
            x = random.Random(M).choice("abcdefghijklmnopqrstuvwxyz")
            if x != m and x not in dis:
                dis.append(x)
        b.append({"enun": f"¿Cuál es la <strong>minúscula</strong> de <span class=\"grande\">{M}</span>?", "ops": [f'<span class="grande">{x}</span>' for x in [m] + dis], "ok": 0,
                  "pista": f"Busque la forma pequeña de la {M}. Vuelva a mirarla en el abecedario si duda.", "exp": f"La minúscula de {M} es <strong>{m}</strong>."})
        b.append({"enun": f"¿Cuál es la <strong>mayúscula</strong> de <span class=\"grande\">{m}</span>?", "ops": [f'<span class="grande">{x}</span>' for x in [M] + [d.upper() for d in dis]], "ok": 0,
                  "pista": f"Busque la forma grande de la {m}.", "exp": f"La mayúscula de {m} es <strong>{M}</strong>."})
    return b


def banco_inicial():
    datos = [("pan", "🍞", "P", "BD", "La p y la b se parecen: la p tiene el palito hacia abajo."), ("vaca", "🐄", "V", "BF", "Suena igual que la b, pero vaca va con v."),
             ("barco", "⛵", "B", "VD", "Suena igual que la v, pero barco va con b."), ("queso", "🧀", "Q", "KC", "Que, qui se escriben con qu."),
             ("casa", "🏠", "C", "KQ", "Ca, co, cu se escriben con c."), ("kilo", "⚖️", "K", "CQ", "Es de las pocas palabras con k."),
             ("hoja", "🍃", "H", "OJ", "Hay una letra muda antes de la o."), ("huevo", "🥚", "H", "UG", "Hay una letra muda al principio."),
             ("zapato", "👞", "Z", "SC", "En América suena como s, pero se escribe con z."), ("sol", "☀️", "S", "ZC", "Se escribe con s."),
             ("cebolla", "🧅", "C", "SZ", "Ce, ci suenan como s en América, pero se escriben con c."), ("gato", "🐱", "G", "JQ", "Ga, go, gu se escriben con g."),
             ("jugo", "🥤", "J", "GH", "Se escribe con j."), ("llave", "🔑", "L", "YI", "Empieza con ll: dos eles juntas."),
             ("yate", "🛥️", "Y", "LI", "Se escribe con y."), ("ñame", "🍠", "Ñ", "NM", "Lleva la letra que solo tiene el español."),
             ("dedo", "👆", "D", "BP", "La d tiene la barriga a la izquierda."), ("uva", "🍇", "U", "OV", "Empieza con una vocal."),
             ("iglesia", "⛪", "I", "EY", "Empieza con una vocal."), ("wifi", "📶", "W", "VU", "Es una palabra que viene del inglés.")]
    return [{"enun": f"<span class=\"emoji-grande\" aria-hidden=\"true\">{e}</span> ¿Con qué letra empieza <strong>{w}</strong>?",
             "ops": [L] + list(d), "ok": 0, "pista": p, "exp": f"<em>{w.capitalize()}</em> empieza con <strong>{L}</strong>."} for w, e, L, d, p in datos]


def banco_mayus():
    datos = [
        (["Mi hija vive en Miami.", "mi hija vive en miami.", "Mi hija vive en miami."], 0, "La oración empieza con mayúscula y Miami es una ciudad."),
        (["El examen es en Abril.", "El examen es en abril.", "el examen es en abril."], 1, "Los meses van con minúscula; la oración empieza con mayúscula."),
        (["Hablo Español e Inglés.", "hablo español e inglés.", "Hablo español e inglés."], 2, "Los idiomas van con minúscula en español."),
        (["Trabajo los Sábados.", "Trabajo los sábados.", "trabajo los sábados."], 1, "Los días de la semana van con minúscula."),
        (["Mi vecino Pedro es Mexicano.", "Mi vecino pedro es mexicano.", "Mi vecino Pedro es mexicano."], 2, "Pedro es nombre propio; las nacionalidades van con minúscula."),
        (["Estudio para el GED.", "Estudio para el ged.", "estudio para el Ged."], 0, "Las siglas van todas en mayúscula."),
        (["La clínica está en la calle Ashland.", "La Clínica está en la Calle Ashland.", "la clínica está en la calle ashland."], 0, "Solo el nombre de la calle (Ashland) es propio."),
        (["Mañana voy a Puerto Rico.", "Mañana voy a puerto rico.", "mañana voy a Puerto Rico."], 0, "Puerto Rico es un nombre propio y la oración empieza con mayúscula."),
        (["El Lunes empieza la clase.", "El lunes empieza la clase.", "el lunes empieza la clase."], 1, "El día va en minúscula; la primera palabra, en mayúscula."),
        (["Mi Mamá se llama Rosa.", "Mi mamá se llama rosa.", "Mi mamá se llama Rosa."], 2, "Rosa es un nombre de persona; mamá es una palabra común."),
    ]
    pist = "Revise tres cosas: la primera palabra, los nombres propios y los días, meses, idiomas o nacionalidades."
    return [{"enun": "¿Cuál está bien escrita?", "ops": o, "ok": k, "pista": pist, "exp": e, "enOrden": False} for o, k, e in datos]


def banco_orden():
    b = []
    letras = [x[0] for x in ABC]
    for i in range(len(letras) - 1):
        ok = letras[i + 1]
        cerca = [letras[j] for j in (i - 1, i + 2, i + 3) if 0 <= j < len(letras) and letras[j] != ok][:2]
        b.append({"enun": f"En el abecedario, ¿qué letra va <strong>después</strong> de la <span class=\"grande\">{letras[i]}</span>?",
                  "ops": [ok] + cerca, "ok": 0, "pista": "Diga el abecedario en voz alta desde un poco antes de esa letra.",
                  "exp": f"{letras[i]}, <strong>{ok}</strong>." + (" La Ñ va justo después de la N." if ok == "Ñ" else "")})
    return b


def practica():
    mods = [
        ("mayus-minus", "Mayúscula y minúscula", C.om("m1", "Elija la otra forma de la letra. Fíjese bien en las letras que se parecen.")),
        ("primera-letra", "¿Con qué letra empieza?", C.om("m2", "Mire el dibujo, diga la palabra en voz alta y elija su primera letra. Cuidado con las letras que suenan igual.")),
        ("mayuscula", "¿Lleva mayúscula?", C.om("m3", "Elija la oración bien escrita: mayúscula al inicio y en los nombres propios; minúscula en días, meses, idiomas y nacionalidades.")),
        ("orden", "El orden del abecedario", C.om("m4", "Elija la letra que va después.")),
    ]
    js = (C.js_datos("MINUS", banco_minus()) + C.js_datos("INI", banco_inicial()) + C.js_datos("MAY", banco_mayus()) + C.js_datos("ORD", banco_orden()) +
          'creaBanco("m1", MINUS);\ncreaBanco("m2", INI);\ncreaBanco("m3", MAY);\ncreaBanco("m4", ORD);\n')
    return C.pagina_practica(N, LE.titulo(N), "Cuatro actividades · los ejercicios cambian cada vez · dos intentos en cada uno", mods, js)


if __name__ == "__main__":
    LE.construye(N, leccion, practica, horas="Unas 3 horas")
