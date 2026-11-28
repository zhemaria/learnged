# -*- coding: utf-8 -*-
"""LearnGED · Artes del lenguaje (español) · Nivel 2 · Lección 6.1 · Gráficas de barras, líneas y circulares; tablas de datos.
Fuente: clases_leng2/clase_6-1.html (GEDparaHispanos) y gramatica/n2-l6-1.html, adaptadas al marco de LearnGED.
Dato real: temperatura promedio de cada mes en Chicago (O'Hare), normales 1991–2020 del Servicio Nacional de Meteorología (NOAA),
redondeadas: 25, 29, 39, 50, 61, 71, 75, 74, 66, 54, 41, 31 °F. Consultado el 28 de noviembre de 2026.
Uso: python3 tools/build_leng2_6_1.py
"""
import os, sys, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import leng_es as LE
from leng_es import C
import graficas_n2 as G

LE.nivel(2)
N = "6-1"
DIAS = ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb"]
VIS = [120, 95, 110, 140, 80, 160]
MESES = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]
TEMP = [25, 29, 39, 50, 61, 71, 75, 74, 66, 54, 41, 31]
FUENTE_T = ('<p class="fuente">Fuente: Servicio Nacional de Meteorología (NOAA), oficina de Chicago, normales climáticas 1991–2020, estación del aeropuerto O\'Hare. '
            'Promedios mensuales redondeados al grado. Consultado el 28 de noviembre de 2026.</p>')
CATS, PC = ["Vivienda", "Comida", "Transporte", "Otros"], [40, 25, 15, 20]


def leccion():
    P = C.Practicas()
    s1 = f"""<p>Las gráficas están en todas partes: en la factura de la luz, en las noticias, en el folleto del médico y, sobre todo, en el GED. En los exámenes de Ciencias y de Estudios Sociales, muchas preguntas traen una gráfica, una tabla o un mapa. La buena noticia es que todas se leen con el mismo método. En esta lección no hará cálculos difíciles: aprenderá a leer lo que la gráfica dice y, tan importante como eso, lo que <strong>no</strong> dice.</p>
<ol><li><strong>El título:</strong> ¿de qué trata? ¿De qué lugar y de qué tiempo son los datos?</li>
<li><strong>Los ejes o las categorías:</strong> ¿qué se mide? ¿Qué representa cada barra, línea o porción?</li>
<li><strong>La escala y las unidades:</strong> ¿de cuánto en cuánto van los números? ¿Son dólares, personas, grados, porcentajes?</li>
<li><strong>Los valores:</strong> lea los datos que necesita. Siga la línea desde la marca hasta el eje.</li>
<li><strong>La tendencia o la conclusión:</strong> ¿qué es lo más grande, lo más pequeño, qué sube, qué baja?</li></ol>
{C.caja("tip", "Lea la pregunta primero", "<p>En un examen, lea antes la pregunta para saber qué dato busca. Después aplique los cinco pasos. Así no se pierde entre tantos números.</p>")}
<h3>Gráficas de barras: comparar</h3>
<p>La gráfica de barras sirve para <strong>comparar cantidades</strong> entre categorías. Cuanto más alta la barra, mayor la cantidad.</p>
{G.barras("Visitas a la biblioteca del barrio en una semana", "Día de la semana", "Número de visitas", DIAS, VIS, py=30)}
<p class="fuente">Datos de ejemplo para la lección.</p>
{P("Barras 1", "¿Qué mide el eje vertical?", ["El número de visitas", "Los días de la semana", "Los libros prestados"], 0, {1: "Ese es el eje horizontal.", 2: "La gráfica no habla de libros."}, "El rótulo del eje lo dice: número de visitas.")}
{P("Barras 2", "¿Qué día tuvo menos visitas?", ["Viernes", "Martes", "Miércoles"], 0, {1: "Tuvo 95.", 2: "Tuvo 110."}, "La barra más baja: 80.")}
{P("Barras 3", "¿Cuántas visitas más hubo el jueves que el martes?", ["35", "45", "55"], 1, {0: "Reste otra vez: 140 − 95.", 2: "Reste otra vez: 140 − 95."}, "140 − 95 = 45.")}"""

    s2 = f"""<p>La gráfica de líneas muestra cómo <strong>cambia algo con el tiempo</strong>. El tiempo va en el eje horizontal. Si la línea sube, la cantidad aumenta; si baja, disminuye; si queda plana, no cambia. Esa dirección se llama <strong>tendencia</strong>.</p>
{G.lineas("Temperatura promedio de cada mes en Chicago (°F)", "Grados Fahrenheit", MESES, TEMP, 90, 15, " °F")}
{FUENTE_T}
{P("Líneas 1", "¿Cuál es el mes más caluroso?", ["Agosto", "Junio", "Julio"], 2, {0: "Agosto tiene 74.", 1: "Junio tiene 71."}, "El punto más alto: 75 °F, en julio.")}
{P("Líneas 2", "¿Cuál es la tendencia de julio a diciembre?", ["Sube", "Baja", "No cambia"], 1, {0: "Siga la línea hacia la derecha.", 2: "La línea no queda plana."}, "La línea <strong>baja</strong>: hace cada vez más frío.")}
{P("Líneas 3", "¿Cuántos grados sube la temperatura promedio de enero a julio?", ["50 grados", "25 grados", "75 grados"], 0, {1: "Ese es el valor de enero.", 2: "Ese es el valor de julio."}, "75 − 25 = 50.")}
<h3>Gráficas circulares: las partes de un todo</h3>
<p>La gráfica circular (también llamada «de pastel») muestra cómo se reparte un total. El círculo completo es el <strong>100 %</strong>, y cada porción es una parte. Las porciones siempre suman 100 %.</p>
{G.circular("Gastos mensuales de la familia Ramírez", CATS, PC)}
<p class="fuente">Datos de ejemplo para la lección.</p>
{C.caja("tip", "Porcentajes que ayudan", "<p>El 50 % es la mitad; el 25 %, un cuarto; el 10 %, una décima parte. Si una porción ocupa casi la mitad del círculo, está cerca del 50 %.</p>")}
{P("Circular 1", "Comida y transporte juntos suman…", ["lo mismo que vivienda", "más que vivienda", "menos que «Otros»"], 0, {1: "25 + 15 = 40.", 2: "25 + 15 = 40, y Otros es 20."}, "25 % + 15 % = 40 %, igual que vivienda.")}
{P("Circular 2", "¿Aproximadamente qué parte del dinero va a comida?", ["Un cuarto", "La mitad", "Casi todo"], 0, {1: "La mitad sería 50 %.", 2: "Es solo el 25 %."}, "25 % es <strong>un cuarto</strong>.")}"""

    s3 = f"""<p>Una tabla organiza los datos en <strong>filas</strong> (horizontales) y <strong>columnas</strong> (verticales). Para encontrar un dato, busque la fila y la columna correctas y mire dónde se cruzan.</p>
<p class="graf-tit">Tres planes de teléfono celular (precios de ejemplo)</p>
{C.tabla("Tres planes de teléfono celular (precios de ejemplo)", ["Plan", "Precio al mes", "Datos de internet", "Llamadas internacionales"],
         [["A", "$25", "5 GB", "No incluye"], ["B", "$35", "15 GB", "México y Canadá"], ["C", "$50", "Ilimitados", "20 países"]])}
{P("Tabla 1", "¿Qué plan tiene datos ilimitados?", ["A", "B", "C"], 2, {0: "Tiene 5 GB.", 1: "Tiene 15 GB."}, "Fila C, columna «Datos de internet».")}
{P("Tabla 2", "Quiere llamar a México gastando lo menos posible. ¿Qué plan elige?", ["A", "B", "C"], 1, {0: "El A no incluye llamadas internacionales.", 2: "El C también sirve, pero cuesta más."}, "El A no incluye llamadas; el B sí, y cuesta menos que el C.")}
<h3>¿Qué se puede concluir?</h3>
<p>Las preguntas más difíciles no piden un número, sino una conclusión: «¿Qué afirmación apoya la gráfica?». Una conclusión es válida solo si los datos la demuestran. Hay tres trampas frecuentes:</p>
{C.tabla("Trampas en las conclusiones sobre gráficas", ["Trampa", "Ejemplo con la gráfica de la biblioteca"],
         [["Habla de algo que la gráfica no mide", "«La gente lee más los sábados.» La gráfica cuenta visitas, no libros leídos."],
          ["Inventa una causa", "«Hay más visitas el sábado porque la gente no trabaja.» Puede ser cierto, pero la gráfica no lo dice."],
          ["Es una opinión", "«La biblioteca debería cerrar los viernes.» Es una recomendación, no un dato."]])}
{C.caja("tip", "La prueba", "<p>Pregúntese: «¿puedo señalar en la gráfica el dato que lo demuestra?». Si puede, la conclusión es válida. Si tiene que suponer algo, no lo es.</p>")}
<p>Todas estas se refieren a la gráfica de la biblioteca:</p>
{P("¿Válida? 1", "«El sábado hubo el doble de visitas que el viernes.»", ["Válida", "No válida"], 0, {1: "Compare: 160 y 80."}, "160 es el doble de 80.")}
{P("¿Válida? 2", "«La gente lee más libros los sábados.»", ["Válida", "No válida"], 1, {0: "¿La gráfica cuenta libros?"}, "La gráfica cuenta visitas, no libros leídos.")}
{P("¿Válida? 3", "«Los viernes viene poca gente porque llueve.»", ["Válida", "No válida"], 1, {0: "¿La gráfica habla del clima?"}, "Inventa una causa: la gráfica no habla del clima.")}
{P("¿Válida? 4", "«La biblioteca debería cerrar los viernes.»", ["Válida", "No válida"], 1, {0: "¿Es un dato o una recomendación?"}, "Es una opinión, no un dato.")}
<p>Si tiene con quién practicar, busquen juntos una gráfica en una noticia o un folleto. Cada uno escribe una conclusión válida y otra que no lo sea; luego el otro adivina cuál es cuál.</p>"""

    secciones = [("s1", "Leer una gráfica y las gráficas de barras", s1), ("s2", "Gráficas de líneas y circulares", s2), ("s3", "Tablas y conclusiones", s3)]
    tarea = [("Una gráfica real.", "Busque una gráfica en un periódico, una factura o un sitio de noticias. Aplique los cinco pasos por escrito y escriba dos conclusiones válidas."),
             ("Mi gráfica.", "Anote durante una semana cuántas horas estudia cada día. Dibuje una gráfica de barras con título, ejes y escala, y escriba una oración con la conclusión."),
             ("Mi presupuesto.", "Dibuje una gráfica circular aproximada de cómo se reparte el dinero en su casa. No hace falta poner cantidades reales; pueden ser porcentajes estimados.")]
    TB = C.tabla("Ventas de una panadería", ["Producto", "Lunes", "Martes"], [["Pan dulce", "40", "55"], ["Bolillos", "90", "70"]])
    quiz = [
        ("¿Qué gráfica conviene para mostrar cómo cambió el precio de la gasolina durante un año?", ["De líneas", "Circular", "Ninguna: hace falta un mapa"], 0, {1: "La circular muestra partes de un todo.", 2: "No hace falta un mapa."}, "<strong>De líneas</strong>: cambio en el tiempo."),
        ("¿Qué gráfica conviene para mostrar cómo se reparte un presupuesto?", ["Circular", "De líneas", "De temperaturas"], 0, {1: "No hay cambio en el tiempo.", 2: "No existe ese tipo."}, "<strong>Circular</strong>: partes de un todo."),
        ("En una gráfica de barras, la barra más alta indica…", ["la cantidad mayor", "la cantidad menor", "la primera categoría"], 0, {1: "Es al revés.", 2: "El orden no importa."}, "La cantidad <strong>mayor</strong>."),
        ("Si la línea de una gráfica baja de izquierda a derecha, la cantidad…", ["disminuye con el tiempo", "aumenta con el tiempo", "se mantiene igual"], 0, {1: "Sería si sube.", 2: "Sería si queda plana."}, "<strong>Disminuye.</strong>"),
        ("Las porciones de una gráfica circular suman siempre…", ["100 %", "50 %", "lo que diga el título"], 0, {1: "Eso es la mitad.", 2: "Siempre es el total."}, "<strong>100 %.</strong>"),
        ("Una porción del 25 % es…", ["un cuarto del total", "la mitad del total", "casi todo el total"], 0, {1: "La mitad es 50 %.", 2: "Casi todo sería cerca del 100 %."}, "<strong>Un cuarto.</strong>"),
        (TB + "¿Cuántos panes dulces se vendieron el martes?", ["55", "40", "70"], 0, {1: "Eso fue el lunes.", 2: "Esos son bolillos."}, "Fila Pan dulce, columna Martes: <strong>55</strong>."),
        (TB + "¿Qué producto se vendió más el lunes?", ["Bolillos", "Pan dulce", "Los dos por igual"], 0, {1: "40 es menos que 90.", 2: "40 y 90 no son iguales."}, "<strong>Bolillos</strong>: 90."),
        (TB + "¿Qué conclusión apoya la tabla?", ["El martes se vendió más pan dulce que el lunes.", "El pan dulce es más sabroso que los bolillos.", "El martes llovió y por eso bajaron los bolillos."], 0,
         {1: "Es una opinión.", 2: "Inventa una causa."}, "55 es más que 40."),
        ("¿Cómo comprueba que una conclusión es válida?", ["Señala el dato de la gráfica que la demuestra", "Mira si suena lógica cuando la lee en voz alta", "Mira si coincide con lo que usted opina del tema"], 0,
         {1: "Sonar lógica no basta.", 2: "Su opinión no es un dato."}, "Señalar el <strong>dato</strong>."),
    ]
    filas = [
        ("Leer gráficas", "Sigo los cinco pasos con barras, líneas y círculos.", "Leo los valores, pero olvido el título o las unidades.", "Me pierdo entre los números (<a href=\"#s1\">repase la sección 1</a>)."),
        ("Tendencias y partes", "Digo si una línea sube o baja y calculo partes de un círculo.", "Dudo con los porcentajes.", "No sé leer líneas ni círculos (<a href=\"#s2\">repase la sección 2</a>)."),
        ("Tablas y conclusiones", "Encuentro datos en una tabla y distingo conclusiones válidas.", "A veces acepto una causa inventada.", "No distingo dato y opinión (<a href=\"#s3\">repase la sección 3</a>)."),
    ]
    cierre = "<p>Ya lee gráficas y tablas con método. En la próxima lección distinguirá entre <strong>fuentes primarias y secundarias</strong>.</p>"
    glosario = [("Eje", "Cada una de las líneas de referencia de una gráfica: horizontal y vertical."), ("Escala", "De cuánto en cuánto van los números de un eje."),
                ("Tendencia", "La dirección general de una línea: sube, baja o se mantiene."), ("Conclusión válida", "Afirmación que se puede demostrar con los datos.")]
    conexion = ("<p>En el Nivel 1 leyó gráficas de barras y de pastel con pocos datos. Ahora sumará las gráficas de líneas y las tablas, y aprenderá a decidir si una conclusión está apoyada por los datos.</p>"
                "<p><strong>Lo que necesita:</strong> el cuaderno y una regla.</p>")
    estd = LE.estandares(["R.9.1/R.7.1"], base=["R.2.7", "R.8.4"])
    return C.pagina_leccion(N, LE.titulo(N), "Lo que la gráfica dice y lo que no dice.", ["Lectura", "Gráficas y tablas"],
                            ["<strong>Leer</strong> una gráfica con cinco pasos.", "<strong>Comparar</strong> con barras y ver cambios con líneas.",
                             "<strong>Interpretar</strong> gráficas circulares y tablas.", "<strong>Decidir</strong> si una conclusión está apoyada por los datos."],
                            estd, conexion, secciones, tarea, quiz, filas, cierre, ("6-2", LE.titulo("6-2")), glosario, P)


def num_ops(v, d):
    o, k = [v], 1
    while len(o) < 3:
        c = v + (1 if k % 2 else -1) * d * ((k + 1) // 2)
        if c >= 0 and c not in o: o.append(c)
        k += 1
    return [f"{x:g}" for x in o]


def otras(r, et, ok):
    x = [e for e in et if e != ok]; r.shuffle(x); return [ok] + x[:2]


def practica():
    r = random.Random(61)
    def distintos(n, a, b, paso):
        s = set()
        while len(s) < n: s.add(r.randint(int(a / paso), int(b / paso)) * paso)
        l = list(s); r.shuffle(l); return l
    ba = []
    CB = [("Estudiantes inscritos en cada curso del centro comunitario", "Curso", "Estudiantes", ["Inglés", "GED", "Computación", "Ciudadanía"], 10, 60, 5),
          ("Litros de leche vendidos cada día en la tienda", "Día", "Litros", ["Lun", "Mar", "Mié", "Jue", "Vie"], 20, 90, 5),
          ("Goles de cada equipo en la liga del barrio", "Equipo", "Goles", ["Águilas", "Leones", "Halcones", "Tigres", "Pumas"], 5, 30, 1),
          ("Horas de voluntariado de los vecinos cada mes", "Mes", "Horas", ["Ene", "Feb", "Mar", "Abr", "May", "Jun"], 10, 50, 2),
          ("Libros prestados por la biblioteca escolar", "Grado", "Libros", ["1.º", "2.º", "3.º", "4.º", "5.º"], 15, 75, 5)]
    for k in range(25):
        t, ex, ey, et, a, b, p = CB[k % len(CB)]
        v = distintos(len(et), a, b, p); mx, mn = max(v), min(v); tipo = k % 4
        if tipo == 0: q, ops, n = "¿Qué categoría tiene el valor más alto?", otras(r, et, et[v.index(mx)]), f"{et[v.index(mx)]}: {mx}, la barra más alta."
        elif tipo == 1: q, ops, n = "¿Qué categoría tiene el valor más bajo?", otras(r, et, et[v.index(mn)]), f"{et[v.index(mn)]}: {mn}, la barra más baja."
        elif tipo == 2:
            i = r.randrange(len(et)); q, ops, n = f"¿Cuál es el valor de «{et[i]}»?", num_ops(v[i], p * 2), f"Lea el número sobre la barra de {et[i]}: {v[i]}."
        else: q, ops, n = "¿Cuál es la diferencia entre el valor más alto y el más bajo?", num_ops(mx - mn, p * 2), f"{mx} − {mn} = {mx - mn}."
        ba.append({"enun": G.barras(t, ex, ey, et, v) + f"<p><strong>{q}</strong></p>", "ops": ops, "ok": 0, "pista": "Vuelva a la gráfica: lea el título, el eje y el número sobre cada barra.", "exp": n})
    li = []
    CL = [("Precio de una docena de huevos en la tienda (dólares)", "Dólares", ["Ene", "Feb", "Mar", "Abr", "May", "Jun"], 2, 6, .5, 8, 2),
          ("Visitantes del parque cada mes (en cientos)", "Cientos de personas", ["Mar", "Abr", "May", "Jun", "Jul", "Ago"], 2, 12, 1, 15, 3),
          ("Estudiantes que asisten a la clase de la noche", "Estudiantes", ["Sem 1", "Sem 2", "Sem 3", "Sem 4", "Sem 5", "Sem 6"], 8, 24, 1, 30, 6),
          ("Lluvia de cada mes (pulgadas)", "Pulgadas", ["Ene", "Feb", "Mar", "Abr", "May", "Jun"], 1, 5, .5, 6, 1)]
    for k in range(24):
        t, ey, et, a, b, p, tope, paso = CL[k % len(CL)]
        v = distintos(len(et), a, b, p); mx, mn = max(v), min(v); tipo = k % 4
        if tipo == 0: q, ops, n = "¿En qué momento se alcanza el valor más alto?", otras(r, et, et[v.index(mx)]), f"El punto más alto está en {et[v.index(mx)]}: {mx:g}."
        elif tipo == 1: q, ops, n = "¿En qué momento se alcanza el valor más bajo?", otras(r, et, et[v.index(mn)]), f"El punto más bajo está en {et[v.index(mn)]}: {mn:g}."
        elif tipo == 2:
            i = r.randrange(len(et) - 1); sube = v[i + 1] > v[i]
            q, ops, n = f"Entre {et[i]} y {et[i + 1]}, ¿qué hace la línea?", ["Sube" if sube else "Baja", "Baja" if sube else "Sube", "Se queda igual"], f"Pasa de {v[i]:g} a {v[i + 1]:g}: {'sube' if sube else 'baja'}."
        else:
            j = r.randrange(len(et)); q, ops, n = f"¿Cuál es el valor en {et[j]}?", num_ops(v[j], p), f"Lea el número junto al punto de {et[j]}: {v[j]:g}."
        li.append({"enun": G.lineas(t, ey, et, v, tope, paso) + f"<p><strong>{q}</strong></p>", "ops": ops, "ok": 0, "pista": "Siga la línea de izquierda a derecha y lea los números junto a cada punto.", "exp": n})
    ci = []
    CC = [("Cómo viajan los estudiantes a la escuela", ["Autobús", "Carro", "A pie", "Bicicleta"]), ("En qué gasta Ana su sueldo", ["Renta", "Comida", "Transporte", "Ahorro"]),
          ("Deporte favorito de la clase", ["Fútbol", "Béisbol", "Básquetbol", "Natación"]), ("Cómo usa Luis su día", ["Trabajo", "Sueño", "Estudio", "Familia"])]
    for k in range(24):
        t, et = CC[k % len(CC)]
        while True:
            a, b, c = r.randint(5, 9) * 5, r.randint(3, 6) * 5, r.randint(2, 4) * 5; d = 100 - a - b - c
            if d >= 5 and len({a, b, c, d}) == 4: break
        v = [a, b, c, d]; r.shuffle(v); mx, mn = max(v), min(v); tipo = k % 3
        if tipo == 0: q, ops, n = "¿Qué porción es la más grande?", otras(r, et, et[v.index(mx)]), f"{et[v.index(mx)]}: {mx} %."
        elif tipo == 1: q, ops, n = "¿Qué porción es la más pequeña?", otras(r, et, et[v.index(mn)]), f"{et[v.index(mn)]}: {mn} %."
        else:
            i = r.randrange(4); j = (i + 1 + r.randrange(3)) % 4; s = v[i] + v[j]
            q, ops, n = f"¿Cuánto suman «{et[i]}» y «{et[j]}»?", [f"{s} %", f"{s + 10} %", f"{s - 5 if s > 5 else s + 5} %"], f"{v[i]} % + {v[j]} % = {s} %."
        ci.append({"enun": G.circular(t, et, v) + f"<p><strong>{q}</strong></p>", "ops": ops, "ok": 0, "pista": "Mire los porcentajes escritos en cada porción y en la leyenda.", "exp": n})
    ta = []
    CT = [("Precios en tres tiendas del barrio (dólares)", ["Tienda A", "Tienda B", "Tienda C"], ["Leche", "Pan", "Huevos"], 2, 7),
          ("Minutos que tarda cada ruta de autobús", ["Ruta 9", "Ruta 49", "Ruta 66"], ["Mañana", "Tarde", "Noche"], 15, 45),
          ("Estudiantes en cada clase por día", ["Inglés", "GED", "Computación"], ["Lunes", "Miércoles", "Viernes"], 8, 30)]
    k = 0
    while len(ta) < 24:
        t, fi, co, a, b = CT[k % 3]; k += 1
        M = [distintos(3, a, b, 1) for _ in fi]; tipo = k % 3; i, j = r.randrange(3), r.randrange(3)
        if tipo == 0: q, ops, n = f"¿Qué valor hay en «{fi[i]}», columna «{co[j]}»?", num_ops(M[i][j], 2), f"Fila {fi[i]}, columna {co[j]}: {M[i][j]}."
        elif tipo == 1:
            col = [M[x][j] for x in range(3)]; mn = min(col)
            if col.count(mn) > 1: continue
            ok = fi[col.index(mn)]; q, ops, n = f"En la columna «{co[j]}», ¿qué fila tiene el valor más bajo?", [ok] + [f for f in fi if f != ok], f"{ok}: {mn}."
        else:
            x = (i + 1) % 3; d = abs(M[i][j] - M[x][j])
            if d == 0: continue
            q, ops, n = f"¿Cuál es la diferencia entre «{fi[i]}» y «{fi[x]}» en «{co[j]}»?", num_ops(d, 2), f"{max(M[i][j], M[x][j])} − {min(M[i][j], M[x][j])} = {d}."
        ta.append({"enun": G.tabla_datos(t, co, list(zip(fi, M))) + f"<p><strong>{q}</strong></p>", "ops": ops, "ok": 0, "pista": "Ponga un dedo en la fila y otro en la columna: el dato está donde se cruzan.", "exp": n})
    mods = [("barras", "Gráficas de barras", C.om("m1", "Lea la gráfica y responda. Los datos de esta práctica son de ejemplo.")), ("lineas", "Gráficas de líneas", C.om("m2", "Siga la línea y responda.")),
            ("circulares", "Gráficas circulares", C.om("m3", "Lea las porciones y responda.")), ("tablas", "Tablas de datos", C.om("m4", "Busque el dato donde se cruzan la fila y la columna."))]
    js = (C.js_datos("BA", ba) + C.js_datos("LI", li) + C.js_datos("CI", ci) + C.js_datos("TA", ta) +
          'creaBanco("m1", BA);\ncreaBanco("m2", LI);\ncreaBanco("m3", CI);\ncreaBanco("m4", TA);\n')
    return C.pagina_practica(N, LE.titulo(N), "Cuatro actividades · los ejercicios cambian cada vez · dos intentos en cada uno", mods, js)


if __name__ == "__main__":
    LE.construye(N, leccion, practica, horas="Unas 3 horas")
