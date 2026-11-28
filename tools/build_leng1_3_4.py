# -*- coding: utf-8 -*-
"""LearnGED · Artes del lenguaje (español) · Nivel 1 · Lección 3.4 · Los tiempos verbales.
Fuente: clases_leng1/clase_3-4.html (GEDparaHispanos) y sus prácticas de gramatica, adaptadas al marco de LearnGED.
Uso: python3 tools/build_leng1_3_4.py
"""
import os, random, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import leng_es as LE
from leng_es import C

LE.nivel(1)
N = "3-4"

PERS = ["yo", "tú", "ella", "nosotros", "ellos"]
TERM = {
    "pas": {"ar": ["é", "aste", "ó", "amos", "aron"], "er": ["í", "iste", "ió", "imos", "ieron"], "ir": ["í", "iste", "ió", "imos", "ieron"]},
    "pre": {"ar": ["o", "as", "a", "amos", "an"], "er": ["o", "es", "e", "emos", "en"], "ir": ["o", "es", "e", "imos", "en"]},
}
FUT = ["é", "ás", "á", "emos", "án"]
VERBOS = [("caminar", "al trabajo"), ("trabajar", "ocho horas"), ("estudiar", "por la noche"), ("cocinar", "arroz con pollo"), ("hablar", "con la maestra"),
          ("comer", "en casa"), ("vender", "frutas en el mercado"), ("beber", "agua fría"), ("vivir", "en Chicago"), ("escribir", "una carta"), ("abrir", "la tienda")]
PISTAS = {"pas": ["Ayer", "Anoche", "La semana pasada", "En 2020"], "pre": ["Hoy", "Ahora", "Todos los días", "Siempre"], "fut": ["Mañana", "El año próximo", "Más tarde", "La semana que viene"]}
NOMBRE = {"pas": "pasado", "pre": "presente", "fut": "futuro"}


def conj(v, t, i):
    if t == "fut":
        return v + FUT[i]
    return v[:-2] + TERM[t][v[-2:]][i]


def leccion():
    P = C.Practicas()
    s1 = f"""<p>El verbo no solo dice qué pasa: también dice <strong>cuándo</strong> pasa. A eso se le llama <strong>tiempo verbal</strong>. Hay tres tiempos básicos:</p>
{C.tabla("Los tres tiempos básicos", ["Tiempo", "Cuándo", "Ejemplo"],
         [["⬅️ Pasado", "Ya ocurrió.", "Ayer <u class=\"verbo\">caminé</u>."], ["▶️ Presente", "Ocurre ahora o siempre.", "Hoy <u class=\"verbo\">camino</u>."], ["➡️ Futuro", "Va a ocurrir.", "Mañana <u class=\"verbo\">caminaré</u>."]])}
{C.caja("ojo", "Un relato, un mismo tiempo", "<p>Dentro de un mismo párrafo, los tiempos tienen que ser coherentes. Si cuenta algo que pasó ayer, mantenga el pasado de principio a fin. Saltar al futuro sin razón confunde al lector, y el examen GED lo marca como error.</p>")}
{P("Compruebe", "<em>Mañana ___ temprano.</em>", ["llegué", "llego", "llegaré"], 2, {0: "Llegué ya pasó; mañana todavía no ha llegado.", 1: "Mañana pide futuro."}, "<strong>llegaré</strong>: «mañana» pide futuro.")}"""

    s2 = f"""<p>Mire cómo cambia el verbo según el tiempo. La raíz se queda (<em>camin-</em>) y cambia la <strong>terminación</strong>. Eso se llama <strong>conjugar</strong>.</p>
<h3>Palabras pista</h3>
{C.tabla("Palabras que avisan el tiempo", ["Tiempo", "Palabras pista"],
         [["Pasado", "ayer, anoche, la semana pasada, hace dos días, antes, en 1995"], ["Presente", "hoy, ahora, ahora mismo, siempre, todos los días, generalmente"],
          ["Futuro", "mañana, más tarde, el año próximo, la semana que viene, dentro de un rato"]])}
<h3>El mismo día en tres tiempos</h3>
<p>Lea en voz alta las tres versiones y fíjese en los verbos subrayados.</p>
<div class="texto-lectura"><p><strong>⬅️ Ayer.</strong> Ayer, Marta <u class="verbo">caminó</u> al trabajo. <u class="verbo">Llegó</u> temprano y <u class="verbo">tomó</u> un café. Después <u class="verbo">trabajó</u> ocho horas y <u class="verbo">regresó</u> a su casa.</p>
<p><strong>▶️ Hoy.</strong> Hoy, Marta <u class="verbo">camina</u> al trabajo. <u class="verbo">Llega</u> temprano y <u class="verbo">toma</u> un café. Después <u class="verbo">trabaja</u> ocho horas y <u class="verbo">regresa</u> a su casa.</p>
<p><strong>➡️ Mañana.</strong> Mañana, Marta <u class="verbo">caminará</u> al trabajo. <u class="verbo">Llegará</u> temprano y <u class="verbo">tomará</u> un café. Después <u class="verbo">trabajará</u> ocho horas y <u class="verbo">regresará</u> a su casa.</p></div>
{C.caja("tip", "La tilde cuenta", "<p><em>Camino</em> (yo, hoy) y <em>caminó</em> (ella, ayer) solo se diferencian por la tilde. La tilde cambia el tiempo y la persona: léala con cuidado.</p>")}
<h3>Las tres familias: -ar, -er, -ir</h3>
<p>Los verbos sin conjugar (el <strong>infinitivo</strong>) terminan en <strong>-ar</strong>, <strong>-er</strong> o <strong>-ir</strong>: <em>hablar, comer, vivir</em>. Cada familia tiene sus terminaciones:</p>
{C.tabla("Hablar, comer y vivir con «yo» y con «ella»", ["Verbo", "Pasado", "Presente", "Futuro"],
         [["hablar", "yo hablé · ella habló", "yo hablo · ella habla", "yo hablaré · ella hablará"], ["comer", "yo comí · ella comió", "yo como · ella come", "yo comeré · ella comerá"],
          ["vivir", "yo viví · ella vivió", "yo vivo · ella vive", "yo viviré · ella vivirá"]])}
{P("Compruebe", "<em>Ayer, Sofía ___ clases.</em>", ["toma", "tomó", "tomará"], 1, {0: "«Ayer» pide pasado.", 2: "Tomará es futuro."}, "<strong>tomó</strong>: «ayer» pide pasado.")}"""

    s3 = f"""<div class="caja caja-tip"><span class="etiqueta et-verde">Actividad oral · «Ayer, hoy, mañana»</span>
<p>Elija tres acciones de su rutina (<em>cocinar, estudiar, manejar, llamar</em>) y diga cada una en los tres tiempos, en voz alta:</p>
<ul><li><em>Ayer caminé al trabajo.</em></li><li><em>Hoy camino al trabajo.</em></li><li><em>Mañana caminaré al trabajo.</em></li></ul>
<p>Si puede, grábese con el celular y escuche si se nota la diferencia entre <em>caminé</em>, <em>camino</em> y <em>caminaré</em>.</p></div>
{P("Compruebe", "¿Qué verbo se sale del tiempo?<br><em>Ayer fui al mercado. Compré frutas y verduras. Mañana preparo una sopa.</em>", ["fui", "Compré", "preparo"], 2,
   {0: "Fui es pasado, como «ayer».", 1: "Compré es pasado, como el resto."}, "<strong>preparo</strong> está en presente, aunque el relato va en pasado. Debería ser <em>preparé</em> (si ya ocurrió) o empezar otro relato con «mañana prepararé».")}"""

    secciones = [("s1", "¿Qué es el tiempo verbal?", s1), ("s2", "El tiempo en acción: conjugar", s2), ("s3", "Práctica: ayer, hoy, mañana", s3)]
    tarea = [("Mi día de ayer.", "Escriba un párrafo de 3 a 5 oraciones sobre lo que hizo ayer, con todos los verbos en pasado. Subraye cada verbo con doble raya."),
             ("Mi día de mañana.", "Escriba el mismo párrafo en futuro: <em>Mañana me levantaré…</em>"),
             ("Tres verbos, tres tiempos.", "Conjugue <em>hablar, comer</em> y <em>vivir</em> con <em>yo, tú</em> y <em>ella</em> en pasado, presente y futuro.")]
    quiz = [
        ("¿Qué dice el <strong>tiempo verbal</strong>?", ["Cuándo ocurre la acción", "Quién hace la acción", "Cómo es el sujeto"], 0, {1: "Eso lo dice el sujeto.", 2: "Eso lo dice el adjetivo."}, "<strong>Cuándo</strong> ocurre la acción."),
        ("<em>Ayer caminé.</em> ¿Qué tiempo es?", ["pasado", "presente", "futuro"], 0, {1: "«Ayer» ya pasó.", 2: "«Ayer» no es futuro."}, "<strong>Pasado</strong>."),
        ("<em>Mañana trabajaré.</em> ¿Qué tiempo es?", ["pasado", "presente", "futuro"], 2, {0: "Mañana todavía no llega.", 1: "La terminación -é al final de -aré es de futuro."}, "<strong>Futuro</strong>."),
        ("<em>Todos los días estudio.</em> ¿Qué tiempo es?", ["pasado", "presente", "futuro"], 1, {0: "«Todos los días» habla de lo que pasa siempre.", 2: "No dice que vaya a pasar después."}, "<strong>Presente</strong>."),
        ("¿Cuál es una palabra pista de <strong>pasado</strong>?", ["anoche", "mañana", "ahora"], 0, {1: "Mañana es futuro.", 2: "Ahora es presente."}, "<strong>anoche</strong>."),
        ("<em>Hoy yo ___ en casa.</em>", ["comí", "como", "comeré"], 1, {0: "Comí es pasado.", 2: "Comeré es futuro."}, "<strong>como</strong>."),
        ("<em>La semana pasada ellos ___ a México.</em>", ["viajan", "viajaron", "viajarán"], 1, {0: "Viajan es presente.", 2: "Viajarán es futuro."}, "<strong>viajaron</strong>."),
        ("<em>El año próximo nosotros ___ el GED.</em>", ["aprobamos", "aprobaremos"], 1, {}, "<strong>aprobaremos</strong>: el año próximo es futuro."),
        ("¿Qué diferencia hay entre <em>camino</em> y <em>caminó</em>?", ["Ninguna", "La tilde: camino es presente (yo) y caminó es pasado (ella o él)", "Caminó es futuro"], 1, {0: "La tilde cambia el significado.", 2: "El futuro sería caminará."}, "La <strong>tilde</strong> cambia el tiempo y la persona."),
        ("¿Qué es el <strong>infinitivo</strong>?", ["El verbo sin conjugar, terminado en -ar, -er o -ir", "El verbo en futuro", "Un sustantivo"], 0, {1: "El futuro es una forma conjugada.", 2: "Es una forma del verbo."}, "Es el verbo <strong>sin conjugar</strong>: <em>hablar, comer, vivir</em>."),
        ("¿Por qué conviene mantener el mismo tiempo en un párrafo?", ["Para que el lector no se confunda", "Porque es más corto"], 0, {}, "Para que el lector sepa <strong>cuándo</strong> pasa todo."),
        ("<em>Ayer Marta llegó temprano y toma un café.</em> ¿Qué está mal?", ["llegó", "toma", "temprano"], 1, {0: "Llegó va bien con ayer.", 2: "Temprano no es un verbo."}, "<strong>toma</strong> debería ser <em>tomó</em>."),
    ]
    filas = [
        ("Reconocer el tiempo", "Sé si un verbo está en pasado, presente o futuro, aunque no haya palabra pista.", "Lo sé cuando hay una palabra pista.", "Confundo los tiempos (<a href=\"#s1\">repase la sección 1</a>)."),
        ("Conjugar", "Conjugo verbos -ar, -er, -ir en los tres tiempos, con su tilde.", "Me equivoco en la tilde o en -er/-ir.", "No sé cambiar la terminación (<a href=\"#s2\">repase la sección 2</a>)."),
        ("Coherencia", "Mantengo el mismo tiempo en todo un párrafo.", "A veces se me escapa un verbo.", "Mezclo los tiempos (<a href=\"#s3\">repase la sección 3</a>)."),
    ]
    cierre = "<p>Ya sabe decir cuándo pasan las cosas. En la próxima lección va a juntar todo (sustantivos, adjetivos y verbos) para escribir <strong>oraciones completas</strong>, y aprenderá a reconocer los fragmentos.</p>"
    glosario = [("Tiempo verbal", "La forma del verbo que dice cuándo ocurre la acción."), ("Conjugar", "Cambiar la terminación del verbo según la persona y el tiempo."),
                ("Infinitivo", "El verbo sin conjugar: <em>hablar, comer, vivir</em>."), ("Palabra pista", "Palabra que avisa el tiempo: <em>ayer, hoy, mañana</em>.")]
    conexion = ("<p>El verbo tiene un superpoder: una máquina del tiempo. Con solo cambiar su final, dice si algo ya pasó, está pasando o va a pasar.</p>"
                "<p><strong>Lo que necesita:</strong> el cuaderno y, si puede, el celular para grabarse.</p>")
    estd = LE.estandares([], base=["L.1.2"])
    return C.pagina_leccion(N, LE.titulo(N), "Ayer, hoy, mañana: el verbo lo dice.", ["Gramática", "Tiempos verbales"],
                            ["<strong>Reconocer</strong> si un verbo está en pasado, presente o futuro.", "<strong>Usar</strong> las palabras pista para elegir el tiempo.",
                             "<strong>Conjugar</strong> verbos regulares -ar, -er, -ir en los tres tiempos.", "<strong>Mantener</strong> el mismo tiempo en un relato."],
                            estd, conexion, secciones, tarea, quiz, filas, cierre, ("3-5", LE.titulo("3-5")), glosario, P)


# ---------------------------------------------------------------- práctica
def banco_tiempo():
    r = random.Random(3)
    b = []
    for v, comp in VERBOS:
        for t in ("pas", "pre", "fut"):
            i = r.choice([0, 1, 2, 4])  # «nosotros» es igual en pasado y presente (caminamos, vivimos)
            pista = r.choice(PISTAS[t])
            b.append({"enun": f"<em>{pista}, {PERS[i]} <u class=\"verbo\">{conj(v, t, i)}</u> {comp}.</em><br>¿En qué tiempo está el verbo?", "ops": ["pasado", "presente", "futuro"],
                      "ok": ["pas", "pre", "fut"].index(t), "enOrden": True, "pista": "Mire la palabra pista del principio y la terminación del verbo.",
                      "exp": f"<strong>{NOMBRE[t].capitalize()}</strong>: «{pista.lower()}» y la terminación de <em>{conj(v, t, i)}</em>."})
    return b


def banco_conjuga():
    r = random.Random(5)
    b = []
    for v, comp in VERBOS:
        for t in ("pas", "pre", "fut"):
            i = r.choice([0, 1, 2, 4])  # «nosotros» es igual en pasado y presente (caminamos, vivimos)
            ops = [conj(v, tt, i) for tt in ("pas", "pre", "fut")]
            pista = r.choice(PISTAS[t])
            b.append({"partes": [f"{pista}, {PERS[i]} ", {"ops": ops, "ok": ["pas", "pre", "fut"].index(t)}, f" {comp}."],
                      "pista": f"«{pista}» pide {NOMBRE[t]}.", "exp": f"<strong>{pista}, {PERS[i]} {conj(v, t, i)} {comp}.</strong>"})
    return b


def banco_relato():
    datos = [
        "Ayer fui al mercado. Compré frutas y verduras. Después *cocino* una sopa para mi familia.",
        "El sábado pasado limpiamos la casa. Mi hijo lavó los platos y yo *barreré* la cocina.",
        "Mañana empezaré un trabajo nuevo. Me levantaré temprano y *tomé* el autobús de las seis.",
        "Todos los días camino al trabajo. Llego a las ocho y *saludé* a mis compañeros.",
        "Anoche estudié dos horas. Leí un cuento y *escribiré* un resumen corto.",
        "El año próximo viviremos en otra ciudad. Mis hijos irán a una escuela nueva y yo *busco* trabajo.",
        "Hoy hace frío. Mi hija se pone el abrigo y *salió* a la escuela.",
        "La semana pasada visité a mi abuela. Ella preparó tamales y nosotros *comemos* juntos.",
    ]
    return [{"consigna": "Toque el verbo que <strong>se sale del tiempo</strong> del relato.", "texto": x, "pista": "Busque primero las palabras pista y vea en qué tiempo van casi todos los verbos.", "exp": ""} for x in datos]


def practica():
    mods = [
        ("tiempo", "¿Pasado, presente o futuro?", C.om("m1", "Use la palabra pista y la terminación del verbo.")),
        ("conjugar", "Elija la forma del verbo", C.huecos("m2", "Elija en el menú la forma que pide la palabra pista.")),
        ("relato", "Un relato, un mismo tiempo", LE.marcar("m3", "En cada relato hay un verbo en el tiempo equivocado. Tóquelo.")),
    ]
    js = (C.js_datos("TIE", banco_tiempo()) + C.js_datos("CON", banco_conjuga()) + C.js_datos("REL", banco_relato()) +
          'creaBanco("m1", TIE);\ncreaHuecos("m2", CON);\ncreaMarcar("m3", REL);\n')
    return C.pagina_practica(N, LE.titulo(N), "Tres actividades · los ejercicios cambian cada vez · dos intentos en cada uno", mods, js)


if __name__ == "__main__":
    LE.construye(N, leccion, practica, horas="Unas 3 horas")
