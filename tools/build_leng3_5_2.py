# -*- coding: utf-8 -*-
"""LearnGED · Artes del lenguaje (español) · Nivel 3 · Lección 5.2 · Integrar información de dos textos.
Fuente: clases_leng3/clase_5-2.html (GEDparaHispanos) y gramatica/n3-l5-2.html, adaptadas al marco de LearnGED.
Datos: Academia Estadounidense de Medicina del Sueño, declaración de postura de 2024 (aasm.org); Departamento de Energía de los EE. UU.,
«Impact of Extended Daylight Saving Time on National Energy Consumption», informe al Congreso de octubre de 2008. Consultados en noviembre de 2026.
Uso: python3 tools/build_leng3_5_2.py
"""
import os, sys, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import leng_es as LE
from leng_es import C

LE.nivel(3)
N = "5-2"
AB = ["Texto A", "Texto B", "Los dos"]
REL = ["Coinciden", "Se complementan", "Se contradicen"]
TA = ["El horario de verano consiste en adelantar los relojes una hora en primavera y atrasarlos en otoño, para que oscurezca más tarde durante los meses largos del año.",
      "Estados Unidos lo adoptó por primera vez en 1918, durante la Primera Guerra Mundial, con la idea de ahorrar energía: si hay luz por la tarde, se encienden menos lámparas. En 1966, una ley federal ordenó las fechas para todo el país, aunque permitió que cada estado decidiera no seguirlo.",
      "Desde 2007, el cambio se hace el segundo domingo de marzo y se deshace el primer domingo de noviembre. Sus defensores dicen que esa hora extra de luz por la tarde favorece las compras, los deportes y las actividades al aire libre después del trabajo."]
TB = ["Para el cuerpo, perder una hora no es poca cosa. Varios estudios han encontrado que en los días que siguen al cambio de primavera aumentan los accidentes de tránsito y los ataques al corazón, porque millones de personas duermen menos.",
      "Por eso, la Academia Estadounidense de Medicina del Sueño recomienda dejar de cambiar la hora y quedarse todo el año con el horario estándar, el de invierno, que se ajusta mejor al reloj interno del cuerpo.",
      "¿Y el ahorro de energía? Un informe del gobierno federal de 2008 calculó que alargar el horario de verano en 2007 ahorró alrededor de medio punto por ciento de electricidad en cada uno de esos días. Hawái y casi todo Arizona, por su parte, no cambian la hora."]
PARES = [("Las bicicletas compartidas llegaron a la ciudad en 2013. Hoy hay estaciones en casi todos los barrios, y un viaje corto cuesta menos que el autobús.", "Muchos ciclistas se quejan de que en invierno las estaciones quedan cubiertas de nieve. Además, en los barrios del sur hay menos estaciones que en el centro."),
         ("Comer pescado dos veces por semana ayuda al corazón, según la mayoría de los médicos, porque contiene grasas saludables.", "Algunos pescados grandes, como el pez espada, acumulan mercurio. Por eso a las mujeres embarazadas se les recomienda elegir pescados pequeños, como la sardina."),
         ("El museo de ciencias del barrio es gratuito para los niños menores de doce años todos los días de la semana.", "En el museo de ciencias del barrio, la entrada para niños cuesta cinco dólares, salvo los martes, que es gratis."),
         ("Los huertos escolares enseñan ciencias de manera práctica: los niños miden, observan y registran el crecimiento de las plantas.", "En las escuelas que tienen huerto, los maestros dicen que los alumnos entienden mejor las lecciones de ciencias porque las ven con sus propios ojos.")]
DQ = [(0, "Las bicicletas compartidas llegaron en 2013.", 0, "Solo el texto A da la fecha."), (0, "En invierno, la nieve cubre las estaciones.", 1, "Es una queja que solo recoge el texto B."),
      (0, "Hay estaciones de bicicletas en varios barrios.", 2, "A dice que hay en casi todos los barrios y B compara el sur con el centro."), (1, "El pescado ayuda al corazón.", 0, "Solo el texto A habla del corazón."),
      (1, "Algunos pescados tienen mercurio.", 1, "Solo el texto B lo menciona."), (1, "Hay consejos de salud sobre comer pescado.", 2, "Los dos dan recomendaciones sobre el pescado."),
      (3, "Los niños miden y registran el crecimiento de las plantas.", 0, "Lo describe el texto A."), (3, "Los maestros opinan sobre los huertos escolares.", 1, "Solo el texto B recoge lo que dicen los maestros."),
      (3, "Los huertos ayudan a aprender ciencias.", 2, "Los dos lo dicen, cada uno a su manera.")]
CC = [(2, "el precio de la entrada para niños", 2, "A dice que es gratis todos los días; B, que cuesta cinco dólares salvo los martes."),
      (3, "lo que aportan los huertos al aprendizaje de ciencias", 0, "Los dos dicen que ayudan a aprender ciencias."),
      (1, "los beneficios y los riesgos de comer pescado", 1, "A da el beneficio y B añade un riesgo y un consejo: no se oponen."),
      (0, "la situación de las bicicletas compartidas", 1, "A da la historia y el precio; B añade problemas que A no menciona."),
      (("Según el censo, la población del barrio creció en los últimos diez años.", "Un informe de la ciudad dice que en la última década el barrio perdió habitantes."), "la población del barrio en los últimos diez años", 2, "Uno dice que creció y el otro que bajó."),
      (("El parque abre de seis de la mañana a once de la noche.", "Los guardias del parque cierran las puertas a las once de la noche."), "la hora de cierre del parque", 0, "Los dos dicen que cierra a las once."),
      (("La biblioteca presta libros electrónicos con la tarjeta de la biblioteca.", "Para leer los libros electrónicos de la biblioteca se necesita una aplicación gratuita en el celular."), "los libros electrónicos de la biblioteca", 1, "B añade cómo se leen, algo que A no dice."),
      (("La cafetería del centro abre a las siete de la mañana.", "Desde las siete de la mañana ya se puede desayunar en la cafetería del centro."), "la hora en que abre la cafetería", 0, "Los dos dicen lo mismo con otras palabras.")]
CO = [(0, ["Las bicicletas compartidas son baratas y llegan a muchos barrios, aunque tienen problemas en invierno y en el sur.", "Las bicicletas compartidas llegaron a la ciudad en el año 2013 y hoy están en todas partes de la ciudad.", "Las bicicletas compartidas no sirven para nada porque se llenan de nieve en el invierno."], "Usa los dos textos sin exagerar. La segunda solo usa A; la tercera exagera lo que dice B."),
      (1, ["Comer pescado es bueno para el corazón, pero conviene elegir pescados pequeños por el mercurio.", "Hay que dejar de comer pescado porque todos los pescados tienen mercurio peligroso.", "Los médicos recomiendan comer pescado dos veces por semana para cuidar el corazón."], "Integra el beneficio de A y el consejo de B. La segunda contradice a A y exagera a B."),
      (3, ["Los huertos escolares ayudan a aprender ciencias porque los niños practican y ven lo que estudian.", "Los huertos escolares sirven para que los niños coman verduras frescas en la escuela.", "Los maestros de las escuelas con huerto opinan sobre cómo aprenden sus alumnos."], "Junta lo que hacen los niños (A) con lo que observan los maestros (B). La segunda habla de algo que no dice ningún texto."),
      (2, ["Los textos no coinciden sobre el precio para niños: hay que averiguarlo antes de ir al museo.", "La entrada al museo de ciencias es siempre gratis para todos los niños menores de doce.", "La entrada al museo de ciencias cuesta cinco dólares todos los días de la semana."], "Cuando los textos se contradicen, una buena conclusión lo reconoce. Las otras dos eligen un texto e ignoran el otro.")]


def par(a, b):
    return f'<div class="dos-textos"><div class="texto-breve"><p><strong>Texto A.</strong> {a}</p></div><div class="texto-breve"><p><strong>Texto B.</strong> {b}</p></div></div>'


def leccion():
    P = C.Practicas()
    s1 = f"""<p>Dos veces al año, en los Estados Unidos, movemos el reloj una hora. ¿Para qué? Si lee un solo artículo, quizá se quede con una sola respuesta. Si lee dos, escritos desde ángulos distintos, empieza a ver el tema completo, con sus ventajas y sus costos. En el GED, varias preguntas presentan dos textos sobre el mismo asunto y piden juntar lo que dicen.</p>
<p>En el Nivel 2 aprendió a <strong>comparar</strong> dos textos: en qué se parecen y en qué se diferencian. <strong>Integrar</strong> es un paso más: es juntar lo que dicen para construir una idea que ninguno de los dos dice solo.</p>
{C.tabla("Diferencia entre comparar e integrar", ["Comparar", "Integrar"],
         [["«El texto A habla de la historia; el texto B, de la salud.»", "«El cambio de hora se creó para ahorrar energía, pero hoy ahorra poca y afecta el sueño de millones de personas.»"]], fila_th=False)}"""

    s2 = f"""{C.tabla("Relaciones entre dos textos y frases para expresarlas", ["Relación", "Qué significa", "Frases para decirlo"],
         [["Coinciden", "Los dos dicen lo mismo, aunque con otras palabras.", "Ambos textos señalan que… · Los dos coinciden en…"],
          ["Se complementan", "Uno añade información que el otro no tiene.", "El texto B añade que… · A esto, el texto A suma…"],
          ["Se contradicen", "Dicen cosas opuestas sobre el mismo punto.", "Mientras que el texto A sostiene…, el texto B afirma… · Sin embargo, según el texto B…"]])}
{C.caja("ojo", "¿De quién es cada dato?", "<p>Al integrar, es fácil mezclar las fuentes. Antes de escribir, anote de qué texto sale cada información. En el GED hay preguntas que lo piden directamente: «¿Qué información aparece solo en el texto 2?».</p>")}
{P("Relación", "Dos textos <strong>se complementan</strong> cuando…", ["dicen cosas opuestas sobre lo mismo", "uno añade información que el otro no tiene", "dicen exactamente las mismas palabras"], 1, {0: "Eso es contradecirse.", 2: "Eso es coincidir."}, "Uno <strong>añade</strong> lo que el otro no tiene.")}"""

    a = "".join(f'<p><span class="num-p" aria-hidden="true">{i}</span>{p}</p>' for i, p in enumerate(TA, 1))
    b = "".join(f'<p><span class="num-p" aria-hidden="true">{i}</span>{p}</p>' for i, p in enumerate(TB, 1))
    s3 = f"""<p>Lea los dos textos. Mientras lee, marque en su cuaderno con una A o una B lo que aporta cada uno. Después responda las preguntas.</p>
<div class="dos-textos">
<div class="articulo"><p><strong>Texto A · Una hora más de luz</strong></p><p>{LE.escuchar(" ".join(TA), "Escuchar el texto A")}</p>{a}</div>
<div class="articulo"><p><strong>Texto B · El precio de mover el reloj</strong></p><p>{LE.escuchar(" ".join(TB), "Escuchar el texto B")}</p>{b}</div></div>
<p class="fuente">Datos del texto B: Academia Estadounidense de Medicina del Sueño, declaración de postura de 2024 (aasm.org); Departamento de Energía de los EE. UU., informe al Congreso sobre el horario de verano extendido, octubre de 2008. Consultados en noviembre de 2026.</p>
<h3>¿De qué texto sale?</h3>
{P("Fuente 1", "«Estados Unidos adoptó el horario de verano en 1918.»", AB, 0, {1: "Busque en el texto A, párrafo 2.", 2: "El texto B no habla de la historia."}, "<strong>Texto A</strong>, párrafo 2.")}
{P("Fuente 2", "«Después del cambio de primavera aumentan los accidentes de tránsito.»", AB, 1, {0: "El texto A no habla de accidentes.", 2: "Solo uno lo dice."}, "<strong>Texto B</strong>, párrafo 1.")}
{P("Fuente 3", "«El cambio de hora se relaciona con el ahorro de energía.»", AB, 2, {0: "El texto B también habla de energía.", 1: "El texto A también habla de energía."}, "<strong>Los dos</strong>: A como la razón original y B para decir que el ahorro es pequeño.")}
{P("Fuente 4", "«Un estado puede decidir no seguir el horario de verano.»", AB, 2, {0: "B da ejemplos de estados que no lo siguen.", 1: "A explica que la ley lo permite."}, "<strong>Los dos</strong>: A explica que la ley lo permite y B da los ejemplos de Hawái y Arizona.")}"""

    s4 = f"""<p>Una <strong>tabla de integración</strong> pone lado a lado lo que dice cada texto sobre cada aspecto y, en la última columna, lo que se entiende al juntarlos.</p>
{C.tabla("Tabla de integración de los dos textos sobre el cambio de hora", ["Aspecto", "Texto A", "Texto B", "Juntos"],
         [["Origen y fechas", "Desde 1918; fechas actuales desde 2007.", "—", "Solo A lo explica: se complementan."],
          ["Ahorro de energía", "Fue la razón original.", "Hoy el ahorro es de alrededor de medio punto por ciento en esos días.", "El propósito original casi no se cumple: B pone en duda lo que A presenta como razón."],
          ["Efectos en las personas", "Más luz para actividades por la tarde.", "Menos sueño, más accidentes e infartos tras el cambio.", "Tiene un beneficio y un costo: miran el tema desde lados opuestos."],
          ["Quién no lo sigue", "La ley permite que un estado no lo siga.", "Hawái y casi todo Arizona no cambian la hora.", "B da los ejemplos de lo que A explica: se complementan."]])}
{P("Tabla 1", "Sobre el <strong>ahorro de energía</strong>, ¿cómo se relacionan los textos?", ["Los dos dicen exactamente lo mismo", "B pone en duda la razón que presenta A", "Solo uno de los dos textos habla de ello"], 1, {0: "A lo da como razón; B dice que es pequeño.", 2: "Los dos hablan de energía."}, "A dice que se creó para ahorrar energía; B, que hoy ahorra muy poco.")}
{P("Tabla 2", "Sobre la <strong>historia del cambio de hora</strong>, ¿cómo se relacionan?", ["Se contradicen: dan fechas distintas", "Coinciden: los dos dan las mismas fechas", "Se complementan: solo A la cuenta"], 2, {0: "B no da fechas.", 1: "B no da fechas."}, "B no habla de la historia; A la aporta.")}"""

    s5 = f"""<p>La <strong>conclusión conjunta</strong> es la idea que usted construye con los dos textos. Debe usar información de ambos y no puede contradecir a ninguno.</p>
<div class="texto-breve"><p><strong>Modelo.</strong> El horario de verano se creó en 1918 para ahorrar energía, y sus defensores destacan que da más luz por la tarde (texto A). <strong>Sin embargo</strong>, según el texto B, hoy ese ahorro es muy pequeño y el cambio de primavera reduce el sueño y aumenta los accidentes. <strong>Al leer los dos textos se entiende que</strong> el cambio de hora tiene un beneficio real para el tiempo libre, pero que su propósito original casi no se cumple y tiene costos para la salud.</p></div>
{C.caja("tip", "Las tres partes del modelo", "<p>Lo que dice A, lo que dice B (con un conector que muestra la relación: <em>sin embargo</em>) y la idea nueva (<em>Al leer los dos textos se entiende que…</em>).</p>")}
{P("Conclusión 1", "¿Qué conclusión integra mejor los dos textos?", ["El cambio de hora es una costumbre que viene de la Primera Guerra Mundial.", "El cambio de hora da más luz por la tarde, pero ahorra poca energía y afecta el sueño.", "El cambio de hora causa ataques al corazón y por eso hay que prohibirlo ya."], 1,
   {0: "Solo usa el texto A.", 2: "Exagera lo que dice B."}, "Usa información de los dos textos sin contradecirlos.")}
{P("Conclusión 2", "¿Qué conclusión <strong>contradice</strong> a uno de los textos?", ["El cambio de hora tiene ventajas y desventajas.", "No todos los estados cambian la hora.", "El cambio de hora ahorra muchísima energía cada año."], 2, {0: "Es fiel a los dos.", 1: "Lo dicen los dos."}, "El texto B dice que el ahorro es muy pequeño.")}
{C.caja("tip", "Si tiene con quién practicar", "<p>Cada uno busca una noticia sobre el mismo tema en un medio distinto (un periódico y la televisión, por ejemplo). Luego cuéntense qué dijo cada uno y lleguen juntos a una conclusión.</p>")}"""

    secciones = [("s1", "De comparar a integrar", s1), ("s2", "Tres relaciones entre dos textos", s2), ("s3", "Lectura: dos textos sobre el cambio de hora", s3),
                 ("s4", "La tabla de integración", s4), ("s5", "La conclusión conjunta", s5)]
    tarea = [("Su conclusión.", "Escriba con sus palabras una conclusión conjunta de los dos textos de la lección, con las tres partes del modelo."),
             ("Dos fuentes reales.", "Busque dos artículos cortos sobre un mismo tema que le interese (el precio de la vivienda, un deporte, una enfermedad). Haga su tabla de integración con tres aspectos."),
             ("Su opinión, con fuentes.", "¿Cree que los Estados Unidos deberían dejar de cambiar la hora? Escriba un párrafo que use al menos un dato de cada texto.")]
    quiz = [
        ("¿Qué es integrar dos textos?", ["Juntar lo que dicen para construir una idea nueva", "Copiar las mejores oraciones de cada uno", "Elegir el texto más largo y leer solo ese"], 0, {1: "Eso es copiar.", 2: "Así se pierde la mitad."}, "Juntar para construir una <strong>idea nueva</strong>."),
        ("¿Qué frase introduce una <strong>contradicción</strong> entre textos?", ["Mientras que el texto A sostiene…, el texto B afirma…", "Ambos textos coinciden en señalar que…", "El texto B añade a lo anterior que…"], 0, {1: "Indica que coinciden.", 2: "Indica que se complementan."}, "<strong>Mientras que…</strong>"),
        ("¿Qué información aparece <strong>solo</strong> en el texto A?", ["El año en que se adoptó el horario de verano", "El efecto del cambio en el sueño", "La recomendación de una academia de médicos"], 0, {1: "Está en B.", 2: "Está en B."}, "El año: <strong>1918</strong>."),
        ("¿Qué recomienda la Academia Estadounidense de Medicina del Sueño?", ["Quedarse todo el año con el horario estándar", "Quedarse todo el año con el horario de verano", "Cambiar la hora tres veces al año"], 0, {1: "Es al revés.", 2: "No."}, "El <strong>horario estándar</strong> todo el año."),
        ("Una buena conclusión conjunta…", ["usa los dos textos y no contradice a ninguno", "usa solo el texto que más le gusta", "repite el título de cada texto"], 0, {1: "Debe usar los dos.", 2: "No basta."}, "Usa los <strong>dos</strong> y no contradice a ninguno."),
        ("¿Para qué sirve una tabla de integración?", ["Para ver lado a lado lo que dice cada texto", "Para contar las palabras de cada texto", "Para copiar el primer párrafo de cada uno"], 0, {1: "No.", 2: "No."}, "Para ver <strong>lado a lado</strong>."),
        ("Cuando dos textos se contradicen, una buena conclusión…", ["reconoce el desacuerdo", "elige uno e ignora el otro", "repite los dos sin explicar"], 0, {1: "Así se pierde información.", 2: "Falta la idea nueva."}, "<strong>Reconoce</strong> el desacuerdo."),
        ("Dos textos dicen lo mismo con otras palabras. ¿Cómo se relacionan?", ["Coinciden", "Se complementan", "Se contradicen"], 0, {1: "Ninguno añade nada nuevo.", 2: "No se oponen."}, "<strong>Coinciden.</strong>"),
        ("¿Qué conviene hacer antes de escribir una conclusión conjunta?", ["Anotar de qué texto sale cada dato", "Leer solo el primer párrafo de cada texto", "Elegir el texto que tenga más cifras"], 0, {1: "No basta.", 2: "No."}, "Anotar de <strong>qué texto</strong> sale cada dato."),
        ("En el modelo de conclusión, ¿qué hace «Al leer los dos textos se entiende que…»?", ["Presenta la idea nueva que sale de juntarlos", "Resume solo el primer texto", "Da la opinión personal de quien escribe"], 0, {1: "No.", 2: "No."}, "Presenta la <strong>idea nueva</strong>."),
    ]
    filas = [
        ("Relaciones", "Reconozco si los textos coinciden, se complementan o se contradicen.", "Dudo entre complementar y coincidir.", "No las distingo (<a href=\"#s2\">repase la sección 2</a>)."),
        ("De qué texto sale", "Sé de qué texto sale cada dato.", "A veces mezclo las fuentes.", "Me confundo (<a href=\"#s3\">repase la sección 3</a>)."),
        ("Conclusión conjunta", "Escribo una conclusión con los dos textos y una idea nueva.", "Uso los dos, pero sin idea nueva.", "Uso solo uno (<a href=\"#s5\">repase la sección 5</a>)."),
    ]
    cierre = "<p>Ya integra dos textos y llega a una conclusión conjunta. En la próxima lección verá las <strong>fuentes primarias y secundarias</strong>: cómo citarlas y relacionarlas.</p>"
    glosario = [("Integrar", "Juntar lo que dicen dos textos para construir una idea nueva."), ("Complementarse", "Cuando un texto añade información que el otro no tiene."),
                ("Contradecirse", "Cuando dos textos dicen cosas opuestas sobre lo mismo."), ("Conclusión conjunta", "Idea que se construye con información de los dos textos.")]
    conexion = ("<p>En la Lección 5.1 del Nivel 2 comparó dos textos y en la 5.1 de este nivel evaluó un argumento. Hoy junta dos fuentes para entender mejor un tema.</p>"
                "<p><strong>Lo que necesita:</strong> su cuaderno para hacer la tabla de integración.</p>")
    estd = LE.estandares(["R.7.2", "R.7.4"], base=["R.7.3", "W.1"])
    return C.pagina_leccion(N, LE.titulo(N), "Dos textos, una idea nueva.", ["Argumentos", "Integrar fuentes"],
                            ["<strong>Reconocer</strong> si dos textos coinciden, se complementan o se contradicen.", "<strong>Saber</strong> de qué texto sale cada dato.",
                             "<strong>Organizar</strong> la información en una tabla de integración.", "<strong>Escribir</strong> una conclusión conjunta."],
                            estd, conexion, secciones, tarea, quiz, filas, cierre, ("5-3", LE.titulo("5-3")), glosario, P)


def practica():
    dq = [{"enun": par(*PARES[p]) + f'<p class="rel">{t}</p><p><strong>¿De dónde sale esta información?</strong></p>', "ops": AB, "ok": k, "enOrden": True,
           "pista": "Vuelva a leer los dos textos y busque esa información en cada uno.", "exp": f"<strong>{AB[k]}.</strong> {n}"} for p, t, k, n in DQ]
    cc = [{"enun": par(*(PARES[p] if isinstance(p, int) else p)) + f'<p class="rel">Sobre {t}</p><p><strong>¿Cómo se relacionan los textos?</strong></p>', "ops": REL, "ok": k, "enOrden": True,
           "pista": "¿Dicen lo mismo, uno añade algo que el otro no dice, o dicen cosas opuestas?", "exp": f"<strong>{REL[k]}.</strong> {n}"} for p, t, k, n in CC]
    co = [{"enun": par(*PARES[p]) + "<p><strong>¿Qué conclusión integra mejor los dos textos?</strong></p>", "ops": o, "ok": 0,
           "pista": "¿Esa conclusión usa información de los dos textos? ¿Contradice o exagera alguno?", "exp": n} for p, o, n in CO]
    mods = [("de-donde", "¿De qué texto sale?", C.om("m1", "Lea los dos textos y decida de dónde sale cada información.") + '<p class="fuente">Textos breves creados para practicar.</p>'),
            ("relacion", "¿Coinciden, se complementan o se contradicen?", C.om("m2", "Decida cómo se relacionan los dos textos sobre el punto indicado.")),
            ("conclusion", "La conclusión que integra", C.om("m3", "Elija la conclusión que usa los dos textos sin contradecirlos."))]
    js = C.js_datos("DQ", dq) + C.js_datos("CC", cc) + C.js_datos("CO", co) + 'creaBanco("m1", DQ);\ncreaBanco("m2", CC);\ncreaBanco("m3", CO);\n'
    return C.pagina_practica(N, LE.titulo(N), "Tres actividades · los ejercicios cambian cada vez · dos intentos en cada uno", mods, js)


if __name__ == "__main__":
    LE.construye(N, leccion, practica, horas="Unas 3 horas")
