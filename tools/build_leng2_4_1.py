# -*- coding: utf-8 -*-
"""LearnGED · Artes del lenguaje (español) · Nivel 2 · Lección 4.1 · Idea principal en varios párrafos y detalles de apoyo.
Fuente: clases_leng2/clase_4-1.html (GEDparaHispanos) y gramatica/n2-l4-1.html, adaptadas al marco de LearnGED.
Uso: python3 tools/build_leng2_4_1.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import leng_es as LE
from leng_es import C

LE.nivel(2)
N = "4-1"
MSG = {"amplia": "Trampa: <strong>muy amplia</strong>. Es verdad, pero serviría para muchos textos distintos.",
       "detalle": "Trampa: <strong>solo un detalle</strong>. Está en el texto, pero es solo una parte.",
       "fuera": "Trampa: <strong>no está en el texto</strong>. Puede sonar lógica, pero el párrafo no lo dice.",
       "contraria": "Trampa: <strong>contraria</strong>. Dice lo opuesto de lo que dice el párrafo."}
IDEAS = [
    ("La biblioteca pública ofrece mucho más que libros. Allí se pueden usar computadoras con internet, tomar clases de inglés y pedir ayuda para buscar empleo. También hay actividades para niños y préstamo de películas. Todo es gratis con la tarjeta de la biblioteca.",
     "La biblioteca pública ofrece muchos servicios gratuitos además de libros.", [("Los servicios públicos son importantes para toda la comunidad.", "amplia"), ("En la biblioteca se pueden usar computadoras con internet.", "detalle"), ("La biblioteca solo sirve para pedir libros prestados.", "contraria")]),
    ("El cuerpo pierde agua al sudar, al respirar y al ir al baño. Cuando no la reponemos, aparecen el cansancio, el dolor de cabeza y la dificultad para concentrarse. En los días de calor, el riesgo es aún mayor. Por eso es importante beber agua durante todo el día, aunque no tengamos sed.",
     "Es importante beber agua durante el día para reponer la que el cuerpo pierde.", [("En los días de calor, el riesgo de perder agua es mayor.", "detalle"), ("Hay que cuidar la salud de muchas maneras distintas.", "amplia"), ("Solo hace falta beber agua cuando se tiene mucha sed.", "contraria")]),
    ("Lucía llegó a Chicago sin hablar inglés. Los primeros meses no entendía las instrucciones en el trabajo y le daba vergüenza preguntar. Empezó a ir a clases dos noches por semana y a practicar con sus compañeros. Hoy ayuda a otros recién llegados a llenar formularios en inglés.",
     "Con esfuerzo, Lucía pasó de no hablar inglés a poder ayudar a otros.", [("Lucía iba a clases de inglés dos noches por semana.", "detalle"), ("Aprender un idioma nuevo es posible a cualquier edad.", "amplia"), ("Lucía consiguió un trabajo mejor pagado gracias al inglés.", "fuera")]),
    ("Los expertos recomiendan limitar el tiempo que los niños pasan frente a las pantallas. Demasiadas horas con el teléfono o la tableta pueden afectar el sueño y la vista. Además, les quitan tiempo para jugar al aire libre, leer y conversar con la familia.",
     "Conviene limitar el tiempo de los niños frente a las pantallas por sus efectos negativos.", [("Las pantallas pueden afectar la vista de los niños.", "detalle"), ("Los niños deberían usar más la tableta para aprender mejor.", "contraria"), ("La tecnología cambió por completo la vida moderna.", "amplia")]),
    ("Ahorrar un poco cada semana puede hacer una gran diferencia. Quien guarda diez dólares semanales tendrá más de quinientos al final del año. Ese dinero puede servir para una emergencia, como una reparación del carro o una visita al médico. Lo importante no es la cantidad, sino la constancia.",
     "Ahorrar una cantidad pequeña cada semana puede hacer una gran diferencia.", [("Diez dólares por semana suman más de quinientos al año.", "detalle"), ("Los bancos pagan muchos intereses a quienes ahorran.", "fuera"), ("Solo vale la pena ahorrar cuando se tienen cantidades grandes.", "contraria")]),
    ("Cada sábado, un grupo de vecinos recoge la basura del parque. Otros reparan las bancas rotas y pintan los juegos de los niños. Algunos traen café y pan para compartir. Gracias a ellos, el parque está más limpio y seguro que nunca.",
     "El trabajo voluntario de los vecinos mejoró mucho el parque.", [("Algunos vecinos traen café y pan para compartir.", "detalle"), ("Los parques son lugares agradables para toda la familia.", "amplia"), ("La ciudad pagó a una empresa para reparar el parque.", "fuera")]),
    ("Los abuelos cumplen un papel importante en muchas familias hispanas. Cuidan a los nietos mientras los padres trabajan, enseñan recetas y tradiciones, y transmiten la lengua de la familia. Para muchos niños nacidos en Estados Unidos, los abuelos son su principal conexión con el español.",
     "Los abuelos cumplen un papel importante en muchas familias hispanas.", [("Los abuelos les enseñan recetas de cocina a sus nietos.", "detalle"), ("La familia es la base de toda la sociedad.", "amplia"), ("Los niños nacidos aquí ya no necesitan a sus abuelos.", "contraria")]),
    ("La gripe se contagia con facilidad en otoño e invierno. Lavarse las manos con frecuencia, cubrirse la boca al toser y quedarse en casa cuando se está enfermo ayudan a evitar el contagio. La vacuna anual es otra forma eficaz de protegerse.",
     "Hay varias maneras sencillas de protegerse de la gripe.", [("Hay que cubrirse la boca con el brazo al toser.", "detalle"), ("La gripe solo afecta a los niños y a los ancianos.", "fuera"), ("Las enfermedades pueden ser muy peligrosas.", "amplia")]),
    ("Antes de una entrevista de trabajo, conviene informarse sobre la empresa. El día de la cita hay que llegar unos minutos antes y vestirse de manera adecuada. Durante la entrevista, es útil mirar a los ojos, responder con calma y hacer alguna pregunta sobre el puesto.",
     "Prepararse antes y durante una entrevista ayuda a causar buena impresión.", [("Hay que llegar unos minutos antes de la hora de la cita.", "detalle"), ("Conseguir un buen trabajo hoy en día es muy difícil.", "amplia"), ("Las empresas siempre prefieren a quienes tienen experiencia.", "fuera")]),
    ("En muchas ciudades, los autobuses y los trenes funcionan con tarjetas recargables. Basta con acercar la tarjeta al lector para pagar el viaje. La tarjeta se recarga en las estaciones, en algunas tiendas o por internet. Así ya no hace falta llevar monedas exactas.",
     "Las tarjetas recargables hacen más fácil pagar el transporte público.", [("La tarjeta se puede recargar en algunas tiendas.", "detalle"), ("El transporte público es necesario en las ciudades grandes.", "amplia"), ("Para pagar el autobús hay que llevar siempre monedas exactas.", "contraria")])]
NOAPOYA = [
    ("Los perros son buenos compañeros para las personas mayores.", "Los gatos duermen muchas horas al día.", ["Les dan compañía y alegría.", "Los obligan a caminar todos los días.", "Les ayudan a sentirse más seguros en casa."], "Habla de gatos, no de lo que los perros hacen por las personas mayores."),
    ("Cocinar en casa es más sano que comer fuera.", "Los restaurantes de comida rápida abren hasta tarde.", ["Uno controla la cantidad de sal y de grasa.", "Se pueden usar ingredientes frescos.", "Las porciones suelen ser más pequeñas."], "El horario de los restaurantes no tiene que ver con la salud."),
    ("El invierno en Chicago puede ser peligroso.", "En verano hay muchos festivales en la ciudad.", ["Las temperaturas bajan muchos grados bajo cero.", "El hielo en las aceras causa caídas.", "La nieve hace más difícil manejar."], "Habla del verano, no de los peligros del invierno."),
    ("Leer con los hijos tiene muchos beneficios.", "Los libros de la biblioteca se devuelven en tres semanas.", ["Mejora su vocabulario.", "Crea un momento de unión familiar.", "Les despierta el gusto por la lectura."], "Es una regla de la biblioteca, no un beneficio de leer juntos."),
    ("Obtener el GED abre nuevas oportunidades.", "El examen tiene cuatro materias.", ["Permite estudiar en un college.", "Muchos empleos lo piden como requisito.", "Suele ayudar a conseguir un mejor salario."], "Es cierto, pero describe el examen; no muestra una oportunidad."),
    ("Usar casco protege a los ciclistas.", "Chicago tiene muchas ciclovías.", ["Reduce las lesiones en la cabeza.", "Absorbe parte del golpe en una caída.", "Evita muchos accidentes graves."], "Las ciclovías no explican cómo protege el casco."),
    ("El desayuno da energía para empezar el día.", "El café se cultiva en muchos países de América.", ["Después de la noche, el cuerpo necesita alimento.", "Ayuda a concentrarse en el trabajo o la escuela.", "Evita llegar con mucha hambre al almuerzo."], "Dónde se cultiva el café no tiene que ver con la energía del desayuno."),
    ("Las plantas mejoran el ambiente de una casa.", "Algunas plantas son originarias de Asia.", ["Alegran los espacios.", "Ayudan a reducir el estrés de quien las cuida.", "Dan una sensación de frescura."], "El origen de las plantas no muestra cómo mejoran la casa."),
    ("Tener un presupuesto ayuda a controlar los gastos.", "Muchos bancos tienen aplicaciones para el teléfono.", ["Muestra en qué se va el dinero cada mes.", "Permite planear los pagos importantes.", "Ayuda a separar dinero para ahorrar."], "Las aplicaciones de los bancos no explican para qué sirve un presupuesto."),
    ("Las vacaciones son necesarias para la salud.", "Las playas de México reciben muchos turistas.", ["Ayudan a reducir el cansancio acumulado.", "Dan tiempo para dormir y descansar.", "Permiten pasar tiempo con la familia."], "Es un dato sobre turismo, no sobre la salud.")]
TEXTOS = [
    ("Los mercados del barrio",
     ["Los mercados al aire libre que se instalan cada fin de semana venden frutas, verduras, huevos y pan recién hechos. Muchas veces los productos son más frescos que los del supermercado, porque se cosecharon el día anterior, y los precios suelen ser razonables.",
      "Comprar en estos mercados también ayuda a los agricultores de la región. El dinero va directamente a las familias que cultivan los alimentos, sin intermediarios. Así, las pequeñas granjas pueden seguir funcionando.",
      "Además, el mercado es un lugar de encuentro. Los vecinos se saludan, conversan con los vendedores y comparten recetas. En algunos hay música y actividades para los niños."],
     [(["Los mercados venden productos frescos a precios razonables.", "Los huevos del mercado son más grandes que los de la tienda.", "Los supermercados cierran los fines de semana."], 0),
      (["Las granjas grandes no necesitan la ayuda de los vecinos.", "Comprar en el mercado ayuda a los agricultores de la región.", "Los intermediarios ganan mucho dinero con los alimentos."], 1),
      (["En algunos mercados hay música para los niños.", "Los vendedores comparten recetas con sus clientes.", "El mercado es un lugar de encuentro para los vecinos."], 2),
      (["Los mercados del barrio benefician a los compradores, a los agricultores y a la comunidad.", "En los mercados del barrio hay actividades y música para los niños.", "Es mejor no comprar nunca en el supermercado y usar solo el mercado."], 0)]),
    ("Listos para el invierno",
     ["Antes de que llegue el frío, conviene revisar la calefacción de la casa. Un técnico puede limpiar el sistema y comprobar que funciona bien. También es buena idea tapar las rendijas de puertas y ventanas para que no se escape el calor.",
      "El carro necesita su propia preparación. Hay que revisar las llantas, cambiar el líquido del limpiaparabrisas y llevar en el baúl un raspador de hielo, una cobija y una linterna por si hay una emergencia en la carretera.",
      "Por último, hay que cuidarse uno mismo. La ropa en varias capas abriga más que una sola prenda gruesa, y los guantes, el gorro y la bufanda protegen las partes del cuerpo que más se enfrían."],
     [(["Hay que preparar la casa para el frío.", "Los técnicos cobran mucho dinero.", "Las ventanas viejas son peligrosas."], 0),
      (["Hay que llevar una linterna en el carro.", "El carro también necesita prepararse para el invierno.", "Las carreteras se cierran en invierno."], 1),
      (["Los guantes y los gorros son caros.", "La ropa gruesa no sirve para el frío.", "Hay que protegerse el cuerpo con la ropa adecuada."], 2),
      (["Para el invierno hay que preparar la casa, el carro y a uno mismo.", "El invierno es la estación más difícil del año en todas partes.", "Hay que llevar una cobija y un raspador de hielo en el carro."], 0)]),
    ("Nunca es tarde para aprender",
     ["Muchas personas piensan que, después de cierta edad, ya es tarde para volver a estudiar. Creen que la memoria ya no ayuda o que no tendrán tiempo. Sin embargo, miles de adultos terminan cada año sus estudios y consiguen el GED.",
      "Los adultos, de hecho, tienen ventajas. Su experiencia de vida les ayuda a entender muchos temas, y saben por qué estudian: para conseguir un mejor trabajo, para ayudar a sus hijos o por orgullo propio. Esa motivación es muy poderosa.",
      "Para lograrlo, ayuda tener un horario fijo de estudio, ponerse metas pequeñas y celebrar cada avance. Pedir ayuda cuando algo no se entiende no es un fracaso: es parte de aprender."],
     [(["La memoria empeora mucho con la edad.", "Aunque muchos creen que es tarde, muchos adultos sí terminan sus estudios.", "El GED es un examen muy difícil para los adultos."], 1),
      (["Los adultos tienen ventajas al estudiar, como la experiencia y la motivación.", "Los adultos estudian para poder ayudar a sus hijos.", "Los jóvenes aprenden más rápido que los adultos."], 0),
      (["Hay que celebrar cada avance, por pequeño que sea.", "Pedir ayuda cuando algo no se entiende es un fracaso.", "Algunos hábitos sencillos ayudan a lograr la meta."], 2),
      (["El GED es necesario para conseguir un buen trabajo.", "Nunca es tarde para estudiar: los adultos tienen ventajas y pueden lograrlo con buenos hábitos.", "Los adultos deben estudiar todos los días, sin descanso."], 1)])]
DORMIR = ["Muchas personas creen que dormir es perder el tiempo. Trabajan hasta tarde, miran el teléfono en la cama y se levantan cansadas. Sin embargo, los médicos coinciden en que el sueño es tan importante para la salud como la comida o el ejercicio.",
          "Mientras dormimos, el cuerpo se repara. Los músculos se recuperan del esfuerzo del día, el corazón descansa y las defensas se fortalecen. Por eso, quienes duermen poco se enferman con más frecuencia y tardan más en sanar.",
          "El sueño también ayuda a la mente. Durante la noche, el cerebro ordena lo que aprendimos en el día y lo guarda en la memoria. Un estudiante que duerme bien antes de un examen recuerda mejor lo que estudió que uno que pasa la noche en vela.",
          "Los expertos recomiendan que un adulto duerma entre siete y nueve horas. Para lograrlo, aconsejan acostarse siempre a la misma hora, apagar las pantallas una hora antes y evitar el café por la tarde. Dormir bien no cuesta dinero, y sus beneficios se notan en todo el cuerpo."]
PA = "Cada vez más familias de Chicago cultivan sus propias verduras. En patios, balcones y huertos comunitarios siembran tomates, chiles, lechugas y hierbas. Además de ahorrar dinero, comen alimentos más frescos y pasan tiempo juntos al aire libre. Algunas incluso venden lo que les sobra en los mercados del barrio."
PB = "Teresa se levanta a las cinco para preparar el almuerzo de sus hijos. Después trabaja ocho horas en una lavandería. Por la noche, cuando todos duermen, abre su cuaderno y estudia para el examen GED. Los domingos repasa con su hija mayor, que la ayuda con las matemáticas."


def pasaje(t):
    return f'<div class="texto-lectura"><p>{t}</p></div>'


def leccion():
    P = C.Practicas()
    s1 = f"""<p>Encontrar la idea principal es la destreza más importante de la lectura y, a la vez, la que más cuesta. Muchas personas leen un texto entero, entienden cada oración y, aun así, no saben decir de qué se trata. Le pasa a casi todo el mundo, y tiene solución: la idea principal no se adivina, se busca con un método. Tómese su tiempo: lo que aprenda aquí lo usará en todas las lecciones que siguen y en todas las materias del GED.</p>
{C.tabla("Tema, idea principal y detalles", ["", "Pregunta que responde", "Cómo se escribe", "Ejemplo"],
         [["Tema", "¿De qué trata?", "Una o pocas palabras", "El agua"], ["Idea principal", "¿Qué dice el autor sobre el tema?", "Una oración completa", "Beber suficiente agua es necesario para la salud."],
          ["Detalles", "¿Cómo lo explica o lo demuestra?", "Ejemplos, datos, razones", "El agua ayuda a regular la temperatura del cuerpo."]])}
<p class="formula"><strong>Tema</strong> + lo que el autor dice sobre el tema = <strong>idea principal</strong></p>
{C.caja("tip", "Una imagen que ayuda", "<p>Piense en una mesa. La idea principal es el tablero; los detalles son las patas que lo sostienen. Si quita una pata, la mesa sigue en pie. Si quita el tablero, solo quedan patas sueltas que no forman nada.</p>")}
<h3>Ejemplo</h3>
{pasaje("Caminar es uno de los ejercicios más completos que existen. Fortalece el corazón y las piernas, ayuda a controlar el peso y reduce el estrés. Además, no hace falta pagar un gimnasio ni comprar equipos especiales: basta con unos zapatos cómodos.")}
<ul><li><strong>Tema:</strong> caminar.</li><li><strong>¿Qué dice el autor sobre caminar?</strong> Que es uno de los ejercicios más completos.</li>
<li><strong>Idea principal:</strong> Caminar es uno de los ejercicios más completos que existen.</li><li><strong>Detalles:</strong> fortalece el corazón, controla el peso, reduce el estrés, no cuesta dinero.</li></ul>
{P("Compruebe", "¿En qué se diferencian el tema y la idea principal?", ["El tema son pocas palabras; la idea principal es una oración completa", "Son exactamente lo mismo, dicho de dos maneras", "El tema está siempre al final y la idea, al principio"], 0,
   {1: "El tema dice de qué trata; la idea dice qué afirma el autor.", 2: "Su lugar puede cambiar."}, "El tema son <strong>pocas palabras</strong>; la idea, <strong>una oración</strong>.")}"""

    s2 = f"""<p>La idea principal puede estar en tres lugares. Lea cada párrafo, piense cuál es su idea principal y luego compruebe.</p>
<h3>1 · Al principio (lo más frecuente)</h3>
{pasaje("Reciclar en casa es más fácil de lo que parece. Basta con tener dos botes: uno para la basura y otro para el papel, el plástico y las latas. Enjuagar los envases antes de tirarlos toma solo unos segundos. Y en muchas ciudades, como Chicago, el camión del reciclaje pasa cada dos semanas por la puerta.")}
<details class="caja caja-tip"><summary><strong>Ver la idea principal</strong></summary><p>«<strong>Reciclar en casa es más fácil de lo que parece.</strong>» Las demás oraciones muestran por qué es fácil.</p></details>
<h3>2 · Al final (como una conclusión)</h3>
{pasaje("Una tarjeta de crédito permite comprar algo hoy y pagarlo después. Pero si no se paga el total cada mes, el banco cobra intereses que pueden ser muy altos. Una deuda pequeña puede crecer mes a mes hasta volverse difícil de pagar. Por eso, la tarjeta de crédito es útil solo si se usa con mucho cuidado.")}
<details class="caja caja-tip"><summary><strong>Ver la idea principal</strong></summary><p>«<strong>Por eso, la tarjeta de crédito es útil solo si se usa con mucho cuidado.</strong>» <em>Por eso</em> anuncia la conclusión.</p></details>
<h3>3 · En ninguna parte: hay que construirla (idea implícita)</h3>
{pasaje("Don Ramón se levanta a las cuatro de la mañana para su primer trabajo en una panadería. Por la tarde limpia oficinas en el centro. Cuando llega a casa, cansado, abre su cuaderno y estudia inglés una hora con ayuda de su nieto. Los sábados no falta a su clase en la biblioteca.")}
<p>Ninguna oración dice la idea principal. Pregúntese: ¿qué tienen en común todos los detalles?</p>
{P("Compruebe", "¿Cuál es la idea principal del párrafo de don Ramón?", ["Don Ramón trabaja en una panadería desde las cuatro de la mañana.", "Don Ramón se esfuerza mucho para superarse, aunque está muy ocupado.", "Aprender inglés es importante para todos los que viven en Estados Unidos."], 1,
   {0: "Es solo un detalle.", 2: "Es muy amplia y el texto no lo dice."}, "Todos los detalles muestran <strong>esfuerzo</strong>: dos trabajos y estudio.")}
{C.caja("tip", "Cómo construir una idea implícita", "<p>Haga una lista de lo que dice cada oración, busque lo que tienen en común y escríbalo en una sola oración que valga para todas. Si su oración solo sirve para una de ellas, es un detalle; si sirve para cualquier texto, es demasiado general.</p>")}"""

    det = [("Un pase mensual cuesta menos que la gasolina de un mes.", True, "Es un dato que demuestra el ahorro."), ("No hay que pagar estacionamiento en el centro.", True, "Es otra forma de ahorrar."),
           ("La Línea Azul del tren llega hasta el aeropuerto O’Hare.", False, "Es cierto, pero no habla de ahorro."), ("Tampoco hay gastos de seguro ni de reparaciones del carro.", True, "Otra razón del ahorro."),
           ("A muchas personas les gusta escuchar música en el tren.", False, "No tiene relación con el dinero."), ("Una familia puede ahorrar cientos de dólares al año.", True, "Resume el beneficio con un dato.")]
    s3 = f"""<p>Los <strong>detalles de apoyo</strong> explican o demuestran la idea principal. Pueden ser ejemplos, datos (números, fechas), razones o explicaciones. Para saber si una oración es un detalle de apoyo, pregúntese: <em>¿esto ayuda a demostrar la idea principal?</em> Si no, es información secundaria o no tiene relación.</p>
<p class="formula">Idea principal: <strong>«Usar el transporte público ayuda a ahorrar dinero.»</strong></p>
<p>En su cuaderno, escriba <strong>A</strong> (apoya) o <strong>N</strong> (no la apoya) junto a cada oración:</p>
<ol>{"".join(f"<li>{t}</li>" for t, _, _ in det)}</ol>
<details class="caja caja-tip"><summary><strong>Ver las respuestas</strong></summary><ol>{"".join(f"<li><strong>{'Apoya' if a else 'No la apoya'}.</strong> {e}</li>" for _, a, e in det)}</ol></details>
<h3>Textos de varios párrafos</h3>
<p>En un texto largo, cada párrafo tiene su propia idea, y todas juntas forman la idea principal del texto completo. El método tiene tres pasos:</p>
<ol><li><strong>Lea un párrafo y deténgase.</strong> Escriba en el cuaderno su idea en una oración corta.</li><li><strong>Repita con cada párrafo.</strong> Al final tendrá una lista: una oración por párrafo.</li>
<li><strong>Lea su lista y pregúntese qué las une.</strong> Esa respuesta, en una oración, es la idea principal del texto. Muchas veces el título y el primer o el último párrafo le dan la pista.</li></ol>
{C.tabla("Organizador para un texto de varios párrafos", ["Párrafo", "Su idea, en una oración"], [["1", "…"], ["2", "…"], ["3", "…"], ["Todo el texto", "¿Qué une las oraciones de arriba?"]])}
<p>Copie este organizador en su cuaderno: lo usará en la sección 4 y en muchas lecciones más.</p>"""

    tr = [("«Las abejas son necesarias para que muchos cultivos produzcan alimentos.»", "Correcta", "Cubre todo el párrafo, está en el texto y dice lo mismo."),
          ("«Los insectos son importantes para la naturaleza.»", "Muy amplia", "Es verdad, pero sirve para cualquier texto sobre insectos."),
          ("«Las almendras necesitan a las abejas.»", "Solo un detalle", "Está en el texto, pero es solo un ejemplo."),
          ("«La miel de abeja es muy nutritiva.»", "No está en el texto", "Puede ser cierto, pero el párrafo no habla de la miel."),
          ("«Las abejas dañan los cultivos de manzana.»", "Contraria", "Dice lo contrario: las abejas ayudan a los cultivos.")]
    s4 = f"""<p>En los exámenes, la pregunta «¿Cuál es la idea principal?» suele tener una respuesta correcta y varias trampas que parecen buenas. Si conoce las trampas, las descarta rápido:</p>
{C.tabla("Las trampas de las opciones", ["Trampa", "Cómo es", "Cómo la reconoce"],
         [["Muy amplia", "Es verdad, pero sirve para muchos textos.", "Podría ser la idea de un libro entero."], ["Solo un detalle", "Está en el texto, pero es una parte pequeña.", "Solo sirve para una oración o un párrafo."],
          ["No está en el texto", "Suena lógica o es cierta en la vida real.", "No la encuentra al releer."], ["Contraria", "Dice lo opuesto de lo que dice el texto.", "Usa palabras del texto, pero cambia el sentido."]])}
<p>Lea el párrafo y, en su cuaderno, diga qué es cada opción: correcta, muy amplia, solo un detalle, no está en el texto o contraria.</p>
{pasaje("Las abejas son esenciales para nuestra alimentación. Al pasar de flor en flor, transportan el polen que muchas plantas necesitan para producir frutos. Sin ellas, cultivos como las manzanas, las almendras y los melones darían muy poca cosecha. Por eso, la disminución de las abejas preocupa a los agricultores de todo el mundo.")}
<ol type="A">{"".join(f"<li>{t}</li>" for t, _, _ in tr)}</ol>
<details class="caja caja-tip"><summary><strong>Ver las respuestas</strong></summary><ol type="A">{"".join(f"<li><strong>{k}.</strong> {e}</li>" for _, k, e in tr)}</ol></details>
{C.caja("tip", "La prueba final", "<p>Antes de elegir, pregúntese si la opción <strong>cubre todo el texto</strong> (no solo una parte), si <strong>está en el texto</strong> y si <strong>dice lo mismo</strong> que el texto. Solo la correcta pasa las tres pruebas.</p>")}
<h3>Lectura guiada: «Dormir bien: el medicamento más barato»</h3>
<p>Lea el texto con el método: después de cada párrafo, responda su pregunta. Al final, responda la pregunta del texto completo, que es la más importante.</p>
{LE.escuchar(" ".join(DORMIR), "Escuchar el texto")}
<div class="texto-lectura"><p><strong>Dormir bien: el medicamento más barato</strong></p>{"".join(f'<p><span class="num-p">{i}</span> {t}</p>' for i, t in enumerate(DORMIR, 1))}</div>
{P("Párrafo 1", "¿Cuál es su idea?", ["Muchas personas miran el teléfono en la cama.", "El sueño es tan importante para la salud como la comida o el ejercicio.", "Los médicos trabajan hasta tarde por las noches."], 1,
   {0: "Es un detalle.", 2: "El párrafo no dice eso."}, "La idea está al final, después de <em>Sin embargo</em>: esa palabra anuncia lo que el autor de verdad quiere decir.")}
{P("Párrafo 2", "¿Cuál es su idea?", ["Mientras dormimos, el cuerpo se repara.", "El corazón es un músculo que trabaja día y noche.", "Las personas que se enferman deben ir al médico."], 0,
   {1: "El párrafo no dice eso.", 2: "El párrafo no dice eso."}, "La idea está en la primera oración; las demás son detalles: músculos, corazón, defensas.")}
{P("Párrafo 3", "¿Cuál es su idea?", ["Los exámenes del GED son difíciles.", "El sueño ayuda a la mente a guardar lo aprendido.", "Un estudiante pasó la noche en vela."], 1,
   {0: "El párrafo no dice eso.", 2: "Es un detalle, un ejemplo."}, "El ejemplo del estudiante es un detalle que demuestra la idea.")}
{P("Párrafo 4", "¿Cuál es su idea?", ["El café es malo para la salud de todos.", "Para dormir bien hay que seguir algunos consejos sencillos.", "Los adultos duermen demasiadas horas."], 1,
   {0: "Es un detalle, y el texto solo dice que se evite por la tarde.", 2: "Es contraria al texto."}, "El párrafo da la cantidad de horas y tres consejos.")}
{P("Todo el texto", "¿Cuál es la idea principal?", ["Los estudiantes deben dormir bien antes de un examen importante.", "La salud depende de muchas cosas, como la comida y el ejercicio.", "Dormir bien es fundamental para el cuerpo y la mente, y se logra con hábitos sencillos.", "Dormir es perder el tiempo que se podría usar en trabajar."], 2,
   {0: "Solo un detalle.", 1: "Muy amplia.", 3: "Contraria."}, "Une las ideas de los cuatro párrafos.")}
<div class="caja caja-tip"><span class="etiqueta et-verde">Actividad · resuma en dos oraciones</span>
<p>Un buen resumen corto tiene la idea principal y los detalles más importantes, con sus propias palabras. Escriba un resumen de «Dormir bien» en dos oraciones: la primera con la idea principal y la segunda con los dos o tres detalles más importantes.</p>
<p>Revise su resumen: ¿un lector que no conoce el texto entendería de qué trata? ¿Copió oraciones enteras del texto? Si es así, dígalo con sus palabras.</p>
<details><summary><strong>Ver un resumen modelo</strong></summary><p>Dormir bien es tan importante para la salud como comer bien o hacer ejercicio. Mientras dormimos, el cuerpo se repara y el cerebro guarda lo aprendido, y para lograrlo conviene dormir de siete a nueve horas con horarios fijos y sin pantallas antes de acostarse.</p></details>
<p>Si tiene con quién practicar, cuéntele a alguien de su casa de qué trata el texto en menos de un minuto, sin mirarlo.</p></div>"""

    secciones = [("s1", "Tema, idea principal y detalles", s1), ("s2", "¿Dónde está la idea principal?", s2),
                 ("s3", "Los detalles y los textos de varios párrafos", s3), ("s4", "Las trampas y una lectura guiada", s4)]
    tarea = [("Un artículo real.", "Elija un artículo corto de un periódico o de una página de noticias. Use el organizador: una oración por párrafo y la idea de todo el texto."),
             ("Tres trampas.", "Para ese mismo artículo, escriba tres opciones falsas: una muy amplia, un detalle y una contraria."),
             ("Mi resumen.", "Resuma el artículo en dos oraciones, con sus propias palabras.")]
    quiz = [
        ("La <strong>idea principal</strong> de un texto es…", ["La oración que resume lo más importante que dice el autor", "La primera oración del texto, sea cual sea su contenido", "El ejemplo más llamativo que el autor incluye en el texto"], 0,
         {1: "No siempre está en la primera oración.", 2: "Eso es un detalle."}, "Lo más importante que <strong>dice el autor</strong>."),
        (pasaje(PA) + "¿Cuál es el <strong>tema</strong> del texto?", ["Los huertos familiares en Chicago", "Los mercados del barrio", "Las lechugas"], 0, {1: "Solo se mencionan al final.", 2: "Es un detalle."}, "<strong>Los huertos familiares en Chicago.</strong>"),
        (pasaje(PA) + "¿Cuál es la <strong>idea principal</strong>?", ["Muchas familias de Chicago cultivan verduras, y eso les trae beneficios.", "Algunas familias de Chicago venden en el mercado lo que les sobra.", "Las verduras frescas son sanas y conviene comerlas todos los días."], 0,
         {1: "Es solo un detalle.", 2: "Es muy amplia: el texto no habla de eso."}, "Cubre <strong>todo el párrafo</strong>."),
        (pasaje(PA) + "¿Cuál es un <strong>detalle de apoyo</strong>?", ["Comen alimentos más frescos.", "Chicago es una ciudad grande.", "Las familias deberían comer menos carne."], 0, {1: "No apoya la idea.", 2: "El texto no lo dice."}, "<strong>Comen alimentos más frescos.</strong>"),
        (pasaje(PB) + "¿Cuál es la idea principal del párrafo?", ["Teresa se esfuerza mucho para estudiar, aunque está muy ocupada.", "Teresa trabaja ocho horas al día en una lavandería del barrio.", "Los hijos mayores deben ayudar a sus padres con las tareas."], 0,
         {1: "Es solo un detalle.", 2: "Es muy amplia y el texto no lo dice."}, "Todos los detalles muestran su <strong>esfuerzo</strong>."),
        (pasaje(PB) + "En este párrafo, la idea principal…", ["No está escrita: hay que construirla con los detalles", "Está en la primera oración", "Está en la última oración"], 0, {1: "La primera oración es un detalle.", 2: "La última oración es un detalle."}, "Es <strong>implícita</strong>."),
        ("En un texto de varios párrafos, la idea principal del texto completo…", ["Une las ideas de todos los párrafos", "Es siempre la primera oración", "Es la idea del párrafo más largo"], 0, {1: "No siempre.", 2: "El largo no importa."}, "<strong>Une las ideas</strong> de todos los párrafos."),
        ("Una opción que es verdad, pero que serviría para muchos textos distintos, es una trampa…", ["muy amplia", "de solo un detalle", "contraria"], 0, {1: "El detalle es una parte pequeña del texto.", 2: "La contraria dice lo opuesto."}, "<strong>Muy amplia.</strong>"),
        ("¿Qué conviene hacer al leer un texto largo?", ["Escribir una oración con la idea de cada párrafo", "Leerlo una sola vez, lo más rápido posible", "Fijarse solo en el último párrafo"], 0, {1: "Así se pierden las ideas.", 2: "Se pierde el resto del texto."}, "Una <strong>oración por párrafo</strong>."),
        ("Antes de elegir la idea principal en un examen, compruebe que la opción…", ["cubre todo el texto, está en él y dice lo mismo", "es la más larga y la que tiene más detalles", "repite las palabras exactas de la primera oración"], 0, {1: "El largo no la hace correcta.", 2: "Las trampas también usan palabras del texto."}, "Las <strong>tres pruebas</strong>."),
    ]
    filas = [
        ("Idea principal", "Distingo el tema de la idea principal y la encuentro al principio, al final o implícita.", "La encuentro cuando está escrita.", "Confundo la idea con un detalle (<a href=\"#s2\">repase la sección 2</a>)."),
        ("Detalles", "Sé qué oraciones apoyan la idea y cuáles no.", "A veces acepto un dato que no tiene relación.", "No distingo los detalles (<a href=\"#s3\">repase la sección 3</a>)."),
        ("Varios párrafos", "Uso el organizador y descarto las cuatro trampas.", "Uso el organizador, pero caigo en alguna trampa.", "Leo todo de una vez y me pierdo (<a href=\"#s4\">repase la sección 4</a>)."),
    ]
    cierre = "<p>Ya tiene un método para encontrar la idea principal de textos largos. En la próxima lección verá la <strong>estructura de la historia y el propósito del autor</strong>.</p>"
    glosario = [("Tema", "De qué trata un texto, en pocas palabras."), ("Idea principal", "Lo más importante que el autor dice sobre el tema, en una oración."),
                ("Idea implícita", "Idea principal que no está escrita y hay que construir."), ("Detalle de apoyo", "Ejemplo, dato o razón que demuestra la idea principal.")]
    conexion = ("<p>En el Nivel 1 encontró la idea principal de un párrafo. Ahora la buscará en textos de varios párrafos, con un método y aprendiendo a descartar las respuestas trampa del examen.</p>"
                "<p><strong>Lo que necesita:</strong> el cuaderno y lápices de dos colores.</p>")
    estd = LE.estandares(["R.2.1", "R.2.4", "R.2.5"], base=["R.2.2"])
    return C.pagina_leccion(N, LE.titulo(N), "Un método para no perderse en un texto largo.", ["Lectura", "Idea principal"],
                            ["<strong>Distinguir</strong> el tema, la idea principal y los detalles.", "<strong>Encontrar</strong> la idea principal al principio, al final o implícita.",
                             "<strong>Construir</strong> la idea de un texto de varios párrafos.", "<strong>Descartar</strong> las opciones trampa."],
                            estd, conexion, secciones, tarea, quiz, filas, cierre, ("4-2", LE.titulo("4-2")), glosario, P)


def practica():
    idb = [{"enun": pasaje(p) + "<strong>¿Cuál es la idea principal?</strong>", "ops": [ok] + [o for o, _ in tr], "ok": 0,
            "pistas": {i + 1: MSG[k] for i, (_, k) in enumerate(tr)}, "exp": "Cubre todo el párrafo, está en el texto y dice lo mismo."} for p, ok, tr in IDEAS]
    no = [{"enun": f"<p class=\"formula\">Idea principal: <strong>{i}</strong></p><strong>¿Qué oración NO apoya esta idea?</strong>", "ops": [n] + s, "ok": 0,
           "pista": "Esa oración sí ayuda a demostrar la idea. Busque la que habla de otra cosa.", "exp": e} for i, n, s, e in NOAPOYA]
    va = []
    for t, ps, qs in TEXTOS:
        texto = f'<div class="texto-lectura"><p><strong>{t}</strong></p>' + "".join(f'<p><span class="num-p">{i}</span> {p}</p>' for i, p in enumerate(ps, 1)) + "</div>"
        for j, (ops, k) in enumerate(qs):
            todo = j == len(qs) - 1
            va.append({"enun": texto + (f"<strong>Todo el texto · ¿Cuál es la idea principal?</strong>" if todo else f"<strong>Párrafo {j + 1} · ¿Cuál es su idea?</strong>"),
                       "ops": ops, "ok": k, "pista": "Esa opción no vale para los tres párrafos." if todo else "Esa opción es un detalle o no está en el párrafo.",
                       "exp": "Une las ideas de los tres párrafos." if todo else f"Es la idea del párrafo {j + 1}; lo demás son detalles."})
    mods = [("idea", "Encuentre la idea principal", C.om("m1", "Lea el párrafo y elija su idea principal. Si cae en una trampa, verá cuál fue.")),
            ("no-apoya", "¿Cuál no apoya la idea?", C.om("m2", "Encuentre la oración que no apoya la idea principal.")),
            ("varios", "Textos de varios párrafos", C.om("m3", "Lea el texto y responda: la idea de un párrafo o la del texto completo."))]
    js = C.js_datos("ID", idb) + C.js_datos("NO", no) + C.js_datos("VA", va) + 'creaBanco("m1", ID);\ncreaBanco("m2", NO);\ncreaBanco("m3", VA);\n'
    return C.pagina_practica(N, LE.titulo(N), "Tres actividades · los ejercicios cambian cada vez · dos intentos en cada uno", mods, js)


if __name__ == "__main__":
    LE.construye(N, leccion, practica, horas="Unas 3 horas")
