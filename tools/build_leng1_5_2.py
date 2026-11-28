# -*- coding: utf-8 -*-
"""LearnGED · Artes del lenguaje (español) · Nivel 1 · Lección 5.2 · El escenario.
Fuente: clases_leng1/clase_5-2.html (GEDparaHispanos) y gramatica/n1-l5-2.html, adaptadas al marco de LearnGED.
Uso: python3 tools/build_leng1_5_2.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import leng_es as LE
from leng_es import C

LE.nivel(1)
N = "5-2"
SENT = ["Vista", "Oído", "Olfato", "Gusto", "Tacto"]
ORGANO = ["con los ojos", "con los oídos", "con la nariz", "con la boca, al saborear", "con la piel, al tocar o sentir"]
DETALLES = [("El cielo se puso rojo y morado al atardecer.", 0), ("Las paredes estaban pintadas de un amarillo muy brillante.", 0), ("A lo lejos se veían las luces del puerto.", 0), ("Un rayo iluminó toda la habitación.", 0),
            ("Se oía el canto de los gallos a lo lejos.", 1), ("La música del vecino retumbaba en las paredes.", 1), ("Solo se escuchaba el goteo de la llave del baño.", 1), ("La puerta chirrió al abrirse.", 1),
            ("La cocina olía a cebolla frita y a ajo.", 2), ("El aroma de las flores llenaba el patio.", 2), ("El metro olía a humedad y a encierro.", 2), ("Desde la esquina llegaba el olor del pan recién horneado.", 2),
            ("El café estaba tan amargo que tuve que echarle azúcar.", 3), ("El mango estaba dulce y jugoso.", 3), ("La sopa sabía demasiado a sal.", 3), ("El chile me picó en la lengua por un buen rato.", 3),
            ("La arena de la playa me quemaba los pies.", 4), ("La sábana estaba suave y fresca.", 4), ("El viento helado me cortaba la cara.", 4), ("La pared áspera me raspó el brazo.", 4)]
# (escenario, atmósfera correcta, dos distractores)
ATMOS = [("Una habitación oscura, sin muebles; solo se oye el viento entre las tablas rotas.", "Soledad y abandono", ["Fiesta y alegría", "Calma y hogar"]),
         ("Un patio lleno de sol, niños que corren y olor a comida en el fogón.", "Alegría y vida familiar", ["Miedo y peligro", "Tristeza y soledad"]),
         ("Un callejón sin luz a medianoche; se oyen pasos detrás.", "Miedo y tensión", ["Calma y paz", "Alegría y fiesta"]),
         ("Una sala de espera de hospital, con luces blancas y un reloj que no avanza.", "Angustia e incertidumbre", ["Alegría y celebración", "Aventura y libertad"]),
         ("Una playa al amanecer, con olas suaves y el cielo rosado.", "Calma y esperanza", ["Prisa y confusión", "Miedo y amenaza"]),
         ("Una estación de autobuses a la hora pico: gente que empuja, bocinas, anuncios a gritos.", "Prisa y confusión", ["Calma y descanso", "Tristeza y soledad"]),
         ("Una cocina tibia, con olor a café y la radio encendida bajito.", "Calidez y hogar", ["Miedo y tensión", "Angustia y prisa"]),
         ("Un cementerio bajo la lluvia, con flores marchitas sobre las tumbas.", "Tristeza y duelo", ["Fiesta y alegría", "Aventura y emoción"]),
         ("Una plaza con banda de música, banderitas de colores y olor a algodón de azúcar.", "Fiesta y alegría", ["Soledad y abandono", "Miedo y peligro"]),
         ("Un bosque al anochecer, con ramas que crujen y sombras que se mueven.", "Miedo y misterio", ["Calma y hogar", "Alegría y fiesta"]),
         ("Un cuarto de hospital vacío, con la cama hecha y una flor seca en la mesa.", "Tristeza y ausencia", ["Alegría y celebración", "Prisa y confusión"]),
         ("La cima de una montaña, con aire fresco y todo el valle a sus pies.", "Libertad y asombro", ["Encierro y angustia", "Miedo y peligro"])]
# (frase, 0 lugar / 1 tiempo)
LUGTIEM = [("en la cocina de la abuela", 0), ("una tarde de domingo", 1), ("en la parada del autobús", 0), ("en el invierno de 1980", 1), ("a medianoche", 1), ("en un pueblo de la sierra", 0),
           ("durante la tormenta", 1), ("en la sala de espera", 0), ("al amanecer", 1), ("en el mercado del barrio", 0), ("en plena Navidad", 1), ("junto al río", 0)]
COCINA = ["Era una tarde de domingo, y la cocina de la abuela olía a café recién colado y a galletas de canela. La luz amarilla del sol entraba por la ventana y dibujaba cuadros tibios sobre el piso de baldosas. Afuera se oía el rumor lejano del tráfico, pero adentro solo se escuchaba el tic-tac del reloj de pared.",
          "La abuela me sirvió una taza. La cerámica caliente me quemó un poco los dedos, pero no me importó. Mordí una galleta y el sabor dulce y especiado me llenó la boca. Me senté junto a ella, sin hablar, y por un momento sentí que el mundo se había detenido en aquella cocina pequeña y luminosa."]


def leccion():
    P = C.Practicas()
    s1 = f"""<p>Los personajes no flotan en el aire: viven en un <strong>escenario</strong>. El escenario es todo lo que los rodea, y tiene tres elementos:</p>
{C.tabla("Los tres elementos del escenario", ["Elemento", "Pregunta", "Ejemplos"],
         [["📍 Lugar", "¿Dónde ocurre?", "Una cocina, un parque, un hospital, una ciudad."],
          ["🕒 Tiempo", "¿Cuándo ocurre?", "De noche, en invierno, en 1950, durante una guerra."],
          ["🌫️ Ambiente", "¿Cómo se siente estar allí?", "Frío, alegre, peligroso, acogedor."]])}
{C.caja("tip", "Idea central", "<p>El escenario responde a <strong>¿dónde?</strong> y <strong>¿cuándo?</strong>, pero los buenos autores agregan una tercera pregunta: <strong>¿cómo se siente estar allí?</strong> El escenario no es un simple fondo: crea un ambiente y a veces anuncia lo que va a pasar.</p>")}
{P("Compruebe", "<em>«una tarde de domingo»</em> dice…", ["el lugar", "el tiempo", "el ambiente"], 1, {0: "No dice dónde.", 2: "No dice cómo se siente."}, "El <strong>tiempo</strong>: cuándo ocurre.")}"""

    s2 = f"""<h3>Los cinco sentidos</h3>
<p>Para que el lector «entre» en la historia, el autor usa <strong>detalles sensoriales</strong>: lo que se ve, se oye, se huele, se saborea y se toca.</p>
{C.tabla("Los detalles de los cinco sentidos", ["Sentido", "Qué capta", "Ejemplo"],
         [["👁️ Vista", "Colores, formas, luz.", "La luz amarilla entraba por la ventana."], ["👂 Oído", "Ruidos, voces, silencio.", "Solo se oía el tic-tac del reloj."],
          ["👃 Olfato", "Aromas y malos olores.", "La cocina olía a café recién colado."], ["👅 Gusto", "Dulce, amargo, salado, picante.", "El sabor dulce de la galleta."],
          ["✋ Tacto", "Frío, calor, suave, áspero.", "La taza caliente me quemó los dedos."]])}
<h3>El escenario y las emociones</h3>
<p>El clima, la luz y los sonidos suelen <strong>coincidir</strong> con lo que sienten los personajes y anuncian lo que va a sentir el lector.</p>
{C.tabla("Detalles del escenario y la emoción que suelen provocar", ["Detalle", "Emoción que suele provocar"],
         [["Lluvia fuerte, cielo gris, viento", "Tristeza, soledad, algo malo por venir."], ["Sol brillante, pájaros, flores", "Alegría, esperanza, un comienzo."],
          ["Casa silenciosa, sombras, frío", "Miedo, tensión."], ["Cocina con olor a comida, voces conocidas", "Calidez, hogar, seguridad."], ["Calle ruidosa, mucha gente, prisa", "Confusión, ansiedad."]])}
{C.caja("ojo", "A veces el autor busca el contraste", "<p>Un personaje triste en un día de sol puede parecer todavía más solo. En el GED, la pregunta clave es: <strong>¿qué efecto produce el escenario que eligió el autor?</strong></p>")}
{P("Compruebe", "<em>La puerta chirrió al abrirse.</em> ¿Con qué sentido se percibe?", SENT, 1, {0: "No se ve: se oye.", 2: "No es un olor.", 3: "No se saborea.", 4: "No se toca."}, "Con el <strong>oído</strong>: chirriar es un ruido.")}"""

    s3 = f"""<h3>Lectura: «La cocina de la abuela»</h3>
<div class="texto-lectura">{"".join(f"<p>{p}</p>" for p in COCINA)}</div>
<div class="caja caja-tip"><span class="etiqueta et-verde">Actividad · en su cuaderno</span>
<p>Haga cinco columnas, una por sentido, y copie en cada una los detalles del texto que le corresponden. Después responda: ¿qué atmósfera crea este escenario?</p></div>
<details class="caja caja-tip"><summary><strong>Ya lo hice: ver el modelo</strong></summary>
<ul><li><strong>Vista:</strong> la luz amarilla del sol, los cuadros tibios sobre el piso de baldosas; cocina pequeña y luminosa.</li>
<li><strong>Oído:</strong> el rumor lejano del tráfico; el tic-tac del reloj de pared.</li>
<li><strong>Olfato:</strong> olor a café recién colado y a galletas de canela.</li>
<li><strong>Gusto:</strong> el sabor dulce y especiado de la galleta.</li>
<li><strong>Tacto:</strong> la cerámica caliente que le quemó los dedos.</li></ul>
<p><strong>Atmósfera:</strong> calidez, paz y hogar. Todos los detalles sirven a la emoción que el narrador quiere transmitir: el bienestar de estar con la abuela.</p></details>
{P("Compruebe", "¿Qué atmósfera crea «La cocina de la abuela»?", ["Calidez y paz", "Miedo y tensión", "Prisa y confusión"], 0,
   {1: "No hay sombras ni peligro: hay café, galletas y compañía.", 2: "Adentro solo se oye el reloj: no hay prisa."}, "<strong>Calidez y paz</strong>: el olor, la luz y el silencio crean un ambiente de hogar.")}"""

    secciones = [("s1", "¿Qué es el escenario?", s1), ("s2", "Los cinco sentidos y las emociones", s2), ("s3", "Práctica: leer un escenario", s3)]
    tarea = [("Mi escenario con los cinco sentidos.", "Elija un lugar que conoce bien: la cocina de su casa, la parada del autobús, el mercado, su trabajo o un sitio de su infancia. Escriba el lugar y el tiempo (dónde, a qué hora, en qué época del año)."),
             ("Un detalle por sentido.", "Anote algo que se ve, algo que se oye, algo que se huele, algo que se saborea y algo que se toca en ese lugar."),
             ("El párrafo.", "Escriba un párrafo de cinco a siete oraciones que describa el lugar con esos detalles, como «La cocina de la abuela». Termine con una oración que diga qué atmósfera quiso crear."),
             ("Póngalo a prueba.", "Lea su párrafo a alguien de su casa sin decirle la atmósfera, y pregúntele qué sintió. ¿Coincide?")]
    quiz = [
        ("¿Qué es el escenario de una historia?", ["Todo lo que rodea a los personajes: lugar, tiempo y ambiente", "El personaje principal", "El final de la historia"], 0, {1: "Eso es el protagonista.", 2: "El escenario no es el final."}, "<strong>Lugar, tiempo y ambiente.</strong>"),
        ("¿Qué pregunta responde el <strong>tiempo</strong>?", ["¿Cuándo ocurre?", "¿Dónde ocurre?", "¿Quién lo hace?"], 0, {1: "Eso es el lugar.", 2: "Eso es el personaje."}, "<strong>¿Cuándo?</strong>"),
        ("<em>«en la parada del autobús»</em> dice…", ["el lugar", "el tiempo", "el ambiente"], 0, {1: "No dice cuándo.", 2: "No dice cómo se siente."}, "El <strong>lugar</strong>."),
        ("<em>La cocina olía a cebolla frita.</em> ¿Qué sentido es?", SENT, 2, {0: "No se ve.", 1: "No se oye.", 3: "Se huele, no se come todavía.", 4: "No se toca."}, "<strong>Olfato.</strong>"),
        ("<em>La sábana estaba suave y fresca.</em> ¿Qué sentido es?", SENT, 4, {0: "Suave se siente con la piel.", 1: "No hace ruido.", 2: "No es un olor.", 3: "No se saborea."}, "<strong>Tacto.</strong>"),
        ("<em>Lluvia fuerte, cielo gris y viento</em> suelen provocar…", ["tristeza o soledad", "fiesta y alegría", "calma y hogar"], 0, {1: "La lluvia y el gris no suelen ser de fiesta.", 2: "No dan sensación de hogar."}, "<strong>Tristeza o soledad.</strong>"),
        ("<em>Un callejón sin luz a medianoche; se oyen pasos detrás.</em> ¿Qué atmósfera crea?", ["Miedo y tensión", "Calma y paz", "Alegría"], 0, {1: "La oscuridad y los pasos no calman.", 2: "No hay nada alegre."}, "<strong>Miedo y tensión.</strong>"),
        ("¿Para qué usa el autor los detalles sensoriales?", ["Para que el lector imagine la escena y sienta la emoción", "Para alargar el texto"], 0, {}, "Para que el lector <strong>entre</strong> en la escena."),
        ("Un personaje triste en un día de sol radiante es un ejemplo de…", ["contraste entre escenario y emoción", "un error del autor", "un conflicto externo"], 0, {1: "Es una elección a propósito.", 2: "No es un problema contra algo de afuera."}, "<strong>Contraste</strong>: la alegría de afuera hace ver más la tristeza."),
        ("En «La cocina de la abuela», ¿qué detalle es del <strong>oído</strong>?", ["el tic-tac del reloj de pared", "el olor a café", "la luz amarilla"], 0, {1: "Es del olfato.", 2: "Es de la vista."}, "<strong>El tic-tac del reloj.</strong>"),
    ]
    filas = [
        ("Lugar y tiempo", "Encuentro dónde y cuándo ocurre una historia.", "Encuentro el lugar, pero no siempre el tiempo.", "No los distingo (<a href=\"#s1\">repase la sección 1</a>)."),
        ("Detalles sensoriales", "Clasifico detalles de los cinco sentidos.", "Confundo el olfato y el gusto.", "Solo veo lo que se ve (<a href=\"#s2\">repase la sección 2</a>)."),
        ("Atmósfera", "Digo qué atmósfera crea un escenario y por qué.", "La siento, pero no sé explicarla.", "No la encuentro (<a href=\"#s3\">repase la sección 3</a>)."),
    ]
    cierre = "<p>Ya sabe leer un escenario con todos los sentidos y ver qué emoción crea. En la próxima lección verá cómo se ordenan los hechos de una historia: <strong>las palabras de secuencia</strong>.</p>"
    glosario = [("Escenario", "Lugar, tiempo y ambiente de una historia."), ("Ambiente o atmósfera", "Lo que se siente al estar en ese lugar: calma, miedo, alegría…"),
                ("Detalle sensorial", "Detalle que se percibe con un sentido: vista, oído, olfato, gusto o tacto."), ("Contraste", "Cuando el escenario es opuesto a lo que siente el personaje.")]
    conexion = ("<p>En la Lección 5.1 aprendió a mirar a los personajes. Ahora va a mirar el mundo donde viven. La misma historia se siente muy distinta en una calle silenciosa de madrugada que en un mercado lleno de gente al mediodía.</p>"
                "<p><strong>Lo que necesita:</strong> el cuaderno y un lugar que conozca bien.</p>")
    estd = LE.estandares(["R.3.2", "R.3.3"])
    return C.pagina_leccion(N, LE.titulo(N), "El escenario no es un fondo: crea la emoción de la historia.", ["R.3.2 · Escenario", "R.3.3 · Relaciones"],
                            ["<strong>Identificar</strong> el lugar, el tiempo y el ambiente de una historia.", "<strong>Clasificar</strong> los detalles de los cinco sentidos.",
                             "<strong>Explicar</strong> qué atmósfera crea un escenario.", "<strong>Escribir</strong> un escenario con los cinco sentidos."],
                            estd, conexion, secciones, tarea, quiz, filas, cierre, ("5-3", LE.titulo("5-3")), glosario, P)


def practica():
    lt = [{"enun": f"<strong>«{f}»</strong><br>¿Dice el lugar o el tiempo?", "ops": ["Lugar", "Tiempo"], "ok": k, "enOrden": True, "pista": "Lugar: ¿dónde? Tiempo: ¿cuándo?",
           "exp": ["Dice <strong>dónde</strong>: es el lugar.", "Dice <strong>cuándo</strong>: es el tiempo."][k]} for f, k in LUGTIEM]
    sen = [{"enun": f"<strong>{d}</strong><br>¿Con qué sentido se percibe?", "ops": SENT, "ok": k, "enOrden": True, "pista": "Pregúntese: ¿lo veo, lo oigo, lo huelo, lo saboreo o lo toco?",
            "exp": f"Se percibe {ORGANO[k]}: <strong>{SENT[k].lower()}</strong>."} for d, k in DETALLES]
    atm = [{"enun": f"<div class=\"texto-lectura\"><p>{e}</p></div>¿Qué atmósfera crea este escenario?", "ops": [ok] + d, "ok": 0, "pista": "Fíjese en la luz, los sonidos y los olores: ¿qué le hacen sentir?",
            "exp": f"<strong>{ok}</strong>: los detalles del lugar, la luz y los sonidos crean esa emoción."} for e, ok, d in ATMOS]
    mods = [("lugar-tiempo", "¿Lugar o tiempo?", C.om("m1", "Decida si la frase dice dónde o cuándo ocurre la historia.")),
            ("sentidos", "¿Qué sentido es?", C.om("m2", "Clasifique cada detalle sensorial.")),
            ("atmosfera", "¿Qué atmósfera crea?", C.om("m3", "Lea el escenario y elija la emoción que produce."))]
    js = C.js_datos("LT", lt) + C.js_datos("SEN", sen) + C.js_datos("ATM", atm) + 'creaBanco("m1", LT);\ncreaBanco("m2", SEN);\ncreaBanco("m3", ATM);\n'
    return C.pagina_practica(N, LE.titulo(N), "Tres actividades · los ejercicios cambian cada vez · dos intentos en cada uno", mods, js)


if __name__ == "__main__":
    LE.construye(N, leccion, practica, horas="Unas 3 horas")
