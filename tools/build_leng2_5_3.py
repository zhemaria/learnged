# -*- coding: utf-8 -*-
"""LearnGED · Artes del lenguaje (español) · Nivel 2 · Lección 5.3 · Significado literal frente a figurado; modismos.
Fuente: clases_leng2/clase_5-3.html (GEDparaHispanos) y gramatica/n2-l5-3.html, adaptadas al marco de LearnGED.
Uso: python3 tools/build_leng2_5_3.py
"""
import os, sys, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import leng_es as LE
from leng_es import C

LE.nivel(2)
N = "5-3"
LF = ["Literal", "Figurado"]
LITFIG = [("Se me partió el corazón al ver a mi hijo llorar.", 1, "Sentir mucha tristeza; el corazón no se parte de verdad."), ("El médico revisó el corazón del paciente.", 0, "Habla del órgano."),
          ("Mi jefe es una fiera cuando se enoja.", 1, "Se comporta con mucha furia; no es un animal."), ("En el zoológico vimos una fiera enorme.", 0, "Un animal salvaje de verdad."),
          ("Estoy muerto de hambre.", 1, "Tener mucha hambre; una exageración."), ("Me comí un plato enorme de arroz con frijoles.", 0, "Pasó de verdad."),
          ("Las palabras de mi madre fueron un bálsamo para mí.", 1, "Me calmaron, como un remedio."), ("La farmacia vende un bálsamo para los labios.", 0, "Un producto de verdad."),
          ("Ese niño es un terremoto: no se queda quieto.", 1, "Es muy inquieto."), ("Anoche hubo un terremoto fuerte en la costa y se cayeron varias casas.", 0, "Un sismo real."),
          ("Le llovieron las críticas después del partido.", 1, "Recibió muchas críticas."), ("Ayer llovió toda la tarde en Chicago.", 0, "Lluvia de verdad."),
          ("Tengo la cabeza llena de ideas para el negocio.", 1, "Se le ocurren muchas ideas."), ("Me duele la cabeza desde la mañana.", 0, "Un dolor real.")]
MODISMOS = [("tomar el pelo", "No le crea: le está tomando el pelo.", ["Engañar a alguien en broma", "Cortarle el pelo a alguien", "Saludar a alguien con cariño"]),
            ("buscarle tres pies al gato", "No le busque tres pies al gato: el problema es sencillo.", ["Complicar algo que es simple", "Buscar a un animal perdido", "Ahorrar dinero poco a poco"]),
            ("estar entre la espada y la pared", "Estoy entre la espada y la pared: si renuncio no tengo dinero, y si me quedo no tengo tiempo.", ["Tener que elegir entre dos opciones malas", "Estar en un peligro real de muerte", "Estar muy tranquilo y sin problemas"]),
            ("ser uña y carne", "Mi hija y su prima son uña y carne.", ["Ser muy amigos, inseparables", "Pelear todo el tiempo", "Parecerse mucho físicamente"]),
            ("no pegar ojo", "Con el ruido de la fiesta no pegué ojo en toda la noche.", ["No poder dormir", "No ver bien", "No querer mirar"]),
            ("dar la lata", "El niño estuvo dando la lata toda la tarde para que le compraran un helado.", ["Molestar insistiendo", "Regalar algo a alguien", "Hacer ruido con una lata"]),
            ("ir al grano", "No tengo mucho tiempo, así que voy al grano.", ["Decir lo importante sin rodeos", "Ir al campo a sembrar maíz", "Comer cereal en el desayuno"]),
            ("estar en las nubes", "Está en las nubes: le pregunté tres veces y no contestó.", ["Estar distraído", "Estar muy contento", "Viajar en avión"]),
            ("ponerse las pilas", "Si quiere el ascenso, tiene que ponerse las pilas.", ["Esforzarse más", "Cambiar las baterías", "Ponerse un abrigo"]),
            ("dar en el clavo", "Con su idea dio en el clavo: eso era lo que faltaba.", ["Acertar", "Lastimarse un dedo", "Arreglar un mueble"]),
            ("quedarse en blanco", "En la entrevista me quedé en blanco y no supe qué decir.", ["Olvidar todo de repente", "Ponerse pálido de frío", "Vestirse de color blanco"]),
            ("estar hecho polvo", "Después de mudarnos, estoy hecho polvo.", ["Estar muy cansado", "Estar muy sucio", "Tener mucha alergia"]),
            ("no tener pelos en la lengua", "Mi abuela no tiene pelos en la lengua: dice todo lo que piensa.", ["Hablar con franqueza", "Hablar muy poco", "Tener la lengua lastimada"]),
            ("consultar con la almohada", "Antes de aceptar el trabajo, lo voy a consultar con la almohada.", ["Pensarlo con calma antes de decidir", "Dormir muchas horas seguidas", "Pedir consejo a un médico de confianza"]),
            ("tirar la toalla", "Después de tres intentos, no tiró la toalla y aprobó.", ["Rendirse", "Lavar la ropa", "Enojarse"]),
            ("costar un ojo de la cara", "Arreglar el techo nos costó un ojo de la cara.", ["Ser muy caro", "Ser peligroso", "Ser muy difícil"])]
SITU = [("Su hermano habla sin parar durante toda la cena.", "Mi hermano habla ___.", ["hasta por los codos", "como pez en el agua", "en las nubes"]),
        ("Usted ayuda a su vecina a cargar las bolsas del mercado.", "Le ___ a mi vecina.", ["eché una mano", "tomé el pelo", "di la lata"]),
        ("Se equivocó y le dio a su jefe el informe de otro cliente.", "¡___!", ["Metí la pata", "Di en el clavo", "Fue pan comido"]),
        ("La tormenta no deja de echar agua desde la mañana.", "Está ___.", ["lloviendo a cántaros", "dando la lata", "yendo al grano"]),
        ("El examen de manejo fue facilísimo.", "El examen fue ___.", ["pan comido", "un ojo de la cara", "una fiera"]),
        ("Su amigo quiere dejar el curso cuando ya casi termina.", "No ___.", ["tires la toalla", "pegues ojo", "metas la pata"]),
        ("Su compañera explica en un minuto lo esencial, sin rodeos.", "Mi compañera ___.", ["fue al grano", "buscó tres pies al gato", "se quedó en blanco"]),
        ("Su primo le hace creer, en broma, que ganó la lotería.", "Mi primo me ___.", ["tomó el pelo", "echó una mano", "dio en el clavo"]),
        ("Tiene que decidir hoy si acepta un trabajo, pero prefiere pensarlo.", "Lo voy a ___.", ["consultar con la almohada", "tirar la toalla", "meter la pata"]),
        ("Dos hermanas siempre están juntas y se lo cuentan todo.", "Son ___.", ["uña y carne", "hechas polvo", "pan comido"]),
        ("El bebé lloró toda la noche y usted no durmió nada.", "No ___ en toda la noche.", ["pegué ojo", "eché una mano", "di en el clavo"]),
        ("Su hijo encuentra la causa exacta de una gotera.", "¡___!", ["Diste en el clavo", "Estás en las nubes", "Metiste la pata"])]
QUINCE = [("Costar un ojo de la cara", "Ser muy caro.", "Ese teléfono me costó un ojo de la cara."), ("Estar en las nubes", "Estar distraído, sin prestar atención.", "Hoy estás en las nubes: no oíste nada de lo que te dije."),
          ("Meter la pata", "Equivocarse, cometer un error.", "Metí la pata: llamé a la señora por otro nombre."), ("Echar una mano", "Ayudar.", "¿Me echas una mano con estas cajas?"),
          ("Ser pan comido", "Ser muy fácil.", "Con tanta práctica, el examen fue pan comido."), ("Quedarse en blanco", "Olvidar todo de repente.", "Me puse nervioso y me quedé en blanco."),
          ("Dar en el clavo", "Acertar, encontrar la respuesta exacta.", "Diste en el clavo: ese era el problema."), ("No tener pelos en la lengua", "Decir lo que se piensa, sin miedo.", "Mi tía no tiene pelos en la lengua."),
          ("Ponerse las pilas", "Esforzarse, ponerse activo.", "Si quieres aprobar, tienes que ponerte las pilas."), ("Hablar hasta por los codos", "Hablar muchísimo.", "Mi vecina habla hasta por los codos."),
          ("Llover a cántaros", "Llover muchísimo.", "Ayer llovió a cántaros y se inundó la calle."), ("Estar como pez en el agua", "Sentirse muy cómodo en un lugar.", "En la cocina, mi abuelo está como pez en el agua."),
          ("Tirar la toalla", "Rendirse, abandonar un esfuerzo.", "No tires la toalla: ya te falta poco."), ("Estar hecho polvo", "Estar muy cansado.", "Después del turno doble, estoy hecho polvo."),
          ("Consultarlo con la almohada", "Pensar algo con calma antes de decidir.", "No te respondo hoy: lo consulto con la almohada.")]
SEMANA = ["La semana pasada fue terrible para Carlos. El lunes [llovía a cántaros] y llegó empapado al trabajo. El martes [metió la pata]: envió un correo importante a la persona equivocada.",
          "El miércoles tenía su examen de matemáticas del GED. Había estudiado mucho, pero al ver la primera pregunta [se quedó en blanco]. Respiró hondo, leyó otra vez con calma y poco a poco recordó todo. Al final, el examen resultó [pan comido].",
          "El jueves, su hermana le pidió que la ayudara con la mudanza. Aunque [estaba hecho polvo], le [echó una mano] toda la tarde.",
          "El viernes, por fin, le dieron una buena noticia: había aprobado. Su madre, que [habla hasta por los codos], llamó a toda la familia para contarlo. Carlos sonrió: después de una semana así, estaba decidido a no [tirar la toalla] nunca."]


def plano(t): return t.replace("[", "").replace("]", "")
def marca(t): return re.sub(r"\[([^\]]+)\]", r'<mark class="mod">\1</mark>', t)


def leccion():
    P = C.Practicas()
    s1 = f"""<p>Si alguien le dice «ese carro me costó un ojo de la cara», no se preocupe por su vista: quiere decir que el carro fue muy caro. Usamos expresiones así todos los días sin pensarlo, y las entendemos porque las conocemos desde niños. Pero en un texto escrito, sobre todo si la expresión es nueva o de otro país, pueden confundir.</p>
{C.tabla("Sentido literal y sentido figurado", ["Sentido", "Qué significa", "Ejemplo"],
         [["Literal", "Las palabras significan exactamente lo que dicen.", "«La pulsera es de oro.»"], ["Figurado", "Las palabras significan otra cosa, por comparación o por costumbre.", "«Mi abuela tiene un corazón de oro.» = es muy buena."]])}
<p>Muchas palabras cotidianas tienen un uso figurado: <em>el pie de la montaña</em> (la parte de abajo), <em>una lluvia de preguntas</em> (muchas preguntas), <em>tener la cabeza dura</em> (ser terco).</p>
{C.caja("tip", "Cómo darse cuenta", "<p>Imagine la frase al pie de la letra. Si lo que imagina es imposible, absurdo o exagerado (una persona con un corazón hecho de metal), la frase es figurada.</p>")}
{P("¿Literal o figurado? 1", "«Hay una <strong>fiebre</strong> por las bicicletas eléctricas: todos quieren una.»", LF, 1, {0: "Las bicicletas no se enferman."}, "<strong>Figurado</strong>: significa una moda muy fuerte.")}
{P("¿Literal o figurado? 2", "«Mi hijo tiene <strong>fiebre</strong> y le duele la garganta.»", LF, 0, {1: "Habla de una fiebre de verdad."}, "<strong>Literal.</strong>")}
{P("¿Literal o figurado? 3", "«La paciencia es la <strong>llave</strong> del éxito.»", LF, 1, {0: "La paciencia no abre puertas de verdad."}, "<strong>Figurado</strong>: lo que permite conseguir algo.")}
{P("¿Literal o figurado? 4", "«Ese hombre es <strong>una roca</strong>: nunca se rinde.»", LF, 1, {0: "Un hombre no es una piedra."}, "<strong>Figurado</strong>: es fuerte y firme.")}"""

    s2 = f"""<p>Un <strong>modismo</strong> es una expresión de varias palabras cuyo significado no se puede deducir de las palabras sueltas. Hay que conocerlo, como se conoce una palabra.</p>
<ul><li><em>Meter la pata</em> no tiene que ver con patas: significa <strong>equivocarse</strong>.</li><li><em>Echar una mano</em> no es lanzar nada: es <strong>ayudar</strong>.</li>
<li><em>Ser pan comido</em> no habla de pan: significa <strong>ser muy fácil</strong>.</li></ul>
{C.caja("ojo", "Los modismos y el registro", "<p>La mayoría son del registro informal (Lección 3.3). Están muy bien en una conversación o un cuento, pero en un texto formal o en la respuesta extendida del GED conviene decirlo de manera directa: en lugar de «metí la pata», escriba «cometí un error».</p>")}
<h3>Quince modismos para conocer</h3>
<p>Estos modismos se entienden en casi todos los países de habla hispana. Piense qué significa cada uno y ábralo para comprobar. Los ejemplos van con «tú», como se dicen en la conversación.</p>
<div class="tarjetas-mod">{"".join(f'<details class="tarjeta-mod"><summary>{m}</summary><p><strong>Significa:</strong> {s}</p><p><em>«{e}»</em> {LE.escuchar(e, "Escuchar")}</p></details>' for m, s, e in QUINCE)}</div>"""

    s3 = f"""<p>La misma frase puede ser literal o figurada según el contexto. Por eso, como en la Lección 5.2, hay que mirar alrededor:</p>
{C.tabla("El contexto decide", ["Literal", "Figurado"],
         [["«Los pescadores rompieron el hielo del lago para pescar.»", "«Para <strong>romper el hielo</strong>, la maestra contó un chiste el primer día.» = quitar la tensión e iniciar la conversación."],
          ["«Lávese bien las manos antes de cocinar.»", "«El gerente <strong>se lavó las manos</strong>: dijo que el problema no era suyo.» = no quiso hacerse responsable."]], fila_th=False)}
{P("Compruebe", "Su compañero está a punto de dejar sus estudios. ¿Qué le dice?", ["«No tires la toalla.»", "«Estás en las nubes.»", "«Diste en el clavo.»"], 0, {1: "Eso es decirle que está distraído.", 2: "Eso es decirle que acertó."}, "<strong>No tires la toalla</strong>: no te rindas.")}
<h3>Lectura: «Una semana para olvidar»</h3>
<p>Lea el texto como un «cazador de modismos». En su cuaderno, copie cada expresión figurada que encuentre y escriba al lado lo que significa. <strong>Hay ocho.</strong> Después compruebe y responda las preguntas.</p>
{LE.escuchar(" ".join(plano(p) for p in SEMANA), "Escuchar el texto")}
<div class="texto-lectura" id="texto-semana">{"".join(f"<p>{plano(p)}</p>" for p in SEMANA)}</div>
<details class="caja caja-tip"><summary><strong>Mostrar las ocho expresiones</strong></summary><div class="texto-lectura">{"".join(f"<p>{marca(p)}</p>" for p in SEMANA)}</div>
<p><em>llover a cántaros</em> (llover muchísimo) · <em>meter la pata</em> (equivocarse) · <em>quedarse en blanco</em> (olvidar todo de repente) · <em>pan comido</em> (muy fácil) · <em>estar hecho polvo</em> (muy cansado) · <em>echar una mano</em> (ayudar) · <em>hablar hasta por los codos</em> (hablar muchísimo) · <em>tirar la toalla</em> (rendirse).</p></details>
{P("Pregunta 1", "¿Qué le pasó a Carlos el martes?", ["Se lastimó el pie", "Cometió un error", "Perdió el autobús"], 1, {0: "No es literal.", 2: "El texto no lo dice."}, "<em>Meter la pata</em>: envió el correo a la persona equivocada.")}
{P("Pregunta 2", "Cuando Carlos <em>se quedó en blanco</em>…", ["olvidó todo por un momento", "se manchó la ropa de blanco", "terminó el examen muy rápido"], 0, {1: "No es literal.", 2: "Ocurrió al ver la primera pregunta."}, "Por los nervios no recordaba nada; luego se calmó.")}
{P("Pregunta 3", "¿Por qué ayudar a su hermana tiene mérito?", ["Porque estaba muy cansado y aun así la ayudó", "Porque no sabía cargar cajas pesadas", "Porque su hermana no le pidió ayuda"], 0, {1: "El texto no lo dice.", 2: "Ella sí se lo pidió."}, "<em>Hecho polvo</em> = muy cansado; <em>echar una mano</em> = ayudar.")}
{P("Pregunta 4", "¿Qué decide Carlos al final?", ["Dejar de estudiar", "No rendirse nunca", "Cambiar de trabajo"], 1, {0: "Es lo contrario.", 2: "El texto no lo dice."}, "<em>No tirar la toalla</em>: no rendirse.")}
<div class="caja caja-tip"><span class="etiqueta et-verde">Actividad · los modismos de su país</span>
<p>Cada país tiene sus propios modismos, y algunos significan cosas distintas de un lugar a otro. Escriba cinco modismos que se usan en su país o en su familia. Para cada uno, anote qué significa, una oración de ejemplo y cómo lo diría en un texto formal, sin el modismo.</p>
<p>Si tiene con quién practicar, pregúnteles a sus padres, abuelos o vecinos de otros países qué modismos usan. Le sorprenderá cuántos son distintos… y cuántos coinciden.</p></div>"""

    secciones = [("s1", "Literal y figurado", s1), ("s2", "Los modismos", s2), ("s3", "El contexto decide", s3)]
    tarea = [("Mi historia con modismos.", "Escriba un párrafo de 6 a 8 oraciones sobre algo que le pasó, usando al menos cuatro modismos de la lección."),
             ("De figurado a directo.", "Reescriba su párrafo en registro formal, sin modismos."),
             ("Cazador de modismos.", "Mire un programa de televisión en español o escuche una canción, y anote tres expresiones figuradas con su significado.")]
    quiz = [
        ("Una expresión tiene <strong>sentido figurado</strong> cuando…", ["significa otra cosa distinta de lo que dicen sus palabras", "significa exactamente lo que dicen sus palabras", "está escrita en otro idioma distinto del español"], 0, {1: "Eso es literal.", 2: "No tiene que ver con el idioma."}, "Significa <strong>otra cosa</strong>."),
        ("«Mi abuela tiene un corazón de oro.» ¿Qué quiere decir?", ["Que es muy buena persona", "Que tiene un problema en el corazón", "Que tiene mucho dinero guardado"], 0, {1: "No es literal.", 2: "No habla de dinero."}, "Que es <strong>muy buena</strong>."),
        ("¿Cuál de estas oraciones es <strong>literal</strong>?", ["El anillo es de oro.", "Tiene un corazón de oro.", "Es una oportunidad de oro."], 0, {1: "Es figurada.", 2: "Es figurada."}, "<strong>El anillo es de oro.</strong>"),
        ("Un <strong>modismo</strong> es…", ["una expresión cuyo significado no sale de sus palabras sueltas", "una palabra muy larga y difícil de escribir", "una palabra que siempre se escribe con tilde"], 0, {1: "No depende del largo.", 2: "No tiene que ver con la tilde."}, "Una expresión que <strong>hay que conocer</strong>."),
        ("«Ese viaje me costó un ojo de la cara.» Significa que el viaje…", ["fue muy caro", "fue peligroso", "le dañó la vista"], 0, {1: "No habla de peligro.", 2: "No es literal."}, "Fue <strong>muy caro</strong>."),
        ("¿Qué significa <em>echar una mano</em>?", ["Ayudar", "Saludar", "Pelear"], 0, {1: "No es saludar.", 2: "Es lo contrario."}, "<strong>Ayudar.</strong>"),
        ("Si un trabajo es <em>pan comido</em>, es…", ["muy fácil", "muy pesado", "de panadería"], 0, {1: "Es lo contrario.", 2: "No es literal."}, "<strong>Muy fácil.</strong>"),
        ("«En la fiesta, mi hija estaba como pez en el agua.» Significa que…", ["se sentía muy cómoda", "tenía mucha sed", "nadó en la piscina"], 0, {1: "No es literal.", 2: "No es literal."}, "Se sentía <strong>cómoda</strong>."),
        ("¿Cómo se diría «me quedé en blanco» en un texto formal?", ["Olvidé lo que iba a decir.", "Me quedé blanquísimo.", "Me pinté de blanco."], 0, {1: "Sigue siendo figurado.", 2: "Es literal y cambia el sentido."}, "<strong>Olvidé lo que iba a decir.</strong>"),
        ("¿Qué decide si una frase es literal o figurada?", ["El contexto en que aparece", "La longitud de la frase", "El número de palabras con tilde"], 0, {1: "El largo no importa.", 2: "La tilde no importa."}, "El <strong>contexto</strong>."),
    ]
    filas = [
        ("Literal y figurado", "Distingo el sentido literal del figurado con la prueba «al pie de la letra».", "Lo distingo en los casos claros.", "Leo todo al pie de la letra (<a href=\"#s1\">repase la sección 1</a>)."),
        ("Modismos", "Conozco los quince modismos y los reemplazo en un texto formal.", "Conozco algunos.", "No los entiendo (<a href=\"#s2\">repase la sección 2</a>)."),
        ("Contexto", "Uso el contexto para decidir el sentido de una frase.", "A veces dudo.", "No miro el contexto (<a href=\"#s3\">repase la sección 3</a>)."),
    ]
    cierre = "<p>Con esta lección termina el Tema 5. Ya compara textos y descubre el significado de palabras y expresiones. En el Tema 6 leerá <strong>gráficas, tablas y fuentes</strong>.</p>"
    glosario = [("Sentido literal", "Lo que las palabras dicen exactamente."), ("Sentido figurado", "Otro significado, por comparación o por costumbre."),
                ("Modismo", "Expresión fija cuyo significado no sale de sus palabras sueltas."), ("Al pie de la letra", "Entendido de manera literal, palabra por palabra.")]
    conexion = ("<p>En la Lección 5.2 descubrió el significado de palabras sueltas por el contexto. Hoy hará lo mismo con expresiones enteras que no dicen lo que sus palabras dicen.</p>"
                "<p><strong>Lo que necesita:</strong> el cuaderno.</p>")
    estd = LE.estandares(["R.4.1", "R.4.3"], base=["L.1.4"])
    return C.pagina_leccion(N, LE.titulo(N), "Cuando las palabras dicen más de lo que dicen.", ["Vocabulario", "Lenguaje figurado"],
                            ["<strong>Distinguir</strong> el sentido literal del figurado.", "<strong>Reconocer</strong> y entender modismos comunes.",
                             "<strong>Usar</strong> el contexto para decidir el sentido.", "<strong>Reemplazar</strong> un modismo en un texto formal."],
                            estd, conexion, secciones, tarea, quiz, filas, cierre, ("6-1", LE.titulo("6-1")), glosario, P)


def practica():
    lf = [{"enun": f"<span class=\"grande\">«{o}»</span><br>¿Literal o figurado?", "ops": LF, "ok": k, "enOrden": True,
           "pista": "Imagínelo al pie de la letra: ¿podría pasar de verdad?", "exp": f"<strong>{LF[k]}</strong>. {e}"} for o, k, e in LITFIG]
    mo = [{"enun": f"<span class=\"grande\">{m}</span><div class=\"texto-lectura\"><p>«{e}»</p></div><strong>¿Qué significa?</strong>", "ops": ops, "ok": 0,
           "pista": "No lo lea al pie de la letra: ¿qué quiere decir la persona en el ejemplo?", "exp": f"«{m}»: {ops[0][0].lower() + ops[0][1:]}."} for m, e, ops in MODISMOS]
    ct = [{"enun": f"<p>{s}</p><span class=\"grande\">{f.replace('___', '_____')}</span>", "ops": ops, "ok": 0,
           "pista": "Piense qué significa cada expresión y cuál describe la situación.", "exp": f"«{f.replace('___', ops[0])}»"} for s, f, ops in SITU]
    mods = [("literal", "¿Literal o figurado?", C.om("m1", "Decida si la oración se entiende al pie de la letra o tiene otro sentido.")),
            ("modismos", "¿Qué significa el modismo?", C.om("m2", "Lea el modismo y su ejemplo, y elija su significado.")),
            ("situaciones", "¿Qué expresión va mejor?", C.om("m3", "Elija la expresión que corresponde a la situación."))]
    js = C.js_datos("LF", lf) + C.js_datos("MO", mo) + C.js_datos("CT", ct) + 'creaBanco("m1", LF);\ncreaBanco("m2", MO);\ncreaBanco("m3", CT);\n'
    return C.pagina_practica(N, LE.titulo(N), "Tres actividades · los ejercicios cambian cada vez · dos intentos en cada uno", mods, js)


if __name__ == "__main__":
    LE.construye(N, leccion, practica, horas="Unas 3 horas")
