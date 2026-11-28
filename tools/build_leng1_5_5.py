# -*- coding: utf-8 -*-
"""LearnGED · Artes del lenguaje (español) · Nivel 1 · Lección 5.5 · La relación de causa y efecto.
Fuente: clases_leng1/clase_5-5.html (GEDparaHispanos) y gramatica/n1-l5-5.html, adaptadas al marco de LearnGED.
Las oraciones de la práctica se generan a partir de pares causa-efecto, con el conector delante de la causa o del efecto.
Uso: python3 tools/build_leng1_5_5.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import leng_es as LE
from leng_es import C

LE.nivel(1)
N = "5-5"
PARES = [("llovió toda la noche", "las calles amanecieron inundadas"), ("Rosa olvidó poner el despertador", "llegó tarde al trabajo"),
         ("subió el precio de la gasolina", "subieron los pasajes del autobús"), ("el niño comió demasiados dulces", "le dolió el estómago"),
         ("hubo una helada", "se perdió la cosecha de tomates"), ("Pedro estudió todos los días", "aprobó el examen"),
         ("se rompió una tubería", "se inundó el sótano"), ("la fábrica cerró", "muchas familias se quedaron sin trabajo"),
         ("no regué las plantas", "se secaron"), ("había mucho tráfico", "el autobús llegó tarde"),
         ("Ana ahorró durante un año", "pudo pagar el curso de inglés"), ("se fue la luz", "se descongeló el refrigerador")]
# Formas: (plantilla, ¿qué viene primero?) — c = causa, e = efecto
FORMAS = ["{C}, así que {e}.", "{E} porque {c}.", "Como {c}, {e}.", "{C}; por eso, {e}.", "{E} ya que {c}.", "{C}; como resultado, {e}."]
# (conector, 0 causa / 1 efecto, ejemplo con el conector en <strong>)
CONECTORES = [("porque", 0, "No salimos <strong>porque</strong> llovía."), ("ya que", 0, "Cerraron la escuela <strong>ya que</strong> no había luz."),
              ("debido a", 0, "El vuelo se retrasó <strong>debido a</strong> la niebla."), ("puesto que", 0, "<strong>Puesto que</strong> no tenía dinero, no compró nada."),
              ("como (al principio)", 0, "<strong>Como</strong> hacía frío, me puse el abrigo."), ("por eso", 1, "Tenía sueño; <strong>por eso</strong>, me acosté."),
              ("así que", 1, "Llovía, <strong>así que</strong> llevé el paraguas."), ("como resultado", 1, "Entrenó mucho; <strong>como resultado</strong>, ganó."),
              ("en consecuencia", 1, "El río creció; <strong>en consecuencia</strong>, evacuaron la zona."), ("por lo tanto", 1, "No hay autobuses; <strong>por lo tanto</strong>, caminaremos."),
              ("por esta razón", 1, "Subió la renta. <strong>Por esta razón</strong>, nos mudamos.")]
HUECOS = [("No fui a trabajar ____ tenía fiebre.", "porque", ["así que", "por eso"], "introduce la causa"),
          ("Tenía fiebre, ____ no fui a trabajar.", "así que", ["porque", "ya que"], "introduce el efecto"),
          ("Cancelaron el partido ____ la lluvia.", "debido a", ["así que", "por eso"], "introduce la causa, y va delante de un sustantivo (la lluvia)"),
          ("Se acabó el gas; ____, no pudimos cocinar.", "por eso", ["porque", "debido a"], "introduce el efecto"),
          ("Practicó todos los días; ____, mejoró mucho.", "como resultado", ["porque", "ya que"], "introduce el efecto"),
          ("Nos quedamos en casa ____ hacía mucho frío.", "ya que", ["por eso", "así que"], "introduce la causa"),
          ("El puente se cayó; ____, cerraron la carretera.", "en consecuencia", ["porque", "debido a"], "introduce el efecto"),
          ("Llegó tarde ____ el tráfico.", "debido a", ["por lo tanto", "así que"], "introduce la causa, y va delante de un sustantivo (el tráfico)"),
          ("No había leche, ____ fui a la tienda.", "así que", ["porque", "debido a"], "introduce el efecto"),
          ("Perdí el autobús ____ me quedé dormido.", "porque", ["por eso", "en consecuencia"], "introduce la causa"),
          ("Ahorramos durante meses; ____, pudimos comprar el carro.", "por lo tanto", ["ya que", "debido a"], "introduce el efecto"),
          ("El restaurante cerró ____ la falta de clientes.", "debido a", ["así que", "por eso"], "introduce la causa, y va delante de un sustantivo")]
# ¿Causa o solo secuencia? (texto, True si hay causa)
SECUENCIA = [("Me puse la camisa azul y después empezó a llover.", False, "La camisa no causó la lluvia: solo pasó antes."),
             ("Dejé la leche fuera del refrigerador toda la noche y se echó a perder.", True, "El calor de la noche fuera del refrigerador echó a perder la leche."),
             ("Desayuné cereal y luego sonó el teléfono.", False, "El cereal no hizo sonar el teléfono."),
             ("Dejé caer el vaso y se rompió.", True, "La caída rompió el vaso."),
             ("Llegó el cartero y después salió el sol.", False, "El cartero no hace salir el sol."),
             ("No pagué la factura y me cortaron el servicio.", True, "Cortaron el servicio por no pagar."),
             ("Me corté el pelo y al día siguiente gané la rifa.", False, "El corte de pelo no tiene nada que ver con la rifa."),
             ("Comí algo en mal estado y me enfermé del estómago.", True, "La comida en mal estado causó el malestar.")]
BARRIO = ["El precio de la renta subió un 40 % el año pasado; como resultado, muchas familias del barrio tuvieron que mudarse lejos.",
          "Varios negocios pequeños cerraron debido a la pérdida de sus clientes de siempre. Por esta razón, la junta de vecinos organizó reuniones con los concejales.",
          "La presión de la comunidad fue constante, así que la alcaldía aprobó un programa de protección del alquiler para las familias de bajos ingresos."]


def may(s):
    return s[0].upper() + s[1:]


def leccion():
    P = C.Practicas()
    s1 = f"""<p>En la Lección 5.3 ordenó los hechos en el tiempo. Ahora va a ver la lógica que los une: no solo <strong>cuándo</strong> pasan, sino <strong>por qué</strong> pasan.</p>
{C.tabla("Las dos preguntas", ["Parte", "Pregunta", "Ejemplo"],
         [["🔵 Causa", "¿Por qué ocurrió?", "Llovió toda la noche."], ["🔴 Efecto", "¿Qué pasó?", "Las calles amanecieron inundadas."]])}
<p>En la realidad, la causa siempre ocurre <strong>antes</strong> que el efecto. Pero al escribir, el autor puede nombrar primero el efecto: «Las calles amanecieron inundadas <strong>porque</strong> llovió toda la noche».</p>
{C.caja("ojo", "Secuencia no es causa", "<p>Que una cosa pase después de otra no quiere decir que la primera la causara. «Me puse la camisa azul y después empezó a llover»: la camisa no causó la lluvia. Para que haya causa y efecto, el primer hecho tiene que <strong>producir</strong> el segundo.</p>")}
{P("Compruebe", "<em>Olvidé poner el despertador, así que llegué tarde al trabajo.</em> ¿Cuál es la causa?", ["Olvidé poner el despertador", "Llegué tarde al trabajo"], 0, {}, "La causa es <strong>olvidar el despertador</strong>: responde a ¿por qué llegó tarde?")}"""

    s2 = f"""<p>Los autores marcan la relación con <strong>conectores de causa</strong>. Lo importante es saber qué viene <strong>después</strong> del conector: ¿la causa o el efecto?</p>
{C.tabla("Conectores de causa y efecto", ["Conector", "Lo que viene después", "Ejemplo"],
         [["porque · ya que · puesto que", "la <strong>causa</strong>", "No fui a trabajar porque estaba enfermo."],
          ["debido a", "la <strong>causa</strong>, dicha con un sustantivo", "El vuelo se retrasó debido a la niebla."],
          ["como (al principio de la oración)", "la <strong>causa</strong>", "Como hacía frío, me puse el abrigo."],
          ["así que · por eso", "el <strong>efecto</strong> (registro informal)", "Tenía hambre, así que preparé un sándwich."],
          ["como resultado · por esta razón", "el <strong>efecto</strong>", "Estudió todos los días; como resultado, aprobó."],
          ["en consecuencia · por lo tanto", "el <strong>efecto</strong> (registro formal)", "El río se desbordó; en consecuencia, evacuaron la zona."]])}
{C.caja("tip", "Un truco", "<p>Ponga «<strong>¿por qué?</strong>» delante de la oración. Si la respuesta empieza por <em>porque…</em>, esa parte es la causa.</p>")}
<h3>Una cadena de causas y efectos</h3>
<p>Un efecto puede convertirse en la causa del hecho siguiente, como los eslabones de una cadena:</p>
<div class="texto-lectura">{"".join(f"<p>{p}</p>" for p in BARRIO)}</div>
<p>Subió la renta → las familias se mudaron → los negocios perdieron clientes y cerraron → los vecinos se organizaron → la alcaldía aprobó el programa.</p>
{P("Compruebe", "En el texto, ¿por qué cerraron los negocios pequeños?", ["Perdieron a sus clientes de siempre", "La alcaldía aprobó un programa", "La junta organizó reuniones"], 0,
   {1: "Eso pasó al final de la cadena: es un efecto, no la causa del cierre.", 2: "Las reuniones vinieron después, por culpa del cierre."}, "<strong>Perdieron a sus clientes</strong>: lo dice «debido a».")}"""

    s3 = f"""<div class="caja caja-tip"><span class="etiqueta et-verde">Actividad · en su cuaderno</span>
<p>Dibuje una cadena de cuatro eslabones con algo que le pasó a usted: «Perdí el autobús → llegué tarde → …». Después escríbala como un párrafo usando tres conectores distintos.</p></div>
{P("Compruebe", "<em>Cancelaron el partido ____ la lluvia.</em> ¿Qué conector va?", ["debido a", "así que", "por eso"], 0,
   {1: "«Así que» introduce un efecto, y la lluvia es la causa.", 2: "«Por eso» introduce un efecto, y la lluvia es la causa."}, "<strong>debido a</strong>: introduce la causa y va delante de un sustantivo.")}
{P("Compruebe", "<em>Desayuné cereal y luego sonó el teléfono.</em> ¿Hay causa y efecto?", ["No: solo es secuencia", "Sí: el cereal hizo sonar el teléfono"], 0, {}, "<strong>Solo secuencia</strong>: una cosa pasó después de la otra, pero no la causó.")}"""

    secciones = [("s1", "¿Qué son la causa y el efecto?", s1), ("s2", "Los conectores de causa", s2), ("s3", "Práctica: cadenas y conectores", s3)]
    tarea = [("Causas y efectos en las noticias.", "Lea una noticia corta (del periódico, la radio o internet). Copie dos oraciones que tengan causa y efecto y subraye la causa con una línea y el efecto con dos."),
             ("Los conectores.", "Encierre en un círculo el conector de cada oración. Si no tiene, escriba la oración de nuevo con uno."),
             ("Mi cadena.", "Pase en limpio la cadena de la sección 3 con al menos tres conectores distintos.")]
    quiz = [
        ("¿Qué pregunta responde la <strong>causa</strong>?", ["¿Por qué ocurrió?", "¿Qué pasó después?", "¿Dónde ocurrió?"], 0, {1: "Eso es el efecto.", 2: "Eso es el lugar."}, "<strong>¿Por qué ocurrió?</strong>"),
        ("¿Qué ocurre primero en la realidad?", ["La causa", "El efecto"], 0, {}, "La <strong>causa</strong>, aunque el texto nombre antes el efecto."),
        ("<em>No fui a trabajar porque estaba enfermo.</em> ¿Cuál es el efecto?", ["No fui a trabajar", "Estaba enfermo"], 0, {}, "<strong>No fui a trabajar</strong>: es lo que pasó."),
        ("¿Qué viene después de <strong>porque</strong>?", ["La causa", "El efecto"], 0, {}, "La <strong>causa</strong>."),
        ("¿Qué viene después de <strong>por lo tanto</strong>?", ["El efecto", "La causa"], 0, {}, "El <strong>efecto</strong>."),
        ("<em>Tenía hambre, ____ preparé un sándwich.</em>", ["así que", "porque", "debido a"], 0, {1: "Lo que sigue es un efecto, no una causa.", 2: "Debido a introduce una causa."}, "<strong>así que</strong>: introduce el efecto."),
        ("<em>Me puse la camisa azul y después empezó a llover.</em> ¿Hay causa y efecto?", ["No: solo secuencia", "Sí"], 0, {}, "<strong>Solo secuencia</strong>."),
        ("¿Qué es una cadena de causas y efectos?", ["Cuando un efecto se vuelve la causa del hecho siguiente", "Una lista de conectores", "Un tipo de personaje"], 0, {1: "No.", 2: "No."}, "Un efecto que <strong>causa</strong> el hecho siguiente."),
        ("<em>El vuelo se retrasó debido a la niebla.</em> ¿Cuál es la causa?", ["la niebla", "el vuelo se retrasó"], 0, {}, "<strong>La niebla.</strong>"),
        ("¿Por qué importa la causa y el efecto en el GED?", ["Aparece en todas las materias: hay que saber qué causó qué", "Solo aparece en matemáticas"], 0, {}, "Aparece en <strong>todas las materias</strong>."),
    ]
    filas = [
        ("Causa y efecto", "Separo la causa del efecto aunque el efecto venga primero.", "Me confundo cuando el efecto va primero.", "No los distingo (<a href=\"#s1\">repase la sección 1</a>)."),
        ("Conectores", "Sé qué conectores introducen la causa y cuáles el efecto.", "Conozco porque y así que, pero no los formales.", "No los reconozco (<a href=\"#s2\">repase la sección 2</a>)."),
        ("Secuencia frente a causa", "Distingo cuando un hecho solo pasó antes y cuando lo causó.", "A veces creo que todo lo que pasa antes es causa.", "No veo la diferencia (<a href=\"#s1\">repase la sección 1</a>)."),
    ]
    cierre = "<p>Ya sabe ver por qué pasan las cosas en un texto. En la última lección del tema va a <strong>comparar y contrastar</strong> información.</p>"
    glosario = [("Causa", "Lo que hace que algo ocurra. Responde a ¿por qué?"), ("Efecto", "Lo que pasa como resultado. Responde a ¿qué pasó?"),
                ("Conector de causa", "Palabra que une la causa y el efecto: porque, así que, por lo tanto…"), ("Cadena de causas", "Serie de hechos en la que cada efecto causa el siguiente.")]
    conexion = ("<p>En la Lección 5.3 ordenó los hechos en el tiempo, y en la 5.4 siguió instrucciones paso a paso. Ahora va a estudiar la lógica que une los hechos. Las relaciones de causa y efecto son la columna de las noticias, la ciencia y la historia, y aparecen en todo el examen GED.</p>"
                "<p><strong>Lo que necesita:</strong> el cuaderno y una noticia corta.</p>")
    estd = LE.estandares(["R.3.4", "R.5.3"], base=["R.3.3"])
    return C.pagina_leccion(N, LE.titulo(N), "Una cosa lleva a la otra: el porqué de los hechos.", ["R.3.4 · Causa y efecto", "R.5.3 · Conectores"],
                            ["<strong>Distinguir</strong> la causa del efecto, aunque el efecto aparezca primero.", "<strong>Usar</strong> los conectores que introducen la causa y el efecto.",
                             "<strong>Seguir</strong> una cadena de causas y efectos.", "<strong>Diferenciar</strong> la secuencia de la causa."],
                            estd, conexion, secciones, tarea, quiz, filas, cierre, ("5-6", LE.titulo("5-6")), glosario, P)


def practica():
    ce = []
    for i, (c, e) in enumerate(PARES):
        for j, f in enumerate([FORMAS[[0, 2, 3, 5][i % 4]], FORMAS[[1, 4][i % 2]]]):
            o = f.format(C=may(c), c=c, E=may(e), e=e)
            pide = (i + j) % 2  # 0: causa, 1: efecto
            ok, otro = (c, e) if pide == 0 else (e, c)
            ce.append({"enun": f"<strong>{o}</strong><br>¿Cuál es {'la <strong>causa</strong>' if pide == 0 else 'el <strong>efecto</strong>'}?", "ops": [may(ok), may(otro)], "ok": 0,
                       "pista": "", "exp": f"{'La causa' if pide == 0 else 'El efecto'} es «{ok}»: {'responde a ¿por qué ocurrió?' if pide == 0 else 'es lo que pasó como resultado'}."})
    co = [{"enun": f"<strong>{ej}</strong><br>Lo que viene después de «{cn}», ¿es la causa o el efecto?", "ops": ["La causa", "El efecto"], "ok": k, "enOrden": True, "pista": "",
           "exp": f"«{cn.split(' (')[0]}» introduce {'la <strong>causa</strong>' if k == 0 else 'el <strong>efecto</strong>'}."} for cn, k, ej in CONECTORES]
    hu = [{"enun": f"<strong>{o}</strong><br>¿Qué conector va en el espacio?", "ops": [ok] + d, "ok": 0, "pista": "¿Lo que sigue al espacio es la causa o el efecto?", "exp": f"Va <strong>{ok}</strong>: {e}."} for o, ok, d, e in HUECOS]
    se = [{"enun": f"<strong>{t}</strong><br>¿Hay causa y efecto, o solo una cosa pasó después de la otra?", "ops": ["Causa y efecto", "Solo secuencia"], "ok": 0 if v else 1, "enOrden": True, "pista": "",
           "exp": e} for t, v, e in SECUENCIA]
    mods = [("causa-efecto", "¿Causa o efecto?", C.om("m1", "Lea la oración y elija la parte que se pide.")),
            ("conectores", "¿Qué introduce el conector?", C.om("m2", "Decida si lo que sigue al conector es la causa o el efecto.")),
            ("completar", "Complete con el conector", C.om("m3", "Elija el conector que expresa la relación.")),
            ("secuencia", "¿Causa o solo secuencia?", C.om("m4", "¿El primer hecho produjo el segundo, o solo pasó antes?"))]
    js = (C.js_datos("CE", ce) + C.js_datos("CO", co) + C.js_datos("HU", hu) + C.js_datos("SE", se) +
          'creaBanco("m1", CE);\ncreaBanco("m2", CO);\ncreaBanco("m3", HU);\ncreaBanco("m4", SE);\n')
    return C.pagina_practica(N, LE.titulo(N), "Cuatro actividades · los ejercicios cambian cada vez · dos intentos en cada uno", mods, js)


if __name__ == "__main__":
    LE.construye(N, leccion, practica, horas="Unas 3 horas")
