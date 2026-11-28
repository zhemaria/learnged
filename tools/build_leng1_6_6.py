# -*- coding: utf-8 -*-
"""LearnGED · Artes del lenguaje (español) · Nivel 1 · Lección 6.6 · Vocabulario de dominio y aplicación.
Fuente: clases_leng1/clase_6-6.html (GEDparaHispanos) y gramatica/n1-l6-6.html, adaptadas al marco de LearnGED.
Datos: población de Chicago en el censo de 2020 (2,746,388); temperaturas por estación en O'Hare, normales 1991–2020 de la NOAA
(invierno 28 °F, primavera 50 °F, verano 73 °F, otoño 54 °F, redondeadas).
Uso: python3 tools/build_leng1_6_6.py
"""
import os, sys, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import leng_es as LE
from leng_es import C

LE.nivel(1)
N = "6-6"
PALABRAS = [("Población", "el número de personas que viven en un lugar", "Estudios Sociales", "Según el censo de 2020, la población de Chicago es de unos 2.7 millones de personas."),
            ("Latitud", "la distancia de un lugar al norte o al sur del ecuador, en grados (°)", "Estudios Sociales", "Chicago está a casi 42° de latitud norte."),
            ("Altitud", "la altura de un lugar sobre el nivel del mar", "Ciencias", "La altitud de Denver es de una milla, unos 1,600 metros: por eso la llaman «la ciudad de una milla de altura»."),
            ("Temperatura", "la medida de lo frío o caliente que está algo, en grados Fahrenheit (°F) o Celsius (°C)", "Ciencias", "En julio, la temperatura máxima promedio en Miami ronda los 90&nbsp;°F."),
            ("Leyenda", "el cuadro que explica los símbolos, colores o líneas de un mapa o una gráfica", "Estudios Sociales", "Según la leyenda, el verde representa las zonas de bosque."),
            ("Escala", "la relación entre el tamaño en el mapa y la distancia real", "Estudios Sociales", "La escala muestra que cada centímetro del mapa equivale a 5 kilómetros.")]
MAS = [("Ecosistema", "los seres vivos de un lugar y el medio en que viven"), ("Clima", "el tiempo atmosférico típico de un lugar durante muchos años"),
       ("Frontera", "la línea que separa dos países o estados"), ("Censo", "el conteo oficial de la población")]
COMPLETA = [("La ____ de Bogotá es de unos 2,640 metros sobre el nivel del mar.", "altitud", ["censo", "ecosistema"], "la altura sobre el nivel del mar"),
            ("Según el ____ de 2020, en el condado viven más de cinco millones de personas.", "censo", ["latitud", "escala"], "el conteo oficial de la población"),
            ("La ____ de la ciudad creció mucho en los últimos diez años: ahora vive más gente.", "población", ["latitud", "escala"], "el número de personas que viven en un lugar"),
            ("Mire la ____ del mapa para saber qué significa cada color.", "leyenda", ["frontera", "temperatura"], "el cuadro que explica los símbolos"),
            ("Según la ____, un centímetro del mapa equivale a 10 kilómetros.", "escala", ["censo", "ecosistema"], "relaciona el mapa con la distancia real"),
            ("Hoy la ____ máxima será de 85 °F.", "temperatura", ["frontera", "altitud"], "lo caliente o frío"),
            ("El río Bravo marca la ____ entre México y Estados Unidos en Texas.", "frontera", ["ecosistema", "leyenda"], "la línea que separa dos países"),
            ("El ____ de Miami es cálido y húmedo casi todo el año.", "clima", ["altitud", "leyenda"], "el tiempo típico de un lugar durante muchos años"),
            ("Un pantano es un ____ donde viven peces, aves, plantas y caimanes.", "ecosistema", ["censo", "leyenda"], "los seres vivos y el medio en que viven"),
            ("Quito está casi en el ecuador: su ____ es de casi 0°.", "latitud", ["población", "escala"], "la distancia al norte o al sur del ecuador")]
# (título, eje X, eje Y, unidad, datos, qué se mide en minúsculas)
GRAFS = [("Clientes de la tienda por día", "Día", "Clientes", "clientes", [("Lunes", 30), ("Martes", 25), ("Miércoles", 20), ("Jueves", 35), ("Viernes", 50)], "el número de clientes de la tienda cada día"),
         ("Lluvia por mes, en pulgadas", "Mes", "Pulgadas", "pulgadas", [("Marzo", 3), ("Abril", 4), ("Mayo", 5), ("Junio", 4), ("Julio", 2)], "la lluvia que cayó cada mes"),
         ("Horas de sueño de la familia", "Persona", "Horas", "horas", [("Papá", 6), ("Mamá", 7), ("Ana", 9), ("Beto", 10)], "cuántas horas duerme cada miembro de la familia"),
         ("Estudiantes por clase", "Clase", "Estudiantes", "estudiantes", [("Inglés", 25), ("Computación", 15), ("GED", 30), ("Costura", 10)], "cuántos estudiantes hay en cada clase")]
ESTACIONES = [("Invierno", 28), ("Primavera", 50), ("Verano", 73), ("Otoño", 54)]


def barras(tit, xe, ye, dat, txt=None, py=None):
    spec = {"tipo": "barras", "xEtq": xe, "yEtq": ye, "barras": [{"etq": c, "valor": v, **({"txt": txt(v)} if txt else {})} for c, v in dat]}
    if py:
        spec["py"] = py
    desc = f"Gráfica de barras: {tit}. " + "; ".join(f"{c}, {v}" for c, v in dat) + "."
    return f'<figure class="figura grafica"><figcaption class="graf-tit">{tit}</figcaption>{C.grafica(spec, desc, ancho=520, alto=300)}</figure>'


def leccion():
    P = C.Practicas()
    filas_p = [[f"<strong>{p}</strong>", m, d, f"<em>{e}</em>"] for p, d, m, e in PALABRAS]
    s1 = f"""<p>En la vida diaria usamos palabras comunes: casa, calle, comida. Pero en un texto de ciencias o de historia aparecen otras: <em>población, latitud, ecosistema, soberanía</em>. Son el <strong>vocabulario de dominio</strong>: palabras propias de un campo de conocimiento.</p>
{C.caja("tip", "Idea central", "<p>No tiene que aprender de memoria todas las palabras técnicas. Lo que necesita es una <strong>estrategia</strong> para reconocerlas y deducir su significado por el contexto.</p>")}
<h3>Seis palabras esenciales</h3>
{C.tabla("Seis palabras de Ciencias y Estudios Sociales", ["Palabra", "Materia", "Qué significa", "Ejemplo"], filas_p)}
<p class="nota-fina">Datos de los ejemplos: Oficina del Censo de los EE. UU., censo de 2020 (Chicago: 2,746,388 personas); NOAA, normales climáticas 1991–2020 (Miami, julio). Consultado en noviembre de 2026.</p>"""

    s2 = f"""<p>Cuando no tenga diccionario, el texto suele dar pistas: son las <strong>claves de contexto</strong> de la Lección 4.5, ahora con palabras de Ciencias y de Estudios Sociales.</p>
{C.tabla("Tres claves de contexto", ["Clave", "Ejemplo", "Qué le dice"],
         [["🔍 Definición", "«La <strong>altitud</strong>, es decir, la altura sobre el nivel del mar, influye en la temperatura.»", "El autor explica la palabra justo después, con comas o con <em>es decir</em>."],
          ["🔍 Ejemplos", "«Los <strong>cítricos</strong>, como la naranja, el limón y la toronja, tienen vitamina C.»", "Los ejemplos muestran que son frutas ácidas."],
          ["🔍 Contraste", "«Algunas regiones son <strong>áridas</strong>, pero otras son muy húmedas y llenas de plantas.»", "Lo opuesto (húmedas) dice que <em>áridas</em> es secas."]])}
{P("Compruebe", "«El <strong>censo</strong>, es decir, el conteo oficial de la población, se hace cada diez años.» ¿Qué clave ayuda?", ["Una definición", "Unos ejemplos", "Un contraste"], 0,
   {1: "No hay una lista de ejemplos.", 2: "No hay un opuesto."}, "Una <strong>definición</strong>: «es decir» la anuncia.")}
{P("Compruebe", "¿Qué palabra significa <em>la línea que separa dos países o estados</em>?", ["Frontera", "Latitud", "Leyenda"], 0, {1: "La latitud es la distancia al ecuador.", 2: "La leyenda explica los símbolos."}, "<strong>Frontera.</strong>")}"""

    graf = barras("Temperatura promedio en Chicago por estación", "Estación del año", "Temperatura (°F)", ESTACIONES, txt=lambda v: f"{v} °F", py=20)
    s3 = f"""<p>Ahora va a usar todo el tema: leer una gráfica y escribir un párrafo corto que la describa. Es una destreza para todo el GED, y también para el trabajo.</p>
{graf}
<p class="nota-fina">Fuente: NOAA, normales climáticas 1991–2020, estación del aeropuerto O'Hare. Valores redondeados. Consultado en noviembre de 2026.</p>
<div class="caja caja-tip"><span class="etiqueta et-verde">Actividad · en su cuaderno</span>
<p>Complete la plantilla con los datos de la gráfica:</p>
<ol><li>«La gráfica muestra ____ en Chicago durante las cuatro estaciones del año.»</li><li>«La temperatura más alta es en ____, con ____ °F.»</li>
<li>«En cambio, la más baja es en ____, con apenas ____ °F.»</li><li>«Esto quiere decir que ____.»</li></ol></div>
<details class="caja caja-tip"><summary><strong>Ya escribí el mío: ver un ejemplo</strong></summary>
<p>«La gráfica muestra la temperatura promedio en Chicago durante las cuatro estaciones del año. La temperatura más alta es en verano, con 73 °F. En cambio, la más baja es en invierno, con apenas 28 °F. Esto quiere decir que en Chicago hay una gran diferencia entre el verano y el invierno: unos 45 grados.»</p>
<p>Fíjese en que usa el título, nombra el valor más alto y el más bajo con sus números, compara con <em>en cambio</em> y termina con una conclusión.</p></details>"""

    secciones = [("s1", "El vocabulario de dominio", s1), ("s2", "Claves de contexto", s2), ("s3", "Práctica escrita: describir una gráfica", s3)]
    tarea = [("Mi glosario.", "Haga en su cuaderno un glosario con las seis palabras esenciales y las cuatro de la práctica (ecosistema, clima, frontera, censo): la palabra, su significado con sus palabras y un ejemplo propio."),
             ("A la caza.", "Busque en una noticia o un folleto dos palabras de Ciencias o de Estudios Sociales que no conozca. Escriba qué clave de contexto le ayudó a entenderlas."),
             ("Mi gráfica, en palabras.", "Describa con la plantilla de la sección 3 la gráfica que hizo en la tarea de la Lección 6.5.")]
    quiz = [
        ("¿Qué es el vocabulario de dominio?", ["Palabras propias de un campo, como la ciencia o la historia", "Palabras de la casa", "Palabras en inglés"], 0, {1: "Esas son palabras comunes.", 2: "No."}, "Palabras de un <strong>campo de conocimiento</strong>."),
        ("¿Qué significa <strong>población</strong>?", ["El número de personas que viven en un lugar", "La altura de un lugar", "El cuadro de los símbolos"], 0, {1: "Eso es la altitud.", 2: "Eso es la leyenda."}, "<strong>El número de personas.</strong>"),
        ("¿Qué significa <strong>latitud</strong>?", ["La distancia al norte o al sur del ecuador", "La altura sobre el mar", "El clima"], 0, {1: "Eso es la altitud.", 2: "No."}, "<strong>La distancia al ecuador.</strong>"),
        ("¿Qué significa <strong>altitud</strong>?", ["La altura sobre el nivel del mar", "La distancia al ecuador", "La temperatura"], 0, {1: "Eso es la latitud.", 2: "No."}, "<strong>La altura sobre el nivel del mar.</strong>"),
        ("«Los <strong>cítricos</strong>, como la naranja y el limón…» ¿Qué clave ayuda?", ["Ejemplos", "Definición", "Contraste"], 0, {1: "No hay «es decir».", 2: "No hay un opuesto."}, "<strong>Ejemplos.</strong>"),
        ("«Unas zonas son <strong>áridas</strong>, pero otras son húmedas.» ¿Qué significa áridas?", ["Secas", "Húmedas", "Frías"], 0, {1: "Es lo contrario: «pero» marca el contraste.", 2: "No se habla del frío."}, "<strong>Secas</strong>: lo dice el contraste con húmedas."),
        ("En la gráfica de Chicago, ¿qué estación es la más fría?", ["Invierno", "Otoño", "Primavera"], 0, {1: "El otoño tiene 54 °F.", 2: "La primavera tiene 50 °F."}, "<strong>Invierno</strong>, con 28 °F."),
        ("¿Qué debe tener un buen párrafo que describe una gráfica?", ["El tema, el dato más alto y el más bajo, y una conclusión", "Solo el título", "Solo la opinión de quien escribe"], 0, {1: "Falta lo más importante.", 2: "Hay que usar los datos."}, "<strong>Tema, datos y conclusión.</strong>"),
        ("¿Qué significa <strong>censo</strong>?", ["El conteo oficial de la población", "El clima de un lugar"], 0, {}, "<strong>El conteo oficial de la población.</strong>"),
        ("¿Qué palabra se usa para comparar en el párrafo modelo?", ["en cambio", "por ejemplo"], 0, {}, "<strong>En cambio</strong>: marca el contraste."),
    ]
    filas = [
        ("Vocabulario", "Explico las seis palabras esenciales con mis palabras.", "Conozco algunas.", "No las recuerdo (<a href=\"#s1\">repase la sección 1</a>)."),
        ("Claves de contexto", "Deduzco una palabra nueva por definición, ejemplos o contraste.", "Uso solo una clave.", "Necesito siempre el diccionario (<a href=\"#s2\">repase la sección 2</a>)."),
        ("Describir una gráfica", "Escribo tema, datos más alto y más bajo, comparación y conclusión.", "Doy datos, pero no concluyo.", "No sé por dónde empezar (<a href=\"#s3\">repase la sección 3</a>)."),
    ]
    cierre = ("<p>Terminó el Tema 6. Ya sabe leer imágenes, artículos, mapas, tablas y gráficas, y hablar de ellos con el vocabulario de Ciencias y de Estudios Sociales.</p>"
              "<p>En el Tema 7 va a escribir: <strong>el párrafo y los tipos de texto</strong>.</p>")
    glosario = [(p, d[0].upper() + d[1:] + ".") for p, d, _, _ in PALABRAS] + [(p, d[0].upper() + d[1:] + ".") for p, d in MAS]
    conexion = ("<p>Ya sabe leer imágenes, mapas, tablas y gráficas. Ahora va a dar el paso final: hablar y escribir sobre lo que ve en ellas, con las palabras propias de Ciencias y de Estudios Sociales.</p>"
                "<p><strong>Lo que necesita:</strong> el cuaderno.</p>")
    estd = LE.estandares(["R.4.1", "R.7.2"], base=["W.2"])
    return C.pagina_leccion(N, LE.titulo(N), "Las palabras de Ciencias y de Estudios Sociales, y una gráfica descrita con ellas.", ["R.4.1 · Vocabulario", "R.7 · Información visual"],
                            ["<strong>Explicar</strong> seis palabras esenciales de Ciencias y de Estudios Sociales.", "<strong>Deducir</strong> palabras nuevas con las claves de contexto.",
                             "<strong>Escribir</strong> un párrafo que describe una gráfica con datos y una conclusión."],
                            estd, conexion, secciones, tarea, quiz, filas, cierre, ("7-1", LE.titulo("7-1")), glosario, P)


def practica():
    r = random.Random(66)
    todas = [p for p, _, _, _ in PALABRAS] + [p for p, _ in MAS]
    defs = [(p, d) for p, d, _, _ in PALABRAS] + MAS
    voc = [{"enun": f"¿Qué palabra significa <em>{d}</em>?", "ops": [p] + r.sample([x for x in todas if x != p], 2), "ok": 0, "pista": "Piense en el ejemplo de cada palabra.", "exp": f"<strong>{p}</strong> es {d}."} for p, d in defs]
    com = [{"enun": f"Complete la oración.<br><strong>{o}</strong>", "ops": [ok] + d, "ok": 0, "pista": "Lea toda la oración: ¿de qué habla?", "exp": f"Va <strong>{ok}</strong>: {e}."} for o, ok, d, e in COMPLETA]
    des = []
    for i, (tit, xe, ye, u, dat, que) in enumerate(GRAFS):
        otro = GRAFS[(i + 1) % len(GRAFS)][5]
        g = barras(tit, xe, ye, dat, txt=lambda v: str(v))
        alto = max(dat, key=lambda x: x[1]); bajo = min(dat, key=lambda x: x[1])
        des.append({"enun": f"{g}¿Qué oración describe bien la gráfica?", "ops": [f"{alto[0]} tiene el valor más alto, con {alto[1]} {u}.", f"{bajo[0]} tiene el valor más alto, con {bajo[1]} {u}.", f"Todas las barras tienen el mismo valor."],
                    "ok": 0, "pista": "Compruebe cada oración en la gráfica: ¿es verdad lo que dice?", "exp": f"<strong>{alto[0]}</strong> tiene la barra más alta: {alto[1]} {u}."})
        des.append({"enun": f"{g}¿Cuál es la mejor primera oración para describir esta gráfica?", "ops": [f"La gráfica muestra {que}.", f"La gráfica muestra {otro}.", f"{bajo[0]} tiene el valor más bajo de todos, con {bajo[1]} {u}."],
                    "ok": 0, "pista": "La primera oración dice de qué trata la gráfica, como el título.", "exp": f"La primera oración presenta el tema, como el título: <strong>La gráfica muestra {que}.</strong>"})
    mods = [("vocabulario", "¿Qué palabra es?", C.om("m1", "Elija la palabra que corresponde a la definición.")),
            ("completar", "Complete la oración", C.om("m2", "Elija la palabra de dominio que completa la oración.")),
            ("describir", "Describa la gráfica", C.om("m3", "Elija la oración que describe bien la gráfica. Los datos son de ejemplo."))]
    js = C.js_datos("VOC", voc) + C.js_datos("COM", com) + C.js_datos("DES", des) + 'creaBanco("m1", VOC);\ncreaBanco("m2", COM);\ncreaBanco("m3", DES);\n'
    return C.pagina_practica(N, LE.titulo(N), "Tres actividades · los ejercicios cambian cada vez · dos intentos en cada uno", mods, js)


if __name__ == "__main__":
    LE.construye(N, leccion, practica, horas="Unas 3 horas")
