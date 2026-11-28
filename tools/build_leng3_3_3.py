# -*- coding: utf-8 -*-
"""LearnGED · Artes del lenguaje (español) · Nivel 3 · Lección 3.3 · Hacer inferencias con evidencia del texto.
Fuente: clases_leng3/clase_3-3.html (GEDparaHispanos) y gramatica/n3-l3-3.html, adaptadas al marco de LearnGED.
Uso: python3 tools/build_leng3_3_3.py
"""
import os, sys, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import leng_es as LE
from leng_es import C
from build_leng3_3_1 import texto

LE.nivel(3)
N = "3-3"


def K(t):
    return f'<span class="idea">{t}</span>'


MARCO = [f"Don Ernesto {K('llegaba siempre media hora antes')} que los demás. Se sentaba en la primera fila, sacaba unos {K('lentes sujetos con cinta adhesiva')} y {K('repasaba un cuaderno')} lleno de fracciones y fechas de historia, escrito con letra apretada.",
         f"Tenía las {K('manos grandes y ásperas, con cicatrices en los nudillos')}. Una vez, la maestra le preguntó a qué se había dedicado. «Cuarenta años poniendo ladrillos», contestó. «{K('Esta ciudad tiene un poquito de mí en cada esquina')}.»",
         f"Le gustaba contar que en la pared de su cocina había {K('un marco vacío')}. «{K('Ahí va a ir algo')}», decía, y no explicaba más.",
         f"El día del examen de práctica, sus compañeros lo vieron {K('borrar y volver a escribir la misma respuesta tres veces')}. Al salir {K('no habló con nadie')}. Se quedó un largo rato en la parada, aunque {K('pasaron dos autobuses que lo llevaban a su casa')}.",
         f"Tres semanas después entró al salón con {K('una corbata que nadie le había visto nunca')}. No dijo nada. Abrió un sobre, sacó una hoja y {K('la levantó con las dos manos para que todos la vieran')}. Al día siguiente, le contó a la maestra que {K('el marco de la cocina ya no estaba vacío')}."]
A = ["El señor Vargas entró a la clínica apoyándose en un bastón. Cada paso le costaba, y se detuvo dos veces a descansar antes de llegar al mostrador.",
     "Cuando la enfermera dijo su nombre, se levantó despacio y sonrió: «Por fin, ya llevaba dos horas aquí»."]
B = ["Al volver del trabajo, Ana encontró la puerta del apartamento abierta. La lámpara de la sala estaba en el suelo y los cajones del escritorio, revueltos.",
     "Llamó a su hermana con la voz temblorosa y no se atrevió a entrar hasta que llegó la policía."]
Cx = ["Miguel se levantó a las cuatro de la mañana, se puso el uniforme anaranjado y salió con su lonchera. Cuando volvió, por la tarde, tenía las botas cubiertas de polvo de cemento.",
      "Se sentó en el sofá y se quedó dormido antes de que su esposa terminara de servir la cena."]
D = ["Los vecinos del edificio llevaban un mes sin agua caliente. Juntaron firmas en una hoja y la dejaron en la oficina del administrador.",
     "Como nadie respondió, el viernes llamaron a un periódico del barrio. El lunes siguiente, un plomero estaba arreglando la caldera."]
E = ["Sofía practicó su discurso frente al espejo toda la semana. La noche antes de la graduación casi no cenó, y se levantó tres veces a repasar sus tarjetas.",
     "Cuando la llamaron al escenario, le temblaban las manos. Al terminar, el público se puso de pie y su madre lloraba en la tercera fila."]
PI = [(A, "El señor Vargas tiene dificultad para caminar.", ["Se apoyaba en un bastón y se detuvo dos veces a descansar.", "La enfermera dijo su nombre en voz alta en la sala.", "Ya llevaba dos horas esperando sentado en la clínica."], "El bastón y las pausas muestran la dificultad."),
      (A, "El señor Vargas estaba cansado de esperar.", ["«Por fin, ya llevaba dos horas aquí.»", "Entró a la clínica apoyándose en un bastón.", "Se levantó despacio cuando lo llamaron."], "«Por fin» y las dos horas muestran su cansancio de esperar."),
      (B, "Alguien entró a robar al apartamento.", ["La lámpara estaba en el suelo y los cajones, revueltos.", "Ana volvió del trabajo a su apartamento por la tarde.", "Ana llamó a su hermana por teléfono en cuanto llegó."], "El desorden y la puerta abierta sugieren un robo."),
      (B, "Ana tenía miedo.", ["Habló con la voz temblorosa y no se atrevió a entrar.", "Encontró la puerta de su apartamento abierta al volver.", "Los cajones del escritorio de la sala estaban revueltos."], "La voz temblorosa y no entrar son señales de miedo."),
      (Cx, "Miguel trabaja en la construcción.", ["Volvió con las botas cubiertas de polvo de cemento.", "Se levantó a las cuatro de la mañana para salir de casa.", "Su esposa le sirvió la cena cuando volvió por la tarde."], "El polvo de cemento apunta a una obra. Madrugar no dice en qué trabaja."),
      (Cx, "El trabajo de Miguel es agotador.", ["Se quedó dormido antes de que le sirvieran la cena.", "Salió de casa muy temprano con su lonchera en la mano.", "Llevaba puesto un uniforme anaranjado para trabajar."], "Dormirse antes de cenar muestra el cansancio."),
      (D, "La presión de los medios ayudó a resolver el problema.", ["Llamaron a un periódico, y al lunes siguiente llegó el plomero.", "Juntaron firmas en una hoja y la dejaron en la oficina.", "Llevaban un mes entero sin agua caliente en el edificio."], "El arreglo llegó justo después de la llamada al periódico; las firmas solas no funcionaron."),
      (E, "Sofía estaba nerviosa por su discurso.", ["Casi no cenó y se levantó tres veces a repasar.", "Practicó frente al espejo durante la semana.", "El público se puso de pie al terminar el acto."], "No comer y repasar de noche muestran nervios."),
      (E, "El discurso de Sofía fue un éxito.", ["Al terminar, el público se puso de pie.", "Le temblaban las manos al subir al escenario.", "Practicó toda la semana frente al espejo."], "El público de pie es una señal de aplauso y aprobación.")]
MI = [(A, "¿Qué se puede inferir del señor Vargas?", ["Es una persona mayor o con un problema de salud.", "Es el médico que trabaja todos los días en esa clínica.", "Nunca le ha gustado ir al médico, ni de joven ni ahora."], "El bastón y lo que le cuesta caminar lo apoyan. La tercera va demasiado lejos."),
      (B, "¿Qué es lo más probable que hiciera la policía al llegar?", ["Revisar el apartamento para ver qué faltaba.", "Felicitar a Ana por el orden de su casa.", "Arrestar a la hermana de Ana por el desorden."], "Es lo razonable ante un posible robo. Nada apoya las otras dos."),
      (Cx, "¿Por qué Miguel se levanta a las cuatro?", ["Su trabajo empieza muy temprano.", "No le gusta dormir en su casa.", "Su esposa lo despierta para molestarlo."], "Se viste con el uniforme y sale con su lonchera: va a trabajar."),
      (D, "¿Qué se puede concluir de las firmas?", ["No bastaron para que el administrador actuara.", "Fueron la única razón del arreglo de la caldera.", "Los vecinos no sabían escribir bien sus nombres."], "«Como nadie respondió» muestra que no bastaron."),
      (E, "¿Cómo se sentía la madre de Sofía al final?", ["Emocionada y orgullosa de su hija.", "Avergonzada del discurso de su hija.", "Aburrida porque el acto duró mucho."], "Llorar mientras el público aplaude de pie sugiere emoción y orgullo."),
      (E, "¿Qué revela que Sofía practicara toda la semana?", ["Que el discurso era importante para ella.", "Que no sabía leer bien todavía.", "Que siempre hace todo de última hora."], "Prepararse tanto muestra que le importaba. La tercera contradice el texto."),
      (B, "¿Por qué Ana no entró hasta que llegó la policía?", ["Temía que todavía hubiera alguien dentro.", "Había perdido las llaves del apartamento.", "Quería que su hermana viera el desorden."], "La puerta abierta y su miedo apoyan la primera; la puerta estaba abierta, así que no necesitaba llaves."),
      (D, "¿Qué sugiere el texto sobre el administrador?", ["No atendía los reclamos de los vecinos hasta que hubo presión.", "Era el mismo plomero que llegó a arreglar la caldera del edificio.", "Vivía en el mismo edificio que los vecinos que firmaron la hoja."], "Solo actuó después de la llamada al periódico.")]
SE = [(A, ["El señor Vargas va todas las semanas a la clínica.", "El señor Vargas camina con mucha dificultad.", "El señor Vargas tuvo que esperar bastante tiempo.", "Al final, la enfermera lo llamó para atenderlo."], "Nada dice cada cuánto va a la clínica."),
      (B, ["Ana sabe quién entró a su apartamento.", "Alguien entró al apartamento sin permiso.", "Ana estaba asustada cuando llamó.", "Ana confía en su hermana para ayudarla."], "El texto no da ninguna pista de quién fue."),
      (Cx, ["Miguel odia su trabajo.", "Miguel trabaja muchas horas.", "Miguel se cansa mucho.", "Miguel trabaja con cemento."], "Que se canse no prueba que odie el trabajo: va más lejos de las pistas."),
      (D, ["El periódico pagó la reparación de la caldera.", "Los vecinos del edificio estaban bien organizados.", "El administrador tardó mucho en actuar.", "El problema del agua caliente duró varias semanas."], "El texto no dice quién pagó; solo que llegó un plomero."),
      (E, ["Sofía nunca había hablado en público.", "Sofía se preparó mucho para su discurso.", "Sofía estaba nerviosa antes de hablar.", "Al público le gustó mucho su discurso."], "Estar nerviosa no prueba que fuera la primera vez. <em>Nunca</em> es una señal de alarma."),
      (Cx, ["Miguel y su esposa están peleados.", "Miguel madruga para ir a trabajar.", "Su esposa le preparó la cena.", "Miguel vuelve a casa por la tarde."], "Que se duerma antes de cenar no muestra ninguna pelea.")]
NOTA_T = '<p class="fuente">Historias y personajes creados para la práctica.</p>'


def leccion():
    P = C.Practicas()
    s1 = f"""<p>Usted llega a casa y ve la cocina llena de platos sucios, un pastel a medio comer y globos en el suelo. Nadie se lo ha dicho, pero sabe que hubo una fiesta. Eso es una <strong>inferencia</strong>: unir lo que ve con lo que ya sabe. Al leer pasa igual: los buenos escritores no lo dicen todo, sino que dejan pistas para que el lector complete la historia.</p>
<p>Una inferencia es una conclusión razonable que se saca juntando dos cosas:</p>
<p class="formula">pista del texto + lo que ya sé = inferencia</p>
{C.tabla("Ejemplos de pista, conocimiento previo e inferencia", ["Pista del texto", "Lo que ya sé", "Inferencia"],
         [["«Marta miró el reloj por quinta vez y tamborileó los dedos en la mesa.»", "La gente mira mucho el reloj y mueve los dedos cuando está impaciente.", "Marta está impaciente o esperando a alguien que se retrasa."],
          ["«Al abrir la puerta, el olor a pan recién horneado llenó el pasillo.»", "El pan recién hecho huele así justo al salir del horno.", "Alguien acaba de hornear pan."],
          ["«Pedro guardó la carta sin abrirla y se le quebró la voz al hablar.»", "Cuando algo nos emociona o nos duele, a veces la voz se quiebra.", "La carta le provoca una emoción fuerte."]])}
{C.caja("tip", "Una inferencia no es una adivinanza", "<p>Cualquier persona que lea las mismas pistas debería poder llegar a la misma conclusión, o a una muy parecida. Si solo usted puede llegar a ella, probablemente está poniendo algo que no está en el texto.</p>")}"""

    s2 = f"""{C.tabla("Clases de inferencia con sus preguntas", ["Se infiere…", "Preguntas típicas del GED"],
         [["Lo que siente un personaje", "¿Cómo se siente X cuando…? ¿Qué revela su reacción?"], ["Por qué actúa así (su motivación)", "¿Por qué X decide…? ¿Qué quiere lograr?"],
          ["La causa de algo que pasa", "¿Qué provocó…? ¿Por qué ocurre…?"], ["Lo que pasará (una predicción)", "¿Qué es más probable que haga X después?"],
          ["El sentido de un detalle", "¿Qué sugiere el detalle de…? ¿Por qué el autor incluye…?"]])}
{C.caja("tip", "Las palabras de la pregunta", "<p>Cuando una pregunta dice <em>sugiere, implica, se puede concluir, es probable que, revela</em>, le está pidiendo una inferencia. La respuesta no estará escrita tal cual en el texto.</p>")}
{P("Inferir 1", "«Las hojas de los árboles estaban amarillas y la gente caminaba con bufandas.» ¿En qué estación es más probable que ocurra?", ["En verano", "En primavera", "En otoño"], 2, {0: "En verano no se usan bufandas.", 1: "En primavera las hojas son verdes."}, "Hojas amarillas y bufandas: <strong>otoño</strong>.")}"""

    s3 = f"""<p>Pase cada inferencia por tres preguntas:</p>
<ol class="proceso"><li><strong>¿Hay pistas en el texto que la apoyan?</strong> Si no puede señalar ninguna, está inventada.</li>
<li><strong>¿Algo del texto la contradice?</strong> Si una sola oración la desmiente, no vale.</li>
<li><strong>¿Va más lejos de lo que permiten las pistas?</strong> Las palabras <em>siempre, nunca, todos, nadie</em> o una conclusión enorme a partir de una pista pequeña son señales de alarma.</li></ol>
<p>Ejemplo: «Marta miró el reloj por quinta vez y tamborileó los dedos en la mesa.»</p>
{C.tabla("Inferencias sobre Marta y si son válidas", ["Inferencia", "¿Válida?"],
         [["Marta está impaciente.", "✓ Sí: las dos pistas la apoyan."], ["Marta espera a su novio.", "✗ No hay ninguna pista de quién es la persona."],
          ["Marta es una persona impaciente que nunca sabe esperar.", "✗ Va demasiado lejos: una escena no dice cómo es Marta siempre."], ["Marta está tranquila y relajada.", "✗ Lo contradicen las pistas."]])}
{P("Válida 1", "«Rosa abrió el refrigerador, suspiró y volvió a cerrarlo. Luego revisó su cartera y contó las monedas dos veces.» ¿Qué inferencia está mejor apoyada?", ["Rosa está a dieta y no quiere comer nada.", "Rosa tiene poco dinero y poca comida en casa.", "Rosa siempre ha sido pobre en su vida."], 1,
   {0: "Contar las monedas no tiene que ver con una dieta.", 2: "<em>Siempre</em> va demasiado lejos."}, "El refrigerador y las monedas apoyan la segunda. La tercera va demasiado lejos.")}
{P("Válida 2", "«El jefe entró, cerró la puerta de su oficina con fuerza y no saludó a nadie.» ¿Qué se infiere?", ["El jefe va a despedir a todos.", "El jefe es siempre una persona grosera.", "El jefe está molesto por algo."], 2,
   {0: "Ninguna pista dice qué va a hacer.", 1: "Una escena no dice cómo es siempre."}, "Las pistas apoyan el enojo de ese momento.")}
{P("Válida 3", "«Cuando sonó el timbre, los niños corrieron hacia la puerta gritando “¡Llegó la abuela!”» ¿Qué se infiere?", ["La abuela vive en la misma casa que ellos.", "Los niños esperaban con alegría a su abuela.", "Los niños tenían miedo de abrir la puerta."], 1,
   {0: "Tocó el timbre: no vive allí.", 2: "Corrieron gritando su nombre."}, "Correr y gritar su nombre muestran alegría y espera.")}"""

    lect = "".join(f'<p><span class="num-p" aria-hidden="true">{i}</span>{p}</p>' for i, p in enumerate(MARCO, 1))
    plano = " ".join(re.sub("<[^>]+>", "", p) for p in MARCO)
    s4 = f"""<p>Lea el cuento. El autor nunca dice algunas cosas importantes: tendrá que deducirlas. En su cuaderno, copie la tabla «pista + lo que sé = inferencia» y llénela con tres inferencias. Después pulse <strong>Mostrar las pistas</strong>.</p>
<p>{LE.escuchar(plano, "Escuchar el cuento")} <button type="button" class="btn-sec" id="btn-p33" aria-pressed="false">Mostrar las pistas</button></p>
<div class="articulo lectura-cl" id="lect-33"><p><strong>El marco vacío</strong></p>{lect}</div>
<p class="fuente">Cuento y personaje creados para esta lección.</p>
<script>(function(){{var b=document.getElementById("btn-p33"),t=document.getElementById("lect-33");b.addEventListener("click",function(){{var on=t.classList.toggle("ver-cl");b.setAttribute("aria-pressed",on?"true":"false");b.textContent=on?"Ocultar las pistas":"Mostrar las pistas";}});}})();</script>
<h3>Lea entre líneas</h3>
{P("Marco 1", "¿Qué se puede inferir de los lentes «sujetos con cinta adhesiva»?", ["Don Ernesto tiene tan mala vista que casi no puede leer nada", "Don Ernesto no gasta en cosas nuevas o no tiene dinero para hacerlo", "A don Ernesto no le importa nada cómo se ve delante de los demás"], 1,
   {0: "La cinta habla de los lentes, no de su vista.", 2: "Va más lejos de lo que dice la pista."}, "Arreglar unos lentes con cinta en lugar de comprar otros sugiere ahorro o poco dinero.")}
{P("Marco 2", "«Esta ciudad tiene un poquito de mí en cada esquina.» ¿Qué revela esta frase?", ["Quiere mudarse pronto a otra ciudad más tranquila", "Le molesta mucho haber trabajado tanto tiempo", "Está orgulloso de lo que construyó con su trabajo"], 2,
   {0: "Nada en el texto lo sugiere.", 1: "El tono no es de queja."}, "Habla de los edificios que levantó con sus manos: es orgullo.")}
{P("Marco 3", "¿Qué pista muestra que el examen de práctica lo dejó preocupado?", ["Se sentaba siempre en la primera fila del salón", "Dejó pasar dos autobuses que lo llevaban a casa", "Tenía las manos grandes y llenas de cicatrices"], 1,
   {0: "Eso pasaba siempre, no ese día.", 2: "Habla de su trabajo, no del examen."}, "Quedarse en la parada sin subir sugiere que estaba pensando, preocupado o triste.")}
{P("Marco 4", "¿Qué hoja sacó don Ernesto del sobre?", ["Una carta larga de un familiar que vive en otra ciudad", "La cuenta de la luz que tenía que pagar ese mes", "Muy probablemente, el resultado aprobado de su examen"], 2,
   {0: "¿Por qué la mostraría con orgullo a toda la clase?", 1: "Nadie se pone corbata para una cuenta."}, "La corbata, el gesto de mostrarla y el marco que «ya no estaba vacío» apuntan a un resultado aprobado.")}
{P("Marco 5", "¿Qué significaba el marco vacío?", ["Un recuerdo triste de una foto perdida", "Una meta que esperaba cumplir: su diploma", "Un adorno que le gustaba mucho a su esposa"], 1,
   {0: "Ninguna pista habla de una foto.", 2: "El texto no menciona a una esposa."}, "«Ahí va a ir algo» al principio y «ya no estaba vacío» al final: el marco esperaba el diploma.")}
<details class="transc"><summary>Ver la tabla de inferencias completa</summary>
{C.tabla("Pistas, conocimiento previo e inferencias sobre don Ernesto", ["Pista del texto", "Lo que ya sé", "Inferencia"],
         [["Lentes con cinta; cuarenta años poniendo ladrillos; manos con cicatrices.", "Un albañil trabaja con las manos; cuarenta años de trabajo es mucho tiempo.", "Don Ernesto es un hombre mayor, de trabajo duro y con poco dinero para gastos."],
          ["Llega media hora antes; repasa su cuaderno.", "Quien llega temprano a estudiar lo toma en serio.", "Está muy comprometido con sus estudios."],
          ["Borra la respuesta tres veces; no habla con nadie; deja pasar los autobuses.", "La gente preocupada o desanimada a veces se aísla.", "El examen de práctica le salió mal o lo dejó muy preocupado."],
          ["Corbata nueva; sobre y hoja levantada; el marco ya no está vacío.", "Uno se arregla para las ocasiones importantes; los diplomas se ponen en marcos.", "Aprobó el GED y puso su diploma en el marco que tenía guardado para eso."]])}</details>
{C.caja("tip", "Si tiene con quién practicar", "<p>Jueguen a los detectives. Uno describe a una persona solo con pistas («Llevaba un casco, tenía polvo blanco en las botas…») y el otro infiere a qué se dedica y dice qué pista lo llevó a esa idea.</p>")}"""

    secciones = [("s1", "¿Qué es una inferencia?", s1), ("s2", "Qué se puede inferir", s2), ("s3", "¿Inferencia válida o no?", s3), ("s4", "Lectura: «El marco vacío»", s4)]
    tarea = [("Su tabla.", "Termine en su cuaderno la tabla «pista + lo que sé = inferencia» de «El marco vacío» con al menos tres filas propias."),
             ("Responda con evidencia.", "En un párrafo de cuatro o cinco oraciones, responda: ¿qué significaba el marco vacío para don Ernesto? Use al menos dos pistas, una de ellas como cita textual. "
              "<details class=\"transc\"><summary>Ver una respuesta posible</summary><p>El marco vacío representaba una meta que don Ernesto todavía no había alcanzado. Desde el principio, él dice: «Ahí va a ir algo», sin explicar qué. Al final, después de levantar con las dos manos la hoja que sacó del sobre, cuenta que el marco «ya no estaba vacío». Estas pistas permiten inferir que el marco esperaba su diploma del GED, y que colgarlo era la recompensa de tantos años de esfuerzo.</p></details>"),
             ("Escriba con pistas.", "Escriba un párrafo corto sobre una persona que está muy nerviosa, sin usar las palabras <em>nervioso</em> ni <em>nerviosa</em>. Muestre su estado solo con pistas.")]
    quiz = [
        ("Una inferencia se forma con…", ["una pista del texto y lo que usted ya sabe", "su opinión y lo que le gustaría", "las palabras exactas del texto"], 0, {1: "Eso no se apoya en el texto.", 2: "Eso es lo explícito."}, "<strong>Pista + lo que ya sé.</strong>"),
        ("¿Qué palabra de una pregunta avisa que hay que inferir?", ["sugiere", "dice", "nombra"], 0, {1: "Pide lo explícito.", 2: "Pide lo explícito."}, "<strong>Sugiere.</strong>"),
        ("«Pedro bostezó, se frotó los ojos y apoyó la cabeza en la mesa.» ¿Qué inferencia está mejor apoyada?", ["Pedro tiene sueño.", "Pedro está enfermo de gravedad.", "Pedro nunca duerme por las noches."], 0, {1: "Va demasiado lejos.", 2: "<em>Nunca</em> es una señal de alarma."}, "<strong>Tiene sueño.</strong>"),
        ("¿Qué hace inválida a una inferencia?", ["Que no haya pistas que la apoyen", "Que la apoyen dos pistas distintas", "Que sea una conclusión muy breve"], 0, {1: "Eso la hace más fuerte.", 2: "El largo no importa."}, "Que <strong>no haya pistas</strong>."),
        ("¿Por qué «Marta nunca sabe esperar» va demasiado lejos?", ["Una sola escena no dice cómo es Marta siempre", "Porque el texto dice que Marta es paciente", "Porque la palabra nunca es una mala palabra"], 0, {1: "El texto no dice eso.", 2: "No es por la palabra en sí."}, "Una escena no dice cómo es <strong>siempre</strong>."),
        ("Una buena inferencia…", ["la sacarían otros lectores con las mismas pistas", "solo la puede sacar quien tiene imaginación", "no necesita ninguna pista del texto"], 0, {1: "No es una adivinanza.", 2: "Siempre necesita pistas."}, "Otros lectores llegarían a ella."),
        ("Si una sola oración del texto contradice una inferencia, la inferencia…", ["no vale", "sigue valiendo", "se vuelve explícita"], 0, {1: "No.", 2: "No."}, "<strong>No vale.</strong>"),
        ("¿Cuál de estas palabras es una señal de alarma en una inferencia?", ["siempre", "parece", "probablemente"], 0, {1: "Es prudente.", 2: "Es prudente."}, "<strong>Siempre</strong> suele exagerar."),
        ("«La niña apretaba la mano de su madre y no soltaba su peluche en la sala de espera del dentista.» ¿Qué se infiere?", ["La niña está nerviosa o tiene miedo.", "La niña nunca ha ido al dentista.", "La madre es dentista en esa clínica."], 0, {1: "<em>Nunca</em> va demasiado lejos.", 2: "Nada lo sugiere."}, "Las pistas muestran <strong>miedo o nervios</strong>."),
        ("¿Qué es lo más probable que haga alguien que mira el cielo nublado y saca el paraguas antes de salir?", ["Prepararse por si llueve", "Ir a la playa a tomar el sol", "Vender paraguas en la calle"], 0, {1: "Lo contradice el cielo nublado.", 2: "Nada lo sugiere."}, "<strong>Prepararse por si llueve.</strong>"),
    ]
    filas = [
        ("Inferir", "Junto pistas y lo que sé para llegar a una conclusión.", "Me cuesta ver las pistas.", "No sé por dónde empezar (<a href=\"#s1\">repase la sección 1</a>)."),
        ("Validar", "Paso cada inferencia por las tres preguntas.", "A veces exagero.", "Invento sin pistas (<a href=\"#s3\">repase la sección 3</a>)."),
        ("Leer entre líneas", "Deduzco lo que el cuento no dice y lo apoyo con evidencia.", "Deduzco, pero no lo apoyo.", "Solo veo lo explícito (<a href=\"#s4\">repase la sección 4</a>)."),
    ]
    cierre = "<p>Ya lee entre líneas y apoya sus inferencias con evidencia. ¡Terminó el Tema 3! En el Tema 4 verá la <strong>estructura del texto</strong> y el <strong>lenguaje literario</strong>.</p>"
    glosario = [("Inferencia", "Conclusión razonable que se saca de las pistas del texto y de lo que uno ya sabe."), ("Pista", "Un detalle del texto que ayuda a deducir algo que no se dice."),
                ("Conocimiento previo", "Lo que uno ya sabe por su experiencia o por lo que ha leído."), ("Predicción", "Inferencia sobre lo que es probable que pase después.")]
    conexion = ("<p>En la Lección 3.2 distinguió lo explícito de lo inferido. Hoy practica cómo hacer inferencias y cómo saber si están bien apoyadas.</p>"
                "<p><strong>Lo que necesita:</strong> su cuaderno para la tabla «pista + lo que sé = inferencia».</p>")
    estd = LE.estandares(["R.3.1", "W.1"], base=["R.2.8", "R.3.2"])
    return C.pagina_leccion(N, LE.titulo(N), "Leer entre líneas, con pruebas.", ["Comprensión", "Inferencias"],
                            ["<strong>Hacer</strong> inferencias con pistas del texto y lo que ya sabe.", "<strong>Reconocer</strong> las preguntas que piden inferir.",
                             "<strong>Validar</strong> una inferencia con tres preguntas.", "<strong>Leer entre líneas</strong> un cuento y apoyar lo que deduce."],
                            estd, conexion, secciones, tarea, quiz, filas, cierre, ("4-1", LE.titulo("4-1")), glosario, P)


def practica():
    pi = [{"enun": texto(t) + f'<p class="rel">Inferencia: <em>{i}</em></p><p><strong>¿Qué pista la apoya?</strong></p>', "ops": o, "ok": 0,
           "pista": "Esa pista es cierta, pero ¿lleva a esta inferencia? Busque la que la sostiene directamente.", "exp": n} for t, i, o, n in PI]
    mi = [{"enun": texto(t) + f'<p class="rel">{q}</p>', "ops": o, "ok": 0, "pista": "¿Esa inferencia tiene pistas? ¿Algo la contradice? ¿Va más lejos de lo que permite el texto?", "exp": n} for t, q, o, n in MI]
    se = [{"enun": texto(t) + "<p><strong>¿Qué inferencia <u>no</u> tiene evidencia en el texto?</strong></p>", "ops": o, "ok": 0,
           "pista": "Esa sí tiene apoyo en el texto. Busque la que no tiene ninguna pista o la que exagera.", "exp": n} for t, o, n in SE]
    mods = [("pista", "¿Qué pista la apoya?", C.om("m1", "Lea el texto breve y elija la pista que sostiene la inferencia.") + NOTA_T),
            ("mejor", "La mejor inferencia", C.om("m2", "Lea el texto breve y elija la inferencia mejor apoyada.")),
            ("sin-evidencia", "La inferencia sin evidencia", C.om("m3", "Encuentre la inferencia que no tiene pistas en el texto o que exagera."))]
    js = C.js_datos("PI", pi) + C.js_datos("MI", mi) + C.js_datos("SE", se) + 'creaBanco("m1", PI);\ncreaBanco("m2", MI);\ncreaBanco("m3", SE);\n'
    return C.pagina_practica(N, LE.titulo(N), "Tres actividades · los ejercicios cambian cada vez · dos intentos en cada uno", mods, js)


if __name__ == "__main__":
    LE.construye(N, leccion, practica, horas="Unas 3 horas")
