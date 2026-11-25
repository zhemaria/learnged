"""Links each Level 1 lesson in math/level-1/index.html as soon as its page exists.
Usage: python3 tools/indice_en.py   (run it each time you add a lesson)"""
import os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
p = os.path.join(ROOT, "math", "level-1", "index.html")
s = open(p, encoding="utf-8").read()
def enlaza(m):
    n, titulo = m.group(1).replace(".", "-"), m.group(2)
    if not os.path.exists(os.path.join(ROOT, "math", "level-1", f"lesson-{n}.html")):
        return m.group(0)
    return f'<li><a href="lesson-{n}.html">Lesson {m.group(1)} · {titulo}</a> · <a href="practice-{n}.html">practice</a></li>'
s2 = re.sub(r'<li class="soon">Lesson (\d\.\d) · (.*?) — coming soon</li>', enlaza, s)
open(p, "w", encoding="utf-8").write(s2)
print("ok:", s2.count("lesson-"), "links to lessons")
