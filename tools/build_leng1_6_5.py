# -*- coding: utf-8 -*-
"""LearnGED · Artes del lenguaje (español) · Nivel 1 · Lección 6.5 · El duelo de las gráficas: barras y pastel.
Fuente: clases_leng1/clase_6-5.html (GEDparaHispanos) y gramatica/n1-l6-5.html, adaptadas al marco de LearnGED.
Las gráficas de barras se dibujan con ciencia.grafica(); la de pastel, aquí. Las preguntas de la práctica se generan
a partir de los datos (todos pares, para que se lean en las líneas de la cuadrícula, de 2 en 2).
Uso: python3 tools/build_leng1_6_5.py
"""
import os, sys, math, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import leng_es as LE
from leng_es import C

LE.nivel(1)
N = "6-5"
COLORES = ["#0b679c", "#b42318", "#00695c", "#6d28d9", "#a15c00"]
FRUTA = [("Manzana", 10), ("Naranja", 8), ("Plátano", 4), ("Pera", 2)]
LIBROS = [("Carlos", 5), ("María", 8), ("José", 3), ("Sofía", 11), ("Diego", 7)]
# (título, eje X, eje Y, sustantivo plural, [(categoría, valor)])
DATOS = [("Vasos de agua que tomó Ana cada día", "Día", "Vasos de agua", "¿Cuántos vasos de agua tomó Ana el {c}?", "¿Cuántos vasos más tomó el {a} que el {b}?", "vasos",
          [("lunes", 6), ("martes", 8), ("miércoles", 4), ("jueves", 2), ("viernes", 6)]),
         ("Personas que visitaron la clínica", "Día", "Número de personas", "¿Cuántas personas visitaron la clínica el {c}?", "¿Cuántas personas más fueron el {a} que el {b}?", "personas",
          [("lunes", 12), ("martes", 8), ("miércoles", 6), ("jueves", 10), ("viernes", 14)]),
         ("Libros prestados por la biblioteca", "Mes", "Libros prestados", "¿Cuántos libros se prestaron en {c}?", "¿Cuántos libros más se prestaron en {a} que en {b}?", "libros",
          [("enero", 10), ("febrero", 14), ("marzo", 8), ("abril", 12)]),
         ("Votos para el nombre del parque", "Nombre propuesto", "Número de votos", "¿Cuántos votos recibió «{c}»?", "¿Cuántos votos más recibió «{a}» que «{b}»?", "votos",
          [("La Paz", 16), ("El Roble", 10), ("Las Flores", 6), ("Del Lago", 12)]),
         ("Horas que durmió cada persona el lunes", "Persona", "Horas de sueño", "¿Cuántas horas durmió {c}?", "¿Cuántas horas más durmió {a} que {b}?", "horas",
          [("Juan", 8), ("Lucía", 6), ("Pedro", 10), ("Ana", 8), ("Luis", 4)]),
         ("Estudiantes en cada clase de la noche", "Clase", "Estudiantes", "¿Cuántos estudiantes hay en la clase de {c}?", "¿Cuántos estudiantes más hay en {a} que en {b}?", "estudiantes",
          [("GED", 18), ("Inglés", 14), ("Computación", 10), ("Ciudadanía", 6)])]
# (situación, 0 barras / 1 pastel)
CUAL = [("Mostrar qué parte del presupuesto del mes se va en renta, comida, transporte y ahorro.", 1), ("Mostrar qué porcentaje de un grupo prefiere café, té o chocolate.", 1),
        ("Mostrar cómo se reparte su día: trabajo, sueño, familia y estudio.", 1), ("Comparar cuántos libros leyeron diez personas.", 0),
        ("Comparar la temperatura de cinco ciudades.", 0), ("Comparar cuántas personas visitaron la biblioteca cada mes del año.", 0),
        ("Comparar las ventas de doce productos de una tienda.", 0), ("Mostrar que la mitad del grupo llegó a pie, un cuarto en autobús y un cuarto en carro.", 1)]


def barras(titulo, xe, ye, datos, num=True, py=2):
    spec = {"tipo": "barras", "xEtq": xe, "yEtq": ye, "py": py, "barras": [{"etq": c, "valor": v, **({} if num else {"txt": ""})} for c, v in datos]}
    desc = f"Gráfica de barras: {titulo}. Eje horizontal: {xe}. Eje vertical: {ye}. " + "; ".join(f"{c}, {v}" for c, v in datos) + "."
    return f'<figure class="figura grafica"><figcaption class="graf-tit">{titulo}</figcaption>{C.grafica(spec, desc, ancho=520, alto=300)}</figure>'


def pastel(titulo, datos):
    tot = sum(v for _, v in datos); cx, cy, r = 130, 130, 110; a = -math.pi / 2; s = []
    for i, (c, v) in enumerate(datos):
        b = a + 2 * math.pi * v / tot
        x1, y1, x2, y2 = cx + r * math.cos(a), cy + r * math.sin(a), cx + r * math.cos(b), cy + r * math.sin(b)
        s.append(f'<path d="M{cx} {cy} L{x1:.1f} {y1:.1f} A{r} {r} 0 {1 if v / tot > .5 else 0} 1 {x2:.1f} {y2:.1f} Z" fill="{COLORES[i]}" stroke="#fff" stroke-width="2"/>')
        s.append(f'<rect x="270" y="{50 + i * 34}" width="20" height="20" fill="{COLORES[i]}"/><text x="298" y="{66 + i * 34}" font-size="16">{c}</text>')
        a = b
    desc = f"Gráfica de pastel: {titulo}. " + "; ".join(f"{c}, {v} de {tot}" for c, v in datos) + ". Las porciones no tienen números."
    return (f'<figure class="figura grafica"><figcaption class="graf-tit">{titulo}</figcaption><svg viewBox="0 0 420 260" role="img" aria-label="{desc}" style="width:100%;max-width:420px;display:block;margin:0 auto">'
            + "".join(s) + "</svg></figure>")


def leccion():
    P = C.Practicas()
    s1 = f"""<p>Una <strong>gráfica</strong> es una imagen que muestra números con barras, círculos o líneas. Sirve para comparar cantidades de un vistazo, sin leer todos los números uno por uno. Es protagonista en los exámenes de Ciencias y de Estudios Sociales.</p>
<p>Se preguntó a 24 personas cuál es su fruta favorita. Se puede escribir así: «Diez personas prefieren la manzana, ocho la naranja, cuatro el plátano y dos la pera». O se puede mostrar así:</p>
{barras("Fruta favorita del grupo", "Fruta", "Número de personas", FRUTA)}
{C.caja("tip", "Idea central", "<p>La gráfica no cambia los datos: los vuelve una imagen para que se comparen fácilmente.</p>")}"""

    s2 = f"""<h3>Los mismos datos, dos gráficas</h3>
{pastel("Fruta favorita del grupo", FRUTA)}
<p>Con el pastel, para saber si la manzana gana a la naranja hay que comparar <strong>ángulos</strong>, y a la vista le cuesta comparar ángulos parecidos. Con las barras, basta comparar <strong>alturas</strong>, que es mucho más fácil.</p>
{C.tabla("¿Cuándo usar cada una?", ["Gráfica", "Sirve para", "Funciona mejor"],
         [["🥧 De pastel (circular)", "Mostrar las <strong>partes de un todo</strong> (el 100 %).", "Con pocas partes y bien distintas."],
          ["📊 De barras", "<strong>Comparar cantidades</strong> entre categorías.", "Aunque haya muchas categorías; permite leer los valores con precisión."]])}
<h3>Las partes de una gráfica de barras</h3>
{C.tabla("Las cuatro partes", ["Parte", "Qué hace"],
         [["1 · Título", "Arriba. Dice qué información muestra."], ["2 · Barras", "Cada una es una categoría. Su altura es el valor."],
          ["3 · Eje Y (vertical)", "La cantidad que se mide. Los números suben hacia arriba."], ["4 · Eje X (horizontal)", "Las categorías que se comparan: personas, días, productos…"]])}
{C.caja("tip", "Tres pasos para leer una gráfica", "<p><strong>1.</strong> Lea el título. <strong>2.</strong> Lea los ejes: ¿qué se mide (Y)? ¿qué se compara (X)? <strong>3.</strong> Compare las barras: ¿cuál es más alta? ¿cuál más baja? Fíjese también en la <strong>fuente</strong>: quién recogió los datos y cuándo.</p>")}
{C.caja("ojo", "En el examen GED", "<p>Pueden aparecer los dos tipos y también otros, como las gráficas de líneas. Lo que aprende con las barras le sirve para leer las demás.</p>")}"""

    s3 = f"""{barras("Libros leídos en marzo", "Persona", "Número de libros", LIBROS, num=False, py=1)}
<p class="nota-fina">Datos de ejemplo.</p>
{P("Pregunta 1", "¿Quién leyó más libros?", ["Sofía", "María", "Diego"], 0, {1: "María leyó 8; hay una barra más alta.", 2: "Diego leyó 7; hay una barra más alta."}, "<strong>Sofía</strong>: su barra es la más alta (11).")}
{P("Pregunta 2", "¿Quién leyó menos libros?", ["José", "Carlos", "Diego"], 0, {1: "Carlos leyó 5; hay una barra más baja.", 2: "Diego leyó 7."}, "<strong>José</strong>: su barra es la más baja (3).")}
{P("Pregunta 3", "¿Cuántos libros leyó María?", ["8", "7", "11"], 0, {1: "Siga la punta de la barra de María hasta el eje Y.", 2: "Esa es la barra de Sofía."}, "<strong>8</strong>: la barra llega a la línea del 8.")}
{P("Pregunta 4", "¿Qué se mide en el eje Y?", ["El número de libros", "Las personas", "Los meses"], 0, {1: "Las personas están en el eje X.", 2: "La gráfica es de un solo mes."}, "El <strong>número de libros</strong>.")}
<h3>Palabras para describir una gráfica</h3>
{C.tabla("Palabras de comparación", ["Palabra", "Ejemplo"],
         [["más que · menos que", "Sofía leyó más libros que María."], ["el más alto · el más bajo", "La barra de José es la más baja."],
          ["el doble · la mitad", "El plátano tiene el doble de votos que la pera (4 y 2)."], ["igual que", "Juan durmió lo mismo que Ana: 8 horas cada uno."]])}"""

    secciones = [("s1", "¿Para qué sirven las gráficas?", s1), ("s2", "Barras y pastel: el duelo", s2), ("s3", "Práctica: leer una gráfica de barras", s3)]
    tarea = [("Mi encuesta.", "Pregunte a seis u ocho personas de su casa o de su trabajo algo sencillo: su comida favorita, cómo llegan al trabajo, cuántas horas duermen."),
             ("Mi gráfica.", "Haga en su cuaderno una gráfica de barras con título, eje X, eje Y y una barra por respuesta."),
             ("Tres oraciones.", "Escriba tres oraciones sobre su gráfica con palabras de comparación: <em>más que, menos que, el más alto, igual que</em>.")]
    quiz = [
        ("¿Para qué sirve una gráfica?", ["Para comparar cantidades de un vistazo", "Para adornar", "Para esconder datos"], 0, {1: "No es un adorno.", 2: "No."}, "Para <strong>comparar</strong> de un vistazo."),
        ("¿Para qué sirve mejor la gráfica de pastel?", ["Para mostrar partes de un todo", "Para comparar doce productos"], 0, {}, "Para <strong>partes de un todo</strong>."),
        ("¿Por qué las barras son más fáciles de comparar?", ["Porque se comparan alturas", "Porque tienen más colores"], 0, {}, "Porque se comparan <strong>alturas</strong>, no ángulos."),
        ("¿Qué muestra el eje Y?", ["La cantidad que se mide", "Las categorías", "El título"], 0, {1: "Esas están en el eje X.", 2: "El título va arriba."}, "La <strong>cantidad</strong>."),
        ("¿Qué muestra el eje X?", ["Las categorías que se comparan", "La cantidad", "La fuente"], 0, {1: "Esa está en el eje Y.", 2: "No."}, "Las <strong>categorías</strong>."),
        ("¿Qué se lee primero en una gráfica?", ["El título", "La barra más alta"], 0, {}, "El <strong>título</strong>."),
        ("En la gráfica de libros, ¿cuántos libros leyó Carlos?", ["5", "8", "3"], 0, {1: "Esa es María.", 2: "Ese es José."}, "<strong>5</strong>."),
        ("Para comparar la temperatura de cinco ciudades, ¿qué gráfica conviene?", ["De barras", "De pastel"], 0, {}, "<strong>De barras</strong>: se comparan cantidades, no partes de un todo."),
        ("¿Por qué importa la fuente de una gráfica?", ["Dice quién recogió los datos y cuándo", "Dice el color de las barras"], 0, {}, "Dice <strong>quién</strong> y <strong>cuándo</strong>: sirve para decidir cuánto confiar."),
        ("En la fruta favorita, ¿cuántas personas más prefieren la manzana que la pera?", ["8", "10", "2"], 0, {1: "10 son las de la manzana; hay que restar las de la pera.", 2: "2 son las de la pera."}, "<strong>8</strong>: 10 − 2."),
    ]
    filas = [
        ("Partes de la gráfica", "Reconozco el título, los ejes y las barras.", "Confundo el eje X con el Y.", "No las distingo (<a href=\"#s2\">repase la sección 2</a>)."),
        ("Leer valores", "Leo el valor de una barra en el eje Y y comparo dos barras.", "Leo la más alta y la más baja, pero no los valores.", "No sé leerla (<a href=\"#s3\">repase la sección 3</a>)."),
        ("Elegir la gráfica", "Sé cuándo conviene barras y cuándo pastel.", "A veces dudo.", "No sé la diferencia (<a href=\"#s2\">repase la sección 2</a>)."),
    ]
    cierre = "<p>Ya sabe leer gráficas de barras y de pastel. En la última lección del tema va a trabajar el <strong>vocabulario propio</strong> de Ciencias y de Estudios Sociales.</p>"
    glosario = [("Gráfica", "Imagen que muestra números con barras, círculos o líneas."), ("Gráfica de barras", "Compara cantidades con la altura de las barras."),
                ("Gráfica de pastel (circular)", "Muestra las partes de un todo."), ("Eje Y", "Línea vertical: la cantidad que se mide."), ("Eje X", "Línea horizontal: las categorías.")]
    conexion = ("<p>Ya sabe leer imágenes, mapas y tablas. Ahora va a estudiar la gráfica, que muestra números en forma de imagen. Se concentrará en las dos más comunes: la de barras y la de pastel.</p>"
                "<p><strong>Lo que necesita:</strong> el cuaderno, una regla y lápices de colores (si tiene).</p>")
    estd = LE.estandares(["R.7.2", "R.7.4"])
    return C.pagina_leccion(N, LE.titulo(N), "Alturas contra ángulos: cuál gráfica se lee mejor.", ["R.7 · Información visual", "Gráficas"],
                            ["<strong>Reconocer</strong> las partes de una gráfica de barras.", "<strong>Leer</strong> valores y comparar barras.",
                             "<strong>Decidir</strong> cuándo conviene una gráfica de barras y cuándo una de pastel.", "<strong>Describir</strong> una gráfica con palabras de comparación."],
                            estd, conexion, secciones, tarea, quiz, filas, cierre, ("6-6", LE.titulo("6-6")), glosario, P)


def practica():
    r = random.Random(65)
    lee = []
    for tit, xe, ye, q1, q2, sus, dat in DATOS:
        g = barras(tit, xe, ye, [(x[0].upper() + x[1:], v) for x, v in dat], num=False)
        M = lambda x: x[0].upper() + x[1:]
        vals = [v for _, v in dat]
        alto = max(dat, key=lambda x: x[1]); bajo = min(dat, key=lambda x: x[1])
        otros = [c for c, v in dat if v not in (alto[1], bajo[1])]
        lee.append({"enun": f"{g}¿Qué barra es la más alta?", "ops": [M(alto[0]), M(bajo[0])] + [M(o) for o in otros[:1]], "ok": 0, "pista": "Busque la barra que llega más arriba.", "exp": f"<strong>{M(alto[0])}</strong>, con {alto[1]} {sus}."})
        lee.append({"enun": f"{g}¿Qué barra es la más baja?", "ops": [M(bajo[0]), M(alto[0])] + [M(o) for o in otros[:1]], "ok": 0, "pista": "Busque la barra que llega menos arriba.", "exp": f"<strong>{M(bajo[0])}</strong>, con {bajo[1]} {sus}."})
        c, v = r.choice(dat)
        dis = sorted({v + 2, v - 2 if v > 2 else v + 4} - {v})
        lee.append({"enun": g + q1.format(c=f"<strong>{c}</strong>"),
                    "ops": [str(v)] + [str(x) for x in dis], "ok": 0, "pista": f"Siga la punta de la barra de {M(c)} hasta el eje Y. Las líneas van de 2 en 2.", "exp": f"<strong>{v}</strong>: la barra llega a la línea del {v}."})
        a, b = alto, bajo
        d = a[1] - b[1]
        lee.append({"enun": g + q2.format(a=f"<strong>{a[0]}</strong>", b=f"<strong>{b[0]}</strong>"),
                    "ops": [str(d), str(a[1]), str(d + 2)], "ok": 0, "pista": "Lea las dos barras y reste: la mayor menos la menor.", "exp": f"<strong>{d}</strong>: {a[1]} − {b[1]}."})
        lee.append({"enun": f"{g}¿Qué se mide en el eje Y (el vertical)?", "ops": [ye, xe], "ok": 0, "pista": "", "exp": f"El eje Y mide <strong>{ye.lower()}</strong>; en el eje X están las categorías ({xe.lower()})."})
    cual = [{"enun": f"<strong>{s}</strong><br>¿Qué gráfica conviene usar?", "ops": ["De barras", "De pastel"], "ok": k, "enOrden": True, "pista": "",
             "exp": ["<strong>De barras</strong>: se comparan cantidades entre categorías.", "<strong>De pastel</strong>: se muestran las partes de un todo."][k]} for s, k in CUAL]
    mods = [("leer", "Lea la gráfica de barras", C.om("m1", "Lea el título, los ejes y compare las barras. Los datos son de ejemplo.")),
            ("elegir", "¿Barras o pastel?", C.om("m2", "Decida qué gráfica conviene para cada situación."))]
    js = C.js_datos("LEE", lee) + C.js_datos("CUAL", cual) + 'creaBanco("m1", LEE);\ncreaBanco("m2", CUAL);\n'
    return C.pagina_practica(N, LE.titulo(N), "Dos actividades · los ejercicios cambian cada vez · dos intentos en cada uno", mods, js)


if __name__ == "__main__":
    LE.construye(N, leccion, practica, horas="Unas 3 horas")
