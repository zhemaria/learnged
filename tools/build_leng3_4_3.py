# -*- coding: utf-8 -*-
"""LearnGED · Artes del lenguaje (español) · Nivel 3 · Lección 4.3 · Lenguaje figurado: símiles, metáforas, modismos y refranes.
Fuente: clases_leng3/clase_4-3.html (GEDparaHispanos) y gramatica/n3-l4-3.html, adaptadas al marco de LearnGED.
Uso: python3 tools/build_leng3_4_3.py
"""
import os, sys, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import leng_es as LE
from leng_es import C

LE.nivel(3)
N = "4-3"
T = ["Símil", "Metáfora", "Modismo", "Refrán"]


def F(t, k):
    return f'<span class="fg fg-{k}">{t}</span>'


CALLE = [f"A las cinco de la mañana, la calle 26 todavía {F('duerme bajo una cobija de niebla', 'm')}. Las luces de los semáforos {F('parpadean como ojos cansados', 's')}. Don Toño abre su panadería, y el olor del pan sale a la calle {F('igual que un perro contento que corre a saludar', 's')}.",
         f"Poco a poco, la avenida se convierte en {F('un río de gente', 'm')}: obreros con su lonchera, enfermeras de uniforme azul, estudiantes con la mochila {F('más pesada que una piedra', 's')}. Nadie se detiene, porque {F('el tiempo es oro', 'r')}.",
         f"—¡Corre, que {F('se te pegaron las sábanas', 'd')}! —le grita doña Rosa a su nieto, que sale detrás del autobús con un pan en la boca.",
         f"El muchacho llega justo, sin aliento, y se sienta junto a la ventana. Su abuela sonríe y piensa: «{F('Camarón que se duerme se lo lleva la corriente', 'r')}».",
         f"Detrás de los techos, {F('el sol asoma su cara naranja', 'm')}, y la calle, por fin, {F('abre los ojos', 'm')}."]
RC = [("Sus ojos brillaban como dos luceros.", 0, "Compara con <em>como</em>."), ("Sus ojos eran dos luceros.", 1, "Dice que los ojos <em>son</em> luceros, sin <em>como</em>."),
      ("Mi abuelo es un libro abierto.", 1, "Lo identifica con un libro: metáfora."), ("Corre igual que una gacela.", 0, "Compara con <em>igual que</em>."),
      ("Ese señor siempre mete la pata.", 2, "Expresión fija: equivocarse."), ("Camarón que se duerme se lo lleva la corriente.", 3, "Frase tradicional con una enseñanza."),
      ("El reloj de la cocina se quejaba con cada segundo.", 1, "Personificación: el reloj hace algo de personas."), ("El examen parecía una montaña imposible de subir.", 0, "Compara con <em>parecía</em>."),
      ("Me costó un ojo de la cara.", 2, "Expresión fija: ser muy caro."), ("Dime con quién andas y te diré quién eres.", 3, "Frase tradicional con una enseñanza."),
      ("La ciudad era un hormiguero.", 1, "Dice que la ciudad <em>es</em> un hormiguero: llena de gente que se mueve sin parar."), ("Se me pegaron las sábanas.", 2, "Expresión fija: dormir de más."),
      ("Es tan dulce como la miel.", 0, "Compara con <em>tan… como</em>."), ("No hay mal que por bien no venga.", 3, "Frase tradicional con una enseñanza."),
      ("La luna nos miraba desde el cielo.", 1, "Personificación: la luna mira, como una persona."),
      ("Estaba como pez en el agua.", 2, "Expresión fija: sentirse muy cómodo en un lugar. Aunque lleva <em>como</em>, es un modismo que todos usan igual.")]
IN = [("«Mi hija es un torbellino: no se queda quieta ni un minuto.»", ["Es muy inquieta y activa", "Le gusta mucho el viento", "Es muy tranquila y callada"], "El torbellino gira sin parar: la hija no se está quieta."),
      ("«Después de la noticia, la casa quedó en un silencio de piedra.»", ["Un silencio total, pesado", "Un ruido muy fuerte y largo", "Una casa hecha de piedra"], "La piedra es dura y no suena: el silencio era total."),
      ("«El dinero se le escapaba como agua entre los dedos.»", ["Gastaba el dinero sin poder evitarlo", "Guardaba el dinero en el agua", "Lavaba el dinero todos los días"], "El agua se escapa de las manos; el dinero también."),
      ("«Su palabra es oro.»", ["Lo que promete, lo cumple", "Habla de joyas todo el tiempo", "Es una persona muy rica"], "El oro vale mucho; su palabra también."),
      ("«Estaba como pez en el agua en su nuevo trabajo.»", ["Se sentía muy cómodo y a gusto", "Trabajaba en una pescadería", "Tenía que nadar todos los días"], "Modismo: sentirse en su ambiente."),
      ("«Le dieron gato por liebre en la tienda.»", ["Lo engañaron con algo de menor calidad", "Le vendieron una mascota", "Le regalaron un conejo blanco"], "Modismo: dar algo peor de lo que se paga."),
      ("«El tren era una serpiente de luces que cruzaba la noche.»", ["El tren, largo y alumbrado, parecía moverse como una serpiente", "Había serpientes peligrosas en las vías del tren por la noche", "El tren llevaba muchos animales del zoológico de la ciudad"], "Metáfora: largo, curvo y con luces, como una serpiente brillante."),
      ("«Ese trabajo es pan comido.»", ["Es muy fácil", "Es en una panadería", "Da mucha hambre"], "Modismo: algo muy fácil."),
      ("«Las palabras de la maestra fueron un bálsamo para Marta.»", ["La consolaron y la hicieron sentir mejor", "Le dieron una medicina para la piel", "La hicieron enojar mucho en la clase"], "El bálsamo calma el dolor: las palabras la consolaron."),
      ("«Tiene un corazón de oro.»", ["Es muy buena y generosa", "Tiene problemas del corazón", "Usa muchas joyas de oro"], "El oro es valioso: su bondad también."),
      ("«Ponerse las pilas antes del examen.»", ["Ponerse a estudiar con energía", "Comprar baterías nuevas", "Cargar el celular a tiempo"], "Modismo: esforzarse, ponerse activo."),
      ("«La noticia cayó como un balde de agua fría.»", ["Fue una sorpresa muy desagradable", "Empezó a llover de repente", "Hacía mucho frío ese día"], "El agua fría de golpe sorprende y molesta: así cayó la noticia.")]
RF = ["Camarón que se duerme se lo lleva la corriente.", "Más vale tarde que nunca.", "Dime con quién andas y te diré quién eres.", "No hay mal que por bien no venga.",
      "Del dicho al hecho hay mucho trecho.", "Al que madruga, Dios lo ayuda.", "En boca cerrada no entran moscas.", "Más vale prevenir que lamentar."]
SIT = [("Don Luis empezó a estudiar para el GED a los 70 años y lo aprobó.", 1, [5, 6]),
       ("Rosa no se inscribió a tiempo y otra persona se quedó con el último lugar del curso.", 0, [3, 2]),
       ("El político prometió arreglar todas las calles, pero un año después no ha arreglado ninguna.", 4, [1, 7]),
       ("Pedro siempre anda con un grupo que se mete en problemas, y la gente ya desconfía de él.", 2, [6, 5]),
       ("Se le descompuso el carro y, por tomar el autobús, conoció a su mejor amigo.", 3, [0, 4]),
       ("María llegó a la oficina de empleo antes de que abriera y consiguió la primera entrevista.", 5, [1, 2]),
       ("Juan habló mal de su jefe en la cafetería y su jefe estaba en la mesa de al lado.", 6, [3, 4]),
       ("Antes de la tormenta, la familia compró agua, pilas y comida por si se iba la luz.", 7, [0, 1])]


def leccion():
    P = C.Practicas()
    s1 = f"""<p>«Mi abuela tenía las manos como raíces.» Nadie piensa que las manos de la abuela eran de madera ni que salían de la tierra. Pero en una sola línea se entiende que eran viejas, fuertes y llenas de arrugas, y que de ellas salió toda la familia. Eso es el <strong>lenguaje figurado</strong>: decir mucho con pocas palabras, a través de una imagen. En el GED aparecen preguntas como «¿Qué sugiere la comparación del párrafo 2?». Esta lección le enseña a responderlas.</p>
<p>En el Nivel 2 aprendió que una expresión puede tener sentido <strong>literal</strong> (lo que dicen exactamente las palabras) o <strong>figurado</strong> (otro sentido, que se entiende por el contexto). «Se me rompió el corazón» no habla de un órgano roto, sino de una gran tristeza. También estudió los modismos, como «estar en las nubes». Hoy conocerá las herramientas con las que se construye ese sentido figurado.</p>"""

    s2 = f"""<p>El <strong>símil</strong> (o comparación) relaciona dos cosas distintas con una palabra que anuncia la comparación: <em>como, igual que, parece, se parece a, tan… como</em>.</p>
{C.tabla("Ejemplos de símil con lo que se compara y lo que comparten", ["Símil", "Se compara…", "Lo que tienen en común"],
         [["Tenía las manos <strong>como</strong> raíces.", "las manos con raíces", "arrugadas, fuertes, antiguas"], ["El niño es <strong>tan</strong> curioso <strong>como</strong> un gato.", "el niño con un gato", "la curiosidad"],
          ["La noticia corrió <strong>igual que</strong> el fuego en el monte.", "la noticia con el fuego", "la rapidez con que se extendió"]])}
{C.caja("tip", "Dos preguntas", "<p>Para interpretar un símil, pregúntese: ¿qué se compara con qué? y ¿en qué se parecen? La respuesta a la segunda es lo que el autor quiere que usted sienta o vea.</p>")}
{C.caja("ojo", "No toda comparación es un símil", "<p>«Mi casa es tan grande como la suya» compara dos casas, cosas de la misma clase, de forma literal. El símil une cosas <strong>distintas</strong> para crear una imagen.</p>")}
{P("Símil", "¿Cuál es un símil?", ["Sus manos eran lija.", "Sus manos eran ásperas como lija.", "Sus manos estaban muy secas."], 1, {0: "No usa <em>como</em>: es una metáfora.", 2: "Es literal."}, "Compara con <em>como</em>: es un <strong>símil</strong>.")}"""

    s3 = f"""<p>La <strong>metáfora</strong> también compara dos cosas distintas, pero sin la palabra que anuncia la comparación: dice que una cosa <em>es</em> la otra, o le da directamente sus rasgos.</p>
{C.tabla("Símil y metáfora de la misma idea", ["Símil", "Metáfora"],
         [["La avenida parecía un río de gente.", "La avenida era un río de gente."], ["Sus ojos brillaban como dos luceros.", "Sus ojos eran dos luceros."], ["Esa mujer es fuerte como un roble.", "Esa mujer es un roble."]], fila_th=False)}
<p>A veces la metáfora no dice <em>es</em>: simplemente le da a algo los rasgos de otra cosa. En «la ciudad despierta» o «el viento susurraba», la ciudad y el viento hacen cosas de personas. A esta clase de metáfora se le llama también <strong>personificación</strong>.</p>
{C.caja("tip", "¿Por qué usar metáforas?", "<p>Una metáfora es más fuerte que un símil: no dice que algo se parece, dice que <em>es</em>. «Esa mujer es un roble» transmite fuerza, firmeza y que nada la derriba, todo en cuatro palabras.</p>")}
{P("Metáfora 1", "«Esa mujer es un roble.» ¿Qué se dice de ella?", ["Que es alta y delgada", "Que vive en el bosque", "Que es fuerte y firme"], 2, {0: "¿Qué rasgo del roble se le pasa a la mujer?", 1: "Es figurado, no literal."}, "Que es <strong>fuerte y firme</strong>, como un roble.")}
{P("Metáfora 2", "«La luna nos miraba desde el cielo.» ¿Qué recurso es?", T, 1, {0: "No hay <em>como</em>.", 2: "No es una expresión fija.", 3: "No da un consejo."}, "<strong>Metáfora</strong> (personificación): la luna mira, como una persona.")}"""

    s4 = f"""<p>Un <strong>modismo</strong> es una expresión fija que todos usan y cuyo sentido no se deduce de sus palabras. Muchos nacieron como metáforas, pero se usaron tanto que ya nadie piensa en la imagen.</p>
{C.tabla("Diferencias entre metáfora y modismo", ["", "Metáfora", "Modismo"],
         [["Quién la crea", "El autor, para ese texto.", "La lengua: la usa todo el mundo."],
          ["¿Se puede cambiar?", "Sí: «la avenida era un río», «un mar», «una corriente»…", "No: se dice «meter la pata», no «meter el pie»."],
          ["Ejemplos", "«Su risa era una campana.»", "<em>costar un ojo de la cara</em> (ser muy caro), <em>pegársele las sábanas</em> (dormir de más), <em>meter la pata</em> (equivocarse)"]])}
{P("Modismo", "¿Por qué «meter la pata» es un modismo y no una metáfora del autor?", ["Porque habla de una parte del cuerpo", "Es una expresión fija que usa todo el mundo", "Porque tiene un sentido literal claro"], 1, {0: "Eso no lo hace modismo.", 2: "Al revés: su sentido no se deduce de las palabras."}, "Es una <strong>expresión fija</strong> de la lengua.")}"""

    s5 = f"""<p>Un <strong>refrán</strong> (o proverbio) es una frase corta y tradicional que encierra un consejo o una enseñanza sobre la vida. Casi siempre usa una imagen concreta para hablar de algo general.</p>
{C.tabla("Refranes y su enseñanza", ["Refrán", "Enseñanza"],
         [["Camarón que se duerme se lo lleva la corriente.", "Quien se descuida pierde las oportunidades."], ["Más vale tarde que nunca.", "Es mejor hacer algo tarde que no hacerlo."],
          ["Dime con quién andas y te diré quién eres.", "Las amistades muestran cómo es una persona."], ["No hay mal que por bien no venga.", "De algo malo puede salir algo bueno."],
          ["Del dicho al hecho hay mucho trecho.", "Es más fácil prometer que cumplir."], ["Al que madruga, Dios lo ayuda.", "El esfuerzo y la diligencia tienen recompensa."]])}
{C.caja("tip", "Refranes de distintos países", "<p>Muchos refranes cambian un poco de un país a otro, o tienen versiones distintas con el mismo sentido. Si conoce otra versión de alguno, es igual de válida.</p>")}
{P("Refrán 1", "Perdió su trabajo, pero así encontró uno mejor. ¿Qué refrán corresponde?", [RF[1], RF[3], RF[2]], 1, {0: "No se trata de hacer algo tarde.", 2: "No habla de amistades."}, "De algo malo salió algo bueno.")}
{P("Refrán 2", "El político prometió arreglar todas las calles, pero un año después no ha arreglado ninguna. ¿Qué refrán corresponde?", [RF[7], RF[4], RF[1]], 1, {0: "No habla de prevenir.", 2: "No ha cumplido, ni tarde."}, "Es más fácil prometer que cumplir.")}"""

    lect = "".join(f"<p>{p}</p>" for p in CALLE)
    plano = " ".join(re.sub("<[^>]+>", "", p) for p in CALLE)
    s6 = f"""<p>Lea el texto. Busque y anote en su cuaderno los símiles, las metáforas, el modismo y los refranes. Para cada uno, escriba qué significa. Después pulse <strong>Mostrar el lenguaje figurado</strong>.</p>
<p>{LE.escuchar(plano, "Escuchar el texto")} <button type="button" class="btn-sec" id="btn-f43" aria-pressed="false">Mostrar el lenguaje figurado</button></p>
<div class="articulo lectura-fg" id="lect-43"><p><strong>Madrugada en la calle 26</strong></p>{lect}</div>
<p class="leyenda-partes" id="ley-43"><span style="background:#dbeafe">Símil</span><span style="background:#ede9fe">Metáfora</span><span style="background:#fef3c7">Modismo</span><span style="background:#dcfce7">Refrán</span></p>
<p class="fuente">Texto creado para esta lección.</p>
<script>(function(){{var b=document.getElementById("btn-f43"),t=document.getElementById("lect-43"),l=document.getElementById("ley-43");b.addEventListener("click",function(){{var on=t.classList.toggle("ver-fg");l.classList.toggle("ver",on);b.setAttribute("aria-pressed",on?"true":"false");b.textContent=on?"Ocultar el lenguaje figurado":"Mostrar el lenguaje figurado";}});}})();</script>
<h3>Interprete</h3>
{P("Calle 1", "«La calle 26 todavía duerme bajo una cobija de niebla.» ¿Qué sugiere la metáfora?", ["Que los vecinos duermen en la calle con cobijas", "Que la niebla cubre la calle por completo, como una manta", "Que hace mucho calor a esa hora de la mañana"], 1, {0: "Es figurado: no hay cobijas de verdad.", 2: "La niebla no sugiere calor."}, "La niebla se compara con una cobija: cubre todo, como una manta sobre alguien dormido.")}
{P("Calle 2", "«Las luces de los semáforos parpadean como ojos cansados.» ¿Qué tienen en común?", ["Son de color rojo y verde por las mañanas", "Miran a la gente que pasa por la calle", "Se encienden y se apagan de forma lenta y débil"], 2, {0: "El color no es lo que se compara.", 1: "No miran de verdad."}, "El parpadeo débil de las luces recuerda a unos ojos con sueño.")}
{P("Calle 3", "«Se te pegaron las sábanas.» ¿Qué le dice doña Rosa a su nieto?", ["Que su cama está sucia y hay que lavarla", "Que se quedó dormido y se levantó tarde", "Que tiene frío y debería abrigarse"], 1, {0: "Es un modismo, no literal.", 2: "No habla del frío."}, "Es un modismo: dormir de más.")}
{P("Calle 4", "¿Por qué la abuela piensa «Camarón que se duerme se lo lleva la corriente»?", ["Porque vio un camarón en la panadería de don Toño", "Porque el nieto se quedó dormido en el autobús", "Porque el nieto casi pierde el autobús por dormir de más"], 2, {0: "El refrán no habla de camarones de verdad.", 1: "En el autobús llegó despierto, sin aliento."}, "El refrán enseña que quien se descuida pierde la oportunidad: casi pierde el autobús.")}
{P("Calle 5", "«La calle, por fin, abre los ojos.» ¿Qué significa al final del texto?", ["Los vecinos de la calle abren las ventanas", "La calle se llena de luz y de actividad: despierta el día", "La calle tiene dos semáforos que se encienden"], 1, {0: "Es figurado: la calle no tiene ojos.", 2: "No habla de semáforos."}, "Personificación: la calle «despierta» como una persona cuando sale el sol.")}
{C.caja("tip", "Si tiene con quién practicar", "<p>Pídale a alguien mayor de su familia que le diga los tres refranes que más usaba su madre o su abuela. Escríbalos en su cuaderno y explique su enseñanza.</p>")}"""

    secciones = [("s1", "Repaso: literal y figurado", s1), ("s2", "El símil: comparar con «como»", s2), ("s3", "La metáfora: comparar sin «como»", s3),
                 ("s4", "¿Metáfora o modismo?", s4), ("s5", "Los refranes", s5), ("s6", "Lectura: «Madrugada en la calle 26»", s6)]
    tarea = [("Sus imágenes.", "Escriba un símil y una metáfora originales sobre su trabajo, su barrio o alguien de su familia. Debajo de cada uno, explique qué se compara y qué tienen en común."),
             ("Del símil a la metáfora.", "Convierta en metáforas: «Su voz era como música» · «El examen fue como una montaña» · «Mi hijo es como un sol». "
              "<details class=\"transc\"><summary>Ver respuestas posibles</summary><p>«Su voz era música.» · «El examen fue una montaña.» · «Mi hijo es un sol.»</p></details>"),
             ("Un refrán en su vida.", "Elija un refrán de la <a href=\"#s5\">sección 5</a> y cuente en un párrafo una experiencia suya que lo demuestre.")]
    quiz = [
        ("¿Qué diferencia hay entre un símil y una metáfora?", ["El símil usa una palabra como «como»; la metáfora, no", "El símil es más largo y la metáfora más corta", "La metáfora siempre habla de animales"], 0, {1: "El largo no importa.", 2: "No."}, "El símil anuncia la comparación; la metáfora, no."),
        ("¿Cuál es una metáfora?", ["Mi madre es mi faro.", "Mi madre es como un faro.", "Mi madre vive cerca del faro."], 0, {1: "Es un símil.", 2: "Es literal."}, "<strong>Mi madre es mi faro.</strong>"),
        ("«La ciudad dormía.» ¿Qué recurso es?", ["Una personificación", "Un refrán", "Un modismo"], 0, {1: "No da un consejo.", 2: "No es una expresión fija."}, "Una <strong>personificación</strong>."),
        ("¿Cuál es un <strong>modismo</strong>?", ["meter la pata", "sus ojos eran estrellas", "rápido como un rayo"], 0, {1: "Es una metáfora.", 2: "Es un símil."}, "<strong>Meter la pata.</strong>"),
        ("¿Qué enseña «Del dicho al hecho hay mucho trecho»?", ["Es más fácil prometer que cumplir", "Hay que caminar mucho cada día", "Las palabras valen más que las obras"], 0, {1: "Es literal.", 2: "Es al revés."}, "Es más fácil <strong>prometer</strong> que cumplir."),
        ("«Llegó tan cansado como un perro después de correr todo el día.» ¿Qué recurso se usa?", ["Un símil", "Un refrán", "Un modismo"], 0, {1: "No da un consejo.", 2: "No es una expresión fija."}, "Un <strong>símil</strong>: <em>tan… como</em>."),
        ("Para interpretar una comparación, ¿qué conviene preguntarse?", ["Qué se compara y en qué se parecen", "Cuántas palabras tiene la oración", "Si la comparación es verdad o mentira"], 0, {1: "No ayuda.", 2: "Es figurada: no es literal."}, "<strong>Qué</strong> se compara y <strong>en qué</strong> se parecen."),
        ("«Mi casa es tan grande como la suya.» ¿Por qué no es un símil?", ["Compara dos cosas de la misma clase, de forma literal", "Porque no usa ninguna palabra de comparación", "Porque habla de una casa y no de una persona"], 0, {1: "Sí usa <em>tan… como</em>.", 2: "No."}, "Compara cosas de la <strong>misma clase</strong>."),
        ("María llegó antes de que abriera la oficina y consiguió la primera entrevista. ¿Qué refrán corresponde?", ["Al que madruga, Dios lo ayuda.", "En boca cerrada no entran moscas.", "Dime con quién andas y te diré quién eres."], 0, {1: "No habla de callar.", 2: "No habla de amistades."}, "<strong>Al que madruga, Dios lo ayuda.</strong>"),
        ("«Ese trabajo es pan comido.» ¿Qué significa?", ["Es muy fácil", "Es en una panadería", "Da mucha hambre"], 0, {1: "Es figurado.", 2: "Es figurado."}, "Es <strong>muy fácil</strong>."),
    ]
    filas = [
        ("Símil y metáfora", "Los distingo y explico qué se compara y en qué se parecen.", "Los distingo, pero me cuesta interpretarlos.", "Los confundo (<a href=\"#s2\">repase las secciones 2 y 3</a>)."),
        ("Modismos", "Reconozco los modismos como expresiones fijas.", "Los confundo con metáforas.", "No los reconozco (<a href=\"#s4\">repase la sección 4</a>)."),
        ("Refranes", "Explico la enseñanza de un refrán y lo aplico a una situación.", "Conozco algunos.", "Me cuesta (<a href=\"#s5\">repase la sección 5</a>)."),
    ]
    cierre = "<p>Ya interpreta símiles, metáforas, modismos y refranes. ¡Terminó el Tema 4! En el Tema 5 aprenderá a <strong>evaluar argumentos</strong> e <strong>integrar fuentes</strong>.</p>"
    glosario = [("Símil", "Comparación de dos cosas distintas con una palabra como «como»."), ("Metáfora", "Comparación sin «como»: dice que una cosa es la otra."),
                ("Personificación", "Metáfora que da a cosas o animales rasgos de personas."), ("Modismo", "Expresión fija cuyo sentido no se deduce de sus palabras."),
                ("Refrán", "Frase corta y tradicional con un consejo o una enseñanza.")]
    conexion = ("<p>En la Lección 5.3 del Nivel 2 distinguió lo literal de lo figurado. Hoy conoce las herramientas del lenguaje figurado y aprende a interpretarlas como pide el GED.</p>"
                "<p><strong>Lo que necesita:</strong> su cuaderno y, si puede, alguien mayor de su familia que le cuente sus refranes.</p>")
    estd = LE.estandares(["R.4.3"], base=["R.4.1", "R.5.4"])
    return C.pagina_leccion(N, LE.titulo(N), "Decir mucho con una imagen.", ["Literatura", "Lenguaje figurado"],
                            ["<strong>Distinguir</strong> el símil, la metáfora y la personificación.", "<strong>Interpretar</strong> qué se compara y en qué se parecen.",
                             "<strong>Separar</strong> la metáfora del modismo.", "<strong>Explicar</strong> la enseñanza de un refrán."],
                            estd, conexion, secciones, tarea, quiz, filas, cierre, ("5-1", LE.titulo("5-1")), glosario, P)


def practica():
    rc = [{"enun": f'<p class="frase">{t}</p><p>¿Qué recurso es?</p>', "ops": T, "ok": k, "enOrden": True,
           "pista": "¿Hay una palabra que anuncia la comparación? ¿Es una expresión fija que usa todo el mundo? ¿Da un consejo?", "exp": f"<strong>{T[k]}.</strong> {n}"} for t, k, n in RC]
    inn = [{"enun": f'<p class="frase">{t}</p><p>¿Qué significa?</p>', "ops": o, "ok": 0, "pista": "Esa es la lectura literal o no encaja. ¿Qué se compara y en qué se parecen?", "exp": n} for t, o, n in IN]
    rf = [{"enun": f'<p class="frase">{t}</p><p>¿Qué refrán le corresponde?</p>', "ops": [RF[c], RF[d[0]], RF[d[1]]], "ok": 0,
           "pista": "¿Qué enseñanza tiene ese refrán? ¿Encaja con lo que pasó?", "exp": f"«{RF[c]}»"} for t, c, d in SIT]
    mods = [("recurso", "¿Qué recurso es?", C.om("m1", "Decida si es un símil, una metáfora, un modismo o un refrán.")),
            ("significa", "¿Qué significa de verdad?", C.om("m2", "Elija lo que significa de verdad la expresión.")),
            ("refran", "El refrán para cada situación", C.om("m3", "Lea la situación y elija el refrán que le corresponde."))]
    js = C.js_datos("RC", rc) + C.js_datos("IN", inn) + C.js_datos("RF", rf) + 'creaBanco("m1", RC);\ncreaBanco("m2", IN);\ncreaBanco("m3", RF);\n'
    return C.pagina_practica(N, LE.titulo(N), "Tres actividades · los ejercicios cambian cada vez · dos intentos en cada uno", mods, js)


if __name__ == "__main__":
    LE.construye(N, leccion, practica, horas="Unas 3 horas")
