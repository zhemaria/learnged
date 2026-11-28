# -*- coding: utf-8 -*-
"""LearnGED · Artes del lenguaje (español) · Nivel 1 · Lección 7.4 · El texto de opinión y la comparación de los tres tipos.
Fuente: clases_leng1/clase_7-4.html (GEDparaHispanos) y gramatica/n1-l7-4.html, adaptadas al marco de LearnGED.
Corrección respecto de la fuente: la respuesta extendida del GED no pide la opinión personal del estudiante, sino decidir qué
argumento de dos textos está mejor apoyado por la evidencia. Se dice así en la lección.
Uso: python3 tools/build_leng1_7_4.py
"""
import os, sys, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import leng_es as LE
from leng_es import C

LE.nivel(1)
N = "7-4"
TIPOS = ["Narrativo", "Informativo", "De opinión"]
TEXTOS = [("Ayer fui al mercado con mi hija. Primero compramos fruta. Después tomamos un café. Al final volvimos a casa en autobús.", 0),
          ("El sábado pasado se fue la luz en todo el barrio. Esa noche cenamos con velas. Más tarde, los vecinos salieron a la calle a conversar.", 0),
          ("Cuando llegué a Chicago, no conocía a nadie. Al principio trabajé limpiando oficinas. Luego conseguí un puesto en una panadería.", 0),
          ("Esta mañana se me hizo tarde. Primero no sonó la alarma. Después perdí el autobús. Finalmente llegué al trabajo a las diez.", 0),
          ("El año pasado mi familia viajó a México. Visitamos a mis abuelos y fuimos a la playa. Regresamos con muchas fotos.", 0),
          ("El corazón es un músculo del tamaño de un puño. Bombea sangre a todo el cuerpo. Late unas cien mil veces al día.", 1),
          ("Los Grandes Lagos son cinco. El lago Michigan es el único que está completamente dentro de los Estados Unidos.", 1),
          ("El examen GED tiene cuatro materias: Razonamiento a través de las Artes del Lenguaje, Matemáticas, Ciencias y Estudios Sociales.", 1),
          ("El agua hierve a 100 °C al nivel del mar. A mayor altitud, hierve a una temperatura más baja.", 1),
          ("La Habana es la capital de Cuba. Está en la costa norte de la isla.", 1),
          ("Creo que todas las escuelas deberían tener un huerto. Los niños aprenden de dónde viene la comida. Además, comen más verduras.", 2),
          ("En mi opinión, la ciudad debería poner más luces en los parques. Así serían más seguros de noche. Por eso, apoyo la propuesta.", 2),
          ("Me parece que leer antes de dormir es el mejor hábito. Relaja la mente y ayuda a dormir. Por estas razones, lo recomiendo.", 2),
          ("Pienso que el transporte público debería ser gratis para los mayores. Muchos viven con poco dinero. Además, así salen más de casa.", 2),
          ("Considero que aprender un segundo idioma es una gran inversión. Abre puertas en el trabajo y en la vida.", 2)]
PISTA_TIPO = ["cuenta sucesos en orden, en pasado", "da hechos que se pueden comprobar, en presente", "dice lo que piensa el autor y da razones"]
HECHO = [("El lago Michigan está en el norte de los Estados Unidos.", True), ("El lago Michigan es el lugar más bonito para pasear.", False), ("Chicago tiene cuatro estaciones bien marcadas.", True),
         ("El invierno de Chicago es insoportable.", False), ("El maíz se cultiva desde hace miles de años.", True), ("Las tortillas de maíz son las más ricas.", False),
         ("La biblioteca presta libros gratis.", True), ("La biblioteca debería abrir los domingos.", False), ("El café tiene cafeína.", True), ("El café de mi abuela es el mejor del mundo.", False),
         ("Miami está en el estado de Florida.", True), ("Miami es una ciudad demasiado calurosa para vivir.", False), ("El agua se congela a 0 °C.", True), ("Bañarse con agua fría es lo más saludable.", False),
         ("El GED tiene cuatro materias.", True), ("Matemáticas es la materia más difícil del GED.", False)]
PARTES = ["La opinión", "Una razón", "La conclusión"]
# Párrafos de opinión: (opinión, razón 1, razón 2, conclusión)
OPINIONES = [("El transporte público de Chicago me parece muy útil para los trabajadores.", "Esto se debe a que algunas líneas funcionan las veinticuatro horas y conectan los barrios con el centro.",
              "Además, cuesta menos que mantener un carro propio.", "Por estas razones, considero que es un servicio indispensable."),
             ("Creo que todas las escuelas deberían tener un huerto.", "Los niños aprenden de dónde viene la comida.", "Además, cuando siembran sus verduras, se animan a comerlas.", "Por eso, apoyo que cada escuela tenga el suyo."),
             ("En mi opinión, estudiar de adulto vale la pena.", "La razón es que abre puertas a mejores trabajos.", "También da un buen ejemplo a los hijos.", "En conclusión, nunca es tarde para volver a estudiar."),
             ("Me parece que la biblioteca debería abrir los domingos.", "Muchas personas trabajan de lunes a sábado.", "Además, el domingo las familias tienen tiempo para leer juntas.", "Por lo tanto, abrir ese día ayudaría a toda la comunidad."),
             ("Pienso que caminar es el mejor ejercicio para empezar.", "No cuesta dinero ni necesita equipo especial.", "Por otra parte, se puede hacer en cualquier barrio.", "Por eso, recomiendo caminar media hora al día.")]


def coloreado(o, r1, r2, c):
    nom = [("op-op", "Opinión"), ("op-ra", "Razón"), ("op-ra", "Razón"), ("op-ci", "Conclusión")]
    return '<p class="hamb-par">' + " ".join(f'<span class="{k}"><span class="cap-oculto">{n}: </span>{x}</span>' for (k, n), x in zip(nom, [o, r1, r2, c])) + "</p>"


def leccion():
    P = C.Practicas()
    s1 = f"""<p>Un texto <strong>de opinión</strong> presenta lo que el autor piensa sobre un tema y lo <strong>defiende con razones</strong>. Está en los editoriales, las reseñas, las cartas a una empresa o al gobierno y los ensayos.</p>
{C.tabla("Los cuatro escalones del texto de opinión", ["Escalón", "Pregunta", "Ejemplo"],
         [["🎯 1 · Presentar el tema", "¿De qué voy a opinar?", "«El transporte público de Chicago…»"], ["💭 2 · Dar una opinión clara", "¿Qué pienso?", "«…me parece muy útil para los trabajadores.»"],
          ["🔗 3 · Dar razones", "¿Por qué lo pienso?", "«Algunas líneas funcionan las 24 horas y conectan los barrios con el centro.»"], ["✅ 4 · Concluir", "¿Cómo cierro?", "«Por eso, considero que es un servicio indispensable.»"]])}
<p class="hamb-ley"><span class="op-op">Opinión</span> <span class="op-ra">Razones</span> <span class="op-ci">Conclusión</span></p>
{coloreado(*OPINIONES[0])}
{C.tabla("Frases útiles", ["Para…", "Frases"],
         [["Dar la opinión", "Pienso que… · Creo que… · En mi opinión… · Me parece que…"], ["Dar una razón", "porque… · Esto se debe a… · La razón es que… · Por ejemplo…"],
          ["Añadir otra razón", "Además… · También… · Por otra parte…"], ["Cerrar", "Por eso… · Por estas razones… · En conclusión… · Por lo tanto…"]])}
{C.caja("ojo", "Sin razón no hay argumento", "<p>«Me gusta» es solo un gusto. Con un <strong>porqué</strong>, la opinión se convierte en un <strong>argumento</strong>.</p>")}
{C.caja("tip", "¿Y la respuesta extendida del GED?", "<p>Ojo: en el ensayo del GED <strong>no se pide su opinión personal</strong>. Se leen dos textos con posiciones opuestas y hay que explicar <strong>cuál argumento está mejor apoyado por la evidencia</strong>. Lo que aprende aquí —opinión clara, razones y conclusión— es la base para eso, pero allí las razones salen de los textos, no de sus gustos.</p>")}"""

    s2 = f"""{C.tabla("Los tres tipos de texto, lado a lado", ["", "📖 Narrativo", "📊 Informativo", "💭 De opinión"],
         [["Pregunta", "¿Qué pasó?", "¿Qué es?", "¿Qué pienso?"], ["Propósito", "Contar", "Informar", "Convencer"], ["Tiempo verbal típico", "Pasado", "Presente", "Presente"],
          ["Palabras clave", "primero, luego, después, finalmente", "es, tiene, contiene, se encuentra", "creo que, me parece, en mi opinión"],
          ["Tono", "Personal", "Neutro, objetivo", "Personal, con razones"], ["Dónde se ve", "Anécdotas, cuentos", "Enciclopedias, manuales", "Editoriales, reseñas"]])}
<h3>La familia, de tres maneras</h3>
<div class="texto-lectura"><p><strong>📖 Narrativo.</strong> El domingo pasado mi familia se reunió en casa. Primero, llegaron mis hijos con sus esposas. Luego, mi hermana trajo el postre. Después, almorzamos arroz con frijoles y conversamos toda la tarde. Finalmente, todos se despidieron contentos.</p></div>
<div class="texto-lectura"><p><strong>📊 Informativo.</strong> Mi familia está formada por seis personas. Tres viven en Chicago y tres en Miami. Nos reunimos dos veces al año, en Navidad y en el cumpleaños de mi madre. Todos hablamos español como primer idioma.</p></div>
<div class="texto-lectura"><p><strong>💭 De opinión.</strong> La familia es lo más importante de mi vida. Creo que es el lugar donde uno aprende los valores más profundos. Mis hijos, por ejemplo, aprendieron el respeto y la honestidad porque en casa siempre se dio el ejemplo. Por eso, considero que cuidar la familia es la mejor inversión.</p></div>
{C.caja("tip", "Lo que cambia", "<p>El tema es el mismo; lo que cambia es el <strong>propósito</strong> del autor.</p>")}
{P("Compruebe", "<em>Considero que aprender un segundo idioma es una gran inversión. Abre puertas en el trabajo y en la vida.</em> ¿Qué tipo de texto es?", TIPOS, 2,
   {0: "No cuenta sucesos.", 1: "«Considero que» marca una opinión."}, "<strong>De opinión</strong>: da un punto de vista y una razón.")}"""

    s3 = f"""<p>Elija <strong>un</strong> tipo de texto y un tema (su familia, su trabajo, su barrio, una comida, algo que le pasó). Escriba en su cuaderno un párrafo de 5 o 6 oraciones con la plantilla que corresponde.</p>
<details class="caja caja-tip"><summary><strong>📖 Plantilla del texto narrativo</strong></summary><ol><li>Oración inicial: qué pasó y cuándo (en pasado).</li><li>Primer suceso: «Primero…».</li><li>Segundo suceso: «Luego…».</li><li>Tercer suceso: «Después…».</li><li>Cierre: «Finalmente…».</li></ol></details>
<details class="caja caja-tip"><summary><strong>📊 Plantilla del texto informativo</strong></summary><ol><li>Oración principal: el tema («El/La … es…»).</li><li>Primer hecho que se pueda comprobar.</li><li>Segundo hecho.</li><li>Tercer hecho.</li><li>Cierre: una oración que resuma, sin opinar.</li></ol></details>
<details class="caja caja-tip"><summary><strong>💭 Plantilla del texto de opinión</strong></summary><ol><li>Tema y opinión: «Pienso que…».</li><li>Primera razón: «porque…» o «La razón es que…».</li><li>Segunda razón: «Además…».</li><li>Un ejemplo: «Por ejemplo…».</li><li>Conclusión: «Por estas razones…».</li></ol></details>
{C.caja("tip", "Revise su párrafo", "<p>¿Se nota el tipo que eligió? ¿Usó sus palabras clave? ¿Tiene unidad, cohesión y coherencia (Lección 7.2)?</p>")}"""

    secciones = [("s1", "El texto de opinión", s1), ("s2", "Los tres tipos, lado a lado", s2), ("s3", "Plantilla: escribo el tipo que elija", s3)]
    tarea = [("Una carta de opinión.", "Escriba un párrafo de opinión sobre algo de su barrio que le gustaría cambiar (más luz en la calle, una parada de autobús, un parque). Use los cuatro escalones."),
             ("Dos razones.", "Asegúrese de dar al menos dos razones y una conclusión con «Por estas razones…»."),
             ("Hecho u opinión.", "Subraye en su párrafo los hechos con una línea y las opiniones con dos.")]
    quiz = [
        ("¿Qué hace un texto de opinión?", ["Da un punto de vista y lo defiende con razones", "Cuenta sucesos en orden", "Da solo datos"], 0, {1: "Eso es el narrativo.", 2: "Eso es el informativo."}, "Da un <strong>punto de vista con razones</strong>."),
        ("¿Cuál es el tercer escalón?", ["Dar razones", "Presentar el tema", "Concluir"], 0, {1: "Ese es el primero.", 2: "Ese es el cuarto."}, "<strong>Dar razones.</strong>"),
        ("¿Qué frase sirve para dar una opinión?", ["Me parece que…", "Primero…", "Contiene…"], 0, {1: "Es de secuencia.", 2: "Es de un texto informativo."}, "<strong>Me parece que…</strong>"),
        ("¿Qué frase sirve para cerrar una opinión?", ["Por estas razones…", "Además…", "Por ejemplo…"], 0, {1: "Añade otra razón.", 2: "Da un ejemplo."}, "<strong>Por estas razones…</strong>"),
        ("«Me gusta el café» sin ninguna razón es…", ["un gusto, no un argumento", "un argumento completo"], 0, {}, "Un <strong>gusto</strong>: le falta el porqué."),
        ("En la respuesta extendida del GED, ¿qué se pide?", ["Explicar qué argumento de dos textos está mejor apoyado", "Dar su opinión personal sobre cualquier tema"], 0, {}, "Decidir qué argumento está <strong>mejor apoyado por la evidencia</strong>."),
        ("¿Qué tono tiene el texto informativo?", ["Neutro y objetivo", "Personal, con razones"], 0, {}, "<strong>Neutro y objetivo.</strong>"),
        ("<em>Esta mañana no sonó la alarma. Después perdí el autobús. Finalmente llegué a las diez.</em>", TIPOS, 0, {1: "No da datos para comprobar.", 2: "No da una opinión."}, "<strong>Narrativo.</strong>"),
        ("<em>Miami es una ciudad demasiado calurosa para vivir.</em>", ["Una opinión", "Un hecho"], 0, {}, "Una <strong>opinión</strong>."),
        ("¿Qué cambia entre los tres textos sobre la familia?", ["El propósito", "El tema"], 0, {}, "El <strong>propósito</strong>; el tema es el mismo."),
    ]
    filas = [
        ("El texto de opinión", "Escribo una opinión clara con dos razones y una conclusión.", "Doy la opinión, pero solo una razón.", "Solo digo «me gusta» (<a href=\"#s1\">repase la sección 1</a>)."),
        ("Los tres tipos", "Distingo los tres por su propósito y sus palabras clave.", "Confundo a veces el informativo y el de opinión.", "No los distingo (<a href=\"#s2\">repase la sección 2</a>)."),
        ("Escribir", "Escribo el tipo que elijo con su plantilla.", "Mezclo rasgos de dos tipos.", "No sé por dónde empezar (<a href=\"#s3\">repase la sección 3</a>)."),
    ]
    cierre = "<p>Ya conoce los tres tipos de texto. En la próxima lección va a escribir sobre lo que ve en <strong>tablas, gráficas e imágenes</strong>.</p>"
    glosario = [("Texto de opinión", "Texto que da un punto de vista y lo defiende con razones."), ("Argumento", "Una opinión apoyada en razones."),
                ("Razón", "El porqué de una opinión."), ("Conclusión", "La oración que cierra la opinión.")]
    conexion = ("<p>En la Lección 7.3 estudió el texto narrativo y el informativo. Ahora completa el panorama con el texto de opinión, el más exigente: no basta con decir lo que piensa, hay que defenderlo con razones.</p>"
                "<p><strong>Lo que necesita:</strong> el cuaderno.</p>")
    estd = LE.estandares(["R.6.1", "W.1"], base=["R.8.2"])
    return C.pagina_leccion(N, LE.titulo(N), "Decir lo que piensa, y por qué: el texto de opinión.", ["Tipos de texto", "Opinión y razones"],
                            ["<strong>Escribir</strong> un texto de opinión con tema, opinión, razones y conclusión.", "<strong>Usar</strong> las frases que introducen la opinión, las razones y el cierre.",
                             "<strong>Comparar</strong> los tres tipos de texto.", "<strong>Elegir</strong> un tipo y escribirlo con su plantilla."],
                            estd, conexion, secciones, tarea, quiz, filas, cierre, ("7-5", LE.titulo("7-5")), glosario, P)


def practica():
    r = random.Random(74)
    tip = [{"enun": f"<div class=\"texto-lectura\"><p>{t}</p></div>¿Qué tipo de texto es?", "ops": TIPOS, "ok": k, "enOrden": True, "pista": "¿Cuenta lo que pasó, da datos o dice lo que alguien piensa?",
            "exp": f"Es <strong>{TIPOS[k].lower()}</strong>: {PISTA_TIPO[k]}."} for t, k in TEXTOS]
    hec = [{"enun": f"<strong>{o}</strong><br>¿Es un hecho o una opinión?", "ops": ["Un hecho", "Una opinión"], "ok": 0 if h else 1, "enOrden": True, "pista": "",
            "exp": "Se puede <strong>comprobar</strong>: es un hecho." if h else "Depende de quién lo diga: es una <strong>opinión</strong>."} for o, h in HECHO]
    par = []
    for o, r1, r2, c in OPINIONES:
        txt = " ".join(f"<strong>({i + 1})</strong> {x}" for i, x in enumerate([o, r1, r2, c]))
        for i, k in [(0, 0), (r.choice([1, 2]), 1), (3, 2)]:
            par.append({"enun": f"<div class=\"texto-lectura\"><p>{txt}</p></div>¿Qué parte del texto de opinión es la oración <strong>({i + 1})</strong>?", "ops": PARTES, "ok": k, "enOrden": True,
                        "pista": "Opinión: lo que piensa. Razón: el porqué. Conclusión: cierra con «por eso», «por estas razones»…", "exp": f"Es <strong>{PARTES[k].lower()}</strong>."})
    mods = [("tipo", "¿Narrativo, informativo o de opinión?", C.om("m1", "Lea el texto y decida su tipo.")),
            ("hecho", "¿Hecho u opinión?", C.om("m2", "¿Se puede comprobar o depende de quién lo diga?")),
            ("partes", "Las partes del texto de opinión", C.om("m3", "Decida qué parte es la oración marcada."))]
    js = C.js_datos("TIP", tip) + C.js_datos("HEC", hec) + C.js_datos("PAR", par) + 'creaBanco("m1", TIP);\ncreaBanco("m2", HEC);\ncreaBanco("m3", PAR);\n'
    return C.pagina_practica(N, LE.titulo(N), "Tres actividades · los ejercicios cambian cada vez · dos intentos en cada uno", mods, js)


if __name__ == "__main__":
    LE.construye(N, leccion, practica, horas="Unas 3 horas")
