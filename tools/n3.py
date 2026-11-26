"""Piezas comunes de las lecciones del Nivel 3: estilos y controles de las páginas de práctica.
Las usan los constructores tools/build_n3_lesson_*.py."""
import bilingue as B

t = B.t

# Estilos de las páginas de práctica del Tema 1 (exponentes): fichas, tablas de patrón y marcador por regla.
ESTILO_EXP = """  .fichas{display:flex;flex-wrap:wrap;align-items:center;gap:6px;justify-content:center;margin:14px 0;font-size:18px;}
  .fichas .grupo{display:inline-flex;flex-wrap:nowrap;max-width:none;gap:4px;padding:4px;border:1px dashed #90a4ae;border-radius:10px;}
  .ficha{display:inline-flex;align-items:center;justify-content:center;min-width:38px;height:38px;padding:0 6px;border-radius:8px;font-weight:700;border:2px solid var(--tema);background:var(--tema-bg);color:var(--tema-d);}
  .ficha.b{border-color:#00695c;background:#e0f2f1;color:#004d40;}
  .ficha.tachada{border-color:#b71c1c;background:#ffebee;color:#b71c1c;text-decoration:line-through;text-decoration-thickness:3px;}
  .signo{font-weight:700;font-size:20px;color:var(--tema-d);padding:0 2px;}
  .linea-frac{display:flex;flex-direction:column;align-items:center;gap:8px;margin:14px 0;}
  .linea-frac .barra{width:100%;max-width:520px;border-top:3px solid var(--tema-d);}
  .tabla-patron{border-collapse:collapse;margin:12px auto;font-size:17px;}
  .tabla-patron caption{font-size:14px;color:var(--gris);padding-bottom:6px;}
  .tabla-patron th,.tabla-patron td{border:1px solid #c8c8c8;padding:8px 14px;text-align:center;min-width:64px;}
  .tabla-patron th{background:var(--tema-bg);color:var(--tema-d);}
  .tabla-patron td.cero{background:#e8f5e9;font-weight:700;}
  .tabla-patron td.neg{background:#fff8e1;}
  .dividir{font-size:13px;color:var(--gris);}
  .marcador-regla{margin-top:12px;}
  .marcador-regla table{border-collapse:collapse;font-size:14px;}
  .marcador-regla caption{text-align:left;font-size:14px;color:var(--gris);padding-bottom:4px;}
  .marcador-regla th,.marcador-regla td{border:1px solid #c8c8c8;padding:5px 10px;text-align:left;}
  .marcador-regla th{background:var(--tema-bg);color:var(--tema-d);}
  .paso .regla{display:inline-block;font-size:13px;font-weight:700;color:var(--tema-d);background:var(--tema-bg);border-radius:6px;padding:1px 8px;margin-left:6px;}
  .fila-resp{display:flex;gap:10px;flex-wrap:wrap;margin-top:10px;}
  .salida .ex,.enun .ex,.opcion .ex{font-size:18px;}
  .campo input.bien,.campo select.bien{border-color:var(--ok);background:var(--ok-bg);}
  .salida:empty{display:none;}
  .campo select.error{border-color:#b71c1c;background:#ffebee;}"""

def numero(i, etiqueta, valor, vmin, vmax):
    """Casilla numérica de un explorador."""
    return f'<div class="campo"><label for="{i}">{etiqueta}</label><input type="number" id="{i}" value="{valor}" min="{vmin}" max="{vmax}" step="1"></div>'

def lista(i, etiqueta, opciones, sel=None):
    """Lista desplegable: opciones = [(valor, texto)]."""
    ops = "".join(f'<option value="{v}"{" selected" if str(v) == str(sel) else ""}>{x}</option>' for v, x in opciones)
    return f'<div class="campo"><label for="{i}">{etiqueta}</label><select id="{i}">{ops}</select></div>'

def panel(*campos):
    return '      <div class="panel"><div class="campos">\n        ' + "\n        ".join(campos) + '\n      </div></div>'

def aviso(i):
    return f'      <div class="caja-aviso" id="{i}" role="alert"></div>'

def salida(i):
    return f'      <div class="salida" aria-live="polite" id="{i}"></div>'

def atencion(titulo, texto):
    return f'      <div class="caja-atencion"><strong>{titulo}</strong> {texto}</div>'

def formula(x):
    return f'      <div class="formula">{x}</div>'

def escrita(pid, titulo, etiqueta):
    """Práctica con respuesta escrita de un entero con signo (ESCRITA de exponents.js)."""
    return f'''      <h3>{titulo}</h3>
      <div class="practica" id="{pid}">
        <div class="enun" id="{pid}-enun"></div>
        <div class="campos"><div class="campo"><label for="{pid}-r">{etiqueta}</label><input type="text" autocomplete="off" class="corto" id="{pid}-r"></div></div>
        <p class="nota">{t("Type a whole number. If it is negative, start with the minus sign: −2 or -2.", "Escriba un número entero. Si es negativo, empiece con el signo menos: −2 o -2.")}</p>
        <div class="fila-btn">
          <button type="button" class="btn" id="{pid}-comprobar">Check</button>
          <button type="button" class="btn-sec" id="{pid}-nuevo">New exercise</button>
        </div>
        <div class="fb" id="{pid}-fb" role="status"></div>
        <p class="marcador" id="{pid}-marcador"></p>
      </div>'''

def tabla_reglas(cinco=True):
    """Tabla de las reglas de los exponentes (tres de la multiplicación o las cinco)."""
    filas = [(t("Product of powers", "Producto de potencias"), "a<sup>m</sup> · a<sup>n</sup> = a<sup>m+n</sup>", t("add", "se suman"), "x<sup>4</sup> · x<sup>3</sup> = x<sup>7</sup>"),
             (t("Power of a power", "Potencia de una potencia"), "(a<sup>m</sup>)<sup>n</sup> = a<sup>m·n</sup>", t("multiply", "se multiplican"), "(x<sup>4</sup>)<sup>3</sup> = x<sup>12</sup>"),
             (t("Power of a product", "Potencia de un producto"), "(a · b)<sup>n</sup> = a<sup>n</sup> · b<sup>n</sup>", t("share it out", "se reparte"), "(2x)<sup>3</sup> = 8x<sup>3</sup>")]
    if cinco:
        filas += [(t("Quotient of powers", "Cociente de potencias"), "a<sup>m</sup> ÷ a<sup>n</sup> = a<sup>m−n</sup>", t("subtract", "se restan"), "x<sup>7</sup> ÷ x<sup>2</sup> = x<sup>5</sup>"),
                  (t("Zero and negative exponents", "Exponente cero y negativo"), "a<sup>0</sup> = 1 · a<sup>−n</sup> = 1/a<sup>n</sup>", t("reciprocal", "recíproco"), "5<sup>0</sup> = 1 · 3<sup>−2</sup> = 1/9")]
    return filas

# Estilos de las páginas de práctica del Tema 2 (notación científica): el recorrido del punto, ordenar y columnas.
ESTILO_SCI = """  .recorrido{display:flex;justify-content:center;align-items:flex-end;flex-wrap:wrap;gap:3px;margin:26px 0 10px;font-family:Consolas,'Courier New',monospace;}
  .celda{position:relative;width:34px;height:46px;border:2px solid var(--tema-bg2);border-radius:6px;background:#fff;display:flex;align-items:center;justify-content:center;font-size:24px;font-weight:700;color:var(--txt);}
  .celda.saltado{background:var(--tema-bg);border-color:var(--tema);}
  .celda.relleno{background:#fff8e1;border-color:#f9a825;border-style:dashed;color:#6d4c00;}
  .celda .marca{position:absolute;top:-22px;left:0;right:0;text-align:center;font-size:13px;color:var(--tema-d);font-family:inherit;}
  .punto{width:14px;height:46px;display:flex;align-items:flex-end;justify-content:center;font-size:34px;line-height:1;font-weight:900;color:#b71c1c;}
  .leyenda{display:flex;gap:16px;flex-wrap:wrap;justify-content:center;font-size:14px;color:var(--gris);margin:4px 0 8px;}
  .leyenda span::before{content:"";display:inline-block;width:14px;height:14px;border-radius:3px;margin-right:6px;vertical-align:-2px;border:2px solid var(--tema-bg2);}
  .leyenda .l-salto::before{background:var(--tema-bg);border-color:var(--tema);}
  .leyenda .l-relleno::before{background:#fff8e1;border-color:#f9a825;border-style:dashed;}
  .estado .grande{font-size:20px;font-weight:700;}
  .lista-orden{list-style:none;margin:12px 0;padding:0;counter-reset:ord;}
  .lista-orden li{display:flex;align-items:center;gap:10px;flex-wrap:wrap;background:#fff;border:2px solid #d8d8d8;border-radius:8px;padding:8px 12px;margin:8px 0;counter-increment:ord;}
  .lista-orden li::before{content:counter(ord);background:var(--tema-bg);color:var(--tema-d);width:26px;height:26px;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;font-weight:700;font-size:14px;flex-shrink:0;}
  .lista-orden li.bien{border-color:var(--ok);background:var(--ok-bg);}
  .lista-orden li.mal{border-color:#b71c1c;background:#ffebee;}
  .lista-orden .nombre{flex:1;min-width:160px;font-weight:600;}
  .lista-orden .flechas{display:flex;gap:6px;}
  .lista-orden .flechas button{background:#fff;border:2px solid var(--tema);color:var(--tema-d);border-radius:6px;width:40px;height:36px;font-weight:700;}
  .columnas{font-family:Consolas,'Courier New',monospace;font-size:22px;text-align:right;display:inline-block;margin:6px auto;padding:10px 18px;background:#fff;border:1px solid #d8d8d8;border-radius:8px;line-height:1.5;}
  .columnas .raya{border-top:3px solid var(--tema);}
  .centro{text-align:center;}
  .salida:empty{display:none;}
  .enun .ex,.opcion .ex,.salida .ex,.lista-orden .ex,.estado .ex{font-size:18px;}"""

def selector(pid, ops):
    """Lista para elegir la operación de un problema: ops = [(valor, texto)]."""
    if not ops:
        return ""
    o = "".join(f'<option value="{v}">{x}</option>' for v, x in ops)
    return f'\n        <div class="campos"><div class="campo" style="margin-bottom:10px;"><label for="{pid}-op">{t("Which operation solves the problem?", "¿Qué operación resuelve el problema?")}</label><select id="{pid}-op"><option value="">{t("Choose an operation", "Elija una operación")}</option>{o}</select></div></div>'

def sci_input(pid, titulo, intro="", ops=None):
    """Practice with a typed answer in scientific notation (creaPracticaSci)."""
    return f'''      <h3>{titulo}</h3>{intro}
      <div class="practica" id="{pid}">
        <div class="enun" id="{pid}-enun"></div>{selector(pid, ops)}
        <div class="campos campos-sci">
          <div class="campo"><label for="{pid}-c">{t("Coefficient", "Coeficiente")}</label><input type="text" inputmode="decimal" autocomplete="off" class="corto" id="{pid}-c"></div>
          <div class="campo" aria-hidden="true" style="font-size:20px;font-weight:700;padding-bottom:8px;white-space:nowrap;">× 10</div>
          <div class="campo"><label for="{pid}-e">{t("Exponent", "Exponente")}</label><input type="text" autocomplete="off" class="corto" id="{pid}-e"></div>
        </div>
        <p class="nota">{t("Use a decimal point (4.5). For a negative exponent, type the minus sign: −3 or -3.", "Use punto decimal (4.5, no 4,5). Para un exponente negativo escriba el signo menos: −3 o -3.")}</p>
        <div class="fila-btn">
          <button type="button" class="btn" id="{pid}-comprobar">Check</button>
          <button type="button" class="btn-sec" id="{pid}-nuevo">New exercise</button>
        </div>
        <div class="fb" id="{pid}-fb" role="status"></div>
        <p class="marcador" id="{pid}-marcador"></p>
      </div>'''


ESTILO_RAD = """  .linea.grande{font-size:1.35rem;font-weight:700;color:var(--acento);}
  .linea.veredicto,.veredicto{font-weight:700;color:var(--ok);}
  .fraccion-grande .grande{font-size:2rem;font-weight:700;}
  .elecciones{display:flex;flex-wrap:wrap;gap:8px;margin:8px 0;}
  .salida:empty{display:none;}"""

def desig(pid, titulo, nota=None):
    """Typed practice for an inequality: sign + boundary number (creaPracticaDesig in inequalities.js)."""
    nota = nota or t("Choose the sign of the solution and type the number. It can be negative or a fraction like 5/2.", "Elija el signo de la solución y escriba el número. Puede ser negativo o una fracción como 5/2.")
    ops = "".join(f'<option value="{v}">{h}</option>' for v, h in (("&lt;", "&lt;"), ("&gt;", "&gt;"), ("≤", "≤"), ("≥", "≥")))
    return f'''      <h3>{titulo}</h3>
      <div class="practica" id="{pid}">
        <div class="enun" id="{pid}-enun"></div>
        <div class="campos campos-sci">
          <div class="campo" aria-hidden="true" style="font-size:22px;font-weight:700;padding-bottom:6px;">x</div>
          <div class="campo"><label for="{pid}-s">{t("Sign", "Signo")}</label><select id="{pid}-s"><option value="">{t("Choose", "Elija")}</option>{ops}</select></div>
          <div class="campo"><label for="{pid}-v">{t("Boundary number", "Número límite")}</label><input type="text" autocomplete="off" class="corto" id="{pid}-v"></div>
        </div>
        <p class="nota">{nota}</p>
        <div class="fila-btn">
          <button type="button" class="btn" id="{pid}-comprobar">Check</button>
          <button type="button" class="btn-sec" id="{pid}-nuevo">New exercise</button>
        </div>
        <div class="fb" id="{pid}-fb" role="status"></div>
        <p class="marcador" id="{pid}-marcador"></p>
      </div>'''
