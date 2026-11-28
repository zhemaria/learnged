# -*- coding: utf-8 -*-
"""LearnGED · Artes del lenguaje (español) · Nivel 1 · Lección 5.6 · Comparar y contrastar información.
Fuente: clases_leng1/clase_5-6.html (GEDparaHispanos) y gramatica/n1-l5-6.html, adaptadas al marco de LearnGED.
Uso: python3 tools/build_leng1_5_6.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import leng_es as LE
from leng_es import C

LE.nivel(1)
N = "5-6"
CC = ["Comparar (parecido)", "Contrastar (diferencia)"]
# (oración con el conector en <em>, 0 comparar / 1 contrastar)
CONECT = [("Mi hermana es enfermera, <em>al igual que</em> mi madre.", 0), ("El invierno en Chicago es muy frío; <em>en cambio</em>, en Miami es templado.", 1),
          ("El perro es leal; <em>de la misma manera</em>, el gato puede ser muy fiel.", 0), ("Yo prefiero el café, <em>mientras que</em> mi esposo prefiere el té.", 1),
          ("<em>A diferencia de</em> su hermano, Luis es muy ordenado.", 1), ("El arroz tiene muchas calorías; <em>asimismo</em>, la pasta tiene bastantes.", 0),
          ("La bicicleta no contamina; <em>por el contrario</em>, el carro sí.", 1), ("El español viene del latín, <em>así como</em> el portugués.", 0),
          ("El examen de ciencias fue fácil; <em>sin embargo</em>, el de matemáticas fue difícil.", 1), ("Mi abuela cocinaba con leña, <em>como</em> la tuya.", 0),
          ("Ella habla rápido, <em>pero</em> su hermano habla muy despacio.", 1), ("Los girasoles necesitan mucho sol; <em>de manera similar</em>, los tomates también.", 0),
          ("<em>En contraste con</em> la ciudad, el pueblo es muy tranquilo.", 1), ("Juan trabaja los sábados; María <em>también</em>.", 0),
          ("La renta en el centro es cara; <em>en cambio</em>, en las afueras es más barata.", 1), ("El tigre es un felino, <em>al igual que</em> el león.", 0),
          ("El metro es rápido; <em>sin embargo</em>, el autobús llega a más lugares.", 1), ("Las naranjas tienen vitamina C, <em>así como</em> las fresas.", 0),
          ("Mi primer trabajo era de día, <em>mientras que</em> el actual es de noche.", 1), ("El mango es una fruta tropical, <em>como</em> la piña.", 0)]
# Diagramas de Venn: (A, B, [(rasgo, 0 solo A / 1 los dos / 2 solo B)])
VENN = [("el perro", "el gato", [("Ladra", 0), ("Maúlla", 2), ("Es una mascota", 1), ("Tiene cuatro patas", 1), ("Hay que sacarlo a pasear", 0), ("Usa una caja de arena", 2)]),
        ("el celular", "la computadora de mesa", [("Cabe en el bolsillo", 0), ("Necesita electricidad", 1), ("Tiene una pantalla grande y un teclado aparte", 2), ("Sirve para enviar correos", 1), ("Funciona con batería", 0)]),
        ("el sol", "la luna", [("Da luz propia", 0), ("Se ve en el cielo", 1), ("Refleja la luz del sol", 2), ("Es una estrella", 0), ("Parece cambiar de forma a lo largo del mes", 2)]),
        ("la biblioteca", "la librería", [("Presta los libros gratis", 0), ("Tiene libros", 1), ("Vende los libros", 2), ("Hay que devolver los libros", 0), ("Tiene estantes", 1)]),
        ("el agua", "el refresco", [("No tiene azúcar ni calorías", 0), ("Es una bebida", 1), ("Tiene burbujas y azúcar", 2), ("Se puede tomar fría", 1)]),
        ("la carta en papel", "el correo electrónico", [("Necesita sello y sobre", 0), ("Llega en segundos", 2), ("Sirve para comunicarse", 1), ("Lleva el nombre de quien la recibe", 1), ("Necesita internet", 2)])]
METRO = ["El metro es un sistema de transporte público que circula por vías propias, bajo tierra o elevadas. Tiene horarios fijos y estaciones fijas. Es rápido porque no lo afecta el tráfico de la calle, y puede mover miles de pasajeros por hora.",
         "Funciona con electricidad y necesita una infraestructura costosa. El boleto suele tener un precio fijo."]
BUS = ["El autobús es un sistema de transporte público que circula por las calles de la ciudad. Tiene horarios fijos y paradas fijas. Su velocidad depende del tráfico, y en las horas pico puede tardar mucho.",
       "La mayoría funciona con diésel o gas, y su infraestructura es más sencilla y económica. El boleto suele tener un precio fijo."]
MB = [("Circula por vías propias, bajo tierra o elevadas", 0), ("Circula por las calles", 2), ("Tiene horarios fijos", 1), ("No lo afecta el tráfico", 0), ("Su velocidad depende del tráfico", 2),
      ("Es transporte público", 1), ("Funciona con electricidad", 0), ("La mayoría funciona con diésel o gas", 2), ("El boleto tiene un precio fijo", 1), ("Infraestructura costosa", 0), ("Infraestructura sencilla y económica", 2)]
ARTICO_A = "La perforación petrolera en el Ártico podría crear miles de empleos en el sector de la energía. Al igual que en otras regiones petroleras, traería inversión, carreteras y crecimiento económico para las comunidades cercanas. Además, reduciría la dependencia del petróleo importado."
ARTICO_B = "La perforación petrolera en el Ártico pone en grave riesgo un ecosistema frágil y único. A diferencia de otras regiones, el Ártico se recupera muy lentamente de un derrame de petróleo. Los defensores de la perforación hablan de empleos; sin embargo, los pueblos indígenas de la zona dependen de la fauna y serían los primeros afectados."

VENN_SVG = """<figure class="figura"><svg viewBox="0 0 520 260" role="img" aria-labelledby="venn-t venn-d" style="max-width:520px;width:100%">
<title id="venn-t">Diagrama de Venn</title><desc id="venn-d">Dos círculos que se cruzan. El de la izquierda es el texto A y guarda lo que solo tiene A. El de la derecha es el texto B y guarda lo que solo tiene B. La zona del centro, donde se cruzan, guarda lo que tienen en común.</desc>
<circle cx="200" cy="130" r="115" fill="#0b679c" fill-opacity=".16" stroke="#004b75" stroke-width="3"/><circle cx="320" cy="130" r="115" fill="#b42318" fill-opacity=".14" stroke="#8b1a1a" stroke-width="3"/>
<text x="125" y="122" text-anchor="middle" font-size="20" font-weight="700" fill="#004b75">Texto A</text><text x="125" y="148" text-anchor="middle" font-size="16" fill="#1f2937">solo A</text>
<text x="395" y="122" text-anchor="middle" font-size="20" font-weight="700" fill="#8b1a1a">Texto B</text><text x="395" y="148" text-anchor="middle" font-size="16" fill="#1f2937">solo B</text>
<text x="260" y="122" text-anchor="middle" font-size="17" font-weight="700" fill="#1f2937">En común</text><text x="260" y="146" text-anchor="middle" font-size="15" fill="#1f2937">(parecidos)</text></svg>
<figcaption>Lo que solo tiene A va a la izquierda; lo que solo tiene B, a la derecha; lo que tienen los dos, en el centro.</figcaption></figure>"""


def leccion():
    P = C.Practicas()
    s1 = f"""<p>En el GED pueden aparecer dos textos sobre el mismo tema. La pregunta entonces no es solo «¿qué dice cada uno?», sino «¿en qué se parecen y en qué se diferencian?».</p>
{C.tabla("Dos operaciones distintas", ["Operación", "Qué busca", "Pregunta clave"],
         [["🟰 Comparar", "Parecidos", "¿Qué tienen en común?"], ["↔️ Contrastar", "Diferencias", "¿En qué se diferencian?"]])}
{C.caja("tip", "Idea central", "<p>En la calle se dice «comparar» para las dos cosas, pero al leer con cuidado son distintas: <strong>comparar</strong> busca parecidos y <strong>contrastar</strong> busca diferencias. Un buen lector hace las dos con el mismo par de textos.</p>")}"""

    s2 = f"""<h3>El diagrama de Venn</h3>
{VENN_SVG}
<h3>Las palabras de comparación y de contraste</h3>
{C.tabla("Conectores de comparación y de contraste", ["Función", "Conectores", "Ejemplo"],
         [["Comparar (parecidos)", "como, al igual que, así como, de la misma manera, de manera similar, también, asimismo", "El perro es un animal doméstico, al igual que el gato."],
          ["Contrastar (diferencias)", "pero, sin embargo, en cambio, por el contrario, en contraste, a diferencia de, mientras que", "El perro suele ser sociable; en cambio, el gato prefiere estar solo."]])}
{C.caja("ojo", "Fíjese en lo que viene después", "<p>Si después del conector aparece algo <strong>parecido</strong>, es comparación; si aparece algo <strong>opuesto</strong>, es contraste.</p>")}
<h3>Dos textos sobre el mismo tema</h3>
<p>Estos dos textos tratan de la perforación petrolera en el Ártico, desde posiciones opuestas.</p>
<div class="texto-lectura"><p><strong>Texto A · A favor</strong></p><p>{ARTICO_A}</p></div>
<div class="texto-lectura"><p><strong>Texto B · En contra</strong></p><p>{ARTICO_B}</p></div>
<p>El texto A usa <em>al igual que</em> para comparar el Ártico con otras regiones; el B usa <em>a diferencia de</em> y <em>sin embargo</em> para marcar contraste.</p>
{P("Compruebe", "¿En qué <strong>coinciden</strong> los dos textos?", ["Los dos hablan de la perforación petrolera en el Ártico", "Los dos están a favor de perforar", "Los dos hablan de los pueblos indígenas"], 0,
   {1: "El texto B está en contra.", 2: "Solo el texto B menciona a los pueblos indígenas."}, "Los dos tratan <strong>el mismo tema</strong>, desde posiciones opuestas.")}
{P("Compruebe", "¿Qué menciona <strong>solo</strong> el texto A?", ["Reducir el petróleo importado", "Los empleos", "El riesgo de un derrame"], 0,
   {1: "El texto B también habla de empleos, para responder a los defensores.", 2: "Eso lo menciona el texto B."}, "<strong>Reducir el petróleo importado</strong> solo aparece en el texto A.")}"""

    s3 = f"""<h3>El metro y el autobús</h3>
<div class="texto-lectura"><p><strong>Texto A · El metro</strong></p>{"".join(f"<p>{p}</p>" for p in METRO)}</div>
<div class="texto-lectura"><p><strong>Texto B · El autobús</strong></p>{"".join(f"<p>{p}</p>" for p in BUS)}</div>
<div class="caja caja-tip"><span class="etiqueta et-verde">Actividad · en su cuaderno</span>
<p>Dibuje un diagrama de Venn y ponga, según los textos, cada rasgo en su lugar: solo el metro, solo el autobús o los dos. Después escriba dos oraciones: una que compare (con <em>al igual que</em> o <em>también</em>) y otra que contraste (con <em>en cambio</em> o <em>mientras que</em>).</p></div>
<details class="caja caja-tip"><summary><strong>Ya lo hice: ver el modelo</strong></summary>
<ul><li><strong>Solo el metro:</strong> vías propias, no lo afecta el tráfico, electricidad, infraestructura costosa.</li>
<li><strong>Los dos:</strong> transporte público, horarios fijos, paradas o estaciones fijas, boleto de precio fijo.</li>
<li><strong>Solo el autobús:</strong> circula por las calles, depende del tráfico, la mayoría usa diésel o gas, infraestructura sencilla.</li></ul>
<p><em>El metro tiene horarios fijos, al igual que el autobús. El metro no depende del tráfico; en cambio, el autobús sí.</em></p></details>"""

    secciones = [("s1", "Comparar y contrastar", s1), ("s2", "El diagrama de Venn y los conectores", s2), ("s3", "Práctica: el metro y el autobús", s3)]
    tarea = [("Dos cosas de mi vida.", "Elija dos cosas que conozca bien: dos trabajos que tuvo, dos lugares donde vivió, dos comidas o dos medios de transporte."),
             ("Mi diagrama.", "Haga su diagrama de Venn con al menos tres rasgos en cada zona."),
             ("Mi párrafo.", "Escriba un párrafo de cinco oraciones que compare y contraste las dos cosas, con al menos dos conectores de comparación y dos de contraste. Subráyelos.")]
    quiz = [
        ("¿Qué busca <strong>comparar</strong>?", ["Parecidos", "Diferencias"], 0, {}, "<strong>Parecidos.</strong>"),
        ("¿Qué busca <strong>contrastar</strong>?", ["Diferencias", "Parecidos"], 0, {}, "<strong>Diferencias.</strong>"),
        ("En un diagrama de Venn, ¿qué va en el centro?", ["Lo que tienen en común", "Lo que solo tiene A", "Lo que solo tiene B"], 0, {1: "Eso va a la izquierda.", 2: "Eso va a la derecha."}, "Lo que tienen <strong>en común</strong>."),
        ("¿Cuál es un conector de <strong>contraste</strong>?", ["sin embargo", "al igual que", "asimismo"], 0, {1: "Señala un parecido.", 2: "Señala un parecido."}, "<strong>sin embargo</strong>."),
        ("¿Cuál es un conector de <strong>comparación</strong>?", ["así como", "en cambio", "mientras que"], 0, {1: "Señala una diferencia.", 2: "Señala una diferencia."}, "<strong>así como</strong>."),
        ("<em>Yo prefiero el café, mientras que mi esposo prefiere el té.</em>", CC, 1, {}, "<strong>Contraste</strong>: gustos distintos."),
        ("<em>El tigre es un felino, al igual que el león.</em>", CC, 0, {}, "<strong>Comparación</strong>: los dos son felinos."),
        ("Biblioteca y librería: <em>Tiene libros.</em> ¿Dónde va?", ["En común", "Solo la biblioteca", "Solo la librería"], 0, {1: "La librería también tiene libros.", 2: "La biblioteca también tiene libros."}, "<strong>En común.</strong>"),
        ("Según los textos, ¿qué tienen <strong>en común</strong> el metro y el autobús?", ["Tienen horarios fijos", "No los afecta el tráfico", "Funcionan con electricidad"], 0, {1: "Al autobús sí lo afecta.", 2: "La mayoría de los autobuses usa diésel o gas."}, "<strong>Horarios fijos.</strong>"),
        ("¿Por qué es útil comparar y contrastar en el GED?", ["Porque hay preguntas con dos textos sobre el mismo tema", "Porque todas las preguntas son de un solo texto"], 0, {}, "Porque hay preguntas con <strong>dos textos</strong>."),
    ]
    filas = [
        ("Comparar y contrastar", "Encuentro parecidos y diferencias entre dos textos.", "Encuentro las diferencias, pero se me escapan los parecidos.", "No sé por dónde empezar (<a href=\"#s1\">repase la sección 1</a>)."),
        ("Diagrama de Venn", "Pongo cada rasgo en su zona según el texto.", "Me confundo con lo que tienen en común.", "No sé usarlo (<a href=\"#s2\">repase la sección 2</a>)."),
        ("Conectores", "Distingo los conectores de comparación y de contraste.", "Conozco pero y como, pero no los demás.", "No los distingo (<a href=\"#s2\">repase la sección 2</a>)."),
    ]
    cierre = ("<p>Terminó el Tema 5. Ya sabe analizar personajes y escenarios, seguir el orden de los hechos y de las instrucciones, ver las causas y los efectos, y comparar dos textos. Son las relaciones entre ideas que pide la lectura del GED.</p>"
              "<p>En el Tema 6 va a leer información que no está solo en palabras: <strong>imágenes, mapas, tablas y gráficas</strong>.</p>")
    glosario = [("Comparar", "Buscar parecidos."), ("Contrastar", "Buscar diferencias."), ("Diagrama de Venn", "Dos círculos que se cruzan: lo propio de cada uno a los lados y lo común en el centro."),
                ("Conector de contraste", "Palabra que marca una diferencia: pero, sin embargo, en cambio, mientras que.")]
    conexion = ("<p>Ya sabe analizar personajes y escenarios, seguir el orden de los hechos y entender por qué ocurren las cosas. Ahora va a cerrar el tema con una destreza que el GED pide mucho: leer dos textos juntos.</p>"
                "<p><strong>Lo que necesita:</strong> el cuaderno.</p>")
    estd = LE.estandares(["R.9.1/R.7.1", "R.3.4"])
    return C.pagina_leccion(N, LE.titulo(N), "Dos textos, un mismo tema: ¿en qué se parecen y en qué se diferencian?", ["R.9.1 · Comparar textos", "R.3.4 · Contraste"],
                            ["<strong>Distinguir</strong> comparar (parecidos) de contrastar (diferencias).", "<strong>Usar</strong> el diagrama de Venn.",
                             "<strong>Reconocer</strong> los conectores de comparación y de contraste.", "<strong>Comparar</strong> dos textos sobre el mismo tema."],
                            estd, conexion, secciones, tarea, quiz, filas, cierre, ("6-1", LE.titulo("6-1")), glosario, P)


def practica():
    con = [{"enun": f"<strong>{o}</strong><br>¿El conector señala un parecido o una diferencia?", "ops": CC, "ok": k, "enOrden": True, "pista": "",
            "exp": ["Señala un <strong>parecido</strong>: es comparación.", "Señala una <strong>diferencia</strong>: es contraste."][k]} for o, k in CONECT]
    def venn(a, b, rasgos, titulo, intro):
        g = [f"Solo {a}", "Los dos", f"Solo {b}"]
        return {"titulo": titulo, "intro": intro, "grupos": g, "etiqueta": "¿Dónde va?",
                "piezas": [{"t": r, "v": v, "pista": "Pregúntese: ¿lo tiene el primero, el segundo o los dos?"} for r, v in rasgos], "extra": ""}
    ven = [venn(a, b, r, f"{a[0].upper() + a[1:]} y {b}", "Ponga cada rasgo en su zona del diagrama de Venn.") for a, b, r in VENN]
    ven.append(venn("el metro", "el autobús", MB, "El metro y el autobús", "Según los textos de la lección (sección 3), ponga cada rasgo en su zona del diagrama de Venn."))
    mods = [("conectores", "¿Comparar o contrastar?", C.om("m1", "Decida si el conector en cursiva señala un parecido o una diferencia.")),
            ("venn", "El diagrama de Venn", C.clasifica("m2", "Elija para cada rasgo: solo el primero, los dos o solo el segundo. Después pulse <strong>Comprobar</strong>."))]
    js = C.js_datos("CON", con) + C.js_datos("VEN", ven) + 'creaBanco("m1", CON);\ncreaClasifica("m2", VEN);\n'
    return C.pagina_practica(N, LE.titulo(N), "Dos actividades · los ejercicios cambian cada vez · dos intentos en cada uno", mods, js)


if __name__ == "__main__":
    LE.construye(N, leccion, practica, horas="Unas 3 horas")
