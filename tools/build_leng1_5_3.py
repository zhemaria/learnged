# -*- coding: utf-8 -*-
"""LearnGED · Artes del lenguaje (español) · Nivel 1 · Lección 5.3 · El orden de los eventos: palabras de secuencia.
Fuente: clases_leng1/clase_5-3.html (GEDparaHispanos) y gramatica/n1-l5-3.html, adaptadas al marco de LearnGED.
Cambio respecto de la fuente: «luego» y «después» significan lo mismo, así que en los ejercicios de ordenar el orden
de los pasos del medio lo decide la lógica de los hechos, no cuál de esas dos palabras lleva cada oración.
Uso: python3 tools/build_leng1_5_3.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import leng_es as LE
from leng_es import C

LE.nivel(1)
N = "5-3"
# (oración con ____, conector correcto, dos distractores, explicación)
HUECOS = [("____, lavo el arroz con agua fría.", "Primero", ["Finalmente", "Mientras tanto"], "es el primer paso de la receta"),
          ("Lavo el arroz. ____, lo pongo en la olla con agua.", "Luego", ["Primero", "Mientras tanto"], "es la acción que sigue"),
          ("Pongo el arroz a cocinar. ____, pico la cebolla para el sofrito.", "Mientras tanto", ["Primero", "Finalmente"], "las dos cosas pasan al mismo tiempo"),
          ("Ya está todo listo. ____, sirvo el arroz en los platos.", "Finalmente", ["Primero", "Mientras tanto"], "es la última acción"),
          ("____, me despierto a las seis de la mañana.", "Primero", ["Por último", "Mientras tanto"], "es lo primero que pasa en el día"),
          ("Me ducho y me visto. ____, desayuno con mi familia.", "Después", ["Primero", "Por último"], "sigue la serie de acciones"),
          ("Yo preparo los almuerzos. ____, mi esposo despierta a los niños.", "Mientras tanto", ["Primero", "Finalmente"], "las dos acciones pasan al mismo tiempo"),
          ("Dejo a los niños en la escuela. ____, tomo el autobús hacia el trabajo.", "Por último", ["Primero", "Mientras tanto"], "es lo último de la serie"),
          ("____, llene la solicitud con sus datos.", "Primero", ["Finalmente", "Mientras tanto"], "es el inicio del trámite"),
          ("Firme la solicitud. ____, entréguela en la ventanilla 3.", "Luego", ["Primero", "Mientras tanto"], "es el paso que sigue"),
          ("Ya entregó los papeles. ____, espere su turno en la sala.", "Después", ["Primero", "Por último"], "continúa la serie"),
          ("La lavadora está trabajando. ____, yo doblo la ropa seca.", "Mientras tanto", ["Primero", "Finalmente"], "las dos acciones pasan al mismo tiempo"),
          ("El partido estuvo muy reñido. ____, ganamos tres a dos.", "Finalmente", ["Primero", "Mientras tanto"], "es el resultado al final"),
          ("____, apague el carro y ponga el freno de mano.", "Primero", ["Por último", "Mientras tanto"], "es lo primero que hay que hacer"),
          ("Abra el capó. ____, revise el nivel del aceite.", "Luego", ["Primero", "Mientras tanto"], "es el paso que sigue"),
          ("Ya revisó el aceite y el agua. ____, cierre el capó con cuidado.", "Por último", ["Primero", "Mientras tanto"], "es el último paso"),
          ("El médico examinaba a mi hijo. ____, yo llenaba los papeles del seguro.", "Mientras tanto", ["Primero", "Por último"], "las dos acciones pasan al mismo tiempo"),
          ("Hirvió el agua. ____, añadimos la pasta.", "Entonces", ["Primero", "Mientras tanto"], "continúa la cadena: pasó una cosa y por eso sigue la otra")]
# Textos para tocar los conectores (* marca las palabras que hay que tocar)
MARCAR = [("*Primero*, abrí la puerta despacio. *Luego*, encendí la luz. *Finalmente*, vi que no había nadie.", "primero, luego y finalmente"),
          ("*Primero*, el agua se calienta. *Después*, se agrega el café. *Mientras* *tanto*, se calienta la leche.", "primero, después y mientras tanto (dos palabras)"),
          ("Llegué temprano a la cita. *Luego*, esperé media hora. *Por* *último*, me llamó la doctora.", "luego y por último (dos palabras)"),
          ("*Primero* busqué trabajo en mi barrio. *Después* me inscribí en el centro de empleo. *Finalmente*, conseguí un puesto en una fábrica.", "primero, después y finalmente"),
          ("Mi hija hacía la tarea. *Mientras* *tanto*, yo cocinaba la cena. *Luego*, comimos juntas.", "mientras tanto y luego"),
          ("*Primero*, lea la pregunta. *Luego*, lea el texto. *Después*, elija la mejor respuesta.", "primero, luego y después"),
          ("Sonó la alarma. *Entonces*, todos salieron por la escalera. *Finalmente*, llegaron los bomberos.", "entonces y finalmente"),
          ("*Primero*, el bebé lloró. *Después*, se calmó con la leche. *Por* *último*, se durmió en mis brazos.", "primero, después y por último")]
# Secuencias en su orden correcto: el orden del medio lo decide la lógica de los hechos.
ORDENAR = [("Cómo preparar un café", ["Primero, hiervo el agua.", "Luego, echo el café molido en el filtro.", "Después, vierto el agua caliente sobre el café.", "Finalmente, sirvo el café en la taza."], [2, 0, 3, 1],
            "Hay que tener el agua caliente y el café en el filtro antes de verter el agua."),
           ("Cómo enviar un correo electrónico", ["Primero, abro la página de mi correo.", "Luego, escribo mi contraseña y entro.", "Después, hago clic en «Redactar» y escribo el mensaje.", "Finalmente, reviso lo que escribí y presiono «Enviar»."], [3, 1, 0, 2],
            "No se puede escribir el mensaje sin entrar al correo, ni enviarlo sin haberlo escrito."),
           ("Un trámite en la oficina", ["Primero, llené el formulario.", "Luego, lo firmé.", "Después, lo llevé a la ventanilla.", "Por último, pagué la cuota y me dieron el recibo."], [2, 3, 0, 1],
            "Se firma un formulario ya lleno, y se entrega uno ya firmado."),
           ("La mañana de Roberto", ["Primero, sonó el despertador.", "Luego, Roberto se levantó de la cama.", "Después, se bañó y se vistió.", "Finalmente, salió rumbo al trabajo."], [1, 3, 2, 0],
            "Uno se despierta, se levanta, se arregla y sale."),
           ("La tormenta", ["Primero, el cielo se nubló.", "Luego, empezó a soplar un viento fuerte.", "Después, cayó un aguacero.", "Finalmente, salió el arcoíris."], [3, 0, 2, 1],
            "El arcoíris sale cuando ya pasó la lluvia."),
           ("El diploma de Carlos", ["Primero, Carlos se inscribió en la clase.", "Luego, estudió la guía durante meses.", "Después, presentó el examen.", "Finalmente, recibió su diploma."], [2, 0, 3, 1],
            "Se estudia antes del examen, y el diploma llega después de aprobarlo."),
           ("La sopa de verduras", ["Primero, compré las verduras en el mercado.", "Luego, las lavé.", "Después, las corté en trozos.", "Finalmente, preparé la sopa."], [1, 3, 0, 2],
            "Se lavan las verduras enteras, antes de cortarlas, y la sopa se hace con ellas ya cortadas.")]
# (texto con los hechos desordenados, pregunta, respuesta, distractores)
CUANDO = [("Finalmente, salió el arcoíris. Primero, el cielo se nubló. Después, cayó un aguacero.", "¿Qué pasó <strong>primero</strong>?", "El cielo se nubló.", ["Salió el arcoíris.", "Cayó un aguacero."]),
          ("Por último, pagué la cuota. Primero, llené el formulario. Luego, lo firmé.", "¿Qué pasó <strong>al final</strong>?", "Pagué la cuota.", ["Llené el formulario.", "Lo firmé."]),
          ("Luego, me levanté de la cama. Finalmente, salí de casa. Primero, sonó el despertador.", "¿Qué pasó <strong>primero</strong>?", "Sonó el despertador.", ["Me levanté de la cama.", "Salí de casa."]),
          ("Mientras tanto, mi hermana lavaba los platos. Primero, cenamos todos juntos. Después, yo barrí la cocina.", "¿Qué pasó <strong>al mismo tiempo</strong> que yo barría?", "Mi hermana lavaba los platos.", ["Cenamos todos juntos.", "Sonó el teléfono."]),
          ("Finalmente, recibió su diploma. Primero, Carlos estudió la guía. Luego, presentó el examen.", "¿Qué pasó <strong>al final</strong>?", "Carlos recibió su diploma.", ["Estudió la guía.", "Presentó el examen."]),
          ("Por último, lo envié. Primero, encendí la computadora. Después, escribí el mensaje.", "¿Qué pasó <strong>primero</strong>?", "Encendí la computadora.", ["Escribí el mensaje.", "Lo envié."]),
          ("Mientras tanto, los niños jugaban en el patio. Primero, mi tío encendió la parrilla. Luego, asó la carne.", "¿Qué hacían los niños <strong>mientras</strong> mi tío cocinaba?", "Jugaban en el patio.", ["Encendían la parrilla.", "Asaban la carne."]),
          ("Finalmente, llegaron los bomberos. Primero, sonó la alarma. Entonces, todos salieron por la escalera.", "¿Qué pasó <strong>al final</strong>?", "Llegaron los bomberos.", ["Sonó la alarma.", "Todos salieron por la escalera."])]
ROBERTO = ["Primero, sonó el despertador a las seis de la mañana. Roberto abrió los ojos despacio y miró el techo durante un minuto.",
           "Luego, se levantó y caminó hacia la cocina. Encendió la cafetera y miró por la ventana: la calle todavía estaba a oscuras.",
           "Después de bañarse, se vistió con la ropa que había preparado la noche anterior. Mientras tanto, su esposa preparaba el desayuno y los niños dormían en la habitación de al lado.",
           "Finalmente, Roberto besó a su esposa, tomó las llaves del carro y salió rumbo al trabajo. Eran las siete en punto."]


def leccion():
    P = C.Practicas()
    s1 = f"""<p>Una historia no es solo personajes y escenario: es una serie de <strong>hechos</strong>, y los hechos ocurren en un orden. Para que el lector no se pierda, el autor usa <strong>palabras de secuencia</strong> (también se llaman conectores de tiempo): dicen si algo pasa antes, al mismo tiempo o después de otra cosa.</p>
{C.tabla("El mismo párrafo sin conectores y con conectores", ["Sin conectores", "Con conectores"],
         [["Me levanté. Me bañé. Desayuné. Salí para el trabajo.", "<strong>Primero</strong> me levanté. <strong>Luego</strong> me bañé. <strong>Después</strong> desayuné. <strong>Finalmente</strong> salí para el trabajo."]])}
<p>Los dos cuentan lo mismo, pero el segundo fluye mejor y deja claro el orden.</p>
{C.caja("tip", "Idea central", "<p>Las palabras de secuencia son <strong>señales</strong> que el autor pone para que el lector no se pierda en el tiempo de la historia.</p>")}"""

    s2 = f"""{C.tabla("Las palabras de secuencia y lo que indican", ["Palabra", "Qué indica", "Ejemplo"],
         [["<strong>Primero</strong>", "El punto de partida.", "Primero hervimos el agua."],
          ["<strong>Luego · Después · Entonces</strong>", "Lo que sigue. Significan casi lo mismo.", "Luego agregamos el café."],
          ["<strong>Mientras tanto</strong>", "Dos cosas que pasan <em>al mismo tiempo</em>.", "Mientras tanto, calentamos la leche."],
          ["<strong>Finalmente · Por último</strong>", "El cierre o el resultado.", "Finalmente servimos el café."]])}
{C.caja("ojo", "Luego y después son intercambiables", "<p>Se puede decir «Primero… Luego… Después…» o «Primero… Después… Luego…». Lo que decide el orden de los pasos del medio no es la palabra, sino <strong>la lógica de los hechos</strong>: no se puede firmar un formulario que todavía no se ha llenado.</p>")}
{C.caja("tip", "La coma", "<p>Estas palabras suelen ir al principio de la oración. Con las cortas (<em>primero, luego, después</em>), la coma es opcional. Con las de varias palabras (<em>mientras tanto, por último</em>), póngala siempre: «Mientras tanto, calentamos la leche». Ojo: <em>después de</em> + verbo no lleva coma: «Después de bañarse, se vistió».</p>")}
<h3>Texto modelo: una mañana cualquiera</h3>
<div class="texto-lectura">{"".join(f"<p>{p}</p>" for p in ROBERTO)}</div>
{P("Compruebe", "¿Qué hacía la esposa de Roberto <strong>mientras</strong> él se vestía?", ["Preparaba el desayuno", "Dormía", "Salía al trabajo"], 0,
   {1: "Los que dormían eran los niños.", 2: "El que sale al trabajo es Roberto, al final."}, "<strong>Preparaba el desayuno</strong>: «mientras tanto» une las dos acciones en el mismo momento.")}
{P("Compruebe", "¿Qué palabra marca la <strong>última</strong> acción de la mañana?", ["Finalmente", "Luego", "Mientras tanto"], 0, {1: "Luego marca lo que sigue, no el cierre.", 2: "Mientras tanto marca algo simultáneo."}, "<strong>Finalmente</strong>: Roberto sale rumbo al trabajo.")}"""

    s3 = f"""<div class="caja caja-tip"><span class="etiqueta et-verde">Actividad · en su cuaderno</span>
<p>Escriba en cinco renglones cómo prepara su bebida favorita (café, té, un batido…), un paso por renglón, empezando cada uno con una palabra de secuencia. Use <em>mientras tanto</em> al menos una vez.</p></div>
{P("Compruebe", "<em>Pongo el arroz a cocinar. ____, pico la cebolla.</em> ¿Qué palabra va?", ["Mientras tanto", "Primero", "Finalmente"], 0,
   {1: "No es el primer paso: el arroz ya está en el fuego.", 2: "Todavía falta: no es el final."}, "<strong>Mientras tanto</strong>: el arroz se cocina al mismo tiempo que usted pica la cebolla.")}
{P("Compruebe", "¿Dónde va la coma?", ["Mientras tanto, calentamos la leche.", "Mientras, tanto calentamos la leche.", "Mientras tanto calentamos, la leche."], 0,
   {1: "«Mientras tanto» es una sola expresión: no se separa.", 2: "La coma va después de la expresión, no dentro de la oración."}, "<strong>Mientras tanto,</strong> calentamos la leche.")}"""

    secciones = [("s1", "¿Qué son las palabras de secuencia?", s1), ("s2", "Las palabras principales", s2), ("s3", "Práctica: ordenar y completar", s3)]
    tarea = [("Mi rutina en orden.", "Escriba en su cuaderno un párrafo de seis a ocho oraciones que cuente algo que hace casi todos los días, paso a paso: su mañana, cómo prepara su comida favorita o cómo llega al trabajo."),
             ("Las señales.", "Use al menos cuatro palabras de secuencia distintas, una de ellas <em>mientras tanto</em>. Subraye cada una y ponga coma después de las de varias palabras."),
             ("El rompecabezas.", "Copie sus oraciones en otra hoja, sin las palabras de secuencia y en desorden. Pídale a alguien de su casa que las ordene. Si no puede, quizás falta una señal.")]
    quiz = [
        ("¿Para qué sirven las palabras de secuencia?", ["Para decir en qué orden pasan los hechos", "Para describir a los personajes", "Para dar la opinión del autor"], 0, {1: "Eso lo hacen los adjetivos.", 2: "No dan opiniones."}, "Dicen el <strong>orden</strong> de los hechos."),
        ("¿Qué palabra marca el <strong>inicio</strong>?", ["Primero", "Finalmente", "Mientras tanto"], 0, {1: "Marca el final.", 2: "Marca algo simultáneo."}, "<strong>Primero.</strong>"),
        ("¿Qué indica <strong>mientras tanto</strong>?", ["Que dos cosas pasan al mismo tiempo", "Que algo pasó al final", "Que algo pasó primero"], 0, {1: "Eso es finalmente.", 2: "Eso es primero."}, "Que pasan <strong>al mismo tiempo</strong>."),
        ("¿Qué palabra significa casi lo mismo que <strong>luego</strong>?", ["después", "primero", "mientras tanto"], 0, {1: "Primero es el inicio.", 2: "Mientras tanto es simultáneo."}, "<strong>Después.</strong>"),
        ("¿Qué palabra marca el <strong>cierre</strong>?", ["Por último", "Luego", "Primero"], 0, {1: "Luego marca lo que sigue.", 2: "Primero es el inicio."}, "<strong>Por último</strong> (o finalmente)."),
        ("<em>La lavadora está trabajando. ____, yo doblo la ropa seca.</em>", ["Mientras tanto", "Primero", "Finalmente"], 0, {1: "La lavadora ya está trabajando: no es el inicio.", 2: "No es el final."}, "<strong>Mientras tanto</strong>: al mismo tiempo."),
        ("¿Cuál está bien puntuada?", ["Por último, cierre el capó.", "Por, último cierre el capó.", "Por último cierre, el capó."], 0, {1: "«Por último» no se separa.", 2: "La coma va después de «por último»."}, "<strong>Por último,</strong> cierre el capó."),
        ("Si dos pasos del medio empiezan con <em>luego</em> y <em>después</em>, ¿qué decide cuál va primero?", ["La lógica de los hechos", "Siempre va primero «luego»"], 0, {}, "La <strong>lógica de los hechos</strong>: las dos palabras significan lo mismo."),
        ("<em>Finalmente, salí de casa. Primero, sonó el despertador. Luego, me levanté.</em> ¿Qué pasó primero?", ["Sonó el despertador", "Salí de casa", "Me levanté"], 0, {1: "«Finalmente» marca lo último.", 2: "«Luego» marca lo que sigue."}, "<strong>Sonó el despertador</strong>: «primero» marca el inicio."),
        ("En el examen GED, las palabras de secuencia ayudan a…", ["ordenar los hechos de un texto", "contar las palabras", "encontrar el título"], 0, {1: "No.", 2: "No."}, "A <strong>ordenar los hechos</strong>, una pregunta frecuente del examen."),
    ]
    filas = [
        ("Reconocer", "Encuentro todas las palabras de secuencia de un texto, también las de dos palabras.", "Se me escapan las de dos palabras.", "No las reconozco (<a href=\"#s2\">repase la sección 2</a>)."),
        ("Ordenar", "Ordeno hechos usando las señales y la lógica.", "Me confundo con luego y después.", "No sé por dónde empezar (<a href=\"#s2\">repase la sección 2</a>)."),
        ("Usar", "Escribo un párrafo con cuatro palabras de secuencia y la coma bien puesta.", "Las uso, pero olvido la coma.", "No las uso (<a href=\"#s3\">repase la sección 3</a>)."),
    ]
    cierre = "<p>Ya sabe seguir el orden de los hechos con sus señales. En la próxima lección va a usar esta destreza en la vida diaria: <strong>seguir instrucciones paso a paso</strong>.</p>"
    glosario = [("Secuencia", "Orden en que ocurren los hechos."), ("Palabra de secuencia", "Palabra que indica el orden: primero, luego, después, mientras tanto, finalmente."),
                ("Simultáneo", "Que ocurre al mismo tiempo que otra cosa."), ("Cronológico", "En el orden en que pasaron las cosas en el tiempo.")]
    conexion = ("<p>Ya conoce a los personajes (Lección 5.1) y el escenario (Lección 5.2). Ahora verá cómo se ordenan los hechos de una historia, de una receta o de unas instrucciones.</p>"
                "<p><strong>Lo que necesita:</strong> el cuaderno.</p>")
    estd = LE.estandares(["R.3.1", "R.5.3"])
    return C.pagina_leccion(N, LE.titulo(N), "Primero, luego, mientras tanto, finalmente: las señales del tiempo.", ["R.3.1 · Secuencia", "R.5.3 · Conectores"],
                            ["<strong>Reconocer</strong> las palabras de secuencia en un texto.", "<strong>Ordenar</strong> hechos con las señales y la lógica.",
                             "<strong>Distinguir</strong> lo que pasa después de lo que pasa al mismo tiempo.", "<strong>Escribir</strong> un párrafo ordenado con palabras de secuencia y la coma bien puesta."],
                            estd, conexion, secciones, tarea, quiz, filas, cierre, ("5-4", LE.titulo("5-4")), glosario, P)


def practica():
    hue = [{"enun": f"<strong>{o}</strong><br>¿Qué palabra va en el espacio?", "ops": [ok] + d, "ok": 0,
            "pista": "¿Es el comienzo, lo que sigue, algo al mismo tiempo o el final?", "exp": f"Va <strong>{ok}</strong>: {e}."} for o, ok, d, e in HUECOS]
    mar = [{"consigna": "Toque todas las palabras de secuencia (algunas son de dos palabras: toque las dos).", "texto": t, "exp": f"Son <strong>{e}</strong>."} for t, e in MARCAR]
    orden = [{"titulo": f"{ti}", "intro": "Ordene los pasos con los botones ▲ y ▼. Las palabras de secuencia ayudan, y la lógica decide.", "pasos": p, "inicio": ini, "cons": {}, "general": g} for ti, p, ini, g in ORDENAR]
    cua = [{"enun": f"<div class=\"texto-lectura\"><p>{t}</p></div>Los hechos están desordenados. {q}", "ops": [ok] + d, "ok": 0, "pista": "Busque la palabra de secuencia de cada oración.",
            "exp": f"<strong>{ok}</strong>"} for t, q, ok, d in CUANDO]
    mods = [("completar", "¿Qué palabra va?", C.om("m1", "Elija la palabra de secuencia que completa la oración.")),
            ("encontrar", "Toque las palabras de secuencia", LE.marcar("m2", "Toque todas las palabras de secuencia. Si se equivoca, vuelva a tocar la palabra para quitar la marca. Después pulse <strong>Comprobar</strong>.")),
            ("ordenar", "Ordene los pasos", C.orden("m3")),
            ("cuando", "¿Qué pasó primero?", C.om("m4", "Lea los hechos desordenados y use las señales para responder."))]
    js = (C.js_datos("HUE", hue) + C.js_datos("MAR", mar) + C.js_datos("ORD", orden) + C.js_datos("CUA", cua) +
          'creaBanco("m1", HUE);\ncreaMarcar("m2", MAR);\ncreaOrden("m3", ORD);\ncreaBanco("m4", CUA);\n')
    return C.pagina_practica(N, LE.titulo(N), "Cuatro actividades · los ejercicios cambian cada vez · dos intentos en cada uno", mods, js)


if __name__ == "__main__":
    LE.construye(N, leccion, practica, horas="Unas 3 horas")
