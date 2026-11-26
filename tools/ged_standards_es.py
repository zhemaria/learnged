"""Cuadro de estándares (GED® y CCR) para las lecciones de LearnGED en español.

Usa la misma tabla de lecciones y estándares que tools/ged_standards.py, de modo que las dos
versiones siempre muestran lo mismo. Los textos de los estándares son traducciones de LearnGED;
los textos oficiales están en inglés (se enlaza el mapa de estándares en inglés).

Uso: python3 tools/ged_standards_es.py   (desde la raíz del repositorio learnged)
     Solo escribe el cuadro en las lecciones en español que ya existen.
"""
import html, os, re, importlib.util

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
spec = importlib.util.spec_from_file_location("g", os.path.join(ROOT, "tools", "ged_standards.py"))
g = importlib.util.module_from_spec(spec); spec.loader.exec_module(g)

# ---------- Traducciones (solo de los códigos que usan las lecciones) ----------
TARGETS_ES = {
 "Q.1.a": "Ordenar fracciones y decimales, también en la recta numérica.",
 "Q.1.b": "Aplicar propiedades de los números relacionadas con múltiplos y factores, como el mínimo común múltiplo, el máximo común divisor o la propiedad distributiva, para reescribir expresiones numéricas.",
 "Q.1.d": "Identificar el valor absoluto de un número racional como su distancia al 0 en la recta numérica, y hallar la distancia entre dos números racionales en la recta numérica, también con el valor absoluto de su diferencia.",
 "Q.2.a": "Sumar, restar, multiplicar y dividir números racionales.",
 "Q.2.d": "Determinar cuándo una expresión numérica no está definida.",
 "MP.3.c": "Mejorar o corregir una línea de razonamiento que tiene errores.",
 "A.1.d": "Sumar, restar y multiplicar polinomios, incluida la multiplicación de dos binomios, o dividir polinomios factorizables.",
 "A.1.h": "Sumar, restar, multiplicar y dividir expresiones racionales.",
 "A.1.e": "Evaluar expresiones polinómicas sustituyendo las cantidades desconocidas por números enteros.",
 "A.1.i": "Evaluar expresiones racionales sustituyendo las cantidades desconocidas por números enteros.",
 "Q.1.c": "Aplicar las reglas de los exponentes en expresiones numéricas con exponentes racionales para escribir expresiones equivalentes.",
 "Q.2.b": "Hacer cálculos y escribir expresiones numéricas con cuadrados y raíces cuadradas de números racionales positivos.",
 "Q.2.c": "Hacer cálculos y escribir expresiones numéricas con cubos y raíces cúbicas de números racionales.",
 "Q.4.e": "Usar el teorema de Pitágoras para hallar la medida de un lado desconocido de un triángulo rectángulo.",
 "Q.2.e": "Resolver problemas aritméticos de la vida real, de uno o de varios pasos, con las cuatro operaciones y números racionales, incluidos los que usan notación científica.",
 "Q.3.a": "Calcular tasas unitarias. Por ejemplo: precio por unidad, velocidad constante, personas por milla cuadrada, BTU por pie cúbico.",
 "Q.3.b": "Usar factores de escala para determinar la magnitud de un cambio de tamaño. Convertir entre dibujos reales y dibujos a escala.",
 "Q.3.d": "Resolver problemas de la vida real, de dos pasos, con porcentajes. Por ejemplo: interés simple, impuestos, aumentos y rebajas de precio, propinas y comisiones, aumento y disminución porcentual.",
 "Q.3.c": "Resolver problemas aritméticos de la vida real, de varios pasos, con razones o proporciones, incluidos los que requieren convertir unidades de medida.",
 "Q.4.b": "Calcular el área y la circunferencia de círculos. Hallar el radio o el diámetro cuando se da el área o la circunferencia.",
 "Q.4.a": "Calcular el área y el perímetro de triángulos y rectángulos. Hallar la medida de los lados de triángulos y rectángulos cuando se da el área o el perímetro.",
 "Q.4.c": "Calcular el perímetro de un polígono. Dada una fórmula geométrica, calcular el área de un polígono. Hallar la medida de los lados de la figura cuando se da el área o el perímetro.",
 "Q.4.d": "Calcular el perímetro y el área de figuras compuestas de dos dimensiones, que pueden incluir círculos, dadas las fórmulas geométricas necesarias.",
 "Q.6.a": "Representar, mostrar e interpretar datos por categorías en gráficas de barras o gráficas circulares.",
 "Q.6.c": "Representar, mostrar e interpretar datos de dos variables en tablas y en el plano de coordenadas, incluidos los diagramas de dispersión y las gráficas.",
 "Q.7.a": "Calcular la media, la mediana, la moda y el rango. Calcular un dato que falta, dada la media y todos los demás datos, y también la media ponderada.",
 "Q.8.a": "Usar técnicas de conteo para resolver problemas y hallar combinaciones y permutaciones.",
 "Q.8.b": "Hallar la probabilidad de eventos simples y compuestos.",
 "A.1.a": "Sumar, restar, factorizar, multiplicar y desarrollar expresiones lineales con coeficientes racionales.",
 "A.1.b": "Evaluar expresiones lineales sustituyendo las cantidades desconocidas por números enteros.",
 "A.1.c": "Escribir expresiones lineales al traducir de palabras a símbolos o para representar situaciones comunes.",
 "Q.5.a": "Dadas las fórmulas geométricas, calcular el volumen y el área de superficie de prismas rectangulares. Hallar la medida de los lados o la altura dado el volumen o el área de superficie.",
 "Q.5.b": "Dadas las fórmulas geométricas, calcular el volumen y el área de superficie de cilindros. Hallar la altura, el radio o el diámetro dado el volumen o el área de superficie.",
 "Q.5.c": "Dadas las fórmulas geométricas, calcular el volumen y el área de superficie de prismas rectos. Hallar la medida de los lados o la altura dado el volumen o el área de superficie.",
 "Q.6.b": "Representar, mostrar e interpretar datos de una variable en gráficas sobre la recta numérica, incluidos los diagramas de puntos, los histogramas y los diagramas de caja.",
 "A.3.a": "Resolver inecuaciones lineales de una variable con coeficientes racionales.",
 "A.3.b": "Identificar o graficar la solución de una inecuación lineal de una variable.",
 "A.3.c": "Resolver problemas de la vida real con inecuaciones.",
 "A.3.d": "Escribir inecuaciones lineales de una variable para representar un contexto.",
 "A.2.a": "Resolver ecuaciones lineales de una variable con coeficientes racionales, incluidas las que requieren aplicar la propiedad distributiva y reducir términos semejantes, o las que tienen coeficientes representados con letras.",
 "A.2.b": "Resolver problemas de la vida real con ecuaciones lineales.",
 "A.2.c": "Escribir ecuaciones lineales de una o de varias variables para representar una situación.",
 "A.7.b": "Representar o identificar una función en una tabla o una gráfica como una relación con exactamente una salida (un elemento del rango) para cada entrada (cada elemento del dominio).",
 "A.7.c": "Evaluar funciones lineales y cuadráticas para valores de su dominio cuando se representan con notación de función.",
 "MP.1.a": "Buscar y reconocer por dónde empezar a resolver un problema.",
 "MP.1.b": "Planear un camino de solución o esbozar una línea de razonamiento.",
 "MP.1.c": "Elegir el mejor camino de solución según ciertos criterios.",
 "MP.1.e": "Elegir la técnica o técnicas matemáticas adecuadas para resolver un problema o seguir una línea de razonamiento.",
 "MP.2.a": "Representar algebraicamente problemas de la vida real.",
 "MP.2.b": "Representar visualmente problemas de la vida real.",
 "MP.2.c": "Reconocer los datos importantes y destacados de un problema.",
 "MP.3.a": "Construir los pasos de una línea de razonamiento o de un camino de solución a partir del paso anterior o de los datos.",
 "MP.4.a": "Manejar y resolver expresiones aritméticas.",
 "MP.4.b": "Transformar y resolver expresiones algebraicas.",
 "MP.4.c": "Mostrar datos o expresiones algebraicas en forma gráfica.",
 "MP.5.a": "Reconocer errores en el razonamiento de otras personas.",
 "MP.5.c": "Identificar la información necesaria para evaluar una línea de razonamiento.",
}
CCR_ES = {
 "5.G.2": "Representar problemas matemáticos y de la vida real ubicando puntos en el primer cuadrante del plano de coordenadas, e interpretar las coordenadas de los puntos según la situación.",
 "3.MD.3": "Hacer una pictografía y una gráfica de barras a escala para representar datos con varias categorías. Resolver problemas de uno y de dos pasos de «cuántos más» y «cuántos menos» con la información de gráficas de barras a escala.",
 "6.SP.3": "Reconocer que una medida de tendencia central de un conjunto de datos numéricos resume todos sus valores en un solo número, mientras que una medida de variación describe con un solo número cómo varían sus valores.",
 "7.SP.5": "Entender que la probabilidad de un evento aleatorio es un número entre 0 y 1 que expresa qué tan posible es que ocurra. Los números mayores indican mayor posibilidad.",
 "7.SP.6": "Aproximar la probabilidad de un evento aleatorio reuniendo datos del proceso que lo produce y observando su frecuencia relativa a largo plazo, y predecir la frecuencia relativa aproximada conocida la probabilidad.",
 "7.SP.8": "Hallar la probabilidad de eventos compuestos con listas organizadas, tablas, diagramas de árbol y simulaciones.",
 "7.SP.7": "Construir un modelo de probabilidad y usarlo para hallar la probabilidad de eventos. Comparar las probabilidades del modelo con las frecuencias observadas; si no coinciden bien, explicar las posibles causas de la diferencia.",
 "6.SP.5": "Resumir grupos de datos numéricos según su contexto: decir cuántas observaciones hay, describir lo que se estudia y sus unidades de medida, y dar medidas del centro (mediana o media) y de la variación.",
 "3.MD.7": "Relacionar el área con las operaciones de multiplicación y suma.",
 "7.G.4": "Conocer las fórmulas del área y de la circunferencia de un círculo y usarlas para resolver problemas; dar una deducción informal de la relación entre la circunferencia y el área de un círculo.",
 "7.G.1": "Resolver problemas con dibujos a escala de figuras geométricas, incluso calcular longitudes y áreas reales a partir de un dibujo a escala y reproducir un dibujo a otra escala.",
 "7.G.5": "Usar las propiedades de los ángulos suplementarios, complementarios, opuestos por el vértice y adyacentes en problemas de varios pasos, para plantear y resolver ecuaciones sencillas que hallen un ángulo desconocido de una figura.",
 "8.G.4": "Entender que una figura de dos dimensiones es semejante a otra si la segunda se obtiene de la primera con una secuencia de rotaciones, reflexiones, traslaciones y dilataciones; dadas dos figuras semejantes, describir una secuencia que muestre la semejanza.",
 "8.G.5": "Usar argumentos informales para establecer propiedades de la suma de los ángulos y del ángulo exterior de un triángulo, de los ángulos que se forman cuando una transversal corta rectas paralelas, y del criterio ángulo-ángulo de semejanza de triángulos.",
 "8.G.6": "Explicar una demostración del teorema de Pitágoras y de su converso.",
 "8.G.7": "Aplicar el teorema de Pitágoras para hallar lados desconocidos de triángulos rectángulos en problemas de la vida real y de matemáticas, en dos y tres dimensiones.",
 "8.G.9": "Conocer las fórmulas del volumen de conos, cilindros y esferas, y usarlas para resolver problemas de la vida real y de matemáticas.",
 "6.SP.2": "Entender que un conjunto de datos reunido para responder una pregunta estadística tiene una distribución que se describe por su centro, su dispersión y su forma general.",
 "6.SP.4": "Representar datos numéricos en gráficas sobre la recta numérica, como diagramas de puntos, histogramas y diagramas de caja.",
 "7.SP.4": "Usar medidas de tendencia central y de variación de datos numéricos de muestras aleatorias para hacer comparaciones informales entre dos poblaciones.",
 "7.G.6": "Resolver problemas de la vida real y de matemáticas sobre el área, el volumen y el área de la superficie de objetos de dos y tres dimensiones formados por triángulos, cuadriláteros, polígonos, cubos y prismas rectos.",
 "6.G.1": "Hallar el área de triángulos rectángulos, de otros triángulos, de cuadriláteros especiales y de polígonos, componiéndolos en rectángulos o descomponiéndolos en triángulos y otras figuras; aplicar estas técnicas para resolver problemas matemáticos y de la vida real.",
 "3.MD.8": "Resolver problemas matemáticos y de la vida real sobre el perímetro de polígonos: hallar el perímetro dadas las medidas de los lados, hallar la medida de un lado desconocido, y mostrar rectángulos con el mismo perímetro y distinta área, o con la misma área y distinto perímetro.",
 "4.MD.3": "Aplicar las fórmulas del área y del perímetro de rectángulos en problemas matemáticos y de la vida real.",
 "3.G.1": "Entender que figuras de distintas categorías (por ejemplo, rombos, rectángulos y otras) pueden compartir atributos (por ejemplo, tener cuatro lados), y que los atributos compartidos pueden definir una categoría mayor (por ejemplo, los cuadriláteros). Reconocer los rombos, los rectángulos y los cuadrados como ejemplos de cuadriláteros, y dibujar ejemplos de cuadriláteros que no pertenecen a ninguna de estas subcategorías.",
 "4.G.1": "Dibujar puntos, rectas, segmentos, semirrectas, ángulos (rectos, agudos, obtusos) y rectas perpendiculares y paralelas. Identificarlos en figuras de dos dimensiones.",
 "4.G.2": "Clasificar figuras de dos dimensiones según tengan o no rectas paralelas o perpendiculares, o ángulos de una medida dada. Reconocer los triángulos rectángulos como una categoría e identificarlos.",
 "5.G.4": "Clasificar figuras de dos dimensiones en una jerarquía, según sus propiedades.",
 "3.MD.1": "Decir y escribir la hora al minuto más cercano y medir intervalos de tiempo en minutos. Resolver problemas verbales de suma y resta de intervalos de tiempo en minutos, por ejemplo, representándolos en una recta numérica.",
 "3.MD.2": "Medir y estimar volúmenes de líquidos y masas de objetos con unidades estándar: gramos (g), kilogramos (kg) y litros (l). Sumar, restar, multiplicar o dividir para resolver problemas verbales de un paso con masas o volúmenes dados en las mismas unidades.",
 "4.MD.1": "Conocer el tamaño relativo de las unidades de medida de un mismo sistema, como km, m, cm; kg, g; lb, oz; l, ml; h, min, s. Dentro de un mismo sistema, expresar medidas de una unidad mayor en una unidad menor. Anotar las equivalencias en una tabla de dos columnas.",
 "4.MD.2": "Usar las cuatro operaciones para resolver problemas verbales de distancias, intervalos de tiempo, volúmenes de líquidos, masas de objetos y dinero, incluidos problemas con fracciones o decimales sencillos y problemas que requieren expresar una medida de una unidad mayor en una unidad menor. Representar cantidades medidas con diagramas, como rectas numéricas con una escala de medida.",
 "5.MD.1": "Convertir entre unidades de medida estándar de distinto tamaño dentro de un mismo sistema (por ejemplo, convertir 5 cm a 0.05 m), y usar estas conversiones para resolver problemas de la vida real de varios pasos.",
 "3.OA.3": "Usar la multiplicación y la división hasta 100 para resolver problemas verbales con grupos iguales, arreglos y medidas.",
 "3.OA.4": "Hallar el número entero desconocido en una ecuación de multiplicación o de división que relaciona tres números enteros.",
 "3.OA.5": "Aplicar las propiedades de las operaciones (conmutativa, asociativa y distributiva) como estrategias para multiplicar y dividir.",
 "3.OA.7": "Multiplicar y dividir con fluidez hasta 100. Saber de memoria todos los productos de dos números de un dígito.",
 "3.OA.8": "Resolver problemas verbales de dos pasos con las cuatro operaciones. Juzgar si la respuesta es razonable con cálculo mental y estimación, incluido el redondeo.",
 "3.OA.9": "Identificar patrones aritméticos (también en las tablas de sumar y de multiplicar) y explicarlos con las propiedades de las operaciones.",
 "3.NF.1": "Entender la fracción 1/b como una de las b partes iguales en que se divide un entero, y la fracción a/b como a partes de tamaño 1/b.",
 "3.NF.3": "Explicar la equivalencia de fracciones en casos sencillos y comparar fracciones razonando sobre su tamaño.",
 "4.NBT.1": "Reconocer que, en un número entero de varios dígitos, un dígito en un lugar vale diez veces lo que valdría en el lugar de su derecha.",
 "4.NBT.2": "Leer y escribir números enteros de varios dígitos con cifras, con palabras y en forma desarrollada. Comparar dos números de varios dígitos con los símbolos >, = y <.",
 "4.NBT.3": "Usar el valor posicional para redondear números enteros de varios dígitos a cualquier lugar.",
 "4.NBT.4": "Sumar y restar con fluidez números enteros de varios dígitos con el algoritmo usual.",
 "4.NBT.5": "Multiplicar un número entero de hasta cuatro dígitos por uno de un dígito, y dos números de dos dígitos, con estrategias basadas en el valor posicional y en las propiedades de las operaciones.",
 "4.NBT.6": "Hallar cocientes y residuos enteros con dividendos de hasta cuatro dígitos y divisores de un dígito.",
 "4.OA.3": "Resolver problemas verbales de varios pasos con números enteros y las cuatro operaciones, incluidos los que obligan a interpretar el residuo. Juzgar si la respuesta es razonable con cálculo mental y estimación, incluido el redondeo.",
 "4.OA.4": "Hallar todos los pares de factores de un número entero del 1 al 100. Reconocer que un número es múltiplo de cada uno de sus factores. Determinar si un número del 1 al 100 es primo o compuesto.",
 "4.OA.5": "Generar un patrón de números o de figuras que siga una regla dada. Identificar características del patrón que la regla no menciona.",
 "4.NF.1": "Explicar con modelos visuales por qué a/b es equivalente a (n × a)/(n × b), y usar ese principio para reconocer y generar fracciones equivalentes.",
 "4.NF.2": "Comparar dos fracciones con numeradores y denominadores distintos, por ejemplo, buscando un denominador o un numerador común o comparándolas con una fracción de referencia como 1/2. Anotar la comparación con >, = o < y justificarla.",
 "4.NF.3": "Entender una fracción a/b con a > 1 como una suma de fracciones 1/b; entender la suma y la resta de fracciones como juntar y separar partes de un mismo entero, y resolver problemas con fracciones de igual denominador.",
 "4.NF.4": "Ampliar lo que se sabe de la multiplicación para multiplicar una fracción por un número entero, y resolver problemas verbales de ese tipo.",
 "4.NF.6": "Usar la notación decimal para fracciones con denominador 10 o 100. Por ejemplo, escribir 0.62 como 62/100.",
 "5.NBT.1": "Reconocer que, en un número de varios dígitos, un dígito en un lugar vale 10 veces lo que valdría en el lugar de su derecha y 1/10 de lo que valdría en el de su izquierda.",
 "5.NBT.3": "Leer, escribir y comparar decimales hasta las milésimas.",
 "5.NBT.4": "Usar el valor posicional para redondear decimales a cualquier lugar.",
 "5.NBT.5": "Multiplicar con fluidez números enteros de varios dígitos con el algoritmo usual.",
 "5.NBT.6": "Hallar cocientes enteros con dividendos de hasta cuatro dígitos y divisores de dos dígitos.",
 "5.NBT.7": "Sumar, restar, multiplicar y dividir decimales hasta las centésimas, con modelos o dibujos y estrategias basadas en el valor posicional; relacionar la estrategia con el método escrito y explicar el razonamiento (con aplicaciones de educación financiera).",
 "5.NF.1": "Sumar y restar fracciones de distinto denominador (también números mixtos) sustituyéndolas por fracciones equivalentes con el mismo denominador.",
 "5.NF.2": "Resolver problemas verbales de suma y resta de fracciones de un mismo entero, también con distinto denominador. Usar fracciones de referencia para estimar y juzgar si la respuesta es razonable.",
 "5.NF.3": "Interpretar una fracción como la división del numerador entre el denominador (a/b = a ÷ b).",
 "5.NF.4": "Ampliar lo que se sabe de la multiplicación para multiplicar una fracción o un número entero por una fracción.",
 "5.NF.6": "Resolver problemas de la vida real con multiplicación de fracciones y números mixtos, por ejemplo, con modelos visuales o ecuaciones.",
 "5.NF.7": "Ampliar lo que se sabe de la división para dividir fracciones unitarias entre números enteros y números enteros entre fracciones unitarias.",
 "6.EE.2": "Escribir, leer y evaluar expresiones en las que las letras representan números.",
 "6.EE.5": "Entender que resolver una ecuación o una desigualdad es responder la pregunta: ¿qué valores de un conjunto dado, si los hay, la hacen verdadera? Usar la sustitución para comprobar si un número dado la hace verdadera.",
 "6.EE.7": "Resolver problemas de la vida real y de matemáticas escribiendo y resolviendo ecuaciones de la forma x + p = q y px = q, en las que p, q y x son números racionales no negativos.",
 "6.NS.1": "Interpretar y calcular cocientes de fracciones, y resolver problemas verbales de división de fracciones entre fracciones, por ejemplo, con modelos visuales y ecuaciones.",
 "6.NS.5": "Entender que los números positivos y negativos se usan juntos para describir cantidades de sentido o valor opuesto (temperaturas sobre o bajo cero, altura sobre o bajo el nivel del mar, créditos y débitos); usarlos para representar cantidades de la vida real y explicar qué significa el 0 en cada situación.",
 "6.NS.6a": "Reconocer que los signos opuestos indican posiciones a lados contrarios del 0 en la recta numérica; reconocer que el opuesto del opuesto de un número es el mismo número, por ejemplo, −(−3) = 3, y que el 0 es su propio opuesto.",
 "6.NS.7": "Entender el orden y el valor absoluto de los números racionales: interpretar una desigualdad como la posición relativa de dos números en la recta numérica, y entender el valor absoluto de un número racional como su distancia al 0 en la recta numérica.",
 "7.NS.1": "Ampliar lo que se sabe de la suma y la resta para sumar y restar números racionales; representar la suma y la resta en una recta numérica horizontal o vertical.",
 "7.NS.2": "Ampliar lo que se sabe de la multiplicación, la división y las fracciones para multiplicar y dividir números racionales.",
 "7.NS.3": "Resolver problemas matemáticos y de la vida real con las cuatro operaciones y números racionales.",
 "5.OA.1": "Usar paréntesis, corchetes o llaves en expresiones numéricas y evaluar expresiones con estos símbolos.",
 "6.EE.2c": "Evaluar expresiones para valores dados de sus variables, también expresiones que salen de fórmulas de problemas de la vida real. Hacer las operaciones, incluidas las de exponentes enteros, en el orden convencional cuando no hay paréntesis que indiquen otro orden (orden de las operaciones).",
 "7.NS.2b": "Entender que los enteros se pueden dividir, siempre que el divisor no sea cero, y que todo cociente de enteros (con divisor distinto de cero) es un número racional. Si p y q son enteros, −(p/q) = (−p)/q = p/(−q).",
 "5.NBT.2": "Explicar los patrones en la cantidad de ceros del producto al multiplicar un número por potencias de 10, y en la posición del punto decimal al multiplicar o dividir un decimal entre una potencia de 10. Usar exponentes enteros para indicar las potencias de 10.",
 "6.EE.1": "Escribir y evaluar expresiones numéricas con exponentes enteros.",
 "8.EE.1": "Conocer y aplicar las propiedades de los exponentes enteros para obtener expresiones numéricas equivalentes.",
 "8.EE.3": "Usar números expresados como un solo dígito por una potencia entera de 10 para estimar cantidades muy grandes o muy pequeñas, y para expresar cuántas veces mayor es una que otra.",
 "8.EE.4": "Operar con números expresados en notación científica, incluidos problemas en los que se usan a la vez la notación decimal y la científica. Usar la notación científica y elegir unidades de tamaño adecuado para medir cantidades muy grandes o muy pequeñas. Interpretar la notación científica que genera la tecnología.",
 "8.EE.2": "Usar los símbolos de raíz cuadrada y raíz cúbica para representar las soluciones de ecuaciones de la forma x² = p y x³ = p, donde p es un número racional positivo. Evaluar las raíces cuadradas de cuadrados perfectos pequeños y las raíces cúbicas de cubos perfectos pequeños.",
 "7.EE.1": "Aplicar las propiedades de las operaciones como estrategias para sumar, restar, factorizar y desarrollar expresiones lineales con coeficientes racionales.",
 "8.EE.7": "Resolver ecuaciones lineales de una variable. Dar ejemplos de ecuaciones lineales de una variable con una solución, con infinitas soluciones o sin solución. Resolver ecuaciones lineales con coeficientes racionales, incluidas las que requieren desarrollar expresiones con la propiedad distributiva y combinar términos semejantes.",
 "6.EE.8": "Escribir una inecuación de la forma x > c o x < c para representar una restricción o condición de un problema real o matemático. Reconocer que estas inecuaciones tienen infinitas soluciones y representarlas en la recta numérica.",
 "7.EE.4": "Usar variables para representar cantidades de un problema real o matemático y plantear ecuaciones e inecuaciones sencillas para resolverlo razonando sobre las cantidades.",
 "A-CED.4": "Reorganizar fórmulas para destacar una cantidad de interés, con el mismo razonamiento que al resolver ecuaciones.",
 "8.NS.1": "Saber que los números que no son racionales se llaman irracionales. Entender de manera informal que todo número tiene una expansión decimal; mostrar que la de los números racionales termina por repetirse y convertir en número racional una expansión decimal que se repite.",
 "8.NS.2": "Usar aproximaciones racionales de números irracionales para comparar su tamaño, ubicarlos aproximadamente en la recta numérica y estimar el valor de expresiones.",
 "6.RP.1": "Comprender el concepto de razón y usar el lenguaje de las razones para describir la relación entre dos cantidades.",
 "6.RP.2": "Comprender el concepto de tasa unitaria a/b asociada a una razón a:b con b ≠ 0, y usar el lenguaje de las tasas en el contexto de una razón.",
 "6.RP.3": "Usar el razonamiento con razones y tasas para resolver problemas matemáticos y de la vida real; por ejemplo, con tablas de razones equivalentes, diagramas de cinta, rectas numéricas dobles o ecuaciones.",
 "6.RP.3b": "Resolver problemas de tasa unitaria, incluidos los de precio por unidad y velocidad constante.",
 "7.RP.2a": "Decidir si dos cantidades están en una relación proporcional; por ejemplo, comprobando si las razones de una tabla son equivalentes o si su gráfica es una recta que pasa por el origen.",
 "7.RP.2c": "Representar relaciones proporcionales con ecuaciones.",
 "6.RP.3d": "Usar el razonamiento con razones para convertir unidades de medida; manipular y transformar las unidades de forma adecuada al multiplicar o dividir cantidades.",
 "6.RP.3c": "Hallar un porcentaje de una cantidad como una tasa por cada 100 (por ejemplo, el 30% de una cantidad es 30/100 por la cantidad); resolver problemas en los que se busca el todo conocidos una parte y el porcentaje.",
 "7.RP.3": "Usar relaciones proporcionales para resolver problemas de varios pasos con razones y porcentajes. Por ejemplo: interés simple, impuestos, aumentos y rebajas de precio, propinas y comisiones, cargos, aumento y disminución porcentual, error porcentual.",
 "6.NS.3": "Sumar, restar, multiplicar y dividir con fluidez decimales de varios dígitos con el algoritmo usual de cada operación.",
 "6.NS.4": "Hallar el máximo común divisor de dos números enteros menores o iguales que 100 y el mínimo común múltiplo de dos números enteros menores o iguales que 12. Usar la propiedad distributiva para sacar un factor común de una suma.",
 "7.NS.2d": "Convertir un número racional en decimal con la división larga; saber que la forma decimal de un número racional termina en ceros o termina por repetirse.",
}

# Lección en inglés → lección en español
def ruta_es(path):
    m = re.match(r"level-(\d)/lesson-(.+)\.html$", path)
    nombre = m.group(2).replace("-gcf-lcm", "-mcd-mcm")
    return os.path.join(ROOT, "es", "matematicas", "nivel-" + m.group(1), f"leccion-{nombre}.html")

e = html.escape
def li(code, cls):
    return f'<li><span class="std-cod {cls}">{code}</span> {e(TARGETS_ES[code])}</li>'

def box(m):
    p = ['<!-- GED-STANDARDS -->', '<details class="estandares" id="estandares-ged">',
         '<summary><span aria-hidden="true">🎓</span> Estándares de esta lección (GED® y CCR)</summary>', '<div class="std-cuerpo">']
    if m["direct"]:
        p.append('<p class="std-tit">Esta lección trabaja estos objetivos de evaluación del GED®:</p><ul>' + "".join(li(c, "std-dir") for c in m["direct"]) + '</ul>')
    if m["builds"]:
        p.append('<p class="std-tit">Esta lección prepara la base para estos objetivos de evaluación del GED®:</p><ul>' + "".join(li(c, "std-base") for c in m["builds"]) + '</ul>')
    if m["mp"]:
        p.append('<p class="std-tit">Prácticas matemáticas que usa:</p><ul>' + "".join(li(c, "std-mp") for c in m["mp"]) + '</ul>')
    if m.get("ccr"):
        p.append('<p class="std-tit">Estándares CCR para la educación de adultos (College and Career Readiness):</p><ul>' + "".join(f'<li><span class="std-cod std-ccr">{c}</span> <span class="std-nivel">Nivel {g.CCR[c][0]}</span> {e(CCR_ES[c])}</li>' for c in m["ccr"]) + '</ul>')
    p.append(f'<p class="std-fuente">Fuentes: {g.SOURCE}; {g.CCR_FUENTE}. Los textos de los estándares son traducciones de LearnGED; los oficiales están en inglés en el <a href="/math/ged-standards.html" hreflang="en">mapa de estándares (en inglés)</a>.</p>')
    p += ['</div>', '</details>', '<!-- /GED-STANDARDS -->']
    return "\n".join(p)

def insert(full, m):
    s = open(full, encoding="utf-8").read()
    b = box(m)
    if "<!-- GED-STANDARDS -->" in s:
        s = re.sub(r"<!-- GED-STANDARDS -->.*?<!-- /GED-STANDARDS -->", lambda _: b, s, flags=re.S)
    else:
        i = s.index('<div class="caja caja-objetivo">')
        j = s.index("</section>", i)
        s = s[:j] + b + "\n" + s[j:]
    open(full, "w", encoding="utf-8").write(s)

if __name__ == "__main__":
    n = 0
    for path, num, name, m in g.LESSONS:
        for c in m["direct"] + m["builds"] + m["mp"]:
            assert c in TARGETS_ES, "Falta la traducción de " + c
        for c in m.get("ccr", []):
            assert c in CCR_ES, "Falta la traducción de " + c
        full = ruta_es(path)
        if os.path.exists(full):
            insert(full, m); n += 1
    print("ok:", n, "lecciones en español")
