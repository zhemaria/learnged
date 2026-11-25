"""Builds the Spanish LearnGED copy of the TI-30XS simulator (js/calculadora.js) from algebra/calculadora-gph.js.
Usage: python3 tools/build-calculadora-es.py <algebra/calculadora-gph.js> js/calculadora.js
Only the branding changes, so LearnGED does not depend on another site; the texts stay as in GEDparaHispanos."""
import sys
src = open(sys.argv[1], encoding="utf-8").read()
def rep(old, new, count=1):
    global src
    n = src.count(old)
    if n != count:
        sys.exit(f"Expected {count} match(es), found {n}: {old[:80]!r}")
    src = src.replace(old, new)
rep(" * Calculadora GPH v2.3 — simulador de la TI-30XS MultiView™ — GEDparaHispanos",
    " * Calculadora LearnGED v2.3 (español) — simulador de la TI-30XS MultiView™ — LearnGED\n * Copia de calculadora-gph.js (GEDparaHispanos) alojada en LearnGED.")
rep(" *   <script src=\"https://zhemaria.github.io/algebra/calculadora-gph.js\" defer></script>", " *   <script src=\"/js/calculadora.js\" defer></script>   (LearnGED, español)")
rep("'GEDparaHispanos · Zhema · recurso educativo'", "'LearnGED · Zhema · recurso educativo'")
rep("<span>Simulador GPH</span>", "<span>Simulador LearnGED</span>")
rep("'gti-pos-calc'", "'lg-pos-calc'", src.count("'gti-pos-calc'"))
rep("'gti-pos-hoja'", "'lg-pos-hoja'", src.count("'gti-pos-hoja'"))
open(sys.argv[2], "w", encoding="utf-8").write(src)
print("ok")
