# -*- coding: utf-8 -*-
"""LearnGED · Artes del lenguaje (español) · Nivel 1 · Lección 7.5 · Escribir sobre información visual.
Fuente: clases_leng1/clase_7-5.html (GEDparaHispanos), adaptada al marco de LearnGED.
Datos: temperatura promedio de julio, normales 1991–2020 de la NOAA (Chicago 75, Miami 84, Phoenix 96, Seattle 67 °F, redondeados).
Horas de luz en Chicago el día 15: según los horarios de salida y puesta del sol (enero, unas 9 h y media; abril, 13; julio, 15; octubre, 11).
Corrección respecto de la fuente: en enero hay unas 9 horas y media de luz, no 10.
Uso: python3 tools/build_leng1_7_5.py
"""
import os, sys, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import leng_es as LE
from leng_es import C

LE.nivel(1)
N = "7-5"
CLASES = ["Sustantivo", "Verbo", "Adjetivo"]
PALABRAS = [("parque", 0), ("perro", 0), ("banco", 0), ("flores", 0), ("autobús", 0), ("vendedor", 0), ("mercado", 0), ("niños", 0),
            ("camina", 1), ("brilla", 1), ("juegan", 1), ("vende", 1), ("espera", 1), ("corre", 1), ("llueve", 1), ("compra", 1),
            ("tranquilo", 2), ("verde", 2), ("soleado", 2), ("ruidoso", 2), ("grande", 2), ("colorido", 2), ("mojado", 2), ("pequeño", 2)]
JULIO = [("Chicago", 75), ("Miami", 84), ("Phoenix", 96), ("Seattle", 67)]
LUZ = [("Enero", 9.5), ("Abril", 13), ("Julio", 15), ("Octubre", 11)]
# Gráficas para la práctica (datos de ejemplo): (título, eje X, eje Y, unidad, datos, tema)
GRAFS = [("Clientes de la panadería por día", "Día", "Clientes", "clientes", [("Lunes", 40), ("Martes", 30), ("Miércoles", 35), ("Jueves", 45), ("Viernes", 60)], "cuántos clientes tuvo la panadería cada día"),
         ("Estudiantes inscritos por mes", "Mes", "Estudiantes", "estudiantes", [("Enero", 20), ("Febrero", 25), ("Marzo", 35), ("Abril", 30)], "cuántos estudiantes se inscribieron cada mes"),
         ("Botellas recicladas por cada piso del edificio", "Piso", "Botellas", "botellas", [("Piso 1", 50), ("Piso 2", 80), ("Piso 3", 30), ("Piso 4", 60)], "cuántas botellas recicló cada piso"),
         ("Minutos de espera en la clínica", "Día", "Minutos", "minutos", [("Lunes", 45), ("Miércoles", 20), ("Viernes", 30), ("Sábado", 60)], "cuántos minutos esperan los pacientes cada día")]
# (oración sobre una gráfica, True si es hecho)
HO = [("Phoenix tiene la temperatura más alta de julio.", True), ("En Phoenix se vive mal por el calor.", False), ("Seattle tiene 67 grados en julio.", True),
      ("Seattle es la ciudad más agradable para vivir.", False), ("Miami tiene más calor que Chicago en julio.", True), ("El verano de Miami es insoportable.", False),
      ("En julio, Chicago tiene unas 15 horas de luz.", True), ("Julio es el mejor mes del año.", False), ("En enero hay menos horas de luz que en abril.", True), ("El invierno es una época triste.", False)]


def barras(tit, xe, ye, dat, txt=None, py=None):
    spec = {"tipo": "barras", "xEtq": xe, "yEtq": ye, "barras": [{"etq": c, "valor": v, **({"txt": txt(v)} if txt else {})} for c, v in dat]}
    if py:
        spec["py"] = py
    desc = f"Gráfica de barras: {tit}. " + "; ".join(f"{c}, {v}" for c, v in dat) + "."
    return f'<figure class="figura grafica"><figcaption class="graf-tit">{tit}</figcaption>{C.grafica(spec, desc, ancho=520, alto=300)}</figure>'


def num(v):
    return str(v).replace(".5", " y media") if isinstance(v, float) else str(v)


def leccion():
    P = C.Practicas()
    s1 = f"""<p>A veces hay que escribir a partir de una imagen, una gráfica, un mapa o una tabla. El error común es empezar a escribir sin observar: sale un párrafo confuso, con detalles sueltos. La <strong>técnica de las tres listas</strong> lo evita.</p>
{C.tabla("Las tres listas, antes de escribir", ["Lista", "Pregunta", "Ejemplo: un parque por la mañana"],
         [["📦 Sustantivos", "¿Qué cosas, personas y lugares veo?", "parque, árboles, banco, persona, perro, flores, sol"],
          ["⚡ Verbos", "¿Qué acciones ocurren?", "camina, brilla, florecen, pasea, descansa"], ["🎨 Adjetivos", "¿Cómo es lo que veo?", "tranquilo, verde, soleado, limpio, pequeño"]])}
<p><span class="escena" role="img" aria-label="Un parque con árboles, un banco, una persona que pasea a su perro, flores y el sol.">🌳 🪑 🚶 🐕 🌷 ☀️</span></p>
<p>Con las listas, las oraciones salen casi solas: junte un sustantivo con un verbo y agréguele uno o dos adjetivos.</p>
<ul><li>El parque está tranquilo y soleado esta mañana.</li><li>Una persona camina con su perro por el sendero.</li><li>Las flores crecen entre el césped verde.</li></ul>
{C.caja("tip", "Idea central", "<p>Las tres listas son un <strong>mapa de la imagen</strong>: primero anota lo que ve, por clases; después escribe con dirección, no a ciegas.</p>")}"""

    g = barras("Temperatura promedio en julio (°F)", "Ciudad", "Temperatura (°F)", JULIO, txt=lambda v: f"{v} °F", py=20)
    s2 = f"""<p>Cuando la imagen es una gráfica, un mapa o una tabla, la descripción sigue tres pasos (los practicó en la Lección 6.6):</p>
<ol><li><strong>Tema general:</strong> qué muestra (el título).</li><li><strong>Datos principales:</strong> al menos dos valores.</li><li><strong>Comparación o conclusión:</strong> cuál es mayor, cuál menor, qué se deduce.</li></ol>
{C.tabla("Frases útiles para describir datos", ["Para…", "Frases"],
         [["Presentar", "La gráfica muestra… · La tabla presenta… · El mapa indica… · Según los datos…"], ["Dar cantidades", "…alcanza… · …llega a… · …registra… · …es de aproximadamente…"],
          ["Comparar", "…es mayor que… · …es menor que… · …el más alto… · …el más bajo… · …el doble de…"], ["Concluir", "Por lo tanto… · En conclusión… · Esto indica que… · Se puede observar que…"]])}
{g}
<p class="nota-fina">Fuente: NOAA, normales climáticas 1991–2020 (valores redondeados). Consultado en noviembre de 2026.</p>
<div class="texto-lectura"><p><strong>(1)</strong> La gráfica muestra la temperatura promedio de julio en cuatro ciudades de los Estados Unidos. <strong>(2)</strong> Phoenix alcanza los 96 grados, Miami llega a 84, Chicago registra 75 y Seattle tiene 67. <strong>(3)</strong> Por lo tanto, Phoenix es la ciudad más calurosa y Seattle la más fresca: la diferencia es de 29 grados.</p></div>
{C.caja("ojo", "Sin opinión", "<p>«Phoenix es la ciudad más calurosa» es un <strong>hecho</strong> que se ve en la gráfica. «En Phoenix se vive mal por el calor» es una <strong>opinión</strong>: no va en esta tarea.</p>")}"""

    g2 = barras("Horas de luz en Chicago (el día 15 de cada mes)", "Mes", "Horas de luz", LUZ, txt=lambda v: f"{num(v)} h".replace(" y media h", " ½ h"), py=2)
    s3 = f"""<p>Describa esta gráfica en su cuaderno, en tres o cuatro oraciones, con los tres pasos.</p>
{g2}
<p class="nota-fina">Valores aproximados, calculados con las horas de salida y puesta del sol en Chicago. Consultado en noviembre de 2026.</p>
{P("Paso 1", "¿Cuál es la mejor primera oración?", ["La gráfica muestra cuántas horas de luz hay en Chicago en cuatro meses del año.", "En julio hay 15 horas de luz.", "Me gusta más el verano que el invierno."], 0,
   {1: "Es un dato: va en el paso 2.", 2: "Es una opinión: no va."}, "La primera oración presenta el <strong>tema</strong>.")}
{P("Paso 2", "¿Qué mes tiene más horas de luz?", ["Julio", "Abril", "Octubre"], 0, {1: "Abril tiene 13.", 2: "Octubre tiene 11."}, "<strong>Julio</strong>, con unas 15 horas.")}
{P("Paso 2", "¿Qué mes tiene menos horas de luz?", ["Enero", "Octubre", "Abril"], 0, {1: "Octubre tiene 11.", 2: "Abril tiene 13."}, "<strong>Enero</strong>, con unas 9 horas y media.")}
{P("Paso 3", "¿Qué conclusión se apoya en los datos?", ["En verano hay muchas más horas de luz que en invierno.", "En invierno hay más luz que en verano.", "Todos los meses tienen las mismas horas de luz."], 0,
   {1: "Enero tiene menos que julio.", 2: "Las barras son distintas."}, "En julio hay unas <strong>5 horas y media más</strong> de luz que en enero.")}
<details class="caja caja-tip"><summary><strong>Ya escribí la mía: ver un ejemplo</strong></summary>
<p>«La gráfica muestra cuántas horas de luz hay en Chicago el día 15 de cuatro meses del año. En julio hay unas 15 horas de luz, y en enero, solo unas 9 y media. Abril y octubre quedan en medio, con 13 y 11 horas. Por lo tanto, en verano hay muchas más horas de luz que en invierno.»</p></details>"""

    secciones = [("s1", "Antes de escribir: las tres listas", s1), ("s2", "Describir gráficas, mapas y tablas", s2), ("s3", "Práctica: describa una gráfica", s3)]
    tarea = [("Una foto de mi vida.", "Elija una foto de su barrio, su trabajo o su familia. Haga las tres listas: al menos cinco sustantivos, cinco verbos y cinco adjetivos."),
             ("El párrafo.", "Escriba un párrafo de 4 a 6 oraciones que describa la foto con las palabras de sus listas."),
             ("Una gráfica.", "Busque una gráfica en un periódico o en internet y descríbala en tres oraciones con los tres pasos. Anote de dónde la sacó y la fecha.")]
    quiz = [
        ("¿Cuál es el error común al escribir sobre una imagen?", ["Empezar a escribir sin observar", "Hacer listas antes"], 0, {}, "Empezar <strong>sin observar</strong>."),
        ("¿Qué tres listas se hacen antes de escribir?", ["Sustantivos, verbos y adjetivos", "Títulos, ejes y fuentes", "Primero, luego y después"], 0, {1: "Eso es de las gráficas.", 2: "Eso son palabras de secuencia."}, "<strong>Sustantivos, verbos y adjetivos.</strong>"),
        ("<em>soleado</em> va en la lista de…", CLASES, 2, {0: "No es una cosa.", 1: "No es una acción."}, "<strong>Adjetivos</strong>: dice cómo es."),
        ("<em>camina</em> va en la lista de…", CLASES, 1, {0: "No es una cosa.", 2: "No dice cómo es algo."}, "<strong>Verbos</strong>: es una acción."),
        ("¿Cuál es el primer paso para describir una gráfica?", ["Decir el tema general", "Dar la conclusión", "Dar mi opinión"], 0, {1: "Ese es el último.", 2: "No va."}, "El <strong>tema general</strong>."),
        ("¿Cuántos datos conviene dar como mínimo?", ["Dos", "Ninguno"], 0, {}, "Al menos <strong>dos</strong>."),
        ("<em>En Phoenix se vive mal por el calor.</em>", ["Es una opinión", "Es un hecho"], 0, {}, "Una <strong>opinión</strong>: no va al describir datos."),
        ("¿Qué frase sirve para concluir?", ["Esto indica que…", "La gráfica muestra…"], 0, {}, "<strong>Esto indica que…</strong>"),
        ("Según la gráfica de julio, ¿cuál es la ciudad más fresca?", ["Seattle", "Chicago", "Miami"], 0, {1: "Chicago tiene 75.", 2: "Miami tiene 84."}, "<strong>Seattle</strong>, con 67 °F."),
        ("¿Qué diferencia hay entre Phoenix (96) y Seattle (67)?", ["29 grados", "163 grados", "19 grados"], 0, {1: "Eso es la suma.", 2: "Reste otra vez: 96 − 67."}, "<strong>29 grados.</strong>"),
    ]
    filas = [
        ("Las tres listas", "Hago las tres listas antes de escribir sobre una imagen.", "Hago una o dos.", "Escribo sin observar (<a href=\"#s1\">repase la sección 1</a>)."),
        ("Describir datos", "Doy el tema, dos datos y una conclusión, sin opinar.", "Doy datos, pero sin conclusión.", "No sé por dónde empezar (<a href=\"#s2\">repase la sección 2</a>)."),
    ]
    cierre = "<p>Ya sabe escribir a partir de una imagen o una gráfica. En la última lección del tema va a aprender a mejorar lo que escribe: <strong>el proceso de revisión</strong>.</p>"
    glosario = [("Técnica de las tres listas", "Anotar sustantivos, verbos y adjetivos antes de escribir sobre una imagen."), ("Descripción de datos", "Tema, datos principales y conclusión, sin opinión.")]
    conexion = ("<p>Ya sabe construir párrafos (Lecciones 7.1 y 7.2) y elegir el tipo de texto (7.3 y 7.4). Ahora va a juntarlo todo para escribir a partir de información visual: una imagen, una gráfica, un mapa o una tabla.</p>"
                "<p><strong>Lo que necesita:</strong> el cuaderno y una foto que pueda mirar con calma.</p>")
    estd = LE.estandares(["W.2", "R.7.2"])
    return C.pagina_leccion(N, LE.titulo(N), "Mirar primero, anotar después, escribir al final.", ["Escritura", "Información visual"],
                            ["<strong>Usar</strong> la técnica de las tres listas antes de escribir sobre una imagen.", "<strong>Describir</strong> una gráfica con tema, datos y conclusión.",
                             "<strong>Evitar</strong> la opinión al describir datos."],
                            estd, conexion, secciones, tarea, quiz, filas, cierre, ("7-6", LE.titulo("7-6")), glosario, P)


def practica():
    r = random.Random(75)
    pal = [{"enun": f"<strong class=\"grande\">{w}</strong><br>¿En qué lista va esta palabra?", "ops": CLASES, "ok": k, "enOrden": True, "pista": "Sustantivo: una cosa, persona o lugar. Verbo: una acción. Adjetivo: cómo es algo.",
            "exp": f"Va en la lista de <strong>{['sustantivos', 'verbos', 'adjetivos'][k]}</strong>."} for w, k in PALABRAS]
    des = []
    for i, (tit, xe, ye, u, dat, tema) in enumerate(GRAFS):
        g = barras(tit, xe, ye, dat, txt=lambda v: str(v))
        alto = max(dat, key=lambda x: x[1]); bajo = min(dat, key=lambda x: x[1]); otro = GRAFS[(i + 1) % len(GRAFS)][5]
        des.append({"enun": f"{g}¿Cuál es la mejor primera oración para describir la gráfica?", "ops": [f"La gráfica muestra {tema}.", f"La gráfica muestra {otro}.", f"{bajo[0]} tiene el valor más bajo, con {bajo[1]} {u}."], "ok": 0,
                    "pista": "La primera oración presenta el tema, como el título.", "exp": f"<strong>La gráfica muestra {tema}.</strong> Los datos van después."})
        des.append({"enun": f"{g}¿Qué oración da los datos correctamente?", "ops": [f"{alto[0]} llega a {alto[1]} {u}, y {bajo[0]} solo a {bajo[1]}.", f"{bajo[0]} llega a {alto[1]} {u}, y {alto[0]} solo a {bajo[1]}.", f"Todos los valores son iguales: {alto[1]} {u}."], "ok": 0,
                    "pista": "Compruebe cada número en la gráfica.", "exp": f"<strong>{alto[0]}</strong> tiene {alto[1]} y <strong>{bajo[0]}</strong> tiene {bajo[1]}."})
        des.append({"enun": f"{g}¿Qué conclusión se apoya en los datos?", "ops": [f"{alto[0]} tiene el valor más alto de la gráfica.", f"{bajo[0]} tiene el valor más alto de la gráfica.", f"Seguramente a nadie le importa esta gráfica."], "ok": 0,
                    "pista": "La conclusión tiene que poder comprobarse en la gráfica, sin opiniones.", "exp": f"<strong>{alto[0]}</strong> tiene la barra más alta: {alto[1]} {u}."})
    ho = [{"enun": f"<strong>{o}</strong><br>¿Va en una descripción de datos?", "ops": ["Sí: es un hecho de la gráfica", "No: es una opinión"], "ok": 0 if h else 1, "enOrden": True, "pista": "",
           "exp": "Es un <strong>hecho</strong> que se ve en la gráfica." if h else "Es una <strong>opinión</strong>: no va al describir datos."} for o, h in HO]
    mods = [("listas", "¿En qué lista va?", C.om("m1", "Clasifique cada palabra en su lista.")),
            ("describir", "Describa la gráfica paso a paso", C.om("m2", "Elija la oración correcta para cada paso. Los datos son de ejemplo.")),
            ("hecho", "¿Hecho u opinión?", C.om("m3", "Decida si la oración va en una descripción de datos (gráficas de la lección)."))]
    js = C.js_datos("PAL", pal) + C.js_datos("DES", des) + C.js_datos("HO", ho) + 'creaBanco("m1", PAL);\ncreaBanco("m2", DES);\ncreaBanco("m3", HO);\n'
    return C.pagina_practica(N, LE.titulo(N), "Tres actividades · los ejercicios cambian cada vez · dos intentos en cada uno", mods, js)


if __name__ == "__main__":
    LE.construye(N, leccion, practica, horas="Unas 3 horas")
