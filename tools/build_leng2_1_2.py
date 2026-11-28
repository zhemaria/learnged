# -*- coding: utf-8 -*-
"""LearnGED · Artes del lenguaje (español) · Nivel 2 · Lección 1.2 · Prefijos y sufijos comunes para leer palabras nuevas.
Fuente: clases_leng2/clase_1-2.html (GEDparaHispanos) y gramatica/n2-l1-2.html, adaptadas al marco de LearnGED.
Uso: python3 tools/build_leng2_1_2.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import leng_es as LE
from leng_es import C

LE.nivel(2)
N = "1-2"
# (palabra, división correcta, dos divisiones erróneas, explicación)
SEPARA = [("desconectar", "des · conectar", ["de · sconectar", "descon · ectar"], "des- · conectar: lo contrario de conectar."),
          ("imposible", "im · posible", ["i · mposible", "impo · sible"], "im- · posible: que no es posible."),
          ("releer", "re · leer", ["rel · eer", "rele · er"], "re- · leer: leer otra vez."),
          ("precalentar", "pre · calentar", ["prec · alentar", "preca · lentar"], "pre- · calentar: calentar antes."),
          ("trabajador", "trabaja · dor", ["trab · ajador", "trabajad · or"], "trabaja · -dor: la persona que trabaja."),
          ("lentamente", "lenta · mente", ["lent · amente", "lentam · ente"], "lenta · -mente: de manera lenta."),
          ("peligroso", "peligr · oso", ["pelig · roso", "peli · groso"], "peligr · -oso: que tiene mucho peligro."),
          ("celebración", "celebra · ción", ["celeb · ración", "celebrac · ión"], "celebra · -ción: la acción de celebrar."),
          ("inútil", "in · útil", ["i · nútil", "inú · til"], "in- · útil: que no es útil."),
          ("deshacer", "des · hacer", ["de · shacer", "desha · cer"], "des- · hacer: hacer lo contrario."),
          ("reconstrucción", "re · construc · ción", ["rec · onstruc · ción", "recons · truc · ción"], "re- · construc · -ción: la acción de construir otra vez."),
          ("ilegal", "i · legal", ["il · egal", "ile · gal"], "i- · legal: que no es legal. Delante de l, in- se escribe i-."),
          ("cariñosamente", "cariñ · osa · mente", ["cari · ñosa · mente", "cariño · sa · mente"], "cariñ · -osa · -mente: de manera cariñosa."),
          ("vendedora", "vende · dora", ["vend · edora", "vended · ora"], "vende · -dora: la mujer que vende."),
          ("preescolar", "pre · escolar", ["pree · scolar", "pr · eescolar"], "pre- · escolar: antes de la escuela."),
          ("sabrosa", "sabr · osa", ["sab · rosa", "sabro · sa"], "sabr · -osa: que tiene mucho sabor.")]
SIGNIF = [("desatar", "Quitar el nudo, soltar", ["Atar otra vez", "Atar antes de tiempo"], "des-: lo contrario de atar."),
          ("incómodo", "Que no es cómodo", ["Muy cómodo", "Cómodo otra vez"], "in-: que no es."),
          ("recalentar", "Calentar otra vez", ["Que no está caliente", "De manera caliente"], "re-: otra vez."),
          ("predecir", "Decir antes lo que va a pasar", ["Decir lo mismo otra vez", "No decir nada"], "pre-: antes."),
          ("jugadora", "La mujer que juega", ["La acción de jugar", "De manera juguetona"], "-dora: quien hace la acción."),
          ("claramente", "De manera clara", ["Que tiene mucha claridad", "La acción de aclarar"], "-mente: de qué manera."),
          ("orgulloso", "Que tiene mucho orgullo", ["Que no tiene orgullo", "Que pierde el orgullo"], "-oso: que tiene mucho de algo."),
          ("construcción", "La acción de construir", ["La persona que construye", "Construir otra vez"], "-ción: la acción o su resultado."),
          ("injusto", "Que no es justo", ["Justo otra vez", "La persona que juzga"], "in-: que no es."),
          ("reaparecer", "Aparecer de nuevo", ["No aparecer nunca", "Aparecer antes que otros"], "re-: de nuevo."),
          ("desconocido", "Que no se conoce", ["Conocido otra vez", "Que conoce a mucha gente"], "des- niega: no conocido."),
          ("secadora", "La máquina que seca", ["La acción de secar", "De manera seca"], "-dora: lo que hace la acción."),
          ("prehistoria", "El tiempo antes de la escritura", ["La historia contada otra vez", "Una historia que no es real"], "pre-: antes de la historia escrita."),
          ("nervioso", "Que tiene muchos nervios", ["Que no tiene nervios", "La acción de ponerse nervioso"], "-oso: que tiene mucho de algo."),
          ("felizmente", "De manera feliz", ["La persona feliz", "Que no es feliz"], "-mente: de qué manera."),
          ("educación", "La acción de educar", ["La persona que educa", "Educar otra vez"], "-ción: la acción.")]
FAMILIA = [("Mi hermano es muy ___: trabaja doce horas al día.", "trabajador", ["trabajo", "trabajar"]), ("La ___ de la casa nos tomó toda la mañana.", "limpieza", ["limpiar", "limpio"]),
           ("Maneja ___: nunca pasa del límite de velocidad.", "cuidadosamente", ["cuidadoso", "cuidado"]), ("Es un perro muy ___: le encanta que lo acaricien.", "cariñoso", ["cariño", "cariñosamente"]),
           ("Tengo que ___ la carta porque tenía errores.", "reescribir", ["escritor", "escritura"]), ("El ___ del mercado me regaló una naranja.", "vendedor", ["vender", "venta"]),
           ("La ___ de cumpleaños fue en el parque.", "celebración", ["celebrar", "celebrado"]), ("___, todos llegaron a tiempo a la reunión.", "Felizmente", ["Feliz", "Felicidad"]),
           ("No encuentro nada: mi cuarto está en total ___.", "desorden", ["ordenar", "ordenado"]), ("Antes de hornear el pan, hay que ___ el horno.", "precalentar", ["caliente", "calentador"]),
           ("Esa calle es ___ de noche: hay muy poca luz.", "peligrosa", ["peligro", "peligrosamente"]), ("Puse la ropa sucia en la ___.", "lavadora", ["lavar", "lavado"]),
           ("Para trabajar mejor, decidimos ___ la oficina.", "reorganizar", ["organización", "organizado"]), ("Es ___ terminar todo hoy; necesitamos más tiempo.", "imposible", ["posible", "posibilidad"])]
HUERTO = ["Durante años, el terreno de la esquina estuvo desocupado. Estaba lleno de basura y parecía inútil. Un día, un grupo de vecinos decidió reorganizar ese espacio. La señora Rosa, una trabajadora muy dedicada, buscó en la biblioteca la información necesaria: qué plantas crecen mejor en un clima lluvioso y cómo abonar la tierra.",
          "Primero limpiaron el terreno cuidadosamente. Después reconstruyeron la cerca vieja, que estaba desarmada. Los niños ayudaron con entusiasmo y aprendieron rápidamente a sembrar.",
          "Al principio, algunos vecinos desconfiaban del proyecto: decían que era imposible cultivar en la ciudad. Hoy el huerto es famoso en todo el barrio. Cada verano hay una celebración, y los vecinos comparten tomates sabrosos y chiles picantes. Como dice la señora Rosa, cuando se trabaja juntos, nada es imposible."]


def pre(x):
    return f'<span class="af-pre">{x}</span>'


def suf(x):
    return f'<span class="af-suf">{x}</span>'


def leccion():
    P = C.Practicas()
    s1 = f"""<p>En la Lección 1.1 separó palabras en sílabas, por sus sonidos. Hoy las va a partir por su <strong>significado</strong>. Muchas palabras largas están hechas con piezas que se repiten. Si conoce esas piezas, <em>desorganización</em> deja de dar miedo: es {pre("des")}·organiza·{suf("ción")}, «la acción de quitar el orden».</p>
{C.tabla("Raíz, prefijo y sufijo", ["Parte", "Qué es", "Ejemplo"],
         [["Raíz", "La parte principal: lleva el significado básico.", "hacer"], ["Prefijo", "Va antes de la raíz y cambia su significado.", f"{pre('des')}hacer · {pre('re')}hacer"],
          ["Sufijo", "Va después de la raíz y forma una palabra nueva.", f"feliz{suf('mente')} · lava{suf('dora')}"]])}
<p>A los prefijos y sufijos juntos se les llama <strong>afijos</strong>. Aquí los prefijos van en {pre("azul")} y los sufijos en {suf("rosa")}.</p>
{C.caja("tip", "La prueba del prefijo", "<p>Si al quitar el prefijo queda una palabra real con un significado relacionado, era un prefijo: <em>releer → leer</em>. Pero en <em>red, reloj, regla, precio</em> o <em>invierno</em> no hay prefijo: al quitar las primeras letras no queda nada con sentido.</p>")}"""

    s2 = f"""{C.tabla("Cuatro prefijos frecuentes", ["Prefijo", "Significa", "Ejemplos"],
         [[pre("des-"), "Hacer lo contrario de una acción, o quitar.", "deshacer · desconectar · desatar · desordenar"], [f"{pre('in-')} · {pre('im-')} · {pre('i-')}", "Que no es o no tiene esa cualidad.", "inútil · injusto · imposible · ilegal · irregular"],
          [pre("re-"), "Otra vez, de nuevo.", "releer · rehacer · reescribir · recalentar"], [pre("pre-"), "Antes.", "precalentar · preescolar · prehistoria · predecir"]])}
{C.caja("tip", "Por qué cambia in-", "<p>Delante de <strong>p</strong> o <strong>b</strong> se escribe <em>im-</em> (imposible, imborrable); delante de <strong>l</strong> o <strong>r</strong>, <em>i-</em> (ilegal, irregular). Significa lo mismo: «no». Y una pista: <em>des-</em> suele ir con acciones (conectar → desconectar); <em>in-</em>, con palabras que describen (útil → inútil).</p>")}
{C.tabla("Cuatro sufijos frecuentes", ["Sufijo", "Forma una palabra que dice…", "Ejemplos"],
         [[suf("-ción"), "La acción o su resultado.", "celebrar → celebración · educar → educación"], [suf("-mente"), "De qué manera se hace algo.", "lenta → lentamente · fácil → fácilmente"],
          [f"{suf('-oso')} · {suf('-osa')}", "Que tiene mucho de algo.", "peligro → peligroso · lluvia → lluviosa"], [f"{suf('-dor')} · {suf('-dora')}", "La persona o la máquina que hace la acción.", "trabajar → trabajador · lavar → lavadora"]])}
{C.caja("ojo", "Dos detalles de -mente", "<p>Se une a la forma femenina (lento → lenta → <em>lentamente</em>), y la palabra conserva la tilde que ya tenía: rápido → <em>rápidamente</em>, fácil → <em>fácilmente</em>.</p>")}
{P("Compruebe", "¿Qué significa <strong>predecir</strong>?", ["Decir antes lo que va a pasar", "Decir otra vez", "No decir nada"], 0, {1: "Otra vez sería re-.", 2: "No sería des- o in-."}, "<strong>pre-</strong> = antes.")}"""

    s3 = f"""<p>Ante una palabra larga que no conoce, no la lea de golpe. Use la <strong>lupa de afijos</strong>:</p>
<ol><li>¿Empieza con un prefijo conocido?</li><li>¿Termina con un sufijo conocido?</li><li>Lo que queda en medio es la raíz: ¿la conoce?</li><li>Lea cada parte y luego la palabra entera. Una los significados.</li></ol>
{C.tabla("La lupa en acción", ["Palabra", "Partes", "Significado"],
         [["reconstrucción", f"{pre('re')} · construc · {suf('ción')}", "la acción de construir otra vez"], ["cariñosamente", f"cariñ · {suf('osa')} · {suf('mente')}", "de manera cariñosa"],
          ["desconocido", f"{pre('des')} · conoc · {suf('ido')}", "que no se conoce"], ["imposible", f"{pre('im')} · posible", "que no es posible"]])}
<h3>Lectura: «Un huerto en el barrio»</h3>
{LE.escuchar(" ".join(HUERTO), "Escuchar el texto")}
<div class="texto-lectura">{"".join(f"<p>{p}</p>" for p in HUERTO)}</div>
<p>En su cuaderno, haga una lista de las palabras del texto que tienen afijos y sepárelas con la lupa.</p>
<details class="caja caja-tip"><summary><strong>Ver la lista</strong></summary><p><em>desocupado, inútil, reorganizar, trabajadora, información, lluvioso, cuidadosamente, reconstruyeron, desarmada, rápidamente, desconfiaban, imposible, famoso, celebración, sabrosos</em>.</p></details>
{P("Comprensión", "Con la lupa, ¿qué significa <strong>desarmada</strong>?", ["Lo contrario de armada: con las piezas separadas", "Armada otra vez", "Muy bien armada"], 0, {1: "Otra vez sería re-.", 2: "des- no intensifica: invierte."}, "<strong>des- + armada</strong>: lo contrario de armada.")}
{P("Comprensión", "¿Qué pensaban al principio algunos vecinos?", ["Que era imposible cultivar en la ciudad", "Que el huerto sería famoso", "Que faltaba agua"], 0, {1: "Eso pasó al final.", 2: "No lo dice el texto."}, "Que era <strong>imposible cultivar en la ciudad</strong>; al final, el huerto se hizo famoso.")}
<div class="caja caja-tip"><span class="etiqueta et-verde">Actividad · familias de palabras</span>
<p>Una <strong>familia de palabras</strong> comparte la misma raíz. Escriba todas las que pueda con <em>trabajo, limpio</em> y <em>orden</em>, y explique cada una. Ejemplo con <em>cuidado</em>: cuidar, cuidadoso, cuidadosamente, descuidado, descuidar.</p></div>
<details class="caja caja-tip"><summary><strong>Ver respuestas posibles</strong></summary><p><strong>trabajo:</strong> trabajar, trabajador, trabajadora, trabajoso. <strong>limpio:</strong> limpiar, limpieza, limpiamente, limpiador. <strong>orden:</strong> ordenar, ordenado, desorden, desordenar, reordenar.</p></details>"""

    secciones = [("s1", "Las partes de una palabra", s1), ("s2", "Prefijos y sufijos frecuentes", s2), ("s3", "La lupa de afijos y la lectura", s3)]
    tarea = [("Cazador de afijos.", "En un periódico, un folleto o una etiqueta, busque cinco palabras con prefijo y cinco con sufijo. Sepárelas con la lupa y escriba qué significan."),
             ("Mis familias.", "Pase en limpio las familias de palabras de la sección 3."),
             ("Mis oraciones.", "Escriba cinco oraciones sobre su semana usando una palabra con des-, una con re-, una con -mente, una con -oso y una con -dor.")]
    quiz = [
        ("¿Qué es la raíz de una palabra?", ["La parte principal, con el significado básico", "La primera letra", "El acento"], 0, {1: "No.", 2: "No."}, "La parte con el <strong>significado básico</strong>."),
        ("¿Dónde va el prefijo?", ["Antes de la raíz", "Después de la raíz"], 0, {}, "<strong>Antes.</strong>"),
        ("¿Qué significa <em>re-</em>?", ["Otra vez", "Antes", "No"], 0, {1: "Eso es pre-.", 2: "Eso es in-."}, "<strong>Otra vez.</strong>"),
        ("¿Por qué se escribe <strong>imposible</strong> y no «inposible»?", ["Porque delante de p se escribe im-", "Porque es una excepción sin regla"], 0, {}, "Delante de <strong>p</strong> o <strong>b</strong>, <em>im-</em>."),
        ("¿Tiene prefijo la palabra <strong>reloj</strong>?", ["No: al quitar «re» no queda una palabra", "Sí: re- significa otra vez"], 0, {}, "<strong>No</strong>: «loj» no es una palabra."),
        ("¿Qué dice una palabra con <em>-mente</em>?", ["De qué manera se hace algo", "Quién hace la acción"], 0, {}, "<strong>De qué manera.</strong>"),
        ("¿Qué es una <strong>secadora</strong>?", ["La máquina que seca", "La acción de secar", "Algo que no está seco"], 0, {1: "Eso sería el secado.", 2: "No."}, "La <strong>máquina que seca</strong> (-dora)."),
        ("¿Cómo se escribe correctamente?", ["rápidamente", "rapidamente"], 0, {}, "<strong>rápidamente</strong>: conserva la tilde."),
        ("¿Qué significa <strong>lluvioso</strong>?", ["Que tiene mucha lluvia", "Que no tiene lluvia"], 0, {}, "Que tiene <strong>mucha lluvia</strong> (-oso)."),
        ("¿Cómo se divide <strong>reconstrucción</strong>?", ["re · construc · ción", "rec · onstruc · ción", "recons · truc · ción"], 0, {1: "El prefijo es re-.", 2: "El prefijo es re- solo."}, "<strong>re · construc · ción.</strong>"),
    ]
    filas = [
        ("Partes de la palabra", "Separo prefijo, raíz y sufijo.", "Encuentro la raíz, pero dudo con los afijos.", "No veo las partes (<a href=\"#s1\">repase la sección 1</a>)."),
        ("Significado de los afijos", "Sé qué significan des-, in-, re-, pre-, -ción, -mente, -oso, -dor.", "Sé algunos.", "No los recuerdo (<a href=\"#s2\">repase la sección 2</a>)."),
        ("Leer palabras nuevas", "Uso la lupa para leer y entender palabras largas.", "A veces.", "Las leo de golpe (<a href=\"#s3\">repase la sección 3</a>)."),
    ]
    cierre = "<p>Ya sabe partir las palabras por su significado. En la próxima lección trabajará la <strong>fluidez lectora</strong>: precisión, ritmo y expresión.</p>"
    glosario = [("Raíz", "Parte principal de la palabra."), ("Prefijo", "Pieza antes de la raíz: des-, in-, re-, pre-."), ("Sufijo", "Pieza después de la raíz: -ción, -mente, -oso, -dor."),
                ("Afijo", "Nombre común de prefijos y sufijos."), ("Familia de palabras", "Palabras que comparten la raíz.")]
    conexion = ("<p>En la Lección 1.1 separó palabras por sus sonidos. Hoy las partirá por su significado, para leer y entender palabras largas que no conoce.</p>"
                "<p><strong>Lo que necesita:</strong> el cuaderno y un periódico, un folleto o una etiqueta.</p>")
    estd = LE.estandares(["R.4.1"], base=["L.2.1"], fund=["RF.3"])
    return C.pagina_leccion(N, LE.titulo(N), "Piezas que se repiten: la llave de las palabras largas.", ["R.4.1 · Vocabulario", "Afijos"],
                            ["<strong>Separar</strong> una palabra en prefijo, raíz y sufijo.", "<strong>Usar</strong> el significado de cuatro prefijos y cuatro sufijos frecuentes.",
                             "<strong>Leer</strong> palabras largas con la lupa de afijos.", "<strong>Formar</strong> familias de palabras."],
                            estd, conexion, secciones, tarea, quiz, filas, cierre, ("1-3", LE.titulo("1-3")), glosario, P)


def practica():
    sep = [{"enun": f"<strong class=\"grande\">{w}</strong><br>¿Cómo se divide en sus partes?", "ops": [ok] + d, "ok": 0, "pista": "Busque primero un prefijo conocido al principio y un sufijo conocido al final.", "exp": e} for w, ok, d, e in SEPARA]
    sig = [{"enun": f"<strong class=\"grande\">{w}</strong><br>¿Qué significa?", "ops": [ok] + d, "ok": 0, "pista": "Separe la palabra y piense qué significa cada pieza.", "exp": f"<strong>{w}</strong>: {ok.lower()}. {e}"} for w, ok, d, e in SIGNIF]
    fam = [{"enun": f"<strong>{o}</strong><br>¿Qué palabra de la familia va en el espacio?", "ops": [ok] + d, "ok": 0, "pista": "¿Hace falta una persona, una acción, una cualidad o una manera?", "exp": f"Va <strong>{ok}</strong>."} for o, ok, d in FAMILIA]
    mods = [("separar", "Separe las partes", C.om("m1", "Elija la división correcta en prefijo, raíz y sufijo.")),
            ("significado", "¿Qué significa?", C.om("m2", "Use la lupa de afijos.")),
            ("familias", "Familias de palabras", C.om("m3", "Elija la palabra de la familia que completa la oración."))]
    js = C.js_datos("SEP", sep) + C.js_datos("SIG", sig) + C.js_datos("FAM", fam) + 'creaBanco("m1", SEP);\ncreaBanco("m2", SIG);\ncreaBanco("m3", FAM);\n'
    return C.pagina_practica(N, LE.titulo(N), "Tres actividades · los ejercicios cambian cada vez · dos intentos en cada uno", mods, js)


if __name__ == "__main__":
    LE.construye(N, leccion, practica, horas="Unas 3 horas")
