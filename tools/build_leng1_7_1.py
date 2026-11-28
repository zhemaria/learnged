# -*- coding: utf-8 -*-
"""LearnGED · Artes del lenguaje (español) · Nivel 1 · Lección 7.1 · El párrafo y la técnica de la hamburguesa.
Fuente: clases_leng1/clase_7-1.html (GEDparaHispanos) y gramatica/n1-l7-1.html, adaptadas al marco de LearnGED.
Uso: python3 tools/build_leng1_7_1.py
"""
import os, sys, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import leng_es as LE
from leng_es import C

LE.nivel(1)
N = "7-1"
# (oraciones: principal, apoyos…, cierre; oración intrusa)
PARRAFOS = [(["Mi barrio tiene todo lo que necesito.", "A dos cuadras hay un supermercado grande.", "La clínica queda frente al parque.", "El autobús pasa por la esquina cada diez minutos.", "Por eso no pienso mudarme de aquí."], "Mi hermano vive en Houston desde 2015."),
            (["Los domingos en mi casa son muy especiales.", "Toda la familia almuerza junta.", "Mi madre prepara arroz con pollo.", "Por la tarde jugamos dominó en el patio.", "Sin duda, es el mejor día de la semana."], "El lunes tengo cita con el dentista."),
            (["Aprender inglés me ha abierto muchas puertas.", "Ahora puedo hablar con el médico sin intérprete.", "En el trabajo me dieron un puesto mejor.", "También ayudo a mis hijos con la tarea.", "Por todo eso, sigo estudiando cada noche."], "Mi color favorito es el azul."),
            (["El invierno en Chicago exige preparación.", "Hay que tener un abrigo grueso, guantes y gorro.", "Conviene revisar la calefacción antes de noviembre.", "Los carros necesitan llantas en buen estado.", "Quien se prepara pasa el invierno sin problemas."], "En Puerto Rico hace calor todo el año."),
            (["Mi trabajo en el restaurante es duro, pero me gusta.", "Entro a las seis de la mañana a preparar los ingredientes.", "A la hora del almuerzo no hay un minuto de descanso.", "Mis compañeros son alegres y trabajadores.", "Al final del día, me voy cansado pero contento."], "Mi vecino tiene un perro muy grande."),
            (["La biblioteca pública ofrece mucho más que libros.", "Tiene computadoras con internet gratis.", "Da clases de inglés y de ciudadanía.", "Los niños pueden ir a la hora del cuento.", "Es un lugar valioso para toda la comunidad."], "Las librerías venden libros nuevos y usados."),
            (["Ahorrar dinero requiere pequeños hábitos.", "Se puede llevar el almuerzo al trabajo.", "Conviene comparar precios antes de comprar.", "Guardar un poco cada semana suma mucho al año.", "Con paciencia, cualquiera puede ahorrar."], "Los bancos cierran los domingos."),
            (["El mercado de mi barrio es mi lugar favorito para comprar.", "Las frutas y las verduras son frescas.", "Los precios son más bajos que en el supermercado.", "Los vendedores me conocen por mi nombre.", "Por eso hago allí casi todas mis compras."], "Mi primo trabaja en una fábrica de muebles."),
            (["Hacer ejercicio trae muchos beneficios.", "Fortalece el corazón.", "Ayuda a dormir mejor.", "Reduce el estrés del día.", "Por estas razones, camino media hora cada mañana."], "Mi programa de televisión favorito empieza a las ocho."),
            (["Mi abuela es la persona que más admiro.", "Crio a seis hijos ella sola.", "Aprendió a leer a los cincuenta años.", "Siempre tiene una palabra amable para todos.", "Quiero parecerme a ella cuando sea mayor."], "Las tortugas pueden vivir muchos años.")]
PARTES = ["Oración principal", "Oración de apoyo", "Oración de cierre"]
MODELOS = [("Mi familia", ["Mi familia es pequeña pero muy unida.", "Vivimos cuatro personas en la casa: mi esposa, mis dos hijos y yo.", "Todos los domingos nos reunimos a almorzar y conversamos sobre la semana.",
                           "Mi esposa prepara la comida y los hijos ayudan a poner la mesa.", "Por eso, para mí, la familia es lo más importante de la vida."]),
           ("Mi barrio", ["El barrio donde vivo es tranquilo y agradable.", "Las calles son anchas y tienen árboles a ambos lados.", "Hay una panadería en la esquina y un parque pequeño a dos cuadras.",
                          "Los vecinos se conocen y se saludan cuando se cruzan en la calle.", "Por estas razones, me siento muy a gusto en este lugar."]),
           ("Mi trabajo", ["Trabajar en una panadería tiene muchas cosas buenas.", "El olor del pan recién horneado llena toda la tienda desde temprano.", "Los clientes llegan contentos porque saben que van a comer algo rico.",
                           "Además, aprendí a preparar diferentes tipos de pan y dulces.", "Sin duda, es un oficio que me da muchas satisfacciones."])]


def coloreado(ors):
    cl = ["hb-pri"] + ["hb-apo"] * (len(ors) - 2) + ["hb-cie"]
    nom = {"hb-pri": "Principal", "hb-apo": "Apoyo", "hb-cie": "Cierre"}
    return '<p class="hamb-par">' + " ".join(f'<span class="{c}"><span class="cap-oculto">{nom[c]}: </span>{o}</span>' for c, o in zip(cl, ors)) + "</p>"


HAMBURGUESA = """<div class="hamburguesa" role="img" aria-label="Una hamburguesa con tres partes: el pan de arriba es la oración principal; el relleno, las oraciones de apoyo; el pan de abajo, la oración de cierre.">
<div class="hb-capa hb-pan-a"><span aria-hidden="true">🍞</span> <strong>Pan de arriba</strong> · Oración principal</div>
<div class="hb-capa hb-relleno"><span aria-hidden="true">🥬🍅🥩</span> <strong>Relleno</strong> · Oraciones de apoyo (detalles, ejemplos, explicaciones)</div>
<div class="hb-capa hb-pan-b"><span aria-hidden="true">🍞</span> <strong>Pan de abajo</strong> · Oración de cierre</div></div>"""
LEYENDA = '<p class="hamb-ley"><span class="hb-pri">Principal</span> <span class="hb-apo">Apoyo</span> <span class="hb-cie">Cierre</span></p>'


def leccion():
    P = C.Practicas()
    s1 = f"""<p>Un <strong>párrafo</strong> es un grupo de oraciones que desarrollan <strong>una sola idea principal</strong>. Empieza con mayúscula y termina con un <strong>punto y aparte</strong>: ahí termina una idea y, si hay otro párrafo, empieza otra.</p>
{C.caja("tip", "Idea central", "<p>Un párrafo no se mide por su largo, sino por su <strong>unidad</strong>: puede tener tres oraciones o diez, pero todas hablan del mismo asunto.</p>")}
<p>En un texto bien escrito, los párrafos se reconocen a simple vista: la primera línea tiene sangría o va después de una línea en blanco, empieza con mayúscula y termina con punto y aparte. Quien escribe sin separar sus ideas en párrafos cansa al lector, que se pierde.</p>"""

    s2 = f"""<p>Un buen párrafo funciona como una hamburguesa: cada parte tiene una función, y si falta una, todo se desarma.</p>
{HAMBURGUESA}
{C.tabla("Las tres partes del párrafo", ["Parte", "Qué hace", "Pregunta que responde"],
         [["🍞 Oración principal", "Anuncia el tema. Al escribir, póngala al principio. Al leer textos de otros, a veces aparece en el medio o al final (Lección 4.3).", "¿De qué voy a hablar?"],
          ["🥩 Oraciones de apoyo", "Dos o tres oraciones con detalles, ejemplos o explicaciones.", "¿Qué quiero decir sobre eso?"],
          ["🍞 Oración de cierre", "Cierra la idea, resume o redondea lo dicho.", "¿Cómo termino?"]])}
{C.caja("ojo", "En este nivel", "<p>Escriba párrafos de <strong>4 a 6 oraciones</strong>: una principal, dos o tres de apoyo y una de cierre.</p>")}"""

    mods = "".join(f"<h3>Modelo {i + 1}: {t}</h3>{coloreado(o)}" for i, (t, o) in enumerate(MODELOS))
    s3 = f"""<p>Los colores señalan qué parte es cada oración.</p>
{LEYENDA}
{mods}
{C.caja("tip", "Para encontrar la oración principal", "<p>Pregúntese: ¿cuál es la oración <strong>más general</strong>? ¿Cuál resume todo el párrafo? ¿Cuál podría ser su título? ¿Cuál abarca a todas las demás?</p>")}
{P("Compruebe", "En el modelo «Mi barrio», ¿qué hace la última oración?", ["Cierra la idea", "Anuncia el tema", "Da un detalle del parque"], 0, {1: "El tema lo anuncia la primera.", 2: "Los detalles van en el relleno."}, "<strong>Cierra la idea</strong>: «Por estas razones, me siento muy a gusto…».")}
{P("Compruebe", "<em>Hacer ejercicio trae muchos beneficios. Fortalece el corazón. Ayuda a dormir mejor. Reduce el estrés.</em> ¿Qué le falta a este párrafo?", ["La oración de cierre", "La oración principal", "Las oraciones de apoyo"], 0,
   {1: "La primera oración es la principal.", 2: "Tiene tres oraciones de apoyo."}, "Le falta <strong>el pan de abajo</strong>, por ejemplo: «Por estas razones, camino media hora cada mañana».")}"""

    s4 = f"""<div class="caja caja-tip"><span class="etiqueta et-verde">Actividad · en su cuaderno</span>
<p>Escriba su propio párrafo-hamburguesa sobre uno de estos temas: <em>mi comida favorita, mi lugar favorito, una persona que admiro</em>. Primero haga la hamburguesa en tres renglones (principal, apoyo, cierre) y después escriba el párrafo completo, de 4 a 6 oraciones.</p></div>
<details class="caja caja-tip"><summary><strong>Ver un ejemplo</strong></summary>
{coloreado(["Mi comida favorita es el arroz con frijoles de mi mamá.", "Lo prepara los domingos con mucho cuidado.", "Los frijoles se cocinan desde la mañana con ajo y cebolla.", "Toda la casa huele a comida rica.", "Para mí, ese plato tiene el sabor de mi familia."])}</details>"""

    secciones = [("s1", "¿Qué es un párrafo?", s1), ("s2", "La técnica de la hamburguesa", s2), ("s3", "Párrafos modelo", s3), ("s4", "Práctica: mi primer párrafo", s4)]
    tarea = [("Mi hamburguesa.", "Escriba en su cuaderno un párrafo de 4 a 6 oraciones sobre su día favorito de la semana, con oración principal, dos o tres de apoyo y una de cierre."),
             ("Marque las partes.", "Subraye la oración principal con una línea, las de apoyo con dos y la de cierre con una línea ondulada."),
             ("Revise.", "¿Todas las oraciones hablan del mismo tema? ¿Empieza con mayúscula y termina con punto y aparte?")]
    quiz = [
        ("¿Qué es un párrafo?", ["Un grupo de oraciones sobre una sola idea", "Una oración muy larga", "Una lista de palabras"], 0, {1: "Un párrafo tiene varias oraciones.", 2: "No."}, "Oraciones sobre <strong>una sola idea</strong>."),
        ("¿Con qué termina un párrafo?", ["Con punto y aparte", "Con una coma", "Con un punto y seguido"], 0, {1: "La coma no cierra.", 2: "El punto y seguido separa oraciones del mismo párrafo."}, "Con <strong>punto y aparte</strong>."),
        ("En la hamburguesa, el pan de arriba es…", PARTES, 0, {1: "Eso es el relleno.", 2: "Eso es el pan de abajo."}, "La <strong>oración principal</strong>."),
        ("¿Qué hacen las oraciones de apoyo?", ["Dan detalles, ejemplos o explicaciones", "Anuncian el tema", "Cierran el párrafo"], 0, {1: "Eso es la principal.", 2: "Eso es el cierre."}, "Dan <strong>detalles</strong>."),
        ("¿Cuántas oraciones conviene escribir en este nivel?", ["De 4 a 6", "Una", "Más de 15"], 0, {1: "Una sola no es párrafo.", 2: "Demasiadas para empezar."}, "<strong>De 4 a 6.</strong>"),
        ("<em>«Sin duda, es el mejor día de la semana.»</em> Al final de un párrafo, es…", PARTES, 2, {0: "No anuncia: cierra.", 1: "No da un detalle."}, "La <strong>oración de cierre</strong>."),
        ("¿Cuál es la oración más general de un párrafo?", ["La principal", "Una de apoyo"], 0, {}, "La <strong>principal</strong>."),
        ("<em>Mi abuela es la persona que más admiro. Crio a seis hijos ella sola. Las tortugas viven muchos años.</em> ¿Qué oración sobra?", ["Las tortugas viven muchos años.", "Crio a seis hijos ella sola.", "Mi abuela es la persona que más admiro."], 0,
         {1: "Esta apoya la idea.", 2: "Esta es la principal."}, "<strong>Las tortugas…</strong> no habla de la abuela."),
        ("¿Qué mide la calidad de un párrafo?", ["Su unidad: que todo hable del mismo tema", "Su largo"], 0, {}, "Su <strong>unidad</strong>."),
        ("Al leer textos de otros, ¿la oración principal siempre va primero?", ["No: a veces va en el medio o al final", "Sí, siempre"], 0, {}, "<strong>No siempre.</strong> Al escribir usted, póngala primero."),
    ]
    filas = [
        ("Reconocer el párrafo", "Reconozco dónde empieza y termina un párrafo.", "A veces me confundo.", "No los distingo (<a href=\"#s1\">repase la sección 1</a>)."),
        ("Las tres partes", "Encuentro la principal, las de apoyo y el cierre.", "Encuentro la principal, pero confundo el cierre.", "No las veo (<a href=\"#s2\">repase la sección 2</a>)."),
        ("Escribir", "Escribo un párrafo de 4 a 6 oraciones con las tres partes.", "Me falta el cierre o el apoyo.", "No sé empezar (<a href=\"#s4\">repase la sección 4</a>)."),
    ]
    cierre = "<p>Ya sabe armar un párrafo como una hamburguesa. En la próxima lección verá qué hace que un párrafo sea bueno: <strong>la unidad, el orden y los conectores</strong>.</p>"
    glosario = [("Párrafo", "Grupo de oraciones sobre una sola idea, que termina con punto y aparte."), ("Oración principal", "La que anuncia el tema del párrafo."),
                ("Oración de apoyo", "La que da detalles, ejemplos o explicaciones."), ("Oración de cierre", "La que termina la idea."), ("Punto y aparte", "Punto que termina un párrafo.")]
    conexion = ("<p>Hasta ahora aprendió a leer oraciones, textos e información visual. Ahora va a dar un paso decisivo: escribir sus propias ideas de forma organizada, empezando por el párrafo.</p>"
                "<p><strong>Lo que necesita:</strong> el cuaderno y un lápiz.</p>")
    estd = LE.estandares(["W.1"], base=["R.2.1", "R.5.1"])
    return C.pagina_leccion(N, LE.titulo(N), "Pan, relleno y pan: la receta del buen párrafo.", ["Escritura", "El párrafo"],
                            ["<strong>Explicar</strong> qué es un párrafo.", "<strong>Reconocer</strong> la oración principal, las de apoyo y la de cierre.",
                             "<strong>Escribir</strong> un párrafo de 4 a 6 oraciones con la técnica de la hamburguesa."],
                            estd, conexion, secciones, tarea, quiz, filas, cierre, ("7-2", LE.titulo("7-2")), glosario, P)


def practica():
    r = random.Random(71)
    pri, par, intr = [], [], []
    for ors, x in PARRAFOS:
        txt = " ".join(ors)
        pri.append({"enun": f"<div class=\"texto-lectura\"><p>{txt}</p></div>¿Cuál es la oración principal?", "ops": [ors[0]] + r.sample(ors[1:-1], 1) + [ors[-1]], "ok": 0,
                    "pista": "Busque la oración más general: la que podría ser el título.", "exp": f"<strong>{ors[0]}</strong> anuncia el tema; las demás lo desarrollan o lo cierran."})
        num = " ".join(f"<strong>({i + 1})</strong> {o}" for i, o in enumerate(ors))
        for i in [0, r.randint(1, len(ors) - 2), len(ors) - 1]:
            k = 0 if i == 0 else 2 if i == len(ors) - 1 else 1
            par.append({"enun": f"<div class=\"texto-lectura\"><p>{num}</p></div>En este párrafo, ¿qué parte es la oración <strong>({i + 1})</strong>?", "ops": PARTES, "ok": k, "enOrden": True,
                        "pista": "Principal: anuncia el tema. Apoyo: da un detalle. Cierre: termina la idea.", "exp": f"Es la <strong>{PARTES[k].lower()}</strong>."})
        pos = r.randint(1, len(ors) - 2)
        con = ors[:pos] + [x] + ors[pos:]
        intr.append({"enun": f"<div class=\"texto-lectura\"><p>{' '.join(con)}</p></div>¿Qué oración <strong>no encaja</strong> en el párrafo?", "ops": [x] + r.sample(ors[1:-1], 2), "ok": 0,
                     "pista": "Lea la oración principal y pregúntese en cada una: ¿habla de lo mismo?", "exp": f"«{x}» no habla del tema del párrafo: <em>{ors[0][0].lower() + ors[0][1:-1]}</em>."})
    mods = [("principal", "Encuentre el pan de arriba", C.om("m1", "Elija la oración principal del párrafo.")),
            ("partes", "¿Qué parte de la hamburguesa es?", C.om("m2", "Decida si la oración es principal, de apoyo o de cierre.")),
            ("intrusa", "La oración que no encaja", C.om("m3", "Una oración habla de otra cosa. Encuéntrela."))]
    js = C.js_datos("PRI", pri) + C.js_datos("PAR", par) + C.js_datos("INT", intr) + 'creaBanco("m1", PRI);\ncreaBanco("m2", PAR);\ncreaBanco("m3", INT);\n'
    return C.pagina_practica(N, LE.titulo(N), "Tres actividades · los ejercicios cambian cada vez · dos intentos en cada uno", mods, js)


if __name__ == "__main__":
    LE.construye(N, leccion, practica, horas="Unas 3 horas")
