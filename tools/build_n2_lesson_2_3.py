"""Level 2 · Lesson 2.3 · Square roots of perfect squares — builds the lesson and its practice page in English and in Spanish.
Then run tools/ged_standards.py, tools/ged_standards_es.py and tools/build_indices.py."""
import json
import bilingue as B
from bilingue import t, T, practica, enlace, calc, caja, ejemplo, tabla, svg
from n2 import pot

B.NIVEL = 2
N = "2-3"
TEMA = ("Fractions, exponents, and roots", "Fracciones, exponentes y raíces")
TIT = ("Square roots of perfect squares", "Raíces cuadradas de cuadrados perfectos")

def rz(n):
    """√n con la raya sobre el radicando."""
    return f'√<span style="border-top:2px solid currentColor;padding:0 2px">{n}</span>'

def cuadricula(n, etiqueta):
    c = 30; x0 = 140; y0 = 16; s = []
    for i in range(n):
        for j in range(n):
            s.append(f'<rect x="{x0 + j*c}" y="{y0 + i*c}" width="{c}" height="{c}" fill="#e3f2fd" stroke="#0d47a1" stroke-width="1"/>')
    s.append(f'<rect x="{x0}" y="{y0}" width="{n*c}" height="{n*c}" fill="none" stroke="#0d47a1" stroke-width="3"/>')
    s.append(f'<text x="{x0 + n*c/2}" y="{y0 + n*c + 26}" text-anchor="middle" font-size="18" font-weight="700" fill="#0d47a1">{t("side", "lado")} = {n}</text>')
    s.append(f'<text x="{x0 - 12}" y="{y0 + n*c/2 + 6}" text-anchor="end" font-size="18" font-weight="700" fill="#0d47a1">{n}</text>')
    return svg(f"0 0 460 {y0 + n*c + 40}", etiqueta, "".join(s), 420)

def recta_raiz():
    """Recta de 6 a 9 con √50 marcado cerca de 7.07."""
    x = lambda v: 40 + (v - 6) * 180
    s = [f'<line x1="20" y1="80" x2="600" y2="80" stroke="#424242" stroke-width="2"/>']
    for v in range(6, 10):
        s.append(f'<line x1="{x(v)}" y1="70" x2="{x(v)}" y2="90" stroke="#424242" stroke-width="2"/><text x="{x(v)}" y="114" text-anchor="middle" font-size="18" fill="#222">{v}</text>')
        s.append(f'<text x="{x(v)}" y="138" text-anchor="middle" font-size="14" fill="#555">(√{v*v})</text>')
    xv = x(50 ** 0.5)
    s.append(f'<circle cx="{xv:.1f}" cy="80" r="8" fill="#b71c1c"/><text x="{xv:.1f}" y="52" text-anchor="middle" font-size="18" font-weight="700" fill="#b71c1c">√50 ≈ 7.1</text>')
    return svg("0 0 620 150", t("A number line from 6 to 9. Under each whole number is its square root form: 6 is √36, 7 is √49, 8 is √64, and 9 is √81. The square root of 50 is marked just to the right of 7, at about 7.1.",
                               "Una recta numérica de 6 a 9. Debajo de cada entero está su forma de raíz: 6 es √36, 7 es √49, 8 es √64 y 9 es √81. La raíz de 50 está marcada justo a la derecha del 7, en 7.1 aproximadamente."), "".join(s), 580)

def leccion():
    n = N
    s1 = f'''<p>{t("In Lesson 2.2 you learned to square numbers and you learned the fifteen perfect squares from 1 to 225. This lesson brings the <strong>inverse operation</strong>: the square root. Just as subtracting undoes adding, the square root undoes squaring.",
"En la Lección 2.2 aprendió a elevar números al cuadrado y se aprendió los quince cuadrados perfectos del 1 al 225. Esta lección trae la <strong>operación inversa</strong>: la raíz cuadrada. Así como restar deshace sumar, la raíz cuadrada deshace el elevar al cuadrado.")}</p>
<p>{t("The square root of a number answers the question: <strong>\"What number times itself gives this number?\"</strong> You write it with the radical sign: √.", "La raíz cuadrada de un número responde a la pregunta: <strong>«¿qué número, multiplicado por sí mismo, da este número?»</strong>. Se escribe con el signo radical: √.")}</p>
<p style="text-align:center;font-size:1.3em"><strong>{t("If", "Si")} {pot(7, 2)} = 49, {t("then", "entonces")} {rz(49)} = 7</strong></p>
<p>{t("The number under the radical sign is the <strong>radicand</strong>. If the radicand is a perfect square, its square root is a whole number.", "El número que está dentro del signo radical se llama <strong>radicando</strong>. Si el radicando es un cuadrado perfecto, su raíz cuadrada es un número entero.")}</p>
{tabla(t("Squares and square roots", "Cuadrados y raíces cuadradas"), t("Each multiplication of a number by itself and the square root it gives", "Cada multiplicación de un número por sí mismo y la raíz cuadrada que da"),
       [t("Because…", "Porque…"), t("…we know that", "…se sabe que")],
       [["5 × 5 = 25", rz(25) + " = 5"], ["9 × 9 = 81", rz(81) + " = 9"], ["12 × 12 = 144", rz(144) + " = 12"], ["15 × 15 = 225", rz(225) + " = 15"]])}
{caja("tip", t("The direct strategy", "La estrategia directa"), t("<p>To find the square root of a perfect square, remember which number squared gives it. The table of perfect squares from Lesson 2.2, read backward, is a table of square roots.</p>",
"<p>Para hallar la raíz cuadrada de un cuadrado perfecto, recuerde qué número elevado al cuadrado lo produjo. La tabla de cuadrados perfectos de la Lección 2.2, leída al revés, es una tabla de raíces.</p>"))}
{caja("ojo", t("Watch out!", "¡Ojo!"), t(f"<p>The square root is <strong>not</strong> half of the number. {rz(64)} is 8, not 32: 8 × 8 = 64.</p>", f"<p>La raíz cuadrada <strong>no</strong> es la mitad del número. {rz(64)} es 8, no 32: 8 × 8 = 64.</p>"))}
{practica("p1", t("Practice 1 — An exact root", "Práctica 1 — Una raíz exacta"), t(f"What is {rz(64)}?", f"¿Cuánto es {rz(64)}?"),
          [("a", "32"), ("b", "8"), ("c", "16"), ("d", "4,096")])}
{practica("p2", t("Practice 2 — Undo the root", "Práctica 2 — Deshacer la raíz"), t(f"If {rz('x')} = 11, what is x?", f"Si {rz('x')} = 11, ¿cuánto vale x?"),
          [("a", "22"), ("b", "121"), ("c", "5.5"), ("d", "111")])}
{enlace(n, t("inverse", "inversa"), t("the root as the inverse operation", "la raíz como operación inversa"), t("Match each perfect square with its root and practice in both directions.", "Relacione cada cuadrado perfecto con su raíz y practique en los dos sentidos."))}'''

    s2 = f'''<p>{t("The square root has a clear meaning in geometry. You find the area of a square by squaring its side. So, if you know the area, the square root of the area gives you the side.", "La raíz cuadrada tiene un significado geométrico muy claro. El área de un cuadrado se halla elevando su lado al cuadrado. Por eso, si se conoce el área, la raíz cuadrada del área da la medida del lado.")}</p>
{cuadricula(6, t("A square made of 36 small squares, with 6 small squares on each side.", "Un cuadrado formado por 36 cuadritos, con 6 cuadritos por lado."))}
<p>{t(f"A square with an area of 36 square units has exactly 6 small squares on each side, because 6 × 6 = 36. You can <em>see</em> that {rz(36)} = 6: it is the length of the side.", f"Un cuadrado de 36 unidades cuadradas de área tiene exactamente 6 cuadritos por lado, porque 6 × 6 = 36. Se <em>ve</em> que {rz(36)} = 6: es la medida del lado.")}</p>
{ejemplo(t("Example: a square garden has an area of 121 square feet. How long is each side?", "Ejemplo: un jardín cuadrado tiene un área de 121 pies cuadrados. ¿Cuánto mide cada lado?"),
  [("1", t("Step 1.", "Paso 1."), t(f"The side is the square root of the area: {rz(121)}.", f"El lado es la raíz cuadrada del área: {rz(121)}.")),
   ("2", t("Step 2.", "Paso 2."), t("Look for the number that squared gives 121: 11 × 11 = 121.", "Se busca el número que al cuadrado da 121: 11 × 11 = 121.")),
   ("✓", t("Result.", "Resultado."), t("Each side of the garden is <strong>11 feet</strong> long.", "Cada lado del jardín mide <strong>11 pies</strong>."))])}
{caja("ojo", t("Area or perimeter?", "¿Área o perímetro?"), t("<p>To get the side from the <strong>area</strong>, take the square root. To get it from the <strong>perimeter</strong>, divide by 4. For a garden of 121 square feet, the side is 11 feet, not 121 ÷ 4.</p>",
"<p>Para hallar el lado a partir del <strong>área</strong>, se saca la raíz cuadrada. A partir del <strong>perímetro</strong>, se divide entre 4. En un jardín de 121 pies cuadrados, el lado mide 11 pies, no 121 ÷ 4.</p>"))}
{practica("p3", t("Practice 3 — The side of a square", "Práctica 3 — El lado de un cuadrado"), t("A square tile covers 100 square inches. How long is each side?", "Una loseta cuadrada cubre 100 pulgadas cuadradas. ¿Cuánto mide cada lado?"),
          [("a", t("25 inches", "25 pulgadas")), ("b", t("50 inches", "50 pulgadas")), ("c", t("10 inches", "10 pulgadas")), ("d", t("1,000 inches", "1,000 pulgadas"))])}
{enlace(n, t("side-of-square", "lado-cuadrado"), t("the root as the side of a square", "la raíz como lado de un cuadrado"), t("Change the area of a square and see how long its side is.", "Cambie el área de un cuadrado y vea cuánto mide su lado."))}'''

    s3 = f'''<p>{t(f"Not every number is a perfect square. The square root of a number like 50 is not a whole number, but you can <strong>estimate</strong> it by placing it between two perfect squares next to each other.", f"No todos los números son cuadrados perfectos. La raíz cuadrada de un número como 50 no es un entero, pero se puede <strong>estimar</strong> ubicándola entre dos cuadrados perfectos consecutivos.")}</p>
{ejemplo(t(f"Example: estimate {rz(50)}", f"Ejemplo: estime {rz(50)}"),
  [("1", t("Step 1.", "Paso 1."), t("Find the perfect squares closest to 50: 49 and 64.", "Se buscan los cuadrados perfectos más cercanos a 50: 49 y 64.")),
   ("2", t("Step 2.", "Paso 2."), t(f"Since 49 &lt; 50 &lt; 64, then {rz(49)} &lt; {rz(50)} &lt; {rz(64)}.", f"Como 49 &lt; 50 &lt; 64, entonces {rz(49)} &lt; {rz(50)} &lt; {rz(64)}.")),
   ("3", t("Step 3.", "Paso 3."), t(f"That is: 7 &lt; {rz(50)} &lt; 8. And 50 is very close to 49, so {rz(50)} is close to 7.", f"Es decir: 7 &lt; {rz(50)} &lt; 8. Y 50 está muy cerca de 49, así que {rz(50)} está cerca de 7.")),
   ("✓", t("Result.", "Resultado."), t(f"{rz(50)} is between 7 and 8, closer to 7 (about 7.1).", f"{rz(50)} está entre 7 y 8, más cerca de 7 (aproximadamente 7.1)."))])}
{recta_raiz()}
{caja("tip", t("Which one is it closer to?", "¿De cuál está más cerca?"), t(f"<p>Look at which perfect square the radicand is closer to. {rz(50)} is almost at {rz(49)}, so its value is just above 7. But {rz(60)} is closer to {rz(64)}, so its value is close to 8 (about 7.7).</p>",
f"<p>Fíjese de qué cuadrado perfecto está más cerca el radicando. {rz(50)} está casi pegado a {rz(49)}, así que su valor queda apenas por encima de 7. En cambio, {rz(60)} está más cerca de {rz(64)}, así que su valor se acerca a 8 (aproximadamente 7.7).</p>"))}
{practica("p4", t("Practice 4 — Between two whole numbers", "Práctica 4 — Entre dos enteros"), t(f"{rz(30)} is between:", f"{rz(30)} está entre:"),
          [("a", t("4 and 5", "4 y 5")), ("b", t("5 and 6", "5 y 6")), ("c", t("6 and 7", "6 y 7")), ("d", t("15 and 16", "15 y 16"))])}
{practica("p5", t("Practice 5 — Not exact", "Práctica 5 — No exacta"), t("Which of these square roots is <strong>not</strong> a whole number?", "¿Cuál de estas raíces <strong>no</strong> es un número entero?"),
          [("a", rz(49)), ("b", rz(100)), ("c", rz(70)), ("d", rz(196))])}
{enlace(n, t("estimate", "estimar"), t("estimating square roots", "estimar raíces no exactas"), t("Place a root between two whole numbers and decide which one it is closer to.", "Ubique una raíz entre dos enteros y decida de cuál está más cerca."))}'''

    s4 = f'''<p>{t(f"Every square root can be checked with the inverse operation: if {rz(144)} = 12, then 12 × 12 must be 144. That way you catch a mistake without a calculator.", f"Toda raíz se comprueba con la operación inversa: si {rz(144)} = 12, entonces 12 × 12 tiene que dar 144. Así se detecta un error sin calculadora.")}</p>
{calc(t("Square roots on the calculator", "Las raíces en la calculadora"), t(f"""<p>On the TI-30XS, the square root is above the {T("x<sup>2</sup>")} key. Press {T("2nd")} {T("x<sup>2</sup>")}, type the radicand, for example {T("1")}{T("4")}{T("4")}, and press {T("enter")}. The screen shows 12.</p>
<p>The calculator is for <strong>checking</strong>. On the GED test time is short: knowing that {rz(81)} = 9 by heart is much faster than typing it.</p>""",
f"""<p>En la TI-30XS, la raíz cuadrada está encima de la tecla {T("x<sup>2</sup>")}. Pulse {T("2nd")} {T("x<sup>2</sup>")}, escriba el radicando, por ejemplo {T("1")}{T("4")}{T("4")}, y pulse {T("enter")}. La pantalla muestra 12.</p>
<p>La calculadora sirve para <strong>comprobar</strong>. En el examen de GED el tiempo es limitado: saber de memoria que {rz(81)} = 9 es mucho más rápido que teclearlo.</p>"""))}
{practica("p6", t("Practice 6 — Check it", "Práctica 6 — Compruébelo"), t(f"Someone wrote {rz(169)} = 14. Is it right?", f"Alguien escribió {rz(169)} = 14. ¿Es correcto?"),
          [("a", t("Yes, it is right.", "Sí, es correcto.")), ("b", t("No: 14 × 14 = 196, so the root is 13.", "No: 14 × 14 = 196, así que la raíz es 13.")), ("c", t("You can only tell with a calculator.", "Solo se puede saber con calculadora."))])}
{enlace(n, t("check", "verificar"), t("checking by squaring", "verificar elevando al cuadrado"), t("Check each root with the inverse operation before you use the calculator.", "Compruebe cada raíz con la operación inversa antes de usar la calculadora."))}'''

    secciones = [("s-" + t("inverse", "inversa"), t("The square root as the inverse operation", "La raíz cuadrada como operación inversa"), s1),
                 ("s-" + t("side-of-square", "lado-cuadrado"), t("The square root as the side of a square", "La raíz cuadrada como lado de un cuadrado"), s2),
                 ("s-" + t("estimate", "estimar"), t("Estimating square roots that are not exact", "Estimar raíces no exactas"), s3),
                 ("s-" + t("check", "verificar"), t("Checking: by squaring and on the calculator", "Verificar: elevando al cuadrado y con la calculadora"), s4)]

    lesson = {"next": t("Lesson 3.1", "Lección 3.1"), "review": t("sections 1, 2, and 3", "las secciones 1, 2 y 3"),
     "practice": {
      "p1": {"ok": "b", "hints": {"a": t("32 is half of 64. The root is the number that times itself gives 64.", "32 es la mitad de 64. La raíz es el número que multiplicado por sí mismo da 64."),
                                   "c": t("16 × 16 = 256, not 64.", "16 × 16 = 256, no 64."),
                                   "d": t("4,096 is 64 squared. The root goes the other way.", "4,096 es 64 al cuadrado. La raíz va en el sentido contrario.")},
             "right": t("8 × 8 = 64.", "8 × 8 = 64."), "solution": t("Which number times itself gives 64? 8 × 8 = 64, so the square root of 64 is 8.", "¿Qué número multiplicado por sí mismo da 64? 8 × 8 = 64, así que la raíz cuadrada de 64 es 8.")},
      "p2": {"ok": "b", "hints": {"a": t("To undo the root, square: 11 × 11, not 11 × 2.", "Para deshacer la raíz, se eleva al cuadrado: 11 × 11, no 11 × 2."),
                                   "c": t("5.5 is half of 11. To undo the root, square 11.", "5.5 es la mitad de 11. Para deshacer la raíz, eleve 11 al cuadrado."),
                                   "d": t("Check the multiplication: 11 × 11.", "Revise la multiplicación: 11 × 11.")},
             "right": t("x = 11 × 11 = 121.", "x = 11 × 11 = 121."), "solution": t("Squaring undoes the root: x = 11<sup>2</sup> = 121. Check: the square root of 121 is 11.", "Elevar al cuadrado deshace la raíz: x = 11<sup>2</sup> = 121. Compruebe: la raíz cuadrada de 121 es 11.")},
      "p3": {"ok": "c", "hints": {"a": t("25 is 100 ÷ 4. That gives the side from the perimeter, not from the area.", "25 es 100 ÷ 4. Eso da el lado a partir del perímetro, no del área."),
                                   "b": t("50 is half of 100. The side is the square root of the area.", "50 es la mitad de 100. El lado es la raíz cuadrada del área."),
                                   "d": t("The side is shorter than the area number. Take the square root of 100.", "El lado es menor que el número del área. Saque la raíz cuadrada de 100.")},
             "right": t("10 × 10 = 100, so each side is 10 inches.", "10 × 10 = 100, así que cada lado mide 10 pulgadas."), "solution": t("The side is the square root of the area: the square root of 100 is 10, because 10 × 10 = 100.", "El lado es la raíz cuadrada del área: la raíz de 100 es 10, porque 10 × 10 = 100.")},
      "p4": {"ok": "b", "hints": {"a": t("4 × 4 = 16 and 5 × 5 = 25. 30 is more than 25.", "4 × 4 = 16 y 5 × 5 = 25. 30 es más que 25."),
                                   "c": t("6 × 6 = 36, and 30 is less than 36.", "6 × 6 = 36, y 30 es menos que 36."),
                                   "d": t("15 is half of 30. Look for perfect squares near 30.", "15 es la mitad de 30. Busque cuadrados perfectos cerca de 30.")},
             "right": t("25 &lt; 30 &lt; 36, so the root is between 5 and 6.", "25 &lt; 30 &lt; 36, así que la raíz está entre 5 y 6."), "solution": t("The perfect squares around 30 are 25 and 36. Their roots are 5 and 6, so the square root of 30 is between 5 and 6.", "Los cuadrados perfectos que rodean al 30 son 25 y 36. Sus raíces son 5 y 6, así que la raíz de 30 está entre 5 y 6.")},
      "p5": {"ok": "c", "hints": {"a": t("49 = 7 × 7. Its root is exact.", "49 = 7 × 7. Su raíz es exacta."),
                                   "b": t("100 = 10 × 10. Its root is exact.", "100 = 10 × 10. Su raíz es exacta."),
                                   "d": t("196 = 14 × 14. Its root is exact.", "196 = 14 × 14. Su raíz es exacta.")},
             "right": t("70 is not a perfect square: 8 × 8 = 64 and 9 × 9 = 81.", "70 no es un cuadrado perfecto: 8 × 8 = 64 y 9 × 9 = 81."), "solution": t("49, 100, and 196 are perfect squares. 70 is between 64 and 81, so its root is between 8 and 9: it is not a whole number.", "49, 100 y 196 son cuadrados perfectos. 70 está entre 64 y 81, así que su raíz está entre 8 y 9: no es un entero.")},
      "p6": {"ok": "b", "hints": {"a": t("Check it: multiply 14 × 14.", "Compruébelo: multiplique 14 × 14."),
                                   "c": t("You can check it by hand: multiply 14 × 14.", "Se puede comprobar a mano: multiplique 14 × 14.")},
             "right": t("14 × 14 = 196, not 169. The root of 169 is 13.", "14 × 14 = 196, no 169. La raíz de 169 es 13."), "solution": t("Check with the inverse operation: 14 × 14 = 196, which is not 169. The right root is 13, because 13 × 13 = 169.", "Se comprueba con la operación inversa: 14 × 14 = 196, que no es 169. La raíz correcta es 13, porque 13 × 13 = 169.")}
     },
     "quiz": {
      "A": {"ok": "d", "hints": {"a": t("That is half of 81.", "Esa es la mitad de 81."), "b": t("8 × 8 = 64.", "8 × 8 = 64."), "c": t("That is 81 squared.", "Eso es 81 al cuadrado.")}, "solution": t("9 × 9 = 81, so the square root of 81 is 9.", "9 × 9 = 81, así que la raíz de 81 es 9.")},
      "B": {"ok": "a", "hints": {"b": t("That is half of 144.", "Esa es la mitad de 144."), "c": t("14 × 14 = 196.", "14 × 14 = 196."), "d": t("11 × 11 = 121.", "11 × 11 = 121.")}, "solution": t("12 × 12 = 144.", "12 × 12 = 144.")},
      "C": {"ok": "c", "hints": {"a": t("That is 225 ÷ 9. Look for a number that times itself gives 225.", "Eso es 225 ÷ 9. Busque un número que multiplicado por sí mismo dé 225."), "b": t("14 × 14 = 196.", "14 × 14 = 196."), "d": t("That is about half of 225.", "Eso es más o menos la mitad de 225.")}, "solution": t("15 × 15 = 225.", "15 × 15 = 225.")},
      "D": {"ok": "b", "hints": {"a": t("That is 196 ÷ 4: the side from the perimeter, not from the area.", "Eso es 196 ÷ 4: el lado a partir del perímetro, no del área."), "c": t("That is half of 196.", "Esa es la mitad de 196."), "d": t("13 × 13 = 169.", "13 × 13 = 169.")}, "solution": t("The side is the square root of the area: 14 × 14 = 196, so each side is 14 feet.", "El lado es la raíz del área: 14 × 14 = 196, así que cada lado mide 14 pies.")},
      "E": {"ok": "c", "hints": {"a": t("5 × 5 = 25 and 6 × 6 = 36: 40 is more than 36.", "5 × 5 = 25 y 6 × 6 = 36: 40 es más que 36."), "b": t("40 is less than 7 × 7 = 49.", "40 es menos que 7 × 7 = 49."), "d": t("20 is half of 40. Look for perfect squares near 40.", "20 es la mitad de 40. Busque cuadrados perfectos cerca de 40.")}, "solution": t("36 &lt; 40 &lt; 49, so the square root of 40 is between 6 and 7.", "36 &lt; 40 &lt; 49, así que la raíz de 40 está entre 6 y 7.")},
      "F": {"ok": "b", "hints": {"a": t("60 is 11 away from 49 and only 4 away from 64.", "60 está a 11 de 49 y solo a 4 de 64."), "c": t("60 is not halfway: it is closer to 64.", "60 no está en el medio: está más cerca de 64."), "d": t("49 &lt; 60 &lt; 64, so the root is between 7 and 8.", "49 &lt; 60 &lt; 64, así que la raíz está entre 7 y 8.")}, "solution": t("60 is closer to 64 than to 49, so its root is closer to 8 (about 7.7).", "60 está más cerca de 64 que de 49, así que su raíz está más cerca de 8 (aproximadamente 7.7).")},
      "G": {"ok": "a", "hints": {"b": t("To undo the root, square: 13 × 13, not 13 × 2.", "Para deshacer la raíz, se eleva al cuadrado: 13 × 13, no 13 × 2."), "c": t("That is half of 13. Square it instead.", "Esa es la mitad de 13. Elévelo al cuadrado."), "d": t("Check the multiplication: 13 × 13 = 130 + 39.", "Revise la multiplicación: 13 × 13 = 130 + 39.")}, "solution": t("x = 13<sup>2</sup> = 169.", "x = 13<sup>2</sup> = 169.")},
      "H": {"ok": "d", "hints": {"a": t("36 = 6 × 6: its root is exact.", "36 = 6 × 6: su raíz es exacta."), "b": t("121 = 11 × 11: its root is exact.", "121 = 11 × 11: su raíz es exacta."), "c": t("225 = 15 × 15: its root is exact.", "225 = 15 × 15: su raíz es exacta.")}, "solution": t("80 is between 64 and 81, so its root is between 8 and 9: not a whole number.", "80 está entre 64 y 81, así que su raíz está entre 8 y 9: no es un entero.")}
     }}

    quiz = [
     ("A", t(f"What is {rz(81)}?", f"¿Cuánto es {rz(81)}?"), [("a", "40.5"), ("b", "8"), ("c", "6,561"), ("d", "9")]),
     ("B", t(f"What is {rz(144)}?", f"¿Cuánto es {rz(144)}?"), [("a", "12"), ("b", "72"), ("c", "14"), ("d", "11")]),
     ("C", t(f"What is {rz(225)}?", f"¿Cuánto es {rz(225)}?"), [("a", "25"), ("b", "14"), ("c", "15"), ("d", "112")]),
     ("D", t("A square room has an area of 196 square feet. How long is each side?", "Una habitación cuadrada tiene un área de 196 pies cuadrados. ¿Cuánto mide cada lado?"), [("a", t("49 feet", "49 pies")), ("b", t("14 feet", "14 pies")), ("c", t("98 feet", "98 pies")), ("d", t("13 feet", "13 pies"))]),
     ("E", t(f"{rz(40)} is between:", f"{rz(40)} está entre:"), [("a", t("5 and 6", "5 y 6")), ("b", t("7 and 8", "7 y 8")), ("c", t("6 and 7", "6 y 7")), ("d", t("20 and 21", "20 y 21"))]),
     ("F", t(f"{rz(60)} is between 7 and 8. Which one is it closer to?", f"{rz(60)} está entre 7 y 8. ¿De cuál está más cerca?"), [("a", t("closer to 7", "más cerca de 7")), ("b", t("closer to 8", "más cerca de 8")), ("c", t("exactly in the middle", "justo en el medio")), ("d", t("It is not between 7 and 8.", "No está entre 7 y 8."))]),
     ("G", t(f"If {rz('x')} = 13, what is x?", f"Si {rz('x')} = 13, ¿cuánto vale x?"), [("a", "169"), ("b", "26"), ("c", "6.5"), ("d", "139")]),
     ("H", t("Which of these square roots is <strong>not</strong> a whole number?", "¿Cuál de estas raíces <strong>no</strong> es un número entero?"), [("a", rz(36)), ("b", rz(121)), ("c", rz(225)), ("d", rz(80))])]

    return B.pagina_leccion(n, 2, t(*TEMA), t(*TIT),
        t("The operation that undoes squaring: exact roots, the side of a square, estimating roots that are not exact, and checking.", "La operación que deshace el elevar al cuadrado: raíces exactas, el lado de un cuadrado, estimar raíces no exactas y comprobar."),
        ("🧮", t("Calculator to check", "Calculadora para comprobar")),
        [t("<strong>Explain</strong> the square root as the inverse of squaring.", "<strong>Explicar</strong> la raíz cuadrada como la operación inversa de elevar al cuadrado."),
         t("<strong>Find</strong> the square roots of the perfect squares up to 225 by heart.", "<strong>Hallar</strong> de memoria las raíces de los cuadrados perfectos hasta el 225."),
         t("<strong>Find</strong> the side of a square from its area.", "<strong>Hallar</strong> el lado de un cuadrado a partir de su área."),
         t("<strong>Estimate</strong> a square root that is not exact between two whole numbers.", "<strong>Estimar</strong> una raíz no exacta entre dos enteros consecutivos."),
         t("<strong>Check</strong> a square root by squaring, and on the calculator.", "<strong>Comprobar</strong> una raíz elevando al cuadrado y con la calculadora.")],
        secciones,
        (t("Write and solve ten exact square roots up to the square root of 225, four estimates between two whole numbers (say which one each root is closer to), and two problems that find the side of a square from its area. Check every root by squaring.",
           "Escriba y resuelva diez raíces exactas hasta la raíz de 225, cuatro estimaciones entre dos enteros (diga de cuál está más cerca cada raíz) y dos problemas que hallen el lado de un cuadrado a partir de su área. Compruebe cada raíz elevando al cuadrado."),
         t("Find something square around you: a floor tile, a window, a table. Measure one side in inches, find the area, and then check that the square root of the area gives the side back.",
           "Busque algo cuadrado a su alrededor: una loseta, una ventana, una mesa. Mida un lado en pulgadas, halle el área y compruebe que la raíz cuadrada del área le devuelve el lado.")),
        quiz,
        t("Self-check checklist for square roots", "Lista de autoevaluación de las raíces cuadradas"),
        t("Self-check checklist: skills for square roots", "Lista de autoevaluación: destrezas con raíces cuadradas"),
        [(t("Roots of perfect squares", "Raíces de cuadrados perfectos"), t("I find them up to 225 without a table and use them in problems.", "Las hallo hasta el 225 sin tabla y las uso en problemas."), t("I find them with the table of squares.", "Las hallo con la tabla de cuadrados."), t("I cannot find them yet, even with the table.", "Todavía no las hallo, ni con la tabla.")),
         (t("Square and root are inverses", "El cuadrado y la raíz son inversos"), t("I explain it and use it to solve and to check.", "Lo explico y lo uso para resolver y para comprobar."), t("I know it, but I do not use it with confidence.", "Lo sé, pero no lo aplico con seguridad."), t("I do not see the connection yet.", "Todavía no veo la relación.")),
         (t("Estimating roots", "Estimar raíces"), t("I place the root between two whole numbers and say which one it is closer to.", "Ubico la raíz entre dos enteros y digo de cuál está más cerca."), t("I place it between two whole numbers with help.", "La ubico entre dos enteros con ayuda."), t("I do not know where to start.", "No sé por dónde empezar.")),
         (t("The side of a square", "El lado de un cuadrado"), t("I find the side from the area and do not confuse it with the perimeter.", "Hallo el lado a partir del área y no lo confundo con el perímetro."), t("I find it, but sometimes I divide by 4 or by 2.", "Lo hallo, pero a veces divido entre 4 o entre 2."), t("I do not know how to find it.", "No sé hallarlo."))],
        t("<p>You finished Topic 2: fractions with signs, powers, and square roots. The idea that ties the topic together: <strong>the square root undoes squaring</strong>, and knowing the perfect squares makes both calculations quick.</p>\n<p><strong>Topic 3 · The full order of operations</strong> opens with <strong>Lesson 3.1 · Order of operations: review and nested parentheses</strong>. There, everything you have studied so far (integers, fractions, powers, and roots) will come together under one system of priorities.</p>",
          "<p>Terminó el Tema 2: las fracciones con signo, las potencias y las raíces cuadradas. La idea que une todo el tema: <strong>la raíz cuadrada deshace el elevar al cuadrado</strong>, y conocer los cuadrados perfectos hace rápidos los dos cálculos.</p>\n<p>El <strong>Tema 3 · PEMDAS completo</strong> abre con la <strong>Lección 3.1 · Orden de operaciones: repaso y paréntesis anidados</strong>. Allí todo lo estudiado hasta ahora (enteros, fracciones, potencias y raíces) se reunirá bajo un solo sistema de prioridades.</p>"),
        ("3-1", ("", t("Lesson 3.1 · Order of operations: review and nested parentheses", "Lección 3.1 · Orden de operaciones: repaso y paréntesis anidados"))),
        [(t("square root", "raíz cuadrada"), t("The number that times itself gives the radicand: the square root of 49 is 7.", "El número que multiplicado por sí mismo da el radicando: la raíz de 49 es 7.")),
         (t("radical sign", "signo radical"), t("The symbol √.", "El símbolo √.")),
         (t("radicand", "radicando"), t("The number under the radical sign.", "El número que está dentro del signo radical.")),
         (t("inverse operations", "operaciones inversas"), t("Two operations that undo each other, like squaring and taking the square root.", "Dos operaciones que se deshacen una a la otra, como elevar al cuadrado y sacar la raíz.")),
         (t("estimate", "estimar"), t("To find a value that is close, not exact: the square root of 50 is about 7.1.", "Hallar un valor cercano, no exacto: la raíz de 50 es aproximadamente 7.1."))],
        lesson)

# ---------------- practice page ----------------
TX = {
 "en": {
  "idaVuelta": "Squaring {n} gives {c}; the square root of {c} gives {n} back. Each operation undoes the other.",
  "raizNoMitad": "The root is not half: it is the number that times itself gives {c}.",
  "siRx": "If {r} = {n}, what is x?", "deshace": "Squaring undoes the root: x = {n}<sup>2</sup> = {c}.", "noDoble": "To undo the root, square: do not double.",
  "queNum": "What positive number times itself gives {c}?", "porque": "{r} = {n}, because {n} × {n} = {c}.",
  "lado": "side", "vozLC": "A square of {a} small squares, with {n} on each side.", "salidaLC": "Area: {a} small squares. Side: {r} = <strong>{n}</strong>, because {n} × {n} = {a}.",
  "ctx": [["A square garden has an area of {a} square feet. How long is each side, in feet?"], ["A square tile covers {a} square inches. How long is its side, in inches?"], ["A square board has {a} squares in all. How many squares are on each side?"], ["A square patio has an area of {a} square yards. How long is each side, in yards?"]],
  "solLado": "The side is the square root of the area: {r} = {n}.", "noPerim": "Dividing by 4 gives the side from the perimeter, not from the area. Here you need the square root.", "noMitadA": "The root is not half of the area.",
  "exacto": "{n} is a perfect square: {r} = {a} exactly.", "entre": "{a2} &lt; {n} &lt; {b2}, so {a} &lt; {r} &lt; {b}.",
  "cerca": "{n} is {x} away from {a2} and {y} away from {b2}: the root is closer to <strong>{c}</strong>. On a calculator, {r} ≈ {v}.", "igualDist": "{a} and {b} equally",
  "vozES": "Number line: the square root of {n} is {d}.", "exactamenteEn": "exactly at {a}", "entreY": "between {a} and {b}",
  "entreQ": "Between which two whole numbers is {r}?", "entreOp": "Between {a} and {b}", "bienEntre": "{a2} &lt; {n} &lt; {b2}.", "malEntre": "Look for the perfect squares around it: {a2} and {b2}. That is why it is between {a} and {b}.", "pistaEntre": "Which perfect squares are just below and just above {n}?",
  "cercaQ": "{r} is between {a} and {b}. Which one is it closer to?", "masCerca": "Closer to {k}", "medio": "Exactly in the middle", "bienCerca": "{n} is {x} away from {a2} and {y} away from {b2}. {r} ≈ {v}.", "pistaCerca": "Is {n} closer to {a2} or to {b2}?",
  "verifQ": "Someone wrote {r} = {k}. Is it right?", "si": "Yes, it is right", "no": "No, it is not right", "calc": "You can only tell with a calculator", "pistaCalc": "You can check by hand: multiply {k} × {k}.",
  "verifBien": "{k} × {k} = {c}, which is exactly {n}: the root is right.", "verifMal": "{k} × {k} = {c}, not {n}. The right root is {s}, because {s} × {s} = {n}.",
  "xEs": "If {r} = {n}, then x is:", "pistaX": "To undo the root, square it.", "bienX": "x = {n}<sup>2</sup> = {c}.",
  "areaQ": "A square has an area of {a} square inches. How long is each side?", "pulg": "inches", "bienArea": "{r} = {n}.", "malArea": "The side is the square root of the area: {n} inches, because {n} × {n} = {a}.", "pistaArea": "Area to side: take the square root.",
  "noEntQ": "Which of these square roots is <strong>not</strong> a whole number?", "bienNoEnt": "{m} is not a perfect square; {a} and {b} are.", "pistaNoEnt": "Which radicand is not a whole number times itself?"
 },
 "es": {
  "idaVuelta": "Elevar {n} al cuadrado da {c}; la raíz de {c} devuelve el {n}. Una operación deshace a la otra.",
  "raizNoMitad": "La raíz no es la mitad: es el número que multiplicado por sí mismo da {c}.",
  "siRx": "Si {r} = {n}, ¿cuánto vale x?", "deshace": "Elevar al cuadrado deshace la raíz: x = {n}<sup>2</sup> = {c}.", "noDoble": "Para deshacer la raíz, se eleva al cuadrado: no se duplica.",
  "queNum": "¿Qué número positivo, multiplicado por sí mismo, da {c}?", "porque": "{r} = {n}, porque {n} × {n} = {c}.",
  "lado": "lado", "vozLC": "Un cuadrado de {a} cuadritos, con {n} por lado.", "salidaLC": "Área: {a} cuadritos. Lado: {r} = <strong>{n}</strong>, porque {n} × {n} = {a}.",
  "ctx": [["Un jardín cuadrado tiene un área de {a} pies cuadrados. ¿Cuánto mide cada lado, en pies?"], ["Una loseta cuadrada cubre {a} pulgadas cuadradas. ¿Cuánto mide su lado, en pulgadas?"], ["Un tablero cuadrado tiene {a} casillas en total. ¿Cuántas casillas hay en cada lado?"], ["Un patio cuadrado tiene un área de {a} yardas cuadradas. ¿Cuánto mide cada lado, en yardas?"]],
  "solLado": "El lado es la raíz cuadrada del área: {r} = {n}.", "noPerim": "Dividir entre 4 da el lado a partir del perímetro, no del área. Aquí hace falta la raíz cuadrada.", "noMitadA": "La raíz no es la mitad del área.",
  "exacto": "{n} es un cuadrado perfecto: {r} = {a} exactamente.", "entre": "{a2} &lt; {n} &lt; {b2}, así que {a} &lt; {r} &lt; {b}.",
  "cerca": "{n} está a {x} de {a2} y a {y} de {b2}: la raíz está más cerca de <strong>{c}</strong>. Con calculadora, {r} ≈ {v}.", "igualDist": "{a} y de {b} por igual",
  "vozES": "Recta numérica: la raíz cuadrada de {n} está {d}.", "exactamenteEn": "exactamente en {a}", "entreY": "entre {a} y {b}",
  "entreQ": "¿Entre qué dos enteros consecutivos está {r}?", "entreOp": "Entre {a} y {b}", "bienEntre": "{a2} &lt; {n} &lt; {b2}.", "malEntre": "Busque los cuadrados perfectos que lo rodean: {a2} y {b2}. Por eso está entre {a} y {b}.", "pistaEntre": "¿Qué cuadrados perfectos quedan justo debajo y justo encima de {n}?",
  "cercaQ": "{r} está entre {a} y {b}. ¿De cuál está más cerca?", "masCerca": "Más cerca de {k}", "medio": "Justo en el medio", "bienCerca": "{n} está a {x} de {a2} y a {y} de {b2}. {r} ≈ {v}.", "pistaCerca": "¿{n} está más cerca de {a2} o de {b2}?",
  "verifQ": "Alguien escribió {r} = {k}. ¿Es correcto?", "si": "Sí, es correcto", "no": "No, no es correcto", "calc": "Solo se puede saber con calculadora", "pistaCalc": "Se puede comprobar a mano: multiplique {k} × {k}.",
  "verifBien": "{k} × {k} = {c}, que es justo {n}: la raíz es correcta.", "verifMal": "{k} × {k} = {c}, no {n}. La raíz correcta es {s}, porque {s} × {s} = {n}.",
  "xEs": "Si {r} = {n}, entonces x es:", "pistaX": "Para deshacer la raíz, se eleva al cuadrado.", "bienX": "x = {n}<sup>2</sup> = {c}.",
  "areaQ": "Un cuadrado tiene un área de {a} pulgadas cuadradas. ¿Cuánto mide cada lado?", "pulg": "pulgadas", "bienArea": "{r} = {n}.", "malArea": "El lado es la raíz cuadrada del área: {n} pulgadas, porque {n} × {n} = {a}.", "pistaArea": "Del área al lado: se saca la raíz cuadrada.",
  "noEntQ": "¿Cuál de estas raíces <strong>no</strong> es un número entero?", "bienNoEnt": "{m} no es un cuadrado perfecto; {a} y {b} sí lo son.", "pistaNoEnt": "¿Qué radicando no es un entero multiplicado por sí mismo?"
 }}

LOGICA = r'''
function F(s, o){ return s.replace(/\{(\w+)\}/g, function(_, k){ return o[k]; }); }
function esCuadrado(n){ var s = Math.round(Math.sqrt(n)); return s * s === n; }
function aprox1(x){ return (Math.round(x * 10) / 10).toFixed(1); }

/* ============ MODULE 1 · the inverse ============ */
function pintaIV(){
  var k = +$("iv-n").value; $("iv-nv").textContent = k;
  $("iv-salida").innerHTML = '<div class="linea grande">' + k + '<sup>2</sup> = ' + k + ' × ' + k + ' = ' + k * k + ' &nbsp;⟷&nbsp; ' + rz(k * k) + ' = ' + k + '</div><div class="linea">' + F(TXT.idaVuelta, { n: k, c: k * k }) + '</div>';
}
function genRaiz(){
  var k = aleatorio(2, 15), tipo = aleatorio(1, 3), c = k * k;
  if (tipo === 1) return { enun: rz(c) + " =", correcta: String(k), solucion: F(TXT.porque, { r: rz(c), n: k, c: c }), evalua: numE(k, c % 2 ? [] : [{ v: c / 2, msg: F(TXT.raizNoMitad, { c: c }) }]) };
  if (tipo === 2) return { enun: F(TXT.siRx, { r: rz("x"), n: k }), correcta: String(c), solucion: F(TXT.deshace, { n: k, c: c }), evalua: numE(c, [{ v: 2 * k, msg: TXT.noDoble }]) };
  return { enun: F(TXT.queNum, { c: c }), correcta: String(k), solucion: F(TXT.porque, { r: rz(c), n: k, c: c }), evalua: numE(k, []) };
}

/* ============ MODULE 2 · the side of a square ============ */
function pintaLC(){
  var A = +$("lc-a").value, k = Math.round(Math.sqrt(A)), c = Math.min(26, 300 / k), x0 = 320 - k * c / 2, y0 = 16;
  var s = '<svg class="figura" viewBox="0 0 640 ' + f1(k * c + 56) + '" role="img" aria-label="' + F(TXT.vozLC, { a: A, n: k }) + '">';
  for (var i = 0; i < k; i++) for (var j = 0; j < k; j++) s += '<rect x="' + f1(x0 + j * c) + '" y="' + f1(y0 + i * c) + '" width="' + f1(c) + '" height="' + f1(c) + '" fill="#e3f2fd" stroke="#0d47a1" stroke-width="1"/>';
  s += '<rect x="' + f1(x0) + '" y="' + y0 + '" width="' + f1(k * c) + '" height="' + f1(k * c) + '" fill="none" stroke="#0d47a1" stroke-width="3"/>';
  s += texto([320, y0 + k * c + 24], TXT.lado + " = " + k, 18, "#0d47a1") + texto([x0 - 16, y0 + k * c / 2], k, 18, "#0d47a1");
  $("lc-svg").innerHTML = s + '</svg>';
  $("lc-salida").innerHTML = '<div class="linea">' + F(TXT.salidaLC, { a: A, r: rz(A), n: k }) + '</div>';
}
function genLado(){
  var k = aleatorio(3, 15), A = k * k, ctx = elige(TXT.ctx), p = [];
  if (A % 4 === 0 && A / 4 !== k) p.push({ v: A / 4, msg: TXT.noPerim });
  if (A % 2 === 0 && A / 2 !== k) p.push({ v: A / 2, msg: TXT.noMitadA });
  return { enun: F(ctx[0], { a: A }), correcta: String(k), solucion: F(TXT.solLado, { r: rz(A), n: k }), evalua: numE(k, p) };
}

/* ============ MODULE 3 · estimating ============ */
function rectaRaiz(lo, hi, v, n, voz){
  var W = 640, x0 = 40, x1 = 600, y = 70; function X(t){ return x0 + (t - lo) * (x1 - x0) / (hi - lo); }
  var s = '<svg class="figura" viewBox="0 0 ' + W + ' 140" role="img" aria-label="' + voz + '">' + linea([x0 - 16, y], [x1 + 16, y], "#424242", 2);
  for (var t = lo; t <= hi + 1e-9; t += 0.1){ var e = Math.abs(t - Math.round(t)) < 1e-6; s += linea([X(t), y - (e ? 10 : 5)], [X(t), y + (e ? 10 : 5)], "#424242", e ? 2 : 1); if (e){ s += texto([X(t), y + 28], Math.round(t), 18, "#222", 400) + texto([X(t), y + 50], "(√" + Math.round(t) * Math.round(t) + ")", 14, "#555", 400); } }
  s += '<circle cx="' + f1(X(v)) + '" cy="' + y + '" r="8" fill="#b71c1c"/>' + texto([X(v), y - 26], "√" + n, 18, "#b71c1c");
  return s + '</svg>';
}
function pintaES(){
  var k = +$("es-n").value, a = Math.floor(Math.sqrt(k) + 1e-9), exacto = a * a === k, r = Math.sqrt(k);
  $("es-nv").textContent = k;
  var lo = exacto ? Math.max(0, a - 1) : a, hi = a + 1;
  $("es-svg").innerHTML = rectaRaiz(lo, hi, r, k, F(TXT.vozES, { n: k, d: exacto ? F(TXT.exactamenteEn, { a: a }) : F(TXT.entreY, { a: a, b: a + 1 }) }));
  var h;
  if (exacto) h = '<div class="linea veredicto">' + F(TXT.exacto, { n: k, r: rz(k), a: a }) + '</div>';
  else {
    var x = k - a * a, y = (a + 1) * (a + 1) - k;
    h = '<div class="linea">' + F(TXT.entre, { a2: a * a, n: k, b2: (a + 1) * (a + 1), a: a, r: rz(k), b: a + 1 }) + '</div><div class="linea">' +
      F(TXT.cerca, { n: k, x: x, a2: a * a, y: y, b2: (a + 1) * (a + 1), c: x < y ? a : (x > y ? a + 1 : F(TXT.igualDist, { a: a, b: a + 1 })), r: rz(k), v: aprox1(r) }) + '</div>';
  }
  $("es-salida").innerHTML = h;
}
function genEstimar(){
  var k; do { k = aleatorio(5, 224); } while (esCuadrado(k));
  var a = Math.floor(Math.sqrt(k)), a2 = a * a, b2 = (a + 1) * (a + 1);
  if (Math.random() < 0.65){
    var o = [a - 1, a, a + 1].filter(function(x){ return x >= 1; }).map(function(x){ return { html: F(TXT.entreOp, { a: x, b: x + 1 }), clave: "e" + x }; });
    if (o.length < 3) o.push({ html: F(TXT.entreOp, { a: a + 2, b: a + 3 }), clave: "e" + (a + 2) });
    return { enun: F(TXT.entreQ, { r: rz(k) }), opciones: o, enOrden: true, correcta: "e" + a, pista: F(TXT.pistaEntre, { n: k }), bien: F(TXT.bienEntre, { a2: a2, n: k, b2: b2 }), mal: F(TXT.malEntre, { a2: a2, b2: b2, a: a, b: a + 1 }) };
  }
  var x = k - a2, y = b2 - k; if (x === y) return genEstimar();
  var exp = F(TXT.bienCerca, { n: k, x: x, a2: a2, y: y, b2: b2, r: rz(k), v: aprox1(Math.sqrt(k)) });
  return { enun: F(TXT.cercaQ, { r: rz(k), a: a, b: a + 1 }), enOrden: true, opciones: [{ html: F(TXT.masCerca, { k: a }), clave: "a" }, { html: F(TXT.masCerca, { k: a + 1 }), clave: "b" }, { html: TXT.medio, clave: "m" }],
    correcta: x < y ? "a" : "b", pista: F(TXT.pistaCerca, { n: k, a2: a2, b2: b2 }), bien: exp, mal: exp };
}

/* ============ MODULE 4 · checking ============ */
function genVerifica(){
  var s = aleatorio(4, 15), ok = Math.random() < 0.5, k = ok ? s : s + elige([-1, 1, 2]), c = k * k, n = s * s;
  var exp = ok ? F(TXT.verifBien, { k: k, c: c, n: n }) : F(TXT.verifMal, { k: k, c: c, n: n, s: s });
  return { enun: F(TXT.verifQ, { r: rz(n), k: k }), enOrden: true, opciones: [{ html: TXT.si, clave: "s" }, { html: TXT.no, clave: "n" }, { html: TXT.calc, clave: "c" }],
    correcta: ok ? "s" : "n", pistas: { c: F(TXT.pistaCalc, { k: k }) }, pista: F(TXT.pistaCalc, { k: k }), bien: exp, mal: exp };
}
function genInversa(){
  var tipo = aleatorio(1, 3), k = aleatorio(4, 15);
  if (tipo === 1) return { enun: F(TXT.xEs, { r: rz("x"), n: k }), opciones: [k * k, 2 * k, k, k * k + 1].map(function(v, i){ return { html: String(v), clave: "v" + i }; }), correcta: "v0", pista: TXT.pistaX, bien: F(TXT.bienX, { n: k, c: k * k }), mal: F(TXT.bienX, { n: k, c: k * k }) };
  if (tipo === 2){ var A = k * k, o = [{ html: k + " " + TXT.pulg, clave: "a" }, { html: com(A / 2) + " " + TXT.pulg, clave: "b" }, { html: com(A / 4) + " " + TXT.pulg, clave: "c" }];
    return { enun: F(TXT.areaQ, { a: A }), opciones: o, correcta: "a", pista: TXT.pistaArea, bien: F(TXT.bienArea, { r: rz(A), n: k }), mal: F(TXT.malArea, { n: k, a: A }) }; }
  var mm; do { mm = aleatorio(20, 200); } while (esCuadrado(mm));
  var s1 = aleatorio(4, 13), s2 = s1 + 1;
  return { enun: TXT.noEntQ, opciones: [{ html: rz(mm), clave: "m" }, { html: rz(s1 * s1), clave: "a" }, { html: rz(s2 * s2), clave: "b" }], correcta: "m", pista: TXT.pistaNoEnt,
    bien: F(TXT.bienNoEnt, { m: mm, a: s1 * s1, b: s2 * s2 }), mal: F(TXT.bienNoEnt, { m: mm, a: s1 * s1, b: s2 * s2 }) };
}

/* ============ Start ============ */
$("iv-n").addEventListener("input", pintaIV); pintaIV();
creaPracticaLibre("p1", genRaiz);
(function(){ var sel = $("lc-a"), h = ""; for (var k = 2; k <= 12; k++) h += '<option value="' + k * k + '"' + (k === 6 ? " selected" : "") + '>' + k * k + '</option>'; sel.innerHTML = h; sel.addEventListener("change", pintaLC); pintaLC(); })();
creaPracticaLibre("p2", genLado);
$("es-n").addEventListener("input", pintaES); pintaES();
creaPracticaOM("p3", genEstimar);
creaPracticaOM("p4", genVerifica);
creaPracticaOM("p5", genInversa);
'''

def libre_n(pid, titulo, etiqueta=None):
    """Respuesta escrita de un número positivo."""
    return B.libre_e(pid, titulo, etiqueta).replace(t("Type an integer. If it is negative, start with the minus sign: −7 or -7.", "Escriba un número entero. Si es negativo, empiece con el signo menos: −7 o -7."), t("Type only the number.", "Escriba solo el número."))

def practica_pagina():
    n = N
    mods = [
     (t("inverse", "inversa"), t("The root as the inverse operation", "La raíz como operación inversa"),
      f'''      <p>{t("The square root answers the question: <strong>\"What number times itself gives this number?\"</strong> Squaring and taking the square root are inverse operations: one undoes the other. So the table of squares, read backward, is the table of roots.", "La raíz cuadrada responde a la pregunta: <strong>«¿qué número, multiplicado por sí mismo, da este número?»</strong>. Elevar al cuadrado y sacar la raíz son operaciones inversas: una deshace a la otra. Por eso la tabla de cuadrados, leída al revés, es la tabla de raíces.")}</p>
      <div class="formula">7<sup>2</sup> = 49 &nbsp;⟷&nbsp; √49 = 7</div>
      <h3>{t("There and back", "Ida y vuelta")}</h3>
      <div class="panel">
        <div class="campos"><div class="campo" style="flex:1;min-width:200px;"><label for="iv-n">{t("Number", "Número")}: <span id="iv-nv"></span></label><input type="range" id="iv-n" min="1" max="15" value="7"></div></div>
        <div class="salida" id="iv-salida" aria-live="polite"></div>
      </div>
{libre_n("p1", t("Practice: exact roots", "Practique: raíces exactas"))}'''),
     (t("side-of-square", "lado-cuadrado"), t("The root as the side of a square", "La raíz como lado de un cuadrado"),
      f'''      <p>{t("The area of a square is its side squared. So, if you know the area, <strong>the square root of the area is the side</strong>. A square of 36 small squares has 6 on each side.", "El área de un cuadrado es su lado al cuadrado. Por eso, si se conoce el área, <strong>la raíz del área es el lado</strong>. Un cuadrado de 36 cuadritos tiene 6 por lado.")}</p>
      <h3>{t("From the area to the side", "Del área al lado")}</h3>
      <div class="panel">
        <div class="campos"><div class="campo"><label for="lc-a">{t("Area of the square (square units)", "Área del cuadrado (unidades cuadradas)")}</label><select id="lc-a"></select></div></div>
        <div id="lc-svg"></div>
        <div class="salida" id="lc-salida" aria-live="polite"></div>
      </div>
{libre_n("p2", t("Practice: find the side", "Practique: hallar el lado"), t("Side", "Lado"))}'''),
     (t("estimate", "estimar"), t("Estimating roots that are not exact", "Estimar raíces no exactas"),
      f'''      <p>{t("If the number is not a perfect square, its root is not a whole number, but you can <strong>trap</strong> it between two perfect squares next to each other: since 49 &lt; 50 &lt; 64, √50 is between 7 and 8, and closer to 7.", "Si el número no es un cuadrado perfecto, su raíz no es entera, pero se puede <strong>acorralar</strong> entre dos cuadrados perfectos consecutivos: como 49 &lt; 50 &lt; 64, √50 está entre 7 y 8, y más cerca de 7.")}</p>
      <h3>{t("Trap the root", "Acorrale la raíz")}</h3>
      <div class="panel">
        <div class="campos"><div class="campo" style="flex:1;min-width:200px;"><label for="es-n">{t("Number", "Número")}: <span id="es-nv"></span></label><input type="range" id="es-n" min="2" max="224" value="50"></div></div>
        <div id="es-svg"></div>
        <div class="salida" id="es-salida" aria-live="polite"></div>
      </div>
{B.om("p3", t("Practice: between which whole numbers?", "Practique: ¿entre qué enteros está?"))}'''),
     (t("check", "verificar"), t("Checking by squaring", "Verificar elevando al cuadrado"),
      f'''      <p>{t("Every root can be checked with the inverse operation: if √144 = 12, then 12 × 12 must be 144. That way you catch a mistake without a calculator. The TI-30XS is a backup, but knowing the squares by heart is faster on the test.", "Toda raíz se comprueba con la operación inversa: si √144 = 12, entonces 12 × 12 tiene que dar 144. Así se detecta un error sin calculadora. La TI-30XS sirve de respaldo, pero conocer los cuadrados de memoria es más rápido en el examen.")}</p>
{B.om("p4", t("Practice: is it right?", "Practique: ¿es correcto?"))}
{B.om("p5", t("Practice: the inverse operation", "Practique: la operación inversa"))}''')]
    js = "var TXT = " + json.dumps(TX[B.L], ensure_ascii=False, indent=1) + ";\n" + LOGICA
    return B.pagina_practica(n, 2, t(*TEMA), t(*TIT),
        t("Four practice activities on one page. The exercises change every time. If you make a mistake, you get a hint and another try.", "Cuatro actividades de práctica en una sola página. Los ejercicios cambian cada vez. Si se equivoca, recibe una pista y otra oportunidad."),
        mods, js, scripts=("/math/integers.js",))

if __name__ == "__main__":
    B.construye(N, leccion, practica_pagina, "Raíces cuadradas de cuadrados perfectos")
