# -*- coding: utf-8 -*-
"""LearnGED · Artes del lenguaje (español) · Nivel 1 · Lección 3.6 · Puntuación básica y uso de mayúsculas.
Fuente: clases_leng1/clase_3-6.html (GEDparaHispanos) y sus prácticas de gramatica, adaptadas al marco de LearnGED.
Uso: python3 tools/build_leng1_3_6.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import leng_es as LE
from leng_es import C

LE.nivel(1)
N = "3-6"

MAYUS = ["el *lunes* voy a *chicago* con *maría*.", "*mi* hermano *carlos* estudia en *truman* *college*.", "*nací* en *guatemala* en septiembre.",
         "*hablo* español y estudio inglés en la escuela *lincoln*.", "*la* doctora *ramírez* trabaja en el hospital *mount* *sinai*.",
         "*en* diciembre celebramos la *navidad* con mi tía *rosa*.", "*mi* familia es de *puerto* *rico* y vive en el norte de *texas*.",
         "*el* martes la señora *gómez* llamó desde *miami*.", "*soy* cubano y vivo en *estados* *unidos* desde *2010*.".replace("*2010*", "2010"),
         "*ana* y *luis* viajan a *méxico* en verano."]
MAYUS[0] = "*el* lunes voy a *chicago* con *maría*."
SIGNOS = [("___Dónde vives___", ["¿Dónde vives?", "Dónde vives?", "¿Dónde vives."], 0, "Las preguntas se abren con ¿ y se cierran con ?."),
          ("___Qué bonito día___", ["Qué bonito día!", "¡Qué bonito día!", "¡Qué bonito día."], 1, "Las exclamaciones se abren con ¡ y se cierran con !."),
          ("Compré pan___ leche y queso.", ["Compré pan, leche y queso.", "Compré pan, leche, y queso.", "Compré pan leche y queso."], 0, "Coma entre los elementos de la lista, pero no antes de «y»."),
          ("María___ ven a cenar.", ["María ven a cenar.", "María, ven a cenar.", "María. Ven a cenar."], 1, "Cuando se llama a alguien por su nombre, el nombre va separado por coma."),
          ("Hoy es lunes___ 18 de mayo de 2026.", ["Hoy es lunes, 18 de mayo de 2026.", "Hoy es lunes 18, de mayo de 2026.", "Hoy es, lunes 18 de mayo de 2026."], 0, "En la fecha, la coma va después del día de la semana."),
          ("___Cuándo es el examen___", ["¿Cuándo es el examen?", "¿Cuando es el examen?", "Cuándo es el examen?"], 0, "Se abre y se cierra, y <em>cuándo</em> lleva tilde en las preguntas."),
          ("Después de cenar___ vimos televisión.", ["Después de cenar, vimos televisión.", "Después, de cenar vimos televisión.", "Después de cenar vimos, televisión."], 0, "La coma va después de la frase del comienzo."),
          ("Los estudiantes de la noche___ llegan a las seis.", ["Los estudiantes de la noche, llegan a las seis.", "Los estudiantes de la noche llegan a las seis."], 1, "Nunca se pone coma entre el sujeto y el verbo."),
          ("___Felicidades___", ["¡Felicidades!", "Felicidades!", "¡Felicidades¡"], 0, "Se abre con ¡ y se cierra con !.")]
PARRAFOS = [("Mi mamá", "Mi mamá se llama Luisa y vive en Chicago. Ella trabaja en un hospital. Mi hermano Carlos estudia en Truman College. Quiere ser doctor."),
            ("La clase", "La clase de inglés empieza el lunes. La maestra se llama Ana Torres. Ella es de Puerto Rico. Los estudiantes llegan a las seis."),
            ("El viaje", "Mis padres viajan a México en diciembre. Van a visitar a mi abuela. Ella vive en Guadalajara. Volverán en enero."),
            ("El trabajo nuevo", "Pedro empezó un trabajo nuevo. Trabaja en una fábrica de Texas. Su jefe se llama Mario. Le gusta mucho su trabajo.")]


def leccion():
    P = C.Practicas()
    s1 = f"""<p>Una oración sin mayúscula inicial es como una persona sin zapatos: la idea está, pero falta el detalle que muestra cuidado. Ya vio lo básico en la Lección 1.1; aquí lo completamos.</p>
<h3>Cuándo sí va mayúscula</h3>
<ul><li><strong>La primera palabra de cada oración.</strong> Después de un punto, siempre.</li>
<li><strong>Nombres de personas:</strong> María, Carlos, la doctora Ramírez, mi tía Lucía.</li>
<li><strong>Nombres de lugares:</strong> Chicago, Cuba, México, Truman College.</li>
<li><strong>Lugares con un punto cardinal en el nombre:</strong> América del Sur, Corea del Norte. Solos, los puntos cardinales van con minúscula: <em>el norte de Chicago</em>.</li>
<li><strong>Fiestas:</strong> Navidad, Año Nuevo.</li></ul>
<h3>Cuándo no va mayúscula en español</h3>
{C.tabla("Con minúscula en español (en inglés van con mayúscula)", ["Qué", "Ejemplos"],
         [["Días de la semana", "lunes, martes, miércoles"], ["Meses", "enero, febrero, septiembre"], ["Estaciones", "primavera, verano, otoño, invierno"],
          ["Idiomas y nacionalidades", "español, inglés, cubano, mexicano"], ["Puntos cardinales", "el norte, el sur"]])}
{C.caja("ojo", "Errores frecuentes que vienen del inglés", "<p><s>Yo hablo Español</s> → <strong>Yo hablo español.</strong> · <s>Soy Cubano</s> → <strong>Soy cubano.</strong> · <s>El Lunes voy al doctor</s> → <strong>El lunes voy al doctor.</strong> · <s>Nací en Septiembre</s> → <strong>Nací en septiembre.</strong></p>")}
{P("Compruebe", "¿Qué palabras llevan mayúscula?<br><em>el lunes voy a chicago con maría.</em>", ["el, lunes, chicago", "el, chicago, maría", "lunes, chicago, maría"], 1,
   {0: "El lunes es un día de la semana: minúscula.", 2: "La primera palabra de la oración siempre va con mayúscula."}, "<strong>El</strong> lunes voy a <strong>Chicago</strong> con <strong>María</strong>.")}"""

    s2 = f"""<p>Los signos de puntuación le dicen al lector dónde respirar, dónde detenerse, dónde preguntar y dónde sentir emoción.</p>
{C.tabla("Los signos básicos", ["Signo", "Para qué sirve", "Ejemplo"],
         [["Punto ( . )", "Cierra una oración. Después va mayúscula.", "Mi familia vive en Chicago. Trabajamos mucho."],
          ["Coma ( , )", "Pausa breve: separa los elementos de una lista y la frase del comienzo.", "Compré harina, tomates, queso y pan."],
          ["Interrogación ( ¿ ? )", "Hace preguntas. En español se abre y se cierra.", "¿Dónde vives?"],
          ["Exclamación ( ¡ ! )", "Muestra emoción o sorpresa. Se abre y se cierra.", "¡Qué bonito día!"]])}
<h3>Los usos más comunes de la coma</h3>
<ul><li><strong>Listas:</strong> <em>Tengo dos hermanos, una hermana y un sobrino.</em> Antes de <em>y</em>, en español no se pone coma (en inglés sí, la llamada <em>coma de Oxford</em>).</li>
<li><strong>Frase al comienzo:</strong> <em>Después de terminar el trabajo, voy a la escuela.</em> Si la frase es muy corta, se puede omitir: <em>Hoy voy al trabajo.</em></li>
<li><strong>Fechas:</strong> <em>Hoy es lunes, 18 de mayo de 2026.</em></li>
<li><strong>Para llamar a alguien:</strong> <em>María, ¿puedes venir?</em></li></ul>
{C.caja("ojo", "Nunca entre el sujeto y el verbo", "<p><s>Los estudiantes de la noche, llegan a las seis.</s> → <strong>Los estudiantes de la noche llegan a las seis.</strong> Aunque el sujeto sea largo y uno haga una pausa al hablar, por escrito no lleva coma. Es una de las trampas del examen GED.</p>")}
{P("Compruebe", "¿Cuál está bien escrita?", ["Compré pan, leche, y queso.", "Compré pan, leche y queso.", "Compré pan leche y queso."], 1,
   {0: "Antes de «y» no va coma en español.", 2: "Entre pan y leche hace falta una coma."}, "<strong>Compré pan, leche y queso.</strong>")}"""

    s3 = f"""<h3>Editor: ponga mayúsculas y signos</h3>
<p>Este párrafo está todo en minúsculas y sin puntuación. Reescríbalo en el cuadro con mayúsculas, puntos y comas. Después compárelo con el modelo.</p>
<div class="texto-lectura"><p>mi mamá se llama luisa y vive en chicago ella trabaja en un hospital los lunes martes y miércoles mi hermano carlos estudia en truman college quiere ser doctor</p></div>
<p><label for="editor36"><strong>Su versión:</strong></label></p>
<textarea id="editor36" rows="5" style="width:100%;font:inherit;font-size:1.1em;padding:10px;border-radius:10px;border:2px solid #b9c5d0"></textarea>
<details class="caja caja-tip"><summary><strong>Ver el modelo (después de intentarlo)</strong></summary>
<p>Mi mamá se llama Luisa y vive en Chicago. Ella trabaja en un hospital los lunes, martes y miércoles. Mi hermano Carlos estudia en Truman College. Quiere ser doctor.</p>
<ul><li>Mayúscula al inicio de cada oración (<em>Mi, Ella, Mi, Quiere</em>).</li><li>Mayúscula en los nombres propios (<em>Luisa, Carlos, Truman College, Chicago</em>).</li>
<li>Punto al final de cada idea.</li><li>Comas en la lista de días, sin coma antes de <em>y</em>; los días, en minúscula.</li></ul></details>
<p>En la <a href="{C.prac(N)}">página de práctica</a> tiene más: dónde va la mayúscula, qué signo va y dónde empieza cada oración.</p>"""

    secciones = [("s1", "Uso de las mayúsculas", s1), ("s2", "La puntuación básica", s2), ("s3", "Práctica: corrija un párrafo", s3)]
    tarea = [("Cinco oraciones.", "Escriba una que afirme algo, una pregunta, una exclamación, una con una lista separada por comas y una con una fecha (<em>Hoy es martes, 6 de octubre de 2026.</em>)."),
             ("Un papel de la casa.", "Busque una nota, una lista o un mensaje escrito y revise sus mayúsculas y sus signos. Si encuentra errores, cópielo corregido."),
             ("Mi propia revisión.", "Revise sus cinco oraciones: ¿empiezan con mayúscula?, ¿terminan con el signo adecuado?, ¿abrió y cerró la pregunta y la exclamación?, ¿puso bien la coma en la lista y en la fecha?")]
    quiz = [
        ("¿Cuál está bien escrita?", ["Yo hablo Español.", "Yo hablo español."], 1, {}, "<strong>Yo hablo español.</strong> Los idiomas van con minúscula."),
        ("¿Cuál está bien escrita?", ["Nací en septiembre.", "Nací en Septiembre."], 0, {}, "<strong>Nací en septiembre.</strong> Los meses van con minúscula."),
        ("¿Cuál está bien escrita?", ["Vivo en el Norte de Chicago.", "Vivo en el norte de Chicago."], 1, {}, "<strong>el norte</strong>: el punto cardinal solo va con minúscula."),
        ("¿Qué lleva mayúscula?", ["navidad", "lunes", "verano"], 0, {1: "Los días van con minúscula.", 2: "Las estaciones van con minúscula."}, "<strong>Navidad</strong>: las fiestas llevan mayúscula."),
        ("¿Cómo se escribe una pregunta en español?", ["Dónde está la escuela?", "¿Dónde está la escuela?", "¿Dónde está la escuela¿"], 1, {0: "Falta el signo de apertura.", 2: "Al final va el signo de cierre: ?"}, "<strong>¿Dónde está la escuela?</strong>"),
        ("¿Cómo se escribe una exclamación?", ["¡Qué alegría!", "Qué alegría!", "¡Qué alegría¡"], 0, {1: "Falta el signo de apertura.", 2: "Al final va el de cierre: !"}, "<strong>¡Qué alegría!</strong>"),
        ("¿Dónde va la coma?<br><em>Compré pan leche y queso.</em>", ["Después de pan", "Después de leche", "Después de queso"], 0, {1: "Antes de y no va coma.", 2: "Al final va el punto."}, "<strong>Compré pan, leche y queso.</strong>"),
        ("¿Cuál está bien escrita?", ["María ven aquí.", "María, ven aquí."], 1, {}, "<strong>María, ven aquí.</strong> El nombre de la persona a quien se habla va con coma."),
        ("¿Cuál está bien escrita?", ["Mi jefe, llegó temprano.", "Mi jefe llegó temprano."], 1, {}, "<strong>Mi jefe llegó temprano.</strong> No va coma entre el sujeto y el verbo."),
        ("¿Qué va después de un punto?", ["Mayúscula", "Minúscula", "Coma"], 0, {1: "Después de punto empieza otra oración.", 2: "Después de punto no va coma."}, "<strong>Mayúscula</strong>."),
        ("¿Para qué sirve la coma?", ["Para una pausa breve y para separar los elementos de una lista", "Para terminar la oración", "Para hacer preguntas"], 0, {1: "Eso lo hace el punto.", 2: "Eso lo hacen ¿ ?."}, "Para una <strong>pausa breve</strong> y para separar listas."),
        ("¿Cuál está bien escrita?", ["Mi tía Rosa vive en Puerto Rico.", "Mi Tía rosa vive en puerto Rico.", "mi tía Rosa vive en Puerto Rico."], 0, {1: "Tía es común; Rosa y Puerto Rico son propios.", 2: "La oración empieza con mayúscula."}, "<strong>Mi tía Rosa vive en Puerto Rico.</strong>"),
    ]
    filas = [
        ("Mayúsculas", "Pongo mayúscula al inicio y en nombres propios, y minúscula en días, meses, idiomas y nacionalidades.", "A veces pongo mayúscula en un día o un idioma.", "Las pongo al azar (<a href=\"#s1\">repase la sección 1</a>)."),
        ("Signos dobles", "Abro y cierro siempre las preguntas y las exclamaciones.", "A veces olvido el de apertura.", "No los uso (<a href=\"#s2\">repase la sección 2</a>)."),
        ("La coma", "Uso la coma en listas, fechas y frases del comienzo, y nunca entre sujeto y verbo.", "Pongo coma antes de «y».", "No sé dónde va (<a href=\"#s2\">repase la sección 2</a>)."),
    ]
    cierre = ("<p>Terminó el Tema 3. Conoció a los sustantivos y los adjetivos y su concordancia, descubrió que el verbo es el corazón de la oración y que dice cuándo pasan las cosas, aprendió a distinguir oraciones completas de fragmentos y ya domina la mecánica básica: mayúsculas, puntos, comas y signos dobles. Todo esto lo evalúa el examen GED en sus preguntas de corrección y en la respuesta escrita.</p>"
              "<p>En el Tema 4 cambia de tarea: va a aprender estrategias para <strong>entender</strong> mejor lo que lee, empezando por predecir y preguntar antes de leer.</p>")
    glosario = [("Signos dobles", "¿ ? y ¡ !: en español se abren y se cierran."), ("Coma de Oxford", "Coma antes de «y» en una lista; se usa en inglés, no en español."),
                ("Vocativo", "El nombre de la persona a quien se habla; va con coma: <em>María, ven.</em>"), ("Punto cardinal", "Norte, sur, este, oeste; van con minúscula si están solos.")]
    conexion = ("<p>Ya sabe escribir oraciones completas. Falta vestirlas bien para salir a la calle: mayúsculas donde tocan, punto al final, comas en su lugar y signos de pregunta y exclamación que abren y cierran.</p>"
                "<p><strong>Lo que necesita:</strong> el cuaderno y algún papel escrito de su casa (una nota, una lista, un mensaje).</p>")
    estd = LE.estandares(["L.2.1", "L.2.4"], base=["L.2.2"])
    return C.pagina_leccion(N, LE.titulo(N), "Mayúscula al empezar, signo al terminar.", ["L.2.1 · Mayúsculas", "L.2.4 · Puntuación"],
                            ["<strong>Usar</strong> la mayúscula al inicio de la oración y en los nombres propios, y la minúscula donde la pide el español.",
                             "<strong>Abrir y cerrar</strong> las preguntas y las exclamaciones.", "<strong>Poner</strong> la coma en listas, fechas, frases del comienzo y al llamar a alguien.",
                             "<strong>Evitar</strong> la coma entre el sujeto y el verbo."],
                            estd, conexion, secciones, tarea, quiz, filas, cierre, ("4-1", LE.titulo("4-1")), glosario, P)


# ---------------------------------------------------------------- práctica
def banco_mayus():
    return [{"consigna": "Toque las palabras que deben ir con <strong>mayúscula</strong>.", "texto": x, "mayus": True,
             "pista": "Primera palabra de la oración y nombres propios. Días, meses, idiomas y nacionalidades van con minúscula.", "exp": ""} for x in MAYUS]


def banco_signos():
    return [{"enun": f"¿Cuál está bien escrita?", "ops": o, "ok": k, "pista": "Revise los signos de apertura y de cierre, y dónde van las comas.", "exp": f"<strong>{o[k]}</strong> {e}"} for _, o, k, e in SIGNOS]


def practica():
    mods = [
        ("mayusculas", "¿Dónde va la mayúscula?", LE.marcar("m1", "La oración está toda en minúsculas. Toque las palabras que deben ir con mayúscula: la página se la pone.")),
        ("signos", "Signos y comas", C.om("m2", "Elija la forma bien escrita.")),
        ("limites", "Mayúscula al inicio, punto al final", '      <p>Toque la <strong>primera palabra de cada oración</strong> (menos la primera del párrafo): la página le pone la mayúscula y el punto. Los nombres propios ya tienen su mayúscula.</p>\n' + C.huecos("m3")),
    ]
    js = (C.js_datos("MAY", banco_mayus()) + C.js_datos("SIG", banco_signos()) + C.js_datos("PAR", [{"titulo": a, "correcto": b} for a, b in PARRAFOS]) +
          'creaMarcar("m1", MAY);\ncreaBanco("m2", SIG);\ncreaLimites("m3", PAR);\n')
    return C.pagina_practica(N, LE.titulo(N), "Tres actividades · los ejercicios cambian cada vez · dos intentos en cada uno", mods, js)


if __name__ == "__main__":
    LE.construye(N, leccion, practica, horas="Unas 3 horas")
