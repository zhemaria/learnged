# -*- coding: utf-8 -*-
"""Página de consulta de los estándares de Artes del Lenguaje (RLA), en inglés y en español.

  rla/ged-standards.html                  (inglés)
  es/artes-del-lenguaje/estandares-ged.html (español)

Reúne, con los datos de tools/rla.py: el formato del examen, los indicadores de cada objetivo
con su DOK y su estándar ancla CCR, los tres rasgos de la respuesta extendida y las trampas de
corrección de cada examen (inglés y español). Sirve a los dos caminos del curso y a los
profesores revisores. Las lecciones enlazan aquí desde su recuadro de estándares.
Corra:  python3 tools/build_rla_estandares.py
"""
import os, sys, html
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rla as R
import build_planes as P

e = html.escape
RAIZ = P.RAIZ
EN_URL, ES_URL = "/rla/ged-standards.html", "/es/artes-del-lenguaje/estandares-ged.html"

CSS_EXTRA = """<style>
  .std-tabla{width:100%;border-collapse:collapse;margin:6px 0 14px;font-size:.95em;background:#fff}
  .std-tabla caption{text-align:left;font-weight:700;color:var(--navy);padding:4px 0 6px}
  .std-tabla th,.std-tabla td{border:1px solid var(--line);padding:6px 9px;vertical-align:top;text-align:left}
  .std-tabla thead th{background:#eef4f8;color:var(--navy)}
  .std-tabla th[scope=row]{white-space:nowrap;color:var(--teal-d)}
  .std-tabla td.dok{white-space:nowrap;text-align:center}
  .scroll{overflow-x:auto}
  .trampa s{color:#8a1c1c;text-decoration-thickness:2px}
  .trampa b{color:#14532d}
  .rasgos{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:12px}
  .rasgos div{border:1px solid var(--line);border-top:5px solid var(--teal);border-radius:10px;padding:10px 14px;background:#fff}
  .rasgos h3{margin:0 0 4px}
  .rasgos p{margin:0}
  body.hc .std-tabla th,body.hc .std-tabla td{border-color:#000}
</style>"""


def tabla_obj(lang, obj):
    en = lang == "en"
    tit_en, tit_es, anclas, _ = R.OBJETIVOS[obj]
    cap = "%s · %s (CCR %s)" % (obj, tit_en if en else tit_es, ", ".join(anclas))
    filas = "".join('<tr><th scope="row">%s</th><td>%s</td><td class="dok">%s</td></tr>' % (c, v[2] if en else v[3], v[1])
                    for c, v in R.RLA.items() if v[0] == obj)
    return ('<div class="scroll"><table class="std-tabla"><caption>%s</caption><thead><tr><th scope="col">%s</th><th scope="col">%s</th><th scope="col">DOK</th></tr></thead><tbody>%s</tbody></table></div>'
            % (e(cap), "Code" if en else "Código", "Indicator" if en else "Indicador", filas))


def tabla_trampas(lang, cual):
    en = lang == "en"
    if cual == "en":
        filas = [(c, (x[0] if en else x[1]), ej) for c, x, ej in R.CONVENCIONES_EN]
        cap = "Editing traps on the GED test in English" if en else "Trampas de corrección del examen GED en inglés"
    else:
        filas = R.CONVENCIONES_ES
        cap = "Editing traps on the GED test in Spanish (the rules of Spanish)" if en else "Trampas de corrección del examen GED en español (norma del español)"
    lt = ' lang="es"' if (cual == "es" and en) else ""
    cuerpo = "".join('<tr><th scope="row">%s</th><td%s>%s</td><td class="trampa" lang="%s">%s</td></tr>' % (c, lt, txt, cual, ej)
                     for c, txt, ej in filas)
    return ('<div class="scroll"><table class="std-tabla"><caption>%s</caption><thead><tr><th scope="col">%s</th><th scope="col">%s</th><th scope="col">%s</th></tr></thead><tbody>%s</tbody></table></div>'
            % (e(cap), "Code" if en else "Código", "What is tested" if en else "Qué se evalúa",
               "Example (<s>wrong</s> → <b>right</b>)" if en else "Ejemplo (<s>error</s> → <b>correcto</b>)", cuerpo))


def cuerpo(lang):
    en = lang == "en"
    R.L = lang
    c = ['<h1>%s</h1>' % ("Reasoning through language arts · GED® standards" if en else "Artes del lenguaje · Estándares del GED®")]
    c.append('<p class="intro">%s</p>' % (
        "What the GED® Reasoning Through Language Arts test measures, indicator by indicator, and how each one lines up with the College and Career Readiness (CCR) standards for adults. Both paths of the course, in English and in Spanish, use this same map: the GED test in Spanish has the same indicators; only the language rules that are corrected change."
        if en else
        "Qué mide el examen GED® de Razonamiento a través de las Artes del Lenguaje, indicador por indicador, y cómo se alinea cada uno con los estándares CCR (College and Career Readiness) para adultos. Los dos caminos del curso, en español y en inglés, usan este mismo mapa: el examen GED en español tiene los mismos indicadores; solo cambian las normas del idioma que se corrigen."))
    c.append(P.indice(lang, [("format", "The test" if en else "El examen"),
                             ("reading", R.DOMINIOS["lectura"][0 if en else 1]),
                             ("arguments", R.DOMINIOS["argumento"][0 if en else 1]),
                             ("writing", R.DOMINIOS["escritura"][0 if en else 1]),
                             ("language", R.DOMINIOS["lenguaje"][0 if en else 1]),
                             ("traps", "Editing traps" if en else "Trampas de corrección"),
                             ("ccr", "CCR anchor standards" if en else "Estándares ancla CCR")]))
    cats = "".join("<li>%s</li>" % (a if en else b) for a, b in R.CATEGORIAS)
    c.append(P.bloque("format", "The test" if en else "El examen",
                      P.lista(R.FORMATO[lang]) + '<h3>%s</h3><ol>%s</ol>' % ("Reporting categories on the score report" if en else "Categorías del informe de resultados", cats), lang))
    for id_, dom, objs in (("reading", "lectura", ["R.2", "R.3", "R.4", "R.5", "R.6", "R.7/R.9"]),
                           ("arguments", "argumento", ["R.8"]),
                           ("writing", "escritura", ["W.1", "W.2", "W.3"]),
                           ("language", "lenguaje", ["L.1", "L.2"])):
        extra = ""
        if id_ == "writing":
            extra = '<h3>%s</h3><div class="rasgos">%s</div>' % (
                "The three traits of the extended response" if en else "Los tres rasgos de la respuesta extendida",
                "".join('<div><h3>%s</h3><p>%s</p></div>' % (tt[0] if en else tt[1], d[0] if en else d[1]) for tt, d in R.RASGOS))
            extra += '<p>%s</p>' % (
                "An essay that is off topic, that only copies the texts, or that gives only a personal opinion without analyzing the two arguments earns very few points or none. Write in your own words and quote the texts only to support what you say."
                if en else
                "Un ensayo que se sale del tema, que solo copia los textos o que solo da una opinión personal sin analizar los dos argumentos obtiene muy pocos puntos o ninguno. Escriba con sus propias palabras y cite los textos solo para apoyar lo que dice.")
        if id_ == "language":
            extra = '<p>%s</p>' % (
                "On the test, these indicators appear as drop-down items inside a short workplace or everyday text, and they also count in Trait 3 of the extended response."
                if en else
                "En el examen, estos indicadores aparecen como menús desplegables dentro de un texto breve del trabajo o de la vida diaria, y cuentan también en el Rasgo 3 de la respuesta extendida.")
        cuerpo_b = "".join(tabla_obj(lang, o) for o in objs) + extra
        c.append(P.bloque(id_, R.DOMINIOS[dom][0 if en else 1], cuerpo_b, lang))
    primero, segundo = ("en", "es") if en else ("es", "en")
    c.append(P.bloque("traps", "Editing traps" if en else "Trampas de corrección",
                      tabla_trampas(lang, primero) + tabla_trampas(lang, segundo), lang,
                      sub=("The L codes are the same on both tests, but each language has its own traps. The path in English works with the first table; the path in Spanish, with the second."
                           if en else
                           "Los códigos L son los mismos en los dos exámenes, pero cada idioma tiene sus propias trampas. El camino en español trabaja con la primera tabla; el camino en inglés, con la segunda.")))
    ccr = "".join('<tr><th scope="row">%s</th><td>%s</td></tr>' % (k, v[0] if en else v[1]) for k, v in R.CCR.items())
    c.append(P.bloque("ccr", "CCR anchor standards" if en else "Estándares ancla CCR",
                      '<div class="scroll"><table class="std-tabla"><caption>%s</caption><thead><tr><th scope="col">%s</th><th scope="col">%s</th></tr></thead><tbody>%s</tbody></table></div>'
                      % ("CCR anchor standards used by the RLA test" if en else "Estándares ancla CCR que usa el examen de RLA",
                         "Code" if en else "Código", "What it asks" if en else "Qué pide", ccr) +
                      '<p class="sub">%s</p>' % (
                          "Sources: GED Testing Service, <cite>Assessment Guide for Educators: Reasoning Through Language Arts</cite> (2016), indicators, DOK ranges, and alignment (the indicators are summarized in our own words); Pimentel, S. (2013), <cite>College and Career Readiness Standards for Adult Education</cite>. The Spanish editing traps follow the rules of the Real Academia Española."
                          if en else
                          "Fuentes: GED Testing Service, <cite>Assessment Guide for Educators: Reasoning Through Language Arts</cite> (2016), indicadores, rangos de DOK y alineación (los indicadores están resumidos con palabras propias); Pimentel, S. (2013), <cite>College and Career Readiness Standards for Adult Education</cite>. Las trampas del español siguen la norma de la Real Academia Española."),
                      lang))
    return "".join(c)


def main():
    for lang, f in (("en", "rla/ged-standards.html"), ("es", "es/artes-del-lenguaje/estandares-ged.html")):
        nm = "GED® standards" if lang == "en" else "Estándares del GED®"
        tit = ("Reasoning through language arts · " if lang == "en" else "Artes del lenguaje · ") + nm
        s = P.pagina(lang, tit, EN_URL, ES_URL, cuerpo(lang), nm)
        s = s.replace("</head>", CSS_EXTRA + "\n</head>", 1)
        s = s.replace("built by tools/build_planes.py", "built by tools/build_rla_estandares.py")
        # migas: Inicio › Artes del lenguaje › Estándares
        plan = ("/rla/", "Reasoning through language arts") if lang == "en" else ("/es/artes-del-lenguaje/", "Artes del lenguaje")
        s = s.replace('<span aria-hidden="true">›</span> <span aria-current="page">',
                      '<span aria-hidden="true">›</span> <a href="%s">%s</a> <span aria-hidden="true">›</span> <span aria-current="page">' % plan, 1)
        p = os.path.join(RAIZ, f)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "w", encoding="utf-8") as fh:
            fh.write(s)
        print("ok", f)


if __name__ == "__main__":
    main()
