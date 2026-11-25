# LearnGED

Preparación gratuita para el GED® en inglés y español · Free GED® prep in English and Spanish.
Sitio: https://www.learnged.com (versión en español: `/es/`).

Evolución bilingüe de GEDparaHispanos. Mascota: **Leo**, el búho.

## Estructura
- `index.html` — portada en inglés (detecta el idioma del navegador; si es español, abre `/es/`).
- `es/` — versión en español. Las lecciones de Matemáticas en español están en `es/matematicas/nivel-1/` (leccion-T-N.html y practica-T-N.html), con el mismo contenido que las de `math/level-1/`.
- `math/lesson.js` y `math/practice.js` sirven a los dos idiomas: si la página tiene `<html lang="es">`, los mensajes salen en español.
- `js/calculator.js` (inglés) y `js/calculadora.js` (español) son el simulador de la TI-30XS; se generan con `tools/build-calculator-en.py` y `tools/build-calculadora-es.py` desde `algebra/calculadora-gph.js`.
- Herramientas para el español: `tools/ged_standards_es.py` (cuadro de estándares), `tools/build_indice_es.py` (índice del nivel) y `tools/espacios_es.py` (espacio fijo entre los grupos de miles).
- `learnged.css` — hoja de estilo común (paleta y tipografía Atkinson Hyperlegible).
- `img/` — logotipos y mascota.
- Favicon (`favicon.*`, `apple-touch-icon.png`, `android-chrome-*.png`, `site.webmanifest`) en la raíz.
- `CNAME` — dominio www.learnged.com.

## Aviso de marca
GED® is a registered trademark of the American Council on Education (ACE) and administered exclusively by GED Testing Service LLC under license. LearnGED is not affiliated with, endorsed by, or approved by ACE or GED Testing Service.
