"""Piezas comunes de las lecciones del Nivel 2 (números con signo): rectas numéricas y fichas en SVG.
Las usan los constructores tools/build_n2_lesson_*.py."""
import bilingue as B

ROJO, VERDE, AZUL, GRIS = "#b71c1c", "#1b5e20", "#0d47a1", "#424242"

def m(n):
    """Entero con el signo menos tipográfico (−) y coma de miles."""
    return ("−" if n < 0 else "") + f"{abs(n):,}"

def p(n):
    """Entero entre paréntesis si es negativo: (−7)."""
    return f"({m(n)})" if n < 0 else m(n)

def recta(lo, hi, label, marcas=(), saltos=(), tramo=None, ancho=620, paso=None):
    """Recta numérica de lo a hi.
    marcas: [(valor, texto, color, abajo)]; saltos: [(de, a, texto, color)]; tramo: (de, a, color)."""
    W, H, x0, x1, y = 660, 170, 26, 634, 112
    X = lambda v: x0 + (v - lo) * (x1 - x0) / (hi - lo)
    s = [f'<line x1="{x0-12}" y1="{y}" x2="{x1+12}" y2="{y}" stroke="{GRIS}" stroke-width="2"/>',
         f'<path d="M{x0-18} {y} l10 -6 v12 z" fill="{GRIS}"/><path d="M{x1+18} {y} l-10 -6 v12 z" fill="{GRIS}"/>']
    if tramo:
        s.append(f'<line x1="{X(tramo[0]):.1f}" y1="{y}" x2="{X(tramo[1]):.1f}" y2="{y}" stroke="{tramo[2]}" stroke-width="7"/>')
    paso = paso or (5 if hi - lo > 24 else (2 if hi - lo > 14 else 1))
    for v in range(lo, hi + 1):
        c = v == 0
        s.append(f'<line x1="{X(v):.1f}" y1="{y-(11 if c else 7)}" x2="{X(v):.1f}" y2="{y+(11 if c else 7)}" stroke="{GRIS}" stroke-width="{3 if c else 1.5}"/>')
        if v % paso == 0 or c:
            s.append(f'<text x="{X(v):.1f}" y="{y+28}" text-anchor="middle" font-size="{17 if c else 15}" font-weight="{700 if c else 400}" fill="#222">{m(v)}</text>')
    for i, (de, a, txt, col) in enumerate(saltos):
        xa, xb, alto = X(de), X(a), 34 + 10 * (i % 2)
        mx, d = (xa + xb) / 2, (-1 if xb > xa else 1)
        s.append(f'<path d="M{xa:.1f} {y-6} Q{mx:.1f} {y-6-2*alto} {xb:.1f} {y-6}" fill="none" stroke="{col}" stroke-width="3"/>')
        s.append(f'<path d="M{xb:.1f} {y-6} l{d*9} -12 l{-d*3} 0 z" fill="{col}" stroke="{col}" stroke-width="2"/>')
        if txt:
            s.append(f'<text x="{mx:.1f}" y="{y-10-alto}" text-anchor="middle" font-size="17" font-weight="700" fill="{col}">{txt}</text>')
    for v, txt, col, abajo in marcas:
        s.append(f'<circle cx="{X(v):.1f}" cy="{y}" r="8" fill="{col}"/>')
        if txt:
            s.append(f'<text x="{X(v):.1f}" y="{y+50 if abajo else y-22}" text-anchor="middle" font-size="16" font-weight="700" fill="{col}">{txt}</text>')
    return B.svg(f"0 0 {W} {H}", label, "".join(s), ancho)

def fichas(a, b, label, pares=False):
    """Fichas de dos colores: una fila para a y otra para b; amarilla (+) = +1, roja (−) = −1.
    pares=True tacha los pares cero."""
    H, r, dx = 150, 15, 36
    W = 100 + max(abs(a), abs(b), 1) * dx
    pos = max(a, 0) + max(b, 0); neg = max(-a, 0) + max(-b, 0); k = min(pos, neg)
    usP = usN = 0; s = []
    for fi, v in enumerate((a, b)):
        y = 40 + fi * 64
        s.append(f'<text x="30" y="{y}" text-anchor="middle" dominant-baseline="middle" font-size="18" font-weight="700" fill="#222">{m(v)}</text>')
        for i in range(abs(v)):
            x = 80 + i * dx; posit = v > 0; cero = False
            if pares:
                if posit and usP < k: cero = True; usP += 1
                elif not posit and usN < k: cero = True; usN += 1
            fill = "#eeeeee" if cero else ("#fbc02d" if posit else "#c62828")
            col = "#9e9e9e" if cero else ("#3e2723" if posit else "#fff")
            s.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="{"#9e9e9e" if cero else GRIS}" stroke-width="2"/>')
            s.append(f'<text x="{x}" y="{y+1}" text-anchor="middle" dominant-baseline="middle" font-size="20" font-weight="700" fill="{col}">{"+" if posit else "−"}</text>')
            if cero:
                s.append(f'<line x1="{x-12}" y1="{y+12}" x2="{x+12}" y2="{y-12}" stroke="#757575" stroke-width="2"/>')
    return B.svg(f"0 0 {W} {H}", label, "".join(s), min(560, int(W * 1.5)))

# ---------- fracciones con signo ----------
def fr(a, b):
    """Fracción apilada tal como se escribe: fr(-3, 4) pone el signo en el numerador; fr(3, -4), en el denominador."""
    return (f'<span class="fracc" aria-hidden="true"><span class="fa">{m(a) if isinstance(a, int) else a}</span><span class="fb2">{m(b) if isinstance(b, int) else b}</span></span>'
            f'<span class="cap-oculto">{m(a) if isinstance(a, int) else a}/{m(b) if isinstance(b, int) else b}</span>')

def frn(a, b):
    """Fracción con el signo menos delante: −a/b."""
    return f'<span aria-hidden="true">−<span class="fracc"><span class="fa">{a}</span><span class="fb2">{b}</span></span></span><span class="cap-oculto">−{a}/{b}</span>'

def frp(a, b):
    """Fracción negativa entre paréntesis si a < 0: (−3/4); positiva sin paréntesis."""
    return f'({frn(-a, b)})' if a < 0 else fr(a, b)

def mixto(e, a, b, neg=False):
    """Número mixto: −2 3/4."""
    s = "−" if neg else ""
    return f'<span aria-hidden="true">{s}{e}&nbsp;<span class="fracc"><span class="fa">{a}</span><span class="fb2">{b}</span></span></span><span class="cap-oculto">{s}{e} {a}/{b}</span>'

def pot(b, e):
    """Potencia: b<sup>e</sup>."""
    return f"{b}<sup>{e}</sup>"

def pasos_panel(pre, otro=None):
    """Panel «paso a paso» (pasoAPaso de integers.js): expresión, botones y pasos."""
    t = B.t
    return f'''      <div class="panel">
        <div class="estado"><span class="grande" id="{pre}-expr"></span></div>
        <div class="fila-btn"><button type="button" class="btn" id="{pre}-sig"></button><button type="button" class="btn-sec" id="{pre}-todo">{t("Show all", "Mostrar todo")}</button><button type="button" class="btn-sec" id="{pre}-nuevo">{otro or t("Another example", "Otro ejemplo")}</button></div>
        <div class="pasos" id="{pre}-pasos" aria-live="polite"></div>
      </div>'''
