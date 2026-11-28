# -*- coding: utf-8 -*-
"""Artes del lenguaje, camino en español: la Bienvenida y el índice de cada nivel.

  es/artes-del-lenguaje/nivel-N/bienvenida.html   «¿Qué es el GED?», primera página del nivel (solo Nivel 1)
  es/artes-del-lenguaje/nivel-N/index.html        índice del nivel: los ocho temas y sus lecciones

Un enlace a una lección solo aparece si su página ya existe, así que basta volver a correr el
script cada vez que se construye una lección nueva. Después corra tools/build_planes.py.
Uso: python3 tools/build_leng_indices.py
"""
import html, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_planes as P
import leng_es as LE

e = html.escape
RAIZ = P.RAIZ
COLOR = {1: "#0b679c", 2: "#00695c", 3: "#6d28d9", 4: "#b42318"}

CSS = """<style>
  .lecciones{list-style:none;padding:0;margin:0}
  .lecciones li{display:flex;flex-wrap:wrap;gap:6px 12px;align-items:baseline;padding:7px 0;border-top:1px solid #eef0f2}
  .lecciones li:first-child{border-top:0}
  .lecciones .n{font-weight:700;color:var(--muted);min-width:2.2em}
  .lecciones a.lec{font-weight:700}
  .lecciones .prac{font-size:.9em}
  .lecciones .pronto{color:var(--muted)}
  .empiece{display:flex;gap:14px;align-items:center;background:#eaf4fa;border:1px solid #b9d7ea;border-radius:12px;padding:12px 18px;margin:10px 0 16px;max-width:60em}
  .empiece img{width:70px;height:auto;flex:none}
  .empiece p{margin:0}
  .materias{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:10px;margin:10px 0}
  .materias div{background:#fff;border:1px solid var(--line);border-top:5px solid #0b679c;border-radius:10px;padding:10px 14px}
  .materias .ico{font-size:1.6em}
  .materias strong{display:block;color:var(--navy)}
  .cita-gran{font-size:1.12em;font-weight:700;color:#004b75;border-left:6px solid #0b679c;padding:6px 14px;margin:12px 0;background:#eaf4fa;border-radius:0 10px 10px 0}
  .cq{background:#fff;border:1px solid var(--line);border-radius:12px;padding:12px 16px;margin:10px 0}
  .cq .enun{font-weight:700;margin:0 0 8px}
  .cq button{display:block;width:100%;text-align:left;font:inherit;background:#fff;border:2px solid #c9d2da;border-radius:10px;padding:8px 12px;margin:6px 0;cursor:pointer;color:var(--ink)}
  .cq button:hover,.cq button:focus-visible{border-color:#0b679c}
  .cq button.si{border-color:#2e7d32;background:#e8f5e9}
  .cq button.no{border-color:#f9a825;background:#fff8e1}
  .cq .exp{margin:8px 0 0;background:#eaf4fa;border-left:5px solid #0b679c;border-radius:8px;padding:8px 12px}
</style>"""

BIENVENIDA_QUIZ = [
    ("¿Qué significan las siglas GED?", ["Graduación Educativa de Diploma", "<span lang=\"en\">General Educational Development</span> (Desarrollo Educativo General)", "Grupo de Estudios Diarios"], 1,
     "GED significa <em lang=\"en\">General Educational Development</em>. Es un examen oficial de los Estados Unidos que certifica conocimientos equivalentes a los de la escuela secundaria."),
    ("¿Cuántas materias evalúa el examen del GED?", ["Dos", "Cuatro", "Seis"], 1, "Cuatro: Razonamiento a través de las artes del lenguaje, Matemáticas, Ciencias y Estudios Sociales."),
    ("¿Qué representa el GED para quien lo obtiene?", ["Un título universitario", "El equivalente al diploma de escuela secundaria (<em lang=\"en\">high school</em>)", "Un certificado de inglés"], 1,
     "El GED equivale al diploma de escuela secundaria. Con él se abren trabajos y estudios que piden ese nivel."),
    ("¿En qué idiomas se puede presentar el GED en los Estados Unidos?", ["Solo en inglés", "En inglés y en español", "En cualquier idioma"], 1, "El GED se puede presentar en inglés o en español. Este curso le prepara para el examen en español."),
    ("¿Dónde se presenta el examen?", ["En la casa, sin supervisión", "En un centro oficial o en línea con supervisión", "En cualquier biblioteca"], 1,
     "En un centro oficial autorizado o en línea con supervisión a distancia. Así el certificado es válido y reconocido."),
    ("¿Qué tipo de habilidades evalúa sobre todo el GED?", ["Memorizar datos", "Pensar, analizar y resolver problemas", "Habilidades artísticas"], 1,
     "El GED evalúa sobre todo comprender, analizar, razonar y resolver problemas: lo mismo que se necesita en el trabajo y en la vida diaria."),
    ("Si una persona no terminó la secundaria, ¿qué significa que estudie para el GED?", ["Que ya es tarde para aprender", "Que está tomando el control de su futuro", "Que solo busca un papel"], 1,
     "Estudiar para el GED es una decisión valiente: esfuerzo, perseverancia y ganas de mejorar. Es una segunda oportunidad real."),
]


def bienvenida():
    c = ['<h1>Bienvenida · ¿Qué es el GED y por qué es importante?</h1>',
         '<p class="intro">Artes del lenguaje · Nivel 1: Iniciación a la lectura y la escritura · Antes de empezar · Unos 30 minutos</p>',
         P.indice("es", [("ged", "¿Qué es el GED?"), ("materias", "Las cuatro materias"), ("puertas", "Las puertas que abre"),
                         ("piense", "Piense un momento"), ("curso", "Cómo funciona este curso"), ("cuestionario", "Cuestionario de bienvenida")])]
    c.append(P.bloque("ged", "¿Qué es el GED?",
        "<p>GED significa <em lang=\"en\">General Educational Development</em> (Desarrollo Educativo General). Son cuatro exámenes que demuestran que una persona tiene los conocimientos y las habilidades de alguien que terminó la escuela secundaria (<em lang=\"en\">high school</em>) en los Estados Unidos.</p>"
        "<p>Mucha gente no pudo terminar la escuela por el trabajo, la familia, un cambio de país o dificultades económicas o personales. No haberla terminado entonces no significa que no se pueda lograr ahora. El GED es esa segunda oportunidad.</p>"
        '<p class="cita-gran">El GED le dice al mundo: «Tengo lo necesario para seguir adelante».</p>', "es"))
    c.append(P.bloque("materias", "Las cuatro materias del GED",
        '<div class="materias">'
        '<div><span class="ico" aria-hidden="true">📖</span><strong>Razonamiento a través de las artes del lenguaje</strong>Leer, comprender, corregir textos y escribir. Es la materia de este curso.</div>'
        '<div><span class="ico" aria-hidden="true">🔢</span><strong>Razonamiento matemático</strong>Números, problemas, álgebra básica, geometría y datos.</div>'
        '<div><span class="ico" aria-hidden="true">🔬</span><strong>Ciencias</strong>Vida, física, química, la Tierra y el espacio, y cómo leer información científica.</div>'
        '<div><span class="ico" aria-hidden="true">🌎</span><strong>Estudios sociales</strong>Cívica, historia, economía y geografía.</div></div>'
        "<p>No se trata de memorizar: el GED evalúa si usted sabe pensar, analizar y resolver problemas.</p>"
        "<p><strong>¿Por qué empezar por el lenguaje?</strong> Porque leer bien ayuda en todas las demás: en Matemáticas hay que entender el problema, y en Ciencias y Estudios Sociales hay que leer textos, tablas y gráficas.</p>", "es"))
    c.append(P.bloque("puertas", "Las puertas que abre el GED",
        P.lista(["Mejores oportunidades de empleo.", "Estudiar en un colegio comunitario (<em lang=\"en\">community college</em>).", "Programas técnicos y universitarios.",
                 "Más confianza en usted mismo.", "Ser un ejemplo para sus hijos y su familia."]) +
        "<p>Para muchos estudiantes, el GED es más que un examen: es sacrificio, esfuerzo y esperanza; la decisión de no rendirse. No significa que usted fracasó ni que es demasiado tarde. Significa que está tomando el control de su futuro.</p>", "es"))
    c.append(P.bloque("piense", "Piense un momento",
        "<p>Tome su cuaderno. En la primera página, responda con sus propias palabras. No hay respuestas buenas ni malas: son solo para usted.</p>"
        "<ol><li>¿Por qué decidí estudiar para el GED?</li><li>¿Qué cambiará en mi vida cuando lo obtenga?</li><li>¿Qué ejemplo quiero dar a mi familia?</li></ol>"
        '<p class="cita-gran">Guarde esa página. El día que esté cansado o con ganas de dejarlo, vuelva a leer lo que escribió hoy.</p>', "es"))
    temas = "".join(f"<li>{v}</li>" for v in LE.NIVELES[1][1].values())
    c.append(P.bloque("curso", "Cómo funciona este curso",
        "<p>Artes del lenguaje tiene <strong>cuatro niveles</strong>, y cada uno se apoya en el anterior:</p>"
        "<ol><li><strong>Iniciación a la lectura y la escritura</strong> (este nivel): las letras, los sonidos, la oración y las primeras estrategias para entender lo que lee.</li>"
        "<li><strong>Conectando ideas y textos</strong>: cómo se arman los textos y cómo se relacionan sus ideas.</li>"
        "<li><strong>Exploración del análisis y la argumentación</strong>: leer con ojo crítico, buscar evidencia y defender una opinión.</li>"
        "<li><strong>Dominio del GED y escritura argumentativa</strong>: la preparación directa para el examen, incluida la respuesta extendida.</li></ol>"
        "<p>Está hecho para estudiar por su cuenta, a su ritmo, en la computadora o en el celular:</p>" +
        P.lista(["<strong>8 temas</strong> con varias lecciones cada uno. Conviene seguirlas en orden.",
                 "Cada lección empieza con lo que va a aprender y un índice: toque cualquier parte para ir directo a ella.",
                 "En la lección hay preguntas para comprobar lo que entendió. Si se equivoca, recibe una pista y otro intento; al segundo error, la explicación.",
                 "Cada lección tiene su <strong>página de práctica</strong>, con ejercicios que cambian cada vez, una tarea para el cuaderno y un quiz que puede repetir.",
                 "Muchas lecciones tienen botones 🔊 para escuchar. Use audífonos o active el volumen."]) +
        "<h3>Lo que necesita</h3>" + P.lista(["Un cuaderno y un lápiz; si puede, dos lápices o resaltadores de colores distintos.",
                                              "Un rato tranquilo cada día. Es mejor estudiar media hora todos los días que cuatro horas un solo día."]) +
        f"<h3>Los ocho temas del Nivel 1</h3><ol>{temas}</ol>", "es"))
    qs = "".join(
        f'<div class="cq" data-ok="{k}"><p class="enun">{i}. {q}</p>' + "".join(f'<button type="button" data-j="{j}">{o}</button>' for j, o in enumerate(ops)) +
        f'<p class="exp" role="status" hidden>{x}</p></div>' for i, (q, ops, k, x) in enumerate(BIENVENIDA_QUIZ, 1))
    c.append(P.bloque("cuestionario", "Cuestionario de bienvenida · sin nota",
        "<p>Este cuestionario no tiene nota: sirve para descubrir lo que ya sabe del GED. Al elegir una respuesta verá una breve explicación.</p>" + qs +
        '<p class="cita-gran">Lo importante no es cuántas acertó, sino que ya dio el primer paso.</p>'
        '<p><a class="btn" href="leccion-1-1.html">Empezar: Lección 1.1 · El alfabeto ›</a></p>', "es"))
    js = """<script>
document.querySelectorAll('.cq').forEach(function(q){
  var ok=q.getAttribute('data-ok'), exp=q.querySelector('.exp');
  q.addEventListener('click',function(ev){
    var b=ev.target.closest('button'); if(!b||b.disabled)return;
    var bien=b.getAttribute('data-j')===ok;
    b.classList.add(bien?'si':'no');
    if(bien){ q.querySelectorAll('button').forEach(function(x){x.disabled=true;}); exp.innerHTML='✓ '+exp.innerHTML.replace(/^✓ |^Todavía no\\. /,''); }
    else if(!exp.dataset.v){ exp.dataset.v=1; exp.innerHTML='Todavía no. '+exp.innerHTML; }
    exp.hidden=false;
  });
});
</script>"""
    return "".join(c), js


def indice_nivel(n):
    nombre, temas = LE.NIVELES[n]
    lecs = LE.LECCIONES[n]
    base = f"es/artes-del-lenguaje/nivel-{n}"
    hechas = [k for k in lecs if os.path.exists(os.path.join(RAIZ, base, f"leccion-{k}.html"))]
    c = [f"<h1>Artes del lenguaje · Nivel {n}: {nombre}</h1>",
         f'<p class="intro">{len(lecs)} lecciones en 8 temas, en español. Cada lección tiene su página de práctica. Conviene seguirlas en orden.</p>']
    if n == 1:
        c.append('<div class="empiece"><img src="/img/leo-saludo.svg" alt=""><p><strong>¿Es su primera vez?</strong> Empiece por la <a href="bienvenida.html">Bienvenida · ¿Qué es el GED?</a> (unos 30 minutos) y después siga con la Lección 1.1.</p></div>')
    if len(hechas) < len(lecs):
        c.append(P.estado("es", f"<strong>En preparación.</strong> Ya están listas {len(hechas)} de las {len(lecs)} lecciones; las demás se irán publicando tema por tema."))
    c.append(P.indice("es", [(f"tema-{k}", f"Tema {k}") for k in temas]))
    for k, tt in temas.items():
        items = []
        for cl, tl in lecs.items():
            if int(cl.split("-")[0]) != k:
                continue
            num = cl.replace("-", ".")
            if cl in hechas:
                items.append(f'<li><span class="n">{num}</span><a class="lec" href="leccion-{cl}.html">{e(tl)}</a> <a class="prac" href="practica-{cl}.html">Práctica</a></li>')
            else:
                items.append(f'<li><span class="n">{num}</span><span class="pronto">{e(tl)}</span></li>')
        c.append(P.bloque(f"tema-{k}", f"Tema {k} · {e(tt)}", f'<ul class="lecciones">{"".join(items)}</ul>', "es"))
    c.append(f'<p><a href="/es/artes-del-lenguaje/estandares-ged.html">Estándares del GED® y CCR de Artes del lenguaje</a> · <a href="/es/artes-del-lenguaje/">Plan del curso</a></p>')
    return "".join(c)


def escribe(ruta, titulo, cuerpo, migas, js=""):
    s = P.pagina("es", titulo, "/rla/", "/" + os.path.dirname(ruta) + "/", cuerpo, migas[-1][1])
    s = s.replace("</head>", CSS + "\n</head>", 1).replace("built by tools/build_planes.py", "built by tools/build_leng_indices.py")
    pasos = "".join(f'<a href="{u}">{e(t)}</a> <span aria-hidden="true">›</span> ' for u, t in migas[:-1])
    s = s.replace('<span aria-hidden="true">›</span> <span aria-current="page">', f'<span aria-hidden="true">›</span> {pasos}<span aria-current="page">', 1)
    if js:
        s = s.replace("</body>", js + "\n</body>", 1)
    p = os.path.join(RAIZ, ruta)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "w", encoding="utf-8").write(s)
    print("ok", ruta)


def main():
    cuerpo, js = bienvenida()
    escribe("es/artes-del-lenguaje/nivel-1/bienvenida.html", "Bienvenida · ¿Qué es el GED? · Artes del lenguaje · Nivel 1", cuerpo,
            [("/es/artes-del-lenguaje/", "Artes del lenguaje"), ("/es/artes-del-lenguaje/nivel-1/", "Nivel 1"), (None, "Bienvenida")], js)
    for n in LE.NIVELES:
        escribe(f"es/artes-del-lenguaje/nivel-{n}/index.html", f"Artes del lenguaje · Nivel {n}", indice_nivel(n),
                [("/es/artes-del-lenguaje/", "Artes del lenguaje"), (None, f"Nivel {n}")])


if __name__ == "__main__":
    main()
