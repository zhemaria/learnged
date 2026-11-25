"""En las páginas en español, une los grupos de miles con un espacio que no se parte (U+00A0):
«3 482 651» nunca queda cortado al final de una línea.
No toca el código (<script>) ni los atributos de dibujo (viewBox, points, d, transform).
Uso: python3 tools/espacios_es.py [--con-script] archivo.html [...]
   --con-script: también dentro de <script> (para las lecciones, cuyo script solo tiene textos)."""
import re, sys
PAT = re.compile(r"(?<=\d) (?=\d{3}(?!\d))")
PROTEGE = re.compile(r'<script\b.*?</script>|\b(?:viewBox|points|d|transform)="[^"]*"', re.S)
args = sys.argv[1:]
if args and args[0] == "--con-script":
    args = args[1:]; PROTEGE = re.compile(r'\b(?:viewBox|points|d|transform)="[^"]*"')
for f in args:
    s = open(f, encoding="utf-8").read()
    # deshace cambios anteriores dentro de las zonas protegidas
    s = PROTEGE.sub(lambda m: m.group().replace(" ", " ") if not m.group().startswith("<script") else m.group(), s)
    out, last, n = [], 0, 0
    for m in PROTEGE.finditer(s):
        seg = s[last:m.start()]; n += len(PAT.findall(seg)); out.append(PAT.sub(" ", seg)); out.append(m.group()); last = m.end()
    seg = s[last:]; n += len(PAT.findall(seg)); out.append(PAT.sub(" ", seg))
    open(f, "w", encoding="utf-8").write("".join(out))
    print(f, n)
