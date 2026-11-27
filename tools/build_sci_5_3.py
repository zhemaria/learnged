"""LearnGED · Ciencias · Lección 5.3 · Ecuaciones químicas, conservación de la materia y termoquímica (EN/ES).
Fuente: clases_ciencias/leccion_5-3.html (diagramas en tools/svg/5-3_*.svg) y el interactivo ciencias/balanceo_3d.
Uso: python3 tools/build_sci_5_3.py
"""
import os, sys, random, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ciencia as C
from ciencia import t

N = "5-3"
SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")


def titulo():
    return t("Chemical equations, conservation of matter, and thermochemistry", "Ecuaciones químicas, conservación de la materia y termoquímica")


def anc(en, es):
    return en if C.L == "en" else es


def R(x):
    return f'<span class="raiz">{x}</span>'


def f(x):
    """Fórmula ASCII → con subíndices."""
    return re.sub(r"(?<=[A-Za-z)])(\d+)", lambda m: m.group(1).translate(SUB), x)


def atomos(form):
    out = {}
    for el, n in re.findall(r"([A-Z][a-z]?)(\d*)", form):
        out[el] = out.get(el, 0) + int(n or 1)
    return out


def lado(forms, coefs):
    tot = {}
    for fo, k in zip(forms, coefs):
        for el, n in atomos(fo).items():
            tot[el] = tot.get(el, 0) + n * k
    return tot


def ecuacion(reac, prod, coefs):
    cs = list(coefs)
    def parte(forms, ks):
        return " + ".join((f"{k} " if k != 1 else "") + f(x) for x, k in zip(forms, ks))
    return parte(reac, cs[:len(reac)]) + " → " + parte(prod, cs[len(reac):])


def equilibrada(reac, prod, coefs):
    return lado(reac, coefs[:len(reac)]) == lado(prod, coefs[len(reac):])


def svg_ecuacion():
    tr = {k: k for k in ("2", "H", "+", "O")}
    tr.update({"REACTIVOS · lo que entra": "REACTANTS · what goes in", "PRODUCTOS · lo que sale": "PRODUCTS · what comes out", "«se transforma en»": "“turns into”", "Coeficiente": "Coefficient",
               "Cuántas moléculas intervienen.": "How many molecules take part.", "SÍ puede cambiarse al equilibrar.": "It CAN be changed when balancing.", "Subíndice": "Subscript",
               "Cuántos átomos hay dentro de la molécula.": "How many atoms are inside the molecule.", "NUNCA se cambia: sería otra sustancia.": "NEVER change it: it would be another substance.",
               "Lectura: dos moléculas de hidrógeno y una de oxígeno producen dos de agua.": "Reading: two molecules of hydrogen and one of oxygen make two of water."})
    return C.svg_orig("5-3_0", tr, "Parts of a balanced chemical equation. The equation shown is: two molecules of hydrogen plus one of oxygen make two molecules of water. To the left of the arrow are the reactants, what goes into the reaction; to the right are the products, what comes out. The large number written in front of a formula is the coefficient and tells how many molecules of that substance take part; it can be changed when balancing. The small number written below and to the right of a symbol is the subscript and tells how many atoms of that element are inside the molecule; it must never be changed, because changing it would turn the substance into a different one.")


def svg_energia():
    return C.svg_orig("5-3_1", {"Exotérmica · libera calor": "Exothermic · releases heat", "E": "E", "Reactivos": "Reactants", "Productos": "Products", "Energía liberada": "Energy released",
                                 "El entorno se calienta": "The surroundings warm up", "Endotérmica · absorbe calor": "Endothermic · absorbs heat", "Energía absorbida": "Energy absorbed", "El entorno se enfría": "The surroundings cool down"},
                       "Two energy diagrams compared. In the left diagram, for an exothermic reaction, the reactants are at a high energy level and the products at a lower one; the difference is released to the surroundings as heat, so the surroundings warm up. In the right diagram, for an endothermic reaction, the reactants are at a low level and the products at a higher one; the difference has been absorbed from the surroundings, which cool down as a result. The reading rule: if the products are below the reactants, the reaction releases heat; if they are above, it absorbs heat.")


def leccion():
    P = C.Practicas()
    s1 = f"""<p>{t("Lesson 5.2 ended with a distinction that now needs to be made formal. When water boils, it is still water: its molecules move apart but none breaks, and cooling it brings back the start. When paper burns, there is no way to get it back: the molecules have broken and their atoms have recombined into different substances.", "La lección anterior terminó con una distinción que ahora conviene formalizar. Cuando el agua hierve, sigue siendo agua: sus moléculas se separan pero ninguna se rompe, y basta enfriarla para recuperar el estado inicial. Cuando el papel arde, en cambio, no hay manera de devolverle su forma: las moléculas se han roto y sus átomos se han recombinado en sustancias distintas.")}</p>
{C.tabla(t("Physical and chemical changes compared: bonds, new substances, reversibility, and examples", "Comparación entre cambio físico y cambio químico según lo que ocurre con los enlaces, la reversibilidad y ejemplos de cada tipo"),
 [t("Test", "Criterio"), t("Physical change", "Cambio físico"), t("Chemical change", "Cambio químico")],
 [[t("What happens to the bonds", "Qué ocurre con los enlaces"), t("They do not break: molecules only move closer or farther apart", "No se rompen: las moléculas solo se acercan o se separan"), t("Some break and new ones form", "Se rompen unos y se forman otros nuevos")],
  [t("Do new substances appear?", "¿Aparecen sustancias nuevas?"), t("No: the substance stays the same", "No: la sustancia sigue siendo la misma"), t("Yes: the products are different from the reactants", "Sí: los productos son distintos de los reactivos")],
  [t("Can it be reversed?", "Reversibilidad"), t("Usually easily: just add or remove energy", "Casi siempre fácil: basta devolver o retirar energía"), t("Hard or impossible by simple means", "Difícil o imposible por medios sencillos")],
  [t("Examples", "Ejemplos"), t("Melting ice, boiling water, dissolving salt, crushing a rock", "Fundir hielo, hervir agua, disolver sal, triturar una roca"), t("Burning, rusting, digesting food, photosynthesis", "Arder, oxidarse, digerir alimentos, fotosintetizar")]])}
<h3>{t("Signs that a reaction has happened", "Las señales de que ha ocurrido una reacción")}</h3>
<p>{t("A chemical change rarely announces itself. You notice it by clues, and the test usually describes one or more of them in the question instead of naming the reaction:", "Un cambio químico rara vez se anuncia. Se detecta por indicios, y el examen suele describir uno o varios en el enunciado en lugar de nombrar la reacción:")}</p>
<ul><li>{t("<strong>A gas is given off:</strong> bubbles appear where there were none.", "<strong>Desprendimiento de un gas:</strong> aparecen burbujas donde antes no las había.")}</li>
<li>{t("<strong>A precipitate forms:</strong> mixing two clear liquids makes a solid.", "<strong>Formación de un precipitado:</strong> al mezclar dos líquidos transparentes surge un sólido.")}</li>
<li>{t("<strong>A lasting color change</strong> that is not just a mix of colors.", "<strong>Cambio de color permanente</strong>, que no se debe a una mezcla de pigmentos.")}</li>
<li>{t("<strong>A temperature change with no outside source:</strong> the mixture warms up or cools down on its own.", "<strong>Cambio de temperatura sin fuente externa:</strong> la mezcla se calienta o se enfría sola.")}</li>
<li>{t("<strong>Light is given off</strong>, as in a flame.", "<strong>Emisión de luz</strong>, como en una llama.")}</li></ul>
{C.caja("ojo", t("No single clue settles it", "Ningún indicio aislado es concluyente"), "<p>" + t("That is the trap. Boiling water also makes bubbles, and yet it is a physical change: the gas is still water. The deciding question is not what you see, but whether the resulting substance is <strong>different</strong> from the starting one. Use that test before answering, especially when the question leans hard on one clue.", "Ahí está la trampa. Al hervir agua también aparecen burbujas, y sin embargo es un cambio físico: el gas que se forma sigue siendo agua. La pregunta decisiva no es qué se observa, sino si la sustancia resultante es <strong>distinta</strong> de la de partida. Conviene aplicar ese criterio antes de responder, sobre todo cuando el enunciado insiste mucho en un solo indicio.") + "</p>")}
{C.enlace(N, anc("physical-chemical", "fisico-quimico"), t("physical or chemical?", "¿físico o químico?"), t("Everyday changes: is there a new substance?", "Cambios cotidianos: ¿hay una sustancia nueva?"))}"""

    s2 = f"""<p>{t("A chemical equation is a short way of counting what happens in a reaction. It is read from left to right: the <strong>reactants</strong> are what goes in, the arrow means “turns into,” and the <strong>products</strong> are what comes out.", "Una ecuación química es la manera abreviada de contar lo que ocurre en una reacción. Se lee de izquierda a derecha: los <strong>reactivos</strong> son lo que entra, la flecha significa «se transforma en» y los <strong>productos</strong> son lo que sale.")}</p>
{svg_ecuacion()}
<p>{t(f"The difference between a coefficient and a subscript is the only truly tricky rule of the lesson. Fix it with an example: 2 {f('H2O')} is two molecules of water, while {f('H4O2')} is not water at all. It is a substance that does not exist. That is why, when balancing, you only touch the large numbers in front.", f"La distinción entre coeficiente y subíndice es la única regla verdaderamente delicada de la lección, y conviene fijarla con un ejemplo: 2 {f('H2O')} son dos moléculas de agua, mientras que {f('H4O2')} no es agua en absoluto. Es una sustancia inexistente. Por eso, al equilibrar, solo se tocan los números grandes de delante.")}</p>
<p>{t("Many equations also give the state of each substance in parentheses: (s) solid, (l) liquid, (g) gas, and (aq) dissolved in water, that is, in an aqueous solution. That last symbol links directly to the solutions of Lesson 5.2.", "Muchas ecuaciones incluyen además el estado de cada sustancia entre paréntesis: (s) sólido, (l) líquido, (g) gas y (ac) disuelto en agua, es decir, en disolución acuosa. Ese último símbolo enlaza directamente con las disoluciones de la Lección 5.2.")}</p>
{P(t("Try it 1 · Three waters", "Pruebe 1 · Tres aguas"), t(f"The expression 3 {f('H2O')} stands for…", f"La expresión 3 {f('H2O')} representa…"),
   [t("one molecule with three oxygen atoms", "una molécula con tres átomos de oxígeno"), t("three molecules of water, with 6 hydrogen atoms and 3 oxygen atoms in all", "tres moléculas de agua, con 6 átomos de hidrógeno y 3 de oxígeno en total"), t("a substance other than water", "una sustancia distinta del agua")], 1,
   {0: t("The 3 multiplies the whole molecule.", "El 3 multiplica la molécula entera."), 2: t("A coefficient does not change the substance.", "Un coeficiente no cambia la sustancia.")}, t("3 × H₂ = 6 H; 3 × O = 3 O.", "3 × H₂ = 6 H; 3 × O = 3 O."))}
{C.enlace(N, anc("count", "contar"), t("count atoms in formulas", "cuente átomos en fórmulas"), t("Coefficient × subscript, element by element.", "Coeficiente × subíndice, elemento por elemento."))}"""

    s3 = f"""<p>{t("Balancing an equation means adjusting the coefficients until there is the same number of atoms of each element on both sides of the arrow. It is not a calculation: it is a count, checked element by element.", "Equilibrar una ecuación consiste en ajustar los coeficientes hasta que haya el mismo número de átomos de cada elemento a los dos lados de la flecha. No es un cálculo: es un conteo, y se comprueba elemento por elemento.")}</p>
{C.ejemplo(t("Example 1 · Making water", "Ejemplo 1 · La formación del agua"),
 [("", t(f"Balance: {f('H2 + O2 → H2O')}", f"Equilibre: {f('H2 + O2 → H2O')}")),
  ("1", t("<strong>Count as it is.</strong> Left: 2 H and 2 O. Right: 2 H and 1 O. Hydrogen matches; oxygen does not.", "<strong>Contar como está.</strong> Izquierda: 2 H y 2 O. Derecha: 2 H y 1 O. El hidrógeno cuadra; el oxígeno no.")),
  ("2", t(f"<strong>Fix the element that is off.</strong> To have 2 O on the right you need two water molecules: {f('H2 + O2 → 2 H2O')}.", f"<strong>Ajustar el elemento descuadrado.</strong> Para tener 2 O a la derecha hacen falta dos moléculas de agua: {f('H2 + O2 → 2 H2O')}.")),
  ("3", t("<strong>Count again.</strong> That change pulled the hydrogen along: now there are 4 H on the right and only 2 on the left.", "<strong>Volver a contar.</strong> Ese cambio arrastró el hidrógeno: ahora hay 4 H a la derecha y solo 2 a la izquierda.")),
  ("4", t(f"<strong>Fix again.</strong> {f('2 H2 + O2 → 2 H2O')}. Final count: 4 H and 2 O on each side. Balanced.", f"<strong>Reajustar.</strong> {f('2 H2 + O2 → 2 H2O')}. Recuento final: 4 H y 2 O a cada lado. Equilibrada."))],
 t("Remember step 3: fixing one element often throws off another. That is why the method goes around in a loop (fix, count again, fix) and does not end until a full count comes out clean.", "El paso 3 es el que conviene retener: ajustar un elemento suele descuadrar otro. Por eso el procedimiento es siempre cíclico —ajustar, volver a contar, ajustar— y no termina hasta que un recuento completo sale limpio."))}
{C.ejemplo(t("Example 2 · Burning methane", "Ejemplo 2 · La combustión del metano"),
 [("", t(f"Balance: {f('CH4 + O2 → CO2 + H2O')}", f"Equilibre: {f('CH4 + O2 → CO2 + H2O')}")),
  ("1", t("<strong>Count as it is.</strong> Left: 1 C, 4 H, 2 O. Right: 1 C, 2 H, 3 O. Carbon matches.", "<strong>Contar como está.</strong> Izquierda: 1 C, 4 H, 2 O. Derecha: 1 C, 2 H, 3 O. El carbono cuadra.")),
  ("2", t(f"<strong>Start with hydrogen</strong>, which is in only one substance on each side. For 4 H on the right: {f('CH4 + O2 → CO2 + 2 H2O')}.", f"<strong>Empezar por el hidrógeno</strong>, que aparece en una sola sustancia a cada lado. Para tener 4 H a la derecha: {f('CH4 + O2 → CO2 + 2 H2O')}.")),
  ("3", t("<strong>Leave oxygen for last</strong>, because it is in two products. Now there are 2 O in the CO₂ plus 2 O in the two waters: 4 O on the right.", "<strong>Dejar el oxígeno para el final</strong>, porque aparece en dos productos. Ahora hay 2 O en el CO₂ más 2 O en las dos moléculas de agua: 4 O en total a la derecha.")),
  ("4", t(f"<strong>Fix the oxygen going in.</strong> {f('CH4 + 2 O2 → CO2 + 2 H2O')}. Final count: 1 C, 4 H, and 4 O on each side. Balanced.", f"<strong>Ajustar el oxígeno de entrada.</strong> {f('CH4 + 2 O2 → CO2 + 2 H2O')}. Recuento final: 1 C, 4 H y 4 O a cada lado. Equilibrada."))])}
{C.tabla(t("Atom count for the balanced equation for burning methane, left and right of the arrow", "Recuento de átomos de la ecuación equilibrada de la combustión del metano, a la izquierda y a la derecha de la flecha"),
 [t("Element", "Elemento"), t("Atoms on the left", "Átomos a la izquierda"), t("Atoms on the right", "Átomos a la derecha"), t("Match?", "¿Cuadra?")],
 [[t("Carbon (C)", "Carbono (C)"), "1", "1", t("Yes", "Sí")], [t("Hydrogen (H)", "Hidrógeno (H)"), "4", "4", t("Yes", "Sí")], [t("Oxygen (O)", "Oxígeno (O)"), "4", "4", t("Yes", "Sí")]])}
{C.caja("tip", t("Two habits that save time on the test", "Dos costumbres que ahorran tiempo en el examen"), "<p>" + t("First: leave for last the elements that appear in more than one substance on the same side (almost always oxygen and hydrogen), because fixing them early makes you redo everything. Second: check your answer by counting, not by rereading. If each element’s count is the same on both sides, the equation is balanced even if the coefficients do not match the answer key.", "La primera: dejar para el final los elementos que aparecen en más de una sustancia del mismo lado —casi siempre el oxígeno y el hidrógeno—, porque ajustarlos antes obliga a rehacerlo todo. La segunda: comprobar la respuesta contando, no releyendo. Si el recuento de cada elemento sale igual a los dos lados, la ecuación está equilibrada aunque los coeficientes no coincidan con los de la clave.") + "</p>")}
{C.caja("ojo", t("The absolute rule: never touch the subscripts", "La prohibición absoluta: no se tocan los subíndices"), "<p>" + t(f"If you are tempted to turn {f('H2O')} into {f('H2O2')} to make the numbers work, the answer is no. Hydrogen peroxide, {f('H2O2')}, is another substance with other properties. Balancing means adjusting how many molecules take part, never what they are made of inside.", f"Si al equilibrar aparece la tentación de convertir {f('H2O')} en {f('H2O2')} para que salgan las cuentas, la respuesta es no. El agua oxigenada, {f('H2O2')}, es otra sustancia con otras propiedades. Equilibrar significa ajustar cuántas moléculas intervienen, jamás cómo son por dentro.") + "</p>")}
{P(t("Try it 2 · What can change", "Pruebe 2 · Qué se puede cambiar"), t("When balancing a chemical equation, the only thing you may change is…", "Al equilibrar una ecuación química, lo único que puede modificarse es…"),
   [t("the subscripts in the formulas", "los subíndices de las fórmulas"), t("the element symbols", "los símbolos de los elementos"), t("the coefficients in front of the formulas", "los coeficientes situados delante de las fórmulas")], 2,
   {0: t("That would make another substance.", "Eso crearía otra sustancia."), 1: t("That would change the elements.", "Eso cambiaría los elementos.")}, t("Only the large numbers in front.", "Solo los números grandes de delante."))}
{P(t("Try it 3 · Six oxygen atoms", "Pruebe 3 · Seis átomos de oxígeno"), t("If the reactants have 6 oxygen atoms, the products must have…", "Si en el lado de los reactivos hay 6 átomos de oxígeno, en el de los productos debe haber…"),
   [t("exactly 6, because matter is neither made nor destroyed", "exactamente 6, porque la materia no se crea ni se destruye"), t("fewer, because some is used up", "menos, porque parte se consume en la reacción"), t("more, because new substances are made", "más, porque la reacción produce sustancias nuevas")], 0,
   {1: t("Atoms are rearranged, not used up.", "Los átomos se recolocan, no se gastan."), 2: t("New substances, same atoms.", "Sustancias nuevas, mismos átomos.")}, t("Conservation of matter.", "Conservación de la materia."))}
{C.enlace(N, anc("balance", "equilibrar"), t("balance equations", "equilibre ecuaciones"), t("Choose the coefficients that balance each equation, and count to check.", "Elija los coeficientes que equilibran cada ecuación y compruebe contando."))}"""

    tipos = [(t("Synthesis", "Síntesis"), "A + B → AB", t("Two or more substances go in and one comes out", "Entran dos o más sustancias y sale una sola"), f("2 H2 + O2 → 2 H2O")),
             (t("Decomposition", "Descomposición"), "AB → A + B", t("One substance goes in and two or more come out", "Entra una sola sustancia y salen dos o más"), f("2 H2O2 → 2 H2O + O2")),
             (t("Replacement", "Sustitución"), "A + BC → AC + B", t("One element takes the place of another in a compound", "Un elemento ocupa el lugar de otro en un compuesto"), f("Zn + 2 HCl → ZnCl2 + H2")),
             (t("Combustion", "Combustión"), t("Fuel + O₂ → CO₂ + H₂O", "Combustible + O₂ → CO₂ + H₂O"), t("It reacts with oxygen, gives off heat, and usually makes carbon dioxide and water", "Reacciona con oxígeno, libera calor y suele dar dióxido de carbono y agua"), f("CH4 + 2 O2 → CO2 + 2 H2O"))]
    s4 = f"""<p>{t("The test does not ask you to memorize mechanisms, but to recognize a shape. The four types it checks are told apart by how many substances go in and come out, and how they rearrange.", "El examen no pide memorizar mecanismos, sino reconocer una forma. Los cuatro tipos que evalúa se distinguen mirando cuántas sustancias entran y cuántas salen, y cómo se recolocan.")}</p>
{C.tabla(t("The four basic types of chemical reaction: general form, how to recognize them, and an example", "Los cuatro tipos básicos de reacción química con su forma general, cómo reconocerlos y un ejemplo de cada uno"),
 [t("Type", "Tipo"), t("General form", "Forma general"), t("How to recognize it", "Cómo se reconoce"), t("Example", "Ejemplo")], [list(x) for x in tipos])}
{C.caja("tip", t("The shortcut", "El atajo para clasificar"), "<p>" + t("Count substances before reading formulas. If there is only one on the left of the arrow, it is decomposition. If there is only one on the right, synthesis. If O₂ is among the reactants and CO₂ and water among the products, combustion. Only when none of those three signs appears do you need to look closely at whether one element has replaced another.", "Consiste en contar sustancias antes de leer fórmulas. Si a la izquierda de la flecha hay una sola, es descomposición. Si a la derecha hay una sola, es síntesis. Si aparece O₂ entre los reactivos y CO₂ y agua entre los productos, es combustión. Solo cuando ninguna de las tres señales aparece hay que mirar con detalle si un elemento ha desplazado a otro.") + "</p>")}
<p>{t("Notice that photosynthesis and cellular respiration from Lesson 3.2 are, in this vocabulary, reverse reactions of each other: the products of one are the reactants of the other. It is the same pair studied then, now written in the language of equations.", "Merece la pena notar que la fotosíntesis de la Lección 3.2 y la respiración celular son, en este vocabulario, reacciones inversas la una de la otra: los productos de una son los reactivos de la otra. Es el mismo par que se estudió entonces, ahora escrito en el lenguaje de las ecuaciones.")}</p>
{P(t("Try it 4 · Which type?", "Pruebe 4 · ¿Qué tipo?"), t(f"The reaction {f('2 H2O2 → 2 H2O + O2')} is…", f"La reacción {f('2 H2O2 → 2 H2O + O2')} es de tipo…"),
   [t("decomposition", "descomposición"), t("synthesis", "síntesis"), t("combustion", "combustión")], 0,
   {1: t("Synthesis has one product; here there is one reactant.", "La síntesis tiene un solo producto; aquí hay un solo reactivo."), 2: t("There is no fuel burning with O₂.", "No hay combustible ardiendo con O₂.")}, t("One substance in, two out.", "Entra una, salen dos."))}
{C.enlace(N, anc("types", "tipos"), t("classify reactions", "clasifique reacciones"), t("Synthesis, decomposition, replacement, or combustion?", "¿Síntesis, descomposición, sustitución o combustión?"))}"""

    s5 = f"""<p>{t("Breaking bonds costs energy; forming them releases energy. The balance between the two decides whether a reaction, overall, gives off heat to its surroundings or takes heat in.", "Romper enlaces cuesta energía; formarlos la libera. El balance entre esas dos cantidades decide si una reacción, en conjunto, desprende calor al entorno o lo absorbe de él.")}</p>
{svg_energia()}
<p>{t("Reading the diagram comes down to comparing two heights: if the products end up <strong>below</strong> the reactants, the reaction released heat and is <strong>exothermic</strong>; if they are <strong>above</strong>, it absorbed heat and is <strong>endothermic</strong>. All the energy that is “missing” or “extra” came from the surroundings or went into them.", "La lectura del diagrama se reduce a comparar dos alturas: si los productos quedan <strong>por debajo</strong> de los reactivos, la reacción libera calor y es <strong>exotérmica</strong>; si quedan <strong>por encima</strong>, lo ha absorbido y es <strong>endotérmica</strong>. Toda la energía que «falta» o que «sobra» ha salido del entorno o ha ido a parar a él.")}</p>
{C.tabla(t("Exothermic and endothermic reactions compared: energy flow, position in the diagram, what you feel, and examples", "Comparación entre reacciones exotérmicas y endotérmicas según el flujo de energía, la posición en el diagrama, lo que se percibe y ejemplos"),
 [t("Test", "Criterio"), t("Exothermic", "Exotérmica"), t("Endothermic", "Endotérmica")],
 [[t("Energy flow", "Flujo de energía"), t("The reaction gives heat to the surroundings", "La reacción entrega calor al entorno"), t("The reaction takes heat from the surroundings", "La reacción toma calor del entorno")],
  [t("In the diagram", "En el diagrama"), t("Products below reactants", "Los productos quedan por debajo de los reactivos"), t("Products above reactants", "Los productos quedan por encima de los reactivos")],
  [t("Touching the container", "Al tocar el recipiente"), t("Feels hot", "Se nota caliente"), t("Feels cold", "Se nota frío")],
  [t("Examples", "Ejemplos"), t("Burning a fuel, iron rusting, cement setting", "Arder un combustible, oxidarse el hierro, fraguar el cemento"), t("An instant cold pack, cooking food, photosynthesis", "La compresa fría instantánea, cocer un alimento, la fotosíntesis")]])}
{C.caja("ojo", t("The vocabulary mistake that costs the most", "El error de vocabulario que más se cobra el examen"), "<p>" + t(f"Thinking “endothermic” means the reaction is hot, because the word sounds like “thermal.” It is the other way around. In an endothermic reaction heat goes <strong>into</strong> the reaction, so the surroundings (and the hand holding the container) get cold. The roots leave no doubt: {R('endo-')}, inward; {R('exo-')}, outward.", f"Creer que «endotérmica» significa que la reacción está caliente, porque el término suena a térmico. Es al revés. En una reacción endotérmica el calor <strong>entra</strong> en la reacción, de modo que el entorno —y con él la mano que sostiene el recipiente— se queda frío. Las raíces lo dicen sin ambigüedad: {R('endo-')}, hacia dentro; {R('exo-')}, hacia fuera.") + "</p>")}
{C.caja("tip", t("The instant cold pack", "La compresa fría instantánea"), "<p>" + t("It is the questions’ favorite example, because it joins 5.2 with this lesson. When you break the inner bag, a salt dissolves in water and the process absorbs heat: the solution takes energy from the surroundings and the pack gets cold with no freezer. It is the same kind of solution as in Lesson 5.2, now read in terms of energy.", "Es el ejemplo favorito de los enunciados, porque une la 5.2 con esta lección. Al romper la bolsa interior, una sal se disuelve en agua y el proceso absorbe calor: la disolución toma energía del entorno y la compresa se enfría sin necesidad de nevera. Es la misma disolución de la Lección 5.2, ahora leída en términos de energía.") + "</p>")}
<h3><span aria-hidden="true">🔤</span> {t("Science vocabulary: roots", "Vocabulario técnico: raíces")}</h3>
<p>{t(f"<strong>Reactant</strong> and <strong>reaction</strong> share the Latin <em>re-agere</em>, to act back or respond. <strong>Product</strong> comes from <em>producere</em>, to bring forward. <strong>Exothermic</strong> and <strong>endothermic</strong> differ only by the Greek prefix: {R('exo-')}, outward, as in <em>exit</em> and <em>exodus</em>, against {R('endo-')}, inward, as in <em>endoscopy</em>; both with {R('thermós')}, heat, as in <em>thermometer</em>. <strong>Synthesis</strong> comes from {R('syn-')}, together, and <em>thesis</em>, placing: putting several things together, which is just what that reaction does. <strong>Decomposition</strong> is its opposite. <strong>Combustion</strong> comes from the Latin <em>comburere</em>, to burn up completely. And <strong>coefficient</strong> comes from <em>co-</em>, with, and <em>efficere</em>, to produce: the number that goes with a formula without being part of it.", f"<strong>Reactivo</strong> y <strong>reacción</strong> comparten el latín <em>re-agere</em>, actuar de vuelta o responder. <strong>Producto</strong> viene de <em>producere</em>, llevar adelante o sacar. <strong>Exotérmico</strong> y <strong>endotérmico</strong> se separan solo por el prefijo griego: {R('exo-')}, hacia fuera, la misma raíz de <em>éxodo</em>, frente a {R('endo-')}, hacia dentro, la de <em>endoscopia</em>; ambas con {R('thermós')}, calor, ya vista en <em>termómetro</em>. <strong>Síntesis</strong> procede de {R('syn-')}, junto, y <em>thesis</em>, colocación: colocar juntas varias cosas, exactamente lo que hace esa reacción. <strong>Descomposición</strong> es su contraria, de <em>des-</em>, separación, y <em>componere</em>, poner junto. <strong>Combustión</strong> viene del latín <em>comburere</em>, quemar por completo. Y <strong>coeficiente</strong>, de <em>co-</em>, junto, y <em>efficere</em>, producir: el número que acompaña a la fórmula sin formar parte de ella.")}</p>
{P(t("Try it 5 · The diagram", "Pruebe 5 · El diagrama"), t("In an energy diagram, the products are clearly below the reactants. The reaction…", "En un diagrama de energía, los productos quedan claramente por debajo de los reactivos. La reacción…"),
   [t("absorbs heat and cools the surroundings", "absorbe calor y enfría el entorno"), t("releases heat and warms the surroundings", "libera calor y calienta el entorno"), t("exchanges no energy", "no intercambia energía con el entorno")], 1,
   {0: t("That is when products are above.", "Eso ocurre cuando los productos están por encima."), 2: t("A difference in height means energy moved.", "Una diferencia de altura significa que se movió energía.")}, t("Products below: energy went out. Exothermic.", "Productos abajo: la energía salió. Exotérmica."))}
{P(t("Try it 6 · Cold pack", "Pruebe 6 · Compresa fría"), t("An instant cold pack gets cold when you activate it. This shows that the process inside…", "Una compresa fría instantánea se enfría al activarla. Eso indica que el proceso del interior…"),
   [t("is combustion", "es una combustión"), t("is exothermic", "es exotérmico"), t("is endothermic: it absorbs heat from the surroundings", "es endotérmico: absorbe calor del entorno")], 2,
   {0: t("Combustion gives off heat.", "La combustión desprende calor."), 1: t("Exothermic would warm up.", "Exotérmico se calentaría.")}, t("Cold to the touch = heat going in = endothermic.", "Frío al tacto = calor que entra = endotérmico."))}
{C.enlace(N, anc("energy", "energia"), t("exothermic or endothermic?", "¿exotérmica o endotérmica?"), t("Diagrams and situations: does heat go out or come in?", "Diagramas y situaciones: ¿el calor sale o entra?"))}"""

    s6 = f"""<p>{t("A short science text written for this level. Notice how a law that seems to go against what we see was tested.", "Texto científico breve adaptado al nivel. Observe cómo se comprueba una ley que parece contradecir lo observable.")}</p>
{C.lectura(t("The candle that weighed less", "La vela que pesaba menos"),
 [t("For centuries it seemed obvious that when something burned, part of the matter was destroyed. A lit candle gets smaller until it disappears; a log leaves only ashes, much lighter than the log. The observation seemed conclusive.", "Durante siglos se consideró evidente que al arder una sustancia se destruía parte de la materia. Una vela encendida disminuye hasta desaparecer; un leño deja solo cenizas, mucho más ligeras que el leño original. La observación parecía concluyente."),
  t("In the 1700s, Antoine Lavoisier put that idea to a different test. Instead of weighing only the solid, he carried out the burning in sealed containers and weighed the whole container, with the air inside, before and after the reaction. The total mass did not change.", "En el siglo XVIII, Antoine Lavoisier sometió esa idea a una prueba distinta. En lugar de pesar únicamente el sólido, realizó las combustiones en recipientes cerrados y pesó el recipiente completo, con el aire de su interior, antes y después de la reacción. La masa total no varió."),
  t("The explanation was that the products of burning include gases (mainly carbon dioxide and water vapor) that escape unweighed from an open container. Once trapped, the scale registered them. Lavoisier also checked the reverse: when certain metals were heated in air, the resulting solid weighed more than the starting metal, because it had taken in oxygen.", "La explicación era que los productos de la combustión incluyen gases —principalmente dióxido de carbono y vapor de agua— que en un recipiente abierto escapan sin ser pesados. Al confinarlos, la balanza los registraba. Lavoisier comprobó además el proceso inverso: al calentar ciertos metales en presencia de aire, el sólido resultante pesaba más que el metal de partida, porque había incorporado oxígeno."),
  t("From these and other experiments came the statement of the conservation of matter. Note that the law was not drawn from direct observation, which pointed the opposite way, but from a change in how things were measured: counting what cannot be seen as well.", "De estos y otros experimentos surgió el enunciado de la conservación de la materia. Conviene señalar que la ley no se dedujo de la observación directa, que apuntaba en sentido contrario, sino de un cambio en el modo de medir: contar también lo que no se ve.")])}
{P(t("Reading · Question 1", "Lectura · Pregunta 1"), t("What is the main idea of the text?", "¿Cuál es la idea central del texto?"),
   [t("Candles and logs do not really burn.", "Las velas y los leños no arden realmente."), t("Lavoisier showed that matter is destroyed when it burns.", "Lavoisier demostró que la materia se destruye al arder."), t("Mass seemed to be lost because the gases were not weighed; measured in a sealed container, it is conserved.", "La masa parecía perderse porque no se pesaban los gases; al medirlos en recipiente cerrado, se comprobó que se conserva.")], 2,
   {0: t("They do burn.", "Sí arden."), 1: t("He showed the opposite.", "Demostró lo contrario.")}, t("Count what you cannot see.", "Contar lo que no se ve."))}
{P(t("Reading · Question 2", "Lectura · Pregunta 2"), t("The key change Lavoisier made was…", "El cambio decisivo que introdujo Lavoisier fue…"),
   [t("weighing the whole sealed container, including the gases inside", "pesar el recipiente cerrado completo, incluidos los gases del interior"), t("using bigger scales", "utilizar balanzas de mayor tamaño"), t("repeating the experiment many more times", "repetir el experimento muchas más veces")], 0,
   {1: t("Size was not the point.", "El tamaño no era la cuestión."), 2: t("The text points to what was weighed, not how often.", "El texto destaca qué se pesó, no cuántas veces.")}, t("Second paragraph.", "Segundo párrafo."))}
{P(t("Reading · Question 3", "Lectura · Pregunta 3"), t("A metal heated in air weighs more than before because…", "Que un metal calentado al aire pese más que antes se explica porque…"),
   [t("heat adds mass to objects", "el calor añade masa a los cuerpos"), t("the metal has taken in oxygen from the air", "el metal ha incorporado oxígeno procedente del aire"), t("the scale goes off with the temperature", "la balanza se descalibra con la temperatura")], 1,
   {0: t("Heat is not matter.", "El calor no es materia."), 2: t("The text does not say that.", "El texto no dice eso.")}, t("The extra mass is oxygen.", "La masa añadida es oxígeno."))}
{P(t("Reading · Question 4", "Lectura · Pregunta 4"), t("Which conclusion does the text support without going beyond it?", "¿Qué conclusión se apoya en el texto sin ir más allá de lo que afirma?"),
   [t("Direct observation is never useful in science.", "La observación directa nunca sirve en ciencia."), t("All chemical reactions make gases.", "Todas las reacciones químicas producen gases."), t("A conclusion can change completely when you change what you decide to measure.", "Una conclusión puede cambiar por completo cuando se modifica lo que se decide medir.")], 2,
   {0: t("“Never” goes too far.", "«Nunca» va demasiado lejos."), 1: t("“All” goes too far.", "«Todas» va demasiado lejos.")}, t("Last paragraph.", "Último párrafo."))}"""

    G = lambda *a: C.ged_item(P, *a)
    temps = {"tipo": "tabla", "encabezados": [t("Mixture", "Mezcla"), t("Start (°C)", "Inicio (°C)"), t("After 1 minute (°C)", "Al minuto (°C)")],
             "filas": [["A", "21", "34"], ["B", "21", "9"], ["C", "21", "21"]]}
    sG = "<p>" + t("These questions work like the ones on the GED® Science test: a short text, a table, or a graph, then a question with four options. Each one shows the science practice it checks and its depth of knowledge (DOK).", "Estas preguntas funcionan como las del examen de Ciencias del GED®: un texto breve, una tabla o una gráfica, y después una pregunta con cuatro opciones. Cada una indica la práctica científica que evalúa y su profundidad de conocimiento (DOK).") + f"""</p>
{G(1, "SP.6.b", "2", t(f"Which coefficients balance <strong>{f('Al + O2 → Al2O3')}</strong>?", f"¿Qué coeficientes equilibran <strong>{f('Al + O2 → Al2O3')}</strong>?"),
   ["4, 3, 2", "2, 3, 1", "1, 1, 1", "2, 1, 1"], 0,
   {1: t("Count O: 6 on the left, 3 on the right.", "Cuente el O: 6 a la izquierda, 3 a la derecha."), 2: t("Al: 1 against 2; O: 2 against 3.", "Al: 1 frente a 2; O: 2 frente a 3."), 3: t("O: 2 against 3.", "O: 2 frente a 3.")},
   t("4 Al = 4 Al; 3 O₂ = 6 O. Right: 2 Al₂O₃ = 4 Al and 6 O.", "4 Al = 4 Al; 3 O₂ = 6 O. Derecha: 2 Al₂O₃ = 4 Al y 6 O."))}
{G(2, "SP.7.a", "2–3", t("<em>A student puts 5 g of baking soda and 50 g of vinegar in a sealed plastic bottle on a scale. The total is 205 g. The mixture fizzes.</em><br>What will the scale read when the fizzing stops, if the bottle stays sealed?", "<em>Un estudiante pone 5 g de bicarbonato y 50 g de vinagre en una botella de plástico cerrada sobre una balanza. El total es 205 g. La mezcla hace burbujas.</em><br>¿Qué marcará la balanza cuando cesen las burbujas, si la botella sigue cerrada?"),
   ["205 g", t("Less than 205 g, because gas formed", "Menos de 205 g, porque se formó gas"), t("More than 205 g, because a new substance formed", "Más de 205 g, porque se formó una sustancia nueva"), "150 g"], 0,
   {1: t("The gas is trapped in the bottle, so it is weighed.", "El gas queda atrapado en la botella, así que se pesa."), 2: t("New substances, same atoms.", "Sustancias nuevas, mismos átomos."), 3: t("That subtracts things that are still in the bottle.", "Eso resta cosas que siguen en la botella.")},
   t("In a sealed container, mass is conserved: 205 g. (Open, the gas would escape and the reading would drop.)", "En un recipiente cerrado la masa se conserva: 205 g. (Abierto, el gas escaparía y la lectura bajaría.)"))}
{G(3, "SP.1.c", "2", t("<em>Look at the energy diagrams in section 5.</em><br>In the right-hand diagram, why do the surroundings cool down?", "<em>Observe los diagramas de energía de la sección 5.</em><br>En el diagrama de la derecha, ¿por qué se enfría el entorno?"),
   [t("The products have more energy than the reactants, so energy was taken from the surroundings.", "Los productos tienen más energía que los reactivos, así que se tomó energía del entorno."), t("The products have less energy than the reactants.", "Los productos tienen menos energía que los reactivos."), t("No energy changes.", "La energía no cambia."), t("The reaction gives off light.", "La reacción emite luz.")], 0,
   {1: t("That is the left-hand (exothermic) diagram.", "Ese es el diagrama de la izquierda (exotérmico)."), 2: t("The levels are at different heights.", "Los niveles están a distinta altura."), 3: t("The diagram says nothing about light.", "El diagrama no dice nada de luz.")},
   t("Products above reactants: endothermic, heat taken in.", "Productos por encima de los reactivos: endotérmica, calor absorbido."))}
{G(4, "SP.3.b", "2", t("<em>A student mixes three pairs of substances and measures the temperature.</em>", "<em>Un estudiante mezcla tres pares de sustancias y mide la temperatura.</em>") + C.grafica(temps, t("Data table", "Tabla de datos")) + t("Which conclusion do the data support?", "¿Qué conclusión apoyan los datos?"),
   [t("A is exothermic, B is endothermic, and C shows no sign of energy change.", "A es exotérmica, B es endotérmica y C no muestra cambio de energía."), t("A is endothermic and B is exothermic.", "A es endotérmica y B exotérmica."), t("All three are chemical reactions.", "Las tres son reacciones químicas."), t("C is the fastest reaction.", "C es la reacción más rápida.")], 0,
   {1: t("A got warmer: heat came out.", "A se calentó: salió calor."), 2: t("C shows no clue of a reaction.", "C no muestra ningún indicio de reacción."), 3: t("Nothing was measured about speed.", "No se midió la velocidad.")},
   t("Warmer = heat out (exothermic). Colder = heat in (endothermic). No change = no evidence either way.", "Más caliente = sale calor (exotérmica). Más frío = entra calor (endotérmica). Sin cambio = no hay evidencia."))}
{G(5, "SP.4.a", "2–3", t("<em>Read “The candle that weighed less” in section 6. Someone says: “The ashes weigh less than the log, so burning destroys matter.”</em><br>How does Lavoisier’s evidence relate to that claim?", "<em>Lea «La vela que pesaba menos» de la sección 6. Alguien afirma: «Las cenizas pesan menos que el leño, así que arder destruye materia».</em><br>¿Qué relación tiene la evidencia de Lavoisier con esa afirmación?"),
   [t("It challenges it: in a sealed container the total mass did not change; the missing mass left as gases.", "La contradice: en un recipiente cerrado la masa total no cambió; la masa que falta salió en forma de gases."), t("It supports it, because ashes are lighter.", "La apoya, porque las cenizas pesan menos."), t("It has nothing to do with it.", "No tiene relación con ella."), t("It proves that ashes have no mass.", "Demuestra que las cenizas no tienen masa.")], 0,
   {1: t("That is the observation Lavoisier explained another way.", "Esa es la observación que Lavoisier explicó de otro modo."), 2: t("It is exactly about that claim.", "Trata justamente de esa afirmación."), 3: t("Ashes do have mass.", "Las cenizas sí tienen masa.")},
   t("The claim only weighs the solid; Lavoisier weighed everything.", "La afirmación solo pesa el sólido; Lavoisier lo pesó todo."))}"""

    secciones = [
        ("s1", t("Physical change and chemical change", "Cambio físico y cambio químico"), s1),
        ("s2", t("How to read a chemical equation", "Cómo se lee una ecuación química"), s2),
        ("s3", t("Balancing: the same atoms out as in", "Equilibrar: que salgan los mismos átomos que entraron"), s3),
        ("s4", t("The four types of reaction", "Los cuatro tipos de reacción"), s4),
        ("s5", t("Thermochemistry: reactions that give heat and reactions that take it", "Termoquímica: reacciones que dan calor y reacciones que lo piden"), s5),
        ("s6", t("Science reading", "Lectura científica"), s6),
        ("s7", t("GED-style questions", "Preguntas tipo GED"), sG),
    ]
    tarea = [
        (t("Balance with coins.", "Equilibre con monedas."), t("Use coins or paper chips as atoms to balance three equations of the lesson before writing them. Then write the atom count for each element on both sides.", "Use monedas o fichas de papel como átomos para equilibrar tres ecuaciones de la lección antes de escribirlas. Después anote el recuento de cada elemento a los dos lados.")),
        (t("Hot or cold?", "¿Caliente o frío?"), t("Find two reactions at home (a match, a hand warmer, a cold pack, baking) and say whether each is exothermic or endothermic, and how you can tell.", "Busque dos reacciones en casa (un fósforo, un calientamanos, una compresa fría, hornear) y diga si cada una es exotérmica o endotérmica, y cómo lo sabe.")),
        (t("In your own words.", "Con sus palabras."), t("Write a short paragraph explaining why you cannot change the subscripts when balancing.", "Escriba un párrafo breve que explique por qué al equilibrar no pueden modificarse los subíndices.")),
    ]
    Q = t
    quiz = [
        (Q("When balancing a chemical equation, you change only…", "Al equilibrar una ecuación química se modifican únicamente…"), [Q("the subscripts", "los subíndices"), Q("the coefficients", "los coeficientes"), Q("the element symbols", "los símbolos de los elementos"), Q("the states in parentheses", "los estados entre paréntesis")], 1, {0: Q("That changes the substance.", "Eso cambia la sustancia."), 2: Q("That changes the elements.", "Eso cambia los elementos."), 3: Q("The states do not count atoms.", "Los estados no cuentan átomos.")}, Q("Only the coefficients.", "Solo los coeficientes.")),
        (Q(f"{f('N2 + 3 H2 → 2 NH3')} is balanced because each side has…", f"La ecuación {f('N2 + 3 H2 → 2 NH3')} está equilibrada porque a cada lado hay…"), [Q("2 N and 6 H", "2 átomos de N y 6 de H"), Q("1 N and 3 H", "1 átomo de N y 3 de H"), Q("2 N and 3 H", "2 átomos de N y 3 de H"), Q("3 N and 2 H", "3 átomos de N y 2 de H")], 0, {1: Q("Multiply by the coefficients.", "Multiplique por los coeficientes."), 2: Q("3 H₂ = 6 H.", "3 H₂ = 6 H."), 3: Q("Count each element.", "Cuente cada elemento.")}, Q("N₂ = 2 N; 3 H₂ = 6 H; 2 NH₃ = 2 N, 6 H.", "N₂ = 2 N; 3 H₂ = 6 H; 2 NH₃ = 2 N, 6 H.")),
        (Q(f"To balance {f('H2 + O2 → H2O')}, the coefficients are…", f"Para equilibrar {f('H2 + O2 → H2O')}, los coeficientes correctos son…"), ["1, 1, 1", "1, 2, 2", "2, 1, 2", "2, 2, 1"], 2, {0: Q("O: 2 against 1.", "O: 2 frente a 1."), 1: Q("O: 4 against 2.", "O: 4 frente a 2."), 3: Q("H: 4 against 2.", "H: 4 frente a 2.")}, Q("2 H₂ + O₂ → 2 H₂O: 4 H and 2 O each side.", "2 H₂ + O₂ → 2 H₂O: 4 H y 2 O a cada lado.")),
        (Q(f"4 {f('CO2')} contains in all…", f"La expresión 4 {f('CO2')} contiene en total…"), [Q("4 carbon and 4 oxygen atoms", "4 átomos de carbono y 4 de oxígeno"), Q("1 carbon and 2 oxygen atoms", "1 átomo de carbono y 2 de oxígeno"), Q("4 carbon and 2 oxygen atoms", "4 átomos de carbono y 2 de oxígeno"), Q("4 carbon and 8 oxygen atoms", "4 átomos de carbono y 8 de oxígeno")], 3, {0: Q("Each CO₂ has 2 O.", "Cada CO₂ tiene 2 O."), 1: Q("That is one molecule.", "Eso es una sola molécula."), 2: Q("Multiply the 2 by 4.", "Multiplique el 2 por 4.")}, Q("4 × 1 C = 4; 4 × 2 O = 8.", "4 × 1 C = 4; 4 × 2 O = 8.")),
        (Q("If the reactants have 10 hydrogen atoms, the products must have…", "Si en los reactivos hay 10 átomos de hidrógeno, en los productos debe haber…"), [Q("exactly 10", "exactamente 10"), Q("fewer than 10, because some is used up", "menos de 10, porque parte se consume"), Q("more than 10, because new substances form", "más de 10, porque se forman sustancias nuevas"), Q("any number, depending on the reaction", "cualquier cantidad, según la reacción")], 0, {1: Q("Atoms are not used up.", "Los átomos no se gastan."), 2: Q("Same atoms, rearranged.", "Mismos átomos, recolocados."), 3: Q("Conservation always holds.", "La conservación se cumple siempre.")}, Q("Conservation of matter.", "Conservación de la materia.")),
        (Q(f"The reaction {f('2 Na + Cl2 → 2 NaCl')} is…", f"La reacción {f('2 Na + Cl2 → 2 NaCl')} es de tipo…"), [Q("decomposition", "descomposición"), Q("synthesis", "síntesis"), Q("replacement", "sustitución"), Q("combustion", "combustión")], 1, {0: Q("Two go in, one comes out.", "Entran dos, sale uno."), 2: Q("Nothing is replaced.", "No se desplaza nada."), 3: Q("No fuel and no CO₂.", "No hay combustible ni CO₂.")}, Q("One product: synthesis.", "Un solo producto: síntesis.")),
        (Q("A reaction in which one substance turns into two or more is…", "Una reacción en la que una sola sustancia se transforma en dos o más se denomina…"), [Q("synthesis", "síntesis"), Q("combustion", "combustión"), Q("decomposition", "descomposición"), Q("replacement", "sustitución")], 2, {0: Q("That is the reverse.", "Eso es lo contrario."), 1: Q("Combustion needs O₂.", "La combustión necesita O₂."), 3: Q("Replacement swaps an element.", "La sustitución intercambia un elemento.")}, Q("One in, several out.", "Una entra, varias salen.")),
        (Q("A fuel reacts with oxygen and makes carbon dioxide and water. This reaction is…", "Un hidrocarburo reacciona con oxígeno y produce dióxido de carbono y agua. Esa reacción es de…"), [Q("decomposition", "descomposición"), Q("synthesis", "síntesis"), Q("replacement", "sustitución"), Q("combustion", "combustión")], 3, {0: Q("Two substances go in.", "Entran dos sustancias."), 1: Q("Two products come out.", "Salen dos productos."), 2: Q("O₂ + fuel → CO₂ + H₂O is the combustion pattern.", "O₂ + combustible → CO₂ + H₂O es el patrón de la combustión.")}, Q("Combustion.", "Combustión.")),
        (Q("In an energy diagram, the products are above the reactants. The reaction is…", "En un diagrama de energía, los productos están por encima de los reactivos. La reacción es…"), [Q("endothermic: it took energy from the surroundings", "endotérmica: ha absorbido energía del entorno"), Q("exothermic: it released energy", "exotérmica: ha liberado energía"), Q("impossible to classify", "imposible de clasificar sin más datos"), Q("a synthesis reaction", "una reacción de síntesis")], 0, {1: Q("That is products below.", "Eso es productos abajo."), 2: Q("The diagram is enough.", "El diagrama basta."), 3: Q("The diagram does not show the type.", "El diagrama no indica el tipo.")}, Q("Above: energy went in.", "Arriba: la energía entró.")),
        (Q("When two substances are mixed, the container feels cold. The reaction…", "Al mezclar dos sustancias, el recipiente se nota frío al tacto. Eso indica que la reacción…"), [Q("gives heat to the surroundings", "libera calor al entorno"), Q("takes heat from the surroundings", "absorbe calor del entorno"), Q("exchanges no energy", "no intercambia energía"), Q("is a combustion", "es una combustión")], 1, {0: Q("That would feel warm.", "Eso se notaría caliente."), 2: Q("Something got colder.", "Algo se enfrió."), 3: Q("Combustion is hot.", "La combustión es caliente.")}, Q("Cold = endothermic.", "Frío = endotérmica.")),
        (Q("Burning a fuel is a reaction that is…", "La combustión de un combustible es una reacción…"), [Q("endothermic, because it needs a spark", "endotérmica, porque necesita una chispa inicial"), Q("without energy exchange", "sin intercambio de energía"), Q("exothermic, because it gives off heat and light", "exotérmica, porque libera calor y luz al entorno"), Q("physical, not chemical", "física, no química")], 2, {0: Q("The spark only starts it; overall it gives off much more heat.", "La chispa solo la inicia; en conjunto libera mucho más calor."), 1: Q("It gives off heat.", "Libera calor."), 3: Q("New substances form.", "Se forman sustancias nuevas.")}, Q("Exothermic.", "Exotérmica.")),
        (Q("The key difference between exothermic and endothermic reactions is…", "La diferencia esencial entre una reacción exotérmica y una endotérmica está en…"), [Q("the number of reactants", "el número de reactivos que intervienen"), Q("the physical state of the products", "el estado físico de los productos"), Q("how fast it happens", "la velocidad a la que ocurre"), Q("whether energy goes out to the surroundings or comes in from them", "si la energía sale hacia el entorno o entra desde él")], 3, {0: Q("Not the number.", "No el número."), 1: Q("Not the state.", "No el estado."), 2: Q("Not the speed.", "No la velocidad.")}, Q("Exo- out, endo- in.", "Exo- fuera, endo- dentro.")),
    ]
    filas = [
        (t("Balance and check each element", "Equilibra y verifica cada elemento"), t("I balance, check every element, and leave elements found in several substances for last.", "Equilibro, verifico todos los elementos y dejo para el final los que aparecen en varias sustancias."), t("I count some elements but do not check the result.", "Cuento algunos elementos, pero no compruebo el resultado."), t("I change coefficients at random.", "Ajusto coeficientes al azar.")),
        (t("Respect conservation without touching subscripts", "Respeta la conservación sin tocar subíndices"), t("I change only coefficients and can explain why a subscript would make another substance.", "Ajusto solo coeficientes y explico por qué un subíndice crearía otra sustancia."), t("I know not to, but do it in hard cases.", "Sé que no debo, pero lo hago en casos difíciles."), t("I change subscripts to make it work.", "Cambio subíndices para que salgan las cuentas.")),
        (t("Classify the type of reaction", "Clasifica el tipo de reacción"), t("I classify all four and name the sign that decides it.", "Clasifico los cuatro tipos y nombro la señal que lo decide."), t("I know combustion but mix up synthesis and decomposition.", "Reconozco la combustión, pero confundo síntesis y descomposición."), t("I cannot tell the types apart.", "No distingo unos tipos de otros.")),
        (t("Tell exothermic from endothermic", "Distingue exotérmica de endotérmica"), t("I use the diagram, what I would feel, and an everyday example.", "Uso el diagrama, lo que percibiría al tacto y un ejemplo cotidiano."), t("I classify correctly but do not use the diagram.", "Clasifico bien, pero no uso el diagrama."), t("I think endothermic means hot.", "Creo que endotérmica significa caliente.")),
    ]
    cierre = "<p>" + t("This lesson closes Topic 5 and the first half of physical science. The three lessons moved up a scale: 5.1 the atom, 5.2 matter in bulk, and 5.3 transformation. One idea runs through all three: <strong>atoms are neither made nor destroyed</strong>. In 5.1 it explained why the number of protons defines the element; in 5.2, why a change of state does not change the substance; here, why every equation must be balanced.", "Con esta lección se cierra el Tema 5 y la primera mitad del dominio de Ciencias físicas. Las tres lecciones recorrieron una escala creciente: la 5.1 el átomo, la 5.2 la materia en cantidad y la 5.3 la transformación. Y una sola idea las atraviesa de principio a fin: <strong>los átomos ni se crean ni se destruyen</strong>. En la 5.1 explicaba por qué el número de protones define al elemento; en la 5.2, por qué un cambio de estado no altera la sustancia; aquí, por qué toda ecuación debe equilibrarse.") + "</p><p>" + \
             t("Topic 6, Physical science II, completes the area with force, motion, energy, and waves. The content changes again, but not the tools: rearranging formulas from 5.2 comes back with speed and work, and reading graphs is still the same skill as always.", "El Tema 6, Ciencias físicas II, completa el dominio con la fuerza, el movimiento, la energía y las ondas. Cambia otra vez el contenido, pero no las herramientas: allí volverá el despeje de fórmulas de la 5.2, ahora con la velocidad y el trabajo, y la lectura de gráficas seguirá siendo la misma destreza de siempre.") + "</p>"
    glosario = [
        (t("Physical / chemical change", "Cambio físico / químico"), t("Same substance, rearranged / new substances formed.", "La misma sustancia, reorganizada / se forman sustancias nuevas.")),
        (t("Reactant / product", "Reactivo / producto"), t("What goes into a reaction / what comes out.", "Lo que entra en una reacción / lo que sale.")),
        (t("Coefficient", "Coeficiente"), t("The large number in front of a formula: how many molecules.", "Número grande delante de una fórmula: cuántas moléculas.")),
        (t("Subscript", "Subíndice"), t("The small number after a symbol: how many atoms in the molecule.", "Número pequeño tras un símbolo: cuántos átomos hay en la molécula.")),
        (t("Conservation of matter", "Conservación de la materia"), t("In a reaction, atoms are neither made nor destroyed.", "En una reacción, los átomos ni se crean ni se destruyen.")),
        (t("Synthesis / decomposition", "Síntesis / descomposición"), t("Several substances become one / one becomes several.", "Varias sustancias se convierten en una / una se convierte en varias.")),
        (t("Replacement / combustion", "Sustitución / combustión"), t("One element takes another’s place / a fuel reacts with oxygen and gives off heat.", "Un elemento ocupa el lugar de otro / un combustible reacciona con oxígeno y libera calor.")),
        (t("Exothermic / endothermic", "Exotérmica / endotérmica"), t("Gives off heat (feels warm) / takes in heat (feels cold).", "Libera calor (se nota caliente) / absorbe calor (se nota frío).")),
    ]
    estd = C.estandares(["SP.6.b", "SP.7.a", "SP.1.c", "SP.3.b"], ["P.c", "P.a"], base=["SP.4.a"])
    conexion = "<p>" + t("Where we are: 5.1 explained why atoms join; 5.2 worked on what happens when they come closer or move apart without breaking. This lesson crosses the line: here bonds break and new ones form, and substances appear that did not exist before.", "Dónde estamos. La 5.1 explicó por qué los átomos se unen; la 5.2 trabajó lo que ocurre cuando se acercan o se separan sin romperse. Esta lección cruza la frontera: aquí los enlaces se rompen y se forman otros nuevos, y aparecen sustancias que antes no existían.") + "</p><p>" + \
               t("And one principle rules everything that follows, as simple to state as it is demanding to apply: in a chemical reaction, <strong>matter is neither made nor destroyed</strong>. The same atoms that go in come out, only rearranged. That is why equations must be balanced, the central skill of this lesson and one of the most tested in the area.", "Y hay un principio que gobierna todo lo que sigue, tan sencillo de enunciar como exigente de aplicar: en una reacción química <strong>no se crea ni se destruye materia</strong>. Los mismos átomos que entran son los que salen, solo que reorganizados. De ahí sale la obligación de equilibrar las ecuaciones, que es la destreza central de esta lección y una de las más evaluadas del dominio.") + "</p><p>" + \
               t("<strong>How to study this lesson:</strong> balance by counting atoms on both sides, first with chips and then with a pencil. What matters is seeing the atoms rearrange, not solving a math equation.", "<strong>Cómo estudiar esta lección:</strong> equilibre contando átomos a ambos lados, primero con las fichas y después con el lápiz. Lo importante es ver que los átomos se recolocan, no que se resuelve una ecuación matemática.") + "</p>"
    return C.pagina_leccion(N, titulo(),
        t("The same atoms go in and come out: read, balance, and classify reactions, and follow where the heat goes.", "Los mismos átomos entran y salen: leer, equilibrar y clasificar reacciones, y seguir adónde va el calor."),
        ["SP.6 · " + t("Expressing science information", "Expresar información científica"), "SP.7 · " + t("Scientific models", "Modelos científicos")],
        [t("<strong>Tell</strong> physical from chemical changes and recognize the signs of a reaction.", "<strong>Distinguir</strong> el cambio físico del químico y reconocer las señales de una reacción."),
         t("<strong>Read</strong> a chemical equation, telling coefficients from subscripts.", "<strong>Leer</strong> una ecuación química distinguiendo coeficientes de subíndices."),
         t("<strong>Balance</strong> equations by counting atoms, based on the conservation of matter.", "<strong>Equilibrar</strong> ecuaciones contando átomos, a partir de la conservación de la materia."),
         t("<strong>Classify</strong> reactions as synthesis, decomposition, replacement, or combustion.", "<strong>Clasificar</strong> reacciones en síntesis, descomposición, sustitución o combustión."),
         t("<strong>Tell</strong> exothermic from endothermic reactions using an energy diagram.", "<strong>Distinguir</strong> reacciones exotérmicas de endotérmicas con un diagrama de energía.")],
        estd, conexion, secciones, tarea, quiz, filas, cierre,
        (None, t("Next: Topic 6 · Physical science II: force, motion, energy, and waves (being written).", "Siguiente: Tema 6 · Ciencias físicas II: fuerza, movimiento, energía y ondas (en preparación).")), glosario, P)


# ---------------------------------------------------------------- práctica
ECS = [(["H2", "O2"], ["H2O"], (2, 1, 2)), (["N2", "H2"], ["NH3"], (1, 3, 2)), (["CH4", "O2"], ["CO2", "H2O"], (1, 2, 1, 2)), (["Na", "Cl2"], ["NaCl"], (2, 1, 2)),
       (["Mg", "O2"], ["MgO"], (2, 1, 2)), (["H2O2"], ["H2O", "O2"], (2, 2, 1)), (["Al", "O2"], ["Al2O3"], (4, 3, 2)), (["Fe", "O2"], ["Fe2O3"], (4, 3, 2)),
       (["C3H8", "O2"], ["CO2", "H2O"], (1, 5, 3, 4)), (["Zn", "HCl"], ["ZnCl2", "H2"], (1, 2, 1, 1)), (["KClO3"], ["KCl", "O2"], (2, 2, 3)), (["N2", "O2"], ["NO"], (1, 1, 2)),
       (["H2", "Cl2"], ["HCl"], (1, 1, 2)), (["Ca", "O2"], ["CaO"], (2, 1, 2)), (["C2H6", "O2"], ["CO2", "H2O"], (2, 7, 4, 6)), (["Li", "O2"], ["Li2O"], (4, 1, 2))]


def banco_equilibrar():
    rnd = random.Random(53)
    out = []
    for reac, prod, ok in ECS:
        assert equilibrada(reac, prod, ok), (reac, prod)
        cands = set()
        while len(cands) < 3:
            c = list(ok); i = rnd.randrange(len(c)); c[i] = max(1, c[i] + rnd.choice([-1, 1, 2]))
            c = tuple(c)
            if c != ok and not equilibrada(reac, prod, c):
                cands.add(c)
        ops = [", ".join(map(str, ok))] + [", ".join(map(str, c)) for c in cands]
        sin = ecuacion(reac, prod, [1] * (len(reac) + len(prod)))
        L, Rr = lado(reac, ok[:len(reac)]), lado(prod, ok[len(reac):])
        cuenta = "; ".join(f"{el}: {L[el]} = {Rr[el]}" for el in L)
        out.append({"enun": "<p>" + t("Which coefficients balance this equation? (in order, left to right)", "¿Qué coeficientes equilibran esta ecuación? (en orden, de izquierda a derecha)") + f"</p><p style='font-size:1.15em'><strong>{sin}</strong></p>",
                    "ops": ops, "ok": 0, "pista": t("Count each element on both sides with each option. Leave oxygen and hydrogen for last.", "Cuente cada elemento a los dos lados con cada opción. Deje el oxígeno y el hidrógeno para el final."),
                    "exp": f"<strong>{ecuacion(reac, prod, ok)}</strong>. " + t("Count: ", "Recuento: ") + cuenta + "."})
    return out


def contar_atomos():
    rnd = random.Random(54)
    forms = ["H2O", "CO2", "O2", "CH4", "NH3", "C6H12O6", "NaCl", "H2O2", "Al2O3", "C3H8", "Fe2O3", "CaCO3", "H2SO4", "C2H6"]
    nom = {"H": t("hydrogen", "hidrógeno"), "O": t("oxygen", "oxígeno"), "C": t("carbon", "carbono"), "N": t("nitrogen", "nitrógeno"), "Na": t("sodium", "sodio"), "Cl": t("chlorine", "cloro"),
           "Al": t("aluminum", "aluminio"), "Fe": t("iron", "hierro"), "Ca": t("calcium", "calcio"), "S": t("sulfur", "azufre")}
    out = []
    for _ in range(40):
        fo = rnd.choice(forms); k = rnd.choice([1, 2, 3, 4, 5, 6]); at = atomos(fo); el = rnd.choice(list(at))
        r = k * at[el]
        expr = (f"{k} " if k > 1 else "") + f(fo)
        out.append({"enun": "<p>" + t(f"How many <strong>{nom[el]}</strong> ({el}) atoms are in <strong>{expr}</strong>?", f"¿Cuántos átomos de <strong>{nom[el]}</strong> ({el}) hay en <strong>{expr}</strong>?") + "</p>",
                    "r": r, "exp": t(f"{k} × {at[el]} = {r}." if k > 1 else f"The subscript after {el} is {at[el]}." if at[el] > 1 else f"No subscript after {el} means 1.",
                                     f"{k} × {at[el]} = {r}." if k > 1 else f"El subíndice tras {el} es {at[el]}." if at[el] > 1 else f"Sin subíndice tras {el} significa 1.")})
    return out


def clasif_cambios():
    G = [t("Physical change", "Cambio físico"), t("Chemical change", "Cambio químico")]
    P = [t("Is it still the same substance?", "¿Sigue siendo la misma sustancia?"), t("Did a new substance form?", "¿Se formó una sustancia nueva?")]
    def item(tit, piezas):
        return {"titulo": tit, "intro": t("Is there a new substance? Decide for each change.", "¿Hay una sustancia nueva? Decida en cada cambio."), "grupos": G, "etiqueta": t("Change:", "Cambio:"),
                "piezas": [{"t": a, "v": v, "pista": P[v]} for a, v in piezas], "extra": t("The question is never “what do I see?” but “is it a new substance?”", "La pregunta nunca es «¿qué veo?», sino «¿es una sustancia nueva?».")}
    return [
        item(t("Set 1", "Grupo 1"), [(t("A nail rusts in the rain.", "Un clavo se oxida con la lluvia."), 1), (t("Sugar dissolves in coffee.", "El azúcar se disuelve en el café."), 0), (t("Bread is toasted until brown.", "El pan se tuesta hasta dorarse."), 1),
                                    (t("Water boils and bubbles.", "El agua hierve y hace burbujas."), 0), (t("Vinegar and baking soda fizz when mixed.", "El vinagre y el bicarbonato burbujean al mezclarlos."), 1)]),
        item(t("Set 2", "Grupo 2"), [(t("A glass breaks into pieces.", "Un vaso se rompe en pedazos."), 0), (t("Milk goes sour.", "La leche se agria."), 1), (t("Wood burns in a fireplace.", "La leña arde en la chimenea."), 1),
                                    (t("A puddle freezes.", "Un charco se congela."), 0), (t("Two clear liquids are mixed and a white solid appears.", "Se mezclan dos líquidos transparentes y aparece un sólido blanco."), 1)]),
    ]


def banco_tipos():
    O = [t("Synthesis", "Síntesis"), t("Decomposition", "Descomposición"), t("Replacement", "Sustitución"), t("Combustion", "Combustión")]
    d = [("2 Mg + O2 → 2 MgO", 0, t("Two in, one out.", "Entran dos, sale una.")), ("2 KClO3 → 2 KCl + 3 O2", 1, t("One in, two out.", "Entra una, salen dos.")),
         ("Fe + CuSO4 → FeSO4 + Cu", 2, t("Iron takes copper’s place.", "El hierro ocupa el lugar del cobre.")), ("C3H8 + 5 O2 → 3 CO2 + 4 H2O", 3, t("Fuel + O₂ → CO₂ + H₂O.", "Combustible + O₂ → CO₂ + H₂O.")),
         ("N2 + 3 H2 → 2 NH3", 0, t("Two in, one out.", "Entran dos, sale una.")), ("CaCO3 → CaO + CO2", 1, t("One in, two out.", "Entra una, salen dos.")),
         ("Zn + 2 HCl → ZnCl2 + H2", 2, t("Zinc takes hydrogen’s place.", "El cinc ocupa el lugar del hidrógeno.")), ("2 C2H6 + 7 O2 → 4 CO2 + 6 H2O", 3, t("Fuel + O₂ → CO₂ + H₂O.", "Combustible + O₂ → CO₂ + H₂O.")),
         ("2 H2O → 2 H2 + O2", 1, t("One in, two out.", "Entra una, salen dos.")), ("C6H12O6 + 6 O2 → 6 CO2 + 6 H2O", 3, t("Glucose burned with O₂: cellular respiration has the combustion pattern.", "La glucosa quemada con O₂: la respiración celular tiene el patrón de la combustión."))]
    return [{"enun": t("What type of reaction is this?", "¿Qué tipo de reacción es esta?") + f"<br><strong>{f(e)}</strong>", "ops": O, "ok": k, "enOrden": True,
             "pista": t("Count substances first: one on the left? one on the right? O₂ in and CO₂ + H₂O out?", "Cuente primero las sustancias: ¿una a la izquierda? ¿una a la derecha? ¿Entra O₂ y salen CO₂ y H₂O?"), "exp": f"<strong>{O[k]}.</strong> {x}"} for e, k, x in d]


def banco_energia():
    O = [t("Exothermic: gives off heat", "Exotérmica: libera calor"), t("Endothermic: takes in heat", "Endotérmica: absorbe calor")]
    d = [(t("A match burns.", "Un fósforo arde."), 0, t("Heat and light come out.", "Salen calor y luz.")), (t("An instant cold pack is squeezed and gets cold.", "Se aprieta una compresa fría instantánea y se enfría."), 1, t("Cold = heat goes in.", "Frío = entra calor.")),
         (t("A hand warmer heats up when opened (iron rusting fast).", "Un calientamanos se calienta al abrirlo (hierro que se oxida rápido)."), 0, t("It warms your hand.", "Le calienta la mano.")), (t("An egg is cooked in boiling water.", "Se cuece un huevo en agua hirviendo."), 1, t("It needs heat from outside the whole time.", "Necesita calor de fuera todo el tiempo.")),
         (t("Photosynthesis stores energy from light in glucose.", "La fotosíntesis almacena en la glucosa la energía de la luz."), 1, t("Energy goes in and is stored.", "La energía entra y se almacena.")), (t("Cement gets warm as it sets.", "El cemento se calienta al fraguar."), 0, t("Heat comes out.", "Sale calor.")),
         (t("In an energy diagram, the products are lower than the reactants.", "En un diagrama de energía, los productos están más abajo que los reactivos."), 0, t("Products below: energy released.", "Productos abajo: energía liberada.")),
         (t("In an energy diagram, the products are higher than the reactants.", "En un diagrama de energía, los productos están más arriba que los reactivos."), 1, t("Products above: energy absorbed.", "Productos arriba: energía absorbida.")),
         (t("A mixture’s temperature goes from 22 °C to 30 °C on its own.", "La temperatura de una mezcla pasa sola de 22 °C a 30 °C."), 0, t("It warmed up: heat came out of the reaction.", "Se calentó: salió calor de la reacción.")),
         (t("A mixture’s temperature goes from 22 °C to 12 °C on its own.", "La temperatura de una mezcla pasa sola de 22 °C a 12 °C."), 1, t("It cooled: the reaction took heat.", "Se enfrió: la reacción tomó calor."))]
    return [{"enun": t("Exothermic or endothermic?", "¿Exotérmica o endotérmica?") + f"<br><strong>{x}</strong>", "ops": O, "ok": k, "enOrden": True,
             "pista": t("Exo- = out (warm to the touch). Endo- = in (cold to the touch).", "Exo- = fuera (caliente al tacto). Endo- = dentro (frío al tacto)."), "exp": f"<strong>{O[k]}.</strong> {e}"} for x, k, e in d]


def practica():
    A = {"en": ["physical-chemical", "count", "balance", "types", "energy"], "es": ["fisico-quimico", "contar", "equilibrar", "tipos", "energia"]}[C.L]
    libre = "      <p>" + t("Coefficient × subscript. No subscript means 1.", "Coeficiente × subíndice. Sin subíndice significa 1.") + "</p>\n" + f'''      <div class="practica" id="m2">
        <div class="enun" id="m2-enun"></div>
        <div class="campos"><div class="campo"><label for="m2-r">{t("Answer", "Respuesta")}</label><input type="text" inputmode="numeric" autocomplete="off" class="ancho" id="m2-r"></div></div>
        <div class="fila-btn">
          <button type="button" class="btn" id="m2-comprobar">{t("Check", "Comprobar")}</button>
          <button type="button" class="btn-sec" id="m2-nuevo">{t("New exercise", "Otro ejercicio")}</button>
        </div>
        <div class="fb" id="m2-fb" role="status"></div>
        <p class="marcador" id="m2-marcador"></p>
      </div>'''
    mods = [
        (A[0], t("Physical or chemical?", "¿Físico o químico?"), C.clasifica("m1", t("Is there a new substance?", "¿Hay una sustancia nueva?"))),
        (A[1], t("Count atoms in formulas", "Cuente átomos en fórmulas"), libre),
        (A[2], t("Balance equations", "Equilibre ecuaciones"), C.om("m3", t("Sixteen equations. Count each element with each option.", "Dieciséis ecuaciones. Cuente cada elemento con cada opción."))),
        (A[3], t("Classify reactions", "Clasifique reacciones"), C.om("m4", t("Count substances before reading formulas.", "Cuente sustancias antes de leer fórmulas."))),
        (A[4], t("Exothermic or endothermic?", "¿Exotérmica o endotérmica?"), C.om("m5", t("Does the heat go out or come in?", "¿El calor sale o entra?"))),
    ]
    pista = t("Multiply the coefficient by the subscript of that element. No subscript means 1.", "Multiplique el coeficiente por el subíndice de ese elemento. Sin subíndice significa 1.")
    js = (C.js_datos("CAM", clasif_cambios()) + C.js_datos("ATO", contar_atomos()) + C.js_datos("EQU", banco_equilibrar()) + C.js_datos("TIP", banco_tipos()) + C.js_datos("ENE", banco_energia()) +
          f"var sacaA = mazo(ATO);\nfunction gA(){{ var q = sacaA(); return {{enun: q.enun, solucion: q.exp, evalua: numN(q.r, [], {C.json.dumps(pista, ensure_ascii=False)})}}; }}\n" +
          'creaClasifica("m1", CAM);\ncreaPracticaLibre("m2", gA);\ncreaBanco("m3", EQU);\ncreaBanco("m4", TIP);\ncreaBanco("m5", ENE);\n')
    return C.pagina_practica(N, titulo(), t("Five activities · new exercises every time · two tries in each one", "Cinco actividades · ejercicios nuevos cada vez · dos intentos en cada uno"), mods, js)


if __name__ == "__main__":
    C.construye(N, leccion, practica)
