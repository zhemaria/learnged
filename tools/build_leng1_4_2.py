# -*- coding: utf-8 -*-
"""LearnGED · Artes del lenguaje (español) · Nivel 1 · Lección 4.2 · Aclarar y resumir lo leído.
Fuente: clases_leng1/clase_4-2.html (GEDparaHispanos), adaptada al marco de LearnGED.
Uso: python3 tools/build_leng1_4_2.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import leng_es as LE
from leng_es import C
from build_leng1_4_1 import CAJA1, CAJA2

LE.nivel(1)
N = "4-2"
SUENO = "El sueño es muy importante para la salud. Cuando una persona duerme ocho horas, su cuerpo descansa y se recupera. El cerebro también necesita el sueño para guardar lo que aprendió durante el día. Los adultos que duermen poco se enferman más y se sienten cansados. Por eso, los doctores recomiendan dormir entre siete y nueve horas cada noche."
AGUA = "Beber suficiente agua es importante para la salud. El agua ayuda a que el cuerpo mantenga la temperatura correcta. También ayuda a la digestión y a que los riñones funcionen bien. Cuando una persona no bebe suficiente agua, puede sentir cansancio y dolor de cabeza. Por eso, conviene tomar agua varias veces al día, aunque no se tenga sed."
ESTR = ["🔁 Releer", "🔍 Buscar pistas", "💬 Preguntar", "📖 Consultar"]
SITUACIONES = [("Una oración larga lo confundió y no sabe de quién habla.", 0), ("No conoce la palabra «frágil», pero la oración dice «se puede romper».", 1),
               ("Encontró una palabra técnica y no hay ninguna pista alrededor.", 3), ("Releyó dos veces y la idea sigue sin estar clara; su hija estudia ese tema.", 2),
               ("Se distrajo y no recuerda qué decía el párrafo anterior.", 0), ("No sabe qué es «panadería», pero el texto dice «comprar pan fresco».", 1),
               ("Lee «hipotecario» en un papel del banco y no hay explicación.", 3), ("No entiende una instrucción del formulario; puede llamar a la oficina.", 2)]
RESUMENES = [
    (SUENO, ["El sueño es importante: el cuerpo descansa y el cerebro guarda lo aprendido. Por eso se recomienda dormir de siete a nueve horas.",
             "Cuando una persona duerme ocho horas, su cuerpo descansa y se recupera. El cerebro también necesita el sueño.",
             "Dormir es lo más importante de la vida y nadie debería trabajar de noche."], 0,
     {1: "Copia oraciones del texto y deja fuera el consejo final.", 2: "Inventa ideas que el texto no dice."}),
    (AGUA, ["El agua es necesaria para que el cuerpo funcione: controla la temperatura y ayuda a la digestión. Si no tomamos suficiente, nos cansamos.",
            "El agua ayuda a que el cuerpo mantenga la temperatura correcta.",
            "Hay que tomar ocho litros de agua cada hora."], 0,
     {1: "Es solo un detalle, no todo el texto.", 2: "Inventa un dato que el texto no da."}),
    ("Marisol vive en un barrio tranquilo de Chicago. Sus vecinos son amables y siempre se saludan en la mañana. A ella le gusta caminar a la panadería los sábados para comprar pan fresco.",
     ["Marisol vive en un barrio de Chicago con vecinos amables, y los sábados camina a comprar pan.", "A Marisol le gusta el pan.", "Marisol vive en un barrio tranquilo de Chicago. Sus vecinos son amables."], 0,
     {1: "Es un detalle; falta lo principal.", 2: "Copia dos oraciones enteras y deja fuera los sábados."}),
]


def leccion():
    P = C.Practicas()
    s1 = f"""<p>En la Lección 4.1 vio lo que hace el lector <strong>antes</strong> de leer. Hoy completa el ciclo:</p>
{C.tabla("El ciclo de la lectura", ["Momento", "Estrategia", "Lección"], [["🔍 Antes", "Predecir y preguntar", "4.1"], ["📖 Durante", "<strong>Aclarar</strong> dudas", "esta lección"], ["✍️ Después", "<strong>Resumir</strong> lo leído", "esta lección"]])}
<h3>Cuatro estrategias para aclarar</h3>
<p>Cuando encuentre una palabra, una oración o una idea que no entiende, no siga como si nada. Pare y use una de estas estrategias:</p>
{C.tabla("Cuatro estrategias para aclarar", ["Estrategia", "Cuándo usarla", "Cómo se hace"],
         [["🔁 Releer", "Una oración lo confundió.", "Vuelva atrás y léala despacio otra vez."], ["🔍 Buscar pistas", "Una palabra es desconocida.", "Mire las palabras de alrededor: pueden darle el significado."],
          ["💬 Preguntar", "La duda no se aclara sola.", "Pregunte a alguien que sepa, o anote la duda para resolverla después."], ["📖 Consultar", "La palabra es nueva y no hay pistas.", "Búsquela en un diccionario o en el celular."]])}
{C.ejemplo("Pensar en voz alta: un lector aclara mientras lee", [
    ("1", "<em>Marisol vive en un barrio <strong>tranquilo</strong> de Chicago. Sus vecinos son <strong>amables</strong> y siempre se saludan en la mañana. A ella le gusta caminar a la <strong>panadería</strong> los sábados para comprar pan fresco.</em>"),
    ("2", "«<strong>Tranquilo</strong>: releo. Si los vecinos son amables y se saludan, tranquilo es calmado, sin ruido ni problemas»."),
    ("3", "«<strong>Amables</strong>: busco pistas. Se saludan cada mañana: amables es buenos con los demás»."),
    ("4", "«<strong>Panadería</strong>: busco pistas. Va a comprar pan fresco: es el lugar donde venden pan»."),
    ], "Nunca dejó de leer: aclaró y siguió.")}
{P("Compruebe", "No conoce la palabra <em>frágil</em>, pero la oración dice «la madera está frágil y se puede romper». ¿Qué estrategia conviene?", ESTR, 1,
   {0: "Releer ayuda, pero aquí la pista ya está en la misma oración.", 2: "No hace falta: el texto ya lo explica.", 3: "Antes de buscar en el diccionario, mire las palabras de al lado."},
   "<strong>Buscar pistas</strong>: «se puede romper» dice qué es frágil.")}"""

    s2 = f"""<p><strong>Resumir</strong> es decir, con sus propias palabras, lo más importante de lo que leyó. Un buen resumen es:</p>
<ul><li><strong>Corto:</strong> deja fuera lo secundario.</li><li><strong>Claro:</strong> cualquiera lo entiende.</li><li><strong>Fiel:</strong> no inventa ni cambia las ideas del texto.</li></ul>
{C.caja("ojo", "Resumir no es copiar", "<p>Resumir es <strong>parafrasear</strong>: decir lo mismo con sus palabras. Si copia oraciones enteras, no está resumiendo. Esta destreza es la misma que pide la respuesta escrita del GED: usar las ideas de un texto sin copiarlo.</p>")}
<h3>Cuatro pasos para resumir</h3>
<ol><li><strong>La idea principal:</strong> ¿de qué se trata? Esa es su primera oración.</li><li><strong>Dos o tres detalles importantes:</strong> los que explican la idea principal.</li>
<li><strong>Deje fuera lo secundario:</strong> ejemplos pequeños, repeticiones.</li><li><strong>Escriba con sus palabras.</strong></li></ol>
<div class="texto-lectura"><p>{SUENO}</p></div>
<div class="caja caja-tip"><span class="etiqueta et-verde">✍️ Resumen en dos oraciones</span><p>«El sueño es muy importante porque el cuerpo descansa y el cerebro guarda lo aprendido. Los doctores recomiendan dormir entre siete y nueve horas cada noche para no enfermarse.»</p>
<p>Dice lo más importante, pero no copia ninguna oración entera: cambian las palabras y el orden; la idea es la misma.</p></div>
<h3>Ahora resuma usted</h3>
<p>Lea este texto y escriba en su cuaderno un resumen de dos oraciones con los cuatro pasos. Después compare.</p>
<div class="texto-lectura"><p>{AGUA}</p></div>
<details class="caja caja-tip"><summary><strong>Ya escribí mi resumen: ver un resumen modelo</strong></summary>
<p>«El agua es necesaria para que el cuerpo funcione bien: controla la temperatura y ayuda a la digestión y a los riñones. Si no tomamos suficiente, nos cansamos y nos duele la cabeza, así que conviene beberla durante todo el día.»</p>
<p>Su resumen no tiene que ser igual. Revise que diga la idea principal y uno o dos detalles importantes, con sus palabras.</p></details>"""

    s3 = f"""<p>Vuelva a leer el cuento de la Lección 4.1, esta vez con las dos estrategias nuevas.</p>
<div class="texto-lectura">{"".join(f"<p>{x}</p>" for x in CAJA1 + CAJA2)}</div>
<p>{LE.escuchar(" ".join(CAJA1 + CAJA2).replace("—", " "), "Escuchar el cuento", 0.85)}</p>
<h3>Aclarar: tres palabras difíciles</h3>
{P("Aclare", "«…la madera está <strong>frágil</strong> y se puede romper…». ¿Qué significa <em>frágil</em>?", ["Muy pesada", "Que se rompe con facilidad", "Muy nueva"], 1,
   {0: "La pista dice «se puede romper», no habla del peso.", 2: "La caja era vieja."}, "<strong>Que se rompe con facilidad.</strong> Estrategia: buscar pistas en la misma oración.")}
{P("Aclare", "«…un pañuelo <strong>bordado</strong> con flores azules». Aquí casi no hay pistas. ¿Qué estrategia conviene?", ESTR, 3,
   {0: "Releer no le da más información.", 1: "La oración casi no da pistas.", 2: "Puede servir, pero lo más rápido es consultar."}, "<strong>Consultar</strong>: <em>bordado</em> es un dibujo hecho con hilo y aguja sobre la tela.")}
{P("Aclare", "«…le contaba cuánto la <strong>extrañaba</strong>». El abuelo trabajaba lejos de casa. ¿Qué significa <em>extrañar</em>?", ["Echar de menos a alguien", "Sentirse raro", "Enojarse"], 0,
   {1: "Puede significar eso en otros textos, pero aquí habla de alguien que está lejos.", 2: "Nada en el texto habla de enojo."}, "<strong>Echar de menos a alguien.</strong> Pista: estaba lejos de su familia.")}
<h3>Resumir el cuento</h3>
<p>Escriba en su cuaderno un resumen en dos oraciones: <strong>quién</strong>, <strong>qué pasó</strong> y <strong>cómo terminó</strong>.</p>
<details class="caja caja-tip"><summary><strong>Ya escribí mi resumen: ver un resumen posible</strong></summary>
<p>«Lucía y su abuela encontraron una caja vieja con las cartas que el abuelo escribió cuando trabajaba lejos. Al leerlas se emocionaron, y decidieron guardar la caja como el tesoro de la familia.»</p></details>"""

    secciones = [("s1", "Aclarar: qué hacer cuando algo no se entiende", s1), ("s2", "Resumir: contar lo leído con sus palabras", s2), ("s3", "De vuelta al cuento: aclare y resuma", s3)]
    tarea = [("Complete «Mis tres preguntas».", "Agregue a lo que escribió en la Lección 4.1 una palabra que aclaró en el cuento, su significado y la estrategia que usó."),
             ("Resumen final.", "Escriba un resumen del cuento de dos oraciones, con sus palabras: quién, qué pasó y cómo terminó."),
             ("Un texto de su vida.", "Lea una noticia corta o un aviso y escriba su resumen en dos oraciones.")]
    quiz = [
        ("¿Qué se hace <strong>durante</strong> la lectura cuando algo no se entiende?", ["Seguir como si nada", "Parar y aclarar con una estrategia"], 1, {}, "<strong>Parar y aclarar.</strong>"),
        ("¿Cuáles son las cuatro estrategias para aclarar?", ["Releer, buscar pistas, preguntar y consultar", "Copiar, borrar, saltar y dormir", "Predecir, resumir, subrayar y contar"], 0, {1: "Saltarse lo difícil no aclara nada.", 2: "Predecir y resumir son de antes y de después."}, "<strong>Releer, buscar pistas, preguntar y consultar.</strong>"),
        ("Una oración larga lo confundió. ¿Qué hace primero?", ["La relee despacio", "Cierra el libro", "Busca otra lectura"], 0, {1: "No se rinda: hay estrategias.", 2: "Primero intente aclararla."}, "<strong>Releer</strong>."),
        ("¿Qué es <strong>resumir</strong>?", ["Copiar las oraciones más largas", "Decir lo más importante con sus propias palabras", "Contar todo con detalle"], 1, {0: "Copiar no es resumir.", 2: "Un resumen deja fuera lo secundario."}, "Decir <strong>lo más importante con sus palabras</strong>."),
        ("¿Cómo es un buen resumen?", ["Largo y con todos los detalles", "Corto, claro y fiel", "Con opiniones propias"], 1, {0: "Lo largo no es resumen.", 2: "Fiel: no agrega opiniones."}, "<strong>Corto, claro y fiel.</strong>"),
        ("¿Qué es <strong>parafrasear</strong>?", ["Decir lo mismo con otras palabras", "Copiar palabra por palabra", "Traducir al inglés"], 0, {1: "Eso es copiar.", 2: "Se parafrasea en el mismo idioma."}, "Decir lo mismo <strong>con otras palabras</strong>."),
        ("¿Cuál es el primer paso para resumir?", ["Encontrar la idea principal", "Contar las palabras", "Elegir el detalle más pequeño"], 0, {1: "La cantidad no importa.", 2: "Los detalles pequeños se dejan fuera."}, "Encontrar la <strong>idea principal</strong>."),
        ("En el cuento, <em>frágil</em> significa…", ["que se rompe fácilmente", "muy grande"], 0, {}, "<strong>Que se rompe fácilmente</strong>: la oración dice «se puede romper»."),
        ("¿Qué pregunta conviene hacerse al terminar un resumen?", ["¿Usé mis palabras o copié?", "¿Tiene muchas comas?"], 0, {}, "<strong>¿Usé mis palabras o copié?</strong>, y ¿dice la idea principal?"),
        ("¿Qué <strong>no</strong> debe tener un resumen?", ["La idea principal", "Ideas que el texto no dice", "Uno o dos detalles importantes"], 1, {0: "La idea principal es lo primero.", 2: "Los detalles importantes sí van."}, "Ideas <strong>inventadas</strong>: el resumen es fiel."),
    ]
    filas = [
        ("Aclarar dudas", "Elijo la estrategia que conviene (releer, buscar pistas, preguntar, consultar).", "Casi siempre releo, aunque haya otra mejor.", "Sigo leyendo sin entender (<a href=\"#s1\">repase la sección 1</a>)."),
        ("Resumir", "Escribo un resumen corto, claro y fiel, con mis palabras.", "Mi resumen copia alguna oración o es largo.", "Copio el texto (<a href=\"#s2\">repase la sección 2</a>)."),
        ("Usar el ciclo completo", "Predigo, aclaro y resumo en cualquier texto.", "Uso solo una o dos estrategias.", "No uso ninguna (<a href=\"#s3\">repase la sección 3</a>)."),
    ]
    cierre = "<p>Ya tiene las cuatro estrategias del buen lector: predecir, preguntar, aclarar y resumir. En la próxima lección trabajará una destreza central del examen GED: encontrar la <strong>idea principal</strong> de un párrafo.</p>"
    glosario = [("Aclarar", "Resolver una duda durante la lectura."), ("Resumir", "Decir lo más importante de un texto con sus propias palabras."),
                ("Parafrasear", "Decir lo mismo con otras palabras."), ("Fiel", "Que no cambia ni inventa las ideas del texto.")]
    conexion = ("<p>Un buen lector no se rinde cuando algo no se entiende: para, piensa y usa una estrategia. Y al terminar, cuenta con sus palabras lo más importante.</p>"
                "<p><strong>Lo que necesita:</strong> el cuaderno con lo que escribió en la Lección 4.1.</p>")
    estd = LE.estandares(["R.2.2", "R.4.1"], base=["W.1"])
    return C.pagina_leccion(N, LE.titulo(N), "Si algo no se entiende, pare y aclare; al terminar, resuma.", ["R.2.2 · Resumir", "R.4.1 · Vocabulario"],
                            ["<strong>Aclarar</strong> palabras e ideas con cuatro estrategias: releer, buscar pistas, preguntar y consultar.", "<strong>Resumir</strong> un texto corto con sus palabras.",
                             "<strong>Reconocer</strong> un buen resumen: corto, claro y fiel.", "<strong>Usar</strong> el ciclo completo con un cuento."],
                            estd, conexion, secciones, tarea, quiz, filas, cierre, ("4-3", LE.titulo("4-3")), glosario, P)


def practica():
    est = [{"enun": f"<strong>{s}</strong><br>¿Qué estrategia conviene?", "ops": ESTR, "ok": k, "enOrden": True,
            "pista": "Releer si una oración confundió; pistas si están cerca; preguntar si alguien sabe; consultar si no hay pistas.", "exp": f"<strong>{ESTR[k]}</strong>."} for s, k in SITUACIONES]
    res = [{"enun": f"<div class=\"texto-lectura\"><p>{t}</p></div>¿Cuál es el mejor resumen?", "ops": o, "ok": k, "pistas": p,
            "exp": f"<strong>{o[k]}</strong> Es corto, claro y fiel."} for t, o, k, p in RESUMENES]
    voc = [("La sopa estaba <strong>hirviendo</strong>: salía humo y no se podía tocar la olla.", ["muy caliente", "muy fría", "muy salada"], 0),
           ("El niño estaba <strong>agotado</strong> después de jugar todo el día; se durmió en el sofá.", ["muy cansado", "muy alegre", "muy enojado"], 0),
           ("El examen fue <strong>sencillo</strong>, no como el anterior, que fue muy difícil.", ["fácil", "largo", "caro"], 0),
           ("Mi vecina es muy <strong>generosa</strong>: siempre comparte su comida con todos.", ["que da y comparte", "que no habla", "que llega tarde"], 0),
           ("La calle estaba <strong>desierta</strong>: no había ni un carro ni una persona.", ["vacía", "llena", "mojada"], 0),
           ("El médico le recetó un <strong>jarabe</strong> para la tos; hay que tomar una cucharada.", ["una medicina líquida", "una pastilla", "una vacuna"], 0)]
    vb = [{"enun": f"{s}<br>¿Qué significa la palabra en negrita?", "ops": o, "ok": k, "pista": "Lea la oración completa: la pista está cerca.", "exp": f"<strong>{o[k]}</strong>."} for s, o, k in voc]
    mods = [("aclarar", "¿Qué estrategia conviene?", C.om("m1", "Elija la estrategia para aclarar cada duda.")),
            ("resumen", "El mejor resumen", C.om("m2", "Lea el texto y elija el resumen corto, claro y fiel.")),
            ("pistas", "Aclare con las pistas", C.om("m3", "Use las palabras de alrededor para saber qué significa la palabra en negrita."))]
    js = (C.js_datos("EST", est) + C.js_datos("RES", res) + C.js_datos("VOC", vb) + 'creaBanco("m1", EST);\ncreaBanco("m2", RES);\ncreaBanco("m3", VOC);\n')
    return C.pagina_practica(N, LE.titulo(N), "Tres actividades · los ejercicios cambian cada vez · dos intentos en cada uno", mods, js)


if __name__ == "__main__":
    LE.construye(N, leccion, practica, horas="Unas 3 horas")
