"""Piezas comunes de las lecciones del Nivel 4: el plano cartesiano dibujado en Python (para las figuras fijas
de las lecciones), la práctica con respuesta de par ordenado y los estilos. Las usan tools/build_n4_lesson_*.py.
El motor del plano en el navegador es math/coord4.js."""
import bilingue as B
from n3 import formula, salida, atencion, panel, numero, lista, aviso  # noqa: F401 (se reexportan)

t = B.t
SCRIPTS = ("/math/radicals.js", "/math/linear.js", "/math/coord4.js")

AZUL, ROJO, VERDE, TINTA, CATETO, MORADO = "#0d47a1", "#b71c1c", "#1b5e20", "#10174f", "#00695c", "#6a1b9a"

ESTILO = """
  [hidden]{display:none !important;}
  .geo-svg{display:block;width:100%;height:auto;margin:12px auto;background:#fff;border:1px solid #cfd8dc;border-radius:10px;}
  .plano-svg:focus{outline:3px solid #6a1b9a;outline-offset:3px;}
  .par-campos{display:flex;align-items:flex-end;gap:6px;flex-wrap:wrap;font-size:22px;font-weight:700;color:var(--tema-d);}
  .par-campos .campo{margin:0;}
  .par-campos input{width:88px;font-size:18px;text-align:center;}
  .par-campos .pa{padding-bottom:6px;}
  .modos{display:flex;flex-wrap:wrap;gap:8px;margin:10px 0;}
  .modos button[aria-pressed="true"]{background:var(--tema);color:#fff;border-color:var(--tema);}
  .leyenda-geo{display:flex;flex-wrap:wrap;gap:14px;font-size:14px;color:var(--gris);margin:4px 0 10px;}
  .leyenda-geo span{display:inline-flex;align-items:center;gap:6px;}
  .lectura-plano{min-height:1.4em;}
  .tabla-lados{border-collapse:collapse;margin:10px 0;font-size:16px;}
  .tabla-lados th,.tabla-lados td{border:1px solid #c8c8c8;padding:6px 12px;text-align:left;}
  .tabla-lados th{background:var(--tema-bg);color:var(--tema-d);}
  .tabla-lados tr.incl td{background:#fff8e1;}
  .salida:empty{display:none;}"""

def par_libre(pid, titulo, nombre="", nota=None):
    """Práctica con respuesta de par ordenado (creaPracticaPar de coord4.js)."""
    nt = f'\n        <p class="nota">{nota}</p>' if nota else ""
    return f'''      <h3>{titulo}</h3>
      <div class="practica" id="{pid}">
        <div class="enun" id="{pid}-enun"></div>
        <div class="par-campos" role="group" aria-label="{t("Your answer as an ordered pair", "Su respuesta como par ordenado")}"><span class="pa" aria-hidden="true">{nombre}(</span>
          <div class="campo"><label for="{pid}-x">x</label><input type="text" inputmode="decimal" autocomplete="off" id="{pid}-x"></div><span class="pa" aria-hidden="true">,</span>
          <div class="campo"><label for="{pid}-y">y</label><input type="text" inputmode="decimal" autocomplete="off" id="{pid}-y"></div><span class="pa" aria-hidden="true">)</span></div>{nt}
        <div class="fila-btn">
          <button type="button" class="btn" id="{pid}-comprobar">Check</button>
          <button type="button" class="btn-sec" id="{pid}-nuevo">New exercise</button>
        </div>
        <div class="fb" id="{pid}-fb" role="status"></div>
        <p class="marcador" id="{pid}-marcador"></p>
      </div>'''

def sg(n):
    n = round(n, 3)
    if n == int(n):
        n = int(n)
    return str(n).replace("-", "−")

def par(x, y):
    return f"({sg(x)}, {sg(y)})"

class Plano:
    """El mismo plano de coord4.js, para dibujar figuras fijas en las lecciones."""
    def __init__(self, xmin=-6, xmax=6, ymin=-6, ymax=6, u=34, cuadrantes=False, paso=1):
        self.xmin, self.xmax, self.ymin, self.ymax, self.u, self.m = xmin, xmax, ymin, ymax, u, 30
        self.W, self.H = (xmax - xmin) * u + 60, (ymax - ymin) * u + 60
        self.cuadrantes, self.paso, self.c = cuadrantes, paso, []
    def X(self, x): return self.m + (x - self.xmin) * self.u
    def Y(self, y): return self.m + (self.ymax - y) * self.u
    def rejilla(self):
        s, X, Y = [], self.X, self.Y
        for x in range(self.xmin, self.xmax + 1):
            s.append(f'<line x1="{X(x)}" y1="{Y(self.ymax)}" x2="{X(x)}" y2="{Y(self.ymin)}" stroke="#cfd8dc" stroke-width="1"/>')
        for y in range(self.ymin, self.ymax + 1):
            s.append(f'<line x1="{X(self.xmin)}" y1="{Y(y)}" x2="{X(self.xmax)}" y2="{Y(y)}" stroke="#cfd8dc" stroke-width="1"/>')
        if self.cuadrantes:
            for r, qx, qy in (("I", .6, .8), ("II", -.6, .8), ("III", -.6, -.8), ("IV", .6, -.8)):
                x = qx * (self.xmax if qx > 0 else -self.xmin); y = qy * (self.ymax if qy > 0 else -self.ymin)
                s.append(f'<text x="{X(x):.1f}" y="{Y(y):.1f}" text-anchor="middle" dominant-baseline="middle" font-size="30" font-weight="700" fill="#b0bec5" font-family="Georgia, serif">{r}</text>')
        y0 = 0 if self.ymin <= 0 <= self.ymax else self.ymin
        x0 = 0 if self.xmin <= 0 <= self.xmax else self.xmin
        s.append(f'<line x1="{X(self.xmin) - 8}" y1="{Y(y0)}" x2="{X(self.xmax) + 10}" y2="{Y(y0)}" stroke="{TINTA}" stroke-width="2"/>')
        s.append(f'<line x1="{X(x0)}" y1="{Y(self.ymin) + 8}" x2="{X(x0)}" y2="{Y(self.ymax) - 10}" stroke="{TINTA}" stroke-width="2"/>')
        s.append(f'<polygon points="{X(self.xmax) + 14},{Y(y0)} {X(self.xmax) + 4},{Y(y0) - 5} {X(self.xmax) + 4},{Y(y0) + 5}" fill="{TINTA}"/>')
        s.append(f'<polygon points="{X(x0)},{Y(self.ymax) - 14} {X(x0) - 5},{Y(self.ymax) - 4} {X(x0) + 5},{Y(self.ymax) - 4}" fill="{TINTA}"/>')
        s.append(f'<text x="{X(self.xmax) + 14}" y="{Y(y0) - 12}" font-size="16" font-style="italic" font-weight="700" fill="{TINTA}" text-anchor="middle">x</text>')
        s.append(f'<text x="{X(x0) + 14}" y="{Y(self.ymax) - 10}" font-size="16" font-style="italic" font-weight="700" fill="{TINTA}">y</text>')
        return "".join(s)
    def numeros(self):
        s, X, Y = [], self.X, self.Y
        y0 = 0 if self.ymin <= 0 <= self.ymax else self.ymin
        x0 = 0 if self.xmin <= 0 <= self.xmax else self.xmin
        h = ' paint-order="stroke" stroke="#fff" stroke-width="3"'
        for x in range(self.xmin, self.xmax):
            if x and x % self.paso == 0:
                s.append(f'<text x="{X(x)}" y="{Y(y0) + 18}" font-size="13" fill="#455a64" text-anchor="middle"{h}>{sg(x)}</text>')
        for y in range(self.ymin, self.ymax):
            if y and y % self.paso == 0:
                s.append(f'<text x="{X(x0) - 6}" y="{Y(y) + 4}" font-size="13" fill="#455a64" text-anchor="end"{h}>{sg(y)}</text>')
        return "".join(s)
    def seg(self, a, b, color=TINTA, ancho=3, raya=None):
        r = f' stroke-dasharray="{raya}"' if raya else ""
        self.c.append(f'<line x1="{self.X(a[0]):.1f}" y1="{self.Y(a[1]):.1f}" x2="{self.X(b[0]):.1f}" y2="{self.Y(b[1]):.1f}" stroke="{color}" stroke-width="{ancho}"{r} stroke-linecap="round"/>')
        return self
    def poli(self, pts, relleno="none", color=TINTA, ancho=3):
        p = " ".join(f"{self.X(x):.1f},{self.Y(y):.1f}" for x, y in pts)
        self.c.append(f'<polygon points="{p}" fill="{relleno}" stroke="{color}" stroke-width="{ancho}" stroke-linejoin="round"/>')
        return self
    def punto(self, p, color=AZUL, etiqueta=None, lado="ne"):
        cx, cy = self.X(p[0]), self.Y(p[1])
        self.c.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="6" fill="{color}" stroke="#fff" stroke-width="2"/>')
        if etiqueta:
            if p[0] == 0 and p[1] != 0:
                lado = ("n" if p[1] > 0 else "s") + "e"
            elif p[1] == 0 and p[0] != 0:
                lado = "n" + ("e" if p[0] > 0 else "w")
            dx = 10 if "e" in lado else -10
            dy = -10 if "n" in lado else 20
            an = "start" if dx > 0 else "end"
            self.c.append(f'<text x="{cx + dx:.1f}" y="{cy + dy:.1f}" font-size="15" font-weight="700" fill="{color}" text-anchor="{an}" paint-order="stroke" stroke="#fff" stroke-width="4">{etiqueta}</text>')
        return self
    def texto(self, p, txt, color=TINTA, tam=14, ancla="middle", dx=0, dy=0):
        self.c.append(f'<text x="{self.X(p[0]) + dx:.1f}" y="{self.Y(p[1]) + dy:.1f}" font-size="{tam}" font-weight="700" fill="{color}" text-anchor="{ancla}" dominant-baseline="middle" paint-order="stroke" stroke="#fff" stroke-width="4">{txt}</text>')
        return self
    def svg(self, voz, ancho=440):
        return B.svg(f"0 0 {self.W} {self.H}", voz, self.rejilla() + "".join(self.c) + self.numeros(), ancho)
