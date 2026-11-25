"""Busca restos de inglés en el texto visible de páginas en español. Uso: python3 revisa.py archivo.html [...]"""
import re, sys
PAL = r"\b(the|and|you|your|is|are|of|to|with|what|how|this|that|Practice|Lesson|Question|Next|Open|Check|Type|Find)\b"
for f in sys.argv[1:]:
    s = open(f, encoding="utf-8").read()
    js = "\n".join(re.findall(r"<script>(.*?)</script>", s, flags=re.S))
    s2 = re.sub(r"<script.*?</script>|<style.*?</style>", "", s, flags=re.S)
    txt = re.sub(r"<[^>]+>", " ", s2)
    attrs = " ".join(re.findall(r'(?:aria-label|title|alt)="([^"]*)"', s2))
    strs = " ".join(re.findall(r'"([^"\n]{3,})"|\'([^\'\n]{3,})\'', js) and [a or b for a, b in re.findall(r'"([^"\n]{3,})"|\'([^\'\n]{3,})\'', js)])
    for nombre, t in (("texto", txt), ("atributos", attrs), ("script", strs)):
        for m in re.finditer(PAL, t):
            print(f"{f.split('/')[-1]} [{nombre}] …{t[max(0, m.start()-40):m.end()+40]!r}")
