"""LearnGED · Archivo de fuentes en inglés (social-studies/sources/).
Lo llama tools/build_soc_fuentes.py. Los textos en inglés de cada ficha están en fuentes_en_a.py, _b.py y _c.py (DOCS).
De cada página española del repositorio sociales (tools/fuentes_src/) se toman automáticamente:
  · el color del documento (:root) y la hoja de estilo de la plantilla nueva (la de Brown);
  · los originales en inglés plegados bajo la traducción (cartas, Addams, Holbrook, The Public, Street Railway Journal);
  · los pasajes en su original de los bloques bilingües («· Original»).
De las lecciones de LearnGED se toman los fragmentos en inglés que ya usan (documento() de cada builder), para que el
Archivo y la lección citen exactamente el mismo texto.
"""
import os, re, sys, html as H, importlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sociales import C
import sociales

from fuentes_en_a import DOCS as DA
from fuentes_en_b import DOCS as DB
from fuentes_en_c import DOCS as DC
DOCS = {**DA, **DB, **DC}

TITULO_LECCION = {"1-1": "Compelling and supporting questions", "1-2": "Primary and secondary sources", "1-3": "Bias, point of view, and persuasive language",
                  "3-1": "From the social contract to the Declaration of Independence", "3-2": "The Constitution: structure and principles",
                  "6-1": "Colonies, the Revolution, and building a nation", "6-2": "Expansion, slavery, the Civil War, and Reconstruction",
                  "6-3": "From the 20th century to today", "7-3": "Resources, the environment, and sustainability", "4-1": "The legislative branch: how a bill becomes a law", "4-3": "The judicial branch: judicial review and precedent", "5-1": "The Bill of Rights and the expansion of citizenship"}
ETIQ = {"La imagen": "The image", "El diagnóstico": "The diagnosis", "El límite": "The limit", "La conclusión": "The conclusion", "El daño": "The harm", "El ritmo": "The pace",
        "Declaración 3": "Resolution 3", "Declaración 4": "Resolution 4", "Declaración 1": "Resolution 1", "XIII, sección 1": "XIII, section 1", "XIV, sección 1": "XIV, section 1",
        "XV, sección 1": "XV, section 1", "El anuncio": "The notice", "La causa": "The cause", "El Norte": "“The North”", "Cláusula declarativa": "The declaratory clause",
        "Sección II": "Section II", "Título II": "Title II", "Título VI": "Title VI", "Título de la ley de 1965": "Title of the 1965 act", "Mayoría": "Majority",
        "Discrepancia": "Dissent", "La declaración": "The declaration", "El motivo declarado": "The stated reason", "El interrogatorio en el bosque": "The questioning in the woods",
        "Quiénes eran": "Who they were", "El alcance": "How far it reached"}


def esc(s):
    return H.escape(s, quote=True)


def estilo_base(src):
    s = open(os.path.join(src, "brown-v-board-1954.html"), encoding="utf-8").read()
    css = re.search(r"<style>(.*?)</style>", s, flags=re.S).group(1)
    css = re.sub(r":root\s*\{.*?\}", "", css, count=1, flags=re.S)
    return css


def raiz(src, slug):
    s = open(os.path.join(src, slug + ".html"), encoding="utf-8").read()
    m = re.search(r":root\s*\{.*?\}", s, flags=re.S)
    return m.group(0) if m else ""


def originales(src, slug):
    """Los originales plegados, en orden, con su posición entre los encabezados del documento."""
    s = open(os.path.join(src, slug + ".html"), encoding="utf-8").read()
    return [m.group(1) for m in re.finditer(r'<details class="original">\s*<summary>.*?</summary>\s*<div class="cuerpo-original">(.*?)</div>\s*</details>', s, flags=re.S)]


def pasajes(src, slug):
    s = open(os.path.join(src, slug + ".html"), encoding="utf-8").read()
    out = []
    for et, txt in re.findall(r'<div class="col en"><span class="et">(.*?)</span>(.*?)</div>', s, flags=re.S):
        et = H.unescape(et).replace(" · Original", "").strip()
        out.append((ETIQ.get(et, et), txt.strip()))
    return out


_CAP = {}


def fragmentos_leccion(n, titulo_en):
    """Las partes en inglés de un documento() de la lección n cuyo título en inglés empieza por titulo_en."""
    if n not in _CAP:
        m = importlib.import_module("build_soc_" + n.replace("-", "_"))
        cap = []
        orig = m.documento
        m.documento = lambda titulo, ficha, partes, nota=None: (cap.append((titulo, partes)), orig(titulo, ficha, partes, nota))[1]
        viejo = C.L
        C.L = "en"
        try:
            m.leccion()
        finally:
            C.L = viejo
            m.documento = orig
        _CAP[n] = cap
    for titulo, partes in _CAP[n]:
        if re.sub("<[^>]+>", "", titulo).startswith(titulo_en):
            return partes
    raise KeyError(f"{n}: {titulo_en}")


def tabla(cap, cab, filas):
    th = "".join(f'<th scope="col">{c}</th>' for c in cab)
    tr = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in f) + "</tr>" for f in filas)
    return f'<table class="reglas"><caption>{cap}</caption><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table>'


def caja(tit, txt):
    return f'<div class="aviso"><strong>{tit}</strong> {txt}</div>'


def enlace(url, tit, sub, cta="Open the original"):
    return f'<a class="enlace-original" href="{url}" rel="noopener"><span class="eo-titulo">{tit}</span><span class="eo-sub">{sub}</span><span class="eo-cta">{cta}</span></a>'


def pagina(slug_es, slug_en, d, src, slugs, barra, lgcss, base_css):
    n = d["n"]
    es_de = dict(slugs)
    nav_extra = ""
    if d.get("pair"):
        pe = slugs[d["pair"] - 1][1]
        nav_extra = f'<a class="nav-sig" href="{pe}.html">Paired document: {d["pair"]} <span aria-hidden="true">→</span></a>'
    cuerpo = []
    card = "".join(f"<dt>{k}</dt><dd>{v}</dd>" for k, v in d["card"])
    cuerpo.append(f'<div class="ficha-fuente"><h2>Document record</h2><dl>{card}</dl></div>')
    cuerpo.append('<div class="bloque"><h2>What this document is about</h2>' + "".join(f"<p>{p}</p>" for p in d["about"]) + "</div>")
    for t_, x in d.get("warn", []):
        cuerpo.append(caja(t_, x))
    # ---- el texto original
    if d.get("folded"):
        ors = originales(src, slug_es)
        cuerpo.append(f'<h2 class="seccion">{d["folded"]["title"]}</h2>')
        if d["folded"].get("intro"):
            cuerpo.append(f'<p>{d["folded"]["intro"]}</p>')
        k = 0
        for bloque in d["folded"]["parts"]:
            if isinstance(bloque, str):
                h, _, nt = bloque.partition("||")
                cuerpo.append(f'<h3 class="seccion-sub">{h}</h3>' + (f'<p class="grupo-nota">{nt}</p>' if nt else ""))
                continue
            tit, nota, cuantos = bloque
            for j in range(cuantos):
                h = tit[j] if isinstance(tit, list) else (tit if j == 0 else "")
                cuerpo.append('<div class="documento" lang="en">' + (f"<h3>{h}</h3>" if h else "") + (f'<p class="encabezamiento">{nota}</p>' if nota and j == 0 else "") + ors[k] + "</div>")
                k += 1
        assert k == len(ors), f"{slug_es}: {k} de {len(ors)} originales"
    for n_, tit_en, cab in d.get("excerpts", []):
        partes = fragmentos_leccion(n_, tit_en)
        bl = []
        for sub, en, _es in partes:
            bl.append((f"<h3>{sub}</h3>" if sub else "") + "".join(f"<p>{p}</p>" for p in en))
        cuerpo.append(f'<div class="documento" lang="en"><h2>{cab}</h2>' + "".join(bl) + "</div>")
    if d.get("excerpts_note"):
        cuerpo.append(f'<p class="nota-pie">{d["excerpts_note"]}</p>')
    ps = pasajes(src, slug_es)
    if ps:
        cuerpo.append('<h2 class="seccion">The exact words</h2>')
        if d.get("passages_intro"):
            cuerpo.append(f'<div class="bloque"><p>{d["passages_intro"]}</p></div>')
        cuerpo.append('<div class="bilingue">' + "".join(f'<div class="par"><div class="col en" lang="en"><span class="et">{a}</span>{b}</div></div>' for a, b in ps) + "</div>")
    for item in d.get("extra", []):
        if item[0] == "h2":
            cuerpo.append(f'<h2 class="seccion">{item[1]}</h2>')
        elif item[0] == "p":
            cuerpo.append(f'<div class="bloque"><p>{item[1]}</p></div>')
        elif item[0] == "table":
            cuerpo.append('<div class="bloque">' + tabla(*item[1:]) + "</div>")
        elif item[0] == "html":
            cuerpo.append(item[1])
        elif item[0] == "box":
            cuerpo.append(caja(item[1], item[2]))
    cuerpo.append('<h2 class="seccion">What this document supports, and what it does not</h2>')
    cuerpo.append('<div class="alcance"><div class="lado sostiene"><h3>It can support</h3><ul>' + "".join(f"<li>{x}</li>" for x in d["supports"]) +
                  '</ul></div><div class="lado nosostiene"><h3>It cannot support</h3><ul>' + "".join(f"<li>{x}</li>" for x in d["nots"]) + "</ul></div></div>")
    for t_, x in d.get("after", []):
        cuerpo.append(caja(t_, x))
    for url, tit, sub in d["links"]:
        cuerpo.append(enlace(url, tit, sub))
    lec = "".join(f'<li><a href="../lesson-{l}.html">Lesson {l.replace("-", ".")} · {TITULO_LECCION.get(l, "")}</a></li>' for l in d["lessons"])
    cuerpo.append(f'<div class="bloque"><h2>Lessons that use this document</h2><ul>{lec}</ul></div>')
    nav = (f'<nav class="navlecciones" aria-label="Course navigation"><a href="../index.html">Course plan</a><span class="nav-sep" aria-hidden="true">·</span>'
           f'<a href="index.html">Source archive</a><span class="nav-sep" aria-hidden="true">·</span><span class="nav-actual" aria-current="page">Document {n}</span>{nav_extra}</nav>')
    pie_nav = nav.replace('class="navlecciones"', 'class="navlecciones pie"').replace('aria-label="Course navigation"', 'aria-label="Course navigation (footer)"')
    extra_css = ".seccion-sub{margin:26px 0 6px;font-size:19px;color:var(--tema-d);} .documento p.encabezamiento{font-style:italic;} .bilingue .par{grid-template-columns:1fr !important;}"
    return f'''<!DOCTYPE html>
<!-- LearnGED · Social studies · Source archive · Document {n} — built by tools/build_soc_fuentes.py (texts in tools/fuentes_en_*.py)
     Record and notes © 2026 José M. Fernández, CC BY-NC-SA 4.0. The original documents are in the public domain. -->
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(d["short"])} · Source archive · LearnGED</title>
<meta name="license" content="CC BY-NC-SA 4.0"><link rel="license" href="https://creativecommons.org/licenses/by-nc-sa/4.0/">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="alternate" hreflang="es" href="/es/estudios-sociales/fuentes/{slug_es}.html">
<style>{raiz(src, slug_es)}{base_css}{lgcss}{extra_css}</style>
</head>
<body>
{barra("en")}
<div class="contenedor">
  <header class="principal">
    <div class="ruta">LearnGED · Social studies · Source archive · Document {n}</div>
    <h1>{d["title"]}</h1>
    <div class="meta">{d["meta"]}</div>
  </header>
  {nav}
  {"".join(cuerpo)}
  {pie_nav}
  <footer>
    <p>LearnGED · Social studies · Source archive · Document {n}</p>
    {C.PIE["en"]}
    <p>{d.get("pd", "The original document is in the public domain.")}</p>
  </footer>
</div>
</body>
</html>
'''


def indice(slugs, barra, lgcss, base_css, src):
    filas = []
    for i, (es, en) in enumerate(slugs, 1):
        d = DOCS[es]
        uso = ", ".join("Lesson " + l.replace("-", ".") for l in d["lessons"])
        filas.append(f'<div class="bloque"><h3><a href="{en}.html">{d["short"]}</a></h3><p class="meta-doc"><strong>Document {i}</strong> · {d["meta"]}</p><p>{d["blurb"]}</p><p class="uso">Used in {uso}.{" Paired with Document " + str(d["pair"]) + "." if d.get("pair") else ""}</p></div>')
    return f'''<!DOCTYPE html>
<!-- LearnGED · Social studies · Source archive (index) — built by tools/build_soc_fuentes.py -->
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Source archive · Social studies · LearnGED</title>
<meta name="license" content="CC BY-NC-SA 4.0"><link rel="license" href="https://creativecommons.org/licenses/by-nc-sa/4.0/">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="alternate" hreflang="es" href="/es/estudios-sociales/fuentes/index.html">
<style>{raiz(src, "index")}{base_css}{lgcss} .meta-doc{{font-size:14px;color:#444;margin:0 0 6px;}} .uso{{font-size:14px;color:#555;}} .bloque h3 a{{color:var(--tema-d);}}</style>
</head>
<body>
{barra("en")}
<div class="contenedor">
  <header class="principal">
    <div class="ruta">LearnGED · Social studies</div>
    <h1>Source archive</h1>
    <div class="meta">Real public-domain documents, each with its record, its limits, and a link to the original</div>
  </header>
  <nav class="navlecciones" aria-label="Course navigation"><a href="../index.html">Course plan</a><span class="nav-sep" aria-hidden="true">·</span><span class="nav-actual" aria-current="page">Source archive</span></nav>
  <div class="bloque">
    <h2>What this archive is</h2>
    <p>The documents in the lessons of this course were not written to teach. They are real sources: letters, reports, speeches, laws, court decisions, and newspaper pages, produced at the time by people who wanted something. That is the material the GED® Social Studies test works with, and so it is the material used here.</p>
    <p>Each document is kept here with its full record and a link to the original in the repository that holds it. In the lessons you see only the working excerpt; here you see where it comes from. The Spanish version of the archive adds the course’s own translation of each document.</p>
  </div>
  <div class="bloque">
    <h2>How a document gets into the archive</h2>
    <ul>
      <li><strong>Public domain, checked.</strong> The legal status of each document is verified, and the record says on what basis and on what date.</li>
      <li><strong>Not adapted.</strong> Irregular spelling and offensive language of the time are kept, because they are part of the evidence.</li>
      <li><strong>Checkable against the original.</strong> Every record says where the original is. When the document is rare, its text is reproduced here; when an official transcription exists online (as with the founding documents), the archive links to it instead of copying it, because the institution that keeps the document checks it better than a copy would.</li>
      <li><strong>With its limit stated.</strong> Each record says what can be supported with the document and what cannot. An archive that only says what a source proves teaches half the job.</li>
    </ul>
  </div>
  <div class="bloque">
    <h2>What cannot be here, and why</h2>
    <p>This archive publishes only documents whose public-domain status is confirmed, and some important sources of the course do not have it. The clearest case is Martin Luther King, Jr. The <em>Letter from Birmingham Jail</em> (April 16, 1963) and the speech of August 28, 1963, in Washington are still under copyright, managed by the King estate through a licensing company. Works published in the United States in 1963 with the required formalities are protected for ninety-five years from publication. The <a href="https://kinginstitute.stanford.edu/letter-birmingham-jail" rel="noopener">King Institute at Stanford University</a> itself states that it cannot grant permission to reproduce any of his writings.</p>
    <p>So Lesson 6.3 works with civil disobedience as a strategy through public-domain documents that record its effects (court decisions, federal laws, and executive orders), and points you to licensed editions to read King directly: the King Institute’s page on the letter, the digital archive of the King Center in Atlanta, and the book <em>Why We Can’t Wait</em> (1963), which any public library can lend you. Who owns the words of a public figure, and for how long, is a real question that this course leaves open.</p>
  </div>
  <h2 class="seccion">Published documents</h2>
  {"".join(filas)}
  <nav class="navlecciones pie" aria-label="Course navigation (footer)"><a href="../index.html">Course plan</a></nav>
  <footer>
    <p>LearnGED · Social studies · Source archive</p>
    {C.PIE["en"]}
    <p>The original documents are in the public domain; each record names its repository.</p>
  </footer>
</div>
</body>
</html>
'''


def construye(en_dir, src, slugs, barra, lgcss):
    os.makedirs(en_dir, exist_ok=True)
    base = estilo_base(src)
    for es, en in slugs:
        open(os.path.join(en_dir, en + ".html"), "w", encoding="utf-8").write(pagina(es, en, DOCS[es], src, slugs, barra, lgcss, base))
    open(os.path.join(en_dir, "index.html"), "w", encoding="utf-8").write(indice(slugs, barra, lgcss, base, src))
    print("ok social-studies/sources/ ·", len(slugs) + 1, "pages")
