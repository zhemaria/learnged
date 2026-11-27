"""LearnGED · Estudios sociales · Lección 7.1 · Oferta, demanda, mercados y el consumidor (EN/ES).
Fuente: sociales/soc-7-1.html (incluido el interactivo «¿Qué curva se mueve?»).
Uso: python3 tools/build_soc_7_1.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sociales import C, t, documento, cita

N = "7-1"
F = 'font-family="Segoe UI, Arial, sans-serif"'


def titulo():
    return t("Supply, demand, markets, and the consumer", "Oferta, demanda, mercados y el consumidor")


def svg_oyd(desplaza=False):
    """Oferta (azul, sube) y demanda (roja, baja). Equilibrio en $5 y 50 unidades.
    desplaza=True añade la demanda desplazada a la derecha (D2) y el nuevo equilibrio."""
    X = lambda q: 70 + q * 5.2      # cantidad 0..100 → 70..590
    Y = lambda p: 300 - p * 26      # precio 0..10 → 300..40
    if desplaza:
        aria = t("Supply and demand graph. The demand curve D shifts to the right, to D2. The equilibrium moves from $5 and 50 units to about $6 and 60 units: price and quantity both rise.",
                 "Gráfica de oferta y demanda. La curva de demanda D se desplaza a la derecha, a D2. El equilibrio pasa de $5 y 50 unidades a unos $6 y 60 unidades: suben el precio y la cantidad.")
    else:
        aria = t("Supply and demand graph. The demand curve slopes down from left to right and the supply curve slopes up. They cross at the equilibrium: a price of $5 and a quantity of 50 units. Above that price there is a surplus; below it, a shortage.",
                 "Gráfica de oferta y demanda. La curva de demanda baja de izquierda a derecha y la de oferta sube. Se cruzan en el equilibrio: un precio de $5 y una cantidad de 50 unidades. Por encima de ese precio sobra producto; por debajo, falta.")
    s = [f'<svg class="diagrama" style="max-width:640px" viewBox="0 0 640 360" role="img" aria-label="{aria}" xmlns="http://www.w3.org/2000/svg">',
         f'<line x1="70" y1="300" x2="610" y2="300" stroke="#3d4753" stroke-width="2"/><line x1="70" y1="300" x2="70" y2="25" stroke="#3d4753" stroke-width="2"/>',
         f'<text x="600" y="330" text-anchor="end" {F} font-size="14" font-weight="700" fill="#1a2330">{t("Quantity", "Cantidad")}</text>',
         f'<text x="26" y="165" text-anchor="middle" transform="rotate(-90 26 165)" {F} font-size="14" font-weight="700" fill="#1a2330">{t("Price", "Precio")}</text>',
         # demanda: p = 10 - q/10 ; oferta: p = q/10
         f'<line x1="{X(5)}" y1="{Y(9.5)}" x2="{X(95)}" y2="{Y(0.5)}" stroke="#c62828" stroke-width="4"/>',
         f'<line x1="{X(5)}" y1="{Y(0.5)}" x2="{X(95)}" y2="{Y(9.5)}" stroke="#1565c0" stroke-width="4"/>',
         f'<text x="{X(97)}" y="{Y(0.5) + 5}" {F} font-size="16" font-weight="700" fill="#c62828">D</text>',
         f'<text x="{X(97)}" y="{Y(9.5) + 5}" {F} font-size="16" font-weight="700" fill="#1565c0">{t("S", "O")}</text>',
         f'<line x1="70" y1="{Y(5)}" x2="{X(50)}" y2="{Y(5)}" stroke="#555" stroke-dasharray="5 4"/><line x1="{X(50)}" y1="{Y(5)}" x2="{X(50)}" y2="300" stroke="#555" stroke-dasharray="5 4"/>',
         f'<circle cx="{X(50)}" cy="{Y(5)}" r="7" fill="#1a2330"/>',
         f'<text x="62" y="{Y(5) + 5}" text-anchor="end" {F} font-size="14" font-weight="700" fill="#1a2330">$5</text>',
         f'<text x="{X(50)}" y="318" text-anchor="middle" {F} font-size="14" font-weight="700" fill="#1a2330">50</text>']
    if desplaza:
        # D2: p = 12 - q/10 ; nuevo equilibrio q=60, p=6
        s += [f'<line x1="{X(25)}" y1="{Y(9.5)}" x2="{X(100)}" y2="{Y(2)}" stroke="#c62828" stroke-width="4" stroke-dasharray="9 6"/>',
              f'<text x="{X(25) - 8}" y="{Y(9.5) + 5}" text-anchor="end" {F} font-size="16" font-weight="700" fill="#c62828">D2</text>',
              f'<line x1="70" y1="{Y(6)}" x2="{X(60)}" y2="{Y(6)}" stroke="#555" stroke-dasharray="5 4"/><line x1="{X(60)}" y1="{Y(6)}" x2="{X(60)}" y2="300" stroke="#555" stroke-dasharray="5 4"/>',
              f'<circle cx="{X(60)}" cy="{Y(6)}" r="7" fill="#9c3d1c"/>',
              f'<text x="62" y="{Y(6) + 5}" text-anchor="end" {F} font-size="14" font-weight="700" fill="#9c3d1c">$6</text>',
              f'<text x="{X(60)}" y="318" text-anchor="middle" {F} font-size="14" font-weight="700" fill="#9c3d1c">60</text>',
              f'<path d="M {X(33)} {Y(7)} L {X(46)} {Y(7)}" stroke="#9c3d1c" stroke-width="2.5" marker-end="url(#fl71)"/>',
              '<defs><marker id="fl71" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#9c3d1c"/></marker></defs>']
    else:
        s += [f'<text x="{X(50)}" y="{Y(10)}" text-anchor="middle" {F} font-size="13.5" fill="#1a2330">{t("Above $5: surplus (sellers lower the price)", "Por encima de $5: sobra producto (bajan el precio)")}</text>',
              f'<text x="{X(50)}" y="{Y(1.0)}" text-anchor="middle" {F} font-size="13.5" fill="#1a2330">{t("Below $5: shortage (buyers bid the price up)", "Por debajo de $5: falta producto (suben el precio)")}</text>',
              f'<text x="{X(50)}" y="{Y(3.4)}" text-anchor="middle" {F} font-size="13.5" font-weight="700" fill="#1a2330" stroke="#fff" stroke-width="5" paint-order="stroke">{t("Equilibrium", "Equilibrio")}</text>']
    s.append("</svg>")
    return "".join(s)


def leccion():
    P = C.Practicas()
    s1 = f"""<p>{t("All of economics comes from one fact: <strong>resources are scarce and wants are not</strong>. Scarce does not mean rare, expensive, or small. It means there is not enough for every possible use at the same time. There is a lot of drinking water in the world, and it is still scarce, because it is not where it is needed and moving it costs money. The test takes one line: if using something for one thing prevents using it for another, it is scarce.", "Toda la economía sale de un solo hecho: <strong>los recursos son escasos y las necesidades no</strong>. Escaso no significa raro, ni caro, ni poco. Significa que no hay suficiente para todos los usos posibles a la vez. Hay muchísima agua potable en el mundo y sigue siendo escasa, porque no está donde se necesita y llevarla cuesta dinero. La prueba cabe en una línea: si usar algo para una cosa impide usarlo para otra, es escaso.")}</p>
<p>{t("From there, with no step in between, comes the concept asked most in this block. <strong>Opportunity cost</strong> is the value of the best alternative you give up. It is not what you pay: it is what you stop doing.", "De ahí sale, sin ningún paso intermedio, el concepto que más se pregunta de este bloque. El <strong>costo de oportunidad</strong> es el valor de la mejor alternativa a la que se renuncia. No es lo que se paga: es lo que se deja de hacer.")}</p>
{C.ejemplo(t("A course, counted completely", "Un curso, contado entero"), [
   ("1", t("What you pay: tuition of $600. It appears on the receipt.", "Lo que se paga: una matrícula de $600. Sale en el recibo.")),
   ("2", t("What you stop doing: 10 hours a week of study that could have been worked at $18 an hour. It appears nowhere.", "Lo que se deja de hacer: 10 horas semanales de estudio que se habrían podido trabajar a $18 la hora. No sale en ningún sitio.")),
   ("3", t("The opportunity cost: the $600 plus what you would have earned in those hours ($180 a week). That is what the test asks.", "El costo de oportunidad: los $600 más lo que se habría ganado en esas horas ($180 a la semana). Es lo que pregunta el examen."))])}
{C.caja("tip", t("Two rules to take away", "Las dos reglas que hay que llevarse"), "<p>" + t("First: look for <strong>one</strong> alternative, the best of the ones given up. Do not add up every option you passed on, only the one you would have chosen if the first did not exist. Second: the opportunity cost <strong>can be time, not money</strong>, and a decision that costs nothing on the receipt can have a huge opportunity cost.", "Primera: se busca <strong>una sola</strong> alternativa, la mejor de las descartadas. No se suman todas las opciones a las que se renunció, solo la que se habría elegido si la primera no existiera. Segunda: el costo de oportunidad <strong>puede ser tiempo y no dinero</strong>, y una decisión que no cuesta nada en el recibo puede tener un costo de oportunidad enorme.") + "</p>")}
{C.caja("ojo", t("The test mistake", "El error de examen"), "<p>" + t("“I spent Saturday studying. It cost me nothing.” It did: the eight-hour shift you did not work, or the day with your family. Free does not mean it costs nothing. If your answer to an opportunity-cost question is “zero,” you almost certainly looked at the price instead of the alternative.", "«Dediqué el sábado a estudiar. No me costó nada.» Sí costó: el turno de ocho horas que no trabajó, o el día con su familia. Que algo sea gratis no significa que no cueste. Si su respuesta a una pregunta de costo de oportunidad es «cero», casi seguro que miró el precio en vez de la alternativa.") + "</p>")}
{P(t("Practice 1 · Opportunity cost", "Práctica 1 · Costo de oportunidad"), t("Ana spends Saturday studying instead of working an eight-hour shift at $18 an hour. What is the opportunity cost of studying?", "Ana dedica el sábado a estudiar en vez de trabajar un turno de ocho horas a $18 la hora. ¿Cuál es el costo de oportunidad de estudiar?"),
   ["$144", "$0", "$18"], 0,
   {1: t("Studying is free, but it is not costless.", "Estudiar es gratis, pero no sale gratis."), 2: t("That is one hour; she gave up eight.", "Eso es una hora; renunció a ocho.")}, t("8 × $18 = $144, the wages she gave up.", "8 × $18 = $144, el sueldo al que renunció."))}"""

    s2 = f"""<p>{t("If resources are scarce, they have to be shared out. In a market economy, the <strong>price</strong> does that, and the price comes from where two curves cross.", "Si los recursos son escasos, hay que repartirlos. En una economía de mercado eso lo hace el <strong>precio</strong>, y el precio sale del cruce de dos curvas.")}</p>
{C.tabla(t("The two curves", "Las dos curvas"), ["", t("Demand · what buyers want", "Demanda · lo que quieren los compradores"), t("Supply · what sellers want", "Oferta · lo que quieren los vendedores")],
  [[t("The rule", "La regla"), t("The higher the price, the less they want to buy.", "Cuanto más alto el precio, menos quieren comprar."), t("The higher the price, the more they want to sell.", "Cuanto más alto el precio, más quieren vender.")],
   [t("The shape", "La forma"), t("It slopes down from left to right (red in this lesson).", "Baja de izquierda a derecha (en rojo en esta lección)."), t("It slopes up from left to right (blue in this lesson).", "Sube de izquierda a derecha (en azul en esta lección).")]])}
<p>{t("Where they cross is the <strong>equilibrium</strong>: the only price at which the quantity people want to buy is exactly the quantity people want to sell. Nothing left over, nothing missing. (The numbers below are chosen so the arithmetic is easy.)", "Donde se cruzan está el <strong>equilibrio</strong>: el único precio al que la cantidad que se quiere comprar es exactamente la que se quiere vender. Ni sobra ni falta. (Los números de abajo están elegidos para que las cuentas salgan fáciles).")}</p>
{svg_oyd()}
<p>{t("Above the equilibrium price there is a surplus, and sellers lower the price. Below it there is a shortage, and buyers compete and push the price up. That is why the market tends toward the crossing.", "Por encima del precio de equilibrio sobra producto y los vendedores bajan el precio. Por debajo falta, y los compradores compiten y lo suben. Por eso el mercado tiende a ese cruce.")}</p>
<h3>{t("The distinction asked most", "La distinción que más se pregunta")}</h3>
{C.tabla(t("A change in demand versus a change in quantity demanded", "Un cambio en la demanda frente a un cambio en la cantidad demandada"), [t("What is said", "Se dice"), t("What happens on the graph", "Qué pasa en la gráfica"), t("What causes it", "Qué lo provoca")],
  [[t("Demand changes", "Cambia la demanda"), t("The whole curve shifts right or left.", "La curva entera se desplaza a la derecha o a la izquierda."), t("Something other than the price: a fashion, more income, a cheaper substitute.", "Algo distinto del precio: una moda, más ingreso, un sustituto más barato.")],
   [t("Quantity demanded changes", "Cambia la cantidad demandada"), t("The curve does not move: you slide along it.", "La curva no se mueve: usted se desplaza a lo largo de ella."), t("The price, and only the price.", "El precio, y solo el precio.")]])}
{C.caja("ojo", t("Why “the price went up, so demand went down” is wrong", "Por qué «subió el precio, así que bajó la demanda» está mal dicho"), "<p>" + t("What went down was the <strong>quantity demanded</strong>. The demand curve stays exactly where it was. And the difference matters: if the curve itself had moved, the equilibrium price would have changed too.", "Lo que bajó fue la <strong>cantidad demandada</strong>. La curva de demanda sigue exactamente donde estaba. Y la diferencia importa: si se hubiera movido la curva, el precio de equilibrio también habría cambiado.") + "</p>")}"""

    s3 = f"""<p>{t("Only four things can happen, and they all fit in this table. It is worth learning, because with it you can solve any question of this kind.", "Solo pueden pasar cuatro cosas, y todas caben en esta tabla. Vale la pena aprendérsela, porque con ella se resuelve cualquier pregunta de este tipo.")}</p>
{C.tabla(t("The four possible shifts and their effect on the equilibrium", "Los cuatro desplazamientos posibles y su efecto sobre el equilibrio"), [t("What happens", "Qué ocurre"), t("Curve that moves", "Curva que se mueve"), t("Price", "Precio"), t("Quantity", "Cantidad")],
  [[t("Demand rises", "Sube la demanda"), t("Demand → right", "Demanda → derecha"), t("↑ Rises", "↑ Sube"), t("↑ Rises", "↑ Sube")],
   [t("Demand falls", "Baja la demanda"), t("Demand → left", "Demanda → izquierda"), t("↓ Falls", "↓ Baja"), t("↓ Falls", "↓ Baja")],
   [t("Supply rises", "Sube la oferta"), t("Supply → right", "Oferta → derecha"), t("↓ Falls", "↓ Baja"), t("↑ Rises", "↑ Sube")],
   [t("Supply falls", "Baja la oferta"), t("Supply → left", "Oferta → izquierda"), t("↑ Rises", "↑ Sube"), t("↓ Falls", "↓ Baja")]])}
{svg_oyd(desplaza=True)}
<p>{t("Here demand shifted right (more buyers, or a fashion): price and quantity both went up, from $5 and 50 to $6 and 60.", "Aquí la demanda se desplazó a la derecha (más compradores, o una moda): subieron el precio y la cantidad, de $5 y 50 a $6 y 60.")}</p>
{C.caja("tip", t("The trick so you don’t memorize four rows", "El truco para no memorizar cuatro filas"), "<p>" + t("When <strong>demand</strong> moves, price and quantity change in the <strong>same direction</strong>. When <strong>supply</strong> moves, they change in <strong>opposite directions</strong>. And one question before moving anything: does the event affect the <strong>buyer</strong> or the <strong>seller</strong>? A drought, a new machine, a tax on production, or the price of fuel touch the seller: they move supply. A fashion, a higher income, a health warning, or the price of a substitute touch the buyer: they move demand. Almost every mistake in this block comes from skipping that question.", "Cuando se mueve la <strong>demanda</strong>, el precio y la cantidad cambian en la <strong>misma dirección</strong>. Cuando se mueve la <strong>oferta</strong>, cambian en <strong>direcciones opuestas</strong>. Y una pregunta antes de mover nada: ¿el suceso afecta al <strong>comprador</strong> o al <strong>vendedor</strong>? Una sequía, una máquina nueva, un impuesto a la producción o el precio del combustible tocan al vendedor: mueven la oferta. Una moda, un sueldo mayor, un aviso de salud o el precio de un sustituto tocan al comprador: mueven la demanda. Casi todos los fallos de este bloque vienen de saltarse esa pregunta.") + "</p>")}
{P(t("Practice 2 · Which curve?", "Práctica 2 · ¿Qué curva?"), t("A frost destroys the orange crop. What happens to the price and quantity of oranges?", "Una helada destruye la cosecha de naranjas. ¿Qué pasa con el precio y la cantidad de naranjas?"),
   [t("Price rises, quantity falls", "El precio sube y la cantidad baja"), t("Both rise", "Los dos suben"), t("Both fall", "Los dos bajan")], 0,
   {1: t("The frost affects sellers: supply, opposite directions.", "La helada afecta al vendedor: oferta, direcciones opuestas."), 2: t("Supply moved, so they go in opposite directions.", "Se movió la oferta, así que van en direcciones opuestas.")}, t("Supply shifts left: price up, quantity down.", "La oferta se desplaza a la izquierda: precio arriba, cantidad abajo."))}
{C.enlace(N, t("which-curve", "que-curva"), t("Which curve moves?", "¿Qué curva se mueve?"), t("Eight events: what happens to the equilibrium price and quantity?", "Ocho sucesos: ¿qué les pasa al precio y a la cantidad de equilibrio?"))}"""

    s4 = f"""<p>{t("So far, markets. Now the part you use the same day you leave class. A washing machine costs $600. Look at what each way of paying costs <strong>in total</strong>.", "Hasta aquí, mercados. Ahora la parte que se usa el mismo día en que se sale de clase. Una lavadora cuesta $600. Vea lo que cuesta cada manera de pagarla <strong>en total</strong>.")}</p>
{C.tabla(t("The total cost of the same $600 purchase, by way of paying (rounded for teaching)", "Costo total de una misma compra de $600 según la forma de pago (cifras redondeadas con fines didácticos)"), [t("Way of paying", "Forma de pago"), t("How it works", "Cómo funciona"), t("What you end up paying", "Lo que acaba pagando")],
  [[t("Cash", "Al contado"), t("Pay $600 today.", "Paga los $600 hoy."), t("$600. But you no longer have that $600 for anything else: that is its opportunity cost.", "$600. Pero se queda sin esos $600 para cualquier otra cosa: ese es su costo de oportunidad.")],
   [t("Installments", "A plazos"), t("24 payments of $32 a month.", "24 cuotas de $32 al mes."), t("$768: $168 in interest, 28% more than the price tag.", "$768: $168 de interés, un 28 % más que el precio de la etiqueta.")],
   [t("Credit card, paying the minimum", "Con tarjeta, pagando el mínimo"), t("A card at 24% a year, paying about the minimum each month.", "Tarjeta al 24 % anual, pagando cerca del mínimo cada mes."), t("Quite a bit more than $768, and the figure grows the longer it takes, because interest is charged every month on what is still owed.", "Bastante más de $768, y la cifra crece cuanto más se tarde, porque el interés se cobra cada mes sobre lo que queda por pagar.")]])}
{C.ejemplo(t("The calculation", "La cuenta"), [("1", t("Multiply the payment by the number of payments: 32 × 24 = 768.", "Multiplique la cuota por el número de cuotas: 32 × 24 = 768.")), ("2", t("Subtract the cash price: 768 − 600 = 168. That is what the credit costs.", "Réstele el precio al contado: 768 − 600 = 168. Eso es lo que cuesta el crédito.")), ("3", t("As a percent: 168 ÷ 600 × 100 = 28%.", "En porcentaje: 168 ÷ 600 × 100 = 28 %."))],
   t("None of the three options is “the right one.” Cash costs less money and leaves less on hand; the other two buy time in exchange for interest, and sometimes that is worth it. What is always a mistake is not doing the math.", "Ninguna de las tres opciones es «la correcta». Al contado cuesta menos dinero y deja menos en la mano; las otras dos compran tiempo a cambio de interés, y a veces eso vale la pena. Lo que sí es siempre un error es no hacer la cuenta."))}
<h3>{t("And inflation, which charges you without being noticed", "Y la inflación, que cobra sin que se note")}</h3>
<p>{t("<strong>Inflation</strong> is a general, sustained rise in prices. Its practical effect is that the same money buys less every year. It is measured with the cost of a basket of typical purchases (example figures):", "La <strong>inflación</strong> es el aumento general y sostenido de los precios. Su efecto práctico es que el mismo dinero compra menos cada año. Se mide con el costo de una canasta de compras típicas (cifras de ejemplo):")}</p>
{C.tabla(t("Inflation from the cost of the same basket", "La inflación a partir del costo de una misma canasta"), [t("Year", "Año"), t("Cost of the basket", "Costo de la canasta"), t("Inflation since the base year", "Inflación desde el año base")],
  [[t("Base year", "Año base"), "$850.00", "0.0%"], [t("One year later", "Un año después"), "$875.00", "(875 − 850) ÷ 850 × 100 = 2.9%"], [t("Two years later", "Dos años después"), "$891.00", "(891 − 850) ÷ 850 × 100 = 4.8%"]])}
{C.caja("tip", t("Two things the test does ask about inflation", "Dos cosas que el examen sí pregunta sobre la inflación"), "<p>" + t("First: not all prices rise the same. Inside the basket some items rise, some fall, and the total can rise anyway. Second: it hurts most those with a <strong>fixed income</strong>, like a retiree, because their money loses value with no raise. For someone with a <strong>fixed-rate debt</strong>, on the other hand, inflation makes the debt cheaper.", "Primera: no todos los precios suben igual. Dentro de la canasta unos artículos suben, otros bajan, y el total puede subir de todas formas. Segunda: castiga más a quien tiene un <strong>ingreso fijo</strong>, como un jubilado, porque su dinero pierde valor sin que nadie le suba nada. A quien tiene una <strong>deuda a tasa fija</strong>, en cambio, la inflación se la abarata.") + "</p>")}
{P(t("Practice 3 · Credit", "Práctica 3 · Crédito"), t("A TV costs $400 cash, or 12 payments of $40. How much does the credit cost?", "Un televisor cuesta $400 al contado, o 12 cuotas de $40. ¿Cuánto cuesta el crédito?"),
   ["$80", "$480", "$40"], 0,
   {1: t("That is the total paid; subtract the cash price.", "Ese es el total pagado; réstele el precio al contado."), 2: t("That is one payment.", "Esa es una cuota.")}, t("12 × 40 = 480; 480 − 400 = 80.", "12 × 40 = 480; 480 − 400 = 80."))}
{C.enlace(N, t("credit", "credito"), t("What does the credit really cost?", "¿Cuánto cuesta de verdad el crédito?"), t("New numbers every time.", "Números nuevos cada vez."))}
{C.enlace(N, t("inflation", "inflacion"), t("Inflation from a basket", "La inflación a partir de una canasta"), t("New numbers every time.", "Números nuevos cada vez."))}"""

    G = lambda *a: C.ged_item(P, *a)
    sG = "<p>" + t("These questions work like the ones on the GED® Social Studies test. Each one shows the social studies practice it checks and its depth of knowledge (DOK). You may use the calculator.",
                   "Estas preguntas funcionan como las del examen de Estudios Sociales del GED®. Cada una indica la práctica de estudios sociales que evalúa y su profundidad de conocimiento (DOK). Puede usar la calculadora.") + f"""</p>
{G(1, "SSP.3.c", "2", t("<em>A popular doctor on television says that eating avocados is good for the heart.</em><br>What will most likely happen in the avocado market?", "<em>Un médico popular dice en la televisión que comer aguacate es bueno para el corazón.</em><br>¿Qué es más probable que ocurra en el mercado del aguacate?"),
   [t("Demand rises: price and quantity both rise.", "Sube la demanda: suben el precio y la cantidad."), t("Supply rises: price falls and quantity rises.", "Sube la oferta: baja el precio y sube la cantidad."), t("Demand falls: price and quantity both fall.", "Baja la demanda: bajan el precio y la cantidad."), t("Supply falls: price rises and quantity falls.", "Baja la oferta: sube el precio y baja la cantidad.")], 0,
   {1: t("The news affects buyers, not growers.", "La noticia afecta a los compradores, no a los productores."), 2: t("Good news raises demand.", "Una buena noticia sube la demanda."), 3: t("Growers did not change.", "Los productores no cambiaron.")},
   t("Buyer → demand → same direction.", "Comprador → demanda → misma dirección."))}
{G(2, "SSP.4.a", "2", t("<em>Luis chose to take an evening class instead of working overtime that would have paid $120.</em><br>In economics, the $120 is the class’s…", "<em>Luis eligió tomar una clase por la noche en vez de hacer horas extra que le habrían pagado $120.</em><br>En economía, los $120 son el… de la clase."),
   [t("opportunity cost", "costo de oportunidad"), t("tuition", "matrícula"), t("interest", "interés"), t("inflation", "inflación")], 0,
   {1: t("He did not pay it; he gave it up.", "No lo pagó; renunció a él."), 2: t("No loan is involved.", "No hay préstamo."), 3: t("No general rise in prices.", "No hay subida general de precios.")},
   t("The best alternative given up.", "La mejor alternativa a la que se renuncia."))}
{G(3, "SSP.10.a", "2", t("<em>A car costs $9,000 cash, or $300 a month for 36 months.</em><br>What percent more than the cash price does the installment plan cost?", "<em>Un auto cuesta $9,000 al contado, o $300 al mes durante 36 meses.</em><br>¿Qué porcentaje más que el precio al contado cuesta el plan a plazos?"),
   ["20%", "12%", "$1,800", "36%"], 0,
   {1: t("Recompute: 300 × 36 = 10,800.", "Rehaga: 300 × 36 = 10,800."), 2: t("That is the interest in dollars; divide by 9,000.", "Ese es el interés en dólares; divida entre 9,000."), 3: t("That is the number of months.", "Ese es el número de meses.")},
   t("300 × 36 = 10,800; 10,800 − 9,000 = 1,800; 1,800 ÷ 9,000 = 0.20 = 20%.", "300 × 36 = 10,800; 10,800 − 9,000 = 1,800; 1,800 ÷ 9,000 = 0.20 = 20 %."))}
{G(4, "SSP.3.c", "2–3", t("<em>The price of tea falls sharply, and many people drink tea instead of coffee.</em><br>What happens in the <strong>coffee</strong> market?", "<em>El precio del té baja mucho, y mucha gente toma té en vez de café.</em><br>¿Qué pasa en el mercado del <strong>café</strong>?"),
   [t("Demand for coffee falls: price and quantity fall.", "Baja la demanda de café: bajan el precio y la cantidad."), t("Supply of coffee falls: price rises.", "Baja la oferta de café: sube el precio."), t("Demand for coffee rises.", "Sube la demanda de café."), t("Nothing, because tea is a different market.", "Nada, porque el té es otro mercado.")], 0,
   {1: t("Coffee growers did not change.", "Los productores de café no cambiaron."), 2: t("A cheaper substitute pulls buyers away.", "Un sustituto más barato se lleva compradores."), 3: t("Substitutes connect markets.", "Los sustitutos conectan los mercados.")},
   t("A cheaper substitute shifts demand left.", "Un sustituto más barato desplaza la demanda a la izquierda."))}
{G(5, "SSP.10.a", "2", t("<em>A basket of groceries cost $200 last year and $210 this year.</em><br>What is the rate of inflation for this basket?", "<em>Una canasta de compras costaba $200 el año pasado y $210 este año.</em><br>¿Cuál es la tasa de inflación de esta canasta?"),
   ["5%", "10%", "$10", "4.8%"], 0,
   {1: t("That is $10 out of $100, not $200.", "Eso serían $10 de $100, no de $200."), 2: t("That is the change in dollars.", "Ese es el cambio en dólares."), 3: t("Divide by the old price, 200, not the new one.", "Divida entre el precio viejo, 200, no el nuevo.")},
   t("(210 − 200) ÷ 200 × 100 = 5%.", "(210 − 200) ÷ 200 × 100 = 5 %."))}"""

    secciones = [
        ("s1", t("There is not enough for everything", "No alcanza para todo"), s1),
        ("s2", t("Two curves and one crossing", "Dos curvas y un cruce"), s2),
        ("s3", t("What happens to the price?", "¿Qué le pasa al precio?"), s3),
        ("s4", t("What it really costs", "Lo que cuesta de verdad"), s4),
        ("s5", t("GED-style questions", "Preguntas tipo GED"), sG),
    ]
    tarea = [
        (t("Your opportunity cost (15 minutes).", "Su costo de oportunidad (15 minutos)."), t("Choose a decision you made this week and write its opportunity cost, in money or in time. <em>Check:</em> name one alternative, not a list.", "Elija una decisión que tomó esta semana y escriba su costo de oportunidad, en dinero o en tiempo. <em>Compruebe:</em> nombre una alternativa, no una lista.")),
        (t("Which curve? (20 minutes).", "¿Qué curva? (20 minutos)."), t("Find two news items about prices (gasoline, eggs, rent). For each, say whether buyers or sellers were affected, which curve moved, and what happened to price and quantity. <em>Check:</em> demand moves both in the same direction; supply in opposite directions.", "Busque dos noticias sobre precios (gasolina, huevos, alquiler). Para cada una, diga si afectó a compradores o vendedores, qué curva se movió y qué pasó con el precio y la cantidad. <em>Compruebe:</em> la demanda los mueve en la misma dirección; la oferta, en direcciones opuestas.")),
        (t("A real contract (20 minutes).", "Un contrato real (20 minutos)."), t("With a real financing offer or bill, compute the total paid, the interest in dollars, and the interest as a percent of the cash price. <em>Check:</em> payment × number of payments − cash price.", "Con una oferta de financiación o una factura reales, calcule el total pagado, el interés en dólares y el interés como porcentaje del precio al contado. <em>Compruebe:</em> cuota × número de cuotas − precio al contado.")),
    ]
    Q = t
    quiz = [
        (Q("“Scarce” in economics means…", "«Escaso» en economía significa…"), [Q("there is not enough for every possible use at once", "que no hay suficiente para todos los usos posibles a la vez"), Q("very rare", "muy raro"), Q("very expensive", "muy caro"), Q("not for sale", "que no está a la venta")], 0, {1: Q("Water is common and still scarce.", "El agua es común y sigue siendo escasa."), 2: Q("Price is a consequence, not the definition.", "El precio es una consecuencia, no la definición."), 3: Q("No.", "No.")}, Q("Using it for one thing prevents another.", "Usarlo para una cosa impide otra.")),
        (Q("Opportunity cost is…", "El costo de oportunidad es…"), [Q("the value of the best alternative given up", "el valor de la mejor alternativa a la que se renuncia"), Q("the price paid", "el precio pagado"), Q("the sum of all alternatives", "la suma de todas las alternativas"), Q("the interest on a loan", "el interés de un préstamo")], 0, {1: Q("Not only what you pay.", "No solo lo que se paga."), 2: Q("Only the best one.", "Solo la mejor."), 3: Q("No.", "No.")}, Q("What you stop doing.", "Lo que se deja de hacer.")),
        (Q("The demand curve slopes…", "La curva de demanda…"), [Q("down from left to right", "baja de izquierda a derecha"), Q("up from left to right", "sube de izquierda a derecha"), Q("flat", "es plana"), Q("straight up", "es vertical")], 0, {1: Q("That is supply.", "Esa es la oferta."), 2: Q("No.", "No."), 3: Q("No.", "No.")}, Q("Higher price, less bought.", "Precio más alto, menos compra.")),
        (Q("At the equilibrium price…", "Al precio de equilibrio…"), [Q("quantity demanded equals quantity supplied", "la cantidad demandada es igual a la ofrecida"), Q("there is a surplus", "sobra producto"), Q("there is a shortage", "falta producto"), Q("the price is zero", "el precio es cero")], 0, {1: Q("That is above it.", "Eso es por encima."), 2: Q("That is below it.", "Eso es por debajo."), 3: Q("No.", "No.")}, Q("Nothing left over, nothing missing.", "Ni sobra ni falta.")),
        (Q("The price of a product rises and people buy less of it. This is a change in…", "Sube el precio de un producto y la gente compra menos. Es un cambio en…"), [Q("quantity demanded", "la cantidad demandada"), Q("demand", "la demanda"), Q("supply", "la oferta"), Q("inflation", "la inflación")], 0, {1: Q("The curve did not move.", "La curva no se movió."), 2: Q("No.", "No."), 3: Q("No.", "No.")}, Q("A slide along the curve.", "Un deslizamiento por la curva.")),
        (Q("When demand rises, price and quantity…", "Cuando sube la demanda, el precio y la cantidad…"), [Q("both rise", "suben los dos"), Q("both fall", "bajan los dos"), Q("move in opposite directions", "van en direcciones opuestas"), Q("stay the same", "no cambian")], 0, {1: Q("That is demand falling.", "Eso es bajar la demanda."), 2: Q("That is a supply shift.", "Eso es un cambio de oferta."), 3: Q("No.", "No.")}, Q("Same direction.", "Misma dirección.")),
        (Q("A new machine lets a factory produce twice as much at the same cost. Which curve moves?", "Una máquina nueva permite a una fábrica producir el doble al mismo costo. ¿Qué curva se mueve?"), [Q("Supply, to the right", "La oferta, a la derecha"), Q("Demand, to the right", "La demanda, a la derecha"), Q("Supply, to the left", "La oferta, a la izquierda"), Q("Neither", "Ninguna")], 0, {1: Q("Buyers did not change.", "Los compradores no cambiaron."), 2: Q("It is easier to produce, not harder.", "Producir es más fácil, no más difícil."), 3: Q("No.", "No.")}, Q("Price down, quantity up.", "Precio abajo, cantidad arriba.")),
        (Q("Fuel for delivery trucks becomes much more expensive. For the goods they deliver, the price…", "El combustible de los camiones de reparto sube mucho. Para los productos que reparten, el precio…"), [Q("rises, because supply shifts left", "sube, porque la oferta se desplaza a la izquierda"), Q("falls, because demand falls", "baja, porque baja la demanda"), Q("does not change", "no cambia"), Q("rises, because demand rises", "sube, porque sube la demanda")], 0, {1: Q("It is a cost for sellers.", "Es un costo para el vendedor."), 2: Q("No.", "No."), 3: Q("Buyers did not change.", "Los compradores no cambiaron.")}, Q("A cost of production moves supply.", "Un costo de producción mueve la oferta.")),
        (Q("24 payments of $50 for a $1,000 item. How much is the interest?", "24 cuotas de $50 por un artículo de $1,000. ¿Cuánto es el interés?"), ["$200", "$1,200", "$50", "$24"], 0, {1: Q("That is the total paid.", "Ese es el total pagado."), 2: Q("One payment.", "Una cuota."), 3: Q("No.", "No.")}, Q("24 × 50 − 1,000 = 200.", "24 × 50 − 1,000 = 200.")),
        (Q("Inflation is…", "La inflación es…"), [Q("a general and sustained rise in prices", "el aumento general y sostenido de los precios"), Q("a rise in one price", "la subida de un precio"), Q("a drop in wages", "una bajada de los sueldos"), Q("the interest on a loan", "el interés de un préstamo")], 0, {1: Q("One price is not inflation.", "Un precio solo no es inflación."), 2: Q("No.", "No."), 3: Q("No.", "No.")}, Q("The same money buys less.", "El mismo dinero compra menos.")),
        (Q("Who is hurt most by inflation?", "¿A quién perjudica más la inflación?"), [Q("People on a fixed income", "A quien tiene un ingreso fijo"), Q("People with fixed-rate debts", "A quien tiene deudas a tasa fija"), Q("Sellers of goods", "A los vendedores"), Q("No one", "A nadie")], 0, {1: Q("Their debt gets cheaper.", "Su deuda se abarata."), 2: Q("Not necessarily.", "No necesariamente."), 3: Q("No.", "No.")}, Q("A retiree, for example.", "Un jubilado, por ejemplo.")),
        (Q("A basket goes from $500 to $520. Inflation is…", "Una canasta pasa de $500 a $520. La inflación es…"), ["4%", "20%", "2%", "$20"], 0, {1: Q("Divide by 500.", "Divida entre 500."), 2: Q("Recompute.", "Rehaga la cuenta."), 3: Q("That is dollars.", "Eso son dólares.")}, Q("20 ÷ 500 × 100 = 4%.", "20 ÷ 500 × 100 = 4 %.")),
    ]
    filas = [
        (t("Explain scarcity and opportunity cost", "Explica la escasez y el costo de oportunidad"), t("I compute the opportunity cost of a real decision, in money or time.", "Calculo el costo de oportunidad de una decisión real, en dinero o en tiempo."), t("I know the definition but add up every alternative.", "Sé la definición, pero sumo todas las alternativas."), t("I confuse it with the price (<a href=\"#s1\">review section 1</a>).", "Lo confundo con el precio (<a href=\"#s1\">repase la sección 1</a>).")),
        (t("Identify which curve shifts", "Identifica qué curva se desplaza"), t("I decide buyer or seller first, and the direction.", "Decido primero comprador o vendedor, y la dirección."), t("I get the obvious cases.", "Acierto en los casos obvios."), t("I mix up demand and quantity demanded (<a href=\"#s2\">review section 2</a>).", "Confundo demanda con cantidad demandada (<a href=\"#s2\">repase la sección 2</a>).")),
        (t("Predict the new equilibrium", "Predice el nuevo equilibrio"), t("I use the trick: demand same direction, supply opposite.", "Uso el truco: demanda, misma dirección; oferta, opuestas."), t("I look up the table each time.", "Miro la tabla cada vez."), t("I guess (<a href=\"#s3\">review section 3</a>).", "Adivino (<a href=\"#s3\">repase la sección 3</a>).")),
        (t("Compute the real cost of credit and inflation", "Calcula el costo real del crédito y la inflación"), t("I compute total, interest, and percent, and inflation from a basket.", "Calculo total, interés y porcentaje, y la inflación a partir de una canasta."), t("I compute the total but not the percent.", "Calculo el total, pero no el porcentaje."), t("I only look at the monthly payment (<a href=\"#s4\">review section 4</a>).", "Solo miro la cuota mensual (<a href=\"#s4\">repase la sección 4</a>).")),
    ]
    cierre = "<p>" + t("This lesson started where all of economics starts: there is not enough for everything, so every choice has an opportunity cost. Then the price, which comes from two curves, and the four ways it can move. And it ended with the calculations you will use at the store: the real cost of credit and of inflation. Lesson 7.2 moves from markets to people: how many there are, how old, where they live, and why they move.",
                         "Esta lección empezó donde empieza toda la economía: no alcanza para todo, así que cada elección tiene un costo de oportunidad. Después, el precio, que sale de dos curvas, y las cuatro maneras en que puede moverse. Y terminó con las cuentas que se usan en la tienda: lo que cuestan de verdad el crédito y la inflación. La Lección 7.2 pasa de los mercados a las personas: cuántas son, de qué edades, dónde viven y por qué se mueven.") + "</p>"
    glosario = [
        (t("Scarcity", "Escasez"), t("Not having enough resources for every possible use at the same time.", "No tener recursos suficientes para todos los usos posibles a la vez.")),
        (t("Opportunity cost", "Costo de oportunidad"), t("The value of the best alternative given up.", "El valor de la mejor alternativa a la que se renuncia.")),
        (t("Demand", "Demanda"), t("How much buyers want to buy at each price.", "Cuánto quieren comprar los compradores a cada precio.")),
        (t("Supply", "Oferta"), t("How much sellers want to sell at each price.", "Cuánto quieren vender los vendedores a cada precio.")),
        (t("Equilibrium", "Equilibrio"), t("The price at which quantity demanded equals quantity supplied.", "El precio al que la cantidad demandada es igual a la ofrecida.")),
        (t("Substitute", "Sustituto"), t("A product used in place of another (tea for coffee).", "Producto que se usa en lugar de otro (té en vez de café).")),
        (t("Interest", "Interés"), t("The price of borrowing money.", "El precio de pedir dinero prestado.")),
        (t("Inflation", "Inflación"), t("A general and sustained rise in prices.", "El aumento general y sostenido de los precios.")),
    ]
    estd = C.estandares(["SSP.3.c", "SSP.4.a", "SSP.6.b", "SSP.10.a"], ["E.c", "E.d", "E.f"], base=["SSP.6.c"])
    conexion = "<p>" + t("Topic 6 ended in the twentieth century. Topic 7 changes field: economics and geography, which together are 30% of the test. And it changes method: here there are fewer documents to interpret and more graphs to read and calculations to do. This lesson starts where all of economics starts: there is not enough for everything.",
                         "El Tema 6 terminó en el siglo XX. El Tema 7 cambia de campo: economía y geografía, que juntas son el 30 % del examen. Y cambia de método: aquí hay menos documentos que interpretar y más gráficas que leer y cuentas que hacer. Esta lección empieza donde empieza toda la economía: no alcanza para todo.") + "</p>"
    return C.pagina_leccion(N, titulo(),
        t("Every choice has a cost you don’t see on the receipt, and every price comes from two curves.", "Toda elección tiene un costo que no sale en el recibo, y todo precio sale de dos curvas."),
        ["SSP.3 · " + t("Cause and effect", "Causa y efecto"), "SSP.6 · " + t("Reading graphs", "Leer gráficas"), "SSP.10 · " + t("Calculations", "Cálculos")],
        [t("<strong>Explain</strong> scarcity and opportunity cost, and calculate the second in a real decision.", "<strong>Explicar</strong> la escasez y el costo de oportunidad, y calcular el segundo en una decisión concreta."),
         t("<strong>Identify</strong> which curve shifts after an event, and in which direction.", "<strong>Identificar</strong> qué curva se desplaza ante un suceso, y en qué dirección."),
         t("<strong>Predict</strong> the effect of that shift on the equilibrium price and quantity.", "<strong>Predecir</strong> el efecto de ese desplazamiento sobre el precio y la cantidad de equilibrio."),
         t("<strong>Calculate</strong> what a purchase on credit really costs, and the rate of inflation.", "<strong>Calcular</strong> lo que cuesta de verdad una compra a crédito, y la tasa de inflación.")],
        estd, conexion, secciones, tarea, quiz, filas, cierre,
        ("7-2", t("Population, migration, and human geography", "Población, migración y geografía humana")), glosario, P, calculadora=True)


# ---------------------------------------------------------------- la práctica
def banco_curvas():
    O = [t("Price ↑ and quantity ↑", "Precio ↑ y cantidad ↑"), t("Price ↓ and quantity ↓", "Precio ↓ y cantidad ↓"), t("Price ↑ and quantity ↓", "Precio ↑ y cantidad ↓"), t("Price ↓ and quantity ↑", "Precio ↓ y cantidad ↑")]
    D = [(t("A frost destroys the orange crop.", "Una helada destruye la cosecha de naranjas."), 2, t("It affects growers: supply shifts left. Supply moved: price and quantity go in opposite directions.", "Afecta al productor: la oferta se desplaza a la izquierda. Se movió la oferta: precio y cantidad en direcciones opuestas.")),
         (t("A sneaker becomes the fashion and everyone wants it.", "Una zapatilla se pone de moda y todo el mundo la quiere."), 0, t("It affects buyers: demand shifts right. Both rise.", "Afecta al comprador: la demanda se desplaza a la derecha. Suben los dos.")),
         (t("A recession arrives and families have less money.", "Llega una recesión y las familias tienen menos dinero."), 1, t("It affects buyers: demand shifts left. Both fall.", "Afecta al comprador: la demanda se desplaza a la izquierda. Bajan los dos.")),
         (t("A new factory can produce twice as much at the same cost.", "Una fábrica nueva puede producir el doble al mismo costo."), 3, t("It affects sellers: supply shifts right. Price down, quantity up.", "Afecta al vendedor: la oferta se desplaza a la derecha. Precio abajo, cantidad arriba.")),
         (t("The price of fuel for delivery trucks rises sharply.", "Sube mucho el precio del combustible de los camiones de reparto."), 2, t("A production cost: supply shifts left. Careful: it is a price, but of an input, not of the product.", "Un costo de producción: la oferta se desplaza a la izquierda. Ojo: es un precio, pero de un insumo, no del producto.")),
         (t("Tea becomes much cheaper, and many people drink it instead of coffee. What happens in the coffee market?", "El té baja mucho de precio y mucha gente lo toma en vez de café. ¿Qué pasa en el mercado del café?"), 1, t("A cheaper substitute affects coffee buyers: coffee demand shifts left. One of the most missed, because the event happens in another market.", "Un sustituto más barato afecta al comprador de café: la demanda de café se desplaza a la izquierda. De los que más se fallan, porque el suceso ocurre en otro mercado.")),
         (t("The government gives a subsidy to corn growers.", "El gobierno da una subvención a los productores de maíz."), 3, t("It makes producing cheaper: supply shifts right. Price down, quantity up.", "Abarata producir: la oferta se desplaza a la derecha. Precio abajo, cantidad arriba.")),
         (t("More people move to a city and the population grows. What happens in the housing market?", "Llega más gente a una ciudad y crece la población. ¿Qué pasa en el mercado de la vivienda?"), 0, t("More buyers: demand shifts right. Both rise.", "Más compradores: la demanda se desplaza a la derecha. Suben los dos."))]
    return [{"enun": "<strong>" + s + "</strong><br>" + t("What happens to the equilibrium?", "¿Qué le pasa al equilibrio?"), "ops": [O[k]] + [o for i, o in enumerate(O) if i != k], "ok": 0, "exp": e} for s, k, e in D]


def tx():
    return {"cred": t("{a} costs ${p} cash, or {n} monthly payments of ${c}. What percent more than the cash price does the installment plan cost?", "{a} cuesta ${p} al contado, o {n} cuotas mensuales de ${c}. ¿Qué porcentaje más que el precio al contado cuesta el plan a plazos?"),
            "art": [t("A refrigerator", "Un refrigerador"), t("A laptop", "Una computadora portátil"), t("A sofa", "Un sofá"), t("A washing machine", "Una lavadora"), t("A phone", "Un teléfono"), t("A television", "Un televisor")],
            "pidePct": t("Write the percent as a number, rounded to one decimal if needed (for example, 28).", "Escriba el porcentaje como número, redondeado a un decimal si hace falta (por ejemplo, 28)."),
            "esDol": t("That is the interest in dollars. Now divide it by the cash price and multiply by 100.", "Ese es el interés en dólares. Ahora divídalo entre el precio al contado y multiplique por 100."),
            "esTot": t("That is the total paid. Subtract the cash price first.", "Ese es el total pagado. Primero réstele el precio al contado."),
            "credP": t("Total = payment × number of payments. Interest = total − cash price. Percent = interest ÷ cash price × 100.", "Total = cuota × número de cuotas. Interés = total − precio al contado. Porcentaje = interés ÷ precio al contado × 100."),
            "inf": t("A basket of typical purchases cost ${a} last year and costs ${b} this year. What is the rate of inflation?", "Una canasta de compras típicas costaba ${a} el año pasado y cuesta ${b} este año. ¿Cuál es la tasa de inflación?"),
            "esDifI": t("That is the change in dollars. Divide it by last year’s cost.", "Ese es el cambio en dólares. Divídalo entre el costo del año pasado."),
            "esNuevo": t("You divided by this year’s cost. Divide by last year’s, the starting point.", "Dividió entre el costo de este año. Divida entre el del año pasado, el punto de partida."),
            "infP": t("Inflation = (new − old) ÷ old × 100.", "Inflación = (nuevo − viejo) ÷ viejo × 100.")}


JS = r"""
function rd1(x){ return Math.round(x * 10) / 10; }
function gCred(){
  var p, n, c, tot, int_, pc, k = 0;
  do {
    p = elige([300, 400, 500, 600, 800, 900, 1000, 1200, 1500]); n = elige([10, 12, 18, 24, 36]);
    var f = elige([1.1, 1.15, 1.2, 1.25, 1.3, 1.4]); c = Math.round(p * f / n);
    tot = c * n; int_ = tot - p; pc = int_ / p * 100; k++;
  } while ((Math.abs(pc * 10 - Math.round(pc * 10)) > 1e-9 || int_ <= 0) && k < 300);
  pc = rd1(pc);
  var enun = "<p>" + TXS.cred.replace("{a}", elige(TXS.art)).replace("{p}", com(p)).replace("{n}", n).replace("{c}", com(c)) + "</p><p>" + TXS.pidePct + "</p>";
  return {enun: enun, resp: leeNumero(String(pc)), explica: n + " × $" + com(c) + " = $" + com(tot) + "; $" + com(tot) + " − $" + com(p) + " = $" + com(int_) + "; " + com(int_) + " ÷ " + com(p) + " × 100 = " + pc + "%.",
    pista: function(x){ if (igual(x, leeNumero(String(int_)))) return TXS.esDol; if (igual(x, leeNumero(String(tot)))) return TXS.esTot; return TXS.credP; }};
}
function gInf(){
  var a, b, r, k = 0;
  do {
    a = elige([200, 250, 400, 500, 800, 850, 1000, 1200]); b = a + elige([4, 6, 8, 10, 12, 15, 20, 24, 30, 40]);
    r = (b - a) / a * 100; k++;
  } while (Math.abs(r * 10 - Math.round(r * 10)) > 1e-9 && k < 300);
  r = rd1(r);
  var enun = "<p>" + TXS.inf.replace("{a}", com(a)).replace("{b}", com(b)) + "</p><p>" + TXS.pidePct + "</p>";
  return {enun: enun, resp: leeNumero(String(r)), explica: "(" + com(b) + " − " + com(a) + ") ÷ " + com(a) + " × 100 = " + r + "%.",
    pista: function(x){ if (igual(x, leeNumero(String(b - a)))) return TXS.esDifI; if (igual(x, leeNumero(String(rd1((b - a) / b * 100))))) return TXS.esNuevo; return TXS.infP; }};
}
"""


def practica():
    A = {"en": ["which-curve", "credit", "inflation"], "es": ["que-curva", "credito", "inflacion"]}[C.L]
    mods = [
        (A[0], t("Which curve moves?", "¿Qué curva se mueve?"), C.om("m1", t("First decide whom the event affects, the buyer or the seller; then apply the trick: demand, same direction; supply, opposite directions.", "Primero decida a quién afecta el suceso, al comprador o al vendedor; después aplique el truco: demanda, misma dirección; oferta, direcciones opuestas."))),
        (A[1], t("What does the credit really cost?", "¿Cuánto cuesta de verdad el crédito?"), "      <p>" + t("New numbers every time. Total, then interest, then percent.", "Números nuevos cada vez. El total, después el interés, después el porcentaje.") + "</p>\n" + C.dec_campo("m2", t("Percent more", "Porcentaje de más"))),
        (A[2], t("Inflation from a basket", "La inflación a partir de una canasta"), "      <p>" + t("New numbers every time. (new − old) ÷ old × 100.", "Números nuevos cada vez. (nuevo − viejo) ÷ viejo × 100.") + "</p>\n" + C.dec_campo("m3", t("Rate of inflation", "Tasa de inflación"))),
    ]
    js = C.js_datos("TXS", tx()) + C.js_datos("CUR", banco_curvas()) + JS + 'creaBanco("m1", CUR);\ncreaPracticaDec("m2", gCred);\ncreaPracticaDec("m3", gInf);\n'
    return C.pagina_practica(N, titulo(), t("Three activities · new exercises every time · two tries in each one · calculator included", "Tres actividades · ejercicios nuevos cada vez · dos intentos en cada uno · con calculadora"), mods, js,
                             scripts=("/math/scinot.js",), calculadora=True)


if __name__ == "__main__":
    C.construye(N, leccion, practica)
