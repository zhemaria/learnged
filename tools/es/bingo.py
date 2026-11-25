"""Crea es/matematicas/juegos/bingo-multiplicacion.html a partir de math/games/multiplication-bingo.html."""
from traduce import Traductor
t = Traductor("math/games/multiplication-bingo.html")
R = t.r
for a, b in [
 ('<html lang="en">', '<html lang="es">'),
 ("<title>Multiplication Bingo · LearnGED</title>", "<title>Bingo de multiplicación · LearnGED</title>"),
 ('<a href="../level-1/index.html">← LearnGED · Math · Level 1</a>', '<a href="../nivel-1/index.html">← LearnGED · Matemáticas · Nivel 1</a>'),
 ("<h1>Multiplication Bingo</h1>", "<h1>Bingo de multiplicación</h1>"),
 ("Practice your times tables and complete a line to call BINGO!", "¡Practique las tablas de multiplicar y complete una línea para cantar BINGO!"),
 ("<summary>Goals</summary>", "<summary>Objetivos</summary>"),
 ("<li>Find products quickly and accurately.</li>", "<li>Hallar productos con rapidez y exactitud.</li>"),
 ("<li>See that the same product can come from different factors.</li>", "<li>Ver que el mismo producto puede salir de factores distintos.</li>"),
 ("<li>Learn the times tables by playing.</li>", "<li>Aprender las tablas de multiplicar jugando.</li>"),
 ("<summary>How to play</summary>", "<summary>Cómo se juega</summary>"),
 ("""            Press
            <strong>Show problem</strong>
            to see a multiplication.""", """            Pulse
            <strong>Mostrar problema</strong>
            para ver una multiplicación."""),
 ("<li>Work out the answer and press the square on your card with that number.</li>", "<li>Calcule el resultado y pulse la casilla de su tarjeta que tiene ese número.</li>"),
 ("<li>If you are right, the square turns green and a new problem appears.</li>", "<li>Si acierta, la casilla se pone verde y aparece un problema nuevo.</li>"),
 ("""            If it is not right, try again. You can use the
            <strong>Hint</strong>
            button if you need it.""", """            Si no es correcto, inténtelo de nuevo. Puede usar el botón
            <strong>Pista</strong>
            si lo necesita."""),
 ("<li>Mark five squares in a line (across, down, or diagonal) to call BINGO!</li>", "<li>¡Marque cinco casillas en línea (horizontal, vertical o diagonal) para cantar BINGO!</li>"),
 ("<summary>Settings</summary>", "<summary>Opciones</summary>"),
 ('<div class="etiqueta-grupo">Level</div>', '<div class="etiqueta-grupo">Nivel</div>'),
 ('aria-pressed="true">Tables 1 to 10</button>', 'aria-pressed="true">Tablas del 1 al 10</button>'),
 ('aria-pressed="false">Tables 2 to 12</button>', 'aria-pressed="false">Tablas del 2 al 12</button>'),
 ('aria-pressed="false">Tables 3 to 12</button>', 'aria-pressed="false">Tablas del 3 al 12</button>'),
 ('<div class="etiqueta-grupo">Center square</div>', '<div class="etiqueta-grupo">Casilla del centro</div>'),
 ('aria-pressed="true">Free center: on</button>', 'aria-pressed="true">Centro libre: sí</button>'),
 ('id="btnNueva">New card</button>', 'id="btnNueva">Tarjeta nueva</button>'),
 ("<h2>Let's play</h2>", "<h2>A jugar</h2>"),
 ("<h3>Current problem</h3>", "<h3>Problema actual</h3>"),
 ('aria-live="polite">Press “Show problem” to start.</div>', 'aria-live="polite">Pulse «Mostrar problema» para empezar.</div>'),
 ('id="btnLlamar">Show problem</button>', 'id="btnLlamar">Mostrar problema</button>'),
 ('id="btnPista">Hint</button>', 'id="btnPista">Pista</button>'),
 ("<h3>Your card</h3>", "<h3>Su tarjeta</h3>"),
 ('aria-label="Five-by-five bingo card"', 'aria-label="Tarjeta de bingo de cinco por cinco"'),
 ("<h3>Your score</h3>", "<h3>Su marcador</h3>"),
 ('<div class="lbl">Problems</div>', '<div class="lbl">Problemas</div>'),
 ('<div class="lbl">Right</div>', '<div class="lbl">Aciertos</div>'),
 ('<div class="lbl">Mistakes</div>', '<div class="lbl">Errores</div>'),
 ("<h3>Problem history</h3>", "<h3>Historial de problemas</h3>"),
 ("<summary>See the problems so far</summary>", "<summary>Ver los problemas hasta ahora</summary>"),
 ("fijarMensaje('Press “Show problem” to start.', 'info');", "fijarMensaje('Pulse «Mostrar problema» para empezar.', 'info');"),
 ("c.textContent = 'FREE';", "c.textContent = 'LIBRE';"),
 ("c.setAttribute('aria-label', 'Free square, already marked');", "c.setAttribute('aria-label', 'Casilla libre, ya marcada');"),
 ("c.setAttribute('aria-label', 'Square with the number ' + estado.valores[i]);", "c.setAttribute('aria-label', 'Casilla con el número ' + estado.valores[i]);"),
 ("fijarMensaje('You marked the whole card!', 'ok');", "fijarMensaje('¡Marcó toda la tarjeta!', 'ok');"),
 ("fijarMensaje('Find the answer on your card and press it.', 'info');", "fijarMensaje('Busque el resultado en su tarjeta y púlselo.', 'info');"),
 ("fijarMensaje('That square is already marked.', 'info');", "fijarMensaje('Esa casilla ya está marcada.', 'info');"),
 ("var ayuda = estado.fallosProblema >= 2 ? ' Press “Hint” if you need it.' : '';", "var ayuda = estado.fallosProblema >= 2 ? ' Pulse «Pista» si la necesita.' : '';"),
 ("fijarMensaje('That is not the answer. Try again.' + ayuda, 'error');", "fijarMensaje('Ese no es el resultado. Inténtelo de nuevo.' + ayuda, 'error');"),
 ("celdas[i].setAttribute('aria-label', 'Square with the number ' + estado.valores[i] + ', marked');", "celdas[i].setAttribute('aria-label', 'Casilla con el número ' + estado.valores[i] + ', marcada');"),
 ("fijarMensaje('Correct!', 'ok');", "fijarMensaje('¡Correcto!', 'ok');"),
 ("fijarMensaje('Card complete! Great work.', 'ok');", "fijarMensaje('¡Tarjeta completa! Muy buen trabajo.', 'ok');"),
 ("fijarMensaje('Look closely at the highlighted square.', 'info');", "fijarMensaje('Mire con atención la casilla resaltada.', 'info');"),
 ("btnLibre.textContent = estado.centroLibre ? 'Free center: on' : 'Free center: off';", "btnLibre.textContent = estado.centroLibre ? 'Centro libre: sí' : 'Centro libre: no';"),
]:
    if a == '<html lang="en">' and a not in t.s: continue
    R(a, b, t.s.count(a) if a in ("fijarMensaje('Press “Show problem” to start.', 'info');",) else 1)
R('<span class="vacio">No problems yet.</span>', '<span class="vacio">Todavía no hay problemas.</span>', 2)
R("fijarMensaje('First press “Show problem.”', 'info');", "fijarMensaje('Primero pulse «Mostrar problema».', 'info');", 2)
t.guarda("es/matematicas/juegos/bingo-multiplicacion.html")
