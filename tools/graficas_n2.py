# -*- coding: utf-8 -*-
"""LearnGED · Artes del lenguaje N2 · Gráficas sencillas en SVG para leer (barras, líneas con rótulos, circular, tabla).
Todas llevan descripción completa para lectores de pantalla."""
import math, html as H
from ciencia import grafica, tabla

COL = ["#0b5d52", "#c2410c", "#1d4ed8", "#7c3aed", "#b45309", "#be185d"]
PAT = ["", "url(#rayas)", "url(#puntos)", "url(#cuadros)"]


def barras(titulo, ex, ey, etq, vals, py=None, ancho=520, alto=300):
    spec = {"tipo": "barras", "xEtq": ex, "yEtq": ey, "barras": [{"etq": e, "valor": v} for e, v in zip(etq, vals)]}
    if py: spec["py"] = py
    desc = f"Gráfica de barras: {titulo}. Eje horizontal: {ex}. Eje vertical: {ey}. " + "; ".join(f"{e}, {v}" for e, v in zip(etq, vals)) + "."
    return f'<figure class="figura grafica"><figcaption class="graf-tit">{titulo}</figcaption>{grafica(spec, desc, ancho=ancho, alto=alto)}</figure>'


def lineas(titulo, ey, etq, vals, ymax, paso, unidad="", ancho=560, alto=300):
    ml, mr, mt, mb = 62, 20, 22, 48
    W, Hh = ancho - ml - mr, alto - mt - mb
    n = len(etq)
    X = lambda i: ml + (i + .5) * W / n
    Y = lambda v: mt + Hh - v / ymax * Hh
    g = []
    v = 0
    while v <= ymax + 1e-9:
        t = f"{v:g}"
        g.append(f'<line x1="{ml}" y1="{Y(v):.1f}" x2="{ml + W}" y2="{Y(v):.1f}" stroke="#e1e6ea"/><text x="{ml - 8}" y="{Y(v) + 5:.1f}" text-anchor="end" font-size="13" fill="#3d4753">{t}</text>')
        v += paso
    g.append(f'<line x1="{ml}" y1="{mt}" x2="{ml}" y2="{mt + Hh}" stroke="#1a2330" stroke-width="1.5"/><line x1="{ml}" y1="{mt + Hh}" x2="{ml + W}" y2="{mt + Hh}" stroke="#1a2330" stroke-width="1.5"/>')
    pts = " ".join(f"{X(i):.1f},{Y(v):.1f}" for i, v in enumerate(vals))
    g.append(f'<polyline points="{pts}" fill="none" stroke="{COL[0]}" stroke-width="3"/>')
    for i, (e, v) in enumerate(zip(etq, vals)):
        g.append(f'<circle cx="{X(i):.1f}" cy="{Y(v):.1f}" r="4.5" fill="{COL[0]}" stroke="#fff" stroke-width="1.5"/>'
                 f'<text x="{X(i):.1f}" y="{Y(v) - 10:.1f}" text-anchor="middle" font-size="12" font-weight="700" fill="#1a2330">{v:g}</text>'
                 f'<text x="{X(i):.1f}" y="{mt + Hh + 18}" text-anchor="middle" font-size="12.5" fill="#3d4753">{e}</text>')
    g.append(f'<text x="16" y="{mt + Hh / 2:.1f}" text-anchor="middle" font-size="13" font-weight="700" fill="#1a2330" transform="rotate(-90 16 {mt + Hh / 2:.1f})">{ey}</text>')
    desc = f"Gráfica de líneas: {titulo}. Eje vertical: {ey}. " + "; ".join(f"{e}, {v:g}{unidad}" for e, v in zip(etq, vals)) + "."
    return (f'<figure class="figura grafica"><figcaption class="graf-tit">{titulo}</figcaption><svg viewBox="0 0 {ancho} {alto}" role="img" aria-label="{H.escape(desc)}" '
            f'style="width:100%;max-width:{ancho}px;height:auto;display:block;margin:6px auto">{"".join(g)}</svg></figure>')


def circular(titulo, etq, pcts):
    cx, cy, r = 135, 135, 115
    a = -math.pi / 2
    s = ['<defs><pattern id="rayas" width="8" height="8" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="8" height="8" fill="#c2410c"/><line x1="0" y1="0" x2="0" y2="8" stroke="#fff" stroke-width="2.5"/></pattern>'
         '<pattern id="puntos" width="9" height="9" patternUnits="userSpaceOnUse"><rect width="9" height="9" fill="#1d4ed8"/><circle cx="4.5" cy="4.5" r="1.8" fill="#fff"/></pattern>'
         '<pattern id="cuadros" width="10" height="10" patternUnits="userSpaceOnUse"><rect width="10" height="10" fill="#7c3aed"/><rect width="5" height="5" fill="#a78bfa"/><rect x="5" y="5" width="5" height="5" fill="#a78bfa"/></pattern></defs>']
    for i, (e, p) in enumerate(zip(etq, pcts)):
        b = a + 2 * math.pi * p / 100
        x1, y1, x2, y2 = cx + r * math.cos(a), cy + r * math.sin(a), cx + r * math.cos(b), cy + r * math.sin(b)
        fill = PAT[i] or COL[0]
        s.append(f'<path d="M{cx} {cy} L{x1:.1f} {y1:.1f} A{r} {r} 0 {1 if p > 50 else 0} 1 {x2:.1f} {y2:.1f} Z" fill="{fill}" stroke="#fff" stroke-width="2"/>')
        m = (a + b) / 2
        s.append(f'<text x="{cx + r * .62 * math.cos(m):.1f}" y="{cy + r * .62 * math.sin(m) + 5:.1f}" text-anchor="middle" font-size="15" font-weight="800" fill="#fff" '
                 f'stroke="#1a2330" stroke-width="3" paint-order="stroke">{p} %</text>')
        s.append(f'<rect x="285" y="{52 + i * 34}" width="20" height="20" fill="{fill}" stroke="#1a2330" stroke-width=".5"/><text x="313" y="{68 + i * 34}" font-size="15">{e} · {p} %</text>')
        a = b
    desc = f"Gráfica circular: {titulo}. " + "; ".join(f"{e}, {p} por ciento" for e, p in zip(etq, pcts)) + "."
    return (f'<figure class="figura grafica"><figcaption class="graf-tit">{titulo}</figcaption><svg viewBox="0 0 470 275" role="img" aria-label="{H.escape(desc)}" '
            f'style="width:100%;max-width:470px;display:block;margin:6px auto">{"".join(s)}</svg></figure>')


def tabla_datos(titulo, cols, filas):
    """filas: [(rótulo, [valores])]"""
    return f'<p class="graf-tit">{titulo}</p>' + tabla(titulo, [""] + cols, [[f] + [str(x) for x in v] for f, v in filas])
