# -*- coding: utf-8 -*-
"""LearnGED · Artes del lenguaje (español) · Nivel 2 · Lección 3.2 · La tilde y la ortografía convencional.
Fuente: clases_leng2/clase_3-2.html (GEDparaHispanos) y gramatica/n2-l3-2.html, adaptadas al marco de LearnGED.
Uso: python3 tools/build_leng2_3_2.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import leng_es as LE
from leng_es import C

LE.nivel(2)
N = "3-2"
TIPOS = ["aguda", "llana", "esdrújula"]
TONICA = [("ca-mión", 1), ("ár-bol", 0), ("mú-si-ca", 0), ("ven-ta-na", 1), ("re-loj", 1), ("te-lé-fo-no", 1), ("tra-ba-jar", 2), ("e-xa-men", 1),
          ("ciu-dad", 1), ("sá-ba-do", 0), ("lá-piz", 0), ("ca-mi-se-ta", 2), ("com-pu-ta-do-ra", 3), ("pá-ja-ro", 0), ("co-ra-zón", 2), ("ma-ña-na", 1),
          ("in-glés", 1), ("mé-di-co", 0)]
TILDE = [("canción", "cancion", "Aguda terminada en <em>n</em>: con tilde."), ("papel", "papél", "Aguda terminada en <em>l</em>: sin tilde."),
         ("árbol", "arbol", "Llana terminada en <em>l</em>: con tilde."), ("examen", "exámen", "Llana terminada en <em>n</em>: sin tilde."),
         ("música", "musica", "Esdrújula: siempre con tilde."), ("ciudad", "ciudád", "Aguda terminada en <em>d</em>: sin tilde."),
         ("fácil", "facil", "Llana terminada en <em>l</em>: con tilde."), ("camiones", "camiónes", "Llana terminada en <em>s</em>: sin tilde."),
         ("sofá", "sofa", "Aguda terminada en vocal: con tilde."), ("comer", "comér", "Aguda terminada en <em>r</em>: sin tilde."),
         ("lápiz", "lapiz", "Llana terminada en <em>z</em>: con tilde."), ("joven", "jóven", "Llana terminada en <em>n</em>: sin tilde."),
         ("médico", "medico", "Esdrújula: siempre con tilde."), ("café", "cafe", "Aguda terminada en vocal: con tilde."),
         ("azúcar", "azucar", "Llana terminada en <em>r</em>: con tilde."), ("nación", "nacion", "Aguda terminada en <em>n</em>: con tilde."),
         ("naciones", "naciónes", "Llana terminada en <em>s</em>: sin tilde."), ("difícil", "dificil", "Llana terminada en <em>l</em>: con tilde."),
         ("autobús", "autobus", "Aguda terminada en <em>s</em>: con tilde."), ("crisis", "crísis", "Llana terminada en <em>s</em>: sin tilde."),
         ("fue", "fué", "Una sola sílaba: sin tilde."), ("día", "dia", "Hiato: la <em>í</em> fuerte lleva tilde.")]
LETRAS = [("Cuando era joven, ___ en una panadería.", ["trabajaba", "trabajava"], "Pasado en <em>-aba</em>: <em>b</em>."),
          ("Mi ___ trabaja en la construcción.", ["hombre", "honbre"], "Antes de <em>b</em> va <em>m</em>: <em>mb</em>."),
          ("Le voy a ___ la foto por mensaje.", ["enviar", "embiar"], "Después de <em>n</em>: <em>v</em>."),
          ("No quiero ___ la cita.", ["olvidar", "olbidar"], "Después de <em>ol</em>: <em>v</em>."),
          ("Mi hija es muy ___.", ["activa", "actiba"], "Termina en <em>-iva</em>: <em>v</em>."),
          ("Voy a ___ una carta a mi madre.", ["escribir", "escrivir"], "Verbo en <em>-bir</em>: <em>b</em>."),
          ("Hoy es un día ___.", ["feliz", "felis"], "De la familia de <em>felicidad</em>: <em>z</em> al final."),
          ("Los niños están muy ___.", ["felices", "felizes"], "La <em>z</em> pasa a <em>c</em> delante de <em>e</em>."),
          ("Me compré unos ___ negros.", ["zapatos", "sapatos"], "<em>za</em>, con <em>z</em>."),
          ("Recibí un ___ de mi jefe.", ["mensaje", "mensage"], "Termina en <em>-aje</em>: <em>j</em>."),
          ("Tiene que ___ entre las dos opciones.", ["elegir", "elejir"], "Verbo en <em>-gir</em>: <em>g</em>."),
          ("Esa ___ es muy bonita.", ["imagen", "imajen"], "Termina en <em>-gen</em>: <em>g</em>."),
          ("La ___ me dio el cambio.", ["cajera", "cagera"], "Termina en <em>-jera</em>: <em>j</em>."),
          ("___ mucho tráfico en la autopista.", ["Hay", "Ay"], "Del verbo <em>haber</em>: <em>hay</em>."),
          ("Ponga las bolsas ___, junto a la puerta.", ["ahí", "hay"], "Es un lugar: <em>ahí</em>."),
          ("Ya he ___ la cena.", ["hecho", "echo"], "Del verbo <em>hacer</em>: <em>hecho</em>."),
          ("Siempre le ___ limón a la sopa.", ["echo", "hecho"], "Del verbo <em>echar</em>: <em>echo</em>."),
          ("Esta ___ sí llegué a tiempo.", ["vez", "ves"], "Una ocasión: <em>vez</em>."),
          ("Vamos ___ qué dice el doctor.", ["a ver", "haber"], "«Mirar, comprobar»: <em>a ver</em>."),
          ("Para el desayuno, compré una docena de ___.", ["huevos", "uevos"], "Empieza por <em>hue-</em>: con <em>h</em>."),
          ("El ___ del incendio llegó hasta mi calle.", ["humo", "umo"], "Empieza por <em>hum-</em>: con <em>h</em>.")]
FRASES = ["El autobús llegó tarde porque había mucho tráfico.", "Mi hijo escribió una canción para su abuela.", "Hay que llevar el lápiz y el cuaderno a la clase.",
          "Ayer trabajaba en la fábrica cuando sonó el teléfono.", "¿Dónde dejaste las llaves del carro?", "En invierno hace mucho frío en Chicago.",
          "La médica me dio una receta para la tos.", "Tú tienes razón: el examen fue difícil.", "Mañana voy a enviar el mensaje a mi jefe.",
          "Mis vecinos están felices con el huerto nuevo.", "Ya he hecho la tarea de esta semana.", "Si llueve, nos quedamos en casa a ver una película."]
PALABRAS = ["camión", "árbol", "música", "reloj", "examen", "teléfono", "invierno", "trabajaba", "lápices", "viaje", "hielo", "país"]


def tipo(pal, k):
    n = len(pal.split("-"))
    return TIPOS[n - 1 - k] if n - 1 - k < 3 else "sobresdrújula"


def leccion():
    P = C.Practicas()
    s1 = f"""<p>En español casi todo se escribe como suena. Casi. La tilde y algunas letras son la excepción, y son también los errores que más se notan en una carta, un correo de trabajo o la respuesta escrita del GED. La buena noticia es que la tilde sigue reglas fijas: si sabe qué sílaba suena más fuerte, sabe si lleva tilde.</p>
<p>En cada palabra hay una sílaba que se pronuncia con más fuerza: la <strong>sílaba tónica</strong>. Para encontrarla, diga la palabra en voz alta como si llamara a alguien de lejos: ca-<strong>MIÓN</strong>, <strong>ÁR</strong>-bol, <strong>MÚ</strong>-si-ca.</p>
{C.tabla("Las palabras según la sílaba tónica", ["Tipo", "La sílaba tónica es…", "Ejemplos"],
         [["Aguda", "la última", "ca-<strong>fé</strong> · re-<strong>loj</strong> · ciu-<strong>dad</strong> · can-<strong>ción</strong>"],
          ["Llana (o grave)", "la penúltima", "<strong>ca</strong>-sa · <strong>ár</strong>-bol · e-<strong>xa</strong>-men · <strong>lá</strong>-piz"],
          ["Esdrújula", "la antepenúltima", "<strong>mú</strong>-si-ca · <strong>sá</strong>-ba-do · te-<strong>lé</strong>-fo-no"]])}
{C.caja("tip", "Un truco", "<p>Si duda, diga la palabra con la fuerza en otra sílaba. Suena raro: «CA-fe», «mu-SI-ca». La versión que suena bien le dice dónde está la fuerza.</p>")}
{P("Compruebe", "<strong>ven-ta-na</strong> es una palabra…", TIPOS, 1, {0: "La fuerza no está en la última sílaba.", 2: "Tiene solo tres sílabas y la fuerza está en ta."}, "<strong>Llana</strong>: ven-<strong>TA</strong>-na.")}"""

    s2 = f"""{C.tabla("Reglas generales de la tilde", ["Tipo", "Lleva tilde cuando…", "Con tilde", "Sin tilde"],
         [["Aguda", "termina en <strong>n, s</strong> o <strong>vocal</strong>", "canción · compás · café · sofá", "reloj · papel · ciudad · comer"],
          ["Llana", "<strong>no</strong> termina en n, s ni vocal", "árbol · lápiz · fácil · azúcar", "casa · examen · lunes · joven"],
          ["Esdrújula", "<strong>siempre</strong>", "música · sábado · teléfono · médico", "—"]])}
{C.caja("tip", "Reglas opuestas", "<p>Lo que hace llevar tilde a una aguda (n, s, vocal) es justo lo que hace que una llana no la lleve. Por eso <em>canción</em> lleva tilde y <em>examen</em> no.</p>")}
<p>Dos casos más que ya conoce:</p>
<ul><li>Las palabras de <strong>una sola sílaba</strong> no llevan tilde: <em>fue, fui, dio, vio, pie, tren, mes</em>. (La excepción son las de la sección 3).</li>
<li>El <strong>hiato</strong> de la Lección 1.1: la <em>í</em> o la <em>ú</em> fuerte junto a otra vocal llevan tilde aunque la regla no lo pida: <em>día, país, baúl, maíz</em>.</li></ul>
{P("Compruebe", "¿Cómo se escribe?", ["examen", "exámen"], 0, {1: "Es llana y termina en n: no lleva tilde."}, "<strong>examen</strong>: llana terminada en n, sin tilde.")}
{P("Compruebe", "¿Cómo se escribe?", ["arbol", "árbol"], 1, {0: "Es llana y termina en l: lleva tilde."}, "<strong>árbol</strong>: llana terminada en l, con tilde.")}"""

    s3 = f"""<p>Algunas palabras de una sílaba se escriben igual pero significan cosas distintas. La tilde sirve para distinguirlas: es la <strong>tilde diacrítica</strong>.</p>
{C.tabla("Palabras que cambian de significado con la tilde", ["Con tilde", "Sin tilde"],
         [["<strong>tú</strong> (la persona): Tú tienes razón.", "<strong>tu</strong> (de ti): Tu casa es bonita."], ["<strong>él</strong> (la persona): Él trabaja aquí.", "<strong>el</strong> (artículo): El trabajo es duro."],
          ["<strong>mí</strong> (la persona): Es para mí.", "<strong>mi</strong> (de mí): Mi hijo estudia."], ["<strong>sí</strong> (afirmación): Sí, quiero.", "<strong>si</strong> (condición): Si llueve, no voy."],
          ["<strong>sé</strong> (de saber): No sé nada.", "<strong>se</strong> (pronombre): Se levanta temprano."], ["<strong>té</strong> (la bebida): Me gusta el té.", "<strong>te</strong> (pronombre): Te llamo luego."],
          ["<strong>más</strong> (cantidad): Quiero más arroz.", "—"]])}
{C.caja("tip", "Las palabras de pregunta", "<p><em>qué, cómo, dónde, cuándo, quién, cuánto</em> llevan tilde cuando preguntan o exclaman, aunque no haya signos: <em>¿Dónde vive? · No sé dónde vive. · ¡Qué bonito!</em> Sin pregunta, no: <em>La casa donde vivo es pequeña. · Creo que sí.</em></p>")}
{P("Compruebe", "Es para ___.", ["mi", "mí"], 1, {0: "Aquí es la persona, no «de mí»."}, "<strong>mí</strong>: la persona.")}
{P("Compruebe", "No sé ___ vive.", ["donde", "dónde"], 1, {0: "Hay una pregunta escondida: ¿dónde vive?"}, "<strong>dónde</strong>: pregunta indirecta.")}"""

    s4 = f"""<p>En el español de América, la <strong>b</strong> y la <strong>v</strong> suenan igual, y también la <strong>s</strong>, la <strong>z</strong> y la <strong>c</strong> delante de e o i. Por eso hay que aprender cómo se escriben. Estas reglas funcionan casi siempre:</p>
{C.tabla("Reglas para letras que suenan igual", ["Se escribe…", "Cuándo", "Ejemplos"],
         [["b", "antes de otra consonante · después de m · en el pasado en -aba · en los verbos en -bir", "blanco, brazo · hombre, cambio · trabajaba · escribir, recibir (excepto hervir, servir, vivir)"],
          ["v", "después de n · después de ol · en las palabras en -ivo, -iva", "invierno, enviar · olvidar, polvo · activo, positiva"],
          ["z / c", "za, zo, zu, pero ce, ci: la z pasa a c en el plural y en la familia", "zapato, azul · cena, cielo · lápiz → lápices · feliz → felicidad"],
          ["s o c", "se aprende por la familia de la palabra", "casa → casita · educar → educación · confuso → confusión"],
          ["g", "en las palabras con -gen · en los verbos en -ger y -gir", "imagen, origen · proteger, elegir (excepto tejer, crujir)"],
          ["j", "en las palabras en -aje y -jero, -jera", "viaje, mensaje, garaje · extranjero, cajera"],
          ["h", "no suena: hay que conocer las palabras. La llevan las que empiezan con hie-, hue- y hum-, y todas las formas de haber y hacer", "hielo, huevo, humo · hay, había, hubo · hago, hizo, hecho"]])}
{C.caja("tip", "La familia ayuda", "<p>Si duda cómo se escribe una palabra, piense en otra de su familia. ¿<em>Lapices</em> o <em>lápices</em>? Viene de <em>lápiz</em>, y como la z no va delante de e, se escribe con c: <em>lápices</em>.</p>")}
<h3>Pares que se confunden</h3>
{C.tabla("Palabras que suenan igual y se escriben distinto", ["Palabra", "Significa", "Ejemplo"],
         [["hay", "del verbo haber: existe", "Hay leche en el refrigerador."], ["ahí", "en ese lugar", "Deje la caja ahí."], ["ay", "una queja o un susto", "¡Ay, me duele!"],
          ["a ver", "mirar, comprobar", "A ver qué dice la carta."], ["haber", "el verbo", "Debe haber un error."], ["hecho", "del verbo hacer", "Ya he hecho la tarea."],
          ["echo", "del verbo echar", "Echo sal a la sopa."], ["vez", "una ocasión", "Otra vez llegó tarde."], ["ves", "del verbo ver", "¿Ves el autobús?"]])}
{C.caja("tip", "hay / ahí / ay", "<p>«Ahí hay un hombre que dice ¡ay!». Si puede cambiarla por <em>allí</em>, es <strong>ahí</strong>; si puede cambiarla por <em>existe</em> o <em>existen</em>, es <strong>hay</strong>.</p>")}
{P("Compruebe", "Ya he ___ la tarea.", ["echo", "hecho"], 1, {0: "Viene de hacer, no de echar."}, "<strong>hecho</strong>, del verbo hacer.")}
<div class="caja caja-tip"><span class="etiqueta et-verde">Actividad · dictado de palabras</span>
<p>Pulse 🔊 en cada número y escriba la palabra en su cuaderno, con su tilde si la lleva. Cuando termine las doce, abra «Ver» en cada una para corregirse. Si falla una, escriba al lado la regla que la explica. Si la voz no suena, pida a alguien que le dicte.</p>
<ol class="dictado-pal">{"".join(f'<li><button type="button" class="dp-btn" data-hablar="{w}" data-vel="0.7" aria-label="Escuchar la palabra {i}">🔊 {i}</button><details><summary>Ver</summary><span class="dp-sol">{w}</span></details></li>' for i, w in enumerate(PALABRAS, 1))}</ol>
<p>Si tiene con quién practicar, hagan un «dictado cooperativo»: uno dicta cinco oraciones de un periódico y el otro las escribe; luego cambian y se corrigen mirando el original.</p></div>"""

    secciones = [("s1", "La sílaba tónica", s1), ("s2", "Las reglas de la tilde", s2), ("s3", "Palabras cortas que cambian con la tilde", s3), ("s4", "Letras que suenan igual", s4)]
    tarea = [("Diez palabras con tilde.", "Busque en un periódico o una revista diez palabras con tilde. Sepárelas en sílabas, marque la tónica y escriba por qué la llevan (aguda en n, esdrújula, hiato…)."),
             ("Mi palabra difícil.", "Elija tres palabras que suele escribir mal. Para cada una, escriba la regla o el truco que le ayudará a recordarla y tres oraciones donde la use."),
             ("Oraciones con pares.", "Escriba una oración con cada palabra: <em>tú, tu, sí, si, hay, ahí, hecho, echo</em>.")]
    quiz = [
        ("<strong>sábado</strong> es una palabra…", TIPOS, 2, {0: "La fuerza no está al final.", 1: "La fuerza está en la antepenúltima: SÁ-ba-do."}, "<strong>Esdrújula</strong>: siempre lleva tilde."),
        ("¿Cuándo lleva tilde una palabra aguda?", ["Cuando termina en n, s o vocal", "Cuando no termina en n, s ni vocal", "Siempre"], 0, {1: "Esa es la regla de las llanas.", 2: "Esa es la regla de las esdrújulas."}, "Termina en <strong>n, s o vocal</strong>."),
        ("¿Cómo se escribe?", ["reloj", "relój"], 0, {1: "Es aguda y termina en j: sin tilde."}, "<strong>reloj</strong>: aguda terminada en j."),
        ("¿Cómo se escribe?", ["fácil", "facil"], 0, {1: "Es llana y termina en l: con tilde."}, "<strong>fácil</strong>."),
        ("¿Cómo se escribe?", ["camiones", "camiónes"], 0, {1: "camiones es llana y termina en s: sin tilde."}, "<strong>camiones</strong>: la tilde desaparece."),
        ("___ tienes razón.", ["Tú", "Tu"], 0, {1: "Es la persona: lleva tilde."}, "<strong>Tú</strong>, la persona."),
        ("___ llueve, no voy.", ["Si", "Sí"], 0, {1: "Es una condición: sin tilde."}, "<strong>Si</strong>: condición."),
        ("Cuando era niño, ___ con mi abuelo.", ["jugaba", "jugava"], 0, {1: "El pasado en -aba se escribe con b."}, "<strong>jugaba</strong>: -aba con b."),
        ("Plural de <strong>voz</strong>:", ["voces", "vozes"], 0, {1: "La z pasa a c delante de e."}, "<strong>voces.</strong>"),
        ("Deje la caja ___.", ["ahí", "hay"], 0, {1: "Es un lugar: se puede cambiar por allí."}, "<strong>ahí</strong>: lugar."),
    ]
    filas = [
        ("Sílaba tónica", "Encuentro la sílaba tónica y digo si la palabra es aguda, llana o esdrújula.", "La encuentro, pero dudo con algunas palabras.", "No la encuentro (<a href=\"#s1\">repase la sección 1</a>)."),
        ("Reglas de la tilde", "Aplico las reglas de agudas, llanas, esdrújulas, monosílabos e hiatos, y la tilde diacrítica.", "Me equivoco con las llanas o con tú/tu, sí/si.", "Pongo la tilde a ojo (<a href=\"#s2\">repase las secciones 2 y 3</a>)."),
        ("Letras", "Uso las reglas de b/v, z/c, g/j, h, y distingo hay/ahí/ay y hecho/echo.", "Dudo con algunas palabras.", "No conozco las reglas (<a href=\"#s4\">repase la sección 4</a>)."),
    ]
    cierre = "<p>Ya sabe por qué una palabra lleva tilde y cómo elegir entre letras que suenan igual. En la próxima lección verá cuándo escribir de manera <strong>formal o informal</strong>.</p>"
    glosario = [("Sílaba tónica", "La que se pronuncia con más fuerza."), ("Aguda, llana, esdrújula", "Palabras con la fuerza en la última, la penúltima o la antepenúltima sílaba."),
                ("Tilde diacrítica", "La que distingue palabras que se escriben igual: tú/tu, sí/si."), ("Hiato", "Dos vocales juntas en sílabas distintas: dí-a, pa-ís.")]
    conexion = ("<p>En la Lección 1.1 aprendió a separar las sílabas y a reconocer el hiato. Con eso ya tiene la mitad del trabajo: la tilde depende de qué sílaba suena más fuerte.</p>"
                "<p><strong>Lo que necesita:</strong> el cuaderno y, para el dictado, la voz encendida o alguien que le dicte.</p>")
    estd = LE.estandares(["W.3"], base=["L.1.1"], fund=["RF.3"])
    return C.pagina_leccion(N, LE.titulo(N), "Las reglas que explican la tilde y las letras dudosas.", ["Ortografía", "Tilde"],
                            ["<strong>Encontrar</strong> la sílaba tónica y clasificar las palabras.", "<strong>Aplicar</strong> las reglas generales de la tilde y la tilde diacrítica.",
                             "<strong>Elegir</strong> entre letras que suenan igual.", "<strong>Escribir</strong> al dictado sin errores de ortografía."],
                            estd, conexion, secciones, tarea, quiz, filas, cierre, ("3-3", LE.titulo("3-3")), glosario, P)


def practica():
    to = []
    for pal, k in TONICA:
        s = pal.split("-")
        t = tipo(pal, k)
        to.append({"enun": f"<span class=\"grande\">{pal.replace('-', '')}</span><br>¿Cuál es la sílaba tónica?", "ops": s, "ok": k, "enOrden": True,
                   "pista": "Diga la palabra en voz alta como si llamara a alguien de lejos. ¿Qué sílaba suena más fuerte?",
                   "exp": "-".join(f"<strong>{x.upper()}</strong>" if i == k else x for i, x in enumerate(s)) + f": es <strong>{t}</strong>."})
    ti = [{"enun": "¿Cómo se escribe?", "ops": [a, b], "ok": 0, "pista": "Separe la palabra en sílabas, busque la tónica y mire en qué letra termina.", "exp": f"«{a}». {e}"} for a, b, e in TILDE]
    def may(s): return s[0].upper() + s[1:]
    le = [{"enun": f"<span class=\"grande\">{o.replace('___', '_____')}</span>", "ops": ops, "ok": 0, "pista": "Busque la regla en las tablas de la lección.",
           "exp": f"«{may(o.replace('___', ops[0]))}» · {e}"} for o, ops, e in LETRAS]
    mods = [("tonica", "La sílaba tónica", C.om("m1", "Toque la sílaba que suena más fuerte.")),
            ("tilde", "¿Con tilde o sin tilde?", C.om("m2", "Elija la escritura correcta.")),
            ("letras", "Letras que suenan igual", C.om("m3", "Elija la palabra bien escrita.")),
            ("dictado", "Dictado", C.huecos("m4", "Escuche la oración, escríbala y pulse <strong>Comprobar</strong>. Las palabras en verde están bien; en naranja, revise la tilde; en rosado, la palabra está mal escrita o sobra. La revisión mira las palabras, las tildes y la mayúscula inicial; las comas y los signos, revíselos usted con la oración final."))]
    js = (C.js_datos("TO", to) + C.js_datos("TI", ti) + C.js_datos("LE", le) + C.js_datos("DC", FRASES) +
          'creaBanco("m1", TO);\ncreaBanco("m2", TI);\ncreaBanco("m3", LE);\ncreaDictado("m4", DC);\n')
    return C.pagina_practica(N, LE.titulo(N), "Cuatro actividades · los ejercicios cambian cada vez · dos intentos en cada uno", mods, js)


if __name__ == "__main__":
    LE.construye(N, leccion, practica, horas="Unas 3 horas")
