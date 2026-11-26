"""Static SVG figures for the Topic 7 lessons (same drawing rules as math/geometry.js → figuraSVG)."""
import math
from bilingue import svg

def _t(p, txt, tam=16, color="#222", peso=700, anc="middle"):
    return f'<text x="{p[0]:.1f}" y="{p[1]:.1f}" text-anchor="{anc}" dominant-baseline="middle" font-size="{tam}" font-weight="{peso}" fill="{color}">{txt}</text>'

def figura(polis, cotas, voz, extras=(), alto=300, ancho=640):
    """polis: [dict(pts, fill, stroke, dash, txt, c)] in units, y up.
    cotas: [(p, q, label)] label outside, to the right of p→q.
    extras: dict(linea=(p, q)) · dict(arco=(c, r, abajo)) · dict(txt, p, col)."""
    xs, ys = [], []
    for P in polis:
        for p in P["pts"]:
            xs.append(p[0]); ys.append(p[1])
    for E in extras:
        for p in E.get("pts", ()):
            xs.append(p[0]); ys.append(p[1])
    mnx, mxx, mny, mxy = min(xs), max(xs), min(ys), max(ys)
    esc = min((ancho - 160) / ((mxx - mnx) or 1), (alto - 90) / ((mxy - mny) or 1))
    ox, oy = ancho / 2 - (mnx + mxx) / 2 * esc, alto / 2 + (mny + mxy) / 2 * esc
    T = lambda p: (ox + p[0] * esc, oy - p[1] * esc)
    s = ""
    for P in polis:
        pts = " ".join(f"{T(p)[0]:.1f},{T(p)[1]:.1f}" for p in P["pts"])
        dash = ' stroke-dasharray="7 5"' if P.get("dash") else ""
        s += f'<polygon points="{pts}" fill="{P.get("fill", "#eceff1")}" stroke="{P.get("stroke", "#37474f")}" stroke-width="{P.get("sw", 3)}"{dash}/>'
        if P.get("txt"):
            s += _t(T(P["c"]), P["txt"], 16, P.get("col", "#1c2a30"))
    for E in extras:
        if "arco" in E:
            c, r, abajo = E["arco"]; c0 = T(c); R = r * esc
            s += f'<path d="M{c0[0] - R:.1f} {c0[1]:.1f} A{R:.1f} {R:.1f} 0 0 {0 if abajo else 1} {c0[0] + R:.1f} {c0[1]:.1f} Z" fill="{E.get("fill", "#cfd8dc")}" stroke="#37474f" stroke-width="3"/>'
    for E in extras:
        if "linea" in E:
            a, b = T(E["linea"][0]), T(E["linea"][1])
            s += f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" stroke="{E.get("color", "#b71c1c")}" stroke-width="2" stroke-dasharray="6 4"/>'
        if "txt" in E:
            s += _t(T(E["p"]), E["txt"], 16, E.get("col", "#1c2a30"))
    for k in cotas:
        a, b = T(k[0]), T(k[1])
        mx, my, dx, dy = (a[0] + b[0]) / 2, (a[1] + b[1]) / 2, b[0] - a[0], b[1] - a[1]
        L = math.hypot(dx, dy) or 1
        ux, uy = -dy / L, dx / L
        anc = "start" if ux > 0.5 else ("end" if ux < -0.5 else "middle")
        d = 16 if anc == "middle" else 9
        s += _t((mx + ux * d, my + uy * d), k[2], 18, "#222", 700, anc)
    return svg(f"0 0 {ancho} {alto}", voz, s, ancho)
