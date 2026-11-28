# -*- coding: utf-8 -*-
"""LearnGED · Artes del lenguaje (español) · Nivel 1 · Lección 7.6 · El proceso de revisión.
Fuente: clases_leng1/clase_7-6.html (GEDparaHispanos) y gramatica/n1-l7-6.html, adaptadas al marco de LearnGED.
Uso: python3 tools/build_leng1_7_6.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import leng_es as LE
from leng_es import C

LE.nivel(1)
N = "7-6"
ERR = ["Falta la mayúscula inicial", "Falta el punto final", "Es un fragmento: le falta el verbo", "Error de concordancia"]
EXP = ["La oración debe empezar con <strong>mayúscula</strong>.", "La oración debe terminar con <strong>punto</strong>.", "Es un <strong>fragmento</strong>: no tiene verbo y no se entiende sola.",
       "El sujeto y el verbo (o el sustantivo y el adjetivo) <strong>no concuerdan</strong>."]
DIAG = [("el parque está lleno hoy.", 0), ("mi hija trabaja en un hospital.", 0), ("ayer llovió toda la tarde.", 0), ("los martes voy a clase de inglés.", 0),
        ("Compré pan en la tienda", 1), ("Mi hermano vive en Texas", 1), ("Hoy hace mucho frío", 1), ("Los vecinos son muy amables", 1),
        ("Los precios bajos en el mercado.", 2), ("Mi amiga del trabajo.", 2), ("Un día muy largo y cansado.", 2), ("Las flores rojas del jardín.", 2),
        ("Los niños juega en el parque.", 3), ("Mi hermana son enfermera.", 3), ("La casa es muy bonito.", 3), ("Los perros ladra toda la noche.", 3)]
VERSION = [("los niños juega en el parque", "Los niños juegan en el parque.", ["Los niños juega en el parque.", "los niños juegan en el parque"]),
           ("mi casa es grande mi casa tiene jardín", "Mi casa es grande y tiene jardín.", ["Mi casa es grande mi casa tiene jardín.", "mi casa es grande, y mi casa tiene jardín"]),
           ("Llovió mucho. No salí de casa.", "Llovió mucho, por eso no salí de casa.", ["Llovió mucho, pero no salí de casa.", "Llovió mucho porque no salí de casa."]),
           ("Los precios bajos en la tienda.", "Los precios son bajos en la tienda.", ["Los precios bajo en la tienda.", "Los precios, bajos en la tienda."]),
           ("voy al trabajo en autobús es muy práctico", "Voy al trabajo en autobús. Es muy práctico.", ["Voy al trabajo en autobús es muy práctico.", "voy al trabajo, en autobús, es muy práctico"]),
           ("La familia de Ana son muy unida.", "La familia de Ana es muy unida.", ["La familia de Ana son muy unidas.", "La familia de Ana es muy unidos."]),
           ("Mi jefe es amable. Mi jefe es justo. Mi jefe es paciente.", "Mi jefe es amable, justo y paciente.", ["Mi jefe es amable. Mi jefe es justo, paciente.", "Mi jefe, mi jefe es amable, justo y paciente."]),
           ("estudié mucho pero el examen fue difícil", "Estudié mucho, pero el examen fue difícil.", ["Estudié mucho pero, el examen fue difícil.", "estudié mucho, pero el examen fue difícil"])]
TOCAR = [("Los niños *juega* en el parque.", "<strong>juega</strong> debe ser <em>juegan</em>: los niños son varios."),
         ("Mi hermana *son* enfermera.", "<strong>son</strong> debe ser <em>es</em>: mi hermana es una."),
         ("La casa es muy *bonito*.", "<strong>bonito</strong> debe ser <em>bonita</em>: la casa es femenino."),
         ("Los perros *ladra* toda la noche.", "<strong>ladra</strong> debe ser <em>ladran</em>."),
         ("Mis vecinos *es* muy amables.", "<strong>es</strong> debe ser <em>son</em>."),
         ("Las manzanas están muy *rico*.", "<strong>rico</strong> debe ser <em>ricas</em>."),
         ("El autobús *llegaron* tarde.", "<strong>llegaron</strong> debe ser <em>llegó</em>: el autobús es uno."),
         ("Mi hija y yo *va* al mercado los sábados.", "<strong>va</strong> debe ser <em>vamos</em>: mi hija y yo = nosotros.")]
LISTA = ["¿Tiene una oración principal clara?", "¿Todas las oraciones hablan del mismo tema (unidad)?", "¿Las oraciones están unidas con conectores (cohesión)?", "¿Las ideas siguen un orden lógico (coherencia)?",
         "¿Cada oración empieza con mayúscula y termina con punto?", "¿Cada oración tiene verbo (no hay fragmentos)?", "¿Concuerdan los sujetos con los verbos, y los sustantivos con los adjetivos?",
         "¿Hay una oración de cierre?"]


def leccion():
    P = C.Practicas()
    s1 = f"""<p>Es un error creer que se escribe un texto perfecto a la primera. Todos los buenos textos pasan por varios <strong>borradores</strong>. El primero es el punto de partida, no el final.</p>
<p>Al escribir, la mente se concentra en producir ideas; es natural que salgan oraciones incompletas o palabras repetidas. <strong>Revisar</strong> es otra tarea: ya no produce ideas, mejora lo escrito. Usted pasa de autor a lector crítico.</p>
{C.caja("tip", "Idea central", "<p>Escribir y revisar son dos tareas distintas. Sepárelas en el tiempo: deje pasar unos minutos, o unas horas, antes de revisar.</p>")}
{C.tabla("El mismo párrafo, en tres borradores", ["Borrador", "Texto"],
         [["❌ 1", "el mercado de mi barrio esta abierto todos los dias. venden frutas y verduras y carne. los precios bajos. me gusta mucho ir."],
          ["⚠️ 2 · corregido, pero pobre", "El mercado de mi barrio está abierto todos los días. Venden frutas, verduras y carne. Los precios son bajos. Me gusta mucho ir."],
          ["✅ Final", "El mercado de mi barrio es un lugar muy útil para las familias. Está abierto todos los días desde temprano. Allí venden frutas frescas, verduras de la temporada y carne recién traída. Los precios son bajos comparados con los del supermercado. Por eso, es el lugar al que más voy a hacer las compras."]])}
<p>El borrador 1 tiene errores de ortografía y oraciones incompletas. El 2 está corregido, pero suena suelto. El final añade una oración principal, detalles, conectores y un cierre.</p>"""

    s2 = f"""{C.tabla("Revisar en tres pasos", ["Paso", "Qué hacer", "Pregunta"],
         [["🔍 1 · Detectar", "Leer el texto <strong>en voz alta</strong>. Donde usted tropieza, casi seguro hay un problema.", "¿Qué hay mal?"],
          ["🩺 2 · Diagnosticar", "Entender por qué no suena bien: ¿falta un verbo, una mayúscula, un conector? ¿Se repite una palabra?", "¿Por qué está mal?"],
          ["✏️ 3 · Reescribir", "<strong>Añadir</strong> lo que falta, <strong>quitar</strong> lo que sobra, <strong>cambiar</strong> lo que no es preciso.", "¿Cómo lo arreglo?"]])}
{C.caja("tip", "Truco para el paso 1", "<p>Si no puede leer en voz alta, mueva los labios sin sonido. O use el botón <strong>🔊 Voz</strong> de esta página, o el de su teléfono, para que le lean su texto.</p>")}
{C.tabla("Los errores más comunes", ["Error", "❌ Así no", "✅ Así sí"],
         [["Sin mayúscula inicial", "el parque está lleno hoy.", "El parque está lleno hoy."], ["Sin punto final", "Compré pan en la tienda", "Compré pan en la tienda."],
          ["Fragmento (sin verbo)", "Los precios bajos en el mercado.", "Los precios son bajos en el mercado."], ["Falta de concordancia", "Los niños juega en el parque.", "Los niños juegan en el parque."],
          ["Palabra repetida", "La casa es grande. La casa tiene jardín. La casa es vieja.", "La casa es grande, tiene jardín y es vieja."], ["Falta de conector", "Llovió mucho. No salí de casa.", "Llovió mucho; por eso, no salí de casa."]])}
{P("Compruebe", "<em>Mi hermana son enfermera.</em> ¿Qué error tiene?", ERR, 3, {0: "Empieza con mayúscula.", 1: "Termina con punto.", 2: "Sí tiene verbo: son."}, "Error de <strong>concordancia</strong>: debe ser <em>es</em>.")}"""

    s3 = f"""<p>Quien no escribió el texto lo lee con ojos frescos. Si alguien de su casa o un compañero puede leer su párrafo, aprovéchelo. Si no, hágase usted las mismas preguntas después de dejar descansar el texto.</p>
{C.tabla("Pida comentarios concretos", ["Para saber…", "Preguntas"],
         [["💚 Qué funciona", "¿De qué trata mi párrafo, en pocas palabras? ¿Qué parte se entiende mejor? ¿Qué detalle le gustó más?"],
          ["🔵 Qué mejorar", "¿En qué oración se perdió? ¿Hay alguna oración que hable de otra cosa? ¿Qué le gustaría saber que no dije?"]])}
{C.caja("tip", "Si a usted le piden comentar", "<p>Diga primero algo bueno y concreto («usó bien el conector <em>porque</em>») y después una sugerencia en forma de pregunta («¿esta oración tiene verbo?»).</p>")}
{C.caja("ojo", "Al recibir comentarios", "<ul><li><strong>Escuche sin defenderse:</strong> si alguien se perdió, es una pista valiosa, no un ataque.</li><li><strong>Usted decide:</strong> el texto es suyo; use las sugerencias que lo mejoran.</li><li><strong>Dé las gracias:</strong> leer con atención el texto de otro es un regalo de tiempo.</li></ul>")}"""

    s4 = f"""<p>Antes de dar por terminado un párrafo, páselo por esta lista. Cópiela en su cuaderno y úsela cada vez que escriba durante el resto del curso.</p>
<ol class="lista-verif">{"".join(f"<li>{x}</li>" for x in LISTA)}</ol>
{P("Compruebe", "¿Cuál es la mejor versión de <em>«mi casa es grande mi casa tiene jardín»</em>?", ["Mi casa es grande y tiene jardín.", "Mi casa es grande mi casa tiene jardín.", "mi casa es grande, y mi casa tiene jardín"], 0,
   {1: "Faltan el punto entre las ideas o un conector, y se repite «mi casa».", 2: "Falta la mayúscula, el punto y sigue la repetición."}, "<strong>Mi casa es grande y tiene jardín.</strong> Mayúscula, punto, conector y sin repetir.")}"""

    secciones = [("s1", "Por qué revisar", s1), ("s2", "La revisión en tres pasos", s2), ("s3", "Otros ojos: pedir y recibir comentarios", s3), ("s4", "La lista de verificación", s4)]
    tarea = [("Un párrafo viejo.", "Tome uno de los párrafos que escribió en este tema (7.1 a 7.5). Léalo en voz alta y marque donde tropieza."),
             ("Diagnóstico.", "Al lado de cada marca, escriba qué error es: mayúscula, punto, fragmento, concordancia, repetición o conector."),
             ("Versión final.", "Escriba la versión final y pásela por la lista de verificación de la sección 4."),
             ("Otros ojos.", "Si puede, pídale a alguien que lo lea con las preguntas de la sección 3.")]
    quiz = [
        ("¿Qué es un borrador?", ["Una primera versión que se va a mejorar", "El texto final", "Un error"], 0, {1: "El final viene después de revisar.", 2: "No es un error: es un paso."}, "Una <strong>primera versión</strong>."),
        ("¿Cuál es el primer paso de la revisión?", ["Detectar, leyendo en voz alta", "Reescribir todo", "Entregar"], 0, {1: "Primero hay que encontrar qué falla.", 2: "No."}, "<strong>Detectar.</strong>"),
        ("¿Qué se hace al diagnosticar?", ["Entender por qué algo está mal", "Leer en voz alta", "Copiar el texto"], 0, {1: "Eso es detectar.", 2: "No."}, "Entender <strong>por qué</strong>."),
        ("¿Cuáles son las tres operaciones de la reescritura?", ["Añadir, quitar y cambiar", "Leer, copiar y entregar"], 0, {}, "<strong>Añadir, quitar y cambiar.</strong>"),
        ("<em>Los precios bajos en el mercado.</em> ¿Qué error tiene?", ERR, 2, {0: "Tiene mayúscula.", 1: "Tiene punto.", 3: "No hay verbo con el que concordar."}, "Es un <strong>fragmento</strong>."),
        ("<em>Hoy hace mucho frío</em> ¿Qué error tiene?", ERR, 1, {0: "Tiene mayúscula.", 2: "Tiene verbo: hace.", 3: "Concuerda."}, "Le falta el <strong>punto final</strong>."),
        ("¿Por qué conviene dejar pasar un tiempo antes de revisar?", ["Para leer el texto con ojos frescos", "Para olvidarlo"], 0, {}, "Para leerlo con <strong>ojos frescos</strong>."),
        ("Al recibir un comentario, conviene…", ["escuchar sin defenderse", "enojarse", "no cambiar nada nunca"], 0, {1: "Es una pista, no un ataque.", 2: "Usted decide, pero escuche primero."}, "<strong>Escuchar sin defenderse.</strong>"),
        ("¿Qué pregunta da un comentario más útil?", ["¿En qué oración se perdió?", "¿Está bien?"], 0, {}, "Una pregunta <strong>concreta</strong>."),
        ("<em>La casa es muy bonito.</em> ¿Cómo se corrige?", ["La casa es muy bonita.", "La casa son muy bonito.", "la casa es muy bonito"], 0, {1: "Empeora la concordancia.", 2: "Sigue el error y falta la mayúscula."}, "<strong>bonita</strong>: concuerda con casa."),
    ]
    filas = [
        ("Detectar", "Leo en voz alta y encuentro dónde tropiezo.", "Encuentro algunos errores.", "No encuentro nada (<a href=\"#s2\">repase la sección 2</a>)."),
        ("Diagnosticar", "Digo qué tipo de error es cada uno.", "Confundo el fragmento con otros errores.", "No sé qué está mal (<a href=\"#s2\">repase la sección 2</a>)."),
        ("Reescribir", "Corrijo añadiendo, quitando o cambiando, y uso la lista de verificación.", "Corrijo la ortografía, pero no mejoro el texto.", "No sé cómo arreglarlo (<a href=\"#s4\">repase la sección 4</a>)."),
    ]
    cierre = ("<p>Terminó el Tema 7. Ya sabe escribir un párrafo con estructura y cualidades, elegir el tipo de texto, escribir sobre información visual y revisar lo que escribe.</p>"
              "<p>En el Tema 8, el último del nivel, va a trabajar la <strong>comunicación, la tecnología y el proyecto final</strong>.</p>")
    glosario = [("Borrador", "Primera versión de un texto, que se va a mejorar."), ("Revisión", "Mejorar un texto ya escrito: detectar, diagnosticar y reescribir."),
                ("Fragmento", "Grupo de palabras sin verbo que no se entiende solo."), ("Concordancia", "Que el sujeto y el verbo, o el sustantivo y el adjetivo, coincidan en número y género.")]
    conexion = ("<p>Ya sabe estructurar un párrafo, elegir el tipo de texto y escribir sobre información visual. Falta la pieza que distingue a quien escribe bien: revisar.</p>"
                "<p><strong>Lo que necesita:</strong> el cuaderno y uno de los párrafos que escribió en este tema.</p>")
    estd = LE.estandares(["L.1.1", "L.2.1", "W.1"], base=["L.1.5"])
    return C.pagina_leccion(N, LE.titulo(N), "Ningún texto sale perfecto a la primera: se mejora revisando.", ["Escritura", "Convenciones"],
                            ["<strong>Revisar</strong> un texto en tres pasos: detectar, diagnosticar y reescribir.", "<strong>Reconocer</strong> los errores más comunes.",
                             "<strong>Pedir y recibir</strong> comentarios útiles.", "<strong>Usar</strong> la lista de verificación del párrafo."],
                            estd, conexion, secciones, tarea, quiz, filas, cierre, ("8-1", LE.titulo("8-1")), glosario, P)


def practica():
    dia = [{"enun": f"<strong>{o}</strong><br>¿Qué error tiene esta oración?", "ops": ERR, "ok": k, "enOrden": True, "pista": "Mire el principio, el final, si hay verbo y si las palabras concuerdan.", "exp": EXP[k]} for o, k in DIAG]
    ver = [{"enun": f"<strong>{o}</strong><br>¿Cuál es la mejor versión corregida?", "ops": [ok] + d, "ok": 0, "pista": "Revise la mayúscula, el punto, la concordancia y los conectores.", "exp": f"<strong>{ok}</strong>"} for o, ok, d in VERSION]
    toc = [{"consigna": "Toque la palabra que tiene el error de concordancia.", "texto": t, "exp": e} for t, e in TOCAR]
    mods = [("diagnostico", "¿Qué error tiene?", C.om("m1", "Diagnostique el error de cada oración.")),
            ("version", "La mejor versión", C.om("m2", "Elija la versión corregida.")),
            ("tocar", "Encuentre el error", LE.marcar("m3", "Toque la palabra que no concuerda. Después pulse <strong>Comprobar</strong>."))]
    js = C.js_datos("DIA", dia) + C.js_datos("VER", ver) + C.js_datos("TOC", toc) + 'creaBanco("m1", DIA);\ncreaBanco("m2", VER);\ncreaMarcar("m3", TOC);\n'
    return C.pagina_practica(N, LE.titulo(N), "Tres actividades · los ejercicios cambian cada vez · dos intentos en cada uno", mods, js)


if __name__ == "__main__":
    LE.construye(N, leccion, practica, horas="Unas 3 horas")
