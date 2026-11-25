"""Crea es/matematicas/nivel-1/decimales-infinitos.html a partir de math/level-1/infinite-decimals.html."""
from traduce import Traductor, LECCION
t = Traductor("math/level-1/infinite-decimals.html")
R = t.r
lic = [p for p in LECCION if p[0].startswith('<p class="licencia">© 2026.')][0]
R(*lic)
R('<link rel="stylesheet" href="../lesson.css">', '<link rel="stylesheet" href="/math/lesson.css">')
R("<title>Decimals never end · Lesson 3.1 · LearnGED</title>", "<title>Los decimales no se acaban · Lección 3.1 · LearnGED</title>")
R('<a class="lg-logo" href="/"><img src="/img/learnged-logo-horizontal.svg" alt="LearnGED home" height="34"></a><a class="lg-link" href="lesson-3-1.html">← Back to Lesson 3.1</a>',
  '<a class="lg-logo" href="/es/"><img src="/img/learnged-logo-horizontal.svg" alt="Inicio de LearnGED" height="34"></a><a class="lg-link" href="leccion-3-1.html">← Volver a la Lección 3.1</a>')
R('<p class="infd-ruta">Math · Level 1 · Lesson 3.1 · Explore more</p>', '<p class="infd-ruta">Matemáticas · Nivel 1 · Lección 3.1 · Para explorar más</p>')
R("<h1>Decimals never end</h1>", "<h1>Los decimales no se acaban</h1>")
R("<p>To order decimals, you place them on the number line. But the number line hides three ideas that often confuse people: between two decimals there are endless more decimals; adding zeros on the right does not change the value; and rounding means choosing where to stop. Explore each idea with your own hands.</p>",
  "<p>Para ordenar decimales, se ubican en la recta numérica. Pero la recta esconde tres ideas que a menudo confunden: entre dos decimales hay infinitos decimales más; agregar ceros a la derecha no cambia el valor; y redondear quiere decir elegir dónde parar. Explore cada idea con sus propias manos.</p>")
R('<p class="infd-cita">Between 0 and 1 there are endless decimals. And between any two of them, too. Zoom in and see for yourself: each step makes the piece of the line ten times smaller… and it never ends.</p>',
  '<p class="infd-cita">Entre 0 y 1 hay infinitos decimales. Y entre dos cualesquiera de ellos, también. Acérquese y compruébelo: cada paso hace el pedazo de recta diez veces más pequeño… y nunca se acaba.</p>')
R("<h2>1. Zoom in: the line never runs out</h2>", "<h2>1. Acérquese: la recta nunca se acaba</h2>")
R('aria-label="Interactive number line. The panel below describes what it shows."', 'aria-label="Recta numérica interactiva. El panel de abajo describe lo que muestra."')
R('<p class="infd-hint">Press any piece of the line to zoom in on it, or use the buttons.</p>', '<p class="infd-hint">Pulse cualquier pedazo de la recta para acercarse a él, o use los botones.</p>')
R('id="infPaso" type="button">Zoom in one level</button>', 'id="infPaso" type="button">Acercarse un nivel</button>')
R('id="infCaida" type="button">Fall into infinity</button>', 'id="infCaida" type="button">Caer al infinito</button>')
R('id="infAlejar" type="button">Zoom out</button>', 'id="infAlejar" type="button">Alejarse</button>')
R('<div class="et">Zoom level</div>', '<div class="et">Nivel de acercamiento</div>')
R('<div class="et">Piece of the line</div>', '<div class="et">Pedazo de la recta</div>')
R('<div class="et">Size of each step</div>', '<div class="et">Tamaño de cada paso</div>')
R('<div class="et">Decimal places so far</div>', '<div class="et">Lugares decimales recorridos</div>')
R('<div class="et">Left to reach the bottom</div>', '<div class="et">Falta para llegar al fondo</div>')
R('<div class="infd-mensaje" id="infMensaje">The number <strong>1/7 = 0.142857&#8230;</strong> lives inside the highlighted piece. Chase it: no matter how close you get, it always has neighbors.</div>',
  '<div class="infd-mensaje" id="infMensaje">El número <strong>1/7 = 0.142857&#8230;</strong> vive dentro del pedazo resaltado. Persígalo: por más que se acerque, siempre tiene vecinos.</div>')
R("<h2>2. Is 0.1 the same as 0.10 and 0.100?</h2>", "<h2>2. ¿0.1 es lo mismo que 0.10 y 0.100?</h2>")
R("<p>Many people think 0.10 is &#8220;greater than&#8221; or &#8220;different from&#8221; 0.1 because it has more digits. Watch the orange point: when you add zeros, the ruler gets finer, but the point does not move at all.</p>",
  "<p>Mucha gente piensa que 0.10 es «mayor que» 0.1, o «distinto de» 0.1, porque tiene más dígitos. Mire el punto anaranjado: al agregar ceros, la regla se hace más fina, pero el punto no se mueve nada.</p>")
R('aria-label="Number line that shows the point 0.1 while zeros are added on the right."', 'aria-label="Recta numérica que muestra el punto 0.1 mientras se agregan ceros a la derecha."')
R('id="cerMas" type="button">Add a zero</button>', 'id="cerMas" type="button">Agregar un cero</button>')
R('id="cerMenos" type="button">Remove a zero</button>', 'id="cerMenos" type="button">Quitar un cero</button>')
R('<div class="infd-mensaje" id="cerMensaje">The orange point marks the value <strong>0.1</strong>. Press &#8220;Add a zero&#8221; and see that the label changes, but the position does not.</div>',
  '<div class="infd-mensaje" id="cerMensaje">El punto anaranjado marca el valor <strong>0.1</strong>. Pulse «Agregar un cero» y vea que cambia la etiqueta, pero no la posición.</div>')
R("<h2>3. So what does rounding mean?</h2>", "<h2>3. Entonces, ¿qué quiere decir redondear?</h2>")
R("<p>Going down forever is impossible, so at some point you have to <strong>stop</strong> at one level. That is exactly what rounding is: choosing how many decimal places to keep and taking the closest mark. Let&#8217;s see where 1/7 = 0.142857&#8230; lands.</p>",
  "<p>Bajar para siempre es imposible, así que en algún momento hay que <strong>parar</strong> en un nivel. Eso es exactamente redondear: elegir cuántos lugares decimales conservar y quedarse con la marca más cercana. Veamos dónde cae 1/7 = 0.142857&#8230;.</p>")
R('aria-label="Number line that shows 1/7 rounded to different numbers of decimal places."', 'aria-label="Recta numérica que muestra 1/7 redondeado a distintas cantidades de lugares decimales."')
R('data-n="1" type="button">To 1 decimal place</button>', 'data-n="1" type="button">A 1 lugar decimal</button>')
R('data-n="2" type="button">To 2 decimal places</button>', 'data-n="2" type="button">A 2 lugares decimales</button>')
R('data-n="3" type="button">To 3 decimal places</button>', 'data-n="3" type="button">A 3 lugares decimales</button>')
R('data-n="4" type="button">To 4 decimal places</button>', 'data-n="4" type="button">A 4 lugares decimales</button>')
R('<div class="infd-mensaje" id="redMensaje">Choose how many decimal places to round to. The orange point is the real value of 1/7; the blue mark is the closest one, the one we round to.</div>',
  '<div class="infd-mensaje" id="redMensaje">Elija a cuántos lugares decimales redondear. El punto anaranjado es el valor real de 1/7; la marca azul es la más cercana, a la que redondeamos.</div>')
R("<h2>Why do we never reach the end?</h2>", "<h2>¿Por qué nunca llegamos al final?</h2>")
R("<summary>Show the math explanation</summary>", "<summary>Ver la explicación matemática</summary>")
R("<p>Take two different decimals, no matter how close; for example, 0.14 and 0.15. Their average, 0.145, sits exactly between them and is different from both. You can average that number again with either neighbor to get another number in between, and so on, forever.</p>",
  "<p>Tome dos decimales distintos, por más cerca que estén; por ejemplo, 0.14 y 0.15. Su promedio, 0.145, queda justo entre los dos y es distinto de ambos. Puede volver a promediar ese número con cualquiera de sus vecinos para obtener otro número en medio, y así para siempre.</p>")
R("<p>This property is called the <strong>density</strong> of numbers: between any two numbers there is always a third one. So any piece of the number line, no matter how tiny, holds endless decimals.</p>",
  "<p>Esta propiedad se llama <strong>densidad</strong> de los números: entre dos números cualesquiera siempre hay un tercero. Por eso cualquier pedazo de la recta, por pequeño que sea, contiene infinitos decimales.</p>")
R("<p>Zeros on the right add no value because they do not change the position of the point: 0.1, 0.10, and 0.100 name the same place. And rounding does not go against the endless decimals; it accepts them: since going down never ends, we decide which level to stop at and choose the closest mark.</p>",
  "<p>Los ceros a la derecha no agregan valor porque no cambian la posición del punto: 0.1, 0.10 y 0.100 nombran el mismo lugar. Y redondear no va en contra de los infinitos decimales; los acepta: como bajar no se acaba nunca, decidimos en qué nivel parar y elegimos la marca más cercana.</p>")
R('<p style="margin-top:1.4rem"><a href="lesson-3-1.html#s-compare">← Back to Lesson 3.1 · Compare and order decimals</a></p>', '<p style="margin-top:1.4rem"><a href="leccion-3-1.html#s-comparar">← Volver a la Lección 3.1 · Comparar y ordenar decimales</a></p>')
R("<footer><p>LearnGED · Math · Level 1 · Lesson 3.1 · Decimals never end</p>", "<footer><p>LearnGED · Matemáticas · Nivel 1 · Lección 3.1 · Los decimales no se acaban</p>")
# Script
R('msg.innerHTML = "The number <strong>1/7 = 0.142857\\u2026</strong> is still inside the highlighted piece. No matter how close you get, it never runs out of neighbors.";', 'msg.innerHTML = "El número <strong>1/7 = 0.142857\\u2026</strong> sigue dentro del pedazo resaltado. Por más que se acerque, nunca se queda sin vecinos.";')
R('msg.innerHTML = "You are now in a piece of the line that is ten times smaller. Even so, it still holds endless decimals.";', 'msg.innerHTML = "Ahora está en un pedazo de la recta diez veces más pequeño. Aun así, sigue conteniendo infinitos decimales.";')
R('panel("You went down many, many levels\\u2026 and the line is still full of numbers. The drawing stops here, but the math does not: you <strong>never</strong> reach the end. Press \\u201CStart over\\u201D to go back to the top.");',
  'panel("Bajó muchísimos niveles\\u2026 y la recta sigue llena de números. El dibujo se detiene aquí, pero las matemáticas no: <strong>nunca</strong> se llega al final. Pulse \\u00ABEmpezar de nuevo\\u00BB para volver arriba.");')
R('panel("We fell " + prefix.length + " levels, and the piece of the line is only " + amplitudTexto(prefix.length) + " long\\u2026 and it still holds endless decimals. We never reach the bottom: that is infinity.");',
  'panel("Caímos " + prefix.length + " niveles, y el pedazo de recta mide apenas " + amplitudTexto(prefix.length) + "\\u2026 y sigue conteniendo infinitos decimales. Nunca llegamos al fondo: eso es el infinito.");')
R('m.innerHTML = "The orange point marks the value <strong>0.1</strong>. Press \\u201CAdd a zero\\u201D and see that the label changes, but the position does not.";', 'm.innerHTML = "El punto anaranjado marca el valor <strong>0.1</strong>. Pulse \\u00ABAgregar un cero\\u00BB y vea que cambia la etiqueta, pero no la posición.";')
R('m.innerHTML = "<strong>" + etq(z) + " = 0.1</strong>. You added " + z + (z === 1 ? " zero" : " zeros") + ", and the point has not moved at all. Zeros on the right make the ruler finer, but they do not change the value.";',
  'm.innerHTML = "<strong>" + etq(z) + " = 0.1</strong>. Agregó " + z + (z === 1 ? " cero" : " ceros") + ", y el punto no se ha movido nada. Los ceros a la derecha hacen más fina la regla, pero no cambian el valor.";')
R('? ("the next digit is " + sig + " (5 or more), so we go up to the higher mark")', '? ("el dígito siguiente es " + sig + " (5 o más), así que subimos a la marca de arriba")')
R(': ("the next digit is " + sig + " (less than 5), so we keep the lower mark");', ': ("el dígito siguiente es " + sig + " (menos de 5), así que nos quedamos con la marca de abajo");')
R('"To " + N + (N === 1 ? " decimal place" : " decimal places") + ": <strong>0.142857\\u2026 \\u2248 " + elegido + "</strong>, because " + razon + ". Rounding means stopping at this level and choosing the closest mark; all the endless decimals after it are summed up in that choice.";',
  '"A " + N + (N === 1 ? " lugar decimal" : " lugares decimales") + ": <strong>0.142857\\u2026 \\u2248 " + elegido + "</strong>, porque " + razon + ". Redondear es parar en este nivel y elegir la marca más cercana; todos los infinitos decimales que siguen quedan resumidos en esa elección.";')
R('c.fillText("1/7 is here", cx', 'c.fillText("1/7 está aquí", cx')
t.guarda("es/matematicas/nivel-1/decimales-infinitos.html")
