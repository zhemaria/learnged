# -*- coding: utf-8 -*-
"""LearnGED · Artes del lenguaje (español) · Nivel 3 · Lección 2.2 · Raíces griegas y latinas; definir con sus palabras.
Fuente: clases_leng3/clase_2-2.html (GEDparaHispanos) y gramatica/n3-l2-2.html, adaptadas al marco de LearnGED.
Uso: python3 tools/build_leng3_2_2.py
"""
import os, sys, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import leng_es as LE
from leng_es import C

LE.nivel(3)
N = "2-2"


def W(palabra):
    """Marca las raíces escritas entre corchetes: «[eco][logía]» → raíces resaltadas al mostrar."""
    palabra = palabra.replace("][", "]\x00[")
    return re.sub(r"\[([^\]]+)\]", r'<b class="rz">\1</b>', palabra).replace("\x00", '<span class="rz-sep" aria-hidden="true">·</span>')


TEXTO = [W("La [eco][logía] es la ciencia que estudia las relaciones entre los seres vivos y su ambiente. Una [eco]loga observa, por ejemplo, cómo los herbí[voro]s, como el venado, se alimentan de plantas; cómo los carní[voro]s, como el lobo, cazan a otros animales; y cómo los [omni][voro]s, como el oso, comen de todo."),
         W("Las plantas producen su propio alimento mediante la [foto]síntesis: usan la luz del sol para transformar el agua y el dióxido de carbono en azúcares. Muchos seres vivos son tan pequeños que solo se ven con un [micro][scopio]; son los [micro]organismos, como las bacterias, que descomponen los restos de plantas y animales y devuelven sus nutrientes a la tierra."),
         W("La [eco][logía] se relaciona con otras ciencias, como la [geo][logía], que estudia la tierra y sus rocas, y la [hidro][logía], que estudia el agua. Para medir los cambios en la naturaleza, los científicos usan [termó][metro]s, [cronó][metro]s y [foto][grafía]s tomadas desde satélites. Con esos datos estudian la [bio]diversidad, es decir, la variedad de seres vivos que hay en un lugar.")]
GRIEGAS = [("bio", "vida", "biología, biografía, antibiótico"), ("geo", "tierra", "geografía, geología"), ("hidro", "agua", "hidratar, hidroeléctrica"), ("termo", "calor, temperatura", "termómetro, termo"),
           ("foto", "luz", "fotografía, fotosíntesis"), ("fono", "sonido, voz", "teléfono, micrófono"), ("grafía, grama", "escritura, descripción", "ortografía, telegrama, geografía"),
           ("logía", "estudio, ciencia", "biología, psicología"), ("metro", "medida", "termómetro, kilómetro"), ("tele", "lejos", "televisión, teléfono"), ("micro", "pequeño", "microscopio, microbio"),
           ("scopio", "instrumento para ver", "microscopio, telescopio"), ("crono", "tiempo", "cronómetro, cronología"), ("psico", "mente", "psicología, psicólogo"),
           ("demo · cracia", "pueblo · gobierno, poder", "democracia, demografía"), ("auto", "uno mismo", "autobiografía, automóvil"), ("eco", "casa, ambiente", "ecología, economía")]
LATINAS = [("acu, acua", "agua", "acuático, acuario, acueducto"), ("port", "llevar", "transportar, exportar, portátil"), ("dic, dict", "decir", "dictar, contradecir, predicción"),
           ("scrib, scrit", "escribir", "escribir, inscribir, manuscrito"), ("vid, vis", "ver", "visión, evidencia, visible"), ("spect", "mirar", "espectador, inspector"),
           ("struct", "construir", "construcción, estructura, destruir"), ("rupt", "romper", "interrumpir, erupción"), ("mis, mit", "enviar", "transmitir, misión, emisora"),
           ("duc", "llevar, guiar", "conducir, producir"), ("voro", "que come", "carnívoro, herbívoro"), ("cida", "que mata", "insecticida, pesticida"), ("omni", "todo", "omnívoro, omnipresente"),
           ("multi", "muchos", "multitud, multiplicar")]
RA = [("bio", "biología, biografía", ["vida", "tierra", "luz"], "griega"), ("geo", "geografía, geología", ["tierra", "agua", "pueblo"], "griega"),
      ("hidro", "hidratar, hidroeléctrica", ["agua", "calor", "sonido"], "griega"), ("termo", "termómetro, termo", ["calor", "tiempo", "medida"], "griega"),
      ("foto", "fotografía, fotosíntesis", ["luz", "vida", "escritura"], "griega"), ("fono", "teléfono, micrófono", ["sonido, voz", "lejos", "pequeño"], "griega"),
      ("grafía", "ortografía, geografía", ["escritura, descripción", "estudio, ciencia", "medida"], "griega"), ("logía", "biología, psicología", ["estudio, ciencia", "escritura", "gobierno"], "griega"),
      ("metro", "kilómetro, termómetro", ["medida", "tiempo", "tierra"], "griega"), ("tele", "televisión, teléfono", ["lejos", "pequeño", "uno mismo"], "griega"),
      ("micro", "microscopio, microbio", ["pequeño", "lejos", "muchos"], "griega"), ("crono", "cronómetro, cronología", ["tiempo", "calor", "mente"], "griega"),
      ("psico", "psicología, psicólogo", ["mente", "vida", "pueblo"], "griega"), ("demo", "democracia, demografía", ["pueblo", "gobierno", "tierra"], "griega"),
      ("auto", "autobiografía, automóvil", ["uno mismo", "todo", "lejos"], "griega"), ("acua", "acuático, acuario", ["agua", "aire", "tierra"], "latina"),
      ("port", "transportar, exportar", ["llevar", "romper", "mirar"], "latina"), ("dict", "dictar, predicción", ["decir", "escribir", "ver"], "latina"),
      ("vis", "visión, visible", ["ver", "enviar", "construir"], "latina"), ("struct", "construcción, estructura", ["construir", "romper", "llevar"], "latina"),
      ("rupt", "interrumpir, erupción", ["romper", "construir", "decir"], "latina"), ("voro", "carnívoro, herbívoro", ["que come", "que mata", "que vive"], "latina"),
      ("cida", "insecticida, pesticida", ["que mata", "que come", "que cura"], "latina"), ("omni", "omnívoro, omnipresente", ["todo", "muchos", "uno mismo"], "latina")]
CN = [("Estudio de los seres vivos", ["biología", "geología", "biografía"], "<em>bio</em> (vida) + <em>logía</em> (estudio)."),
      ("Instrumento para ver objetos lejanos", ["telescopio", "microscopio", "telégrafo"], "<em>tele</em> (lejos) + <em>scopio</em> (instrumento para ver)."),
      ("Historia de la vida de una persona escrita por otra", ["biografía", "autobiografía", "bibliografía"], "<em>bio</em> (vida) + <em>grafía</em> (escritura). Si la escribe la misma persona, es <em>autobiografía</em>."),
      ("Instrumento que mide el tiempo con precisión", ["cronómetro", "termómetro", "cronología"], "<em>crono</em> (tiempo) + <em>metro</em> (medida)."),
      ("Animal que se alimenta de carne", ["carnívoro", "herbívoro", "omnívoro"], "<em>carni</em> (carne) + <em>voro</em> (que come)."),
      ("Producto que mata las plagas del campo", ["pesticida", "pestilencia", "insectívoro"], "<em>peste</em> + <em>cida</em> (que mata)."),
      ("Descripción de la tierra: países, ríos, montañas", ["geografía", "geología", "hidrografía"], "<em>geo</em> (tierra) + <em>grafía</em> (descripción)."),
      ("Forma de gobierno en la que el pueblo elige", ["democracia", "demografía", "autocracia"], "<em>demo</em> (pueblo) + <em>cracia</em> (gobierno)."),
      ("Aparato que capta la voz para grabarla o amplificarla", ["micrófono", "teléfono", "microscopio"], "<em>micro</em> + <em>fono</em> (voz, sonido)."),
      ("Que se puede llevar de un lugar a otro", ["portátil", "portador", "importante"], "<em>port</em> (llevar)."),
      ("Corte o pausa en algo que estaba pasando", ["interrupción", "erupción", "construcción"], "<em>inter</em> (entre) + <em>rupt</em> (romper)."),
      ("Persona que aprende por su cuenta, sin maestro", ["autodidacta", "autobiografía", "automóvil"], "<em>auto</em> (uno mismo) + <em>didacta</em> (que enseña).")]
RF = [("termómetro", ["Instrumento que mide la temperatura del cuerpo o del aire.", "Lo que sirve para saber si algo es térmico.", "Algo que se usa en casa cuando hay fiebre."], "Categoría (instrumento) y rasgo (mide la temperatura). La segunda gira en círculo y la tercera da solo un uso."),
      ("geología", ["Ciencia que estudia la tierra, sus rocas y su formación.", "Lo que estudian los geólogos en la universidad.", "Una materia difícil de la escuela de ciencias."], "Categoría (ciencia) y rasgo (qué estudia)."),
      ("herbívoro", ["Animal que se alimenta de plantas.", "Un animal que es herbívoro, como la vaca.", "La vaca, el caballo, el venado y la oveja."], "Categoría y rasgo. Dar ejemplos ayuda, pero no es una definición."),
      ("democracia", ["Forma de gobierno en la que el pueblo elige a sus gobernantes.", "Lo que tienen todos los países que son democráticos.", "El sistema de los Estados Unidos y de muchos países más."], "Categoría (forma de gobierno) y rasgo (el pueblo elige)."),
      ("microscopio", ["Instrumento para ver cosas que no se ven a simple vista.", "Un aparato microscópico que es muy caro de comprar.", "Lo que usan los científicos en los laboratorios."], "Categoría y rasgo, sin repetir la palabra."),
      ("biografía", ["Relato de la vida de una persona, escrito por otra.", "Un libro biográfico sobre alguien muy famoso.", "Lo que se lee a veces en la clase de historia."], "Categoría (relato) y rasgo (la vida de alguien, escrita por otro)."),
      ("insecticida", ["Producto que se usa para matar insectos.", "Algo que es insecticida y que huele fuerte.", "Lo que se compra cuando hay cucarachas."], "Categoría (producto) y rasgo (mata insectos)."),
      ("cronología", ["Lista de hechos ordenados según el tiempo en que ocurrieron.", "Lo que tiene que ver con todo lo que es cronológico.", "Una de las partes de los libros de historia del colegio."], "Categoría (lista) y rasgo (ordenada en el tiempo)."),
      ("acueducto", ["Construcción que lleva agua de un lugar a otro.", "Un tipo de conducto acuático muy antiguo.", "Lo que construyeron los romanos en sus ciudades."], "Categoría (construcción) y rasgo (lleva agua). Se forma con <em>acua</em> (agua) y <em>duc</em> (llevar)."),
      ("telescopio", ["Instrumento para observar objetos que están muy lejos.", "Un aparato telescópico que se usa para mirar.", "Algo que usan los astrónomos de noche en el campo."], "Categoría y rasgo, sin repetir la palabra.")]


def leccion():
    P = C.Practicas()
    s1 = f"""<p>¿Qué será un <strong>hidrómetro</strong>? Aunque nunca haya visto la palabra, puede adivinarlo: <em>hidro</em> está en <em>hidratarse</em> y en <em>hidroeléctrica</em>, y tiene que ver con el agua; <em>metro</em> está en <em>termómetro</em> y en <em>kilómetro</em>, y tiene que ver con medir. Un hidrómetro es un instrumento que mide algo del agua. Muchas palabras de los textos de Ciencias y de Estudios Sociales del GED se construyen así, con piezas que vienen del griego y del latín.</p>
<p>En el Nivel 2 aprendió que muchas palabras tienen <strong>prefijo</strong> (al principio), <strong>raíz</strong> (el centro, con el significado principal) y <strong>sufijo</strong> (al final):</p>
<p class="formula">des + orden + ado → desordenado</p>
<p>Las palabras de esta lección son un poco distintas: casi siempre se forman con <strong>dos raíces</strong> unidas, como dos piezas de un rompecabezas:</p>
<p class="formula">bio (vida) + logía (estudio) → biología: el estudio de la vida</p>"""

    s2 = f"""<p>El griego antiguo dio al español la mayoría de las palabras de la ciencia. Estas son las raíces que más va a encontrar:</p>
{C.tabla("Raíces griegas frecuentes con su significado y ejemplos", ["Raíz", "Significa", "Ejemplos"], [[f"<strong>{a}</strong>", b, c] for a, b, c in GRIEGAS])}
{C.caja("tip", "Dos de Estudios Sociales", "<p><strong>Democracia</strong> es el gobierno (<em>cracia</em>) del pueblo (<em>demo</em>), y <strong>cronología</strong> es el estudio (<em>logía</em>) del orden en el tiempo (<em>crono</em>). Las dos salen mucho en el GED de Estudios Sociales.</p>")}
{P("Griega 1", "Por sus raíces, ¿qué es un <em>termómetro</em>?", ["Un aparato que transmite sonidos lejos", "Un instrumento que mide la temperatura", "Un instrumento que mide el tiempo"], 1, {0: "Eso sería con <em>tele</em> y <em>fono</em>.", 2: "Eso sería con <em>crono</em>."}, "<em>termo</em> (calor) + <em>metro</em> (medida).")}
{P("Griega 2", "¿Qué palabra significa «estudio del orden de los hechos en el tiempo»?", ["cronómetro", "biografía", "cronología"], 2, {0: "Un <em>cronómetro</em> mide el tiempo.", 1: "Una <em>biografía</em> cuenta una vida."}, "<em>crono</em> (tiempo) + <em>logía</em> (estudio).")}"""

    s3 = f"""<p>El español viene del latín, así que muchas raíces latinas ya están dentro de palabras que usa todos los días:</p>
{C.tabla("Raíces latinas frecuentes con su significado y ejemplos", ["Raíz", "Significa", "Ejemplos"], [[f"<strong>{a}</strong>", b, c] for a, b, c in LATINAS])}
{C.caja("tip", "La misma idea en las dos lenguas", "<p>El agua es <em>hidro</em> en griego y <em>acua</em> en latín. Por eso tenemos a la vez <em>hidratarse</em> y <em>acuático</em>.</p>")}
{C.caja("tip", "Le sirve también en inglés", "<p>Estas raíces están igual en muchas palabras inglesas: <em>transport, inspector, structure, interrupt, evidence</em>. Si estudia inglés, aprenderlas le ayuda en los dos idiomas.</p>")}
{P("Latina 1", "La raíz latina <em>port</em>, de <em>transportar</em> y <em>exportar</em>, significa…", ["romper", "llevar", "mirar"], 1, {0: "Esa es <em>rupt</em>.", 2: "Esa es <em>spect</em>."}, "<em>Port</em> significa <strong>llevar</strong>.")}
{P("Latina 2", "Un animal <em>herbívoro</em>…", ["se alimenta de carne", "se alimenta de todo", "se alimenta de plantas"], 2, {0: "Ese es el carnívoro.", 1: "Ese es el omnívoro."}, "<em>herbi</em> (hierba) + <em>voro</em> (que come).")}"""

    s4 = f"""<p>Cuando encuentre una palabra larga que no conoce, siga tres pasos:</p>
<ol class="proceso"><li><strong>Sepárela</strong> en piezas que reconozca: <em>hidro · grafía</em>.</li>
<li><strong>Junte los significados</strong> en una idea: «descripción del agua».</li>
<li><strong>Compruebe con el contexto:</strong> «La hidrografía de México incluye ríos, lagos y lagunas». Sí: es la descripción de las aguas de un lugar.</li></ol>
{C.caja("ojo", "Una pista, no una prueba", "<p>Las raíces le dan una idea, pero el significado exacto lo confirma el contexto o el diccionario. Por ejemplo, <em>economía</em> tiene <em>eco</em> (casa), pero hoy no significa «reglas de la casa», sino el manejo del dinero y los recursos.</p>")}
{P("Descomponer", "«La <em>hidrografía</em> de la región incluye tres ríos y un lago.» ¿Qué es la hidrografía?", ["El estudio del calor de una región", "La descripción de las aguas de un lugar", "El mapa de las montañas de la región"], 1, {0: "El calor sería <em>termo</em>.", 2: "Ríos y lagos no son montañas."}, "<em>hidro</em> (agua) + <em>grafía</em> (descripción), y el contexto lo confirma.")}"""

    s5 = f"""<p>Una buena definición tiene dos partes: la <strong>categoría</strong> a la que pertenece la palabra y el <strong>rasgo</strong> que la distingue de las demás de esa categoría.</p>
{C.tabla("Definiciones con categoría y rasgo", ["Palabra", "Categoría", "Rasgo que la distingue"],
         [["termómetro", "un instrumento", "que mide la temperatura"], ["herbívoro", "un animal", "que se alimenta de plantas"], ["democracia", "una forma de gobierno", "en la que el pueblo elige a sus gobernantes"]])}
{C.caja("ojo", "Evite la definición en círculo", "<p>«La biología es la ciencia de lo biológico» no explica nada, porque usa la misma palabra. Diga: «La biología es la ciencia que estudia los seres vivos».</p>")}
{C.caja("tip", "Reformular", "<p>Cuando lea una definición del diccionario, dígala con sus palabras sin perder el sentido. El <em>Diccionario de la lengua española</em> de la Real Academia Española es gratuito en línea (dle.rae.es). Si dice «Instrumento óptico que permite observar objetos muy pequeños», usted puede decir: «Aparato para ver cosas que a simple vista no se ven».</p>")}
{P("Definir 1", "¿Cuál es la mejor definición de <em>telescopio</em>?", ["Un aparato telescópico que se usa para mirar.", "Algo que usan los astrónomos de noche en el campo.", "Instrumento para observar objetos que están muy lejos."], 2, {0: "Gira en círculo: repite la palabra.", 1: "Solo dice quién lo usa y cuándo."}, "Categoría (instrumento) y rasgo (para ver lo lejano).")}
{P("Definir 2", "¿Por qué «La psicología es lo que estudian los psicólogos» es una mala definición?", ["Es demasiado corta y sencilla", "Gira en círculo y no explica nada", "Usa una raíz griega y no latina"], 1, {0: "Una definición corta puede ser buena.", 2: "El origen de la raíz no importa."}, "Define la palabra con otra de la misma familia: no dice qué estudia.")}"""

    texto = "".join(f"<p>{p}</p>" for p in TEXTO)
    plano = " ".join(re.sub("<[^>]+>", "", p.replace('<span class="rz-sep" aria-hidden="true">·</span>', "")) for p in TEXTO)
    s6 = f"""<p>Lea el texto y anote en su cuaderno las palabras que tengan raíces de esta lección. Separe cada una en sus piezas. Después pulse <strong>Mostrar las raíces</strong> para comprobarlo.</p>
<p>{LE.escuchar(plano, "Escuchar el texto")} <button type="button" class="btn-sec" id="btn-r22" aria-pressed="false">Mostrar las raíces</button></p>
<div class="articulo lectura-cl" id="lect-22"><p><strong>¿Qué estudia la ecología?</strong></p>{texto}</div>
<script>(function(){{var b=document.getElementById("btn-r22"),t=document.getElementById("lect-22");b.addEventListener("click",function(){{var on=t.classList.toggle("ver-cl");b.setAttribute("aria-pressed",on?"true":"false");b.textContent=on?"Ocultar las raíces":"Mostrar las raíces";}});}})();</script>
<h3>Deduzca el significado</h3>
{P("Ecología 1", "Por sus raíces, un <em>omnívoro</em> es un animal que…", ["come solo carne", "come de todo", "come solo plantas"], 1, {0: "Ese es el carnívoro.", 2: "Ese es el herbívoro."}, "<em>omni</em> (todo) + <em>voro</em> (que come).")}
{P("Ecología 2", "Un <em>microscopio</em> es un instrumento para…", ["medir el tiempo exacto", "oír sonidos lejanos", "ver cosas muy pequeñas"], 2, {0: "Eso es un cronómetro.", 1: "Eso tendría <em>tele</em> y <em>fono</em>."}, "<em>micro</em> (pequeño) + <em>scopio</em> (instrumento para ver).")}
{P("Ecología 3", "La <em>hidrología</em> es…", ["el estudio del agua", "el estudio de la tierra", "el estudio de la vida"], 0, {1: "Esa es la geología.", 2: "Esa es la biología."}, "<em>hidro</em> (agua) + <em>logía</em> (estudio).")}
{P("Ecología 4", "Según el texto, la <em>biodiversidad</em> es…", ["el estudio de los animales que comen plantas", "la variedad de seres vivos de un lugar", "la ciencia que estudia las rocas"], 1, {0: "Busque la explicación después de «es decir».", 2: "Esa es la geología."}, "El texto la define después de «es decir»: <em>bio</em> (vida) + <em>diversidad</em> (variedad).")}
{C.caja("tip", "Si tiene con quién practicar", "<p>Jueguen a «¿qué será?». Uno inventa una palabra con dos raíces de la lección (<em>hidrófono, geoscopio</em>) y el otro adivina qué significaría. Algunas existen de verdad: búsquenlas en el diccionario.</p>")}"""

    secciones = [("s1", "Repaso: las partes de una palabra", s1), ("s2", "Raíces griegas", s2), ("s3", "Raíces latinas", s3), ("s4", "Cómo descomponer una palabra desconocida", s4),
                 ("s5", "Definir con sus palabras", s5), ("s6", "Lectura: «¿Qué estudia la ecología?»", s6)]
    tarea = [("Mi colección de raíces.", "Elija cinco raíces de esta lección y escriba en su cuaderno tres palabras con cada una. Al menos una de las tres debe ser nueva para usted: búsquela en el diccionario."),
             ("Deduzca y compruebe.", "Sin diccionario, escriba qué cree que significan <em>cronograma</em>, <em>acuífero</em> y <em>autodidacta</em>. Después búsquelas y compare."),
             ("Defina con sus palabras", "(categoría + rasgo): <em>telescopio</em>, <em>insecticida</em>, <em>autobiografía</em>. "
              "<details class=\"transc\"><summary>Ver respuestas posibles</summary><p>Cronograma: un plan escrito que dice cuándo se hace cada cosa. Acuífero: una capa de tierra o roca que guarda agua bajo el suelo. Autodidacta: una persona que aprende por su cuenta, sin maestro.</p>"
              "<p>Telescopio: un instrumento para ver objetos que están muy lejos. Insecticida: un producto que mata insectos. Autobiografía: un libro en el que una persona cuenta su propia vida.</p></details>")]
    quiz = [
        ("¿Qué significa la raíz griega <em>bio</em>?", ["vida", "tierra", "agua"], 0, {1: "Esa es <em>geo</em>.", 2: "Esa es <em>hidro</em>."}, "<strong>Vida.</strong>"),
        ("¿Qué significa la raíz <em>logía</em>?", ["estudio, ciencia", "escritura", "medida"], 0, {1: "Esa es <em>grafía</em>.", 2: "Esa es <em>metro</em>."}, "<strong>Estudio, ciencia.</strong>"),
        ("¿Qué palabra tiene una raíz que significa <strong>agua</strong>?", ["acueducto", "autógrafo", "espectador"], 0, {1: "<em>auto</em> y <em>grafo</em>.", 2: "<em>spect</em> es mirar."}, "<strong>Acueducto</strong>: <em>acua</em>."),
        ("¿Qué significa <em>democracia</em> por sus raíces?", ["Gobierno del pueblo", "Estudio de los pueblos", "Escritura del pueblo"], 0, {1: "Eso sería con <em>logía</em>.", 2: "Eso sería <em>demografía</em>."}, "<strong>Gobierno del pueblo.</strong>"),
        ("La raíz latina <em>rupt</em>, de <em>interrumpir</em> y <em>erupción</em>, significa…", ["romper", "llevar", "construir"], 0, {1: "Esa es <em>port</em>.", 2: "Esa es <em>struct</em>."}, "<strong>Romper.</strong>"),
        ("Un <em>cronómetro</em> mide…", ["el tiempo", "la temperatura", "la distancia"], 0, {1: "Eso sería <em>termo</em>.", 2: "No."}, "El <strong>tiempo</strong>."),
        ("Un producto <em>insecticida</em>…", ["mata insectos", "come insectos", "atrae insectos"], 0, {1: "Eso es <em>insectívoro</em>.", 2: "No."}, "<em>cida</em>: que <strong>mata</strong>."),
        ("¿Cuál es la mejor definición de <em>herbívoro</em>?", ["Animal que se alimenta de plantas.", "Un animal que es herbívoro, como la vaca.", "La vaca, el caballo, el venado y la oveja."], 0, {1: "Gira en círculo.", 2: "Solo da ejemplos."}, "Categoría y rasgo."),
        ("Una buena definición tiene…", ["una categoría y un rasgo que distingue", "la misma palabra y un sinónimo", "solo ejemplos de la palabra"], 0, {1: "Sería en círculo.", 2: "Los ejemplos ayudan, pero no definen."}, "<strong>Categoría y rasgo.</strong>"),
        ("Las raíces de una palabra…", ["dan una pista que el contexto confirma", "dicen siempre el significado exacto", "solo sirven para palabras en inglés"], 0, {1: "Recuerde <em>economía</em>.", 2: "Sirven en los dos idiomas."}, "Dan una <strong>pista</strong>."),
    ]
    filas = [
        ("Raíces", "Reconozco las raíces griegas y latinas y su significado.", "Conozco algunas.", "Me cuesta (<a href=\"#s2\">repase las secciones 2 y 3</a>)."),
        ("Descomponer", "Separo, junto los significados y compruebo con el contexto.", "Separo, pero no compruebo.", "No sé por dónde empezar (<a href=\"#s4\">repase la sección 4</a>)."),
        ("Definir", "Defino con categoría y rasgo, sin círculos.", "A veces doy solo ejemplos.", "Repito la misma palabra (<a href=\"#s5\">repase la sección 5</a>)."),
    ]
    cierre = "<p>Ya lee palabras cultas por sus raíces y las define con precisión. En la próxima lección trabajará el <strong>vocabulario académico</strong>: sinónimos, antónimos y relaciones entre palabras.</p>"
    glosario = [("Raíz", "La parte de una palabra que lleva el significado principal."), ("Categoría", "El grupo general al que pertenece algo: un instrumento, un animal, una ciencia."),
                ("Rasgo", "Lo que distingue a algo de los demás de su grupo."), ("Definición en círculo", "La que usa la misma palabra para explicarla y no aclara nada.")]
    conexion = ("<p>En la Lección 1.2 del Nivel 2 leyó palabras nuevas por sus prefijos y sufijos, y en la 5.2, por sus raíces. Hoy lleva esa destreza a las palabras de las ciencias.</p>"
                "<p><strong>Lo que necesita:</strong> su cuaderno y, si puede, el diccionario de la RAE en línea.</p>")
    estd = LE.estandares(["R.4.1"], base=["R.4.2"], fund=["RF.3"])
    return C.pagina_leccion(N, LE.titulo(N), "Leer palabras nuevas por sus piezas.", ["Vocabulario", "Raíces"],
                            ["<strong>Reconocer</strong> raíces griegas y latinas frecuentes.", "<strong>Descomponer</strong> una palabra desconocida y comprobar con el contexto.",
                             "<strong>Definir</strong> con categoría y rasgo, con sus propias palabras."],
                            estd, conexion, secciones, tarea, quiz, filas, cierre, ("2-3", LE.titulo("2-3")), glosario, P)


def practica():
    ra = [{"enun": f'<p class="grande">{r}</p><p>como en <em>{ej}</em> · raíz {o}</p>', "ops": ops, "ok": 0, "pista": "Piense qué tienen en común las dos palabras de ejemplo.",
           "exp": f"<em>{r}</em> significa «{ops[0]}»."} for r, ej, ops, o in RA]
    cn = [{"enun": f'<p class="frase">{d}</p><p>¿Qué palabra es?</p>', "ops": o, "ok": 0, "pista": "¿Qué raíz dice lo principal del significado? Fíjese en las palabras que se parecen.",
           "exp": f"<strong>{o[0]}</strong> · {e}"} for d, o, e in CN]
    rf = [{"enun": f'<p class="grande">{w}</p><p>¿Cuál es la mejor definición?</p>', "ops": o, "ok": 0, "pista": "¿Esa definición dice la categoría y el rasgo? ¿Repite la misma palabra o solo da un ejemplo?",
           "exp": e} for w, o, e in RF]
    mods = [("raices", "¿Qué significa la raíz?", C.om("m1", "Lea la raíz y sus ejemplos, y elija su significado.")),
            ("construya", "Construya la palabra", C.om("m2", "Lea el significado y elija la palabra que se forma con esas raíces.")),
            ("defina", "La mejor definición", C.om("m3", "Elija la definición que tiene categoría y rasgo, sin repetir la palabra."))]
    js = C.js_datos("RA", ra) + C.js_datos("CN", cn) + C.js_datos("RF", rf) + 'creaBanco("m1", RA);\ncreaBanco("m2", CN);\ncreaBanco("m3", RF);\n'
    return C.pagina_practica(N, LE.titulo(N), "Tres actividades · los ejercicios cambian cada vez · dos intentos en cada uno", mods, js)


if __name__ == "__main__":
    LE.construye(N, leccion, practica, horas="Unas 3 horas")
