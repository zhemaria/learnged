"""LearnGED · Estudios sociales · Archivo de fuentes (EN/ES).
  es/estudios-sociales/fuentes/  · las 18 fichas del curso en español y su índice, tomadas tal cual del repositorio `sociales`
                                   (copiadas en tools/fuentes_src/) y puestas en el marco de LearnGED: barra superior, enlaces
                                   a las lecciones de LearnGED, números al estilo de EE. UU. y nombre del sitio.
  social-studies/sources/        · las mismas fichas en inglés (tools/fuentes_en.py): ficha, de qué trata, el texto original
                                   cuando el Archivo lo reproduce (o los pasajes exactos que usan las lecciones), qué sostiene
                                   y qué no, y el enlace al original en el repositorio que lo custodia. La traducción al español
                                   no aparece en inglés: el original ocupa su lugar.
Uso: python3 tools/build_soc_fuentes.py  (después, tools/build_planes.py)
"""
import os, re, sys, html as H
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sociales import C

AQUI = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(AQUI, "fuentes_src")
ES_DIR = os.path.join(C.ROOT, "es", "estudios-sociales", "fuentes")
EN_DIR = os.path.join(C.ROOT, "social-studies", "sources")

# slug español -> slug inglés (el orden es el del Archivo: Documentos 1 a 18)
SLUGS = [("cartas-migrantes-1917", "migrant-letters-1917"), ("addams-primeros-dias-1889", "addams-first-days-1889"), ("holbrook-mapas-1895", "holbrook-maps-1895"),
         ("the-public-traccion-1905", "the-public-traction-1905"), ("street-railway-traccion-1905", "street-railway-traction-1905"),
         ("declaracion-independencia-1776", "declaration-of-independence-1776"), ("federalista-10-51-1788", "federalist-10-51-1788"), ("brutus-ensayo-1-1787", "brutus-essay-1-1787"),
         ("derechos-agravios-1765", "rights-and-grievances-1765"), ("ley-declaratoria-1766", "declaratory-act-1766"), ("washington-knox-1786", "washington-to-knox-1786"),
         ("enmiendas-13-14-15", "amendments-13-14-15"), ("testimonio-colby-1871", "colby-testimony-1871"), ("jacobs-anuncio-1835", "jacobs-notice-1835"),
         ("brown-v-board-1954", "brown-v-board-1954"), ("leyes-1964-1965", "acts-of-1964-and-1965"), ("orden-8802-1941", "executive-order-8802-1941"), ("massachusetts-epa-2007", "massachusetts-v-epa-2007")]
ES2EN = dict(SLUGS)
ES2EN["index"] = "index"
TEMA_ANCLA = {"1": "tools", "2": "tools", "3": "civics", "4": "civics", "5": "civics", "6": "history", "7": "economics", "8": "ged"}

LGBAR_CSS = ".lg-bar{display:flex;align-items:center;justify-content:space-between;gap:12px;flex-wrap:wrap;background:#fff;border-bottom:1px solid #e3e7ec;padding:8px 18px;font-family:'Segoe UI',system-ui,sans-serif;position:sticky;top:0;z-index:60}.lg-bar img{display:block;height:34px;width:auto}.lg-link{color:#1E3A5F;font-weight:700;text-decoration:none;font-size:15px}.lg-link:hover,.lg-link:focus{text-decoration:underline}@media print{.lg-bar{display:none}}"


def barra(lang):
    if lang == "es":
        return ('<nav class="lg-bar" aria-label="LearnGED"><a class="lg-logo" href="/es/"><img src="/img/learnged-logo-horizontal.svg" alt="Inicio de LearnGED" height="34"></a>'
                '<a class="lg-link" href="../">Estudios sociales · todas las lecciones</a></nav>')
    return ('<nav class="lg-bar" aria-label="LearnGED"><a class="lg-logo" href="/"><img src="/img/learnged-logo-horizontal.svg" alt="LearnGED home" height="34"></a>'
            '<a class="lg-link" href="../">Social studies · all lessons</a></nav>')


# ---------------------------------------------------------------- español: las páginas del repositorio sociales en el marco de LearnGED
def a_learnged_es(s, slug):
    s = s.replace('lang="es">', 'lang="es">', 1)
    # cabecera: icono, versión inglesa y barra
    s = s.replace("</head>", f'<link rel="icon" href="/favicon.svg" type="image/svg+xml">\n<link rel="alternate" hreflang="en" href="/social-studies/sources/{ES2EN[slug]}.html">\n<style>{LGBAR_CSS}</style>\n</head>', 1)
    s = re.sub(r"(<body[^>]*>)", lambda m: m.group(1) + "\n" + barra("es"), s, count=1)
    # enlaces a las lecciones y al plan del curso de LearnGED
    s = re.sub(r'href="\.\./soc-(\d)-(\d)\.html"', r'href="../leccion-\1-\2.html"', s)
    s = re.sub(r'href="\.\./index\.html#tema-(\d)"', lambda m: f'href="../index.html#{TEMA_ANCLA[m.group(1)]}"', s)
    # las etiquetas de prácticas del repositorio original seguían otra numeración: en LearnGED se omiten
    s = re.sub(r'\s*<div class="practicas-sp">.*?</div>', "", s, flags=re.S)
    # el nombre del sitio
    s = s.replace("Spanish ASE Social Studies · ", "").replace("Spanish ASE Social Studies", "LearnGED · Estudios sociales")
    s = s.replace("GEDparaHispanos · Archivo de fuentes", "LearnGED · Estudios sociales · Archivo de fuentes").replace("· GEDparaHispanos", "· LearnGED").replace("GEDparaHispanos", "LearnGED")
    # números al estilo de EE. UU. fuera de los originales en inglés (en el Archivo solo aparecen en Holbrook: 1,25 dólares)
    partes = re.split(r"(<details.*?</details>|<style.*?</style>|<script.*?</script>)", s, flags=re.S)
    for i in range(0, len(partes), 2):
        partes[i] = re.sub(r"(?<=[\s>])(\d{1,2}),(\d{2})(?=[\s<.;)])", r"\1.\2", partes[i])
        partes[i] = re.sub(r"(\d{1,3})[   ](\d{3})(?!\d)", r"\1,\2", partes[i])
    s = "".join(partes)
    # aviso de marca del GED al pie
    s = s.replace("</footer>", '  <p style="font-size:12px;color:#555">GED® es una marca registrada del American Council on Education (ACE), administrada exclusivamente por GED Testing Service LLC bajo licencia. LearnGED no está afiliado a ACE ni a GED Testing Service, ni cuenta con su respaldo o aprobación.</p>\n  </footer>', 1)
    return s


def construye_es():
    os.makedirs(ES_DIR, exist_ok=True)
    for f in sorted(os.listdir(SRC)):
        if not f.endswith(".html"):
            continue
        slug = f[:-5]
        s = open(os.path.join(SRC, f), encoding="utf-8").read()
        open(os.path.join(ES_DIR, f), "w", encoding="utf-8").write(a_learnged_es(s, slug))
    print("ok es/estudios-sociales/fuentes/ ·", len([f for f in os.listdir(ES_DIR) if f.endswith(".html")]), "páginas")


if __name__ == "__main__":
    construye_es()
    import fuentes_en
    fuentes_en.construye(EN_DIR, SRC, SLUGS, barra, LGBAR_CSS)
