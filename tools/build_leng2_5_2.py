# -*- coding: utf-8 -*-
"""LearnGED · Artes del lenguaje (español) · Nivel 2 · Lección 5.2 · Vocabulario por contexto: pistas, afijos y raíces.
Fuente: clases_leng2/clase_5-2.html (GEDparaHispanos) y gramatica/n2-l5-2.html, adaptadas al marco de LearnGED.
Uso: python3 tools/build_leng2_5_2.py
"""
import os, sys, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import leng_es as LE
from leng_es import C

LE.nivel(2)
N = "5-2"
PISTAS = [("El doctor le recetó un [analgésico], es decir, un medicamento para calmar el dolor.", ["Un medicamento contra el dolor", "Un examen de sangre completo", "Una dieta especial para adelgazar"], "Definición: «es decir»."),
          ("Mi vecino es muy [generoso]; siempre comparte lo que tiene con los demás.", ["Que da y comparte con gusto", "Que habla mucho con todos", "Que vive solo en su casa"], "Sentido general: comparte lo que tiene."),
          ("El primer apartamento era [amplio], pero el segundo era muy pequeño.", ["Grande, con mucho espacio", "Caro, con un alquiler alto", "Viejo, con muchos años"], "Contraste: «pero… muy pequeño»."),
          ("En la tienda venden [herramientas], como martillos, serruchos y destornilladores.", ["Instrumentos para trabajar", "Ropa para el trabajo", "Materiales de limpieza"], "Ejemplo: martillos, serruchos, destornilladores."),
          ("Estaba [perplejo]: tan confundido que no sabía qué decir.", ["Muy confundido", "Muy enojado", "Muy cansado"], "Sinónimo: «tan confundido»."),
          ("El accidente fue [leve]; nadie se lastimó y los carros solo tuvieron rayones.", ["Sin gravedad", "Muy grave", "Muy rápido"], "Sentido general: nadie se lastimó."),
          ("Por la sequía, el río estaba casi [seco]; en cambio, el año pasado venía muy crecido.", ["Sin agua", "Muy sucio", "Muy hondo"], "Contraste con «crecido»."),
          ("Mi hija es [bilingüe]: habla español e inglés desde pequeña.", ["Que habla dos idiomas", "Que estudia mucho", "Que vive en dos países"], "Definición después de los dos puntos."),
          ("Le dieron un [reembolso], o sea, le devolvieron el dinero del producto dañado.", ["La devolución del dinero", "Un descuento para la próxima compra", "Una multa por el daño"], "Definición: «o sea»."),
          ("El examen fue [agotador]; después de cuatro horas, todos salimos sin energía.", ["Que cansa mucho", "Que es muy fácil", "Que es muy corto"], "Sentido general: sin energía."),
          ("Prefiere los colores [vivos], como el rojo, el amarillo y el naranja.", ["Fuertes y brillantes", "Oscuros y tristes", "Claros y suaves"], "Ejemplo: rojo, amarillo, naranja."),
          ("El discurso fue [breve]: duró solo tres minutos.", ["Corto", "Aburrido", "Importante"], "Definición: «duró solo tres minutos»."),
          ("El niño era muy [tímido]; su hermana, por el contrario, hablaba con todo el mundo.", ["Que le cuesta hablar con otros", "Que hace muchas travesuras", "Que tiene mucha energía"], "Contraste: «por el contrario, hablaba con todo el mundo»."),
          ("Hay que [desinfectar] la herida, es decir, limpiarla para que no se infecte.", ["Limpiar para evitar una infección", "Cubrir con una venda limpia", "Dejar que se seque sola al aire"], "Definición: «es decir».")]
AFIJOS = [("La carretera quedó [intransitable] por la nieve.", ["No se podía pasar por ella", "Estaba recién pavimentada", "Tenía muchísimo tráfico"], "in- (no) + transitar (pasar) + -able (que se puede)."),
          ("Hay que [reutilizar] las bolsas del mercado.", ["Volver a usar", "Tirar a la basura", "Comprar nuevas"], "re- (otra vez) + utilizar."),
          ("El [panadero] del barrio empieza a trabajar a las tres.", ["La persona que hace pan", "El dueño del edificio", "El cartero del barrio"], "Familia de pan; -ero, quien hace o vende."),
          ("Con el frío, sus mejillas empezaron a [enrojecer].", ["Ponerse rojas", "Ponerse pálidas", "Secarse mucho"], "Familia de rojo."),
          ("Las instrucciones eran [incomprensibles]; nadie supo armar el mueble.", ["Que no se pueden entender", "Muy largas y aburridas", "Muy fáciles de seguir"], "in- (no) + comprender + -ble (que se puede)."),
          ("Mi tía es una gran [cocinera].", ["Persona que cocina", "Persona que limpia", "Persona que vende"], "Familia de cocinar; -era, quien hace la acción."),
          ("Antes de pintar, hay que [desarmar] la cama.", ["Separar sus piezas", "Limpiarla bien", "Moverla de lugar"], "des- (lo contrario) + armar."),
          ("El agua del lago era muy [cristalina].", ["Clara y transparente", "Fría y salada", "Sucia y oscura"], "Familia de cristal: como el cristal."),
          ("Es un trabajo [peligrosísimo].", ["Extremadamente peligroso", "Un poco peligroso", "Nada peligroso"], "peligroso + -ísimo (muchísimo)."),
          ("Hay que [actualizar] la aplicación del teléfono.", ["Ponerla al día", "Borrarla", "Comprarla"], "Familia de actual: hacer que esté al día."),
          ("El tanque de gasolina lleva un letrero de [inflamable].", ["Que se quema con facilidad", "Que no se puede quemar", "Que ya está vacío"], "Aquí in- no niega: el contexto (gasolina) lo confirma."),
          ("El [ensordecedor] ruido de la fábrica no lo dejaba pensar.", ["Tan fuerte que deja sordo", "Muy suave y lejano", "Agradable de escuchar"], "Familia de sordo: que ensordece.")]
ENTRADAS = {"planta": ["Ser vivo que crece en la tierra, como un árbol o una flor.", "Fábrica o instalación industrial.", "Cada uno de los pisos de un edificio.", "Parte de abajo del pie."],
            "carta": ["Papel escrito que se envía a otra persona.", "Cada uno de los naipes de una baraja.", "Lista de comidas y bebidas de un restaurante."],
            "sierra": ["Herramienta con dientes para cortar madera.", "Cadena de montañas."],
            "cola": ["Extremo del cuerpo de algunos animales.", "Fila de personas que esperan su turno.", "Pegamento."],
            "sobre": ["Cubierta de papel en la que se mete una carta.", "Encima de algo.", "Acerca de, hablando de un tema."]}
ACEP = [("planta", "Mi esposo trabaja en una planta de automóviles.", 1), ("planta", "Le duele la planta del pie derecho.", 3), ("planta", "Riega la planta de la cocina dos veces por semana.", 0),
        ("planta", "La oficina está en la tercera planta del edificio.", 2), ("carta", "El mesero nos trajo la carta para elegir la comida.", 2), ("carta", "Recibí una carta de mi abuela desde Honduras.", 0),
        ("carta", "Le tocó la mejor carta del juego.", 1), ("sierra", "Cortó la tabla con una sierra eléctrica.", 0), ("sierra", "Los fines de semana suben a la sierra a caminar.", 1),
        ("cola", "Había una cola larguísima para entrar al concierto.", 1), ("cola", "El perro movía la cola de alegría.", 0), ("cola", "Pegó las piezas rotas con cola.", 2),
        ("sobre", "Dejé las llaves sobre la mesa.", 1), ("sobre", "Metí la carta en un sobre y le puse una estampilla.", 0), ("sobre", "Leímos un artículo sobre la salud del corazón.", 2)]
PLANTA = ["El lunes, Jorge empezó a trabajar en una planta empacadora de alimentos. Estaba [ansioso]: no había dormido bien y le sudaban las manos.",
          "La supervisora le explicó las reglas de [higiene], es decir, las normas de limpieza que todos deben seguir: lavarse las manos, cubrirse el pelo y usar guantes. Luego le mostró la línea de producción, donde las cajas avanzaban por una banda [sin interrupción], sin detenerse ni un momento.",
          "—Aquí todo es muy [riguroso] —le advirtió—. Un pequeño descuido puede contaminar un lote entero.",
          "A Jorge le tocó revisar las [fechas de caducidad] de las latas, para que ningún producto vencido saliera de la planta. Al principio era lento, pero sus compañeros, a diferencia de lo que temía, fueron muy amables y le dieron consejos. Al final del turno, ya no estaba nervioso: se sentía [sereno] y orgulloso de su primer día."]


def az(t):
    return re.sub(r"\[([^\]]+)\]", r'<span class="nueva">\1</span>', t)


def plano(t):
    return t.replace("[", "").replace("]", "")


def entrada(pal):
    return f'<div class="entrada-dicc"><p class="lema">{pal}</p><ol>' + "".join(f"<li>{a}</li>" for a in ENTRADAS[pal]) + "</ol></div>"


def leccion():
    P = C.Practicas()
    s1 = f"""<p>Ningún lector conoce todas las palabras. La diferencia entre un buen lector y uno que se rinde es lo que hace cuando encuentra una palabra nueva: el buen lector no se detiene ni busca cada palabra en el diccionario; mira a su alrededor y la descubre. En el GED no hay diccionario, y muchas preguntas piden justamente eso: «¿Qué significa la palabra X en el párrafo 2?».</p>
<p>El <strong>contexto</strong> son las palabras y oraciones que rodean a una palabra. Como las piezas alrededor de un hueco en un rompecabezas, el contexto le dice qué forma debe tener la pieza que falta.</p>
<div class="texto-lectura"><p>«Después de correr diez cuadras bajo el sol, Pedro estaba <span class="nueva">exhausto</span> y se dejó caer en una silla.»</p></div>
<p>Aunque no conozca la palabra <em>exhausto</em>, el contexto se lo dice: corrió diez cuadras, bajo el sol, y se dejó caer. Significa <strong>muy cansado</strong>.</p>
{C.caja("tip", "La prueba del cambio", "<p>Cuando crea saber qué significa, ponga su significado en lugar de la palabra y lea la oración: «Pedro estaba <em>muy cansado</em> y se dejó caer en una silla.» Si la oración tiene sentido, acertó.</p>")}
<p>Las palabras nuevas de esta lección aparecen <span class="nueva">así</span>: en azul, en negrita y subrayadas.</p>"""

    s2 = f"""{C.tabla("Cinco tipos de pistas del contexto", ["Pista", "Cómo la reconoce", "Ejemplo"],
         [["Definición", "El texto explica la palabra, a menudo entre comas o después de <em>es decir, o sea, que significa</em>.", "Revisaron el <span class=\"nueva\">inventario</span>, es decir, la lista de todo lo que hay en el almacén."],
          ["Sinónimo", "Cerca aparece otra palabra que significa lo mismo.", "El jefe estaba <span class=\"nueva\">furioso</span>; nunca lo habíamos visto tan enojado."],
          ["Contraste", "Una palabra como <em>pero, en cambio</em> o <em>a diferencia de</em> presenta lo contrario.", "Su hermano es muy hablador; ella, en cambio, es muy <span class=\"nueva\">reservada</span>."],
          ["Ejemplo", "Después de <em>como, por ejemplo</em> o <em>tales como</em> vienen casos concretos.", "Venden <span class=\"nueva\">legumbres</span>, como frijoles, lentejas y garbanzos."],
          ["Sentido general", "No hay una pista concreta: lo dice la situación entera.", "El niño se <span class=\"nueva\">extravió</span> en el mercado y su madre lo buscó durante una hora."]])}
{C.caja("tip", "En el ejemplo de contraste", "<p>Si el hermano habla mucho y ella es lo contrario, <em>reservada</em> significa que habla poco y guarda sus cosas para sí.</p>")}
{P("Compruebe", "«La empresa decidió <span class=\"nueva\">contratar</span>, o sea, dar empleo, a veinte personas más.» ¿Qué pista hay?", ["Definición", "Ejemplo", "Contraste"], 0, {1: "No hay una lista de casos.", 2: "No se presenta lo contrario."}, "<em>o sea, dar empleo</em> explica la palabra.")}
{P("Compruebe", "«Mi abuela es muy <span class=\"nueva\">longeva</span>: tiene ciento dos años y todavía cocina.» ¿Qué significa <em>longeva</em>?", ["Que vive muchos años", "Que cocina muy bien", "Que es muy alta"], 0, {1: "Cocinar es un detalle.", 2: "El texto no habla de estatura."}, "El sentido general: ciento dos años.")}
{P("Compruebe", "«Estaba <span class=\"nueva\">aterrado</span>; nunca había sentido tanto miedo.» ¿Qué pista hay?", ["Ejemplo", "Contraste", "Sinónimo"], 2, {0: "No hay casos concretos.", 1: "No hay nada contrario."}, "<em>tanto miedo</em> repite la idea con otras palabras.")}
{P("Compruebe", "«Tras la tormenta, el río se <span class=\"nueva\">desbordó</span> e inundó las calles cercanas.» ¿Qué significa?", ["Se secó por completo", "Se salió de su cauce", "Cambió de color"], 1, {0: "Si inundó las calles, tenía mucha agua.", 2: "El texto no habla de colores."}, "Si inundó las calles, el agua salió del río.")}"""

    s3 = f"""<p>En la Lección 1.2 aprendió a separar una palabra en prefijo, raíz y sufijo. Esa misma herramienta sirve para adivinar el significado: si conoce las piezas, conoce la palabra.</p>
<ul><li>La calle quedó <span class="nueva">intransitable</span> por la nieve. → <strong>in-</strong> (no) + <strong>transitar</strong> (pasar) + <strong>-able</strong> (que se puede): por donde no se puede pasar.</li>
<li>Hay que <span class="nueva">reutilizar</span> las bolsas. → <strong>re-</strong> (otra vez) + <strong>utilizar</strong>: volver a usar.</li>
<li>Fue una decisión <span class="nueva">precipitada</span>. Aquí los afijos no bastan, pero el contexto sí: si se tomó sin pensar, significa hecha demasiado rápido.</li></ul>
<p>También ayuda la <strong>familia de la palabra</strong>. Si no conoce <em>panadero</em>, pero conoce <em>pan</em>, ya sabe de qué se trata. Si no conoce <em>enrojecer</em>, piense en <em>rojo</em>: ponerse rojo.</p>
{C.caja("ojo", "Afijos y contexto juntos", "<p>Los afijos dan una pista, pero el contexto decide. <em>Inflamable</em> no significa «que no se puede inflamar»: significa que <strong>se quema con facilidad</strong>. Aquí <em>in-</em> no niega. Por eso los camiones con gasolina llevan el letrero «inflamable»: es un aviso de peligro.</p>")}
{P("Compruebe", "¿Qué significa <em>irrompible</em>?", ["Que no se puede romper", "Que se rompe con facilidad", "Que ya está roto"], 0, {1: "in- (aquí ir-) niega.", 2: "-ble significa «que se puede»."}, "<strong>ir-</strong> (no) + romper + <strong>-ble</strong>: que no se puede romper.")}
<h3>El diccionario: elegir la acepción</h3>
<p>Cuando el contexto no basta, se confirma en un diccionario. En línea puede usar el de la Real Academia Española, <a href="https://dle.rae.es" rel="noopener">dle.rae.es</a>. Muchas palabras tienen varios significados, llamados <strong>acepciones</strong>, y hay que elegir el que corresponde al texto.</p>
<div class="entrada-dicc"><p class="lema">banco <em>m.</em></p><ol><li>Asiento, a veces con respaldo, en el que pueden sentarse varias personas.</li><li>Empresa que guarda dinero, presta y hace pagos.</li>
<li>Conjunto de peces que van juntos en gran número.</li><li>Lugar donde se guardan órganos, sangre u otros elementos para su uso médico: <em>banco de sangre</em>.</li></ol></div>
<p class="fuente">Entrada adaptada para la lección. Abreviaturas frecuentes: <em>m.</em> = sustantivo masculino · <em>f.</em> = sustantivo femenino · <em>adj.</em> = adjetivo · <em>tr.</em> o <em>intr.</em> = verbo.</p>
{P("Acepción 1", "«Fui al <strong>banco</strong> a cobrar mi cheque.»", ["Acepción 1", "Acepción 2", "Acepción 3", "Acepción 4"], 1, {0: "No es un asiento.", 2: "No son peces.", 3: "No es un banco de sangre."}, "Una empresa que maneja dinero.")}
{P("Acepción 2", "«Desde el barco vimos un <strong>banco</strong> de sardinas.»", ["Acepción 1", "Acepción 2", "Acepción 3", "Acepción 4"], 2, {0: "No es un asiento.", 1: "No es una empresa.", 3: "No es un lugar médico."}, "Muchos peces juntos.")}
<h3>La estrategia de tres pasos</h3>
<ol><li><strong>Relea</strong> la oración completa, y también la anterior y la siguiente. Busque las cinco pistas.</li>
<li><strong>Mire las piezas</strong> de la palabra: ¿tiene un prefijo o un sufijo conocidos? ¿Se parece a otra palabra que conoce?</li>
<li><strong>Pruebe</strong> su significado en lugar de la palabra. Si tiene sentido, siga leyendo. Si es una palabra clave y sigue con dudas, confírmelo en el diccionario.</li></ol>
{C.caja("tip", "No todas las palabras importan igual", "<p>Si una palabra desconocida no cambia el sentido de lo que lee, siga adelante. Deténgase solo en las que necesita para entender la idea.</p>")}"""

    s4 = f"""<p>Lea el texto como un «detective de palabras». Antes de responder las preguntas, escriba en su cuaderno qué cree que significa cada palabra marcada y qué pista usó.</p>
{LE.escuchar(" ".join(plano(p) for p in PLANTA), "Escuchar el texto")}
<div class="texto-lectura"><p><strong>El primer día en la planta</strong></p>{"".join(f"<p>{az(p)}</p>" for p in PLANTA)}</div>
{P("Palabra 1", "<em>ansioso</em> significa…", ["Nervioso y preocupado", "Muy contento", "Con mucha hambre"], 0, {1: "No durmió y le sudaban las manos.", 2: "El texto no habla de comida."}, "Sentido general: no durmió y le sudaban las manos. Más adelante el texto lo confirma: «ya no estaba nervioso».")}
{P("Palabra 2", "¿Qué pista explica <em>higiene</em>?", ["Un contraste con «pero»", "Una definición con «es decir»", "Un sinónimo al final del texto"], 1, {0: "Busque justo después de la palabra.", 2: "Está al lado de la palabra."}, "«es decir, las normas de limpieza».")}
{P("Palabra 3", "<em>riguroso</em> significa…", ["Estricto, muy exigente", "Divertido, relajado", "Sucio, descuidado"], 0, {1: "Un descuido puede contaminar todo.", 2: "Es lo contrario."}, "Sentido general: un pequeño descuido puede contaminar un lote.")}
{P("Palabra 4", "<em>fecha de caducidad</em> es…", ["El día en que se fabricó la lata", "El día a partir del cual el producto ya no sirve", "El día de pago del trabajador"], 1, {0: "Piense en «producto vencido».", 2: "No tiene que ver con el sueldo."}, "Pista: «para que ningún producto vencido saliera».")}
{P("Palabra 5", "¿Qué pista ayuda con <em>sereno</em>?", ["Un contraste: «ya no estaba nervioso»", "Un ejemplo con «como»", "Una definición con «o sea»"], 0, {1: "No hay «como».", 2: "No hay «o sea»."}, "Si ya no estaba nervioso, estaba tranquilo: eso es <em>sereno</em>.")}
<p>Si tiene con quién practicar, lean juntos un artículo del periódico y que cada uno elija una palabra difícil. Intenten descubrir su significado por el contexto antes de buscarla.</p>"""

    secciones = [("s1", "¿Qué es el contexto?", s1), ("s2", "Cinco tipos de pistas", s2), ("s3", "Afijos, familias y diccionario", s3), ("s4", "Lectura: «El primer día en la planta»", s4)]
    tarea = [("Mi cuaderno de palabras.", "Abra una sección del cuaderno para palabras nuevas. Cada vez que encuentre una, anote la oración donde la vio, su significado deducido, la pista que usó y, después, la definición del diccionario."),
             ("Cinco palabras de la semana.", "Lea un artículo de un periódico en español y encuentre cinco palabras que no conocía. Siga la estrategia de tres pasos con cada una."),
             ("Escriba pistas.", "Escriba cinco oraciones, una por cada tipo de pista, con una palabra que conozca bien. Ejemplo de pista de ejemplo: «Me gustan los cítricos, como la naranja, el limón y la toronja».")]
    quiz = [
        ("El <strong>contexto</strong> de una palabra es…", ["las palabras y oraciones que la rodean", "su definición en el diccionario", "la primera letra de la palabra"], 0, {1: "Eso es una acepción.", 2: "No tiene que ver con las letras."}, "Lo que <strong>rodea</strong> a la palabra."),
        ("«Llevó al perro al <em>veterinario</em>, es decir, al médico de los animales.» ¿Qué pista hay?", ["Definición", "Contraste", "Ejemplo"], 0, {1: "No hay nada contrario.", 2: "No hay casos."}, "<strong>Definición</strong>: «es decir»."),
        ("«Juan es muy <em>tacaño</em>; su hermana, en cambio, es generosa con todos.» ¿Qué significa <em>tacaño</em>?", ["Que no le gusta gastar ni dar", "Que es muy alto y fuerte", "Que trabaja mucho"], 0, {1: "Busque el contraste.", 2: "Busque el contraste."}, "Lo contrario de <strong>generoso</strong>."),
        ("«Compré varios <em>lácteos</em>, como leche, queso y yogur.» ¿Qué son los lácteos?", ["Productos hechos con leche", "Frutas de temporada", "Productos de limpieza"], 0, {1: "Mire los ejemplos.", 2: "Mire los ejemplos."}, "Productos de <strong>leche</strong>."),
        ("«La sala estaba <em>repleta</em>: no cabía ni una persona más.» ¿Qué significa <em>repleta</em>?", ["Llena por completo", "Vacía y oscura", "Muy limpia"], 0, {1: "Es lo contrario.", 2: "No habla de limpieza."}, "<strong>Llena</strong>."),
        ("«Estaba <em>dichoso</em>, muy feliz, el día de su graduación.» ¿Qué pista hay?", ["Sinónimo", "Ejemplo", "Contraste"], 0, {1: "No hay casos.", 2: "No hay nada contrario."}, "<strong>Sinónimo</strong>: muy feliz."),
        ("Un cartel dice «Material <em>inflamable</em>». ¿Qué significa?", ["Que se quema con facilidad", "Que no se puede quemar", "Que es muy pesado"], 0, {1: "Aquí in- no niega.", 2: "No habla del peso."}, "Se <strong>quema</strong> con facilidad."),
        ("Las distintas definiciones de una palabra en el diccionario se llaman…", ["acepciones", "afijos", "sinónimos"], 0, {1: "Los afijos son piezas de la palabra.", 2: "Un sinónimo es otra palabra."}, "<strong>Acepciones.</strong>"),
        ("¿Cuál es el primer paso ante una palabra desconocida?", ["Releer la oración completa y buscar pistas", "Cerrar el libro y buscar otro texto", "Saltar al último párrafo del texto"], 0, {1: "No hay que rendirse.", 2: "La pista está cerca de la palabra."}, "<strong>Releer</strong> y buscar pistas."),
        ("¿Cómo comprueba si acertó el significado?", ["Lo pone en lugar de la palabra y mira si la oración tiene sentido", "Mira si la palabra es larga o corta", "Lo compara con el título del texto"], 0, {1: "El largo no dice nada.", 2: "El título no basta."}, "La <strong>prueba del cambio</strong>."),
    ]
    filas = [
        ("Pistas", "Reconozco las cinco pistas: definición, sinónimo, contraste, ejemplo y sentido general.", "Reconozco la definición y el ejemplo.", "No busco pistas (<a href=\"#s2\">repase la sección 2</a>)."),
        ("Afijos y familias", "Uso prefijos, sufijos y familias, y dejo que el contexto decida.", "Uso los afijos, pero a veces me engañan.", "No miro las piezas (<a href=\"#s3\">repase la sección 3</a>)."),
        ("Diccionario", "Elijo la acepción que corresponde a la oración.", "Dudo entre dos acepciones.", "Tomo siempre la primera (<a href=\"#s3\">repase la sección 3</a>)."),
    ]
    cierre = "<p>Ya tiene una estrategia para las palabras nuevas. En la próxima lección verá cuándo una expresión dice <strong>más de lo que sus palabras dicen</strong>: el lenguaje figurado y los modismos.</p>"
    glosario = [("Contexto", "Las palabras y oraciones que rodean a otra."), ("Pista de contraste", "Palabra como «pero» o «en cambio» que presenta lo contrario."),
                ("Familia de palabras", "Palabras que comparten la misma raíz: pan, panadero, panadería."), ("Acepción", "Cada uno de los significados de una palabra en el diccionario.")]
    conexion = ("<p>En la Lección 1.2 separó palabras en prefijo, raíz y sufijo, y en el Nivel 1 usó las claves de contexto. Hoy juntará las dos herramientas en una estrategia de tres pasos.</p>"
                "<p><strong>Lo que necesita:</strong> el cuaderno y, si puede, un periódico en español.</p>")
    estd = LE.estandares(["R.4.1"], base=["L.1.1"])
    return C.pagina_leccion(N, LE.titulo(N), "Descubrir una palabra sin salir del texto.", ["Vocabulario", "Contexto"],
                            ["<strong>Reconocer</strong> las cinco pistas del contexto.", "<strong>Usar</strong> afijos y familias de palabras.",
                             "<strong>Elegir</strong> la acepción correcta en el diccionario.", "<strong>Aplicar</strong> la estrategia de tres pasos."],
                            estd, conexion, secciones, tarea, quiz, filas, cierre, ("5-3", LE.titulo("5-3")), glosario, P)


def practica():
    pi = [{"enun": f'<div class="texto-lectura"><p>{az(o)}</p></div><strong>¿Qué significa la palabra marcada?</strong>', "ops": ops, "ok": 0,
           "pista": "Ponga esa respuesta en lugar de la palabra marcada: ¿la oración tiene sentido?", "exp": f"Pista: {e}"} for o, ops, e in PISTAS]
    af = [{"enun": f'<div class="texto-lectura"><p>{az(o)}</p></div><strong>¿Qué significa la palabra marcada?</strong>', "ops": ops, "ok": 0,
           "pista": "Separe la palabra en piezas o busque una palabra conocida dentro de ella.", "exp": e} for o, ops, e in AFIJOS]
    di = [{"enun": entrada(p) + f'<div class="texto-lectura"><p>«{o.replace(p, f"<span class=nueva>{p}</span>", 1)}»</p></div><strong>¿Qué acepción corresponde?</strong>',
           "ops": [f"Acepción {i + 1}" for i in range(len(ENTRADAS[p]))], "ok": k, "enOrden": True, "pista": "Pruebe ese significado en la oración: ¿tiene sentido?",
           "exp": f"Acepción {k + 1}: {ENTRADAS[p][k]}"} for p, o, k in ACEP]
    mods = [("pistas", "Pistas del contexto", C.om("m1", "Lea la oración y elija el significado de la palabra marcada.")),
            ("afijos", "Afijos y familias", C.om("m2", "Descubra el significado por las piezas de la palabra y por el contexto.")),
            ("acepciones", "Elija la acepción", C.om("m3", "Lea la entrada del diccionario y la oración. ¿Qué acepción corresponde?"))]
    js = C.js_datos("PI", pi) + C.js_datos("AF", af) + C.js_datos("DI", di) + 'creaBanco("m1", PI);\ncreaBanco("m2", AF);\ncreaBanco("m3", DI);\n'
    return C.pagina_practica(N, LE.titulo(N), "Tres actividades · los ejercicios cambian cada vez · dos intentos en cada uno", mods, js)


if __name__ == "__main__":
    LE.construye(N, leccion, practica, horas="Unas 3 horas")
