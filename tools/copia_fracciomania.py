"""Copia Fracciomanía (interactivos/fraccion_operacion) a LearnGED: bilingüe (?lang=en|es), fuentes locales,
usted en español, dos intentos (pista y otra oportunidad) y texto para lectores de pantalla."""
import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding="utf-8").read()
def r(a, b, n=1):
    global s
    c = s.count(a)
    assert c == n, (c, a[:80])
    s = s.replace(a, b)

r('<!DOCTYPE html>\n<html lang="es">', '<!DOCTYPE html>\n<!-- LearnGED · Fracciomanía: game of fractions (English and Spanish; the language goes in the link: ?lang=en or ?lang=es)\n     Copy of interactivos/fraccion_operacion, adapted for LearnGED · José M. Fernández · CC BY-NC-SA 4.0 -->\n<html lang="es">')
r('<title>Fracciomanía — Juego de fracciones | GEDparaHispanos</title>', '<title>Fracciomanía · LearnGED</title>\n<meta name="license" content="CC BY-NC-SA 4.0"><link rel="license" href="https://creativecommons.org/licenses/by-nc-sa/4.0/">')
i = s.index(' <link rel="icon"'); j = s.index('\n', i)
s = s[:i] + '<link rel="icon" href="/favicon.svg" type="image/svg+xml">' + s[j:]
r('<link rel="preconnect" href="https://fonts.googleapis.com">\n<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n<link href="https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&family=Nunito:wght@600;700;800&display=swap" rel="stylesheet">',
  '<link href="/fonts/fonts.css" rel="stylesheet">')
s = s.replace("'Fredoka', sans-serif", "'Poppins', sans-serif").replace("'Nunito', system-ui, sans-serif", "'Atkinson Hyperlegible', system-ui, sans-serif")
r('<style>', '<style>\n  .sr-only{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border:0}\n  .barra-lg{max-width:900px;margin:0 auto 6px;display:flex;justify-content:space-between;align-items:center;gap:10px;flex-wrap:wrap;font-size:15px;font-weight:700}\n  .barra-lg a{color:#002060}', 1)

# texts of the page → data-tx keys, filled by the script
r('<div class="pantalla">', '<div class="pantalla">\n  <nav class="barra-lg" aria-label="LearnGED"><a id="lnkInicio" href="/es/"><img src="/img/learnged-logo-horizontal.svg" alt="LearnGED" height="30"></a><a id="lnkVolver" href="/es/matematicas/nivel-2/practica-2-1.html" data-tx="volver">← Práctica de la Lección 2.1</a></nav>')
r('<div class="subtitulo">Suma, resta, multiplica y divide fracciones — ¡como un juego!</div>', '<div class="subtitulo" data-tx="subtitulo">Suma, resta, multiplica y divide fracciones como en un juego.</div>')
r('<span class="etiqueta">Puntos</span>', '<span class="etiqueta" data-tx="puntos">Puntos</span>')
r('<span class="etiqueta">Racha</span>', '<span class="etiqueta" data-tx="racha">Racha</span>')
r('<span class="etiqueta">Pregunta</span>', '<span class="etiqueta" data-tx="pregunta">Pregunta</span>')
r('aria-label="Pregunta actual"', 'aria-label="Pregunta actual" data-txa="preguntaActual"')
r('aria-label="Opciones de respuesta"', 'aria-label="Opciones de respuesta" data-txa="opciones"')
r('<div class="pista" id="pista"></div>', '<div class="pista" id="pista" role="status" aria-live="polite"></div>')
r('>Siguiente pregunta ➡️</button>', ' data-tx="siguiente">Siguiente pregunta ➡️</button>')
r('>🔄 Empezar de nuevo</button>', ' data-tx="reiniciar">🔄 Empezar de nuevo</button>')
r('<p>GEDparaHispanos · Profesor José M. Fernández — Truman College</p>',
  '<p>LearnGED · José M. Fernández, ABE/ASE Math Master Teacher, Harry S. Truman College — City Colleges of Chicago · <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/" rel="license" style="color:inherit">CC BY-NC-SA 4.0</a></p>\n    <p data-tx="marca" style="font-size:.85em;margin-top:4px">GED® es una marca registrada del American Council on Education (ACE), administrada exclusivamente por GED Testing Service LLC bajo licencia. LearnGED no está afiliado a ACE ni a GED Testing Service.</p>')

# dictionary and language
r("  'use strict';\n", """  'use strict';
  const LANG = (function(){ var l = null; try { l = new URLSearchParams(location.search).get('lang'); } catch (e) {}
    if (l !== 'en' && l !== 'es') l = (navigator.language || 'en').toLowerCase().indexOf('es') === 0 ? 'es' : 'en'; return l; })();
  const T = LANG === 'en' ? {
    subtitulo: 'Add, subtract, multiply, and divide fractions, like a game.', puntos: 'Points', racha: 'Streak', pregunta: 'Question',
    preguntaActual: 'Current question', opciones: 'Answer choices', siguiente: 'Next question ➡️', reiniciar: '🔄 Start over',
    volver: '← Practice for Lesson 2.1', marca: 'GED® is a registered trademark of the American Council on Education (ACE) and administered exclusively by GED Testing Service LLC under license. LearnGED is not affiliated with ACE or GED Testing Service.',
    ops: { '+': 'Addition', '−': 'Subtraction', '×': 'Multiplication', '÷': 'Division' },
    entero: 'Remember: a whole number like <b>3</b> can be written as <b>3/1</b>.', mixto: 'First change the <b>mixed numbers</b> to improper fractions.',
    suma: 'To <b>add or subtract</b> you need a <b>common denominator</b>.', mult: 'To <b>multiply</b>: numerator × numerator and denominator × denominator.',
    div: 'To <b>divide</b>: <b>flip the second</b> fraction and multiply.', final: 'At the end, <b>simplify</b> and write it as a mixed number if it is more than 1.',
    pista: (op) => `💡 <b>Hint for this ${op}:</b> `, otra: ' <b>Choose again.</b>', era: (x) => `The answer was ${x}. Press <b>Next question</b>.`,
    menos: 'minus', y: 'and', sobre: 'over', igual: 'equals what?'
  } : {
    subtitulo: 'Sume, reste, multiplique y divida fracciones como en un juego.', puntos: 'Puntos', racha: 'Racha', pregunta: 'Pregunta',
    preguntaActual: 'Pregunta actual', opciones: 'Opciones de respuesta', siguiente: 'Siguiente pregunta ➡️', reiniciar: '🔄 Empezar de nuevo',
    volver: '← Práctica de la Lección 2.1', marca: 'GED® es una marca registrada del American Council on Education (ACE), administrada exclusivamente por GED Testing Service LLC bajo licencia. LearnGED no está afiliado a ACE ni a GED Testing Service.',
    ops: { '+': 'Suma', '−': 'Resta', '×': 'Multiplicación', '÷': 'División' },
    entero: 'Recuerde: un entero como <b>3</b> se puede escribir como <b>3/1</b>.', mixto: 'Convierta primero los <b>números mixtos</b> en fracciones impropias.',
    suma: 'Para <b>sumar o restar</b> hace falta un <b>denominador común</b>.', mult: 'Para <b>multiplicar</b>: numerador × numerador y denominador × denominador.',
    div: 'Para <b>dividir</b>: <b>dé vuelta la segunda</b> fracción y multiplique.', final: 'Al final, <b>simplifique</b> y escríbala como número mixto si es mayor que 1.',
    pista: (op) => `💡 <b>Pista para esta ${op}:</b> `, otra: ' <b>Elija otra vez.</b>', era: (x) => `La respuesta era ${x}. Pulse <b>Siguiente pregunta</b>.`,
    menos: 'menos', y: 'y', sobre: 'sobre', igual: '¿igual a cuánto?'
  };
  document.documentElement.lang = LANG;
  document.querySelectorAll('[data-tx]').forEach(e => { e.textContent = T[e.dataset.tx]; });
  document.querySelectorAll('[data-txa]').forEach(e => { e.setAttribute('aria-label', T[e.dataset.txa]); });
  document.getElementById('lnkInicio').href = LANG === 'en' ? '/' : '/es/';
  document.getElementById('lnkVolver').href = LANG === 'en' ? '/math/level-2/practice-2-1.html' : '/es/matematicas/nivel-2/practica-2-1.html';
""")
r("const NOMBRES_OP = { '+': 'Suma', '−': 'Resta', '×': 'Multiplicación', '÷': 'División' };", "const NOMBRES_OP = T.ops;")
# screen reader text for each fraction
r("  function frac2html(f) {\n", """  function fracTxt(f) {
    const neg = f.num < 0 ? T.menos + ' ' : '', a = Math.abs(f.num);
    if (f.den === 1) return neg + a;
    if (a < f.den) return neg + a + ' ' + T.sobre + ' ' + f.den;
    const e = Math.trunc(a / f.den), rr = a % f.den;
    return rr === 0 ? neg + e : neg + e + ' ' + T.y + ' ' + rr + ' ' + T.sobre + ' ' + f.den;
  }
  function frac2html(f) { return '<span aria-hidden="true">' + frac2html0(f) + '</span><span class="sr-only">' + fracTxt(f) + '</span>'; }
  function frac2html0(f) {
""")
r("""    if (tieneEntero) consejos.push('Recuerda: un entero como <b>3</b> se puede escribir como <b>3/1</b>.');
    if (tieneMixto)  consejos.push('Convierte primero los <b>números mixtos</b> a fracciones impropias.');""",
  """    if (tieneEntero) consejos.push(T.entero);
    if (tieneMixto)  consejos.push(T.mixto);""")
r("consejos.push('Para <b>sumar o restar</b> necesitas <b>denominador común</b>.');", "consejos.push(T.suma);")
r("consejos.push('Para <b>multiplicar</b>: numerador × numerador y denominador × denominador.');", "consejos.push(T.mult);")
r("consejos.push('Para <b>dividir</b>: <b>invierte la segunda</b> fracción y multiplica.');", "consejos.push(T.div);")
r("consejos.push('Al final, <b>simplifica</b> y conviértela a número mixto si aplica.');", "consejos.push(T.final);")
r("return `💡 <b>Pista para esta ${op}:</b> ` + consejos.join(' ');", "return T.pista(op) + consejos.join(' ');")
r("const op = NOMBRES_OP[p.op].toLowerCase();", "const op = LANG === 'en' ? NOMBRES_OP[p.op].toLowerCase() : NOMBRES_OP[p.op].toLowerCase();")
# two tries: a hint and another try, then the answer
r("""  function responder(indice, tarjeta) {
    if (estado.bloqueado) return;
    estado.bloqueado = true;
    sonidoClick();

    const p = estado.problema;
    const correcta = indice === p.indiceCorrecto;
    const todasTarjetas = document.querySelectorAll('.tarjeta');
    todasTarjetas.forEach(t => t.classList.add('bloqueada'));
""", """  function responder(indice, tarjeta) {
    if (estado.bloqueado || tarjeta.classList.contains('incorrecta')) return;
    sonidoClick();

    const p = estado.problema;
    const correcta = indice === p.indiceCorrecto;
    estado.intentos = (estado.intentos || 0) + 1;
    if (!correcta && estado.intentos === 1) {
      tarjeta.classList.add('incorrecta');
      tarjeta.disabled = true;
      sonidoIncorrecto();
      mostrarFeedback(pick(['🤔', '🧐', '💭']));
      const pista1 = $('pista');
      pista1.innerHTML = generaPista(p) + T.otra;
      pista1.classList.add('activa');
      return;
    }
    estado.bloqueado = true;
    const todasTarjetas = document.querySelectorAll('.tarjeta');
    todasTarjetas.forEach(t => t.classList.add('bloqueada'));
""")
r("""      const pista = $('pista');
      pista.innerHTML = generaPista(p);
      pista.classList.add('activa');""", """      const pista = $('pista');
      pista.innerHTML = generaPista(p) + ' ' + T.era('<b>' + fracTxt(p.opciones[p.indiceCorrecto]) + '</b>');
      pista.classList.add('activa');""")
r("""    estado.bloqueado = false;
  }""", """    estado.bloqueado = false;
    estado.intentos = 0;
  }""")
r("const html = `${frac2html(p.f1)} <span class=\"op\">${p.op}</span> ${frac2html(p.f2)} <span class=\"op\">=</span> <span class=\"op\">?</span>`;",
  "const html = `${frac2html(p.f1)} <span class=\"op\">${p.op}</span> ${frac2html(p.f2)} <span class=\"op\" aria-hidden=\"true\">= ?</span><span class=\"sr-only\">${T.igual}</span>`;")
open(dst, "w", encoding="utf-8").write(s)
print("ok", dst)
