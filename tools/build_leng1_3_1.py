# -*- coding: utf-8 -*-
"""LearnGED · Artes del lenguaje (español) · Nivel 1 · Lección 3.1 · Sustantivos y adjetivos.
Fuente: clases_leng1/clase_3-1.html (GEDparaHispanos), adaptada al marco de LearnGED.
Uso: python3 tools/build_leng1_3_1.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import leng_es as LE
from leng_es import C

LE.nivel(1)
N = "3-1"

TEXTOS = [
    ("La familia", "Mi *familia* es pequeña pero feliz. Mi *papá* trabaja en una *fábrica* en el *sur* de *Chicago*. Mi *mamá* cuida la *casa* y prepara *comida* deliciosa. Mi *hermana* menor estudia en la *escuela* primaria. Tenemos mucho *amor* y *respeto*."),
    ("La casa", "Nuestra *casa* tiene tres *cuartos*. La *cocina* es grande y luminosa. En la *sala* hay un *sofá* azul y una *mesa* de *madera*. El *jardín* tiene *flores* de muchos *colores*. Mi *perro* *Rocky* duerme en la *terraza*."),
    ("El trabajo", "Mi *trabajo* en el *restaurante* me gusta mucho. Mi *jefe* se llama *Carlos* y es muy amable. Trabajo con dos *compañeros*: *Ana* y *Luis*. Yo limpio las *mesas* y los *platos*. La *paciencia* y la *responsabilidad* son importantes."),
]


def leccion():
    P = C.Practicas()
    s1 = f"""<p>Toda oración necesita un protagonista, y ese protagonista suele ser un <strong>sustantivo</strong>: la palabra que usamos para <strong>nombrar</strong>.</p>
{C.tabla("Qué nombran los sustantivos", ["Nombra", "Ejemplos"],
         [["Una persona", "María, profesor, hermana, doctora"], ["Un lugar", "Chicago, parque, casa, escuela"], ["Un objeto", "mesa, lápiz, carro, taza"], ["Una idea o un sentimiento", "amor, libertad, miedo, alegría"]])}
<h3>Comunes y propios</h3>
{C.tabla("Sustantivos comunes y propios", ["Tipo", "Qué hace", "Ejemplos"],
         [["Común", "Nombra cualquier cosa de una clase, sin distinguirla de las demás. Va con minúscula.", "perro, ciudad, niña, río"],
          ["Propio", "Nombra a alguien o algo concreto y único. Va con mayúscula (lo vio en la Lección 1.1).", "Rocky, Chicago, María, Misisipi"]])}
{C.caja("tip", "Truco para reconocerlo", "<p>Si delante de la palabra puede decir <em>el, la, los, las, un, una</em>, casi seguro es un sustantivo: <em>el carro, la mesa, una sonrisa, las metas</em>.</p>")}
{P("Compruebe", "¿Cuál de estas palabras es un <strong>sustantivo</strong>?", ["rápido", "ventana", "corre"], 1,
   {0: "¿Puede decir «el rápido» de una cosa? Rápido dice cómo es algo.", 2: "Corre dice qué hace alguien: es un verbo."}, "<strong>ventana</strong>: se puede decir <em>la ventana</em>. Nombra un objeto.")}
{P("Compruebe", "¿Cuál es un sustantivo <strong>propio</strong>?", ["ciudad", "Houston", "río"], 1,
   {0: "Ciudad nombra cualquier ciudad: es común.", 2: "Río nombra cualquier río: es común."}, "<strong>Houston</strong>: nombra una ciudad concreta y va con mayúscula.")}"""

    s2 = f"""<p>Si solo usáramos sustantivos, la escritura sería gris: <em>el perro, la casa, la niña</em>. Los <strong>adjetivos</strong> le ponen color: dicen <strong>cómo es</strong> o <strong>cómo está</strong> el sustantivo.</p>
<ul><li><strong>Color:</strong> un suéter <em>verde</em>, una camisa <em>roja</em>.</li><li><strong>Tamaño:</strong> un carro <em>grande</em>, una taza <em>pequeña</em>.</li>
<li><strong>Forma:</strong> una mesa <em>redonda</em>.</li><li><strong>Estado de ánimo:</strong> un niño <em>feliz</em>.</li><li><strong>Otras cualidades:</strong> una sopa <em>caliente</em>, una persona <em>amable</em>.</li></ul>
<p class="oracion-ej">el <span class="fr fr-f">suéter</span> <span class="fr fr-b">verde</span> · la <span class="fr fr-f">casa</span> <span class="fr fr-b">amarilla</span> de mi tía · un <span class="fr fr-f">niño</span> <span class="fr fr-b">feliz</span></p>
<p class="nota-fina">Con borde azul, el sustantivo; con borde punteado naranja, el adjetivo.</p>
{C.caja("tip", "Pregúntele al sustantivo", "<p>¿Cómo es la casa? → <em>amarilla</em>. ¿Cómo está el niño? → <em>feliz</em>. La respuesta es el adjetivo. En español casi siempre va <strong>después</strong> del sustantivo (<em>casa amarilla</em>), al revés que en inglés (<em>yellow house</em>).</p>")}
{P("Compruebe", "¿Cuál es el <strong>adjetivo</strong>?<br><em>Compré una blusa nueva.</em>", ["Compré", "blusa", "nueva"], 2,
   {0: "Compré es lo que hice: un verbo.", 1: "Blusa es el sustantivo: la cosa. ¿Cómo es la blusa?"}, "<strong>nueva</strong>: dice cómo es la blusa.")}
{P("Compruebe", "En <em>El gato negro duerme en el sofá viejo</em>, ¿qué palabras son sustantivos?", ["gato y sofá", "negro y viejo", "duerme y viejo"], 0,
   {1: "Esas dicen cómo son: son adjetivos.", 2: "Duerme es la acción."}, "<strong>gato</strong> y <strong>sofá</strong>. Los adjetivos son <em>negro</em> y <em>viejo</em>.")}"""

    s3 = f"""<div class="caja caja-tip"><span class="etiqueta et-verde">Actividad · en su cuaderno</span>
<p><strong>«Así soy yo».</strong> Escriba 3 oraciones que lo describan a usted, con un sustantivo y un adjetivo:</p>
<ul><li><em>Tengo ojos castaños.</em></li><li><em>Hoy llevo una camisa azul.</em></li><li><em>Mi pelo es corto.</em></li></ul>
<p>Después escriba otras 3 sobre alguien de su familia. Léalas en voz alta y, en cada una, encierre el sustantivo en un círculo y subraye el adjetivo.</p></div>
{C.caja("tip", "Si tiene con quién practicar", "<p>Lea sus oraciones a alguien de su casa sin decir de quién habla. ¿Adivina quién es? Si lo adivina, sus adjetivos funcionaron.</p>")}"""

    textos = "".join(f'<h3>Texto {i} · {t}</h3><div class="texto-lectura"><p>{x.replace("*", "")}</p></div>' for i, (t, x) in enumerate(TEXTOS, 1))
    s4 = f"""<p>Lea en voz alta estos tres textos. En su cuaderno, haga una tabla con cuatro columnas (<em>persona, lugar, objeto, idea</em>) y anote los sustantivos de cada texto. Después compruebe en la <a href="{C.prac(N)}#detective">página de práctica</a>, donde puede tocarlos uno por uno.</p>
{textos}
{P("Compruebe", "¿Cuántos sustantivos <strong>propios</strong> hay en el Texto 3?", ["1", "3", "5"], 1,
   {0: "Busque los nombres de persona: empiezan con mayúscula y no están al principio de una oración.", 2: "Cuente solo los nombres de persona."}, "<strong>3</strong>: Carlos, Ana y Luis.")}"""

    secciones = [("s1", "Los sustantivos: los que nombran", s1), ("s2", "Los adjetivos: los que describen", s2),
                 ("s3", "Actividad: describir con sustantivos y adjetivos", s3), ("s4", "Lectura: textos descriptivos", s4)]
    tarea = [("Un objeto de mi casa.", "Elija un objeto de su casa y escriba 3 oraciones que lo describan con al menos 2 adjetivos (<em>Mi mesa de cocina es redonda y vieja.</em>). Guárdelas: las usará en la Lección 3.2."),
             ("Diez sustantivos.", "Escriba 5 sustantivos comunes y 5 propios de su vida diaria (<em>autobús, Chicago</em>)."),
             ("Busque adjetivos.", "En un anuncio, una etiqueta o una receta, copie 5 adjetivos con el sustantivo que describen (<em>pan integral, leche fresca</em>).")]
    quiz = [
        ("¿Qué hace un <strong>sustantivo</strong>?", ["Nombra personas, lugares, objetos o ideas", "Dice qué hace alguien", "Dice cómo es algo"], 0, {1: "Eso lo hace el verbo.", 2: "Eso lo hace el adjetivo."}, "El sustantivo <strong>nombra</strong>."),
        ("¿Qué hace un <strong>adjetivo</strong>?", ["Nombra una cosa", "Dice cómo es o cómo está un sustantivo", "Une dos oraciones"], 1, {0: "Eso lo hace el sustantivo.", 2: "Eso lo hacen palabras como y, pero."}, "El adjetivo <strong>describe</strong>."),
        ("¿Cuál es un sustantivo?", ["bonito", "escuela", "camina"], 1, {0: "Bonito dice cómo es algo.", 2: "Camina es una acción."}, "<strong>escuela</strong>: <em>la escuela</em>."),
        ("¿Cuál es un adjetivo?", ["caliente", "café", "toma"], 0, {1: "Café nombra una cosa.", 2: "Toma es una acción."}, "<strong>caliente</strong>: dice cómo está algo."),
        ("¿Qué palabra nombra una <strong>idea</strong> o un sentimiento?", ["mesa", "alegría", "parque"], 1, {0: "Mesa es un objeto.", 2: "Parque es un lugar."}, "<strong>alegría</strong>."),
        ("¿Cuál es un sustantivo <strong>propio</strong>?", ["país", "México", "montaña"], 1, {0: "Es común: cualquier país.", 2: "Es común: cualquier montaña."}, "<strong>México</strong>, con mayúscula."),
        ("¿Cómo se escribe un sustantivo propio?", ["Con mayúscula", "Con minúscula", "Entre comillas"], 0, {1: "Los comunes van con minúscula.", 2: "No hacen falta comillas."}, "Con <strong>mayúscula</strong>."),
        ("¿Cuál es el adjetivo?<br><em>Mi hermana tiene un carro rojo.</em>", ["hermana", "carro", "rojo"], 2, {0: "Hermana es una persona: sustantivo.", 1: "Carro es un objeto: sustantivo."}, "<strong>rojo</strong>."),
        ("¿Qué pregunta ayuda a encontrar el adjetivo?", ["¿Quién?", "¿Cómo es?", "¿Cuándo?"], 1, {0: "¿Quién? busca el sujeto.", 2: "¿Cuándo? busca el tiempo."}, "<strong>¿Cómo es?</strong> o <strong>¿cómo está?</strong>"),
        ("¿Cuántos sustantivos hay?<br><em>El niño come una manzana.</em>", ["1", "2", "3"], 1, {0: "Busque todas las palabras que nombran.", 2: "Come no nombra: es una acción."}, "<strong>2</strong>: niño y manzana."),
        ("¿Qué orden es el más común en español?", ["casa blanca", "blanca casa"], 0, {}, "<strong>casa blanca</strong>: el adjetivo suele ir después del sustantivo."),
        ("En <em>La sopa está caliente</em>, ¿qué palabra describe a la sopa?", ["La", "está", "caliente"], 2, {0: "La es un artículo: acompaña al sustantivo.", 1: "Está une la sopa con su descripción."}, "<strong>caliente</strong>."),
    ]
    filas = [
        ("Reconocer sustantivos", "Encuentro todos los sustantivos de un texto, también las ideas (amor, respeto).", "Encuentro personas y objetos, pero se me pasan las ideas.", "Confundo sustantivos con otras palabras (<a href=\"#s1\">repase la sección 1</a>)."),
        ("Comunes y propios", "Distingo comunes y propios y uso bien la mayúscula.", "A veces olvido la mayúscula.", "No los distingo (<a href=\"#s1\">repase la sección 1</a>)."),
        ("Reconocer adjetivos", "Encuentro el adjetivo preguntando ¿cómo es? o ¿cómo está?", "Lo encuentro cuando va después del sustantivo.", "Lo confundo con el sustantivo (<a href=\"#s2\">repase la sección 2</a>)."),
    ]
    cierre = "<p>Ya conoce a los protagonistas (los sustantivos) y a los que les ponen color (los adjetivos). En la próxima lección verá la regla que los hace bailar juntos: la <strong>concordancia</strong> de género y número.</p>"
    glosario = [("Sustantivo", "Palabra que nombra una persona, un lugar, un objeto o una idea."), ("Sustantivo común", "Nombra cualquier cosa de una clase: <em>perro, ciudad</em>."),
                ("Sustantivo propio", "Nombra algo único y va con mayúscula: <em>Chicago, Ana</em>."), ("Adjetivo", "Palabra que dice cómo es o cómo está un sustantivo."),
                ("Artículo", "Las palabras <em>el, la, los, las, un, una, unos, unas</em>, que acompañan al sustantivo.")]
    conexion = ("<p>Empieza el Tema 3. Ya sabe moverse por el papel, contar sílabas, decodificar y leer con fluidez. Ahora va a conocer a los actores del lenguaje. Piense en una oración como en una película: sin protagonista no hay historia, y sin descripciones la película queda en blanco y negro.</p>"
                "<p><strong>Lo que necesita:</strong> el cuaderno y dos lápices o resaltadores de colores.</p>")
    estd = LE.estandares([], base=["L.2.1", "L.1.2"])
    return C.pagina_leccion(N, LE.titulo(N), "Los sustantivos nombran; los adjetivos les ponen color.", ["L.2.1 · Mayúsculas", "Gramática"],
                            ["<strong>Reconocer</strong> los sustantivos de un texto: personas, lugares, objetos e ideas.", "<strong>Distinguir</strong> sustantivos comunes y propios, y escribir los propios con mayúscula.",
                             "<strong>Encontrar</strong> el adjetivo preguntando ¿cómo es? o ¿cómo está?", "<strong>Describir</strong> personas y cosas con sustantivos y adjetivos."],
                            estd, conexion, secciones, tarea, quiz, filas, cierre, ("3-2", LE.titulo("3-2")), glosario, P)


# ---------------------------------------------------------------- práctica
def banco_clase():
    sus = ["mesa", "Chicago", "alegría", "doctora", "zapato", "ciudad", "amor", "ventana", "trabajo", "María", "libertad", "cocina"]
    adj = ["rojo", "feliz", "grande", "caliente", "amable", "redonda", "cansado", "nuevo", "limpia", "triste", "fuerte", "verde"]
    otros = ["corre", "come", "estudia", "duerme"]
    b = []
    for w in sus:
        b.append({"enun": f"¿Qué es <strong class=\"grande\">{w}</strong>?", "ops": ["Sustantivo (nombra)", "Adjetivo (describe)", "Verbo (acción)"], "ok": 0, "enOrden": True,
                  "pista": "¿Puede decir «el», «la» o «un» delante?", "exp": f"<strong>{w}</strong> nombra algo: es un sustantivo."})
    for w in adj:
        b.append({"enun": f"¿Qué es <strong class=\"grande\">{w}</strong>?", "ops": ["Sustantivo (nombra)", "Adjetivo (describe)", "Verbo (acción)"], "ok": 1, "enOrden": True,
                  "pista": "¿Responde a «¿cómo es?» o «¿cómo está?»?", "exp": f"<strong>{w}</strong> dice cómo es o cómo está algo: es un adjetivo."})
    for w in otros:
        b.append({"enun": f"¿Qué es <strong class=\"grande\">{w}</strong>?", "ops": ["Sustantivo (nombra)", "Adjetivo (describe)", "Verbo (acción)"], "ok": 2, "enOrden": True,
                  "pista": "¿Dice qué hace alguien?", "exp": f"<strong>{w}</strong> dice lo que alguien hace: es un verbo (lo verá en la Lección 3.3)."})
    return b


def banco_detective():
    b = [{"consigna": f"Texto «{t}»: toque todos los <strong>sustantivos</strong>.", "texto": x, "pista": "Pregúntese en cada palabra: ¿puedo decir el, la o un delante? No olvide las ideas, como amor o paciencia.",
          "exp": "Fíjese en los sustantivos de idea: no se tocan, pero se nombran."} for t, x in TEXTOS]
    cortas = [("El *perro* negro duerme en la *cama*.", "sustantivos"), ("Mi *hermana* compró una *blusa* nueva en la *tienda*.", "sustantivos"),
              ("La *maestra* explica la *lección* con *paciencia*.", "sustantivos"), ("El *café* está caliente y la *leche* está fría.", "sustantivos"),
              ("Mi *perro* es *negro* y muy *juguetón*.", None), ("La sopa *caliente* tiene un olor *rico*.", "adjetivos"), ("Tengo una casa *pequeña* y un jardín *bonito*.", "adjetivos"),
              ("El niño *feliz* juega con una pelota *roja*.", "adjetivos"), ("Mi jefe es *amable* y *paciente*.", "adjetivos")]
    for x, que in cortas:
        if que is None:
            continue
        b.append({"consigna": f"Toque todos los <strong>{que}</strong>.", "texto": x,
                  "pista": "Sustantivo: ¿puedo decir el o la delante?" if que == "sustantivos" else "Adjetivo: responde a ¿cómo es? o ¿cómo está?", "exp": ""})
    return b


def banco_describe():
    datos = [("¿Cómo es el cielo de noche?", "oscuro", ["dormir", "estrella"]), ("¿Cómo está una persona que no durmió?", "cansada", ["cama", "dormir"]),
             ("¿Cómo es un elefante?", "grande", ["selva", "come"]), ("¿Cómo está el café recién hecho?", "caliente", ["taza", "toma"]),
             ("¿Cómo es una persona que ayuda a todos?", "amable", ["ayuda", "vecina"]), ("¿Cómo es un limón?", "amarillo", ["jugo", "corta"]),
             ("¿Cómo está la ropa después de lavarla?", "limpia", ["lavadora", "lava"]), ("¿Cómo es un camino sin curvas?", "recto", ["calle", "camina"])]
    return [{"enun": q, "ops": [ok] + d, "ok": 0, "pista": "Busque la palabra que describe, no la que nombra ni la que dice una acción.",
             "exp": f"<strong>{ok}</strong> es el adjetivo."} for q, ok, d in datos]


def practica():
    mods = [
        ("clase", "¿Sustantivo, adjetivo o verbo?", C.om("m1", "Pregúntese: ¿nombra algo?, ¿dice cómo es?, ¿dice qué hace?")),
        ("detective", "Detective de sustantivos y adjetivos", LE.marcar("m2", "Toque las palabras que se piden. Si se equivoca, vuelva a tocarla para quitar la marca. Después pulse <strong>Comprobar</strong>.")),
        ("describir", "La palabra que describe", C.om("m3", "Elija el adjetivo que responde a la pregunta.")),
    ]
    js = (C.js_datos("CLA", banco_clase()) + C.js_datos("DET", banco_detective()) + C.js_datos("DES", banco_describe()) +
          'creaBanco("m1", CLA);\ncreaMarcar("m2", DET);\ncreaBanco("m3", DES);\n')
    return C.pagina_practica(N, LE.titulo(N), "Tres actividades · los ejercicios cambian cada vez · dos intentos en cada uno", mods, js)


if __name__ == "__main__":
    LE.construye(N, leccion, practica, horas="Unas 3 horas")
