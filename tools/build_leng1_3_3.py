# -*- coding: utf-8 -*-
"""LearnGED · Artes del lenguaje (español) · Nivel 1 · Lección 3.3 · El verbo.
Fuente: clases_leng1/clase_3-3.html (GEDparaHispanos), adaptada al marco de LearnGED.
Uso: python3 tools/build_leng1_3_3.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import leng_es as LE
from leng_es import C

LE.nivel(1)
N = "3-3"

# Oraciones con el verbo marcado con * y su tipo (a = acción, e = enlace)
ORACIONES = [("María *cocina* arroz.", "a"), ("El niño *corre* en el parque.", "a"), ("Mi mamá *es* doctora.", "e"), ("El café *está* caliente.", "e"),
             ("Nicolás *trabaja* en una fábrica.", "a"), ("Los estudiantes *escriben* en sus cuadernos.", "a"), ("La sopa *está* caliente.", "e"),
             ("Mi hermana *es* enfermera.", "e"), ("Usted *parece* cansado.", "e"), ("Mi vecino *canta* en la iglesia.", "a"), ("Los perros *ladran* de noche.", "a"),
             ("La maestra *parece* contenta.", "e"), ("Yo *estudio* después del trabajo.", "a"), ("Las flores *son* amarillas.", "e"), ("Mi jefe *llega* temprano.", "a"),
             ("El examen *fue* difícil.", "e"), ("Ana *lava* los platos.", "a"), ("Mis hijos *están* contentos.", "e"), ("El autobús *sale* a las seis.", "a"), ("Tú *eres* muy amable.", "e")]


def marca(o):
    """Oración con el verbo en doble subrayado."""
    return o.replace("*", "<u class=\"verbo\">", 1).replace("*", "</u>", 1)


def leccion():
    P = C.Practicas()
    s1 = f"""<p>El sustantivo es el protagonista. Pero un protagonista quieto, sin hacer nada, no cuenta ninguna historia. Aquí entra el <strong>verbo</strong>: la palabra que dice <strong>qué hace</strong> el sujeto, o <strong>cómo es</strong> o <strong>cómo está</strong>. El verbo es el corazón de la oración: <strong>sin verbo no hay oración</strong>.</p>
<p class="oracion-ej">{marca("María *cocina* arroz.")}</p>
<p class="oracion-ej">{marca("El niño *corre* en el parque.")}</p>
<p class="oracion-ej">{marca("Mi mamá *es* doctora.")}</p>
<p class="oracion-ej">{marca("El café *está* caliente.")}</p>
<p class="nota-fina">A mano se acostumbra subrayar el verbo con <strong>doble raya</strong>, como aquí.</p>
{C.caja("tip", "Pista de oro", "<p>Para encontrar el verbo, pregunte: <strong>¿qué hace el sujeto?</strong> o <strong>¿cómo es o cómo está?</strong> La palabra que responde es el verbo. Otra pista: el verbo cambia si cambia la persona o el tiempo (<em>cocino, cocinas, cocinó, cocinará</em>); los sustantivos no.</p>")}
{P("Compruebe", f"¿Cuál es el verbo?<br><em>Mi vecino canta en la iglesia.</em>", ["vecino", "canta", "iglesia"], 1,
   {0: "Vecino es quien lo hace: el sujeto.", 2: "Iglesia es el lugar: un sustantivo."}, "<strong>canta</strong>: es lo que hace el vecino.")}"""

    s2 = f"""<h3>Verbos de acción</h3>
<p>Dicen algo que el sujeto <strong>hace</strong>: <em>correr, comer, escribir, cantar, leer, trabajar, estudiar, dormir</em>.</p>
<p class="oracion-ej">{marca("Nicolás *trabaja* en una fábrica.")}</p>
<p class="oracion-ej">{marca("Los estudiantes *escriben* en sus cuadernos.")}</p>
<h3>Verbos de enlace</h3>
<p>No muestran una acción: <strong>unen</strong> al sujeto con una descripción. Los principales son <strong>ser</strong>, <strong>estar</strong> y <strong>parecer</strong>. También se llaman <em>copulativos</em>.</p>
<p class="oracion-ej">{marca("La sopa *está* caliente.")}</p>
<p class="oracion-ej">{marca("Mi hermana *es* enfermera.")}</p>
<p class="oracion-ej">{marca("Usted *parece* cansado.")}</p>
{C.tabla("Verbos de acción y de enlace", ["Tipo", "Qué hace", "Ejemplos"],
         [["De acción", "Muestra lo que hace el sujeto.", "correr, comer, hablar, escribir, dormir, trabajar, estudiar, cantar"],
          ["De enlace", "Une al sujeto con una descripción.", "ser, estar, parecer"]])}
{C.caja("ojo", "Ser y estar", "<p><strong>Ser</strong> suele decir cómo es algo de forma estable (<em>Mi hermana es enfermera</em>); <strong>estar</strong>, cómo está en un momento (<em>Hoy está cansada</em>). <em>Estar</em> también dice dónde está algo: <em>El libro está en la mesa.</em></p>")}
{P("Compruebe", f"En <em>{marca('Tú *pareces* cansado.')}</em>, el verbo es…", ["de acción", "de enlace"], 1, {},
   "<strong>De enlace</strong>: <em>pareces</em> no es algo que se hace; une a «tú» con «cansado».")}
{P("Compruebe", f"En <em>{marca('Ana *lava* los platos.')}</em>, el verbo es…", ["de acción", "de enlace"], 0, {},
   "<strong>De acción</strong>: lavar es algo que Ana hace.")}"""

    s3 = f"""<p>En la <a href="{C.prac(N)}#verbo">página de práctica</a> va a tocar el verbo de muchas oraciones y a decidir si es de acción o de enlace. Antes, pruebe con estas:</p>
{P("Compruebe", "¿Cuál es el verbo?<br><em>Los perros ladran de noche.</em>", ["perros", "ladran", "noche"], 1, {0: "Perros es el sujeto.", 2: "Noche dice cuándo."}, "<strong>ladran</strong>.")}
{P("Compruebe", "¿Cuál es el verbo?<br><em>El examen fue difícil.</em>", ["examen", "fue", "difícil"], 1, {0: "Examen es el sujeto.", 2: "Difícil dice cómo fue: es un adjetivo."}, "<strong>fue</strong> (del verbo <em>ser</em>): un verbo de enlace.")}
<div class="caja caja-tip"><span class="etiqueta et-verde">Actividad · en su cuaderno</span>
<p>Escriba 5 oraciones sobre lo que hace en un día normal y subraye el verbo con doble raya (<em>Me levanto a las seis. Preparo el café.</em>). Después escriba una con <em>ser</em>, una con <em>estar</em> y una con <em>parecer</em>.</p></div>"""

    secciones = [("s1", "¿Qué es el verbo?", s1), ("s2", "Verbos de acción y verbos de enlace", s2), ("s3", "Práctica: encuentre el verbo", s3)]
    tarea = [("Mi día en verbos.", "Escriba 5 oraciones con verbos de acción sobre su día. Subraye el verbo con doble raya."),
             ("Cómo soy, cómo estoy.", "Escriba 3 oraciones con verbos de enlace: una con <em>ser</em>, una con <em>estar</em> y una con <em>parecer</em> (<em>Soy trabajador. Hoy estoy cansado. Mi jefe parece contento.</em>)."),
             ("Verbos en la cocina.", "Busque una receta y copie 5 verbos de acción (<em>mezcle, corte, hierva…</em>).")]
    quiz = [
        ("¿Qué dice el <strong>verbo</strong>?", ["Qué hace el sujeto, o cómo es o cómo está", "Cómo se llama una cosa", "Cuántas cosas hay"], 0, {1: "Eso lo dice el sustantivo.", 2: "Eso lo dicen los números."}, "El verbo dice <strong>qué hace</strong> o <strong>cómo es o está</strong> el sujeto."),
        ("¿Puede haber una oración sin verbo?", ["Sí", "No"], 1, {}, "<strong>No</strong>: sin verbo no hay oración completa."),
        ("¿Cuál es el verbo?<br><em>Yo estudio después del trabajo.</em>", ["Yo", "estudio", "trabajo"], 1, {0: "Yo es el sujeto.", 2: "Aquí «trabajo» va con «el»: es un sustantivo."}, "<strong>estudio</strong>."),
        ("¿Cuál es el verbo?<br><em>Las flores son amarillas.</em>", ["flores", "son", "amarillas"], 1, {0: "Flores es el sujeto.", 2: "Amarillas es un adjetivo."}, "<strong>son</strong>."),
        ("¿Cuál es un verbo de enlace?", ["correr", "estar", "comer"], 1, {0: "Correr es una acción.", 2: "Comer es una acción."}, "<strong>estar</strong>, como <em>ser</em> y <em>parecer</em>."),
        ("¿Cuál es un verbo de acción?", ["ser", "parecer", "escribir"], 2, {0: "Ser es de enlace.", 1: "Parecer es de enlace."}, "<strong>escribir</strong>."),
        ("En <em>Mi mamá es doctora</em>, el verbo es…", ["de acción", "de enlace"], 1, {}, "<strong>De enlace</strong>: une a «mi mamá» con «doctora»."),
        ("En <em>El autobús sale a las seis</em>, el verbo es…", ["de acción", "de enlace"], 0, {}, "<strong>De acción</strong>: salir es algo que el autobús hace."),
        ("¿Qué pregunta ayuda a encontrar el verbo?", ["¿Qué hace el sujeto?", "¿De qué color es?", "¿Cuántos son?"], 0, {1: "Esa busca un adjetivo.", 2: "Esa busca un número."}, "<strong>¿Qué hace el sujeto?</strong> (o ¿cómo es o está?)."),
        ("¿Qué palabra <strong>cambia</strong> si decimos la oración en pasado?<br><em>Ana lava los platos.</em>", ["Ana", "lava", "platos"], 1, {0: "El nombre no cambia con el tiempo.", 2: "Los platos siguen siendo platos."}, "<strong>lava → lavó</strong>: el verbo cambia con el tiempo."),
        ("<em>Hoy estoy cansado.</em> ¿Qué verbo usa?", ["ser", "estar", "parecer"], 1, {0: "«Estoy» viene de otro verbo.", 2: "«Estoy» no es de parecer."}, "<strong>estar</strong>: cómo está en un momento."),
        ("¿Cuántos verbos hay?<br><em>Llego a casa y preparo la cena.</em>", ["1", "2", "3"], 1, {0: "Busque todas las acciones.", 2: "Casa y cena son sustantivos."}, "<strong>2</strong>: llego y preparo."),
    ]
    filas = [
        ("Encontrar el verbo", "Encuentro el verbo de cualquier oración sencilla, aunque haya dos.", "Lo encuentro cuando va justo después del sujeto.", "Lo confundo con el sustantivo (<a href=\"#s1\">repase la sección 1</a>)."),
        ("Acción o enlace", "Distingo los verbos de acción de ser, estar y parecer.", "Dudo con estar.", "No los distingo (<a href=\"#s2\">repase la sección 2</a>)."),
        ("Ser y estar", "Uso ser para lo estable y estar para el momento o el lugar.", "A veces los cambio.", "Los confundo seguido (<a href=\"#s2\">repase la sección 2</a>)."),
    ]
    cierre = "<p>Ya conoce el corazón de la oración. En la próxima lección verá su superpoder: el verbo no solo dice qué pasa, también dice <strong>cuándo</strong> pasa: ayer, hoy o mañana.</p>"
    glosario = [("Verbo", "Palabra que dice qué hace el sujeto, o cómo es o cómo está."), ("Verbo de acción", "El que dice algo que el sujeto hace: <em>corre, escribe</em>."),
                ("Verbo de enlace (copulativo)", "Une al sujeto con una descripción: <em>ser, estar, parecer</em>."), ("Doble subrayado", "Manera de marcar el verbo a mano: con dos rayas.")]
    conexion = ("<p>Ya sabe que el sustantivo es el protagonista y que el adjetivo le pone color. Hoy conoce al tercer actor, el más importante: el verbo.</p>"
                "<p><strong>Lo que necesita:</strong> el cuaderno y una receta de cocina (de un empaque, un libro o internet).</p>")
    estd = LE.estandares([], base=["L.1.2", "L.2.2"])
    return C.pagina_leccion(N, LE.titulo(N), "Sin verbo no hay oración.", ["Gramática", "L.2.2 · Oraciones completas"],
                            ["<strong>Reconocer</strong> el verbo de una oración preguntando ¿qué hace? o ¿cómo es o está?", "<strong>Distinguir</strong> los verbos de acción de los de enlace (ser, estar, parecer).",
                             "<strong>Usar</strong> ser y estar según lo que se quiere decir.", "<strong>Marcar</strong> el verbo con doble subrayado."],
                            estd, conexion, secciones, tarea, quiz, filas, cierre, ("3-4", LE.titulo("3-4")), glosario, P)


# ---------------------------------------------------------------- práctica
def banco_marcar():
    return [{"consigna": "Toque el <strong>verbo</strong>.", "texto": o, "pista": "Pregunte: ¿qué hace el sujeto?, ¿cómo es?, ¿cómo está?",
             "exp": "El verbo es de " + ("acción." if t == "a" else "enlace.")} for o, t in ORACIONES] + [
        {"consigna": "Toque los <strong>dos verbos</strong>.", "texto": x, "pista": "Hay dos acciones o dos enlaces.", "exp": ""}
        for x in ["Llego a casa y *preparo* la cena.".replace("Llego", "*Llego*"), "Mi hijo *estudia* y *trabaja*.", "Ella *es* alta y *corre* rápido.", "*Lavo* la ropa y *limpio* la cocina."]]


def banco_tipo():
    return [{"enun": f"<em>{marca(o)}</em><br>¿El verbo es de acción o de enlace?", "ops": ["De acción", "De enlace"], "ok": 0 if t == "a" else 1, "enOrden": True,
             "exp": ("Es algo que el sujeto <strong>hace</strong>." if t == "a" else "No es algo que se hace: <strong>une</strong> al sujeto con una descripción (ser, estar, parecer).")} for o, t in ORACIONES]


def banco_completa():
    datos = [("Mi hermana ", ["es", "corre", "come"], 0, " enfermera.", "Con «enfermera» hace falta un verbo de enlace."),
             ("El perro ", ["está", "ladra", "es"], 1, " toda la noche.", "¿Qué hace el perro toda la noche?"),
             ("Hoy yo ", ["estoy", "soy", "parece"], 0, " cansado.", "Cansado es cómo está ahora."),
             ("Los niños ", ["juegan", "son", "están"], 0, " en el parque.", "¿Qué hacen en el parque?"),
             ("La sopa ", ["está", "es", "come"], 0, " fría.", "Fría es cómo está en este momento."),
             ("Mi papá ", ["trabaja", "está", "es"], 0, " en una fábrica.", "¿Qué hace en la fábrica?"),
             ("Usted ", ["parece", "corre", "come"], 0, " preocupado.", "Preocupado es una descripción: hace falta un enlace."),
             ("El libro ", ["está", "es", "lee"], 0, " en la mesa.", "Para decir dónde está algo se usa estar.")]
    return [{"partes": [a, {"ops": o, "ok": k}, b], "pista": pi, "exp": f"<strong>{a}{o[k]}{b}</strong>"} for a, o, k, b, pi in datos]


def practica():
    mods = [
        ("verbo", "Toque el verbo", LE.marcar("m1", "Toque el verbo de la oración (a veces son dos). Si se equivoca, vuelva a tocar la palabra para quitar la marca.")),
        ("tipo", "¿Acción o enlace?", C.om("m2", "¿El sujeto hace algo, o el verbo solo lo une con una descripción?")),
        ("completar", "Complete con el verbo", C.huecos("m3", "Elija en el menú el verbo que completa la oración.")),
    ]
    js = (C.js_datos("VER", banco_marcar()) + C.js_datos("TIP", banco_tipo()) + C.js_datos("COM", banco_completa()) +
          'creaMarcar("m1", VER);\ncreaBanco("m2", TIP);\ncreaHuecos("m3", COM);\n')
    return C.pagina_practica(N, LE.titulo(N), "Tres actividades · los ejercicios cambian cada vez · dos intentos en cada uno", mods, js)


if __name__ == "__main__":
    LE.construye(N, leccion, practica, horas="Unas 3 horas")
