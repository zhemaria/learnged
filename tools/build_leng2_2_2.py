# -*- coding: utf-8 -*-
"""LearnGED · Artes del lenguaje (español) · Nivel 2 · Lección 2.2 · Pronombres reflexivos y concordancia.
Fuente: clases_leng2/clase_2-2.html (GEDparaHispanos) y gramatica/n2-l2-2.html, adaptadas al marco de LearnGED.
Uso: python3 tools/build_leng2_2_2.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import leng_es as LE
from leng_es import C

LE.nivel(2)
N = "2-2"
PRON = ["me", "te", "se", "nos"]
REF = [("Yo ___ despierto con la alarma.", "me", "yo → me."), ("Mi abuela ___ sienta junto a la ventana.", "se", "ella → se."),
       ("Tú ___ cepillas los dientes después de comer.", "te", "tú → te."), ("Mis vecinos ___ quejan del ruido.", "se", "ellos → se."),
       ("Mi esposo y yo ___ acostamos a las diez.", "nos", "mi esposo y yo = nosotros → nos."), ("Ustedes ___ preparan muy bien para las entrevistas.", "se", "ustedes → se."),
       ("¿Por qué ___ vas tan temprano?", "te", "Se le habla a «tú»: te vas."), ("Nosotras ___ vestimos para la fiesta.", "nos", "nosotras → nos."),
       ("Voy a duchar___ antes de salir.", "me", "Yo voy a ducharme: el pronombre pegado también concuerda."), ("Estamos preparándo___ para el examen.", "nos", "Nosotros: preparándonos."),
       ("Juan, ¡siénta___ aquí!", "te", "Orden a «tú»: siéntate."), ("Señora, ¿quiere sentar___?", "se", "A «usted» → se: sentarse."),
       ("Niños, ¡no ___ levanten de la mesa!", "se", "Orden negativa a «ustedes»: no se levanten."), ("Cuando ___ enfermo, llamo al médico.", "me", "Cuando yo me enfermo."),
       ("Mi hija ___ está peinando en el baño.", "se", "ella → se está peinando."), ("¿A qué hora ___ levantas los sábados?", "te", "tú → te levantas.")]
CONC = [("Las paredes del cuarto están ___.", ["pintadas", "pintados", "pintada"], "paredes: femenino plural."),
        ("El agua del vaso está ___.", ["limpia", "limpio", "limpios"], "agua es femenina aunque lleve el."),
        ("Mi papá y mi tío ___ en una fábrica.", ["trabajan", "trabaja", "trabajamos"], "Sujeto doble: plural."),
        ("Mi hermana y yo ___ al mercado los sábados.", ["vamos", "van", "va"], "mi hermana y yo = nosotros."),
        ("El equipo de mi hijo ___ el partido.", ["ganó", "ganaron", "ganamos"], "equipo es colectivo: singular."),
        ("Los problemas de matemáticas son ___.", ["difíciles", "difícil", "dificilas"], "problemas: plural."),
        ("El mapa de la ciudad es muy ___.", ["viejo", "vieja", "viejas"], "mapa es masculino aunque termine en -a."),
        ("La mano me duele: la tengo ___.", ["hinchada", "hinchado", "hinchados"], "mano es femenina aunque termine en -o."),
        ("El águila ___ voló sobre el lago.", ["blanca", "blanco", "blancas"], "águila es femenina: el águila blanca."),
        ("Mis compañeras de clase son muy ___.", ["amables", "amable", "amablas"], "plural; amable no cambia de género."),
        ("La gente del mercado ___ muy temprano.", ["llega", "llegan", "llegamos"], "gente: singular."),
        ("Tú y tu hermano ___ mucho.", ["se parecen", "te pareces", "nos parecemos"], "tú y tu hermano = ustedes → se parecen."),
        ("Las flores que compraste son ___.", ["preciosas", "preciosos", "preciosa"], "flores: femenino plural."),
        ("Mi familia ___ en Chicago desde 2010.", ["vive", "viven", "vivimos"], "familia: singular."),
        ("Los días de invierno son ___.", ["cortos", "cortas", "corto"], "días: masculino plural."),
        ("El hacha ___ está en el garaje.", ["nueva", "nuevo", "nuevas"], "hacha es femenina: el hacha nueva.")]
BIEN = [(["Me lavo las manos antes de comer.", "Me lavo mis manos antes de comer.", "Se lavo las manos antes de comer."], "Con verbo reflexivo, las partes del cuerpo llevan artículo."),
        (["Mis padres se levantan temprano.", "Mis padres se levanta temprano.", "Mis padres nos levantan temprano."], "padres: plural → se levantan."),
        (["Voy a acostarme temprano.", "Voy a acostarse temprano.", "Voy a me acostar temprano."], "yo → acostarme."),
        (["¡Levántate, que es tarde!", "¡Levantate, que es tarde!", "¡Te levanta, que es tarde!"], "Orden afirmativa: pronombre pegado y tilde."),
        (["El agua está fría.", "El agua está frío.", "La agua está fría."], "el agua, pero fría."),
        (["Mi esposo y yo nos fuimos al parque.", "Mi esposo y yo se fuimos al parque.", "Mi esposo y yo me fui al parque."], "mi esposo y yo = nosotros."),
        (["La gente está contenta con el huerto.", "La gente están contentos con el huerto.", "La gente están contenta con el huerto."], "gente: singular y femenino."),
        (["Estoy vistiéndome para la boda.", "Estoy vistiendome para la boda.", "Estoy me vistiendo para la boda."], "Pronombre pegado al gerundio: lleva tilde."),
        (["No te preocupes por eso.", "No preocúpate por eso.", "No te preocupas por eso."], "Orden negativa: el pronombre va antes."),
        (["Las sillas nuevas son cómodas.", "Las sillas nuevos son cómodas.", "Las sillas nuevas es cómodas."], "sillas: femenino plural, y el verbo en plural."),
        (["Mi hija se peina sola.", "Mi hija me peina sola.", "Mi hija se peinan sola."], "ella → se peina."),
        (["Siéntense, por favor.", "Sientense, por favor.", "Se sienten, por favor."], "Orden afirmativa a «ustedes»: siéntense."),
        (["El problema fue difícil.", "El problema fue difícila.", "La problema fue difícil."], "problema es masculino."),
        (["¿Te acuerdas de mi nombre?", "¿Se acuerdas de mi nombre?", "¿Te acuerda de mi nombre?"], "tú → te acuerdas.")]
ROSA = ["Los lunes, Rosa se despierta a las cinco y media. Primero se levanta sin hacer ruido para no despertar a su esposo. Se baña rápidamente, se viste y se peina frente al espejo.",
        "Después despierta a sus hijos, que siempre se quejan porque tienen sueño.", "—¡Levántense, que ya es tarde! —les dice.",
        "Mientras los niños se lavan la cara y se cepillan los dientes, Rosa prepara el desayuno. A las siete, todos se sientan a la mesa. Luego Rosa lleva a los niños a la escuela y se va al trabajo.",
        "Por la noche, cuando todos se acuestan, ella se sienta un rato en el sofá y lee un libro. Es su momento favorito del día."]


def leccion():
    P = C.Practicas()
    s1 = f"""<p>Piense en lo que hace cada mañana: se despierta, se levanta, se baña, se viste. Esas acciones las hace sobre usted mismo, y por eso el español las dice con una palabrita delante: <strong>me, te, se, nos</strong>. Son los <strong>pronombres reflexivos</strong>.</p>
<p>Un verbo es reflexivo cuando la acción vuelve a la misma persona que la hace, como un reflejo en el espejo. En el diccionario aparece con <strong>-se</strong> al final: <em>levantarse, bañarse, vestirse, peinarse, acostarse, sentarse</em>.</p>
{C.tabla("Pronombres reflexivos con el verbo levantarse", ["Persona", "Pronombre", "Ejemplo"],
         [["yo", "me", "me levanto"], ["tú", "te", "te levantas"], ["él, ella, usted", "se", "se levanta"], ["nosotros, nosotras", "nos", "nos levantamos"], ["ellos, ellas, ustedes", "se", "se levantan"]])}
{C.caja("tip", "¿Y «os»?", "<p>En España, para hablar a varias personas en confianza se usa <em>vosotros os levantáis</em>. En América se dice <em>ustedes se levantan</em>, que es la forma que usamos en el curso.</p>")}
{P("Compruebe", "Mi esposo y yo ___ acostamos a las diez.", PRON, 3, {0: "El sujeto no es solo «yo».", 2: "Mi esposo y yo = nosotros."}, "<strong>nos</strong>: mi esposo y yo = nosotros.")}
<h3>¿Con pronombre o sin él?</h3>
<p>Muchos verbos se usan de las dos maneras. La diferencia está en quién recibe la acción:</p>
{C.tabla("El mismo verbo con y sin pronombre reflexivo", ["La acción va hacia otro", "La acción vuelve a mí"],
         [["Lavo el carro.", "Me lavo las manos."], ["Baño al bebé.", "Me baño."], ["Despierto a mi hijo.", "Me despierto."], ["Siento a los niños a la mesa.", "Me siento a la mesa."]])}
{C.caja("ojo", "Las partes del cuerpo", "<p>Con un verbo reflexivo, el español usa <strong>el, la, los, las</strong>, no <em>mi, tu, su</em>: <em>Me lavo <strong>las</strong> manos</em>, <em>Me corté <strong>el</strong> dedo</em>. «Lavo mis manos» es una traducción directa del inglés.</p>")}
{P("Compruebe", "¿Cuál está bien escrita?", ["Me lavo mis manos.", "Me lavo las manos."], 1, {0: "Con verbo reflexivo, la parte del cuerpo lleva artículo."}, "<strong>Me lavo las manos.</strong>")}"""

    s2 = f"""{C.tabla("Dónde va el pronombre", ["Con…", "El pronombre va…", "Ejemplos"],
         [["Un verbo conjugado", "Antes, separado.", "Me visto. · No te preocupes."], ["Un infinitivo (-ar, -er, -ir)", "Pegado al final, o antes del verbo que lo acompaña.", "Voy a acostarme. = Me voy a acostar."],
          ["Un gerundio (-ando, -iendo)", "Pegado al final, o antes del verbo estar.", "Estoy vistiéndome. = Me estoy vistiendo."], ["Una orden afirmativa", "Pegado al final, siempre.", "¡Levántate! · ¡Siéntense, por favor!"],
          ["Una orden negativa", "Antes, siempre.", "¡No te levantes! · No se sienten ahí."]])}
{C.caja("tip", "Aparece una tilde", "<p>Al pegar el pronombre, la palabra crece y muchas veces necesita tilde para conservar su sonido fuerte: <em>vistiendo → vistiéndome</em>, <em>levanta → levántate</em>, <em>preparando → preparándonos</em>. Con el infinitivo no hace falta: <em>bañarme, vestirse</em>.</p>")}
{C.caja("ojo", "El pronombre pegado también concuerda", "<p><em>Yo voy a bañar<strong>me</strong></em>, no «yo voy a bañarse». <em>Nosotros vamos a sentar<strong>nos</strong></em>.</p>")}
{P("Compruebe", "¿Cuál está bien escrita?", ["¡No te levantes!", "¡No levántate!"], 0, {1: "En la orden negativa, el pronombre va antes."}, "<strong>¡No te levantes!</strong>: orden negativa, pronombre antes.")}
{P("Compruebe", "¿Cuál está bien escrita?", ["Estoy vistiendome.", "Estoy vistiéndome."], 1, {0: "Al pegar el pronombre, la palabra necesita tilde."}, "<strong>vistiéndome</strong>, con tilde.")}"""

    s3 = f"""<p>En el Nivel 1 aprendió la regla de oro: el sustantivo y el adjetivo van de acuerdo en género y en número. Ahora la extendemos a toda la oración:</p>
<ul><li><strong>Artículo, sustantivo y adjetivo:</strong> <em>las sillas nuevas, el carro viejo</em>.</li>
<li><strong>Sujeto y verbo:</strong> el verbo va en la misma persona y número que el sujeto: <em>Mi hijo trabaja · Mis hijos trabajan</em>.</li>
<li><strong>Sujeto doble:</strong> dos sujetos unidos por <em>y</em> llevan el verbo en plural: <em>Mi tía y mi prima viven aquí</em>. Si uno de ellos es <em>yo</em>, el verbo va con <em>nosotros</em>: <em>Mi hermana y yo nos levantamos temprano</em>.</li>
<li><strong>Colectivos</strong> (Lección 2.1): <em>La gente está contenta</em>.</li></ul>
{C.caja("ojo", "La trampa de «el agua»", "<p>Las palabras femeninas que empiezan con <em>a</em> o <em>ha</em> con fuerza usan <strong>el</strong> en singular para que suene mejor: <em>el agua, el águila, el hacha</em>. Pero siguen siendo femeninas, y el adjetivo va en femenino: <em>el agua fría, el hacha afilada</em>. En plural vuelve <em>las</em>: <em>las aguas frías</em>.</p>")}
{C.caja("tip", "Más trampas de género", "<p>Algunas palabras no siguen la pista de la -o y la -a: <em>el mapa, el problema, el día</em> son masculinas; <em>la mano, la foto, la radio</em> son femeninas. El adjetivo sigue al género real: <em>el problema difícil, la mano hinchada</em>.</p>")}
{P("Compruebe", "El agua del vaso está ___.", ["fría", "frío"], 0, {1: "agua es femenina, aunque lleve el."}, "<strong>fría</strong>: el agua es femenina.")}
{P("Compruebe", "Mi papá y mi tío ___ en una fábrica.", ["trabaja", "trabajan"], 1, {0: "Son dos sujetos: el verbo va en plural."}, "<strong>trabajan</strong>: sujeto doble, plural.")}
<h3>Lectura: «Los lunes de Rosa»</h3>
<p>Lea el texto en voz alta. En su cuaderno, copie todos los verbos que llevan pronombre reflexivo y escriba su infinitivo (por ejemplo: <em>se despierta → despertarse</em>). Atención: dos verbos se parecen, pero no son reflexivos.</p>
{LE.escuchar(" ".join(ROSA), "Escuchar el texto")}
<div class="texto-lectura">{"".join(f"<p>{p}</p>" for p in ROSA)}</div>
<details class="caja caja-tip"><summary><strong>Ver las respuestas</strong></summary>
<p><strong>Reflexivos:</strong> despertarse, levantarse, bañarse, vestirse, peinarse, quejarse, levantarse (<em>Levántense</em>: orden afirmativa, pronombre pegado y tilde), lavarse, cepillarse, sentarse, irse, acostarse.</p>
<p><strong>Sin pronombre:</strong> <em>despertar a su esposo</em> y <em>despierta a sus hijos</em>: la acción va hacia otra persona.</p>
<p>Fíjese también en <em>se lavan la cara</em> y <em>se cepillan los dientes</em>: con artículo, no con <em>su</em>.</p></details>
<div class="caja caja-tip"><span class="etiqueta et-verde">Actividad · mi día</span>
<p>Escriba un párrafo de 6 a 8 oraciones sobre su rutina en un día de trabajo o de estudio. Use al menos cinco verbos reflexivos distintos y una orden (lo que le dice a alguien de su casa por la mañana). Después revíselo:</p>
<ul><li>¿Cada pronombre va de acuerdo con la persona? (<em>yo me, nosotros nos</em>…)</li><li>¿Los pronombres pegados al gerundio o a la orden tienen su tilde?</li>
<li>¿Usó <em>el, la, los, las</em> con las partes del cuerpo?</li><li>¿Los verbos concuerdan con su sujeto, también los sujetos dobles?</li></ul>
<p>Si tiene con quién practicar, pregúntele a alguien de su familia por su rutina («¿A qué hora te levantas?») y escriba sus respuestas con <em>se</em>: «Mi hija se levanta a las siete».</p></div>"""

    secciones = [("s1", "Los pronombres reflexivos", s1), ("s2", "Dónde va el pronombre", s2), ("s3", "La concordancia en toda la oración", s3)]
    tarea = [("Con y sin.", "Escriba cuatro pares de oraciones con el mismo verbo, una reflexiva y otra no: <em>Peino a mi hija / Me peino</em>."),
             ("Dos posiciones.", "Reescriba cada oración con el pronombre en la otra posición: <em>Me voy a duchar · Estamos preparándonos · Te tienes que sentar</em>."),
             ("Corrija.", "«Mis padres se levanta temprano», «Yo voy a acostarse», «El agua está frío», «Mi esposo y yo se fuimos al parque»."
              "<details><summary>Ver las respuestas</summary><p>Voy a ducharme · Nos estamos preparando · Tienes que sentarte.</p><p>Mis padres se levantan temprano. · Yo voy a acostarme. · El agua está fría. · Mi esposo y yo nos fuimos al parque.</p></details>")]
    quiz = [
        ("Nosotros ___ levantamos a las seis.", PRON, 3, {0: "El sujeto es nosotros.", 2: "se es para él, ella, usted, ellos o ustedes."}, "<strong>nos</strong> levantamos."),
        ("¿En qué oración el verbo <strong>no</strong> es reflexivo?", ["Baño al bebé.", "Me baño.", "Se baña."], 0, {1: "La acción vuelve a mí.", 2: "La acción vuelve a quien la hace."}, "<strong>Baño al bebé</strong>: la acción va hacia otro."),
        ("¿Cuál está bien escrita?", ["Me corté el dedo.", "Me corté mi dedo."], 0, {1: "Con verbo reflexivo, la parte del cuerpo lleva artículo."}, "<strong>Me corté el dedo.</strong>"),
        ("¿Cuál está bien escrita?", ["Voy a acostarme.", "Voy a acostarse."], 0, {1: "El sujeto es yo: me."}, "<strong>acostarme</strong>: el pronombre pegado concuerda."),
        ("¿Cuál está bien escrita?", ["¡Siéntense, por favor!", "¡Se sienten, por favor!"], 0, {1: "En la orden afirmativa, el pronombre va pegado al final."}, "<strong>Siéntense</strong>: pegado y con tilde."),
        ("Otra forma de decir <em>Me estoy vistiendo</em>:", ["Estoy vistiéndome.", "Estoy me vistiendo.", "Estoy vistiendome."], 0, {1: "El pronombre va antes de estar o pegado al gerundio.", 2: "Falta la tilde."}, "<strong>Estoy vistiéndome.</strong>"),
        ("Mi hermana y yo ___ al mercado.", ["vamos", "van", "va"], 0, {1: "Mi hermana y yo = nosotros.", 2: "Son dos sujetos."}, "<strong>vamos</strong>: mi hermana y yo = nosotros."),
        ("El agua está ___.", ["fría", "frío"], 0, {1: "agua es femenina."}, "<strong>fría</strong>."),
        ("¿Cuál está bien escrita?", ["El problema fue difícil.", "La problema fue difícil."], 0, {1: "problema es masculino."}, "<strong>El problema</strong>: masculino."),
        ("La gente del barrio ___ contenta.", ["está", "están"], 0, {1: "gente es colectivo: singular."}, "<strong>está</strong>: colectivo, singular."),
    ]
    filas = [
        ("Pronombres", "Uso me, te, se, nos según la persona y sé cuándo el verbo es reflexivo.", "Dudo con nosotros o con ustedes.", "No sé qué pronombre usar (<a href=\"#s1\">repase la sección 1</a>)."),
        ("Posición", "Coloco el pronombre con infinitivos, gerundios y órdenes, con su tilde.", "Olvido la tilde al pegarlo.", "No sé dónde va (<a href=\"#s2\">repase la sección 2</a>)."),
        ("Concordancia", "Hago concordar artículo, sustantivo, adjetivo y verbo, también con sujeto doble y «el agua».", "Me equivoco en los casos difíciles.", "No reviso la concordancia (<a href=\"#s3\">repase la sección 3</a>)."),
    ]
    cierre = "<p>Ya usa los pronombres reflexivos y revisa la concordancia de toda la oración. En la próxima lección verá los <strong>verbos regulares e irregulares</strong>.</p>"
    glosario = [("Verbo reflexivo", "Verbo cuya acción vuelve a la persona que la hace: levantarse, vestirse."), ("Pronombre reflexivo", "me, te, se, nos: acompaña al verbo reflexivo."),
                ("Concordancia", "Acuerdo de género, número y persona entre las palabras de la oración."), ("Sujeto doble", "Dos sujetos unidos por «y»; llevan el verbo en plural.")]
    conexion = ("<p>En la Lección 2.1 vio que el colectivo lleva el verbo en singular. Hoy aplicará esa misma atención a toda la oración, y conocerá unos pronombres que usa todos los días sin pensarlo.</p>"
                "<p><strong>Lo que necesita:</strong> el cuaderno.</p>")
    estd = LE.estandares(["L.1.2", "L.1.3", "L.1.7"], base=["L.1.4"])
    return C.pagina_leccion(N, LE.titulo(N), "Las acciones que vuelven a uno mismo, y todo de acuerdo.", ["Gramática", "Pronombres y concordancia"],
                            ["<strong>Usar</strong> los pronombres reflexivos me, te, se, nos.", "<strong>Colocar</strong> el pronombre con infinitivos, gerundios y órdenes.",
                             "<strong>Hacer concordar</strong> todas las palabras de la oración.", "<strong>Evitar</strong> las trampas de «el agua» y de los sujetos dobles."],
                            estd, conexion, secciones, tarea, quiz, filas, cierre, ("2-3", LE.titulo("2-3")), glosario, P)


def practica():
    re_ = [{"enun": f"<span class=\"grande\">{o.replace('___', '<u>&nbsp;?&nbsp;</u>')}</span><br>¿Qué pronombre falta?", "ops": PRON, "ok": PRON.index(p), "enOrden": True,
            "pista": "¿Quién hace la acción? Busque el sujeto o la persona a quien se le habla.", "exp": f"«{o.replace('___', p)}» · {e}"} for o, p, e in REF]
    co = [{"enun": f"<span class=\"grande\">{o.replace('___', '_____')}</span>", "ops": ops, "ok": 0, "pista": "¿Con qué palabra tiene que ir de acuerdo? Fíjese en su género y en su número.",
           "exp": f"«{o.replace('___', ops[0])}» · {e}"} for o, ops, e in CONC]
    bi = [{"enun": "¿Cuál está bien escrita?", "ops": ops, "ok": 0, "pista": "Revise el pronombre, la tilde y la concordancia.", "exp": f"«{ops[0]}» · {e}"} for ops, e in BIEN]
    mods = [("reflexivos", "Pronombres reflexivos", C.om("m1", "Elija el pronombre que falta.")),
            ("concordancia", "Concordancia", C.om("m2", "Elija la forma que va de acuerdo.")),
            ("bien-escrita", "¿Cuál está bien escrita?", C.om("m3", "Elija la versión sin errores."))]
    js = C.js_datos("RE", re_) + C.js_datos("CO", co) + C.js_datos("BI", bi) + 'creaBanco("m1", RE);\ncreaBanco("m2", CO);\ncreaBanco("m3", BI);\n'
    return C.pagina_practica(N, LE.titulo(N), "Tres actividades · los ejercicios cambian cada vez · dos intentos en cada uno", mods, js)


if __name__ == "__main__":
    LE.construye(N, leccion, practica, horas="Unas 3 horas")
