# -*- coding: utf-8 -*-
"""LearnGED · Artes del lenguaje (español) · Nivel 1 · Lección 6.3 · La anatomía de los mapas.
Fuente: clases_leng1/clase_6-3.html (GEDparaHispanos) y gramatica/n1-l6-3.html, adaptadas al marco de LearnGED.
El mapa del barrio Las Flores se dibuja aquí en SVG; las preguntas de dirección se calculan a partir de la cuadrícula.
Uso: python3 tools/build_leng1_6_3.py
"""
import os, sys, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import leng_es as LE
from leng_es import C

LE.nivel(1)
N = "6-3"
# lugar: (fila 0 norte → 2 sur, columna 0 oeste → 2 este, emoji, color)
LUGARES = {"la escuela": (0, 0, "🏫"), "la tienda": (0, 2, "🛒"), "la biblioteca": (1, 1, "📚"), "el hospital": (1, 2, "🏥"), "mi casa": (2, 0, "🏠"), "el parque": (2, 1, "🌳")}
LEY = [("🏫", "Escuela"), ("📚", "Biblioteca"), ("🏥", "Hospital"), ("🌳", "Parque"), ("🛒", "Tienda"), ("🏠", "Mi casa"), ("🚏", "Parada de autobús")]
BX = [20, 164, 308]
BY = [60, 204, 348]
B = 120


def mapa(k="m"):
    s = [f'<svg viewBox="0 0 660 520" role="img" aria-labelledby="{k}-t {k}-d" class="mapa-svg">',
         f'<title id="{k}-t">Mapa del barrio Las Flores</title>',
         f'<desc id="{k}-d">Mapa visto desde arriba, con el norte arriba. Dos calles cruzan de oeste a este: la Calle Roble, más al norte, y la Calle Pino, más al sur. '
         'Dos avenidas van de norte a sur: la Avenida Sol, al oeste, y la Avenida Luna, al este. Quedan nueve cuadras. Fila de arriba, de oeste a este: la escuela, una cuadra vacía y la tienda. '
         'Fila del medio: una cuadra vacía, la biblioteca y el hospital. Fila de abajo: mi casa, el parque y una cuadra vacía. Hay tres paradas de autobús: dos en la Calle Roble y una en la Calle Pino. '
         'A la derecha están la rosa de los vientos y la leyenda; abajo, la escala: la barra mide 100 metros, lo mismo que una cuadra.</desc>',
         '<rect x="0" y="0" width="660" height="520" fill="#fff"/>',
         '<text x="214" y="34" text-anchor="middle" font-size="22" font-weight="800" fill="#111827">Mapa del barrio Las Flores</text>',
         '<rect x="20" y="180" width="408" height="24" fill="#9ca3af"/><rect x="20" y="324" width="408" height="24" fill="#9ca3af"/>',
         '<rect x="140" y="60" width="24" height="408" fill="#9ca3af"/><rect x="284" y="60" width="24" height="408" fill="#9ca3af"/>',
         '<text x="400" y="197" text-anchor="end" font-size="14" font-weight="700" fill="#fff">Calle Roble</text>',
         '<text x="400" y="341" text-anchor="end" font-size="14" font-weight="700" fill="#fff">Calle Pino</text>',
         '<text x="157" y="440" font-size="14" font-weight="700" fill="#fff" transform="rotate(-90 157 440)">Av. Sol</text>',
         '<text x="301" y="440" font-size="14" font-weight="700" fill="#fff" transform="rotate(-90 301 440)">Av. Luna</text>']
    for f in range(3):
        for c in range(3):
            s.append(f'<rect x="{BX[c]}" y="{BY[f]}" width="{B}" height="{B}" rx="6" fill="#ecfdf5" stroke="#6b7280"/>')
    for n, (f, c, e) in LUGARES.items():
        s.append(f'<text x="{BX[c] + 60}" y="{BY[f] + 78}" text-anchor="middle" font-size="54">{e}</text>')
    for x, y in [(80, 192), (224, 192), (224, 336)]:
        s.append(f'<text x="{x}" y="{y + 8}" text-anchor="middle" font-size="22">🚏</text>')
    # rosa de los vientos
    s += ['<g transform="translate(545 110)"><polygon points="0,-46 9,-8 0,-14 -9,-8" fill="#b42318"/><polygon points="0,46 9,8 0,14 -9,8" fill="#374151"/>',
          '<polygon points="46,0 8,9 14,0 8,-9" fill="#374151"/><polygon points="-46,0 -8,9 -14,0 -8,-9" fill="#374151"/>',
          '<text x="0" y="-52" text-anchor="middle" font-size="18" font-weight="800" fill="#b42318">N</text><text x="0" y="68" text-anchor="middle" font-size="18" font-weight="800">S</text>',
          '<text x="58" y="6" text-anchor="middle" font-size="18" font-weight="800">E</text><text x="-58" y="6" text-anchor="middle" font-size="18" font-weight="800">O</text></g>']
    # leyenda
    s.append('<rect x="460" y="200" width="195" height="250" rx="8" fill="#f8fafc" stroke="#94a3b8"/><text x="557" y="224" text-anchor="middle" font-size="17" font-weight="800">Leyenda</text>')
    for i, (e, n) in enumerate(LEY):
        s.append(f'<text x="480" y="{256 + i * 29}" font-size="20">{e}</text><text x="512" y="{254 + i * 29}" font-size="15">{n}</text>')
    # escala
    s += ['<g transform="translate(20 496)"><rect x="0" y="-8" width="60" height="8" fill="#111827"/><rect x="60" y="-8" width="60" height="8" fill="#fff" stroke="#111827"/>',
          '<text x="0" y="12" font-size="13" text-anchor="middle">0</text><text x="60" y="12" font-size="13" text-anchor="middle">50</text><text x="120" y="12" font-size="13" text-anchor="middle">100 m</text>',
          '<text x="160" y="0" font-size="14" font-weight="700">Escala</text></g>']
    s.append('</svg>')
    return '<figure class="figura mapa">' + "".join(s) + "</figure>"


def direccion(a, b):
    """¿Hacia dónde queda a con respecto a b?"""
    fa, ca, _ = LUGARES[a]; fb, cb, _ = LUGARES[b]
    ns = "norte" if fa < fb else "sur" if fa > fb else ""
    eo = "este" if ca > cb else "oeste" if ca < cb else ""
    return "al " + ((ns[:3] if ns == "norte" else ns) + eo if ns and eo else ns or eo)


TODAS = ["al norte", "al sur", "al este", "al oeste", "al noreste", "al noroeste", "al sureste", "al suroeste"]
OPUESTO = {"norte": "sur", "sur": "norte", "este": "oeste", "oeste": "este", "noreste": "suroeste", "suroeste": "noreste", "noroeste": "sureste", "sureste": "noroeste"}
TIPOS = [("Un mapa que muestra montañas y ríos es un mapa…", "físico", ["político", "de calles"]), ("Un mapa que muestra las fronteras entre países es un mapa…", "político", ["físico", "histórico"]),
         ("Un mapa que muestra cómo cambió un territorio con el tiempo es un mapa…", "histórico", ["de calles", "físico"]), ("Un mapa con avenidas, paradas y edificios de un barrio es un mapa…", "de calles", ["político", "histórico"])]
ELEM = [("¿Qué elemento del mapa le dice qué significa cada símbolo?", "La leyenda", ["La escala", "El título"]), ("¿Qué elemento le dice hacia dónde queda el norte?", "La rosa de los vientos", ["La leyenda", "La escala"]),
        ("¿Qué elemento le ayuda a saber cuántos metros hay entre dos lugares?", "La escala", ["La rosa de los vientos", "El título"]), ("¿Qué elemento le dice de qué lugar es el mapa?", "El título", ["La escala", "La leyenda"]),
        ("En el mapa, la barra que dice «100 m» es…", "la escala", ["la leyenda", "la rosa de los vientos"]), ("El cuadro que muestra cada símbolo con su nombre es…", "la leyenda", ["el título", "la escala"])]
LEE = [("Según la leyenda, ¿qué significa 🚏?", "Una parada de autobús", ["Un banco", "Una biblioteca"]), ("Según la leyenda, ¿qué significa 📚?", "La biblioteca", ["La escuela", "La tienda"]),
       ("¿Cuántas paradas de autobús hay en la Calle Roble?", "Dos", ["Una", "Tres"]), ("¿Qué calle está más al sur?", "La Calle Pino", ["La Calle Roble", "La Avenida Sol"]),
       ("¿Qué avenida está más al este?", "La Avenida Luna", ["La Avenida Sol", "La Calle Roble"]), ("¿Qué hay justo al sur de la escuela, al otro lado de la Calle Roble?", "Una cuadra vacía", ["La biblioteca", "Mi casa"]),
       ("Según la escala, ¿cuánto mide más o menos una cuadra de lado?", "100 metros", ["10 metros", "1 kilómetro"]), ("¿Entre qué calles está el hospital?", "Entre la Calle Roble y la Calle Pino", ["Al norte de la Calle Roble", "Al sur de la Calle Pino"])]


def leccion():
    P = C.Practicas()
    s1 = f"""<p>Un mapa es una imagen plana que muestra un lugar <strong>visto desde arriba</strong>, como desde un avión. Sirve para saber dónde están las cosas unas respecto de otras. En el examen de Estudios Sociales aparece mucho.</p>
{C.tabla("Tipos básicos de mapas", ["Tipo", "Qué muestra"],
         [["🗺️ Político", "Las divisiones entre países, estados o ciudades: las fronteras."], ["⛰️ Físico", "Montañas, ríos, valles y otras formas del terreno."],
          ["🏙️ De calles", "Calles, avenidas y lugares importantes de una ciudad o un barrio."], ["📜 Histórico", "Cómo cambió un territorio con el tiempo."]])}
{P("Compruebe", "Un mapa que muestra las fronteras entre los estados es un mapa…", ["político", "físico", "de calles"], 0, {1: "El físico muestra montañas y ríos.", 2: "El de calles muestra un barrio."}, "<strong>Político</strong>.")}"""

    s2 = f"""<p>Todo mapa bien hecho tiene cuatro elementos. Sin ellos, es un dibujo sin contexto.</p>
{C.tabla("Los cuatro elementos del mapa", ["Elemento", "Qué hace"],
         [["1 · Título", "Dice de qué lugar o época es el mapa. Léalo primero."], ["2 · Rosa de los vientos", "Muestra los puntos cardinales: norte, sur, este y oeste."],
          ["3 · Leyenda (o clave)", "Explica qué significan los símbolos, colores y líneas."], ["4 · Escala", "Relaciona el tamaño en el papel con la distancia real."]])}
{C.caja("tip", "La regla práctica", "<p>En la mayoría de los mapas, el <strong>norte está arriba</strong>. Entonces el sur está abajo, el este a la derecha y el oeste a la izquierda. Pero compruébelo siempre en la rosa de los vientos. Entre dos puntos están las direcciones intermedias: <strong>noreste</strong> (arriba a la derecha), <strong>noroeste</strong> (arriba a la izquierda), <strong>sureste</strong> y <strong>suroeste</strong>.</p>")}
{C.caja("ojo", "La escala", "<p>El mapa es una versión «encogida» del lugar real. La escala dice cuánto mide en la realidad un trozo del mapa: en un mapa de un país, un centímetro puede ser 100 kilómetros; en el de un barrio, solo 50 metros. En este nivel basta con saber leerla, sin cálculos complicados.</p>")}"""

    s3 = f"""<p>Mire el mapa. Los edificios no tienen nombre: use la <strong>leyenda</strong> para saber qué es cada uno.</p>
{mapa()}
{P("Compruebe", "¿Hacia dónde queda la escuela con respecto a la tienda?", ["al oeste", "al este", "al norte"], 0, {1: "La escuela está a la izquierda de la tienda.", 2: "Están en la misma fila."}, "<strong>Al oeste</strong>: está a la izquierda, en la misma fila.")}
{P("Compruebe", "¿Hacia dónde queda el hospital con respecto a mi casa?", ["al noreste", "al suroeste", "al norte"], 0, {1: "El hospital está arriba y a la derecha.", 2: "No está justo arriba: también está a la derecha."}, "<strong>Al noreste</strong>: arriba y a la derecha.")}
<div class="caja caja-tip"><span class="etiqueta et-verde">Actividad · en voz alta y en su cuaderno</span>
<p>Escriba cómo ir desde mi casa hasta el hospital, con los puntos cardinales y los nombres de las calles. Léalo en voz alta mientras sigue la ruta con el dedo.</p></div>
<details class="caja caja-tip"><summary><strong>Ya escribí mi ruta: ver un modelo</strong></summary>
<p>«Salgo de mi casa y camino hacia el norte por la Avenida Sol hasta la Calle Pino. Doblo hacia el este por la Calle Pino y paso al lado del parque, que queda al sur. Cruzo la Avenida Luna. El hospital queda al norte de la Calle Pino, en la esquina con la Avenida Luna.»</p>
<p>Hay otras rutas. Lo importante es usar los puntos cardinales para que otra persona pueda seguirla sin perderse.</p></details>"""

    secciones = [("s1", "¿Qué es un mapa?", s1), ("s2", "Los cuatro elementos", s2), ("s3", "Práctica: el barrio Las Flores", s3)]
    tarea = [("El mapa de mi barrio.", "Dibuje en su cuaderno un mapa sencillo de su cuadra o de su barrio, con su casa y tres lugares que conozca."),
             ("Los cuatro elementos.", "Póngale título, rosa de los vientos (con el norte arriba), una leyenda con un símbolo para cada lugar y una escala aproximada."),
             ("Mi ruta.", "Escriba cómo ir de su casa a uno de esos lugares con los puntos cardinales. Si alguien de su casa quiere participar, que siga la ruta sin ayuda.")]
    quiz = [
        ("¿Desde dónde se ve un lugar en un mapa?", ["Desde arriba", "Desde el costado", "Desde abajo"], 0, {1: "No.", 2: "No."}, "<strong>Desde arriba.</strong>"),
        ("¿Qué elemento explica los símbolos?", ["La leyenda", "La escala", "La rosa de los vientos"], 0, {1: "La escala es de distancias.", 2: "La rosa es de direcciones."}, "<strong>La leyenda.</strong>"),
        ("¿Qué elemento muestra el norte?", ["La rosa de los vientos", "El título", "La leyenda"], 0, {1: "No.", 2: "No."}, "<strong>La rosa de los vientos.</strong>"),
        ("Si el norte está arriba, ¿dónde está el este?", ["A la derecha", "A la izquierda", "Abajo"], 0, {1: "Ahí está el oeste.", 2: "Ahí está el sur."}, "<strong>A la derecha.</strong>"),
        ("¿Qué dirección está arriba a la izquierda?", ["noroeste", "noreste", "sureste"], 0, {1: "Noreste es arriba a la derecha.", 2: "Sureste es abajo a la derecha."}, "<strong>Noroeste.</strong>"),
        ("¿Para qué sirve la escala?", ["Para saber la distancia real", "Para saber el nombre del lugar", "Para saber los colores"], 0, {1: "Eso es el título.", 2: "Eso es la leyenda."}, "Para la <strong>distancia real</strong>."),
        ("Un mapa con montañas y ríos es…", ["físico", "político", "histórico"], 0, {1: "El político muestra fronteras.", 2: "El histórico muestra cambios en el tiempo."}, "<strong>Físico.</strong>"),
        ("En el mapa de Las Flores, ¿hacia dónde queda el parque con respecto a la biblioteca?", ["al sur", "al norte", "al este"], 0, {1: "El parque está abajo.", 2: "Están en la misma columna."}, "<strong>Al sur.</strong>"),
        ("¿Qué se lee primero en un mapa?", ["El título", "La escala"], 0, {}, "<strong>El título.</strong>"),
        ("¿Cómo se escriben los puntos cardinales dentro de una oración?", ["Con minúscula: norte, sur, este, oeste", "Siempre con mayúscula"], 0, {}, "Con <strong>minúscula</strong>. Solo en la rosa se usan N, S, E y O."),
    ]
    filas = [
        ("Elementos del mapa", "Encuentro el título, la rosa, la leyenda y la escala y sé para qué sirven.", "Confundo la leyenda con la escala.", "No los encuentro (<a href=\"#s2\">repase la sección 2</a>)."),
        ("Direcciones", "Digo hacia dónde queda un lugar, también noreste, noroeste, sureste y suroeste.", "Solo uso norte, sur, este y oeste.", "Me pierdo (<a href=\"#s2\">repase la sección 2</a>)."),
        ("Rutas", "Escribo una ruta que otra persona puede seguir.", "Mi ruta tiene huecos.", "No sé describirla (<a href=\"#s3\">repase la sección 3</a>)."),
    ]
    cierre = "<p>Ya sabe leer un mapa con sus cuatro elementos. En la próxima lección va a leer <strong>tablas</strong>: filas, columnas y el dato donde se cruzan.</p>"
    glosario = [("Mapa", "Imagen plana de un lugar visto desde arriba."), ("Rosa de los vientos", "Dibujo que muestra los puntos cardinales."),
                ("Leyenda (o clave)", "Cuadro que explica los símbolos del mapa."), ("Escala", "Relación entre el tamaño en el mapa y la distancia real."),
                ("Puntos cardinales", "Norte, sur, este y oeste.")]
    conexion = ("<p>En las Lecciones 6.1 y 6.2 aprendió a leer imágenes y las pistas de un artículo. Ahora va a conocer una herramienta visual fundamental para el examen de Estudios Sociales: el mapa.</p>"
                "<p><strong>Lo que necesita:</strong> el cuaderno y un lápiz.</p>")
    estd = LE.estandares(["R.7.4"], base=["R.2.1"])
    return C.pagina_leccion(N, LE.titulo(N), "Título, rosa de los vientos, leyenda y escala: las cuatro llaves del mapa.", ["R.7 · Información visual", "Mapas"],
                            ["<strong>Reconocer</strong> los tipos básicos de mapas.", "<strong>Usar</strong> el título, la rosa de los vientos, la leyenda y la escala.",
                             "<strong>Decir</strong> hacia dónde queda un lugar con respecto a otro.", "<strong>Describir</strong> una ruta con los puntos cardinales."],
                            estd, conexion, secciones, tarea, quiz, filas, cierre, ("6-4", LE.titulo("6-4")), glosario, P)


def practica():
    r = random.Random(63)
    nombres = list(LUGARES)
    dirs = []
    for a in nombres:
        for b in nombres:
            if a == b:
                continue
            ok = direccion(a, b)
            op = "al " + OPUESTO[ok[3:]]
            otras = [x for x in TODAS if x not in (ok, op)]
            ops = [ok, op] + r.sample(otras, 2)
            dirs.append({"enun": f"Mire el mapa. ¿Hacia dónde queda <strong>{a}</strong> con respecto a <strong>{b}</strong>?", "ops": [o[0].upper() + o[1:] for o in ops], "ok": 0,
                         "pista": f"Ponga el dedo en {b}. ¿{a[0].upper() + a[1:]} queda arriba o abajo? ¿A la derecha o a la izquierda?",
                         "exp": f"{a[0].upper() + a[1:]} queda <strong>{ok}</strong> de {b}."})
    ele = [{"enun": q, "ops": [ok] + d, "ok": 0, "pista": "Título: de qué lugar. Rosa: direcciones. Leyenda: símbolos. Escala: distancias.", "exp": f"<strong>{ok}</strong>."} for q, ok, d in ELEM + TIPOS]
    lee = [{"enun": q, "ops": [ok] + d, "ok": 0, "pista": "Mire el mapa con calma: la leyenda, las calles y la escala.", "exp": f"<strong>{ok}</strong>."} for q, ok, d in LEE]
    mods = [("direcciones", "¿Hacia dónde queda?", mapa("mp1") + C.om("m1", "Use la rosa de los vientos: el norte está arriba.")),
            ("leer", "Lea el mapa", mapa("mp2") + C.om("m2", "Use la leyenda, las calles y la escala.")),
            ("elementos", "Los elementos y los tipos de mapas", C.om("m3", "Elija el elemento o el tipo de mapa."))]
    js = C.js_datos("DIR", dirs) + C.js_datos("LEE", lee) + C.js_datos("ELE", ele) + 'creaBanco("m1", DIR);\ncreaBanco("m2", LEE);\ncreaBanco("m3", ELE);\n'
    return C.pagina_practica(N, LE.titulo(N), "Tres actividades · los ejercicios cambian cada vez · dos intentos en cada uno", mods, js)


if __name__ == "__main__":
    LE.construye(N, leccion, practica, horas="Unas 3 horas")
