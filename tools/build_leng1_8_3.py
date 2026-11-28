# -*- coding: utf-8 -*-
"""LearnGED · Artes del lenguaje (español) · Nivel 1 · Lección 8.3 · Alfabetización tecnológica y vocabulario digital.
Fuente: clases_leng1/clase_8-3.html (GEDparaHispanos) y gramatica/n1-l8-3.html, adaptadas al marco de LearnGED.
La sección «Cómo moverse por una lección» describe ahora las páginas de LearnGED.
Uso: python3 tools/build_leng1_8_3.py
"""
import os, sys, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import leng_es as LE
from leng_es import C

LE.nivel(1)
N = "8-3"
PARTES = [("🖥️ Monitor", "La pantalla donde vemos imágenes y textos."), ("⌨️ Teclado", "Las teclas para escribir letras, números y símbolos."),
          ("🖱️ Ratón (mouse)", "Mueve el cursor por la pantalla y hace clic."), ("📦 Torre", "La caja que guarda el procesador y la memoria. Mucha gente la llama «el CPU», aunque el CPU es solo el procesador que va adentro."),
          ("🖨️ Impresora", "Pasa al papel lo que está en la pantalla."), ("🔊 Bocinas", "Por ellas sale el sonido.")]
VOCAB = [("ventana", "El marco rectangular donde se ve un programa o un documento.", "Abrí dos ventanas: una con el correo y otra con esta lección."),
         ("pestaña", "Una «hoja» dentro de la misma ventana del navegador.", "Abra una pestaña nueva para buscar sin cerrar esta página."),
         ("ícono", "Una imagen pequeña que representa un programa o un archivo.", "Haga doble clic en el ícono del navegador."),
         ("cursor", "La flecha o la barra que se mueve en la pantalla al mover el ratón.", "Ponga el cursor encima del botón azul."),
         ("archivo", "Un documento, una foto o un video guardado en la computadora.", "El archivo de mi tarea se llama «mi-historia.docx»."),
         ("carpeta", "Un contenedor que guarda varios archivos juntos.", "Guarde la tarea en la carpeta «Tareas Nivel 1»."),
         ("navegador", "El programa con el que se entra a internet, como Chrome, Firefox o Edge.", "Abra el navegador y escriba la dirección."),
         ("enlace", "Una palabra o imagen que, al hacer clic, lleva a otra página.", "Haga clic en el enlace azul para abrir el documento."),
         ("guardar", "Conservar un archivo para no perder lo que se hizo.", "Guarde el documento antes de cerrar la ventana."),
         ("subir", "Enviar un archivo de su computadora o su teléfono a internet.", "Suba la foto de su identificación al formulario."),
         ("descargar", "Traer un archivo de internet a su computadora o su teléfono.", "Descargue el PDF que mandó la escuela."),
         ("adjuntar", "Agregar un archivo a un correo o a un mensaje.", "Adjunte la foto al correo antes de enviarlo.")]
COMPLETA = [("Haga doble clic en el ____ del navegador para abrirlo.", "ícono", ["cursor", "archivo"]), ("Abra una nueva ____ para buscar algo sin cerrar esta página.", "pestaña", ["carpeta", "ícono"]),
            ("Ponga el ____ encima del botón azul y haga clic.", "cursor", ["ícono", "archivo"]), ("Guarde la tarea en la ____ «Tareas Nivel 1».", "carpeta", ["pestaña", "ventana"]),
            ("El ____ de mi tarea se llama «mi-historia.docx».", "archivo", ["navegador", "enlace"]), ("Haga clic en el ____ azul para abrir el documento.", "enlace", ["navegador", "cursor"]),
            ("Abra el ____ y escriba la dirección de la página.", "navegador", ["enlace", "archivo"]), ("____ el documento antes de cerrar la ventana, o perderá los cambios.", "Guarde", ["Descargue", "Suba"]),
            ("La escuela mandó un PDF. Lo voy a ____ para leerlo sin internet.", "descargar", ["subir", "adjuntar"]), ("El formulario pide una foto de su identificación. Tiene que ____ la foto.", "subir", ["descargar", "guardar"]),
            ("Tengo dos ____ abiertas: una con el correo y otra con un documento.", "ventanas", ["carpetas", "enlaces"]), ("Tomé una foto con el celular y quiero ____ al correo.", "adjuntarla", ["descargarla", "guardarla"])]
ATAJOS = [("Ctrl + C", "Copiar", "guarda una copia de lo seleccionado"), ("Ctrl + V", "Pegar", "pone lo copiado donde está el cursor"), ("Ctrl + X", "Cortar", "saca lo seleccionado para pegarlo en otro lugar"),
          ("Ctrl + Z", "Deshacer", "anula la última acción"), ("Ctrl + S", "Guardar", "guarda los cambios del archivo"), ("Ctrl + A", "Seleccionar todo", "marca todo el contenido")]
CASOS = [("Borró un párrafo sin querer. ¿Qué atajo se lo devuelve?", "Ctrl + Z", "Deshacer anula la última acción."),
         ("Quiere mover una oración del principio al final del texto. ¿Qué atajo usa primero?", "Ctrl + X", "Primero se corta; después se pega en el lugar nuevo."),
         ("Ya cortó la oración y puso el cursor al final. ¿Qué atajo usa ahora?", "Ctrl + V", "Pegar pone lo cortado donde está el cursor."),
         ("Lleva media hora escribiendo y no quiere perder nada. ¿Qué atajo usa?", "Ctrl + S", "Guardar a menudo evita perder el trabajo."),
         ("Quiere cambiar el tipo de letra de todo el documento. ¿Qué atajo marca todo el texto?", "Ctrl + A", "Seleccionar todo marca el documento completo."),
         ("Quiere poner su correo en un formulario sin escribirlo otra vez. ¿Qué atajo usa antes de pegarlo?", "Ctrl + C", "Primero se copia; después se pega.")]


def leccion():
    P = C.Practicas()
    s1 = f"""<p>La <strong>alfabetización tecnológica</strong> es usar las herramientas digitales con un propósito. No hace falta ser experto: basta con manejar lo básico con confianza (abrir una ventana, copiar un texto, enviar un correo, guardar un archivo). Lo necesita casi cualquier trabajo, y también el examen GED, que se hace en computadora.</p>
{C.caja("tip", "Idea clave", "<p>Lo importante es conocer las <strong>palabras correctas</strong> para lo que ve en la pantalla. Si sabe decir «se cerró la ventana» en vez de «se cerró eso», puede pedir ayuda con precisión y entender un manual o un video.</p>")}
<h3>El hardware: lo que se puede tocar</h3>
{C.tabla("Partes de una computadora de escritorio", ["Parte", "Para qué sirve"], [list(x) for x in PARTES])}
<p>En una <strong>laptop</strong>, la pantalla, el teclado y el ratón (en forma de <em>touchpad</em>) van en un solo aparato. En un <strong>celular</strong>, la pantalla es a la vez monitor y teclado.</p>
{C.caja("ojo", "El software: lo que no se toca", "<p>El <strong>software</strong> son los programas, las aplicaciones y los archivos que viven dentro del aparato. El navegador con el que lee esta página es software.</p>")}"""

    s2 = f"""{C.tabla("Doce palabras digitales", ["Palabra", "Qué es", "Ejemplo"], [[f"<strong>{p}</strong>", d, f"<em>{e}</em>"] for p, d, e in VOCAB])}
{P("Compruebe", "La escuela le mandó un PDF y lo quiere tener en su teléfono para leerlo sin internet. ¿Qué tiene que hacer?", ["Descargarlo", "Subirlo", "Adjuntarlo"], 0,
   {1: "Subir es enviar algo suyo a internet.", 2: "Adjuntar es agregarlo a un correo."}, "<strong>Descargarlo</strong>: traerlo de internet a su teléfono.")}"""

    s3 = f"""<p>Un <strong>atajo de teclado</strong> es una combinación de teclas que hace una acción rápida sin el ratón: se mantiene presionada la primera tecla (normalmente <kbd>Ctrl</kbd>) y se toca la segunda.</p>
{C.tabla("Los seis atajos más útiles", ["Atajo", "Qué hace"], [[f"<kbd>{a}</kbd>", f"<strong>{b}</strong>: {c}."] for a, b, c in ATAJOS])}
{C.caja("tip", "Truco de memoria", "<p>Las letras vienen del inglés: <strong>C</strong>opy (copiar), <strong>S</strong>ave (guardar), <strong>A</strong>ll (todo). La V está al lado de la C; la X parece unas tijeras; la Z es la de deshacer. En una <strong>Mac</strong> se usa <kbd>⌘ Cmd</kbd> en vez de <kbd>Ctrl</kbd>: copiar es <kbd>⌘ + C</kbd>.</p>")}
{P("Compruebe", "Quiere mover una oración a otro lugar del texto. ¿Qué atajos usa, en orden?", ["Ctrl + X y después Ctrl + V", "Ctrl + C y después Ctrl + Z", "Ctrl + A y después Ctrl + S"], 0,
   {1: "Copiar deja la oración donde estaba, y deshacer anula lo último.", 2: "Eso selecciona todo y guarda."}, "<strong>Cortar y pegar</strong>: Ctrl + X y luego Ctrl + V.")}"""

    s4 = f"""<h3>Cómo moverse por una lección de LearnGED</h3>
<ol><li>Abra el navegador y entre a <strong>www.learnged.com</strong>, o toque el enlace que le dieron.</li>
<li>Lea lo que va a aprender y mire el <strong>contenido de la lección</strong>: toque una parte para ir directo a ella.</li>
<li>Si quiere oír los textos, toque el botón <strong>🔊 Voz</strong> de la barra de arriba.</li>
<li>Responda las preguntas «Compruebe»: si se equivoca, recibe una pista y tiene otro intento.</li>
<li>Al final, haga la tarea en su cuaderno, el cuestionario y la <strong>práctica</strong> de la lección (los ejercicios cambian cada vez).</li></ol>
<h3>Cómo crear su cuenta en GED.com</h3>
<p>Para inscribirse en el examen GED hace falta una cuenta en la página oficial. Las pantallas pueden cambiar, pero los pasos generales son estos:</p>
<ol><li>Abra el navegador y escriba <strong>ged.com</strong>. Fíjese en que sea la página oficial.</li><li>Si aparece, cambie el idioma a español.</li>
<li>Toque el botón para crear una cuenta (en inglés suele decir <em>Sign up</em>).</li><li>Escriba sus datos con cuidado: el nombre completo tal como aparece en su identificación, su fecha de nacimiento y un correo que revise a menudo.</li>
<li>Cree una contraseña segura y anótela en un lugar seguro.</li><li>Revise su correo: le llegará un mensaje para confirmar la cuenta. Toque el enlace.</li>
<li>Entre a su cuenta: ahí verá los exámenes de práctica y, cuando esté listo, podrá programar su examen.</li></ol>
{C.caja("ojo", "Cuidado", "<p>Crear la cuenta en GED.com es <strong>gratis</strong>. Desconfíe de páginas que le cobren por crearla o que le prometan el diploma sin presentar el examen.</p>")}"""

    secciones = [("s1", "Las partes de la computadora", s1), ("s2", "Vocabulario digital", s2), ("s3", "Atajos de teclado", s3), ("s4", "LearnGED y GED.com, paso a paso", s4)]
    tarea = [("Mis palabras digitales.", "Escriba en su cuaderno las doce palabras de la sección 2 con un ejemplo propio de cada una."),
             ("Practique los atajos.", "En un documento o en el correo, escriba una oración, cópiela, péguela, córtela y deshaga el cambio. Anote qué atajo usó en cada paso."),
             ("Mi cuenta.", "Si todavía no la tiene, cree su cuenta en GED.com con la lista de la sección 4. Anote su correo y guarde su contraseña en un lugar seguro.")]
    quiz = [
        ("¿Qué es el hardware?", ["Las partes físicas que se pueden tocar", "Los programas", "Internet"], 0, {1: "Eso es software.", 2: "No."}, "Lo que se <strong>puede tocar</strong>."),
        ("¿Qué es el navegador?", ["El programa para entrar a internet", "Una carpeta", "El ratón"], 0, {1: "No.", 2: "Eso es hardware."}, "El programa para <strong>entrar a internet</strong>."),
        ("¿Qué es una pestaña?", ["Una «hoja» dentro de la misma ventana del navegador", "Una carpeta", "Un ícono"], 0, {1: "No.", 2: "No."}, "Una <strong>hoja</strong> dentro de la ventana."),
        ("Enviar una foto de su teléfono a un formulario en internet es…", ["subir", "descargar", "cortar"], 0, {1: "Descargar es traer de internet.", 2: "No."}, "<strong>Subir.</strong>"),
        ("¿Qué hace <kbd>Ctrl + Z</kbd>?", ["Deshacer", "Guardar", "Copiar"], 0, {1: "Guardar es Ctrl + S.", 2: "Copiar es Ctrl + C."}, "<strong>Deshacer.</strong>"),
        ("¿Qué atajo pega lo copiado?", ["Ctrl + V", "Ctrl + C", "Ctrl + A"], 0, {1: "Ese copia.", 2: "Ese selecciona todo."}, "<strong>Ctrl + V.</strong>"),
        ("En una Mac, ¿qué tecla reemplaza a Ctrl?", ["⌘ Cmd", "Alt", "Shift"], 0, {1: "No.", 2: "No."}, "<strong>⌘ Cmd.</strong>"),
        ("¿Cuánto cuesta crear la cuenta en GED.com?", ["Es gratis", "Hay que pagar para crearla"], 0, {}, "Es <strong>gratis</strong>."),
        ("¿Cómo debe escribir su nombre en GED.com?", ["Tal como aparece en su identificación", "Con un apodo"], 0, {}, "<strong>Como en su identificación.</strong>"),
        ("¿Cómo se hace el examen GED?", ["En computadora", "A mano, en papel"], 0, {}, "En <strong>computadora</strong>."),
    ]
    filas = [
        ("Vocabulario digital", "Nombro las partes de la computadora y las doce palabras digitales.", "Conozco algunas.", "Digo «eso» en vez del nombre (<a href=\"#s2\">repase la sección 2</a>)."),
        ("Atajos", "Uso copiar, pegar, cortar, deshacer, guardar y seleccionar todo.", "Uso copiar y pegar.", "No los uso (<a href=\"#s3\">repase la sección 3</a>)."),
        ("GED.com", "Sé crear mi cuenta y reconocer la página oficial.", "Necesito ayuda para algún paso.", "No sé por dónde empezar (<a href=\"#s4\">repase la sección 4</a>)."),
    ]
    cierre = "<p>Ya tiene el vocabulario y los atajos básicos. En la próxima lección va a preparar una <strong>presentación oral breve</strong>: el ensayo de su proyecto final.</p>"
    glosario = [("Hardware", "Las partes físicas de la computadora."), ("Software", "Los programas y archivos."), ("Navegador", "Programa para entrar a internet."),
                ("Atajo de teclado", "Combinación de teclas que hace una acción rápida."), ("Subir / descargar", "Enviar un archivo a internet / traerlo de internet.")]
    conexion = ("<p>En las Lecciones 8.1 y 8.2 trabajó la comunicación oral. Ahora va a trabajar otra destreza que necesita para el examen y para la vida: usar la computadora con confianza.</p>"
                "<p><strong>Lo que necesita:</strong> una computadora o un teléfono, y el cuaderno.</p>")
    estd = LE.estandares([], base=["R.4.1"], fund=["SL.2"])
    return C.pagina_leccion(N, LE.titulo(N), "Las palabras de la pantalla, para pedir ayuda y no perderse.", ["Tecnología", "Vocabulario"],
                            ["<strong>Nombrar</strong> las partes de la computadora y distinguir hardware de software.", "<strong>Usar</strong> doce palabras del vocabulario digital.",
                             "<strong>Usar</strong> seis atajos de teclado.", "<strong>Moverse</strong> por una lección de LearnGED y crear la cuenta en GED.com."],
                            estd, conexion, secciones, tarea, quiz, filas, cierre, ("8-4", LE.titulo("8-4")), glosario, P)


def practica():
    r = random.Random(83)
    pals = [p for p, _, _ in VOCAB]
    voc = [{"enun": f"<strong>{d}</strong><br>¿Qué palabra corresponde a esta definición?", "ops": [p] + r.sample([x for x in pals if x != p], 2), "ok": 0, "pista": "Piense en el ejemplo de cada palabra.",
            "exp": f"Es <strong>{p}</strong>. Ejemplo: {e}"} for p, d, e in VOCAB]
    com = [{"enun": f"Complete la oración.<br><strong>{o}</strong>", "ops": [ok] + d, "ok": 0, "pista": "Lea la oración completa: ¿qué se hace o qué se usa?", "exp": f"Va <strong>{ok}</strong>."} for o, ok, d in COMPLETA]
    ata = []
    for a, b, c in ATAJOS:
        otros = [x for x in ATAJOS if x[0] != a]
        ata.append({"enun": f"¿Qué hace el atajo <strong>{a}</strong>?", "ops": [b] + [x[1] for x in r.sample(otros, 2)], "ok": 0, "pista": "Recuerde: C copia, V pega, X corta, Z deshace, S guarda, A selecciona todo.", "exp": f"<strong>{a}</strong>: {b.lower()}, {c}."})
        ata.append({"enun": f"¿Qué atajo sirve para <strong>{b.lower()}</strong>?", "ops": [a] + [x[0] for x in r.sample(otros, 2)], "ok": 0, "pista": "Recuerde: C copia, V pega, X corta, Z deshace, S guarda, A selecciona todo.", "exp": f"<strong>{a}</strong>: {c}."})
    for q, a, e in CASOS:
        ata.append({"enun": q, "ops": [a] + r.sample([x[0] for x in ATAJOS if x[0] != a], 2), "ok": 0, "pista": "Piense qué acción necesita: copiar, pegar, cortar, deshacer, guardar o seleccionar todo.", "exp": f"<strong>{a}</strong>. {e}"})
    mods = [("vocabulario", "¿Qué palabra es?", C.om("m1", "Elija la palabra digital que corresponde.")),
            ("completar", "Complete la oración", C.om("m2", "Elija la palabra que completa la oración.")),
            ("atajos", "Los atajos de teclado", C.om("m3", "Elija el atajo o la acción."))]
    js = C.js_datos("VOC", voc) + C.js_datos("COM", com) + C.js_datos("ATA", ata) + 'creaBanco("m1", VOC);\ncreaBanco("m2", COM);\ncreaBanco("m3", ATA);\n'
    return C.pagina_practica(N, LE.titulo(N), "Tres actividades · los ejercicios cambian cada vez · dos intentos en cada uno", mods, js)


if __name__ == "__main__":
    LE.construye(N, leccion, practica, horas="Unas 3 horas")
