# -*- coding: utf-8 -*-
"""LearnGED · Artes del lenguaje (español) · Nivel 3 · Lección 2.3 · Vocabulario académico: sinónimos, antónimos y relaciones.
Fuente: clases_leng3/clase_2-3.html (GEDparaHispanos) y gramatica/n3-l2-3.html, adaptadas al marco de LearnGED.
Datos de la mariposa monarca: Servicio Forestal de los EE. UU. (fs.usda.gov, «Monarch Butterfly») y Servicio de Pesca y Vida
Silvestre de los EE. UU. (fws.gov, «The monarch super generation»); consultados en noviembre de 2026.
Uso: python3 tools/build_leng3_2_3.py
"""
import os, sys, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import leng_es as LE
from leng_es import C

LE.nivel(3)
N = "2-3"


def V(t):
    return f'<b class="cl-w">{t}</b>'


TEXTO = [f"Cada otoño, millones de mariposas monarca {V('emprenden')} uno de los viajes más largos del mundo de los insectos. {V('Parten')} del sureste de Canadá y del noreste de los Estados Unidos y {V('recorren')} hasta unos 4800 kilómetros hasta los bosques de oyamel del centro de México. Allí pasan el invierno agrupadas en los árboles, en {V('reposo')}.",
         f"La generación que migra es muy {V('distinta')} de las demás: mientras las mariposas del verano viven entre dos y cinco semanas, las que hacen el viaje pueden vivir hasta ocho meses. En primavera inician el regreso, pero ninguna mariposa completa sola el viaje de ida y vuelta: hacen falta tres o cuatro generaciones para volver al norte.",
         f"Los científicos {V('sostienen')} que las monarcas se orientan por el sol. También {V('advierten')} que su número ha {V('disminuido')} en las últimas décadas, en parte por la {V('pérdida')} de su hábitat. Por eso muchas personas siembran algodoncillo en sus jardines: es la única planta de la que se alimentan las orugas de la monarca."]
MAPA = [["emprenden", "comienzan, inician", "terminan, concluyen"], ["parten", "salen", "llegan"], ["recorren", "atraviesan, viajan", "—"], ["reposo", "descanso, quietud", "actividad, movimiento"],
        ["distinta", "diferente", "igual, parecida"], ["sostienen", "afirman, defienden", "niegan"], ["advierten", "alertan, avisan", "—"], ["disminuido", "reducido, bajado", "aumentado, crecido"],
        ["pérdida", "desaparición", "recuperación"]]
SI = [("El proyecto <b>concluyó</b> en diciembre.", ["terminó", "empezó", "creció"], "<em>Concluir</em> es terminar."),
      ("Los resultados fueron <b>evidentes</b> para todos.", ["claros", "dudosos", "secretos"], "<em>Evidente</em>: que se ve con claridad."),
      ("La lluvia <b>ocasionó</b> varios accidentes.", ["causó", "evitó", "redujo"], "<em>Ocasionar</em> es causar."),
      ("El número de casos <b>aumentó</b> en el invierno.", ["creció", "bajó", "se detuvo"], "<em>Aumentar</em> es crecer."),
      ("Es una idea <b>fundamental</b> del texto.", ["principal", "secundaria", "falsa"], "<em>Fundamental</em>: que sirve de base, principal."),
      ("El médico <b>analizó</b> los resultados.", ["examinó", "escondió", "imprimió"], "<em>Analizar</em> es examinar con detalle."),
      ("Los dos textos tratan un tema <b>similar</b>.", ["parecido", "opuesto", "extraño"], "<em>Similar</em> es parecido."),
      ("La empresa quiere <b>reducir</b> los gastos.", ["disminuir", "duplicar", "pagar"], "<em>Reducir</em> es hacer menor."),
      ("El autor <b>sostiene</b> una opinión clara.", ["defiende", "abandona", "esconde"], "<em>Sostener</em> una idea es defenderla."),
      ("Hubo una <b>escasez</b> de agua en el pueblo.", ["falta", "abundancia", "limpieza"], "<em>Escasez</em> es falta de algo."),
      ("El clima de la región es muy <b>árido</b>.", ["seco", "húmedo", "frío"], "<em>Árido</em>: seco, con poca agua."),
      ("Hay que <b>verificar</b> los datos antes de publicar.", ["comprobar", "borrar", "inventar"], "<em>Verificar</em> es comprobar si algo es cierto."),
      ("Fue una decisión <b>difícil</b> para la familia.", ["complicada", "sencilla", "rápida"], "<em>Difícil</em> y <em>complicada</em> son sinónimos."),
      ("El incendio <b>destruyó</b> tres casas.", ["arrasó", "construyó", "visitó"], "<em>Arrasar</em> es destruir por completo.")]
PP = [("En una carta formal: «Le escribo para ___ un permiso.»", ["solicitar", "exigir", "agarrar"], "Pedir de manera formal: <em>solicitar</em>."),
      ("«Los trabajadores ___ un salario justo; dicen que es su derecho.»", ["exigen", "piden por favor", "sugieren"], "Pedir con fuerza, como un derecho: <em>exigir</em>."),
      ("«El guardia ___ la entrada toda la noche.»", ["vigila", "observa", "mira"], "Mirar para cuidar o controlar: <em>vigilar</em>."),
      ("«El nuevo hospital se ___ con una ceremonia el lunes.»", ["inaugura", "inicia", "empieza"], "Abrir algo nuevo con un acto público: <em>inaugurar</em>."),
      ("«Las acciones de la empresa se ___ en un solo día: perdieron la mitad de su valor.»", ["desplomaron", "redujeron", "bajaron"], "Caer de golpe y mucho: <em>desplomarse</em>."),
      ("«El acusado ___ haber estado en el lugar del robo.»", ["negó", "admitió", "sostuvo"], "Decir que algo no es cierto: <em>negar</em>."),
      ("«Tras ver el video, el entrenador ___ que se había equivocado.»", ["reconoció", "negó", "advirtió"], "Aceptar algo, a su pesar: <em>reconocer</em>."),
      ("«Las autoridades ___ que el agua del río no es potable.»", ["advierten", "sugieren", "admiten"], "Avisar de un peligro: <em>advertir</em>."),
      ("«El informe ___ que podría haber más casos, pero no está claro.»", ["sugiere", "demuestra", "asegura"], "Proponer algo con poca seguridad: <em>sugerir</em>."),
      ("«La investigadora ___ su teoría con datos de veinte años.»", ["sostiene", "sospecha", "supone"], "Afirmar y defender con pruebas: <em>sostener</em>."),
      ("«El concejal ___ el alto costo del proyecto y pide explicaciones.»", ["cuestiona", "celebra", "admite"], "Mostrar duda o desacuerdo: <em>cuestionar</em>."),
      ("«El calor ___ un apagón en todo el barrio.»", ["provocó", "calmó", "sugirió"], "Causar algo repentino y negativo: <em>provocar</em>.")]
RE = [("<em>Página</em> es a <em>libro</em> como…", ["<em>ladrillo</em> es a <em>pared</em>", "<em>leer</em> es a <em>escribir</em>", "<em>libro</em> es a <em>biblioteca</em>"], "Parte y todo."),
      ("<em>Caliente</em> es a <em>frío</em> como…", ["<em>alto</em> es a <em>bajo</em>", "<em>agua</em> es a <em>hielo</em>", "<em>sol</em> es a <em>verano</em>"], "Antónimos graduales."),
      ("<em>Termómetro</em> es a <em>temperatura</em> como…", ["<em>reloj</em> es a <em>tiempo</em>", "<em>médico</em> es a <em>hospital</em>", "<em>fiebre</em> es a <em>gripe</em>"], "Instrumento y lo que mide."),
      ("<em>Perro</em> es a <em>mamífero</em> como…", ["<em>rosa</em> es a <em>flor</em>", "<em>gato</em> es a <em>ratón</em>", "<em>casa</em> es a <em>puerta</em>"], "Ejemplo y categoría."),
      ("<em>Sequía</em> es a <em>hambre</em> como…", ["<em>fuego</em> es a <em>humo</em>", "<em>lluvia</em> es a <em>nube</em>", "<em>sed</em> es a <em>agua</em>"], "Causa y efecto."),
      ("<em>Maestro</em> es a <em>alumno</em> como…", ["<em>médico</em> es a <em>paciente</em>", "<em>escuela</em> es a <em>clase</em>", "<em>libro</em> es a <em>página</em>"], "Relación recíproca entre dos papeles."),
      ("<em>Comprar</em> es a <em>vender</em> como…", ["<em>prestar</em> es a <em>pedir prestado</em>", "<em>pagar</em> es a <em>dinero</em>", "<em>tienda</em> es a <em>cliente</em>"], "Antónimos recíprocos: dos caras de la misma acción."),
      ("<em>Estado</em> es a <em>país</em> como…", ["<em>barrio</em> es a <em>ciudad</em>", "<em>alcalde</em> es a <em>ciudad</em>", "<em>mapa</em> es a <em>país</em>"], "Parte y todo."),
      ("<em>Tijeras</em> es a <em>cortar</em> como…", ["<em>escoba</em> es a <em>barrer</em>", "<em>papel</em> es a <em>cortar</em>", "<em>cuchillo</em> es a <em>tenedor</em>"], "Instrumento y su uso."),
      ("¿Qué relación hay entre <em>vivienda</em> y <em>apartamento</em>?", ["Categoría y ejemplo", "Parte y todo", "Antónimos"], "Un apartamento es una clase de vivienda."),
      ("¿Qué relación hay entre <em>ejercicio</em> y <em>cansancio</em>?", ["Causa y efecto", "Categoría y ejemplo", "Sinónimos"], "El ejercicio causa cansancio."),
      ("¿Qué relación hay entre <em>aprobado</em> y <em>reprobado</em>?", ["Antónimos complementarios", "Antónimos graduales", "Sinónimos"], "Si es uno, no puede ser el otro: no hay punto medio.")]


def hueco(t):
    return t.replace("___", '<span class="hueco">_____</span>')


def leccion():
    P = C.Practicas()
    s1 = f"""<p>Compare:</p>
<ul><li>«El alcalde <strong>dijo</strong> que bajarán los impuestos.»</li><li>«El alcalde <strong>prometió</strong> que bajarán los impuestos.»</li><li>«El alcalde <strong>admitió</strong> que bajarán los impuestos.»</li></ul>
<p>Las tres cuentan lo mismo, pero cada verbo deja ver algo distinto: una información, un compromiso o algo que el alcalde preferiría no tener que decir. En el GED, muchas preguntas de vocabulario preguntan justamente eso: qué matiz añade una palabra y por qué el autor la eligió.</p>
<ul><li>Los <strong>sinónimos</strong> tienen un significado parecido: <em>empezar</em> y <em>comenzar</em>; <em>bonito</em> y <em>lindo</em>.</li>
<li>Los <strong>antónimos</strong> tienen un significado opuesto: <em>subir</em> y <em>bajar</em>; <em>aumentar</em> y <em>disminuir</em>.</li></ul>
<p>En el Nivel 2 vio que algunas palabras parecidas cambian la intensidad: <em>tibio, caliente, ardiente</em>. Hoy da un paso más: en los textos académicos casi nunca hay dos sinónimos que digan exactamente lo mismo, y elegir bien es parte de escribir con precisión.</p>"""

    s2 = f"""<p>Los sinónimos se parecen, pero cada uno tiene su <strong>matiz</strong>: más fuerte o más suave, más formal o más cotidiano, o un uso propio.</p>
{C.tabla("Grupos de sinónimos con su matiz", ["Sinónimos", "El matiz"],
         [["pedir · solicitar · exigir", "<em>Pedir</em> es lo común; <em>solicitar</em>, lo formal (una beca, un permiso); <em>exigir</em>, pedir con fuerza, como un derecho."],
          ["mirar · observar · vigilar", "<em>Observar</em> es mirar con atención para aprender; <em>vigilar</em>, mirar para cuidar o controlar."],
          ["empezar · iniciar · inaugurar", "<em>Iniciar</em> es más formal; <em>inaugurar</em> se usa para algo nuevo que se abre con un acto público."],
          ["causar · provocar · ocasionar", "<em>Provocar</em> sugiere algo repentino o negativo; <em>ocasionar</em> es formal y neutro."],
          ["disminuir · reducir · desplomarse", "<em>Disminuir</em> y <em>reducir</em> son neutros; <em>desplomarse</em> es caer de golpe y mucho."]])}
{C.caja("tip", "La prueba del cambio", "<p>Ponga cada sinónimo en la oración y pregúntese si dice exactamente lo que quiere. «Los trabajadores <strong>exigen</strong> un aumento» no es lo mismo que «Los trabajadores <strong>piden</strong> un aumento».</p>")}
{P("Matiz 1", "¿Qué palabra es más adecuada en una carta formal: «Quisiera ___ información sobre el curso»?", ["exigir", "solicitar", "agarrar"], 1, {0: "Es demasiado fuerte para pedir información.", 2: "Es muy informal y no significa pedir."}, "<em>Solicitar</em> es pedir de manera formal.")}
{P("Matiz 2", hueco("«La científica ___ los pájaros durante horas para estudiar su conducta.»"), ["vigila", "ve", "observa"], 2, {0: "Vigilar es cuidar o controlar.", 1: "<em>Ver</em> no dice que mira con atención."}, "Mirar con atención para aprender: <em>observar</em>.")}"""

    s3 = f"""<p>Cuando un texto cuenta lo que dijo otra persona, el verbo que elige el autor revela <strong>cómo</strong> lo dijo, y a veces lo que el autor piensa de ello. Estos verbos son muy frecuentes en las lecturas del GED:</p>
{C.tabla("Verbos para citar y lo que revelan", ["Verbo", "Qué revela", "Ejemplo"],
         [["afirma, sostiene", "Lo presenta como algo seguro; <em>sostiene</em> añade que lo defiende.", "La investigadora sostiene que el plan funcionará."],
          ["sugiere, plantea", "Lo propone con menos seguridad.", "El estudio sugiere una relación entre sueño y memoria."],
          ["admite, reconoce", "Acepta algo, a veces a su pesar.", "El gerente admitió que hubo errores."],
          ["niega, rechaza", "Dice que algo no es cierto o no lo acepta.", "La empresa niega haber contaminado el río."],
          ["advierte, alerta", "Anuncia un peligro.", "El médico advierte que el calor es peligroso."],
          ["critica, cuestiona", "Muestra desacuerdo o duda.", "El concejal cuestiona el costo del proyecto."]])}
{C.caja("tip", "En el GED", "<p>Si una pregunta dice «¿Qué sugiere la palabra <em>admitió</em> sobre el gerente?», la respuesta casi siempre tiene que ver con este matiz: que reconoció algo que no le convenía.</p>")}
{P("Citar 1", "«El alcalde <strong>admitió</strong> que el proyecto costó más de lo previsto.» El verbo sugiere que el alcalde…", ["anunció algo de lo que estaba orgulloso", "reconoció algo que no le convenía", "prometió algo que piensa hacer"], 1, {0: "<em>Admitir</em> no transmite orgullo.", 2: "<em>Admitir</em> habla de algo que ya pasó."}, "<em>Admitir</em>: aceptar algo, a su pesar.")}
{P("Citar 2", hueco("«El informe ___ que podría haber más casos, pero no está claro.»"), ["demuestra", "asegura", "sugiere"], 2, {0: "«No está claro»: no hay prueba.", 1: "«No está claro»: no hay seguridad."}, "Proponer algo con poca seguridad: <em>sugerir</em>.")}"""

    s4 = f"""{C.tabla("Clases de antónimos", ["Clase", "Cómo funcionan", "Ejemplos"],
         [["Complementarios", "Si es uno, no puede ser el otro. No hay punto medio.", "vivo / muerto · aprobado / reprobado"],
          ["Graduales", "Hay puntos intermedios entre los dos extremos.", "frío / (tibio) / caliente · barato / caro"],
          ["Recíprocos", "Uno no existe sin el otro: son las dos caras de una misma acción.", "comprar / vender · prestar / pedir prestado · maestro / alumno"]])}
<p>Muchos antónimos se forman con un prefijo: <em>inútil, ilegal, desconocido, anormal</em>.</p>
{C.caja("tip", "Por qué importa", "<p>Si un texto dice que una medida «no es cara», no quiere decir que sea «barata»: <em>caro</em> y <em>barato</em> son graduales, y puede estar en el medio. Leer con precisión es no saltar al extremo contrario.</p>")}
{P("Antónimos 1", "<em>Comprar</em> y <em>vender</em> son antónimos…", ["complementarios", "graduales", "recíprocos"], 2, {0: "No se trata de ser uno u otro.", 1: "No hay puntos intermedios."}, "<strong>Recíprocos</strong>: uno no existe sin el otro.")}
{P("Antónimos 2", "Un texto dice que el plan «no es caro». ¿Qué se puede concluir con seguridad?", ["Que es el plan más barato de todos", "Que no cuesta mucho, aunque no sea barato", "Que es gratis para todos"], 1, {0: "Eso salta al extremo contrario.", 2: "Eso va mucho más allá del texto."}, "<em>Caro</em> y <em>barato</em> son graduales: puede estar en el medio.")}"""

    s5 = f"""{C.tabla("Relaciones entre palabras", ["Relación", "Ejemplos"],
         [["Categoría y ejemplo: una palabra general incluye a otras.", "mamífero → perro, ballena, murciélago · vivienda → casa, apartamento"],
          ["Parte y todo", "página → libro · estado → país · capítulo → novela"], ["Causa y efecto", "sequía → escasez · ejercicio → cansancio"],
          ["Instrumento y uso", "termómetro → medir la temperatura · tijeras → cortar"]])}
<h3>Las analogías</h3>
<p>Una <strong>analogía</strong> compara dos pares de palabras que tienen la misma relación. Se lee «A es a B como C es a D»:</p>
<p class="formula">Página es a libro como ladrillo es a pared.</p>
{C.caja("tip", "El truco", "<p>Diga la relación del primer par en una oración («una página es una parte de un libro») y busque el par que cabe en la misma oración («un ladrillo es una parte de una pared»).</p>")}
{P("Analogía 1", hueco("Complete: «<em>Tijeras</em> es a <em>cortar</em> como <em>termómetro</em> es a ___.»"), ["calentar", "medir", "fiebre"], 1, {0: "El termómetro no calienta.", 2: "La fiebre es lo que se mide, no el uso."}, "Instrumento y uso: el termómetro sirve para <strong>medir</strong>.")}
{P("Analogía 2", "¿Qué relación hay entre <em>capítulo</em> y <em>novela</em>?", ["Causa y efecto", "Parte y todo", "Antónimos"], 1, {0: "El capítulo no causa la novela.", 2: "No son opuestos."}, "Un capítulo es una <strong>parte</strong> de la novela.")}"""

    texto = "".join(f"<p>{p}</p>" for p in TEXTO)
    plano = " ".join(re.sub("<[^>]+>", "", p) for p in TEXTO)
    s6 = f"""<p>Lea el texto. Después pulse <strong>Mostrar el vocabulario</strong> y copie en su cuaderno un mapa de palabras: para cada palabra marcada, escriba un sinónimo y, si lo tiene, un antónimo.</p>
<p>{LE.escuchar(plano, "Escuchar el texto")} <button type="button" class="btn-sec" id="btn-v23" aria-pressed="false">Mostrar el vocabulario</button></p>
<div class="articulo lectura-cl" id="lect-23"><p><strong>El viaje de la mariposa monarca</strong></p>{texto}</div>
<p class="fuente">Datos: Servicio Forestal de los EE. UU., «Monarch Butterfly» (fs.usda.gov), y Servicio de Pesca y Vida Silvestre de los EE. UU., «The monarch super generation» (fws.gov). Consultados en noviembre de 2026.</p>
<script>(function(){{var b=document.getElementById("btn-v23"),t=document.getElementById("lect-23");b.addEventListener("click",function(){{var on=t.classList.toggle("ver-cl");b.setAttribute("aria-pressed",on?"true":"false");b.textContent=on?"Ocultar el vocabulario":"Mostrar el vocabulario";}});}})();</script>
<details class="transc"><summary>Ver el mapa de palabras</summary>{C.tabla("Mapa de palabras de la lectura", ["Palabra", "Sinónimo", "Antónimo"], MAPA)}</details>
<h3>Preguntas de vocabulario</h3>
{P("Monarca 1", "En el texto, <em>emprenden</em> el viaje significa que…", ["lo terminan", "lo comienzan", "lo evitan"], 1, {0: "Es al revés: el viaje empieza en otoño.", 2: "Sí hacen el viaje."}, "<em>Emprender</em> es comenzar algo grande o difícil.")}
{P("Monarca 2", "¿Qué palabra del texto es un antónimo de <em>llegan</em>?", ["recorren", "sostienen", "parten"], 2, {0: "<em>Recorrer</em> es ir de un lugar a otro.", 1: "<em>Sostener</em> es afirmar."}, "<em>Parten</em> (salen) es lo contrario de <em>llegan</em>.")}
{P("Monarca 3", "Los científicos «advierten» que su número ha disminuido. ¿Qué añade el verbo?", ["Que es un dato curioso sin importancia", "Que todavía no están seguros", "Que es un peligro y hay que prestar atención"], 2, {0: "<em>Advertir</em> anuncia un peligro.", 1: "Eso lo diría <em>sugieren</em>."}, "<em>Advertir</em> es avisar de un peligro.")}
{P("Monarca 4", "«Su número ha <em>disminuido</em>». ¿Qué sinónimo cambia menos el sentido?", ["se ha desplomado", "se ha reducido", "ha desaparecido"], 1, {0: "<em>Desplomarse</em> es caer de golpe y mucho.", 2: "<em>Desaparecer</em> es dejar de existir."}, "<em>Reducirse</em> es neutro, como <em>disminuir</em>.")}
{P("Monarca 5", "<em>Mariposa</em> es a <em>insecto</em> como <em>oyamel</em> es a…", ["bosque", "árbol", "México"], 1, {0: "Un oyamel no es una clase de bosque.", 2: "México es un lugar, no una categoría."}, "Ejemplo y categoría: la mariposa es un insecto y el oyamel es un árbol.")}
{C.caja("tip", "Si tiene con quién practicar", "<p>Tomen una noticia corta de un periódico en español y busquen juntos los verbos que usa para contar lo que dijo cada persona (<em>dijo, afirmó, negó, admitió…</em>). ¿Qué piensa el periodista de cada uno?</p>")}"""

    secciones = [("s1", "Repaso: sinónimos y antónimos", s1), ("s2", "Sinónimos con matiz", s2), ("s3", "Los verbos para citar a un autor", s3),
                 ("s4", "Tres clases de antónimos", s4), ("s5", "Otras relaciones entre palabras", s5), ("s6", "Lectura: «El viaje de la mariposa monarca»", s6)]
    tarea = [("Tres matices.", "Escriba tres oraciones sobre su trabajo o su barrio con <em>pedir</em>, <em>solicitar</em> y <em>exigir</em>, de modo que cada una necesite ese verbo y no otro."),
             ("Cuente lo que dijo.", "Piense en algo que le dijo alguien esta semana y cuéntelo tres veces, con <em>afirmó</em>, <em>admitió</em> y <em>sugirió</em>. Explique qué cambia."),
             ("Invente analogías.", "Complete con sus palabras: «Pétalo es a flor como ___ es a ___» · «Lluvia es a inundación como ___ es a ___» · «Comprar es a vender como ___ es a ___». "
              "<details class=\"transc\"><summary>Ver respuestas posibles</summary><p>Parte y todo: hoja es a árbol, rueda es a carro. · Causa y efecto: sequía es a escasez, fuego es a humo. · Antónimos recíprocos: prestar es a pedir prestado, enseñar es a aprender.</p></details>")]
    quiz = [
        ("¿Cuál es la diferencia entre <em>pedir</em> y <em>exigir</em>?", ["Exigir es pedir con fuerza, como un derecho", "Exigir es una forma más cortés de pedir", "No hay diferencia: significan lo mismo"], 0, {1: "Es al revés.", 2: "Tienen matices distintos."}, "<em>Exigir</em> es pedir <strong>con fuerza</strong>."),
        ("¿Qué verbo muestra que alguien dice que algo <strong>no</strong> es cierto?", ["niega", "sostiene", "advierte"], 0, {1: "Afirma y defiende.", 2: "Anuncia un peligro."}, "<strong>Niega.</strong>"),
        ("¿Qué verbo presenta una idea con <strong>menos seguridad</strong>?", ["sugiere", "afirma", "sostiene"], 0, {1: "Es seguro.", 2: "Es seguro y lo defiende."}, "<strong>Sugiere.</strong>"),
        ("<em>Vivo</em> y <em>muerto</em> son antónimos…", ["complementarios: no hay punto medio", "graduales: hay puntos intermedios", "recíprocos: uno no existe sin el otro"], 0, {1: "No hay un punto medio.", 2: "No son dos caras de una acción."}, "<strong>Complementarios.</strong>"),
        ("<em>Barato</em> y <em>caro</em> son antónimos…", ["graduales", "complementarios", "recíprocos"], 0, {1: "Hay precios intermedios.", 2: "No son dos caras de una acción."}, "<strong>Graduales.</strong>"),
        (hueco("Complete: «<em>Sequía</em> es a <em>escasez</em> como <em>lluvia</em> es a ___.»"), ["inundación", "nube", "paraguas"], 0, {1: "La nube es la causa, no el efecto.", 2: "Es un instrumento."}, "Causa y efecto: <strong>inundación</strong>."),
        ("¿Qué palabra es una categoría que incluye a <em>casa</em> y <em>apartamento</em>?", ["vivienda", "cocina", "barrio"], 0, {1: "Es una parte.", 2: "Es un lugar más grande."}, "<strong>Vivienda.</strong>"),
        (hueco("«Los trabajadores ___ un salario justo; dicen que es su derecho.»"), ["exigen", "piden por favor", "sugieren"], 0, {1: "No es suave: es su derecho.", 2: "Es demasiado suave."}, "<strong>Exigen.</strong>"),
        (hueco("«Las autoridades ___ que el agua del río no es potable.»"), ["advierten", "sugieren", "admiten"], 0, {1: "Es un peligro, no una idea dudosa.", 2: "No reconocen algo propio."}, "<strong>Advierten</strong> de un peligro."),
        ("¿Qué relación hay entre <em>ejercicio</em> y <em>cansancio</em>?", ["Causa y efecto", "Categoría y ejemplo", "Sinónimos"], 0, {1: "El cansancio no es un ejercicio.", 2: "No significan lo mismo."}, "<strong>Causa y efecto.</strong>"),
    ]
    filas = [
        ("Sinónimos con matiz", "Elijo el sinónimo exacto según el contexto.", "A veces uno demasiado fuerte o suave.", "Los uso como si fueran iguales (<a href=\"#s2\">repase la sección 2</a>)."),
        ("Verbos para citar", "Sé qué revela afirma, sugiere, admite, niega o advierte.", "Conozco algunos.", "No veo la diferencia (<a href=\"#s3\">repase la sección 3</a>)."),
        ("Antónimos y analogías", "Distingo las tres clases de antónimos y resuelvo analogías.", "Me cuestan las analogías.", "Me pierdo (<a href=\"#s4\">repase las secciones 4 y 5</a>)."),
    ]
    cierre = "<p>Ya elige la palabra precisa y reconoce las relaciones entre palabras. ¡Terminó el Tema 2! En el Tema 3 verá la <strong>comprensión inferencial</strong> y la <strong>evidencia textual</strong>.</p>"
    glosario = [("Matiz", "La pequeña diferencia de sentido entre palabras parecidas."), ("Antónimo gradual", "Opuesto con puntos intermedios: frío, tibio, caliente."),
                ("Antónimo recíproco", "Opuesto que no existe sin el otro: comprar y vender."), ("Analogía", "Comparación de dos pares de palabras con la misma relación.")]
    conexion = ("<p>En la Lección 2.2 entendió palabras nuevas por sus raíces. Hoy afina la elección entre palabras parecidas, como pide el GED.</p>"
                "<p><strong>Lo que necesita:</strong> su cuaderno y, si puede, una noticia corta en español.</p>")
    estd = LE.estandares(["R.4.2", "R.4.3"], base=["L.1.4"])
    return C.pagina_leccion(N, LE.titulo(N), "Elegir la palabra precisa.", ["Vocabulario", "Relaciones entre palabras"],
                            ["<strong>Distinguir</strong> los matices entre sinónimos.", "<strong>Interpretar</strong> los verbos con que un autor cita a otros.",
                             "<strong>Reconocer</strong> tres clases de antónimos.", "<strong>Resolver</strong> analogías por la relación entre palabras."],
                            estd, conexion, secciones, tarea, quiz, filas, cierre, ("3-1", LE.titulo("3-1")), glosario, P)


def practica():
    si = [{"enun": f'<p class="frase">{t.replace("<b>", "<b class=\"marca\">")}</p><p>¿Qué palabra significa lo mismo?</p>', "ops": o, "ok": 0,
           "pista": "Cambie la palabra marcada por la que eligió: ¿la oración dice lo mismo?", "exp": f"<strong>{o[0]}</strong> · {e}"} for t, o, e in SI]
    pp = [{"enun": f'<p class="frase">{hueco(t)}</p>', "ops": o, "ok": 0, "pista": "¿El contexto pide algo formal o común, fuerte o suave, seguro o dudoso?",
           "exp": f"<strong>{o[0]}</strong> · {e}"} for t, o, e in PP]
    re_ = [{"enun": f'<p class="frase">{t}</p>', "ops": o, "ok": 0, "pista": "Diga la relación del primer par en una oración y compruebe si el otro par cabe en ella.", "exp": e} for t, o, e in RE]
    mods = [("sinonimos", "Sinónimos", C.om("m1", "Elija la palabra que significa lo mismo que la marcada.")),
            ("precisa", "La palabra precisa", C.om("m2", "Elija la palabra que dice exactamente lo que pide el contexto.")),
            ("relaciones", "Relaciones y analogías", C.om("m3", "Descubra la relación entre las palabras y complete la analogía."))]
    js = C.js_datos("SI", si) + C.js_datos("PP", pp) + C.js_datos("RE", re_) + 'creaBanco("m1", SI);\ncreaBanco("m2", PP);\ncreaBanco("m3", RE);\n'
    return C.pagina_practica(N, LE.titulo(N), "Tres actividades · los ejercicios cambian cada vez · dos intentos en cada uno", mods, js)


if __name__ == "__main__":
    LE.construye(N, leccion, practica, horas="Unas 3 horas")
