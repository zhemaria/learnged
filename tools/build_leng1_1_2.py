# -*- coding: utf-8 -*-
"""LearnGED · Artes del lenguaje (español) · Nivel 1 · Lección 1.2 · La dirección de la lectura y la oración.
Fuentes: clases_leng1/clase_1-2.html y gramatica/n1-l1-2.html (GEDparaHispanos), adaptadas al marco de LearnGED.
Uso: python3 tools/build_leng1_1_2.py
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import leng_es as LE
from leng_es import C

LE.nivel(1)
N = "1-2"

PARRAFOS = [
    ("La huerta de la escuela", "Los niños siembran una huerta en la escuela. Cada mañana riegan las plantas con cuidado. El sol ayuda a que las hojas crezcan. La maestra revisa el trabajo del grupo. Todos esperan la primera cosecha."),
    ("El desayuno en familia", "Mi familia desayuna muy temprano. Mi madre prepara café con leche. Mi hermano corta la fruta en trozos. Yo pongo los platos en la mesa. Después todos lavamos la loza. El desayuno nos da energía para el día."),
    ("Camino al trabajo", "Espero el autobús en la esquina. El viaje dura media hora. Siempre llevo un libro para leer. La ventana me deja ver la ciudad. Bajo cerca de mi trabajo."),
    ("La biblioteca", "La biblioteca abre a las nueve. Los estantes guardan miles de libros. Un cartel pide silencio a los visitantes. Puedo pedir tres libros prestados. Devuelvo cada libro en dos semanas. Ese lugar me ayuda a estudiar."),
    ("Mi perro", "Mi perro duerme junto a la puerta. Come dos veces al día. Sale al parque todas las tardes. Ladra cuando escucha un ruido extraño. Mi familia lo cuida con cariño."),
    ("Un día de lluvia", "Hoy llueve sobre la ciudad. Las calles se llenan de charcos. La gente camina con paraguas. Los carros avanzan despacio. El aire queda fresco y limpio. Mañana volverá el sol."),
    ("En la cocina del restaurante", "Trabajo en la cocina de un restaurante. Llego antes de las siete. Preparo las verduras para el almuerzo. El cocinero revisa cada plato. Salimos cuando termina el turno."),
    ("La clase de la noche", "La clase empieza a las seis de la tarde. La maestra explica las fracciones en la pizarra. Los estudiantes resuelven ejercicios en parejas. Nadie sale del salón sin preguntar. Al final repasamos los errores más comunes."),
    ("El mercado", "El mercado abre los sábados. Los puestos venden frutas y verduras frescas. Muchas personas llegan muy temprano. Los precios bajan al final del día. Siempre regreso con la bolsa llena."),
    ("Caminar cada día", "Camino treinta minutos cada día. Salgo de casa después de la cena. Recorro el mismo camino del parque. El ejercicio mejora mi descanso. Ahora subo las escaleras sin cansancio."),
    ("La computadora", "Uso la computadora para estudiar. La enciendo apenas llego a casa. Busco videos sobre el tema de la clase. Guardo mis tareas en una carpeta. Apago el equipo antes de dormir."),
    ("El domingo", "El domingo descanso en casa. Duermo una hora más de lo normal. Preparo un almuerzo sencillo para todos. Por la tarde llamo a mi familia. La noche llega tranquila y silenciosa."),
]


def svg_recorrido():
    aria = ("Recorrido de los ojos al leer: tres líneas de texto. Cada línea se lee de izquierda a derecha, siguiendo una flecha. "
            "Al terminar una línea, una flecha punteada baja y regresa al comienzo de la línea siguiente.")
    F = 'font-family="Segoe UI, Arial, sans-serif"'
    s = [f'<svg class="recorrido" viewBox="0 0 520 210" role="img" aria-label="{aria}" xmlns="http://www.w3.org/2000/svg">',
         '<defs><marker id="fl-rec" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10z" fill="#004b75"/></marker>'
         '<marker id="fl-rec2" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10z" fill="#a3154f"/></marker></defs>']
    for i, y in enumerate((40, 105, 170)):
        s.append(f'<text x="20" y="{y - 12}" {F} font-size="14" font-weight="700" fill="#1b1f24">Línea {i + 1}</text>')
        s.append(f'<line x1="20" y1="{y}" x2="490" y2="{y}" stroke="#004b75" stroke-width="4" marker-end="url(#fl-rec)"/>')
        if i < 2:
            s.append(f'<path d="M490 {y + 8} L40 {y + 47}" stroke="#a3154f" stroke-width="2.5" stroke-dasharray="7 6" fill="none" marker-end="url(#fl-rec2)"/>')
    s.append("</svg>")
    return "".join(s)


def leccion():
    P = C.Practicas()
    texto_guia = ["María se levantó muy temprano esa mañana.", "El cielo todavía estaba oscuro y el café olía rico.", "Ella sabía que el día sería largo, pero hermoso."]
    s1 = f"""<p>En español, como en inglés, leemos <strong>de izquierda a derecha</strong> y <strong>de arriba abajo</strong>. Al terminar una línea, los ojos bajan y vuelven al comienzo de la siguiente. Parece obvio, pero cuando uno lleva tiempo sin leer, los ojos saltan, regresan o se pierden entre líneas. Se puede volver a entrenar ese movimiento.</p>
{svg_recorrido()}
<h3>Practique con la guía de lectura</h3>
<p>Pulse <strong>Empezar la guía</strong>: cada palabra se ilumina por turno, en el orden en que deben moverse sus ojos. Sígala con la vista y, si quiere, con el dedo sobre la pantalla. Después lea usted el párrafo en voz alta, despacio.</p>
{LE.AVISO_VOZ}
<div class="guia" id="g1">
<p class="guia-texto">{"".join(f'<span class="guia-linea">{l}</span>' for l in texto_guia)}</p>
<p><button type="button" class="btn-voz" id="g1-empezar">▶ Empezar la guía</button>
<button type="button" class="btn-voz" id="g1-oir"><span aria-hidden="true">🔊</span> Escuchar el párrafo</button>
<label for="g1-vel">Velocidad:</label> <select id="g1-vel"><option value="1000">Muy despacio</option><option value="700" selected>Despacio</option><option value="450">Normal</option></select></p>
</div>
{C.caja("tip", "Con papel también funciona", "<p>Tome cualquier texto impreso (una receta, una carta, el periódico) y léalo pasando el dedo o un lápiz debajo de cada línea. Hasta los lectores expertos lo hacen cuando el texto se pone difícil. Si los ojos se le van solos, no se preocupe: vuelva al principio del párrafo y respire. La lectura no es una carrera.</p>")}
{P("Compruebe", "Al terminar de leer una línea, ¿adónde van los ojos?", ["Al final de la línea de arriba", "Al comienzo de la línea de abajo", "Al comienzo de la misma línea"], 1,
   {0: "Los ojos nunca suben para seguir leyendo: el texto avanza hacia abajo.", 2: "Esa línea ya la leyó. El texto sigue en la línea siguiente."},
   "Bajan y regresan <strong>al comienzo de la línea de abajo</strong>.")}"""

    s2 = f"""<p>Una <strong>oración</strong> es un grupo de palabras que expresa una <strong>idea completa</strong>. Si alguien dice «el carro rojo», todavía no hay oración: no sabemos qué pasa con el carro. «El carro rojo está estacionado» sí es una oración.</p>
<p>Toda oración tiene dos partes:</p>
<div class="leyenda-sp"><span><span class="suj">Sujeto</span> (subrayado recto): ¿<strong>quién</strong> o <strong>qué</strong>?</span><span><span class="pred">Predicado</span> (subrayado ondulado): ¿<strong>qué hace</strong> o <strong>qué le pasa</strong>?</span></div>
<p class="oracion-ej"><span class="suj">El perro</span> <span class="pred">corre por el parque.</span> {LE.escuchar("El perro corre por el parque.", "Escuchar")}</p>
<p class="oracion-ej"><span class="suj">Mi vecina</span> <span class="pred">canta los domingos.</span> {LE.escuchar("Mi vecina canta los domingos.", "Escuchar")}</p>
<p class="oracion-ej"><span class="suj">Los estudiantes de la noche</span> <span class="pred">estudian con muchas ganas.</span> {LE.escuchar("Los estudiantes de la noche estudian con muchas ganas.", "Escuchar")}</p>
{C.tabla("Más ejemplos de sujeto y predicado", ["Sujeto (¿quién o qué?)", "Predicado (¿qué hace o qué le pasa?)"],
         [["Mi mamá", "prepara arroz con pollo los domingos."], ["El profesor", "explica con paciencia."], ["Nosotros", "aprendemos cosas nuevas cada día."],
          ["La lluvia", "cayó toda la tarde."], ["Usted", "va a aprobar este examen."]])}
{C.ejemplo("Ejemplo · Cómo encontrar el sujeto y el predicado", [
    ("1", "Lea la oración: <em>Mi hermano trabaja de noche.</em>"),
    ("2", "Pregunte por la acción: ¿qué se hace? <em>Trabaja de noche</em>. Ese es el <span class=\"pred\">predicado</span>."),
    ("3", "Pregunte quién lo hace: ¿quién trabaja de noche? <em>Mi hermano</em>. Ese es el <span class=\"suj\">sujeto</span>.")],
    "<span class=\"suj\">Mi hermano</span> <span class=\"pred\">trabaja de noche.</span>")}
{C.caja("ojo", "El sujeto escondido", "<p>A veces el sujeto no está escrito porque se entiende por el verbo: <em>Estudio todos los días</em>. ¿Quién estudia? <strong>Yo</strong>, aunque no se diga. A ese sujeto se le llama <strong>sujeto tácito</strong> (sobreentendido). En español es muy común; en inglés, casi nunca.</p>")}
{P("Compruebe", "¿Cuál es el <strong>sujeto</strong> de esta oración?<br><em>La lluvia cayó toda la tarde.</em>", ["La lluvia", "cayó toda la tarde", "toda la tarde"], 0,
   {1: "Eso es lo que pasó: el predicado. ¿Quién o qué cayó?", 2: "Eso dice cuándo. ¿Qué cayó toda la tarde?"}, "El sujeto es <span class=\"suj\">La lluvia</span>: es lo que cayó.")}
{P("Compruebe", "¿Cuál de estos grupos de palabras <strong>es</strong> una oración?", ["La casa grande de la esquina", "La casa de la esquina está en venta.", "Con mucho cuidado"], 1,
   {0: "Dice qué cosa, pero no qué pasa con ella. ¿Falta el predicado?", 2: "No dice quién ni qué hace."}, "<em>La casa de la esquina está en venta.</em> tiene sujeto (la casa de la esquina) y predicado (está en venta).")}"""

    S = ["El gato negro", "Mi hermana", "Los niños", "El sol", "Mis amigos"]
    Pr = ["duerme en el sofá.", "cocina muy sabroso.", "juegan en el parque.", "brilla en el cielo.", "llegan tarde."]
    ok = {"0": [0, 1, 3], "1": [0, 1, 3], "2": [2, 4], "3": [0, 1, 3], "4": [2, 4]}
    s3 = f"""<p>Ahora arme usted las oraciones. Elija primero un <strong>sujeto</strong> y después un <strong>predicado</strong>, y pulse <strong>Comprobar</strong>. Lea en voz alta cada oración que forme. Algunas combinaciones salen graciosas («el sol cocina muy sabroso»), pero están bien construidas; otras no suenan bien porque el verbo no concuerda con el sujeto.</p>
<div class="armar" data-suj='{json.dumps(S, ensure_ascii=False)}' data-pred='{json.dumps(Pr, ensure_ascii=False)}' data-ok='{json.dumps(ok)}'>
<p><strong>Sujetos:</strong></p><div class="armar-suj" role="group" aria-label="Sujetos"></div>
<p><strong>Predicados:</strong></p><div class="armar-pred" role="group" aria-label="Predicados"></div>
<p><strong>Su oración:</strong></p><p class="armar-frase" aria-live="polite"></p>
<p><button type="button" class="btn armar-comprobar">Comprobar</button> <button type="button" class="btn-sec armar-limpiar">Limpiar</button></p>
<div class="fb" role="status" aria-live="polite"></div>
<p><strong>Oraciones que ya armó:</strong></p><ul class="armar-lista"></ul>
</div>
{C.caja("tip", "Versión en papel", "<p>Corte diez tarjetas. En cinco escriba sujetos (<em>Mi abuela, El autobús, Mis amigos…</em>) y en las otras cinco, predicados (<em>llega tarde, ríen mucho…</em>). Mézclelas, forme oraciones y léalas en voz alta. Si alguien de su casa quiere jugar, háganlo por turnos.</p>")}"""

    s4 = f"""<p>Al escribir, cada oración empieza con <strong>mayúscula</strong> y termina con <strong>punto</strong>. Así el lector sabe dónde empieza y dónde termina cada idea. Sin esas marcas, el texto se vuelve una cadena de palabras difícil de seguir:</p>
<p class="oracion-ej">mi perro duerme junto a la puerta come dos veces al día sale al parque todas las tardes</p>
<p>Para separarlo, léalo en voz alta y pregúntese en cada parada: ¿ya dije quién y qué hace? Ahí termina una oración.</p>
<p class="oracion-ej"><strong>M</strong>i perro duerme junto a la puerta<strong>.</strong> <strong>C</strong>ome dos veces al día<strong>.</strong> <strong>S</strong>ale al parque todas las tardes<strong>.</strong></p>
{C.caja("tip", "Sujeto escondido otra vez", "<p>En <em>Come dos veces al día</em> no aparece el sujeto, pero se entiende: <strong>él</strong> (el perro). Es una oración completa con sujeto tácito.</p>")}
{P("Compruebe", "¿Cuántas oraciones hay en este texto?<br><em>hoy llueve sobre la ciudad las calles se llenan de charcos la gente camina con paraguas</em>", ["Una", "Dos", "Tres"], 2,
   {0: "Busque cuántas veces se dice quién y qué hace. ¿Hay una sola idea?", 1: "Cuente otra vez: la ciudad, las calles, la gente…"},
   "Tres: <em>Hoy llueve sobre la ciudad. Las calles se llenan de charcos. La gente camina con paraguas.</em>")}
<p>En la <a href="{C.prac(N)}#limites">página de práctica</a> tiene doce párrafos para marcar dónde empieza cada oración.</p>"""

    secciones = [("s1", "La dirección de la lectura", s1), ("s2", "¿Qué es una oración? Sujeto y predicado", s2),
                 ("s3", "Práctica: arme sus propias oraciones", s3), ("s4", "Mayúscula al inicio, punto al final", s4)]
    tarea = [("Diez oraciones sobre mi día.", "Escriba diez oraciones sobre lo que hace en un día normal (<em>Mi hijo se levanta a las siete.</em>). Cada una empieza con mayúscula y termina con punto."),
             ("Sujeto y predicado.", "En cada una de sus diez oraciones, subraye el sujeto con una raya recta y el predicado con una raya ondulada."),
             ("¿Oración o no?", "Copie estos grupos de palabras y escriba al lado si son oración o no. Cuando no lo sean, complételos: <em>La tienda de la esquina · Mi jefe llegó temprano · Con mucho cuidado · El bebé duerme</em>."),
             ("Lectura con guía.", "Lea en voz alta un texto corto de su vida diaria pasando el dedo debajo de cada línea. Hágalo dos veces; la segunda, intente no detenerse.")]
    quiz = [
        ("En español, ¿en qué dirección leemos cada línea?", ["De derecha a izquierda", "De izquierda a derecha", "De abajo arriba"], 1, {0: "Así se lee el árabe, no el español.", 2: "Las líneas se leen de arriba abajo, y cada línea, de un lado al otro."}, "<strong>De izquierda a derecha.</strong>"),
        ("¿Qué es una oración?", ["Una sola palabra importante", "Una lista de palabras sueltas", "Un grupo de palabras que expresa una idea completa"], 2, {0: "Una palabra sola casi nunca dice quién y qué pasa.", 1: "Sueltas no forman una idea."}, "Una oración expresa una <strong>idea completa</strong>."),
        ("¿Cuál de estos grupos de palabras es una oración?", ["El carro rojo", "El carro rojo está estacionado.", "Con el carro rojo"], 1, {0: "Falta decir qué pasa con el carro.", 2: "No dice quién ni qué hace."}, "<em>El carro rojo está estacionado.</em>"),
        ("¿Cuál <strong>no</strong> es una oración?", ["Mi hermano trabaja de noche.", "La lluvia cayó toda la tarde.", "La casa grande de la esquina"], 2, {0: "Tiene sujeto (mi hermano) y predicado (trabaja de noche).", 1: "Tiene sujeto (la lluvia) y predicado (cayó toda la tarde)."}, "<em>La casa grande de la esquina</em> no dice qué pasa con la casa."),
        ("¿A qué pregunta responde el sujeto?", ["¿Quién o qué?", "¿Cuándo?", "¿Qué hace o qué le pasa?"], 0, {1: "Eso lo dicen palabras como hoy o mañana.", 2: "Esa pregunta es la del predicado."}, "El sujeto responde <strong>¿quién o qué?</strong>"),
        ("¿A qué pregunta responde el predicado?", ["¿Dónde?", "¿Qué hace o qué le pasa?", "¿Quién o qué?"], 1, {0: "El lugar puede estar en el predicado, pero el predicado dice más.", 2: "Esa pregunta es la del sujeto."}, "El predicado responde <strong>¿qué hace o qué le pasa?</strong>"),
        ("¿Cuál es el sujeto?<br><em>Mi vecina canta los domingos.</em>", ["Mi vecina", "canta", "los domingos"], 0, {1: "Canta es la acción. ¿Quién canta?", 2: "Eso dice cuándo."}, "<span class=\"suj\">Mi vecina</span>."),
        ("¿Cuál es el predicado?<br><em>Los estudiantes de la noche estudian con muchas ganas.</em>", ["Los estudiantes", "estudian con muchas ganas", "de la noche"], 1, {0: "Ese es el sujeto (y está incompleto).", 2: "De la noche es parte del sujeto: dice qué estudiantes."}, "<span class=\"pred\">estudian con muchas ganas</span>."),
        ("¿Qué predicado completa mejor la oración?<br><em>El sol ___</em>", ["brilla en el cielo.", "juegan en el parque.", "duermen en el sofá."], 0, {1: "El sol es uno solo; juegan es para varios.", 2: "Duermen es para varios."}, "<em>El sol brilla en el cielo.</em> Un sujeto, un verbo en singular."),
        ("¿Qué sujeto completa mejor la oración?<br><em>___ juegan en el parque.</em>", ["El niño", "Los niños", "Mi hermana"], 1, {0: "Juegan es para varios; el niño es uno.", 2: "Mi hermana es una sola persona."}, "<em>Los niños juegan en el parque.</em>"),
        ("En «Estudio todos los días», ¿cuál es el sujeto?", ["todos los días", "Estudio", "yo (aunque no está escrito)"], 2, {0: "Eso dice cuándo.", 1: "Estudio es el verbo, la acción."}, "El sujeto es <strong>yo</strong>: es un sujeto tácito."),
        ("¿Cuántas oraciones hay?<br><em>Espero el autobús en la esquina. El viaje dura media hora.</em>", ["Una", "Dos", "Tres"], 1, {0: "Cuente los puntos y las mayúsculas.", 2: "Hay solo dos ideas, cada una con su punto."}, "Dos: cada una empieza con mayúscula y termina con punto."),
    ]
    filas = [
        ("Seguir la dirección de la lectura", "Leo de izquierda a derecha y bajo a la línea siguiente sin perderme.", "A veces me salto una línea.", "Me pierdo entre líneas (<a href=\"#s1\">repase la sección 1</a>)."),
        ("Reconocer el sujeto y el predicado", "Encuentro el sujeto y el predicado en cualquier oración sencilla, también el sujeto tácito.", "Los encuentro cuando el sujeto va al principio.", "No los distingo (<a href=\"#s2\">repase la sección 2</a>)."),
        ("Marcar los límites de la oración", "Separo un párrafo en oraciones con mayúscula y punto.", "Me equivoco cuando el sujeto está escondido.", "No sé dónde termina cada oración (<a href=\"#s4\">repase la sección 4</a>)."),
    ]
    cierre = ("<p>Ya sabe hacia dónde se mueven los ojos al leer y de qué partes está hecha una oración. Esa idea, que cada oración dice <em>quién</em> y <em>qué hace</em>, va a volver en el Tema 3, cuando distinga las oraciones completas de los fragmentos.</p>"
              "<p>En la próxima lección dará el paso que une todo: leer un texto completo en voz alta con precisión, ritmo y expresión.</p>")
    glosario = [("Oración", "Grupo de palabras que expresa una idea completa; empieza con mayúscula y termina con punto."),
                ("Sujeto", "La parte de la oración que dice quién o qué."), ("Predicado", "La parte de la oración que dice qué hace o qué le pasa al sujeto."),
                ("Sujeto tácito", "Sujeto que no está escrito pero se entiende por el verbo: <em>(Yo) estudio</em>."),
                ("Concordancia", "Acuerdo entre el sujeto y el verbo: uno → <em>juega</em>; varios → <em>juegan</em>.")]
    conexion = ("<p>Leer es como caminar: nadie nace sabiéndolo, pero cuando se aprende a llevar bien los pies (o los ojos), no se olvida. En esta lección verá dos cosas que parecen pequeñas y son la base de todo: hacia dónde miran los ojos al leer y de qué está hecha una oración.</p>"
                "<p><strong>Lo que necesita:</strong> su cuaderno, dos lápices o resaltadores de colores distintos y el volumen activado.</p>")
    estd = LE.estandares([], base=["L.2.2", "L.1.2", "L.2.1"], fund=["RF.1"])
    return C.pagina_leccion(N, LE.titulo(N), "Los ojos van de izquierda a derecha; cada oración dice quién y qué hace.",
                            ["Fundamentos de lectura", "L.2.2 · Límites de la oración"],
                            ["<strong>Seguir</strong> el texto con la vista de izquierda a derecha y de arriba abajo.",
                             "<strong>Reconocer</strong> el sujeto (¿quién o qué?) y el predicado (¿qué hace o qué le pasa?) de una oración, también el sujeto tácito.",
                             "<strong>Construir</strong> oraciones completas y leerlas en voz alta.",
                             "<strong>Marcar</strong> dónde empieza y dónde termina cada oración de un párrafo."],
                            estd, conexion, secciones, tarea, quiz, filas, cierre, ("1-3", LE.titulo("1-3")), glosario, P)


# ---------------------------------------------------------------- práctica
def banco_oracion():
    si = ["El bebé duerme.", "Mi jefe llegó temprano.", "La tienda abre a las ocho.", "Los niños juegan en el patio.", "Llueve.", "Trabajo de noche.",
          "El autobús llegó tarde.", "Mi hija estudia enfermería.", "Ana cocina los domingos.", "Las clases empiezan en enero."]
    no = ["La tienda de la esquina", "Con mucho cuidado", "Después del trabajo", "El carro rojo de mi vecino", "Porque estaba cansado", "En la mesa de la cocina",
          "Mi hermana y su esposo", "Todos los días por la mañana", "Muy temprano", "Para la clase de mañana"]
    b = []
    for x in si:
        b.append({"enun": f"¿Es una oración completa?<br><strong>{x}</strong>", "ops": ["Sí, es una oración", "No, le falta algo"], "ok": 0, "enOrden": True,
                  "exp": "Dice quién o qué y qué hace o qué le pasa." + (" El sujeto está escondido en el verbo." if x in ("Trabajo de noche.",) else "") + (" Es una oración de una sola palabra: el verbo dice todo." if x == "Llueve." else "")})
    for x in no:
        b.append({"enun": f"¿Es una oración completa?<br><strong>{x}</strong>", "ops": ["Sí, es una oración", "No, le falta algo"], "ok": 1, "enOrden": True,
                  "exp": "No es una idea completa: falta decir quién o qué pasa. Por ejemplo: <em>" + {
                      "La tienda de la esquina": "La tienda de la esquina cerró.", "Con mucho cuidado": "Abrí la caja con mucho cuidado.", "Después del trabajo": "Después del trabajo voy a clase.",
                      "El carro rojo de mi vecino": "El carro rojo de mi vecino es nuevo.", "Porque estaba cansado": "Me dormí porque estaba cansado.", "En la mesa de la cocina": "Las llaves están en la mesa de la cocina.",
                      "Mi hermana y su esposo": "Mi hermana y su esposo viven en Texas.", "Todos los días por la mañana": "Camino todos los días por la mañana.",
                      "Muy temprano": "Me levanto muy temprano.", "Para la clase de mañana": "Estudio para la clase de mañana."}[x] + "</em>"})
    return b


def banco_partes():
    datos = [("El perro", "ladra toda la noche."), ("Mi mamá", "prepara tamales en diciembre."), ("La maestra", "explica la lección."), ("Los vecinos", "riegan las plantas."),
             ("El tren de las siete", "llegó tarde."), ("Mi primo Luis", "trabaja en una fábrica."), ("La clínica del barrio", "abre los sábados."), ("Nosotros", "estudiamos juntos."),
             ("El café", "está muy caliente."), ("Las fresas del mercado", "cuestan poco.")]
    b = []
    for i, (s, p) in enumerate(datos):
        otro = datos[(i + 3) % len(datos)]
        pal = p.split(" ")
        b.append({"enun": f"¿Cuál es el <strong>sujeto</strong>?<br><em>{s} {p}</em>", "ops": [s, p.rstrip("."), pal[0]], "ok": 0,
                  "pista": "Busque la acción y pregunte: ¿quién o qué lo hace?", "exp": f"<span class=\"suj\">{s}</span> es quien {pal[0]}."})
        b.append({"enun": f"¿Cuál es el <strong>predicado</strong>?<br><em>{s} {p}</em>", "ops": [p.rstrip("."), s, otro[1].rstrip(".")], "ok": 0,
                  "pista": "El predicado dice qué hace o qué le pasa al sujeto, y está en esta misma oración.", "exp": f"<span class=\"pred\">{p.rstrip('.')}</span>: es lo que hace o le pasa a {s[0].lower() + s[1:]}."})
    return b


def banco_concuerda():
    datos = [("El niño", ["juega en el parque.", "juegan en el parque."], 0), ("Los niños", ["juega en el parque.", "juegan en el parque."], 1),
             ("Mi hermana", ["trabaja en un hospital.", "trabajan en un hospital."], 0), ("Mis hermanas", ["trabaja en un hospital.", "trabajan en un hospital."], 1),
             ("El autobús", ["llega a las seis.", "llegan a las seis."], 0), ("Los autobuses", ["llega a las seis.", "llegan a las seis."], 1),
             ("Nosotros", ["estudia de noche.", "estudiamos de noche."], 1), ("Yo", ["trabajo los sábados.", "trabaja los sábados."], 0)]
    return [{"enun": f"¿Qué predicado va con este sujeto?<br><strong>{s} ___</strong>", "ops": o, "ok": k, "enOrden": True,
             "exp": f"<em>{s} {o[k]}</em> El verbo concuerda con el sujeto."} for s, o, k in datos]


def practica():
    mods = [
        ("oracion", "¿Es una oración completa?", C.om("m1", "Lea en voz alta y pregúntese: ¿dice quién o qué, y qué hace o qué le pasa?")),
        ("sujeto-predicado", "Sujeto y predicado", C.om("m2", "Primero busque la acción. Después pregunte quién la hace.")),
        ("concordancia", "¿Qué predicado va?", C.om("m3", "Si el sujeto es uno, el verbo va en singular; si son varios, en plural.")),
        ("limites", "¿Dónde empieza cada oración?", '      <p>Este párrafo perdió sus puntos y sus mayúsculas. Toque la <strong>primera palabra de cada oración</strong> (menos la primera del párrafo, que ya está marcada): la página le pone la mayúscula y el punto que va antes. Si se equivoca, toque otra vez la palabra para quitar la marca. Después pulse <strong>Comprobar</strong>.</p>\n' + C.huecos("m4")),
    ]
    js = (C.js_datos("ORA", banco_oracion()) + C.js_datos("PAR", banco_partes()) + C.js_datos("CON", banco_concuerda()) +
          C.js_datos("LIM", [{"titulo": a, "correcto": b} for a, b in PARRAFOS]) +
          'creaBanco("m1", ORA);\ncreaBanco("m2", PAR);\ncreaBanco("m3", CON);\n')
    html = C.pagina_practica(N, LE.titulo(N), "Cuatro actividades · los ejercicios cambian cada vez · dos intentos en cada uno", mods, js)
    # creaLimites está en /rla/leng.js, que se carga después: se llama al terminar de cargar la página
    return html.replace("iniciaNavegacion();", 'iniciaNavegacion();\ndocument.addEventListener("DOMContentLoaded", function () { creaLimites("m4", LIM); });')


if __name__ == "__main__":
    LE.construye(N, leccion, practica, horas="Unas 3 horas")
