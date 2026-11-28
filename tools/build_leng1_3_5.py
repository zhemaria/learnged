# -*- coding: utf-8 -*-
"""LearnGED · Artes del lenguaje (español) · Nivel 1 · Lección 3.5 · Oración completa frente a fragmento.
Fuente: clases_leng1/clase_3-5.html (GEDparaHispanos) y sus prácticas de gramatica, adaptadas al marco de LearnGED.
Uso: python3 tools/build_leng1_3_5.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import leng_es as LE
from leng_es import C

LE.nivel(1)
N = "3-5"

COMPLETAS = ["Los niños juegan en el parque.", "Mi mamá prepara arroz con frijoles.", "Llueve.", "Cocino todos los domingos.", "El autobús llegó tarde.",
             "Yo trabajo en un restaurante.", "Cuando llegó mi mamá, cenamos juntos.", "El carro rojo de mi tío es nuevo.", "Estudiamos de noche.",
             "La clínica abre a las ocho.", "Mi hijo aprobó el examen.", "Después del trabajo, voy a la escuela."]
# fragmento: (texto, qué le falta, una reparación)
FRAGMENTOS = [("Niños jugando en el parque.", "v", "Los niños juegan en el parque."), ("Cuando llegó mi mamá.", "i", "Cuando llegó mi mamá, cenamos juntos."),
              ("El carro rojo de mi tío.", "v", "El carro rojo de mi tío es nuevo."), ("Caminando hacia el trabajo.", "sv", "Camino hacia el trabajo."),
              ("Porque llovía mucho.", "i", "No salimos porque llovía mucho."), ("El perro de la vecina.", "v", "El perro de la vecina ladra mucho."),
              ("Después del trabajo.", "sv", "Después del trabajo voy a la escuela."), ("Mi tío en el carro.", "v", "Mi tío espera en el carro."),
              ("Si tengo tiempo mañana.", "i", "Si tengo tiempo mañana, te llamo."), ("Una casa grande con jardín.", "v", "Una casa grande con jardín cuesta mucho."),
              ("Comiendo juntos en la cocina.", "sv", "Comemos juntos en la cocina."), ("Para aprobar el examen.", "sv", "Estudio mucho para aprobar el examen."),
              ("Mis hermanos y mis primos.", "v", "Mis hermanos y mis primos viven en Texas."), ("Aunque estaba cansada.", "i", "Fue a trabajar aunque estaba cansada.")]
FALTA = {"v": "Le falta el verbo", "sv": "Le faltan el sujeto y el verbo", "i": "Tiene sujeto y verbo, pero la idea queda a medias"}


def leccion():
    P = C.Practicas()
    s1 = f"""<p>Una <strong>oración completa</strong> expresa una idea completa. Para estarlo necesita, como mínimo:</p>
<ul><li><strong>Un sujeto</strong>: quién. Puede estar escrito (<em>Mi mamá cocina</em>) o sobreentendido (<em>Cocino</em>: el sujeto es yo), como vio en la Lección 1.2.</li>
<li><strong>Un verbo conjugado</strong>: qué hace, o cómo es o cómo está.</li>
<li>Y al final, un <strong>punto</strong> que cierra la idea.</li></ul>
{C.tabla("Oración completa y fragmento", ["", "Ejemplo", "Por qué"],
         [["✅ Completa", "Los niños juegan en el parque.", "Sujeto (los niños) + verbo conjugado (juegan) + punto."],
          ["❌ Fragmento", "Niños jugando en el parque.", "<em>Jugando</em> no es un verbo conjugado: no dice quién juega ni cuándo. La idea queda colgando."]])}
{P("Compruebe", "¿Es una oración completa?<br><em>Llueve.</em>", ["Sí", "No"], 0, {}, "<strong>Sí</strong>: tiene un verbo conjugado y la idea está cerrada. Algunos verbos, como <em>llover</em>, no necesitan sujeto.")}"""

    s2 = f"""<p>Un <strong>fragmento</strong> es un grupo de palabras al que le falta algo. Por eso no expresa una idea completa, y el lector se queda esperando: <em>¿y qué pasó?</em></p>
{C.tabla("Tres clases de fragmentos", ["Fragmento", "Qué le falta", "Versión completa"],
         [["Niños ayudando en la cocina.", "El verbo conjugado.", "Los niños <strong>ayudan</strong> en la cocina."],
          ["Cuando llegó mi mamá.", "Terminar la idea: ¿qué pasó cuando llegó?", "Cuando llegó mi mamá, <strong>cenamos juntos</strong>."],
          ["El carro rojo de mi tío.", "El verbo: ¿qué hace o cómo es el carro?", "El carro rojo de mi tío <strong>es muy bonito</strong>."]])}
{C.caja("tip", "Prueba rápida", "<p>Léase la oración en voz alta. Si al terminar se queda esperando que diga algo más, es un fragmento. Una oración completa cierra la idea.</p>")}
{C.caja("ojo", "Palabras que dejan la idea abierta", "<p>Cuando un grupo de palabras empieza con <em>cuando, porque, si, aunque, después de, para</em>, casi siempre necesita otra parte para cerrar la idea: <em>Porque llovía mucho</em> → <em>No salimos <strong>porque llovía mucho</strong>.</em></p>")}
{P("Compruebe", "¿Qué le falta a <em>Porque estaba cansado</em>?", ["El verbo", "Terminar la idea", "Nada"], 1,
   {0: "Tiene verbo: estaba.", 2: "Léala en voz alta: ¿qué pasó porque estaba cansado?"}, "Le falta <strong>terminar la idea</strong>: <em>Me dormí temprano porque estaba cansado.</em>")}"""

    s3 = f"""<p>En la parte escrita del GED cuenta mucho la calidad de las oraciones. Un consejo que casi nunca falla: <strong>escriba oraciones cortas y claras</strong>. Una oración de cuatro líneas, en la que se pierden el sujeto y el verbo, confunde al lector. Use esta fórmula:</p>
<p class="bloques"><span class="ficha sil">Sujeto</span> + <span class="ficha sil2">Verbo</span> + <span class="ficha sil">Complemento</span> + <span class="ficha sil2">.</span></p>
<p>Quién + qué hace + sobre qué o dónde + punto.</p>
{LE.oracion("Mi mamá", "prepara arroz con frijoles.")}
{LE.oracion("Los estudiantes", "leen el libro de matemáticas.")}
{LE.oracion("El perro", "duerme en la sala.")}
{C.caja("ojo", "No le tenga miedo a las oraciones cortas", "<p>Escribir bien no es escribir largo. Una oración corta y clara vale más que una larga y confusa. Punto. Nueva oración. Punto. Así, paso a paso, se construye un buen párrafo.</p>")}
<h3>El detective gramatical</h3>
<p>Este texto tiene <strong>tres fragmentos</strong> escondidos. Léalo despacio y cópielos en su cuaderno. Después abra la versión correcta.</p>
<div class="texto-lectura"><p>Mi familia vive en Chicago. Una casa grande con jardín. Mi papá trabaja en una fábrica. Cuando llega del trabajo. Mi mamá lo recibe con café caliente. Comiendo juntos en la cocina. Mis hermanos hacen la tarea.</p></div>
<details class="caja caja-tip"><summary><strong>Ver la versión correcta (después de intentarlo)</strong></summary>
<p>Mi familia vive en Chicago. <strong>Vivimos en</strong> una casa grande con jardín. Mi papá trabaja en una fábrica. Cuando llega del trabajo<strong>, mi</strong> mamá lo recibe con café caliente. <strong>Después comemos</strong> juntos en la cocina. Mis hermanos hacen la tarea.</p>
<ul><li><em>Una casa grande con jardín</em> → se le agregó lo que faltaba: <em>Vivimos en…</em> (sujeto sobreentendido y verbo).</li><li><em>Cuando llega del trabajo</em> → se unió con la oración siguiente para cerrar la idea.</li><li><em>Comiendo juntos</em> → se cambió por el verbo conjugado <em>comemos</em>.</li></ul></details>"""

    secciones = [("s1", "¿Qué es una oración completa?", s1), ("s2", "¿Qué es un fragmento?", s2), ("s3", "Estrategia para el GED: oraciones cortas", s3)]
    tarea = [("Corrija los fragmentos.", "Convierta en oraciones completas: <em>Mi tío en el carro. · Caminando hacia el trabajo. · Porque llovía mucho. · El perro de la vecina. · Después del trabajo.</em> No hay una sola respuesta: lo importante es que la idea quede cerrada."),
             ("Con la fórmula.", "Escriba 5 oraciones sobre su trabajo o su familia con la fórmula sujeto + verbo + complemento + punto. Subraye el sujeto con una raya y el verbo con dos."),
             ("Revise un mensaje.", "Busque un mensaje de texto que haya escrito esta semana. ¿Tiene fragmentos? Escríbalo otra vez con oraciones completas.")]
    quiz = [
        ("¿Qué necesita como mínimo una oración completa?", ["Un verbo conjugado y una idea cerrada", "Muchas palabras", "Un adjetivo"], 0, {1: "Puede ser muy corta: «Llueve.»", 2: "No hace falta adjetivo."}, "Un <strong>verbo conjugado</strong> y una idea cerrada (el sujeto puede estar sobreentendido)."),
        ("¿Qué es un <strong>fragmento</strong>?", ["Una oración muy corta", "Un grupo de palabras al que le falta algo para ser oración", "Una pregunta"], 1, {0: "Una oración corta puede estar completa.", 2: "Las preguntas pueden ser completas."}, "Un grupo de palabras <strong>incompleto</strong>."),
        ("¿Cuál es una oración completa?", ["Caminando hacia el trabajo.", "Camino hacia el trabajo.", "Hacia el trabajo."], 1, {0: "Caminando no es un verbo conjugado.", 2: "No tiene verbo."}, "<strong>Camino hacia el trabajo.</strong>"),
        ("¿Cuál es un fragmento?", ["Estudiamos de noche.", "El perro de la vecina.", "Mi hijo aprobó el examen."], 1, {0: "Tiene verbo conjugado (estudiamos).", 2: "Tiene sujeto y verbo."}, "<strong>El perro de la vecina.</strong> No tiene verbo."),
        ("¿Qué le falta a <em>Cuando llegó mi mamá</em>?", ["El sujeto", "El verbo", "Terminar la idea"], 2, {0: "El sujeto es mi mamá.", 1: "El verbo es llegó."}, "<strong>Terminar la idea</strong>: ¿qué pasó cuando llegó?"),
        ("¿Qué le falta a <em>Niños jugando en el parque</em>?", ["Un verbo conjugado", "Un adjetivo", "Nada"], 0, {1: "No hace falta adjetivo.", 2: "Léala en voz alta: ¿está completa?"}, "Un <strong>verbo conjugado</strong>: <em>Los niños juegan…</em>"),
        ("¿Es completa <em>Cocino todos los domingos</em>?", ["Sí", "No"], 0, {}, "<strong>Sí</strong>: el sujeto (yo) está en el verbo."),
        ("¿Cuál repara bien <em>Mi tío en el carro</em>?", ["Mi tío en el carro rojo.", "Mi tío espera en el carro.", "En el carro mi tío."], 1, {0: "Sigue sin verbo.", 2: "Sigue sin verbo."}, "<strong>Mi tío espera en el carro.</strong>"),
        ("¿Cuál es la fórmula para el GED?", ["Sujeto + verbo + complemento + punto", "Muchas comas y una idea larga", "Solo adjetivos"], 0, {1: "Las oraciones largas confunden.", 2: "Sin verbo no hay oración."}, "<strong>Sujeto + verbo + complemento + punto.</strong>"),
        ("¿Por qué conviene escribir oraciones cortas en el GED?", ["Son más claras y no se pierde el sujeto ni el verbo", "El examen pide pocas palabras"], 0, {}, "Porque son <strong>más claras</strong>."),
        ("¿Cuál de estas palabras suele dejar la idea abierta?", ["porque", "mesa", "corre"], 0, {1: "Es un sustantivo.", 2: "Es un verbo."}, "<strong>porque</strong>: necesita otra parte que cierre la idea."),
        ("¿Cuántos fragmentos hay?<br><em>Mi papá trabaja de noche. Después de la cena. Mi mamá lo espera. Leyendo un libro.</em>", ["1", "2", "3"], 1, {0: "Revise cada parte que termina en punto.", 2: "Mi papá trabaja de noche y Mi mamá lo espera están completas."}, "<strong>2</strong>: <em>Después de la cena</em> y <em>Leyendo un libro</em>."),
    ]
    filas = [
        ("Reconocer oraciones completas", "Sé si un grupo de palabras es oración completa, también con sujeto sobreentendido.", "Dudo cuando el sujeto no está escrito.", "No las distingo (<a href=\"#s1\">repase la sección 1</a>)."),
        ("Reparar fragmentos", "Sé qué le falta a cada fragmento y lo reparo.", "Los encuentro, pero me cuesta repararlos.", "No los encuentro (<a href=\"#s2\">repase la sección 2</a>)."),
        ("Oraciones cortas", "Escribo oraciones cortas y claras con la fórmula.", "Mis oraciones a veces se alargan.", "Escribo ideas largas sin puntos (<a href=\"#s3\">repase la sección 3</a>)."),
    ]
    cierre = "<p>Ya escribe oraciones completas. En la última lección del tema aprenderá a vestirlas bien: mayúsculas, puntos, comas y signos de pregunta y de exclamación.</p>"
    glosario = [("Oración completa", "Grupo de palabras con verbo conjugado que expresa una idea cerrada."), ("Fragmento", "Grupo de palabras al que le falta algo para ser oración."),
                ("Verbo conjugado", "Verbo que dice quién y cuándo: <em>juega, jugó, jugará</em>. <em>Jugando</em> y <em>jugar</em> no lo son."),
                ("Complemento", "La parte que completa lo que dice el verbo: <em>arroz con frijoles</em>, <em>en la sala</em>.")]
    conexion = ("<p>Aquí se junta todo lo del tema: los sustantivos, los adjetivos y los verbos se unen para formar oraciones que de verdad expresan una idea, no las que se quedan a medias. Esta lección es clave para el GED.</p>"
                "<p><strong>Lo que necesita:</strong> el cuaderno y un mensaje de texto que haya escrito esta semana.</p>")
    estd = LE.estandares(["L.2.2"], base=["W.3"])
    return C.pagina_leccion(N, LE.titulo(N), "Una idea completa: quién, qué hace y punto.", ["L.2.2 · Fragmentos", "W.3 · Escritura clara"],
                            ["<strong>Distinguir</strong> oraciones completas de fragmentos.", "<strong>Decir</strong> qué le falta a un fragmento: el verbo, el sujeto y el verbo, o terminar la idea.",
                             "<strong>Reparar</strong> fragmentos para cerrar la idea.", "<strong>Escribir</strong> oraciones cortas y claras con la fórmula del GED."],
                            estd, conexion, secciones, tarea, quiz, filas, cierre, ("3-6", LE.titulo("3-6")), glosario, P)


# ---------------------------------------------------------------- práctica
def banco_cual():
    b = [{"enun": f"<strong>{x}</strong><br>¿Oración completa o fragmento?", "ops": ["Oración completa", "Fragmento"], "ok": 0, "enOrden": True,
          "exp": "Tiene verbo conjugado y la idea está cerrada."} for x in COMPLETAS]
    b += [{"enun": f"<strong>{x}</strong><br>¿Oración completa o fragmento?", "ops": ["Oración completa", "Fragmento"], "ok": 1, "enOrden": True,
           "exp": f"Es un fragmento: {FALTA[f][0].lower() + FALTA[f][1:]}. Por ejemplo: <em>{r}</em>"} for x, f, r in FRAGMENTOS]
    return b


def banco_falta():
    ops = [FALTA["v"], FALTA["sv"], FALTA["i"]]
    return [{"enun": f"¿Qué le falta a <strong>{x}</strong>?", "ops": ops, "ok": ["v", "sv", "i"].index(f), "enOrden": True,
             "pista": "Busque primero si hay un verbo conjugado; después, si hay alguien que lo hace; y por último, si la idea se cierra.",
             "exp": f"{FALTA[f]}. Por ejemplo: <em>{r}</em>"} for x, f, r in FRAGMENTOS]


def banco_repara():
    b = []
    for x, f, r in FRAGMENTOS:
        malo1 = x.rstrip(".") + " de siempre."
        malo2 = "Y " + x[0].lower() + x[1:]
        b.append({"enun": f"¿Cuál repara el fragmento <strong>{x}</strong>?", "ops": [r, malo1, malo2], "ok": 0,
                  "pista": "La versión buena tiene un verbo conjugado y cierra la idea.", "exp": f"<strong>{r}</strong>"})
    return b


def banco_texto():
    textos = [
        (["Mi hermana trabaja en un hospital.", "Cuidando a los enfermos.", "Ella es muy paciente."], 1),
        (["Los sábados vamos al mercado.", "Compramos frutas y verduras.", "Porque son más baratas."], 2),
        (["El perro de mi vecino.", "Ladra toda la noche.", "Nadie puede dormir."], 0),
        (["Estudio en la biblioteca.", "Si tengo tiempo después del trabajo.", "Allí hay silencio."], 1),
        (["Mi hijo aprobó el examen.", "Estamos muy contentos.", "Una fiesta pequeña en casa."], 2),
    ]
    return [{"enun": "En este texto hay un fragmento. ¿Cuál es?", "ops": o, "ok": k, "enOrden": True,
             "pista": "Léalas en voz alta una por una. ¿Cuál deja la idea colgando?", "exp": f"<strong>{o[k]}</strong> es el fragmento."} for o, k in textos]


def practica():
    mods = [
        ("completa", "¿Completa o fragmento?", C.om("m1", "Lea en voz alta. ¿Hay verbo conjugado? ¿La idea se cierra?")),
        ("que-falta", "¿Qué le falta?", C.om("m2", "Decida qué le falta a cada fragmento.")),
        ("reparar", "Repare el fragmento", C.om("m3", "Elija la versión completa.")),
        ("en-el-texto", "Fragmentos en un texto", C.om("m4", "Busque el fragmento escondido entre oraciones completas.")),
    ]
    js = (C.js_datos("CUA", banco_cual()) + C.js_datos("FAL", banco_falta()) + C.js_datos("REP", banco_repara()) + C.js_datos("TXT", banco_texto()) +
          'creaBanco("m1", CUA);\ncreaBanco("m2", FAL);\ncreaBanco("m3", REP);\ncreaBanco("m4", TXT);\n')
    return C.pagina_practica(N, LE.titulo(N), "Cuatro actividades · los ejercicios cambian cada vez · dos intentos en cada uno", mods, js)


if __name__ == "__main__":
    LE.construye(N, leccion, practica, horas="Unas 3 horas")
