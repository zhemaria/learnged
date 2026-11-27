"""LearnGED · Estudios sociales · Lección 3.1 · Del contrato social a la Declaración de Independencia (EN/ES).
Fuente: sociales/soc-3-1.html. Textos originales: Locke (1689), Montesquieu (trad. de Nugent, 1750) y la Declaración (1776).
Uso: python3 tools/build_soc_3_1.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sociales import C, t, documento, cita

N = "3-1"
F = 'font-family="Segoe UI, Arial, sans-serif"'
def hechos():
    return [
    (1763, t("Treaty of Paris ends the French and Indian War; Proclamation Line", "El Tratado de París cierra la guerra franco-india; Línea de Proclamación")),
    (1765, t("Stamp Act: a tax on printed paper, passed in London", "Ley del Timbre: un impuesto sobre el papel impreso, aprobado en Londres")),
    (1766, t("Stamp Act repealed; Declaratory Act claims full power over the colonies", "Se deroga la Ley del Timbre; la Ley Declaratoria reclama pleno poder sobre las colonias")),
    (1767, t("Townshend Acts: taxes on glass, paper, paint, and tea", "Leyes Townshend: impuestos sobre el vidrio, el papel, la pintura y el té")),
    (1770, t("Boston Massacre: British soldiers kill five colonists", "Masacre de Boston: soldados británicos matan a cinco colonos")),
    (1773, t("Tea Act and Boston Tea Party", "Ley del Té y Motín del Té de Boston")),
    (1774, t("Coercive (“Intolerable”) Acts close Boston’s port; First Continental Congress", "Leyes Coercitivas cierran el puerto de Boston; Primer Congreso Continental")),
    (1775, t("Fighting at Lexington and Concord: the war begins", "Combates de Lexington y Concord: empieza la guerra")),
    (1776, t("Declaration of Independence, July 4", "Declaración de Independencia, 4 de julio")),
    ]


def titulo():
    return t("From the social contract to the Declaration of Independence", "Del contrato social a la Declaración de Independencia")


def svg_linea():
    aria = t("Timeline from 1763 to 1776. ", "Línea de tiempo de 1763 a 1776. ") + " ".join(f"{a}: {h}." for a, h in hechos())
    X = lambda a: 60 + (a - 1763) / 13 * 600
    s = [f'<svg class="diagrama" style="max-width:720px" viewBox="0 0 720 470" role="img" aria-label="{aria}" xmlns="http://www.w3.org/2000/svg">',
         '<line x1="60" y1="40" x2="660" y2="40" stroke="#7a4a2e" stroke-width="4"/>']
    for a in range(1763, 1777):
        s.append(f'<line x1="{X(a):.0f}" y1="34" x2="{X(a):.0f}" y2="46" stroke="#7a4a2e" stroke-width="2"/>')
    s.append(f'<text x="60" y="24" text-anchor="middle" {F} font-size="13" font-weight="700" fill="#3e2a25">1763</text><text x="660" y="24" text-anchor="middle" {F} font-size="13" font-weight="700" fill="#3e2a25">1776</text>')
    for i, (a, h) in enumerate(hechos()):
        y = 78 + i * 44
        s.append(f'<circle cx="{X(a):.0f}" cy="40" r="6" fill="#7a4a2e"/>')
        s.append(f'<rect x="20" y="{y - 16}" width="680" height="34" rx="8" fill="#f6ede6"/>')
        s.append(f'<text x="34" y="{y + 6}" {F} font-size="15" font-weight="700" fill="#7a4a2e">{a}</text><text x="90" y="{y + 6}" {F} font-size="14" fill="#1a2330">{h}</text>')
    s.append("</svg>")
    return "".join(s)


def doc_locke():
    ficha = [(t("Author", "Autor"), "John Locke (1632–1704)"), (t("Work", "Obra"), t("<cite>Second Treatise of Government</cite>, 1689", "<cite>Segundo tratado sobre el gobierno civil</cite>, 1689")),
             (t("Kind of source", "Tipo de fuente"), t("Primary · political philosophy", "Primaria · filosofía política")), (t("Legal status", "Situación legal"), t("Public domain", "Dominio público"))]
    partes = [(t("Why people form a government · chapter IX, § 123", "Para qué se forma un gobierno · capítulo IX, § 123"),
               ["[Man] seeks out, and is willing to join in society with others, who are already united, or have a mind to unite, for the mutual preservation of their lives, liberties and estates, which I call by the general name, property."],
               ["[El hombre] busca y está dispuesto a unirse en sociedad con otros que ya están unidos, o que tienen intención de unirse, para la conservación mutua de sus vidas, sus libertades y sus bienes, cosas a las que doy el nombre general de propiedad."]),
              (t("What happens when a government goes past its purpose · chapter XIII, § 149", "Qué ocurre cuando un gobierno rebasa su fin · capítulo XIII, § 149"),
               ["All power given with trust for the attaining an end, being limited by that end, whenever that end is manifestly neglected, or opposed, the trust must necessarily be forfeited, and the power devolve into the hands of those that gave it, who may place it anew where they shall think best for their safety and security."],
               ["Todo poder concedido en confianza para alcanzar un fin está limitado por ese fin; y siempre que ese fin se descuide o se contraríe de manera manifiesta, la confianza se pierde necesariamente, y el poder vuelve a manos de quienes lo concedieron, que pueden colocarlo de nuevo donde crean mejor para su seguridad."])]
    return documento(t("Document A · John Locke", "Documento A · John Locke"), ficha, partes)


def doc_montesquieu():
    ficha = [(t("Author", "Autor"), "Charles de Montesquieu (1689–1755)"), (t("Work", "Obra"), t("<cite>The Spirit of the Laws</cite>, 1748, book XI. Written in French; English translation by Thomas Nugent, 1750.", "<cite>Del espíritu de las leyes</cite>, 1748, libro XI. Escrito en francés; la versión inglesa es la de Thomas Nugent, 1750.")),
             (t("Kind of source", "Tipo de fuente"), t("Primary · political philosophy", "Primaria · filosofía política")), (t("Legal status", "Situación legal"), t("Public domain", "Dominio público"))]
    partes = [(t("Why power must be divided · book XI, chapters 4 and 6", "Por qué hay que repartir el poder · libro XI, capítulos 4 y 6"),
               ["Constant experience shows us that every man invested with power is apt to abuse it. To prevent this abuse, it is necessary from the very nature of things that power should be a check to power.",
                "There would be an end of every thing, were the same man, or the same body, whether of the nobles or of the people, to exercise those three powers, that of enacting laws, that of executing the public resolutions, and of trying the causes of individuals."],
               ["Es una experiencia eterna que todo hombre que tiene poder tiende a abusar de él. Para que no se pueda abusar del poder, hace falta que, por la disposición de las cosas, el poder detenga al poder.",
                "Todo estaría perdido si un mismo hombre, o un mismo cuerpo, de nobles o del pueblo, ejerciera esos tres poderes: el de hacer las leyes, el de ejecutar las decisiones públicas y el de juzgar los delitos y los pleitos entre particulares."])]
    return documento(t("Document B · Montesquieu", "Documento B · Montesquieu"), ficha, partes)


PREAMBULO = ("We hold these truths to be self-evident, that all men are created equal, that they are endowed by their Creator with certain unalienable Rights, that among these are Life, Liberty and the pursuit of Happiness. — That to secure these rights, Governments are instituted among Men, deriving their just powers from the consent of the governed, — That whenever any Form of Government becomes destructive of these ends, it is the Right of the People to alter or to abolish it, and to institute new Government.",
             "Sostenemos como evidentes estas verdades: que todos los hombres son creados iguales; que son dotados por su Creador de ciertos derechos inalienables; que entre estos están la vida, la libertad y la búsqueda de la felicidad; que para garantizar estos derechos se instituyen entre los hombres los gobiernos, que derivan sus poderes legítimos del consentimiento de los gobernados; que cuando quiera que una forma de gobierno se haga destructora de estos fines, es derecho del pueblo reformarla o abolirla e instituir un nuevo gobierno.")
AGRAVIOS = [
    (1, "He has refused his Assent to Laws, the most wholesome and necessary for the public good.", "Se ha negado a dar su asentimiento a las leyes más saludables y necesarias para el bien público.", 1),
    (9, "He has made Judges dependent on his Will alone, for the tenure of their offices, and the amount and payment of their salaries.", "Ha hecho que los jueces dependan solo de su voluntad en cuanto a la duración de sus cargos y a la cuantía y el pago de sus salarios.", 0),
    (17, "For imposing Taxes on us without our Consent.", "Por imponernos contribuciones sin nuestro consentimiento.", 0),
    (24, "He has plundered our seas, ravaged our Coasts, burnt our towns, and destroyed the lives of our people.", "Ha saqueado nuestros mares, asolado nuestras costas, incendiado nuestras ciudades y destruido la vida de nuestro pueblo.", 2),
    (25, "He is at this time transporting large Armies of foreign Mercenaries to compleat the works of death, desolation and tyranny, already begun with circumstances of Cruelty & perfidy scarcely paralleled in the most barbarous ages.", "Está transportando en este momento grandes ejércitos de mercenarios extranjeros para completar la obra de muerte, desolación y tiranía ya iniciada, con circunstancias de crueldad y perfidia apenas igualadas en las épocas más bárbaras.", 2),
]


def leccion():
    P = C.Practicas()
    s1 = f"""<p>{t("In 1776 nobody invented anything new in the world of ideas. The Declaration applies a theory that had been going around for almost a century, and it is worth knowing it before reading the document, because the document takes it for granted.", "En 1776 nadie inventó nada nuevo en el terreno de las ideas. La Declaración aplica una teoría que llevaba casi un siglo circulando, y conviene conocerla antes de leer el documento, porque el documento la da por sabida.")}</p>
<p>{t("The question it tried to answer was this: <strong>why should anyone obey a government?</strong> The old answer was that the king ruled by the will of God, and disobeying him was disobeying God. The new answer turns that order around. People exist before government and have rights because they exist. Government is an agreement those people make to protect those rights, and its authority comes from there and from nowhere else. That is the <strong>social contract</strong>.", "La pregunta que intentaba responder era esta: <strong>¿por qué tendría alguien que obedecer a un gobierno?</strong> La respuesta antigua era que el rey gobernaba por voluntad divina, y desobedecerlo era desobedecer a Dios. La respuesta nueva invierte el orden. Las personas existen antes que el gobierno y tienen derechos por el hecho de existir. El gobierno es un acuerdo que esas personas hacen para proteger esos derechos, y su autoridad viene de ahí y de ningún otro sitio. Eso es el <strong>contrato social</strong>.")}</p>
<p>{t("Two consequences follow, and in 1776 they were explosive: the power of government has a limit, which is the purpose it was created for; and if it goes past that limit again and again, the people who made the agreement can undo it.", "De ahí se siguen dos consecuencias que en 1776 eran explosivas: el poder del gobierno tiene un límite, que es el fin para el que se creó; y si lo rebasa una y otra vez, quienes hicieron el acuerdo pueden deshacerlo.")}</p>
{doc_locke()}
<p>{t("Montesquieu adds the practical part. If Locke says what government is for, Montesquieu asks how to build one that does not end up abusing its power.", "Montesquieu añade la parte práctica. Si Locke dice para qué existe el gobierno, Montesquieu se pregunta cómo se construye uno que no acabe abusando de su poder.")}</p>
{doc_montesquieu()}
{C.caja("tip", t("How the work is split between the two", "Cómo se reparten el trabajo los dos"), "<p>" + t("Locke answers why we obey and when the duty to obey ends. Montesquieu answers how to organize a government so that moment never comes. <strong>The Declaration of 1776 uses Locke; the Constitution of 1787, which you will see in Lesson 3.2, uses Montesquieu.</strong>", "Locke responde por qué obedecemos y cuándo deja de haber obligación de hacerlo. Montesquieu responde cómo se organiza un gobierno para que ese momento no llegue. <strong>La Declaración de 1776 usa a Locke; la Constitución de 1787, que verá en la Lección 3.2, usa a Montesquieu.</strong>") + "</p>")}
{P(t("Practice 1 · The social contract", "Práctica 1 · El contrato social"), t("According to the social contract, where does a government’s authority come from?", "Según la teoría del contrato social, ¿de dónde viene la autoridad de un gobierno?"),
   [t("From the will of God", "De la voluntad divina"), t("From tradition and age", "De la tradición y la antigüedad"), t("From the consent of the governed", "Del consentimiento de los gobernados")], 2,
   {0: t("That is the old answer the theory replaced.", "Esa es la respuesta antigua que la teoría sustituyó."), 1: t("Locke grounds authority in an agreement, not in custom.", "Locke funda la autoridad en un acuerdo, no en la costumbre.")}, t("The people make the agreement, so the authority comes from them.", "El pueblo hace el acuerdo, así que la autoridad viene de él."))}
{P(t("Practice 2 · Montesquieu", "Práctica 2 · Montesquieu"), t("What does Montesquieu add to what Locke said?", "¿Qué añade Montesquieu a lo que ya decía Locke?"),
   [t("That rights are natural", "Que los derechos son naturales"), t("How to organize government so that “power should be a check to power”", "Cómo organizar el gobierno para que «el poder detenga al poder»"), t("That the king rules by the will of God", "Que el rey gobierna por voluntad divina")], 1,
   {0: t("That was already Locke’s idea.", "Esa idea ya era de Locke."), 2: t("Both of them reject that.", "Los dos lo rechazan.")}, t("Separating the three powers so that none can rule alone.", "Separar los tres poderes para que ninguno pueda mandar solo."))}"""

    s2 = f"""<p>{t("In 1763 the colonists celebrated a British victory in a war they had fought on the British side. Thirteen years later they declared independence. What happened in between explains the grievances.", "En 1763 los colonos celebraban una victoria británica en una guerra en la que habían combatido del lado británico. Trece años después declaraban la independencia. Lo que pasó en medio explica los agravios.")}</p>
{svg_linea()}
{C.caja("tip", t("The slogan that sums up the conflict", "La consigna que resume el conflicto"), "<p>" + t("The war left Britain with a huge debt and new land to defend, and Parliament decided the colonies should help pay, with taxes passed in London and not in the colonial assemblies. <strong>“No taxation without representation”</strong> was not a complaint about the amount of money. It was a complaint about <em>who decides</em>. The colonists had no seats in the Parliament that taxed them, and they held that a tax is legitimate only if the representatives of those who pay it approve it. That principle is the social contract applied to a tax bill.", "La guerra dejó a Gran Bretaña con una deuda enorme y un territorio nuevo que defender, y el Parlamento decidió que las colonias ayudaran a pagarlo, con impuestos aprobados en Londres y no en las asambleas coloniales. <strong>«Ningún impuesto sin representación»</strong> no era una queja sobre la cantidad de dinero. Era una queja sobre <em>quién decide</em>. Los colonos no tenían escaños en el Parlamento que les cobraba, y sostenían que un impuesto solo es legítimo si lo aprueban los representantes de quien lo paga. Ese principio es el contrato social aplicado a un recibo.") + "</p>")}
{C.enlace(N, t("timeline", "cronologia"), t("Put the events in order", "Ordene los hechos"), t("Rebuild the chain from 1763 to 1776.", "Reconstruya la cadena de 1763 a 1776."))}"""

    s3 = f"""<p>{t("The Declaration is not an emotional outburst, even if it sounds like one when read aloud. It is an argument shaped like a court case, built in three parts that do three different jobs.", "La Declaración no es una proclama emocional, aunque lo parezca al leerla en voz alta. Es un argumento con forma de expediente judicial, construido en tres partes que hacen tres trabajos distintos.")}</p>
{C.tabla(t("The three parts of the Declaration and what each one does", "Las tres partes de la Declaración y qué hace cada una"), [t("Part", "Parte"), t("What it contains", "Qué contiene"), t("Its job", "Qué función cumple")],
  [[t("1 · Philosophical premise", "1 · Premisa filosófica"), t("The first two paragraphs. A general theory of government. It does not mention Britain.", "Los dos primeros párrafos. Una teoría general del gobierno. No menciona a Gran Bretaña."), t("Set the rule by which the king will be judged. A reader who accepts it is already half convinced.", "Fijar la regla con la que se va a juzgar. Si el lector la acepta, ya está medio convencido.")],
   [t("2 · The grievances", "2 · Los agravios"), t("Twenty-seven charges against the king, most of them starting with the same words: “He has…”", "Veintisiete cargos contra el rey, casi todos encabezados con la misma fórmula: «Ha…»."), t("Supply the facts that, under the rule, allow the contract to be broken.", "Aportar los hechos que, según esa regla, autorizan a romper el contrato.")],
   [t("3 · Conclusion", "3 · Conclusión"), t("The final paragraph: the declaration itself.", "El párrafo final: la declaración propiamente dicha."), t("Draw the consequence: if the rule holds and the facts are true, separation is legitimate.", "Sacar la consecuencia: si la regla vale y los hechos son ciertos, la separación es legítima.")]])}
{documento(t("The premise of the Declaration of Independence", "La premisa de la Declaración de Independencia"),
   [(t("Document", "Documento"), t("Declaration of Independence, second paragraph", "Declaración de Independencia, segundo párrafo")), (t("Date", "Fecha"), t("July 4, 1776", "4 de julio de 1776")), (t("Main author", "Autor principal"), t("Thomas Jefferson, for a committee of the Second Continental Congress", "Thomas Jefferson, por encargo de una comisión del Segundo Congreso Continental")), (t("Kind of source", "Tipo de fuente"), t("Primary · founding document", "Primaria · documento fundacional"))],
   [("", [PREAMBULO[0]], [PREAMBULO[1]])])}
<p>{t("Notice the order. The premise comes first, and that is no accident: it makes the reader accept the standard before seeing the facts it will be applied to. Right after the premise, the text says: <em>“To prove this, let Facts be submitted to a candid world.”</em> With that sentence the Declaration stops talking like one side in a quarrel and starts talking like a prosecutor presenting evidence. Its audience is not only the king: it is Europe, and especially France, from which an alliance was hoped for.", "Fíjese en el orden. La premisa va primero, y eso no es casual: obliga al lector a aceptar el criterio antes de conocer los hechos que se van a medir con él. Justo después de la premisa, el texto dice: <em>«Para probar esto, sométanse los hechos al juicio de un mundo imparcial»</em>. Con esa frase la Declaración deja de hablar como un bando en una disputa y empieza a hablar como un fiscal que presenta pruebas. Su destinatario no es solo el rey: es Europa, y en particular Francia, de la que se esperaba una alianza.")}</p>"""

    V, R, M = t("Verifiable", "Verificable"), t("Rhetorical, as written", "Retórico, tal como está redactado"), t("In between: real facts, words chosen for effect", "Zona intermedia: hechos reales, palabras elegidas para impresionar")
    agr = "".join(f'<li value="{n}"><span lang="en">{en}</span>' + (f'<br><em>{es}</em>' if C.L == "es" else "") + "</li>" for n, en, es, k in AGRAVIOS)
    s4 = f"""<p>{t("This is the central work of the lesson, and it is exactly the work of Lesson 1.2: separating what a document supports from what it only seems to support.", "Este es el trabajo central de la lección, y es exactamente el de la Lección 1.2: separar lo que un documento sostiene de lo que solo parece sostener.")}</p>
<p>{t("A grievance is <strong>verifiable</strong> if a historian could, in principle, look up the fact and check it: a specific law, a date, an appointment, a ship. It is <strong>rhetorical</strong> if it accuses in terms that point to no checkable fact, or if the effect it seeks is emotional rather than evidence-based.", "Un agravio es <strong>verificable</strong> si un historiador podría, en principio, buscar el hecho y comprobarlo: una ley concreta, una fecha, un nombramiento, un barco. Es <strong>retórico</strong> si acusa en términos que no señalan ningún hecho comprobable, o si el efecto que busca es emocional antes que probatorio.")}</p>
{C.caja("ojo", t("Rhetorical does not mean false", "Retórico no significa falso"), "<p>" + t("It means that, as written, it cannot be checked. Many rhetorical grievances describe something real; the document just does not give the fact that would let you check it. The difference is in the form of the charge, not in whether it is true.", "Significa que, tal como está redactado, no se puede comprobar. Muchos agravios retóricos describen algo real; el documento simplemente no da el dato que permitiría verificarlo. La distinción está en la forma de la acusación, no en su verdad.") + "</p>")}
<p>{t("Five of the twenty-seven grievances, in the original English" + "", "Cinco de los veintisiete agravios, en el inglés original y en traducción del curso") }:</p>
<ol class="agravios">{agr}</ol>
<p class="nota">{t("The numbers follow the usual count of 27 grievances; some editions group them differently.", "La numeración sigue la cuenta habitual de 27 agravios; algunas ediciones los agrupan de otra manera.")}</p>
{P(t("Practice 3 · Grievance 9", "Práctica 3 · Agravio 9"), t("Grievance 9, about judges who depend on the king’s will for their jobs and salaries, is…", "El agravio 9, sobre los jueces que dependen de la voluntad del rey para su cargo y su salario, es…"), [V, R, M], 0,
   {1: t("Could a historian check who paid colonial judges and who could remove them?", "¿Podría un historiador comprobar quién pagaba a los jueces coloniales y quién podía destituirlos?"), 2: t("The wording is plain and points to a specific arrangement.", "La redacción es sobria y señala un arreglo concreto.")}, t("It points to a concrete arrangement that can be checked in the records.", "Señala un arreglo concreto que se puede comprobar en los registros."))}
{P(t("Practice 4 · Grievance 1", "Práctica 4 · Agravio 1"), t("Grievance 1, about refusing to approve the laws “most wholesome and necessary for the public good,” is…", "El agravio 1, sobre negarse a aprobar las leyes «más saludables y necesarias para el bien público», es…"), [V, R, M], 1,
   {0: t("Which laws? “Most wholesome” is a judgment.", "¿Qué leyes? «Más saludables» es un juicio."), 2: t("It names no fact at all to check.", "No nombra ningún hecho que comprobar.")}, t("As written, it names no law. It may describe something real, but the text gives nothing to check.", "Tal como está redactado, no nombra ninguna ley. Puede describir algo real, pero el texto no da nada que comprobar."))}
{P(t("Practice 5 · Grievance 25", "Práctica 5 · Agravio 25"), t("Grievance 25, about “large Armies of foreign Mercenaries,” is…", "El agravio 25, sobre «grandes ejércitos de mercenarios extranjeros», es…"), [V, R, M], 2,
   {0: t("There is a checkable fact, but look at the rest of the sentence.", "Hay un hecho comprobable, pero mire el resto de la frase."), 1: t("Britain really did hire German soldiers (the Hessians).", "Gran Bretaña sí contrató soldados alemanes (los hessianos).")}, t("Britain did hire German troops: a checkable fact. “Scarcely paralleled in the most barbarous ages” is wording chosen for effect.", "Gran Bretaña contrató tropas alemanas: un hecho comprobable. «Apenas igualadas en las épocas más bárbaras» es una redacción elegida para impresionar."))}
{C.enlace(N, t("grievances", "agravios"), t("Verifiable or rhetorical?", "¿Verificable o retórico?"), t("More grievances from the Declaration to classify.", "Más agravios de la Declaración para clasificar."))}"""

    s5 = f"""<p>{t("Put side by side, the borrowing is easy to see. So is the change.", "Puestos uno al lado del otro, el préstamo se ve solo. Y también se ve el cambio.")}</p>
{C.tabla(t("What Locke says and what the Declaration says", "Qué dice Locke y qué dice la Declaración"), ["Locke, 1689", t("Declaration, 1776", "Declaración, 1776")],
  [[t("People unite “for the mutual preservation of their lives, liberties and estates.”", "Los hombres se unen «para la conservación mutua de sus vidas, sus libertades y sus bienes»."), t("Among the unalienable rights “are Life, Liberty and the pursuit of Happiness.”", "Entre los derechos inalienables «están la vida, la libertad y la búsqueda de la felicidad».")],
   [t("When the trust is betrayed, power returns “into the hands of those that gave it.”", "Cuando se traiciona la confianza, el poder vuelve «a manos de quienes lo concedieron»."), t("“It is the Right of the People to alter or to abolish it.”", "«Es derecho del pueblo reformarla o abolirla».")],
   [t("Power is given “for the attaining an end” and is “limited by that end.”", "El poder se concede «para alcanzar un fin» y está «limitado por ese fin»."), t("Governments derive “their just powers from the consent of the governed.”", "Los gobiernos derivan «sus poderes legítimos del consentimiento de los gobernados».")]], fila_th=False)}
{C.caja("ojo", t("One word changed", "Una palabra cambiada"), "<p>" + t("Where Locke wrote <em>estates</em> (property), the Declaration wrote <em>the pursuit of Happiness</em>. People have argued about that change for two and a half centuries, and they do not agree. Some see a generous widening; others, a way to avoid committing to property at an awkward moment. The lesson does not need to settle it: it needs you to notice that someone changed a word on purpose, and to ask why.", "Donde Locke escribía <em>estates</em> (bienes, propiedad), la Declaración escribe <em>the pursuit of Happiness</em> (la búsqueda de la felicidad). Sobre ese cambio se discute desde hace dos siglos y medio, y no hay acuerdo. Unos ven una ampliación generosa; otros, una manera de no comprometerse con la propiedad en un momento incómodo. La lección no necesita resolverlo: necesita que usted note que alguien cambió una palabra a propósito, y que se pregunte por qué.") + "</p>")}
<h3>{t("Political vocabulary the test takes for granted", "Vocabulario político que el examen da por sabido")}</h3>
{C.tabla(t("Four words", "Cuatro palabras"), [t("Word", "Palabra"), t("Meaning", "Significado")],
  [[t("Sovereignty", "Soberanía"), t("The final authority to decide in a territory, the one that answers to no other. In 1776 the question was where it lay: in the king and Parliament, or in the people of the colonies.", "La autoridad última para decidir en un territorio, la que no responde ante ninguna otra. En 1776 la cuestión era dónde residía: en el rey y el Parlamento, o en el pueblo de las colonias.")],
   [t("Tyranny", "Tiranía"), t("Power used beyond the limits it was given for, to benefit the ruler and not the governed. It does not just mean cruelty: it means power without a legitimate limit.", "El ejercicio del poder fuera de los límites para los que se concedió, en beneficio de quien manda y no de los gobernados. No significa solo crueldad: significa poder sin límite legítimo.")],
   [t("Consent", "Consentimiento"), t("The agreement of the governed, the only thing that turns command into legitimate authority. It can be given through representatives, which is why taxes were the flash point.", "El acuerdo de los gobernados, lo único que convierte el mando en autoridad legítima. Puede darse por medio de representantes, y por eso los impuestos fueron el punto de ruptura.")],
   [t("Unalienable", "Inalienable"), t("That cannot be transferred, sold, or taken away. An unalienable right is not a permit the government gives: the government finds it already there. (The Declaration spells it <em>unalienable</em>.)", "Que no se puede transferir, vender ni retirar. Un derecho inalienable no es un permiso que da el gobierno: el gobierno lo encuentra ya puesto. (La Declaración lo escribe <em>unalienable</em>).")]])}"""

    G = lambda *a: C.ged_item(P, *a)
    sG = "<p>" + t("These questions work like the ones on the GED® Social Studies test. Each one shows the social studies practice it checks and its depth of knowledge (DOK).",
                   "Estas preguntas funcionan como las del examen de Estudios Sociales del GED®. Cada una indica la práctica de estudios sociales que evalúa y su profundidad de conocimiento (DOK).") + f"""</p>
{G(1, "SSP.4.a", "2", cita(t("“…deriving their just powers from the consent of the governed…”", "«…que derivan sus poderes legítimos del consentimiento de los gobernados…»"), t("Declaration of Independence, 1776", "Declaración de Independencia, 1776")) +
   t("In this phrase, “just powers” means powers that are…", "En esta frase, «poderes legítimos» (<em>just powers</em>) significa poderes que son…"),
   [t("rightful, because the people agreed to them", "justificados, porque el pueblo los aceptó"), t("small and limited in number", "pocos y limitados en número"), t("fair to every person in the same way", "igual de justos para todas las personas"), t("held only by judges", "propios solo de los jueces")], 0,
   {1: t("“Just” here is not about size.", "«Just» aquí no tiene que ver con el tamaño."), 2: t("The phrase is about where power comes from.", "La frase trata de dónde viene el poder."), 3: t("It is about all government.", "Se refiere a todo gobierno.")},
   t("Powers are legitimate (“just”) because they come from the consent of the governed.", "Los poderes son legítimos («just») porque vienen del consentimiento de los gobernados."))}
{G(2, "SSP.3.c", "2", t("<em>Look at the timeline in section 2.</em><br>Which event most directly led colonists to protest “taxation without representation”?", "<em>Observe la línea de tiempo de la sección 2.</em><br>¿Qué hecho llevó más directamente a los colonos a protestar contra los «impuestos sin representación»?"),
   [t("The Stamp Act of 1765", "La Ley del Timbre de 1765"), t("The battles of Lexington and Concord", "Los combates de Lexington y Concord"), t("The Treaty of Paris of 1763", "El Tratado de París de 1763"), t("The Declaration of Independence", "La Declaración de Independencia")], 0,
   {1: t("That was armed conflict, years later.", "Eso fue un conflicto armado, años después."), 2: t("The treaty ended a war; the taxes came after.", "El tratado cerró una guerra; los impuestos vinieron después."), 3: t("That was the result, not the cause.", "Eso fue el resultado, no la causa.")},
   t("The Stamp Act was a tax passed in London on the colonies, which had no representatives there.", "La Ley del Timbre fue un impuesto aprobado en Londres sobre las colonias, que no tenían representantes allí."))}
{G(3, "SSP.5.a", "2–3", cita(t("“He has plundered our seas, ravaged our Coasts, burnt our towns, and destroyed the lives of our people.”", "«Ha saqueado nuestros mares, asolado nuestras costas, incendiado nuestras ciudades y destruido la vida de nuestro pueblo»."), t("Declaration of Independence, grievance 24", "Declaración de Independencia, agravio 24")) +
   t("Why does the author list four violent verbs in a row?", "¿Por qué el autor pone cuatro verbos violentos seguidos?"),
   [t("To build a strong emotional effect against the king", "Para crear un fuerte efecto emocional contra el rey"), t("To give the exact number of towns burned", "Para dar el número exacto de ciudades incendiadas"), t("To show the colonists were neutral", "Para mostrar que los colonos eran neutrales"), t("To list laws passed by Parliament", "Para enumerar leyes aprobadas por el Parlamento")], 0,
   {1: t("No numbers are given.", "No se da ninguna cifra."), 2: t("The whole document takes a side.", "Todo el documento toma partido."), 3: t("These are acts of war, not laws.", "Son actos de guerra, no leyes.")},
   t("The events were real, but the piled-up verbs are chosen for effect: loaded language (Lesson 1.3).", "Los hechos fueron reales, pero la acumulación de verbos busca el efecto: lenguaje cargado (Lección 1.3)."))}
{G(4, "SSP.1.a", "2", cita(t("“To prevent this abuse, it is necessary from the very nature of things that power should be a check to power.”", "«Para que no se pueda abusar del poder, hace falta que, por la disposición de las cosas, el poder detenga al poder»."), t("Montesquieu, <cite>The Spirit of the Laws</cite>, 1748", "Montesquieu, <cite>Del espíritu de las leyes</cite>, 1748")) +
   t("Which feature of the U.S. Constitution best reflects this idea?", "¿Qué rasgo de la Constitución de los Estados Unidos refleja mejor esta idea?"),
   [t("Each branch of government can limit the others.", "Cada rama del gobierno puede limitar a las otras."), t("The president is elected every four years.", "El presidente se elige cada cuatro años."), t("The Constitution can be amended.", "La Constitución se puede enmendar."), t("Congress can collect taxes.", "El Congreso puede cobrar impuestos.")], 0,
   {1: t("Elections check power through voters, but the quote is about power checking power.", "Las elecciones controlan el poder por medio de los votantes, pero la cita habla de un poder que frena a otro."), 2: t("That is about changing the rules.", "Eso trata de cambiar las reglas."), 3: t("That is a power, not a check.", "Eso es un poder, no un freno.")},
   t("Checks and balances: power stops power.", "Controles y equilibrios: el poder detiene al poder."))}"""

    secciones = [
        ("s1", t("The idea before the document", "La idea antes del documento"), s1),
        ("s2", t("Thirteen years, from allies to enemies", "Trece años, de aliados a enemigos"), s2),
        ("s3", t("The anatomy of an argument", "Anatomía de un argumento"), s3),
        ("s4", t("Verifiable grievance or rhetoric?", "¿Agravio verificable o recurso retórico?"), s4),
        ("s5", t("The sentences that come from Locke", "Las frases que vienen de Locke"), s5),
        ("s6", t("GED-style questions", "Preguntas tipo GED"), sG),
    ]
    tarea = [
        (t("The three parts (20 minutes).", "Las tres partes (20 minutos)."), t("Read the full Declaration (it fits on two pages; it is at the National Archives, archives.gov). Mark where the premise ends and where the conclusion begins. <em>Check:</em> the premise ends with “let Facts be submitted to a candid world”; the conclusion begins “We, therefore, the Representatives…”.", "Lea la Declaración completa (cabe en dos páginas; está en el sitio de los Archivos Nacionales, archives.gov). Marque dónde termina la premisa y dónde empieza la conclusión. <em>Compruebe:</em> la premisa termina con «sométanse los hechos al juicio de un mundo imparcial»; la conclusión empieza «Nosotros, por tanto, los representantes…».")),
        (t("Ten grievances (30 minutes).", "Diez agravios (30 minutos)."), t("Choose ten grievances and classify each one as verifiable, rhetorical, or in between. For each verifiable one, write what document a historian would look for. <em>Check:</em> if every one came out “verifiable” or every one “rhetorical,” read again: the document mixes both on purpose.", "Elija diez agravios y clasifique cada uno como verificable, retórico o intermedio. Para cada verificable, escriba qué documento buscaría un historiador. <em>Compruebe:</em> si todos le salieron «verificables» o todos «retóricos», vuelva a leer: el documento mezcla los dos a propósito.")),
        (t("Your own declaration (30 minutes).", "Su propia declaración (30 minutos)."), t("Write a short “declaration” about a problem in your community with the same three parts: a general rule, three facts (at least two verifiable), and a conclusion. <em>Check:</em> a reader who disagrees with you should still be able to check your facts.", "Escriba una «declaración» breve sobre un problema de su comunidad con las mismas tres partes: una regla general, tres hechos (al menos dos verificables) y una conclusión. <em>Compruebe:</em> alguien que no esté de acuerdo con usted debería poder comprobar sus hechos.")),
    ]
    Q = t
    quiz = [
        (Q("According to the social contract, a government’s authority comes from…", "Según el contrato social, la autoridad de un gobierno viene de…"), [Q("God", "Dios"), Q("tradition", "la tradición"), Q("the consent of the governed", "el consentimiento de los gobernados"), Q("the army", "el ejército")], 2,
         {0: Q("That is the old theory.", "Esa es la teoría antigua."), 1: Q("Not according to Locke.", "No según Locke."), 3: Q("Force is not authority.", "La fuerza no es autoridad.")}, Q("The people agree to it.", "El pueblo lo acuerda.")),
        (Q("For Locke, what happens when a government goes against the purpose it was created for?", "Para Locke, ¿qué ocurre cuando un gobierno va contra el fin para el que se creó?"), [Q("Power returns to the people, who can place it anew", "El poder vuelve al pueblo, que puede colocarlo de nuevo"), Q("Nothing: it must be obeyed", "Nada: hay que obedecerlo"), Q("The king chooses a new government", "El rey elige un gobierno nuevo"), Q("The courts take over", "Los tribunales toman el mando")], 0,
         {1: Q("Locke says the trust is “forfeited.”", "Locke dice que la confianza «se pierde»."), 2: Q("The king is the problem here.", "El rey es aquí el problema."), 3: Q("Locke does not say that.", "Locke no dice eso.")}, Q("The trust is forfeited.", "La confianza se pierde.")),
        (Q("Montesquieu’s main idea is that…", "La idea central de Montesquieu es que…"), [Q("power should be divided so it can check itself", "el poder debe dividirse para que se frene a sí mismo"), Q("kings rule by divine right", "los reyes gobiernan por derecho divino"), Q("taxes need representation", "los impuestos necesitan representación"), Q("property is the main right", "la propiedad es el derecho principal")], 0,
         {1: Q("He opposes that.", "Él se opone a eso."), 2: Q("That is the colonists’ slogan.", "Esa es la consigna de los colonos."), 3: Q("That is closer to Locke.", "Eso se acerca más a Locke.")}, Q("Power should be a check to power.", "El poder debe detener al poder.")),
        (Q("“No taxation without representation” was a complaint about…", "«Ningún impuesto sin representación» era una queja sobre…"), [Q("the amount of the taxes", "la cantidad de los impuestos"), Q("who decides the taxes", "quién decide los impuestos"), Q("taxes on tea only", "los impuestos solo sobre el té"), Q("the price of stamps", "el precio de los sellos")], 1,
         {0: Q("Some taxes were actually small.", "Algunos impuestos eran en realidad pequeños."), 2: Q("It was about all taxes from London.", "Se refería a todos los impuestos de Londres."), 3: Q("The Stamp Act taxed paper, but the slogan is about principle.", "La Ley del Timbre gravaba el papel, pero la consigna es de principio.")}, Q("Consent through one’s own representatives.", "El consentimiento por medio de los propios representantes.")),
        (Q("Which came first?", "¿Qué ocurrió primero?"), [Q("The Stamp Act", "La Ley del Timbre"), Q("The Boston Tea Party", "El Motín del Té"), Q("Lexington and Concord", "Lexington y Concord"), Q("The Coercive Acts", "Las Leyes Coercitivas")], 0,
         {1: Q("1773.", "1773."), 2: Q("1775.", "1775."), 3: Q("1774.", "1774.")}, Q("1765.", "1765.")),
        (Q("The first part of the Declaration (the premise)…", "La primera parte de la Declaración (la premisa)…"), [Q("lists the king’s crimes", "enumera los delitos del rey"), Q("sets out a general theory of government without naming Britain", "expone una teoría general del gobierno sin nombrar a Gran Bretaña"), Q("declares war on France", "declara la guerra a Francia"), Q("creates the three branches", "crea las tres ramas")], 1,
         {0: Q("That is part 2.", "Eso es la parte 2."), 2: Q("France was a hoped-for ally.", "Francia era un aliado esperado."), 3: Q("That is the Constitution.", "Eso es la Constitución.")}, Q("It sets the rule first.", "Fija primero la regla.")),
        (Q("Why does the premise come before the grievances?", "¿Por qué la premisa va antes que los agravios?"), [Q("So the reader accepts the standard before seeing the facts", "Para que el lector acepte el criterio antes de ver los hechos"), Q("By chance", "Por casualidad"), Q("Because the grievances were written later", "Porque los agravios se escribieron después"), Q("To make the document shorter", "Para que el documento sea más corto")], 0,
         {1: Q("The structure is deliberate.", "La estructura es deliberada."), 2: Q("Order of writing is not the point.", "El orden de redacción no es la cuestión."), 3: Q("It is about persuasion.", "Se trata de persuasión.")}, Q("Like a prosecutor: first the law, then the evidence.", "Como un fiscal: primero la ley, después las pruebas.")),
        (Q("A grievance is “verifiable” when…", "Un agravio es «verificable» cuando…"), [Q("it is true", "es cierto"), Q("a historian could look up the fact and check it", "un historiador podría buscar el hecho y comprobarlo"), Q("it uses strong words", "usa palabras fuertes"), Q("the king admitted it", "el rey lo admitió")], 1,
         {0: Q("Rhetorical grievances can be true too.", "Los agravios retóricos también pueden ser ciertos."), 2: Q("Strong words point to rhetoric.", "Las palabras fuertes apuntan a la retórica."), 3: Q("That is not the test.", "Esa no es la prueba.")}, Q("It points to a checkable fact.", "Señala un hecho comprobable.")),
        (Q("“For imposing Taxes on us without our Consent” is…", "«Por imponernos contribuciones sin nuestro consentimiento» es…"), [Q("verifiable: the tax laws can be found", "verificable: las leyes de impuestos se pueden encontrar"), Q("purely rhetorical", "puramente retórico"), Q("false", "falso"), Q("an opinion", "una opinión")], 0,
         {1: Q("The Stamp Act and Townshend Acts exist.", "La Ley del Timbre y las Leyes Townshend existen."), 2: Q("The taxes were real.", "Los impuestos fueron reales."), 3: Q("It points to laws.", "Señala leyes.")}, Q("Specific laws can be checked.", "Hay leyes concretas que se pueden comprobar.")),
        (Q("Where Locke wrote “estates,” the Declaration wrote…", "Donde Locke escribió «bienes», la Declaración escribió…"), [Q("“property”", "«propiedad»"), Q("“the pursuit of Happiness”", "«la búsqueda de la felicidad»"), Q("“taxes”", "«impuestos»"), Q("“independence”", "«independencia»")], 1,
         {0: Q("That is what Locke meant; the Declaration changed it.", "Eso es lo que quería decir Locke; la Declaración lo cambió."), 2: Q("Not in that list of rights.", "No en esa lista de derechos."), 3: Q("Not in that list.", "No en esa lista.")}, Q("Life, Liberty and the pursuit of Happiness.", "La vida, la libertad y la búsqueda de la felicidad.")),
        (Q("“Unalienable” rights are rights that…", "Los derechos «inalienables» son derechos que…"), [Q("the government gives", "da el gobierno"), Q("cannot be taken away or given up", "no se pueden quitar ni ceder"), Q("only citizens have", "solo tienen los ciudadanos"), Q("can be sold", "se pueden vender")], 1,
         {0: Q("The government finds them already there.", "El gobierno los encuentra ya puestos."), 2: Q("The Declaration says “all men.”", "La Declaración dice «todos los hombres»."), 3: Q("The opposite.", "Lo contrario.")}, Q("Not transferable, not removable.", "Ni transferibles ni retirables.")),
        (Q("“Sovereignty” means…", "«Soberanía» significa…"), [Q("the final authority to decide in a territory", "la autoridad última para decidir en un territorio"), Q("a tax on paper", "un impuesto sobre el papel"), Q("a type of army", "un tipo de ejército"), Q("a court decision", "una sentencia")], 0,
         {1: Q("That is the Stamp Act.", "Eso es la Ley del Timbre."), 2: Q("Not related.", "No tiene relación."), 3: Q("Not related.", "No tiene relación.")}, Q("The authority that answers to no other.", "La autoridad que no responde ante ninguna otra.")),
    ]
    filas = [
        (t("Explain the social contract", "Explica el contrato social"), t("I explain where authority comes from, its limit, and what follows when it is broken, quoting Locke.", "Explico de dónde viene la autoridad, cuál es su límite y qué se sigue cuando se rompe, citando a Locke."), t("I know authority comes from the people but cannot say what follows.", "Sé que la autoridad viene del pueblo, pero no qué se sigue de ello."), t("I confuse it with the divine right of kings (<a href=\"#s1\">review section 1</a>).", "Lo confundo con el derecho divino de los reyes (<a href=\"#s1\">repase la sección 1</a>).")),
        (t("Order the causes", "Ordena las causas"), t("I put the events of 1763–1776 in order and explain how each led to the next.", "Ordeno los hechos de 1763 a 1776 y explico cómo cada uno llevó al siguiente."), t("I know the events but mix up their order.", "Conozco los hechos, pero confundo el orden."), t("I do not know why the colonies broke with Britain (<a href=\"#s2\">review section 2</a>).", "No sé por qué rompieron las colonias con Gran Bretaña (<a href=\"#s2\">repase la sección 2</a>).")),
        (t("Analyze the argument", "Analiza el argumento"), t("I name the three parts, their jobs, and why the premise comes first.", "Nombro las tres partes, su función y por qué la premisa va primero."), t("I see the parts but not why they are in that order.", "Veo las partes, pero no por qué van en ese orden."), t("I read it as a list of complaints (<a href=\"#s3\">review section 3</a>).", "La leo como una lista de quejas (<a href=\"#s3\">repase la sección 3</a>).")),
        (t("Tell verifiable from rhetorical", "Distingue lo verificable de lo retórico"), t("I classify grievances, name the record that would check each verifiable one, and know rhetorical ≠ false.", "Clasifico agravios, nombro el registro que comprobaría cada verificable y sé que retórico ≠ falso."), t("I classify the clear cases but call rhetorical ones false.", "Clasifico los casos claros, pero llamo falsos a los retóricos."), t("I treat every grievance as a proven fact (<a href=\"#s4\">review section 4</a>).", "Trato cada agravio como un hecho probado (<a href=\"#s4\">repase la sección 4</a>).")),
    ]
    cierre = "<p>" + t("This lesson read the founding document as Topic 1 taught: an argument with a structure, a purpose, and an audience, made of facts that can be checked and words chosen to move. The Declaration explained <em>why</em> to break with a government. It did not say how to build the next one.",
                         "Esta lección leyó el documento fundacional como enseñó el Tema 1: un argumento con estructura, propósito y destinatario, hecho de hechos comprobables y de palabras elegidas para conmover. La Declaración explicó <em>por qué</em> romper con un gobierno. No dijo cómo construir el siguiente.") + "</p><p>" + \
             t("Lesson 3.2 answers that with the Constitution of 1787: its structure, its five principles, and the great argument over whether to ratify it, between the Federalists and the Anti-Federalists.", "La Lección 3.2 lo responde con la Constitución de 1787: su estructura, sus cinco principios y la gran discusión sobre si ratificarla, entre federalistas y antifederalistas.") + "</p>"
    glosario = [
        (t("Social contract", "Contrato social"), t("The theory that government is an agreement among people to protect their rights, and gets its authority from their consent.", "Teoría según la cual el gobierno es un acuerdo entre las personas para proteger sus derechos, y obtiene su autoridad de su consentimiento.")),
        (t("Natural rights", "Derechos naturales"), t("Rights people have because they exist, before any government (life, liberty, property).", "Derechos que se tienen por existir, antes de cualquier gobierno (vida, libertad, propiedad).")),
        (t("Separation of powers", "Separación de poderes"), t("Dividing the power to make, carry out, and judge the laws among different bodies.", "Repartir entre órganos distintos el poder de hacer, ejecutar y juzgar las leyes.")),
        (t("Grievance", "Agravio"), t("A formal complaint about a wrong; the Declaration lists 27 against the king.", "Queja formal por una injusticia; la Declaración enumera 27 contra el rey.")),
        (t("Sovereignty", "Soberanía"), t("The final authority to decide in a territory.", "La autoridad última para decidir en un territorio.")),
        (t("Tyranny", "Tiranía"), t("Power used beyond its legitimate limits, for the ruler’s benefit.", "Poder ejercido fuera de sus límites legítimos, en beneficio de quien manda.")),
        (t("Unalienable", "Inalienable"), t("That cannot be taken away or given up.", "Que no se puede quitar ni ceder.")),
    ]
    estd = C.estandares(["SSP.1.a", "SSP.4.a", "SSP.5.a", "SSP.7.b"], ["USH.a", "USH.b", "CG.b"], base=["SSP.3.a", "SSP.3.c"])
    conexion = "<p>" + t("Topics 1 and 2 built the tools: questioning a source, telling what it supports from what it only suggests, spotting bias, and reading numbers. Topic 3 uses those tools on the founding documents of the United States. The GED test asks more about civics and government than about anything else (about half of the questions), and almost always with a document in front of you.",
                         "Los Temas 1 y 2 construyeron las herramientas: interrogar una fuente, separar lo que sostiene de lo que solo sugiere, detectar el sesgo y leer números. El Tema 3 las aplica a los documentos fundacionales de los Estados Unidos. El examen del GED pregunta más sobre educación cívica y gobierno que sobre cualquier otra cosa (cerca de la mitad de las preguntas), y casi siempre con un documento delante.") + "</p><p>" + \
               t("This lesson does not ask you to memorize the Declaration. It asks you to read it the way a historian does: where its ideas came from, how its argument is built, and which of its charges can be checked.", "Esta lección no le pide memorizar la Declaración. Le pide leerla como lo hace un historiador: de dónde vienen sus ideas, cómo está construido su argumento y cuáles de sus acusaciones se pueden comprobar.") + "</p>"
    return C.pagina_leccion(N, titulo(),
        t("The Declaration of Independence is an argument built like a court case, on an idea that was almost a century old.", "La Declaración de Independencia es un argumento construido como un expediente judicial, sobre una idea que tenía casi un siglo."),
        ["SSP.1 · " + t("Reading founding documents", "Leer documentos fundacionales"), "SSP.4 · " + t("Political vocabulary", "Vocabulario político"), "SSP.5 · " + t("Purpose and rhetoric", "Propósito y retórica")],
        [t("<strong>Explain</strong> the social contract and the separation of powers, with Locke’s and Montesquieu’s own words.", "<strong>Explicar</strong> el contrato social y la separación de poderes, con las palabras de Locke y de Montesquieu."),
         t("<strong>Put in order</strong> the events from 1763 to 1776 and explain how they led to independence.", "<strong>Ordenar</strong> los hechos de 1763 a 1776 y explicar cómo llevaron a la independencia."),
         t("<strong>Analyze</strong> the three-part structure of the Declaration and the job of each part.", "<strong>Analizar</strong> la estructura en tres partes de la Declaración y la función de cada una."),
         t("<strong>Tell apart</strong> a verifiable grievance from a rhetorical one, and use the political vocabulary the test expects.", "<strong>Distinguir</strong> un agravio verificable de uno retórico, y usar el vocabulario político que el examen da por sabido.")],
        estd, conexion, secciones, tarea, quiz, filas, cierre,
        ("3-2", t("The Constitution: structure and principles", "La Constitución: estructura y principios")), glosario, P)


# ---------------------------------------------------------------- la práctica
def banco_quien():
    L_, M_, D_ = "Locke", "Montesquieu", t("A defender of the divine right of kings", "Un defensor del derecho divino de los reyes")
    datos = [
        (t("“People join together to protect their lives, liberties, and property.”", "«Las personas se unen para proteger sus vidas, sus libertades y sus bienes»."), 0),
        (t("“If one person makes the laws, carries them out, and judges them, all is lost.”", "«Si una misma persona hace las leyes, las ejecuta y las juzga, todo está perdido»."), 1),
        (t("“The king answers to God alone; resisting him is a sin.”", "«El rey solo responde ante Dios; resistirle es pecado»."), 2),
        (t("“When rulers betray the trust placed in them, power returns to the people.”", "«Cuando los gobernantes traicionan la confianza depositada en ellos, el poder vuelve al pueblo»."), 0),
        (t("“Every person with power tends to abuse it, so power must stop power.”", "«Todo el que tiene poder tiende a abusar de él, así que el poder debe detener al poder»."), 1),
        (t("“Subjects have no right to judge their king.”", "«Los súbditos no tienen derecho a juzgar a su rey»."), 2),
        (t("“Government exists for a purpose, and that purpose is its limit.”", "«El gobierno existe para un fin, y ese fin es su límite»."), 0),
        (t("“Judges must be separate from those who make the laws.”", "«Los jueces deben estar separados de quienes hacen las leyes»."), 1),
    ]
    ops = [L_, M_, D_]
    return [{"enun": t("Who would most likely say this?", "¿Quién diría esto con más probabilidad?") + "<br><strong>" + s + "</strong>", "ops": ops, "ok": k, "exp": f"<strong>{ops[k]}.</strong>", "enOrden": True} for s, k in datos]


def banco_agravios():
    V, R, M = t("Verifiable", "Verificable"), t("Rhetorical, as written", "Retórico, tal como está redactado"), t("In between", "Zona intermedia")
    datos = AGRAVIOS + [
        (11, "He has kept among us, in times of peace, Standing Armies without the Consent of our legislatures.", "Ha mantenido entre nosotros, en tiempos de paz, ejércitos permanentes sin el consentimiento de nuestras asambleas.", 0),
        (14, "For quartering large bodies of armed troops among us.", "Por alojar grandes cuerpos de tropas armadas entre nosotros.", 0),
        (16, "For cutting off our Trade with all parts of the world.", "Por cortar nuestro comercio con todas las partes del mundo.", 2),
        (18, "For depriving us in many cases, of the benefits of Trial by Jury.", "Por privarnos en muchos casos de los beneficios del juicio por jurado.", 0),
        (10, "He has erected a multitude of New Offices, and sent hither swarms of Officers to harrass our people, and eat out their substance.", "Ha creado una multitud de cargos nuevos y ha enviado aquí enjambres de funcionarios para hostigar a nuestro pueblo y devorar su sustento.", 2),
        (2, "He has forbidden his Governors to pass Laws of immediate and pressing importance.", "Ha prohibido a sus gobernadores aprobar leyes de importancia inmediata y apremiante.", 1),
    ]
    exp = {0: t("It points to a specific, checkable fact: a law, a practice, or a decision that can be looked up.", "Señala un hecho concreto y comprobable: una ley, una práctica o una decisión que se puede buscar."),
           1: t("As written, it names no specific law or event that could be checked; “most wholesome” or “pressing importance” are judgments.", "Tal como está redactado, no nombra ninguna ley ni suceso concreto que se pueda comprobar; «más saludables» o «importancia apremiante» son juicios."),
           2: t("There is a real fact underneath, but the wording (“all parts of the world,” “swarms,” “eat out their substance,” “barbarous ages”) is chosen for effect.", "Hay un hecho real debajo, pero la redacción («todas las partes del mundo», «enjambres», «devorar su sustento», «épocas bárbaras») está elegida para impresionar.")}
    ops = [V, R, M]
    return [{"enun": t("Grievance", "Agravio") + f" {n}: <strong lang=\"en\">“{en}”</strong>" + (f"<br><em>{es}</em>" if C.L == "es" else "") + "<br>" + t("How is it written?", "¿Cómo está redactado?"),
             "ops": ops, "ok": k, "exp": f"<strong>{ops[k]}.</strong> " + exp[k], "enOrden": True} for n, en, es, k in datos]


def casos_orden():
    def caso(tit, idx):
        pasos = [hechos()[i][1] for i in idx]
        import random
        r = random.Random(sum(idx))
        ini = list(range(len(idx)))
        while ini == sorted(ini):
            r.shuffle(ini)
        return {"titulo": tit, "intro": t("Put the events in the order they happened, using ▲ and ▼.", "Ponga los hechos en el orden en que ocurrieron, con ▲ y ▼."), "pasos": pasos, "inicio": ini, "cons": {},
                "general": t("Dates: ", "Fechas: ") + ", ".join(str(hechos()[i][0]) for i in idx) + "."}
    return [caso(t("From the war to the first taxes", "De la guerra a los primeros impuestos"), [0, 1, 2, 3, 4]),
            caso(t("From the taxes to the war", "De los impuestos a la guerra"), [3, 4, 5, 6, 7, 8]),
            caso(t("The whole chain", "La cadena completa"), [0, 1, 4, 5, 6, 7, 8])]


def banco_vocab():
    datos = [
        (t("“The colonists argued that only their own assemblies could tax them, since Parliament had no right to rule them without their ______.”", "«Los colonos sostenían que solo sus propias asambleas podían cobrarles impuestos, porque el Parlamento no tenía derecho a gobernarlos sin su ______»."), [t("consent", "consentimiento"), t("sovereignty", "soberanía"), t("tyranny", "tiranía")], t("Consent: their agreement, through representatives.", "Consentimiento: su acuerdo, por medio de representantes.")),
        (t("“A ruler who uses power beyond its legitimate limits, for his own benefit, is practicing ______.”", "«Un gobernante que usa el poder más allá de sus límites legítimos, en su propio beneficio, practica la ______»."), [t("tyranny", "tiranía"), t("consent", "consentimiento"), t("representation", "representación")], t("Tyranny: power without a legitimate limit.", "Tiranía: poder sin límite legítimo.")),
        (t("“The question in 1776 was where ______ lay: in the king and Parliament, or in the people.”", "«La cuestión en 1776 era dónde residía la ______: en el rey y el Parlamento, o en el pueblo»."), [t("sovereignty", "soberanía"), t("liberty", "libertad"), t("property", "propiedad")], t("Sovereignty: the final authority to decide.", "Soberanía: la autoridad última para decidir.")),
        (t("“A right that the government cannot take away, and that a person cannot sell or give up, is ______.”", "«Un derecho que el gobierno no puede quitar, y que una persona no puede vender ni ceder, es ______»."), [t("unalienable", "inalienable"), t("delegated", "delegado"), t("verifiable", "verificable")], t("Unalienable: not transferable, not removable.", "Inalienable: ni transferible ni retirable.")),
        (t("“Locke used the word ______ to mean, all together, a person’s life, liberty, and estate.”", "«Locke usó la palabra ______ para referirse, en conjunto, a la vida, la libertad y los bienes de una persona»."), [t("property", "propiedad"), t("happiness", "felicidad"), t("sovereignty", "soberanía")], t("“…which I call by the general name, property.”", "«…a lo que doy el nombre general de propiedad».")),
        (t("“A formal complaint about a wrong, like each of the 27 charges against the king, is a ______.”", "«Una queja formal por una injusticia, como cada uno de los 27 cargos contra el rey, es un ______»."), [t("grievance", "agravio"), t("premise", "premisa"), t("treaty", "tratado")], t("Grievance: a charge of wrongdoing.", "Agravio: una acusación de injusticia.")),
    ]
    return [{"enun": t("Choose the word that completes the sentence:", "Elija la palabra que completa la frase:") + "<br><strong>" + s + "</strong>", "ops": ops, "ok": 0, "exp": e} for s, ops, e in datos]


def practica():
    A = {"en": ["who", "grievances", "timeline", "words"], "es": ["quien", "agravios", "cronologia", "palabras"]}[C.L]
    mods = [
        (A[0], t("Locke, Montesquieu, or the king?", "¿Locke, Montesquieu o el rey?"), C.om("m1", t("Locke: why we obey and when the duty ends. Montesquieu: dividing power so it checks itself. The divine right of kings: authority comes from God.", "Locke: por qué obedecemos y cuándo termina la obligación. Montesquieu: repartir el poder para que se frene a sí mismo. El derecho divino: la autoridad viene de Dios."))),
        (A[1], t("Verifiable or rhetorical?", "¿Verificable o retórico?"), C.om("m2", t("Ask: could a historian look up a specific fact? Remember: rhetorical does not mean false.", "Pregúntese: ¿podría un historiador buscar un hecho concreto? Recuerde: retórico no significa falso."))),
        (A[2], t("Put the events in order", "Ordene los hechos"), C.orden("m3")),
        (A[3], t("Political vocabulary", "Vocabulario político"), C.om("m4", t("Choose the word that fits the sentence.", "Elija la palabra que encaja en la frase."))),
    ]
    js = (C.js_datos("QUI", banco_quien()) + C.js_datos("AGR", banco_agravios()) + C.js_datos("ORD", casos_orden()) + C.js_datos("VOC", banco_vocab()) +
          'creaBanco("m1", QUI);\ncreaBanco("m2", AGR);\ncreaOrden("m3", ORD);\ncreaBanco("m4", VOC);\n')
    return C.pagina_practica(N, titulo(), t("Four activities · the order of the exercises changes every time · two tries in each one", "Cuatro actividades · el orden de los ejercicios cambia cada vez · dos intentos en cada uno"), mods, js)


if __name__ == "__main__":
    C.construye(N, leccion, practica)
