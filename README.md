# LearnGED

Preparación gratuita para el GED® en inglés y español · Free GED® prep in English and Spanish.
Sitio: https://www.learnged.com (versión en español: `/es/`).

Evolución bilingüe de GEDparaHispanos. Mascota: **Leo**, el búho.

## Estructura
- `index.html` — portada en inglés (detecta el idioma del navegador; si es español, abre `/es/`).
- `es/` — versión en español. Las lecciones de Matemáticas en español están en `es/matematicas/nivel-1/` (leccion-T-N.html y practica-T-N.html), con el mismo contenido que las de `math/level-1/`.
- Nivel 2: `math/level-2/` (lesson-T-N.html y practice-T-N.html) y `es/matematicas/nivel-2/` (leccion-T-N.html y practica-T-N.html). `math/integers.js` reúne lo común de los números con signo (recta numérica, fichas, práctica de signo y valor). `math/pemdas.js` es el motor del orden de las operaciones (Tema 3) y `math/rates.js` reúne lo de razones, tasas y dinero (Temas 4 a 6); `math/geometry.js` dibuja las figuras con sus medidas y evalúa las respuestas con π (Tema 7); `math/stats.js` reúne la estadística, los gráficos circulares y la probabilidad (Tema 8). `math/level-2/tengo-debo.html` es el complemento bilingüe de la Lección 1.2 y `math/level-2/fracciomania.html`, el juego de la Lección 2.1 (el idioma va en el enlace: `?lang=en` o `?lang=es`).
- Nivel 3: `math/level-3/` (lesson-T-N.html y practice-T-N.html) y `es/matematicas/nivel-3/` (leccion-T-N.html y practica-T-N.html), construidas con `tools/build_n3_lesson_T_N.py` (usan `tools/bilingue.py` y `tools/n3.py`). `math/exponents.js` es el motor del Tema 1 (monomios, fichas y las prácticas de dos intentos) `math/scinot.js`, el del Tema 2 (notación científica exacta con BigInt), `math/radicals.js`, el del Tema 3 (radicales, términos, fracciones y recta numérica), `math/linear.js`, el del Tema 4 (fracciones exactas, ecuaciones lineales y polinomios; se carga después de `radicals.js`), y `math/inequalities.js`, el del Tema 5 (inecuaciones, regla del signo, gráfica en la recta y práctica «signo + número»; se carga después de `linear.js`). Los ejercicios de rapidez del Tema 3 (`math/level-3/speed-irrationals.html` y `es/matematicas/nivel-3/rapidez-irracionales.html`) se construyen con `tools/build_n3_speed.py`; su lógica bilingüe está en `math/speed-irrationals.js`. La comprobación del Tema 1 está en `math/level-3/topic-1-check.html` y `es/matematicas/nivel-3/comprobacion-tema-1.html` (`tools/build_n3_check_1.py`).
- Cada lección del Nivel 2 se construye en los dos idiomas a la vez con `tools/build_n2_lesson_T_N.py` (usa `tools/bilingue.py` y `tools/n2.py`). Después: `tools/ged_standards.py`, `tools/ged_standards_es.py` y `tools/build_indices.py`.
- `math/lesson.js` y `math/practice.js` sirven a los dos idiomas: si la página tiene `<html lang="es">`, los mensajes salen en español.
- `js/calculator.js` (inglés) y `js/calculadora.js` (español) son el simulador de la TI-30XS; se generan con `tools/build-calculator-en.py` y `tools/build-calculadora-es.py` desde `algebra/calculadora-gph.js`.
- Herramientas para el español: `tools/ged_standards_es.py` (cuadro de estándares) y `tools/build_indice_es.py` (índice del nivel). Los números se escriben igual en los dos idiomas: coma para los miles (3,482,651) y punto para los decimales (3.5), como en el examen GED.
- `learnged.css` — hoja de estilo común (paleta y tipografía Atkinson Hyperlegible).
- `img/` — logotipos y mascota.
- Favicon (`favicon.*`, `apple-touch-icon.png`, `android-chrome-*.png`, `site.webmanifest`) en la raíz.
- `CNAME` — dominio www.learnged.com.

## Aviso de marca
GED® is a registered trademark of the American Council on Education (ACE) and administered exclusively by GED Testing Service LLC under license. LearnGED is not affiliated with, endorsed by, or approved by ACE or GED Testing Service.
