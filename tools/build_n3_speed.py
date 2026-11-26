"""Level 3 · Topic 3 · Speed practice: irrational numbers (port of GEDparaHispanos math/fast_irracionales).
Builds math/level-3/speed-irrationals.html and es/matematicas/nivel-3/rapidez-irracionales.html.
The logic is in math/speed-irrationals.js (both languages); the styles in tools/speed.css."""
import os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSS = open(os.path.join(ROOT, "tools", "speed.css"), encoding="utf-8").read()
CSS += """  body{font-family:'Segoe UI',system-ui,sans-serif;}
  .lg-bar{display:flex;align-items:center;justify-content:space-between;gap:12px;flex-wrap:wrap;background:#fff;border-bottom:1px solid #e3e7ec;padding:8px 18px;}
  .lg-bar img{display:block;height:34px;width:auto}
  .lg-link{color:#1E3A5F;font-weight:700;text-decoration:none;font-size:15px}
  .lg-link:hover,.lg-link:focus{text-decoration:underline}
  @media print{.lg-bar{display:none}}
"""

def pagina(en):
    t = (lambda a, b: a) if en else (lambda a, b: b)
    lec = t("lesson-3-3.html", "leccion-3-3.html")
    return f'''<!DOCTYPE html>
<!-- LearnGED · {t("Speed practice: irrational numbers", "Ejercicios de rapidez: números irracionales")}
     José M. Fernández, ABE/ASE Math Master Teacher, Harry S. Truman College — City Colleges of Chicago · CC BY-NC-SA 4.0 -->
<html lang="{t("en", "es")}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{t("Speed practice · Irrational numbers · LearnGED", "Rapidez · Números irracionales · LearnGED")}</title>
<meta name="license" content="CC BY-NC-SA 4.0"><link rel="license" href="https://creativecommons.org/licenses/by-nc-sa/4.0/">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<style>
{CSS}</style>
</head>
<body>
<nav class="lg-bar" aria-label="LearnGED"><a class="lg-logo" href="{t("/", "/es/")}"><img src="/img/learnged-logo-horizontal.svg" alt="{t("LearnGED home", "Inicio de LearnGED")}" height="34"></a><a class="lg-link" href="{lec}#s-{t("homework", "tarea")}">{t("← Back to Lesson 3.3", "← Volver a la Lección 3.3")}</a></nav>
<div class="contenedor">
<header class="principal">
  <div class="ruta">{t("LearnGED · Math · Level 3 · Speed practice", "LearnGED · Matemáticas · Nivel 3 · Ejercicios de rapidez")}</div>
  <h1>{t("Irrational numbers against the clock", "Números irracionales contra reloj")}</h1>
  <p>{t("Classify, place, approximate, convert, and compare real numbers · Level 3, Topic 3", "Clasificar, ubicar, aproximar, convertir y comparar números reales · Nivel 3, Tema 3")}</p>
</header>
<main>
<section id="pantalla-inicio" aria-labelledby="t-inicio">
  <div class="tarjeta">
    <h2 id="t-inicio">{t("How it works", "Cómo funciona")}</h2>
    <ul class="instr">
      <li>{t("Each question has a time limit. If time runs out, the question counts as unanswered and the explanation is shown.", "Cada pregunta tiene un tiempo límite. Si se acaba, la pregunta cuenta como no contestada y se muestra la explicación.")}</li>
      <li>{t("After each answer you see an explanation of the steps. Read it calmly before you go on to the next one.", "Después de cada respuesta aparece la explicación del procedimiento. Lea con calma antes de pasar a la siguiente.")}</li>
      <li>{t("Work <strong>without a calculator</strong>: the goal is to recognize the numbers quickly, as in the part of the GED test where the calculator is not allowed.", "Trabaje <strong>sin calculadora</strong>: la meta es reconocer los números con rapidez, como en la parte del GED donde no se permite.")}</li>
      <li>{t("You can answer with the mouse or with the keys <strong>1</strong>, <strong>2</strong>, <strong>3</strong>, and <strong>4</strong>; the <strong>Enter</strong> key goes to the next question.", "Puede responder con el ratón o con las teclas <strong>1</strong>, <strong>2</strong>, <strong>3</strong> y <strong>4</strong>; la tecla <strong>Intro</strong> pasa a la siguiente pregunta.")}</li>
      <li>{t("If you prefer to go at your own pace, choose “No clock.”", "Si prefiere ir a su ritmo, elija «Sin reloj».")}</li>
    </ul>
  </div>
  <div class="tarjeta">
    <h2 id="t-modos">{t("Choose what to practice", "Elija qué practicar")}</h2>
    <p style="margin:0;">{t("Each option has its own link: you can save it or share it to go straight to that category.", "Cada opción tiene su propio enlace: puede guardarlo o compartirlo para ir directamente a esa categoría.")}</p>
    <nav aria-labelledby="t-modos"><ul class="modos" id="lista-modos"></ul></nav>
    <p class="elegido" id="elegido" aria-live="polite"></p>
    <div class="fila-ajustes" role="group" aria-labelledby="rot-tiempo">
      <span class="rot" id="rot-tiempo">{t("Time:", "Tiempo:")}</span>
      <button type="button" class="conmutador" id="con-tiempo" aria-pressed="true">{t("With clock", "Con reloj")}</button>
      <button type="button" class="conmutador" id="sin-tiempo" aria-pressed="false">{t("No clock (at my own pace)", "Sin reloj (a mi ritmo)")}</button>
    </div>
    <div class="botones"><button type="button" class="btn" id="btn-comenzar">{t("Start", "Comenzar")}</button></div>
  </div>
</section>
<section id="pantalla-juego" class="oculto" aria-labelledby="t-juego">
  <h2 id="t-juego" class="sr-only">{t("Current question", "Pregunta en curso")}</h2>
  <div class="tarjeta">
    <div class="barra-sup">
      <span class="contador" id="contador"></span>
      <span class="insignia" id="insignia"></span>
      <span class="puntos" id="puntos"></span>
    </div>
    <div class="progreso" aria-hidden="true"><div id="barra-progreso"></div></div>
    <div class="reloj" id="reloj">
      <span class="num" id="reloj-num" aria-hidden="true">30 s</span>
      <div class="pista" aria-hidden="true"><div id="reloj-barra"></div></div>
    </div>
    <p class="sr-only" id="aviso-reloj" aria-live="assertive"></p>
    <p class="pregunta-txt" id="pregunta-txt"></p>
    <div class="expresion" id="expresion"></div>
    <div class="opciones" id="opciones" role="group" aria-labelledby="pregunta-txt"></div>
    <div id="retro" class="retro oculto" aria-live="polite"></div>
    <div class="botones">
      <button type="button" class="btn oculto" id="btn-siguiente">{t("Next", "Siguiente")}</button>
      <button type="button" class="btn sec" id="btn-salir">{t("Finish now", "Terminar ahora")}</button>
    </div>
  </div>
</section>
<section id="pantalla-resultados" class="oculto" aria-labelledby="t-res">
  <div class="tarjeta">
    <h2 id="t-res" tabindex="-1">{t("Results", "Resultados")}</h2>
    <p class="marcador" id="marcador"></p>
    <p class="mensaje" id="mensaje"></p>
    <table class="desglose">
      <caption class="sr-only">{t("Correct answers in each category of the practice.", "Aciertos obtenidos en cada categoría del ejercicio.")}</caption>
      <thead><tr><th scope="col">{t("Category", "Categoría")}</th><th scope="col">{t("Correct", "Correctas")}</th><th scope="col">{t("Percent", "Porcentaje")}</th></tr></thead>
      <tbody id="tabla-desglose"></tbody>
    </table>
    <div id="consejo"></div>
    <div id="zona-fallos"></div>
    <div class="botones">
      <button type="button" class="btn" id="btn-repetir">{t("Try again with new numbers", "Repetir con otros números")}</button>
      <button type="button" class="btn sec" id="btn-inicio">{t("Back to the start", "Volver al inicio")}</button>
    </div>
  </div>
</section>
</main>
<footer>
  <p>{t("LearnGED · Math · Speed practice · Irrational numbers", "LearnGED · Matemáticas · Ejercicios de rapidez · Números irracionales")}</p>
  <p>José M. Fernández, ABE/ASE Math Master Teacher, Harry S. Truman College — City Colleges of Chicago</p>
  <p>© 2026. {t('This work is licensed under <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/" rel="license">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)</a>.', 'Esta obra está licenciada bajo <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/deed.es" rel="license">Creative Commons Reconocimiento-NoComercial-CompartirIgual 4.0 Internacional (CC BY-NC-SA 4.0)</a>.')}</p>
</footer>
</div>
<script src="/math/speed-irrationals.js"></script>
</body>
</html>
'''

for en, ruta in ((True, "math/level-3/speed-irrationals.html"), (False, "es/matematicas/nivel-3/rapidez-irracionales.html")):
    open(os.path.join(ROOT, ruta), "w", encoding="utf-8").write(pagina(en))
    print("ok", ruta)
