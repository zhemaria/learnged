# -*- coding: utf-8 -*-
"""LearnGED · Artes del lenguaje (español) · Nivel 1 · Lección 7.2 · Cualidades del párrafo y conectores básicos.
Fuente: clases_leng1/clase_7-2.html (GEDparaHispanos) y gramatica/n1-l7-2.html, adaptadas al marco de LearnGED.
Uso: python3 tools/build_leng1_7_2.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import leng_es as LE
from leng_es import C

LE.nivel(1)
N = "7-2"
CON = ["y", "pero", "porque", "entonces"]
FUN = ["añade información", "marca un contraste: la segunda parte se opone a la primera", "da la razón o la causa", "presenta la consecuencia"]
HUECOS = [("Compré arroz ___ frijoles en la tienda.", 0), ("Mi hija estudia enfermería ___ trabaja los fines de semana.", 0), ("Limpié la cocina ___ lavé la ropa.", 0), ("Hoy desayuné café ___ pan tostado.", 0),
          ("Quería ir a la fiesta, ___ tenía que trabajar.", 1), ("El carro es viejo, ___ funciona muy bien.", 1), ("Estudié mucho, ___ el examen fue difícil.", 1), ("Me gusta el verano, ___ no soporto la humedad.", 1), ("La tienda es pequeña, ___ tiene de todo.", 1),
          ("No fui a trabajar ___ estaba enfermo.", 2), ("Llegué tarde ___ perdí el autobús.", 2), ("Me pongo el abrigo ___ hace mucho frío.", 2), ("Estoy contenta ___ aprobé el examen.", 2), ("Los niños duermen temprano ___ están cansados.", 2),
          ("Se acabó la leche; ___, fui a comprar más.", 3), ("No encontraba las llaves; ___, llamé a mi hermano.", 3), ("Estaba lloviendo; ___, me quedé en casa.", 3), ("El autobús no llegaba; ___, tomé un taxi.", 3), ("Tenía mucha hambre; ___, preparé un sándwich.", 3)]
CUAL = ["Le falta unidad", "Le falta cohesión", "Le falta coherencia"]
EXPL = ["Una oración se sale del tema: falta <strong>unidad</strong>.", "Las oraciones están sueltas, sin conectores: falta <strong>cohesión</strong>.", "Las ideas están desordenadas: falta <strong>coherencia</strong>."]
FALTA = [("El mercado abre a las siete. Venden frutas y carne fresca. Mi sobrino estudia en California. Los precios son bajos.", 0),
         ("Mi casa es pequeña y cómoda. Tiene dos cuartos y un patio. Mi jefe es muy exigente. Me siento feliz allí.", 0),
         ("El parque es agradable. Hay muchos árboles. El precio de la gasolina subió. Los niños juegan en los columpios.", 0),
         ("El invierno es frío. Cae nieve. Uso abrigo. Uso guantes. Me quedo en casa.", 1),
         ("Me levanté. Desayuné. Salí. Tomé el autobús. Llegué.", 1),
         ("Mi hijo juega fútbol. Entrena los martes. Es delantero. Le gusta mucho.", 1),
         ("Comimos el pastel. Mi hija sopló las velas. Compramos el pastel por la mañana. Ayer fue su cumpleaños.", 2),
         ("Finalmente, llegué al trabajo. Primero, me desperté. Luego, tomé el tren.", 2),
         ("Por eso me gusta tanto. Mi perro se llama Toby. Es pequeño y juguetón. Siempre me espera en la puerta.", 2)]
ORDENAR = [("El sábado de Rosa", ["Los sábados son el día favorito de Rosa porque no trabaja.", "Se levanta tarde y desayuna con calma.", "Después sale al parque con sus nietos.", "Por eso espera el sábado toda la semana."]),
           ("La clase de la noche", ["Estudiar de noche es difícil, pero vale la pena.", "Llego cansado del trabajo y tengo sueño.", "Sin embargo, en clase aprendo cosas nuevas y hago amigos.", "Por eso, aunque me cueste, no falto nunca."]),
           ("La tormenta", ["Ayer hubo una tormenta muy fuerte en el barrio.", "Primero, el cielo se puso negro y empezó a soplar el viento.", "Luego cayó un aguacero que inundó las calles.", "Finalmente, salió el sol y los vecinos limpiaron juntos."])]


def leccion():
    P = C.Practicas()
    s1 = f"""<p>Saber dónde va cada parte del párrafo no basta: las oraciones también tienen que sostenerse unas a otras. Un buen párrafo tiene tres cualidades.</p>
{C.tabla("Las tres cualidades del párrafo", ["Cualidad", "Qué es", "Si falta…"],
         [["🎯 Unidad", "Hablar de un solo tema.", "Una oración se sale del tema."], ["🔗 Cohesión", "Unir las oraciones con conectores, para que fluyan como un río y no como piedras sueltas.", "Las oraciones quedan sueltas, cortadas."],
          ["🧠 Coherencia", "Que las ideas sigan un orden lógico.", "El lector no entiende la secuencia."]])}
{C.tabla("Tres párrafos, antes y después", ["Falta…", "❌ Así no", "✅ Así sí"],
         [["Unidad", "El mercado de mi barrio abre a las siete. Allí venden frutas, verduras y carne fresca. <s>Mi sobrino estudia en una universidad de California.</s> Los precios son bajos.",
           "El mercado de mi barrio abre a las siete. Allí venden frutas, verduras y carne fresca. Los precios son bajos. Por eso prefiero comprar allí."],
          ["Cohesión", "El invierno en Chicago es muy frío. Cae mucha nieve. Las personas usan abrigo. Los carros llevan llantas especiales.",
           "El invierno en Chicago es muy frío <strong>y</strong> cae mucha nieve. <strong>Por eso</strong>, las personas usan abrigo. <strong>Además</strong>, los carros llevan llantas especiales."],
          ["Coherencia", "Comimos pastel. Mi hija sopló las velas. Compramos un pastel de chocolate. Ayer fue el cumpleaños de mi hija.",
           "Ayer fue el cumpleaños de mi hija. Compramos un pastel de chocolate. Cantamos todos juntos y mi hija sopló las velas. Después comimos pastel."]])}
{C.caja("tip", "Resumen", "<p>La <strong>unidad</strong> es el tema único; la <strong>cohesión</strong>, el pegamento entre oraciones; la <strong>coherencia</strong>, el orden lógico.</p>")}"""

    s2 = f"""<p>Los <strong>conectores</strong> son palabras pequeñas con un gran trabajo: unen oraciones y dicen qué relación hay entre ellas. Sin conectores, las oraciones son ladrillos sueltos; con conectores, forman una pared.</p>
{C.tabla("Cuatro conectores básicos", ["Conector", "Para qué sirve", "Ejemplo"],
         [["y", "Añadir información.", "Compré pan y leche."], ["pero", "Marcar un contraste.", "Quería ir al cine, pero estaba lloviendo."],
          ["porque", "Dar una razón o causa.", "Llegué tarde porque perdí el autobús."], ["entonces", "Presentar una consecuencia.", "No había azúcar; entonces, compré una bolsa."]])}
<div class="texto-lectura"><p>Los sábados son mi día favorito <strong>porque</strong> no trabajo. Me levanto tarde, desayuno con calma <strong>y</strong> leo el periódico. A veces planeo salir al parque, <strong>pero</strong> si hace mal tiempo, me quedo en casa viendo películas. Ese día no tengo prisa; <strong>entonces</strong>, haga el tiempo que haga, siempre lo disfruto.</p></div>
{C.caja("ojo", "La puntuación de los conectores", "<ul><li>Antes de <strong>pero</strong> casi siempre va coma: «Estudié mucho, pero el examen fue difícil».</li><li><strong>Y</strong> no lleva coma en oraciones simples: «Comí arroz y frijoles».</li><li><strong>Porque</strong> no suele llevar coma ni ir al principio; al principio se usa <em>como</em>: «Como no trabajo, me levanto tarde».</li><li><strong>Entonces</strong> suele llevar coma después: «Entonces, decidí descansar».</li></ul>")}
{P("Compruebe", "<em>El carro es viejo, ___ funciona muy bien.</em>", CON, 1, {0: "No se añade algo parecido: se opone.", 2: "Funcionar bien no es la razón de ser viejo.", 3: "No es una consecuencia."}, "<strong>pero</strong>: marca el contraste entre viejo y funciona bien.")}"""

    pasos = ORDENAR[0][1]
    s3 = f"""<div class="caja caja-tip"><span class="etiqueta et-verde">Actividad · en su cuaderno</span>
<p>Las oraciones de este párrafo están desordenadas. Cópielas en el orden correcto. Recuerde: la principal anuncia el tema y la de cierre termina la idea.</p>
<ul><li>{pasos[2]}</li><li>{pasos[3]}</li><li>{pasos[0]}</li><li>{pasos[1]}</li></ul></div>
<details class="caja caja-tip"><summary><strong>Ya lo ordené: ver el párrafo</strong></summary><p>{" ".join(pasos)}</p></details>
<div class="caja caja-tip"><span class="etiqueta et-verde">Actividad · mi primer párrafo con conectores</span>
<p>Escriba un párrafo de 4 a 6 oraciones sobre su día favorito de la semana. Use al menos tres de los cuatro conectores (<em>y, pero, porque, entonces</em>) y subráyelos. Después revise: ¿tiene unidad, cohesión y coherencia?</p></div>"""

    secciones = [("s1", "Las tres cualidades del párrafo", s1), ("s2", "Los conectores básicos", s2), ("s3", "Práctica: ordenar y escribir", s3)]
    tarea = [("Mi párrafo.", "Pase en limpio el párrafo de la sección 3. Revise con las tres preguntas: ¿un solo tema? ¿oraciones unidas? ¿orden lógico?"),
             ("Los conectores en mi vida.", "Escriba cuatro oraciones sobre su semana, una con cada conector: y, pero, porque, entonces."),
             ("Detective.", "Busque en un periódico o folleto un párrafo y encierre en un círculo sus conectores.")]
    quiz = [
        ("¿Qué es la <strong>unidad</strong> de un párrafo?", ["Hablar de un solo tema", "Usar conectores", "Seguir un orden lógico"], 0, {1: "Eso es la cohesión.", 2: "Eso es la coherencia."}, "Hablar de <strong>un solo tema</strong>."),
        ("¿Qué es la <strong>cohesión</strong>?", ["Unir las oraciones con conectores", "Hablar de un tema", "Escribir oraciones largas"], 0, {1: "Eso es la unidad.", 2: "No."}, "<strong>Unir las oraciones</strong>."),
        ("¿Qué es la <strong>coherencia</strong>?", ["Que las ideas sigan un orden lógico", "Usar muchas palabras", "Poner títulos"], 0, {1: "No.", 2: "No."}, "El <strong>orden lógico</strong>."),
        ("<em>Quería ir al cine, ___ estaba lloviendo.</em>", CON, 1, {0: "No añade algo parecido.", 2: "No es la razón.", 3: "No es una consecuencia."}, "<strong>pero</strong>."),
        ("<em>Llegué tarde ___ perdí el autobús.</em>", CON, 2, {0: "No añade algo parecido.", 1: "No hay contraste.", 3: "Perder el autobús es la causa, no la consecuencia."}, "<strong>porque</strong>: da la causa."),
        ("<em>No había azúcar; ___, compré una bolsa.</em>", CON, 3, {0: "No es algo que se añade.", 1: "No hay contraste.", 2: "Comprar no es la causa."}, "<strong>entonces</strong>: la consecuencia."),
        ("¿Dónde va la coma con <strong>pero</strong>?", ["Antes: «…, pero…»", "Después: «… pero, …»"], 0, {}, "<strong>Antes</strong> de pero."),
        ("<em>El mercado abre a las siete. Venden frutas. Mi sobrino estudia en California.</em> ¿Qué le falta?", CUAL, 0, {1: "El problema es una oración fuera del tema.", 2: "El problema es una oración fuera del tema."}, "<strong>Unidad.</strong>"),
        ("<em>Me levanté. Desayuné. Salí. Llegué.</em> ¿Qué le falta?", CUAL, 1, {0: "Todo habla de lo mismo.", 2: "El orden está bien."}, "<strong>Cohesión</strong>: faltan conectores."),
        ("Al principio de la oración, en vez de «porque» se usa…", ["como", "pero"], 0, {}, "<strong>Como</strong>: «Como no trabajo, me levanto tarde»."),
    ]
    filas = [
        ("Las tres cualidades", "Reconozco cuándo a un párrafo le falta unidad, cohesión o coherencia.", "Reconozco la unidad, pero confundo las otras dos.", "No las distingo (<a href=\"#s1\">repase la sección 1</a>)."),
        ("Conectores", "Uso y, pero, porque y entonces con su puntuación.", "Los uso, pero olvido la coma.", "No los uso (<a href=\"#s2\">repase la sección 2</a>)."),
        ("Escribir", "Mi párrafo tiene las tres partes y las tres cualidades.", "Le falta una cualidad.", "No logro escribirlo (<a href=\"#s3\">repase la sección 3</a>)."),
    ]
    cierre = "<p>Ya sabe escribir un párrafo unido, bien conectado y ordenado. En la próxima lección verá para qué se escribe: <strong>el texto narrativo y el informativo</strong>.</p>"
    glosario = [("Unidad", "Que todas las oraciones hablen del mismo tema."), ("Cohesión", "Que las oraciones estén unidas con conectores."),
                ("Coherencia", "Que las ideas sigan un orden lógico."), ("Conector", "Palabra que une oraciones y muestra su relación: y, pero, porque, entonces.")]
    conexion = ("<p>En la Lección 7.1 aprendió la estructura del párrafo con la técnica de la hamburguesa. Ahora verá qué hace que las oraciones se sostengan unas a otras, y usará los conectores para unirlas.</p>"
                "<p><strong>Lo que necesita:</strong> el cuaderno.</p>")
    estd = LE.estandares(["W.1"], base=["L.2.1", "R.5.3"])
    return C.pagina_leccion(N, LE.titulo(N), "Unidad, cohesión y coherencia: el párrafo que se sostiene solo.", ["Escritura", "Conectores"],
                            ["<strong>Reconocer</strong> la unidad, la cohesión y la coherencia de un párrafo.", "<strong>Usar</strong> los conectores y, pero, porque y entonces, con su puntuación.",
                             "<strong>Ordenar</strong> las oraciones de un párrafo.", "<strong>Escribir</strong> un párrafo con las tres cualidades."],
                            estd, conexion, secciones, tarea, quiz, filas, cierre, ("7-3", LE.titulo("7-3")), glosario, P)


def practica():
    hue = [{"enun": f"<strong>{o}</strong><br>¿Qué conector va en el espacio?", "ops": CON, "ok": k, "enOrden": True, "pista": "Y: añade. Pero: contraste. Porque: la razón. Entonces: la consecuencia.",
            "exp": f"Va <strong>{CON[k]}</strong>: {FUN[k]}."} for o, k in HUECOS]
    fal = [{"enun": f"<div class=\"texto-lectura\"><p>{t}</p></div>¿Qué cualidad le falta a este párrafo?", "ops": CUAL, "ok": k, "enOrden": True,
            "pista": "¿Hay una oración fuera del tema? ¿Faltan conectores? ¿Están las ideas en desorden?", "exp": EXPL[k]} for t, k in FALTA]
    ini = [[2, 0, 3, 1], [3, 1, 0, 2], [1, 3, 2, 0]]
    ordn = [{"titulo": t, "intro": "Ordene las oraciones con los botones ▲ y ▼ para formar un párrafo con unidad, cohesión y coherencia.", "pasos": p, "inicio": ini[i], "cons": {},
             "general": "La principal va primero, el cierre al final, y las del medio siguen el orden lógico que marcan los conectores."} for i, (t, p) in enumerate(ORDENAR)]
    mods = [("conectores", "¿Y, pero, porque o entonces?", C.om("m1", "Elija el conector que une las dos partes.")),
            ("cualidades", "¿Qué le falta al párrafo?", C.om("m2", "Decida qué cualidad le falta: unidad, cohesión o coherencia.")),
            ("ordenar", "Arme el párrafo", C.orden("m3"))]
    js = C.js_datos("HUE", hue) + C.js_datos("FAL", fal) + C.js_datos("ORD", ordn) + 'creaBanco("m1", HUE);\ncreaBanco("m2", FAL);\ncreaOrden("m3", ORD);\n'
    return C.pagina_practica(N, LE.titulo(N), "Tres actividades · los ejercicios cambian cada vez · dos intentos en cada uno", mods, js)


if __name__ == "__main__":
    LE.construye(N, leccion, practica, horas="Unas 3 horas")
