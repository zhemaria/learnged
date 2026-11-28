# -*- coding: utf-8 -*-
"""LearnGED · Artes del lenguaje (español) · Nivel 1 · Lección 2.2 · Decodificación.
Fuente: clases_leng1/clase_2-2.html (GEDparaHispanos), adaptada al marco de LearnGED.
Los sonidos de las letras son grabaciones del profesor (es/artes-del-lenguaje/audio/s.m4a, p.m4a…);
la voz sintética no sabe decirlos. La tabla se amplía con j, t, c, b y g.
Uso: python3 tools/build_leng1_2_2.py
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import leng_es as LE
from leng_es import C

LE.nivel(1)
N = "2-2"

LETRAS = [("S", "ese", "sss", "largo", "s", "sol"), ("M", "eme", "mmm", "largo", "m", "mesa"), ("N", "ene", "nnn", "largo", "n", "nube"),
          ("L", "ele", "lll", "largo", "l", "luna"), ("F", "efe", "fff", "largo", "f", "foca"), ("R", "erre", "rrr (fuerte)", "largo", "r", "ratón"),
          ("J", "jota", "jjj", "largo", "j", "jugo"), ("P", "pe", "p… pa", "corto", "p", "pan"), ("T", "te", "t… ta", "corto", "t", "taza"),
          ("C", "ce", "c… ca (como en casa)", "corto", "c", "casa"), ("B", "be", "b… ba", "corto", "b", "boca"), ("D", "de", "d… da", "corto", "d", "dedo"),
          ("G", "ge", "g… ga (como en gato)", "corto", "g", "gato")]
SILABAS = ["ca", "sa", "me", "ma", "lo", "pa", "ta", "to", "la", "so", "pe", "mo"]
REALES = ["casa", "cama", "capa", "caso", "sala", "mesa", "meta", "mapa", "masa", "mala", "malo", "mato", "mata", "mamá", "loca", "lata", "losa", "lomo",
          "loma", "pato", "pata", "pasa", "paso", "pala", "palo", "papa", "papá", "tapa", "tasa", "toca", "toma", "laca", "sopa", "sola", "solo", "pesa",
          "peca", "pelo", "pela", "peso", "mota", "tapa", "saca", "lame", "sapo"]
def _se_arma(w):
    w = w.replace("á", "a").replace("é", "e")
    return any(w == a + b for a in SILABAS for b in SILABAS)


REALES = sorted({w for w in REALES if _se_arma(w)})
LISTA = [("bebé", "be-bé"), ("bota", "bo-ta"), ("boca", "bo-ca"), ("dado", "da-do"), ("tigre", "ti-gre"), ("taxi", "ta-xi"), ("mesa", "me-sa"), ("pato", "pa-to"),
         ("silla", "si-lla"), ("leche", "le-che"), ("vaso", "va-so"), ("gato", "ga-to")]


def bloques(a, b, w):
    return (f'<p class="bloques">{LE.escuchar(a, a, 0.6).replace("btn-voz", "btn-voz sil")} + {LE.escuchar(b, b, 0.6).replace("btn-voz", "btn-voz sil2")} = '
            f'{LE.escuchar(w, "¡" + w + "!", 0.8)}</p>')


def leccion():
    P = C.Practicas()
    filas = []
    for L, nom, son, tipo, clave, ej in LETRAS:
        voz = {"be": "beh", "pe": "la pe"}.get(nom, nom)
        boton = f'<button type="button" class="btn-voz mini" data-hablar="{voz}" data-vel="0.7" aria-label="Escuchar el nombre de la {L}"><span aria-hidden="true">🔊</span></button>'
        filas.append([L, f"«{nom}» " + boton, f"/{son}/ · {tipo}",
                      f'<button type="button" class="btn-voz mini" data-sonido="{clave}" hidden><span aria-hidden="true">🔊</span> sonido</button> <em>{ej}</em>'])
    s1 = f"""<p>En la lección anterior entrenó el oído: sílabas, rimas y sonidos. Hoy da el gran salto: va a unir esos sonidos con las <strong>letras</strong> que ve en el papel. Mirar una letra y decir el sonido que le corresponde se llama <strong>decodificar</strong>. Cuando junta varios sonidos seguidos, sale una palabra. ¡Eso es leer!</p>
{C.caja("ojo", "Regla de oro", "<p>Para leer se usa el <strong>sonido</strong> de la letra, no su nombre. Si dice «pe-a-ene», no sale nada; si dice «p… a… nnn», sale <em>pan</em>. Con el nombre la palabra se complica; con el sonido, todo encaja.</p>")}
<h3>Nombre y sonido de las letras</h3>
<p>Escuche el nombre de cada letra con su botón 🔊. Hay dos clases de sonidos: los <strong>largos</strong>, que se pueden estirar (sss, mmm), y los <strong>cortos</strong>, que salen de un golpe y necesitan una vocal para oírse bien (p… pa).</p>
{LE.AVISO_VOZ}
{C.tabla("Nombre y sonido de trece letras", ["Letra", "Nombre", "Sonido", "Ejemplo"], filas)}
<p class="nota-audio" data-nota="s m n l f r j p t c b d g">🗣️ <strong>Los sonidos dígalos usted en voz alta:</strong> los largos, estirados y sin vocal al final («sss», no «se»); los cortos, de un golpe y enseguida con la a («p… pa»). Muy pronto estarán aquí grabados.</p>
{P("Compruebe", "Para leer <strong>sol</strong>, ¿qué dice?", ["«ese… o… ele»", "«sss… o… lll»"], 1, {},
   "Con los <strong>sonidos</strong>: sss… o… lll → <em>sol</em>. Con los nombres saldría «ese-o-ele», que no es ninguna palabra.")}"""

    s2 = f"""<p>Las palabras más fáciles son las de <strong>una sola sílaba</strong>: se dicen de un golpe, como un solo paso de baile.</p>
<p class="frecuentes">{" ".join(LE.escuchar(w, w, 0.8) for w in ["luz", "pan", "sol", "mar", "flor"])}</p>
<h3>Dos pasos de baile: las palabras de dos sílabas</h3>
<p>Para leer una palabra de dos sílabas, primero se dice la primera, después la segunda, y al unirlas sale la palabra. Toque cada bloque para oírlo y después la palabra completa:</p>
{bloques("va", "ca", "vaca")}
{bloques("lá", "piz", "lápiz")}
{bloques("be", "bé", "bebé")}
{C.caja("tip", "Con papel también funciona", "<p>Tome dos papelitos de colores distintos. Toque el primero y diga la primera sílaba; toque el segundo y diga la segunda. Después júntelos y diga la palabra. Pruebe con <em>mesa</em>, <em>casa</em> y <em>luna</em>.</p>")}
<h3>Arme usted las palabras</h3>
<p>Toque <strong>dos sílabas</strong> en orden y pulse <strong>Leer mi palabra</strong>. Algunas combinaciones forman palabras de verdad (<em>casa, mesa, pato</em>…) y otras son inventadas. ¿Cuántas de verdad encuentra?</p>
<div class="constructor" data-grupos='{json.dumps([SILABAS])}' data-sep="" data-max="2" data-reales='{json.dumps(REALES, ensure_ascii=False)}' data-titulos='["Sílabas"]'>
<div class="cons-fichas"></div>
<p><strong>Su palabra:</strong></p><p class="cons-frase" aria-live="polite"></p>
<p><button type="button" class="btn cons-leer"><span aria-hidden="true">🔊</span> Leer mi palabra</button> <button type="button" class="btn-sec cons-limpiar">Limpiar</button></p>
<div class="fb" role="status" aria-live="polite"></div>
<p><strong>Palabras de verdad que encontró:</strong></p><ul class="cons-lista"></ul>
</div>
{P("Compruebe", "¿Qué palabra se forma con <strong>me</strong> + <strong>sa</strong>?", ["mesa", "sama", "misa"], 0,
   {1: "El orden importa: primero me, después sa.", 2: "Mire bien la primera sílaba: tiene e, no i."}, "<strong>me + sa = mesa</strong>.")}"""

    filas_l = "".join(f'<tr><th scope="row">{w}</th><td>{sep}</td><td>{LE.escuchar(sep.replace("-", ". ") + ".", "por sílabas", 0.55)} {LE.escuchar(w, "entera", 0.85)}</td></tr>' for w, sep in LISTA)
    s3 = f"""<p>Estas palabras de dos sílabas aparecen muchísimo en la vida diaria. Léalas en voz alta: primero <strong>por sílabas</strong>, despacio, y después <strong>enteras</strong>. Use los botones solo si se traba.</p>
<div aria-label="Lista de palabras (tabla desplazable horizontalmente)" class="tabla-scroll" role="region" tabindex="0"><table class="tabla-trad"><caption class="cap-oculto">Palabras de dos sílabas para leer</caption>
<thead><tr><th scope="col">Palabra</th><th scope="col">Por sílabas</th><th scope="col">Escuchar</th></tr></thead><tbody>{filas_l}</tbody></table></div>
{C.caja("tip", "Tres veces cada palabra", "<p>Lea cada palabra por sílabas, después entera, y otra vez entera. Con la práctica, la pausa entre sílabas desaparece y la palabra sale de un golpe. Es como aprender a manejar: al principio se siente cada movimiento; con el tiempo, sale solo.</p>")}
{C.caja("ojo", "Sílabas con dos consonantes", "<p>En <em>tigre</em>, la segunda sílaba es <strong>gre</strong>: dos consonantes juntas (g y r) antes de la vocal. Lo mismo pasa en <em>flor, tren, plato, libro</em>. Se leen juntas, de un golpe: <em>ti-gre</em>, no <em>tig-re</em>.</p>")}
<h3>Pruébese con palabras nuevas</h3>
<p>Lea estas palabras, que no ha practicado, decodificando sílaba por sílaba. Después confirme con el botón:</p>
<p class="frecuentes">{" ".join(f'<strong style="font-size:1.4em">{w}</strong> {LE.escuchar(w, "", 0.8)}' for w in ["gato", "pelo", "lima", "sopa", "dedo"])}</p>"""

    secciones = [("s1", "¿Qué es decodificar?", s1), ("s2", "Palabras de una y dos sílabas", s2), ("s3", "Lectura independiente", s3)]
    tarea = [("Mis diez palabras.", "Copie las doce palabras de la sección 3, sepárelas en sílabas con guiones (<em>me-sa</em>) y léalas tres veces: por sílabas, de corrido y otra vez de corrido."),
             ("Arme palabras.", "Con el constructor de la sección 2, encuentre por lo menos ocho palabras de verdad y escríbalas en el cuaderno."),
             ("Palabras de la casa.", "Busque cinco cosas de su casa cuyo nombre tenga una o dos sílabas (<em>sal, taza, silla</em>). Escriba cada nombre y cuántas sílabas tiene."),
             ("Lea un empaque.", "Tome una caja o una lata de la cocina y lea tres palabras cortas, sílaba por sílaba.")]
    quiz = [
        ("¿Qué es <strong>decodificar</strong>?", ["Escribir muy rápido", "Unir el sonido de cada letra para leer la palabra", "Memorizar el abecedario"], 1, {0: "Decodificar es leer, no escribir.", 2: "Saber el abecedario ayuda, pero decodificar es leer palabras."}, "Decodificar es <strong>pasar de las letras a los sonidos</strong> y unirlos."),
        ("Para leer, ¿qué se usa?", ["El nombre de la letra", "El sonido de la letra"], 1, {}, "El <strong>sonido</strong>: con el nombre no sale la palabra."),
        ("¿Cómo <strong>suena</strong> la letra M?", ["«eme»", "«mmm»", "«ma»"], 1, {0: "Ese es su nombre.", 2: "Eso ya es una sílaba: m más a."}, "Suena <strong>«mmm»</strong>, con los labios cerrados."),
        ("¿Cuál de estas palabras tiene <strong>una</strong> sola sílaba?", ["mesa", "luz", "pato"], 1, {0: "Me-sa: dos golpes.", 2: "Pa-to: dos golpes."}, "<strong>luz</strong>: un solo golpe."),
        ("¿Qué palabra se forma con <strong>va</strong> + <strong>ca</strong>?", ["cava", "vaca", "vaso"], 1, {0: "El orden importa: primero va.", 2: "La segunda sílaba es ca, no so."}, "<strong>vaca</strong>."),
        ("¿Qué palabra se forma con <strong>pa</strong> + <strong>to</strong>?", ["pato", "topa", "pata"], 0, {1: "El orden importa: primero pa.", 2: "La segunda sílaba termina en o."}, "<strong>pato</strong>."),
        ("¿Cómo se divide <strong>bota</strong>?", ["b-ota", "bo-ta", "bot-a"], 1, {0: "Una sílaba necesita su vocal: la b sola no es sílaba.", 2: "Cada sílaba empieza con consonante cuando puede: bo…"}, "<strong>bo-ta</strong>."),
        ("¿Cómo se divide <strong>tigre</strong>?", ["tig-re", "ti-gre", "t-igre"], 1, {0: "La g y la r van juntas antes de la vocal.", 2: "La t sola no es sílaba."}, "<strong>ti-gre</strong>: gr va junto."),
        ("¿Qué sílaba falta? <strong>me__</strong> (lo que se usa para comer)", ["so", "sa", "se"], 1, {0: "«Meso» no existe.", 2: "«Mese» no existe."}, "<strong>me-sa</strong>."),
        ("¿Qué sílaba falta? <strong>__to</strong> (un animal que hace cua, cua)", ["ga", "pa", "ma"], 1, {0: "El gato hace miau.", 2: "«Mato» no es un animal."}, "<strong>pa-to</strong>."),
        ("Al principio, leer por sílabas suena lento. Eso es…", ["Normal: con práctica, la palabra sale de un golpe", "Señal de que no puede aprender"], 0, {}, "Es <strong>normal</strong>. Con la lectura repetida la pausa desaparece."),
    ]
    filas_r = [
        ("Nombre y sonido", "Uso el sonido de cada letra, no su nombre, al leer.", "A veces digo el nombre de la letra.", "Confundo nombre y sonido (<a href=\"#s1\">repase la sección 1</a>)."),
        ("Leer palabras de una y dos sílabas", "Leo palabras de dos sílabas de corrido.", "Las leo, pero con una pausa larga entre sílabas.", "Me trabo en la mayoría (<a href=\"#s2\">repase la sección 2</a>)."),
        ("Palabras nuevas", "Leo palabras que no he practicado, sílaba por sílaba.", "Necesito escucharlas antes.", "No puedo leerlas solo (<a href=\"#s3\">repase la sección 3</a>)."),
    ]
    cierre = "<p>Ya sabe decodificar: pasar de las letras a los sonidos y de los sonidos a la palabra. En la próxima lección le pondrá velocidad: hay palabras que aparecen tanto que conviene reconocerlas de un vistazo, sin decodificarlas cada vez.</p>"
    glosario = [("Decodificar", "Leer una palabra pasando de cada letra a su sonido y uniendo los sonidos."), ("Principio alfabético", "La idea de que las letras representan sonidos."),
                ("Monosílaba", "Palabra de una sola sílaba: <em>pan, sol</em>."), ("Bisílaba", "Palabra de dos sílabas: <em>me-sa</em>.")]
    conexion = ("<p>Ya tiene el oído entrenado: sabe contar sílabas, oír rimas y aislar sonidos. Hoy va a unir esos sonidos con las letras escritas.</p>"
                "<p><strong>Lo que necesita:</strong> el cuaderno, dos papelitos de colores y el volumen activado.</p>")
    estd = LE.estandares([], fund=["RF.3", "RF.2"])
    return C.pagina_leccion(N, LE.titulo(N), "Letra por letra, sonido por sonido: así nace una palabra.", ["Fundamentos de lectura", "Decodificación"],
                            ["<strong>Distinguir</strong> el nombre de cada letra de su sonido.", "<strong>Unir</strong> sonidos y sílabas para leer palabras de una y dos sílabas.",
                             "<strong>Separar</strong> en sílabas palabras de dos sílabas, también con dos consonantes juntas (<em>ti-gre</em>).", "<strong>Leer</strong> palabras nuevas sílaba por sílaba."],
                            estd, conexion, secciones, tarea, quiz, filas_r, cierre, ("2-3", LE.titulo("2-3")), glosario, P)


# ---------------------------------------------------------------- práctica
def banco_forma():
    datos = [("me", "sa", "mesa", ["sama", "misa"]), ("pa", "to", "pato", ["topa", "pata"]), ("ca", "sa", "casa", ["saca", "cosa"]), ("lu", "na", "luna", ["nalu", "lana"]),
             ("bo", "ca", "boca", ["cabo", "bota"]), ("ga", "to", "gato", ["toga", "gota"]), ("ma", "no", "mano", ["nomo", "mono"]), ("si", "lla", "silla", ["llasi", "sella"]),
             ("le", "che", "leche", ["chele", "lecha"]), ("va", "so", "vaso", ["sova", "beso"]), ("pe", "lo", "pelo", ["lope", "palo"]), ("ti", "gre", "tigre", ["greti", "tigra"]),
             ("pla", "to", "plato", ["topla", "pato"]), ("li", "bro", "libro", ["broli", "libre"])]
    return [{"enun": f"¿Qué palabra se forma con <strong>{a}</strong> + <strong>{b}</strong>?", "ops": [w] + d, "ok": 0,
             "pista": "Lea las dos sílabas en el orden en que están y júntelas.", "exp": f"<strong>{a} + {b} = {w}</strong>."} for a, b, w, d in datos]


def banco_falta():
    datos = [("me", "__", "sa", "Lo que se usa para comer.", ["sa", "so", "se"]), ("__", "to", "pa", "Un animal que dice cua, cua.", ["pa", "ga", "ma"]),
             ("lu", "__", "na", "Se ve en el cielo de noche.", ["na", "ma", "no"]), ("__", "sa", "ca", "Donde vive una familia.", ["ca", "co", "ma"]),
             ("ma", "__", "no", "Tiene cinco dedos.", ["no", "na", "to"]), ("__", "che", "le", "La toma el bebé.", ["le", "la", "no"]),
             ("ga", "__", "to", "Un animal que dice miau.", ["to", "ta", "lo"]), ("__", "ca", "bo", "Con ella hablamos y comemos.", ["bo", "ba", "to"]),
             ("si", "__", "lla", "Sirve para sentarse.", ["lla", "lo", "ya"]), ("__", "da", "rue", "La tiene un carro o una bicicleta.", ["rue", "ro", "ra"])]
    b = []
    for a, x, ok, pista, ops in datos:
        w = (a + ok) if x == "__" else (ok + x)
        mostrado = f"{a}__" if x == "__" else f"__{x}"
        b.append({"enun": f"¿Qué sílaba falta? <strong class=\"grande\">{mostrado}</strong><br><em>{pista}</em>", "ops": ops, "ok": 0,
                  "pista": "Pruebe cada sílaba en voz alta y quédese con la que forma la palabra de la pista.", "exp": f"<strong>{w}</strong>."})
    return b


def banco_dibujo():
    datos = [("vaca", "🐄", ["🐴", "🐖"]), ("pato", "🦆", ["🐔", "🐟"]), ("silla", "🪑", ["🛏️", "🚪"]), ("luna", "🌙", ["☀️", "⭐"]), ("boca", "👄", ["👃", "👂"]),
             ("pan", "🍞", ["🧀", "🍎"]), ("sol", "☀️", ["🌙", "☁️"]), ("taza", "☕", ["🍽️", "🥄"]), ("dado", "🎲", ["🃏", "⚽"]), ("gato", "🐱", ["🐶", "🐭"]),
             ("pelota", "⚽", ["🎲", "🎈"]), ("llave", "🔑", ["🔒", "🚪"]), ("foca", "🦭", ["🐟", "🐧"]), ("taxi", "🚕", ["🚌", "🚲"])]
    return [{"enun": f"Lea la palabra: <strong class=\"grande\">{w}</strong><br>¿Qué dibujo es?", "ops": [f'<span class="emoji-grande" role="img" aria-label="{w}">{e}</span>'] +
             [f'<span class="emoji-grande" aria-hidden="true">{d}</span><span class="cap-oculto">otro dibujo</span>' for d in ds], "ok": 0,
             "pista": "Léala sílaba por sílaba, en voz alta, y piense qué cosa es.", "exp": f"<strong>{w}</strong>."} for w, e, ds in datos]


def banco_nombre():
    b = []
    for L, nom, son, tipo, clave, ej in LETRAS:
        b.append({"enun": f"¿Cuál es el <strong>sonido</strong> de la letra <strong class=\"grande\">{L}</strong>?", "ops": [f"/{son.split(' (')[0]}/", f"«{nom}»"], "ok": 0, "enOrden": False,
                  "exp": f"La {L} se llama «{nom}», pero suena <strong>/{son}/</strong>, como en <em>{ej}</em>."})
    return b


def practica():
    mods = [
        ("formar", "¿Qué palabra se forma?", C.om("m1", "Junte las dos sílabas en el orden en que están.")),
        ("falta", "¿Qué sílaba falta?", C.om("m2", "Use la pista para saber qué palabra es.")),
        ("dibujo", "Lea y elija el dibujo", C.om("m3", "Lea la palabra sílaba por sílaba y elija lo que nombra.")),
        ("sonido", "¿Nombre o sonido?", C.om("m4", "Elija cómo suena la letra dentro de una palabra.")),
    ]
    js = (C.js_datos("FOR", banco_forma()) + C.js_datos("FAL", banco_falta()) + C.js_datos("DIB", banco_dibujo()) + C.js_datos("NOM", banco_nombre()) +
          'creaBanco("m1", FOR);\ncreaBanco("m2", FAL);\ncreaBanco("m3", DIB);\ncreaBanco("m4", NOM);\n')
    return C.pagina_practica(N, LE.titulo(N), "Cuatro actividades · los ejercicios cambian cada vez · dos intentos en cada uno", mods, js)


if __name__ == "__main__":
    LE.construye(N, leccion, practica, horas="Unas 3 horas")
