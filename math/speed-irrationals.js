/* LearnGED · Speed practice: irrational numbers (English and Spanish; the language comes from <html lang>).
   Ported from GEDparaHispanos math/fast_irracionales · José M. Fernández · CC BY-NC-SA 4.0 */
(function () {
  'use strict';
  var EN = document.documentElement.lang === 'en';
  function T(en, es) { return EN ? en : es; }

  /* ───────── Helpers ───────── */
  function rnd(a, b) { return a + Math.floor(Math.random() * (b - a + 1)); }
  function pick(arr) { return arr[rnd(0, arr.length - 1)]; }
  function mezclar(a) { a = a.slice(); for (var i = a.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)); var t = a[i]; a[i] = a[j]; a[j] = t; } return a; }
  function esCuadrado(n) { var r = Math.round(Math.sqrt(n)); return r * r === n; }
  function mcd(a, b) { while (b) { var t = b; b = a % b; a = t; } return a; }
  function frac(n, d) { var g = mcd(n, d); return d / g === 1 ? String(n / g) : (n / g) + '/' + (d / g); }
  function noCuadrado(min, max) { var n; do { n = rnd(min, max); } while (esCuadrado(n)); return n; }
  function f1(x) { return x.toFixed(1); }
  function f2(x) { return x.toFixed(2); }
  function aprox(v) { return Math.abs(v * 100 - Math.round(v * 100)) < 1e-9 ? '= ' + f2(v) : '≈ ' + f2(v); }

  /* The correct option goes first in the list; then the list is shuffled (unless a fixed order is given) */
  function armar(cat, texto, expr, correcta, distractores, explica, fijo) {
    var lista = [correcta].concat(distractores), vistos = {};
    lista.forEach(function (o) { if (vistos[o]) throw new Error('Repeated option: ' + o); vistos[o] = 1; });
    var ops = fijo ? fijo.slice() : mezclar(lista);
    return { cat: cat, texto: texto, expr: expr, ops: ops, correcta: ops.indexOf(correcta), explica: explica };
  }

  /* ───────── 1. Classify ───────── */
  var NAT = T('Natural', 'Natural'), ENT = T('Integer', 'Entero'), RAC = T('Rational', 'Racional'), IRR = T('Irrational', 'Irracional');
  function genClasificar() {
    var OPS = [NAT, ENT, RAC, IRR];
    var texto = T('What is the most specific set this number belongs to?', '¿Cuál es el conjunto más específico al que pertenece este número?');
    var tipo = rnd(0, 3), expr, c, exp, k, v;
    if (tipo === 0) {
      k = rnd(2, 12); expr = '√' + (k * k); c = NAT;
      exp = [T('√' + (k * k) + ' = ' + k + ', because ' + k + '² = ' + (k * k) + '.', '√' + (k * k) + ' = ' + k + ', porque ' + k + '² = ' + (k * k) + '.'),
             T('The root is exact and gives a counting number: it is natural (and also an integer, rational, and real).', 'La raíz es exacta y da un número de contar: es natural (y también entero, racional y real).')];
    } else if (tipo === 1) {
      v = rnd(0, 3); c = ENT;
      if (v <= 1) { k = rnd(2, 15); expr = '−' + k; exp = [T('−' + k + ' is negative and has no decimal part.', '−' + k + ' es negativo y no tiene parte decimal.'), T('It belongs to the integers, but not to the natural numbers, which start at 1.', 'Pertenece a los enteros, pero no a los naturales, que empiezan en 1.')]; }
      else if (v === 2) { k = rnd(2, 9); expr = '−√' + (k * k); exp = [T('−√' + (k * k) + ' = −' + k + ': the root is exact and the sign is negative.', '−√' + (k * k) + ' = −' + k + ': la raíz es exacta y el signo es negativo.'), T('Its most specific set is the integers.', 'Su conjunto más específico es el de los enteros.')]; }
      else { expr = '0'; exp = [T('0 is an integer, but not a natural number: the natural numbers start at 1.', 'El 0 es entero, pero no natural: los naturales empiezan en 1.')]; }
    } else if (tipo === 2) {
      v = rnd(0, 3); c = RAC;
      if (v === 0) {
        var b = pick([2, 3, 4, 5, 7, 8]), a; do { a = rnd(1, 15); } while (a % b === 0);
        expr = a + '/' + b; exp = [T(expr + ' is a fraction of two integers that does not give a whole number.', expr + ' es una fracción de dos enteros que no da un número entero.'), T('Every fraction of integers is a rational number.', 'Toda fracción de enteros es un número racional.')];
      } else if (v === 1) {
        var w = rnd(0, 9), cen; do { cen = rnd(1, 99); } while (cen % 10 === 0);
        expr = w + '.' + (cen < 10 ? '0' + cen : cen);
        var fr = (w * 100 + cen) + '/100' + (frac(w * 100 + cen, 100) !== (w * 100 + cen) + '/100' ? ' = ' + frac(w * 100 + cen, 100) : '');
        exp = [T('The decimal ' + expr + ' ends, so it can be written as a fraction: ' + fr + '.', 'El decimal ' + expr + ' termina, así que se puede escribir como fracción: ' + fr + '.'), T('That is why it is rational.', 'Por eso es racional.')];
      } else if (v === 2) {
        var d = pick([1, 2, 4, 5, 7, 8]);
        expr = '0.' + d + d + d + '…';
        exp = [T('The decimal ' + expr + ' repeats forever with the same pattern.', 'El decimal ' + expr + ' se repite sin fin con el mismo patrón.'), T('Every repeating decimal is rational: ' + expr + ' = ' + frac(d, 9) + '.', 'Todo decimal periódico es racional: ' + expr + ' = ' + frac(d, 9) + '.')];
      } else {
        var bb = pick([3, 4, 5, 7]), aa; do { aa = rnd(1, 9); } while (aa % bb === 0);
        expr = '−' + aa + '/' + bb; exp = [T(expr + ' is a negative fraction of two integers and does not give a whole number.', expr + ' es una fracción negativa de dos enteros y no da un número entero.'), T('It is rational (it is not an integer or a natural number).', 'Es racional (no es entero ni natural).')];
      }
    } else {
      v = rnd(0, 3); c = IRR;
      if (v <= 1) {
        var n = noCuadrado(2, 99), r = Math.floor(Math.sqrt(n));
        expr = '√' + n;
        exp = [T(n + ' is not a perfect square: it is between ' + (r * r) + ' and ' + ((r + 1) * (r + 1)) + '.', n + ' no es cuadrado perfecto: está entre ' + (r * r) + ' y ' + ((r + 1) * (r + 1)) + '.'),
               T('Its root is not exact; its decimal (≈ ' + f2(Math.sqrt(n)) + '…) does not end or repeat. It is irrational.', 'Su raíz no es exacta; su decimal (≈ ' + f2(Math.sqrt(n)) + '…) no termina ni se repite. Es irracional.')];
      } else if (v === 2) {
        expr = 'π'; exp = [T('π ≈ 3.14159… has endless decimals that do not repeat.', 'π ≈ 3.14159… tiene infinitos decimales que no se repiten.'), T('It cannot be written as an exact fraction: it is irrational. (22/7 and 3.14 are only approximations.)', 'No se puede escribir como fracción exacta: es irracional. (22/7 y 3.14 son solo aproximaciones.)')];
      } else {
        var kk = rnd(2, 5), m = pick([2, 3, 5, 6, 7]);
        expr = kk + '√' + m; exp = [T('√' + m + ' is irrational, because ' + m + ' is not a perfect square.', '√' + m + ' es irracional, porque ' + m + ' no es cuadrado perfecto.'), T('A whole number times an irrational number is still irrational: ' + expr + ' is irrational.', 'Un entero por un irracional sigue siendo irracional: ' + expr + ' es irracional.')];
      }
    }
    return armar('clasificar', texto, expr, c, OPS.filter(function (o) { return o !== c; }), exp, OPS);
  }

  /* ───────── 2. Place on the number line ───────── */
  function par(a) { return T('Between ' + a + ' and ' + (a + 1), 'Entre ' + a + ' y ' + (a + 1)); }
  function genRecta() {
    var expr, a, exp, mitad = null;
    if (Math.random() < 0.2) {
      var o = pick([{ e: 'π', v: Math.PI }, { e: '2π', v: 2 * Math.PI }, { e: '3π', v: 3 * Math.PI }, { e: 'π/2', v: Math.PI / 2 }]);
      expr = o.e; a = Math.floor(o.v);
      exp = [T('π ≈ 3.14, so ' + o.e + ' ≈ ' + f2(o.v) + '.', 'π ≈ 3.14, así que ' + o.e + ' ≈ ' + f2(o.v) + '.'), T('That value is between ' + a + ' and ' + (a + 1) + '.', 'Ese valor queda entre ' + a + ' y ' + (a + 1) + '.')];
    } else {
      var n = noCuadrado(5, 150);
      a = Math.floor(Math.sqrt(n)); expr = '√' + n; mitad = Math.floor(n / 2);
      exp = [(a * a) + ' < ' + n + ' < ' + ((a + 1) * (a + 1)) + T(', that is, ', ', es decir, ') + a + '² < ' + n + ' < ' + (a + 1) + '².',
             T('So ', 'Por lo tanto ') + a + ' < √' + n + ' < ' + (a + 1) + '.',
             T('A common mistake: dividing the number by 2. The square root is not half the number.', 'Error frecuente: dividir el número entre 2. La raíz cuadrada no es la mitad del número.')];
    }
    var cands = [];
    if (mitad !== null && Math.abs(mitad - a) > 1) cands.push(mitad);
    if (a - 1 >= 0) cands.push(a - 1);
    cands.push(a + 1);
    var extra = a + 2;
    while (cands.length < 3) { if (cands.indexOf(extra) < 0 && extra !== a) cands.push(extra); extra++; }
    cands = cands.slice(0, 3);
    return armar('recta', T('Between which two consecutive whole numbers is this number?', '¿Entre qué dos enteros consecutivos se ubica este número?'), expr, par(a), cands.map(par), exp);
  }

  /* ───────── 3. Approximate to the tenth ───────── */
  function genAproximar() {
    var n, L, c, a, cL, cH, dL, dH;
    for (;;) {
      n = noCuadrado(2, 99);
      var r = Math.sqrt(n);
      L = Math.floor(r * 10); c = Math.round(r * 10);
      cL = L * L / 100; cH = (L + 1) * (L + 1) / 100;
      dL = n - cL; dH = cH - n;
      var metodo = dL < dH ? L : L + 1;
      if (metodo === c && Math.abs(dL - dH) > 0.02) break;
    }
    a = Math.floor(Math.sqrt(n));
    var lin = Math.round((a + (n - a * a) / (2 * a + 1)) * 10);
    var dist = [c - 1, c + 1];
    if (lin !== c && dist.indexOf(lin) < 0) dist.push(lin);
    else dist.push(c + 2 <= (a + 1) * 10 ? c + 2 : c - 2);
    var cerca = dL < dH ? cL : cH;
    var exp = [T('√' + n + ' is between ' + a + ' and ' + (a + 1) + ', because ' + a + '² = ' + (a * a) + ' and ' + (a + 1) + '² = ' + ((a + 1) * (a + 1)) + '.', '√' + n + ' está entre ' + a + ' y ' + (a + 1) + ', porque ' + a + '² = ' + (a * a) + ' y ' + (a + 1) + '² = ' + ((a + 1) * (a + 1)) + '.'),
               T('Try the neighboring tenths: (' + f1(L / 10) + ')² = ' + f2(cL) + ' and (' + f1((L + 1) / 10) + ')² = ' + f2(cH) + '.', 'Se prueban las décimas vecinas: (' + f1(L / 10) + ')² = ' + f2(cL) + ' y (' + f1((L + 1) / 10) + ')² = ' + f2(cH) + '.'),
               T(n + ' is closer to ' + f2(cerca) + ', so √' + n + ' ≈ ' + f1(c / 10) + '.', n + ' está más cerca de ' + f2(cerca) + ', así que √' + n + ' ≈ ' + f1(c / 10) + '.')];
    if (lin !== c) exp.push(T('Careful: splitting the distance between ' + (a * a) + ' and ' + ((a + 1) * (a + 1)) + ' into equal parts gives ' + f1(lin / 10) + ', which is not right. Square roots do not grow evenly; that is why you square the tenths.', 'Cuidado: repartir la distancia en partes iguales entre ' + (a * a) + ' y ' + ((a + 1) * (a + 1)) + ' da ' + f1(lin / 10) + ', que no es correcto. Las raíces no crecen de forma pareja; por eso se elevan las décimas al cuadrado.'));
    return armar('aproximar', T('Approximate to the nearest tenth:', 'Aproxime a la décima más cercana:'), '√' + n, f1(c / 10), dist.map(function (x) { return f1(x / 10); }), exp);
  }

  /* ───────── 4. Decimals and fractions ───────── */
  function genDecimales() {
    var v = rnd(0, 2), d, expr, exp, tx = T('What fraction is equal to this repeating decimal?', '¿Qué fracción es igual a este decimal periódico?');
    if (v === 0) {
      d = rnd(1, 8); expr = '0.' + d + d + d + '…';
      var fd = d + '/9' + (frac(d, 9) !== d + '/9' ? ' = ' + frac(d, 9) : '');
      exp = [T('Let x = ' + expr + ' Multiply by 10: 10x = ' + d + '.' + d + d + d + '…', 'Sea x = ' + expr + ' Al multiplicar por 10: 10x = ' + d + '.' + d + d + d + '…'),
             T('Subtract: 10x − x = ' + d + ', that is, 9x = ' + d + '.', 'Se resta: 10x − x = ' + d + ', es decir, 9x = ' + d + '.'),
             T('x = ' + fd + '. One repeating digit goes over 9, not over 10.', 'x = ' + fd + '. Una cifra que se repite va sobre 9, no sobre 10.')];
      return armar('decimales', tx, expr, frac(d, 9), [d + '/10', d + '/90', d + '/100'], exp);
    }
    if (v === 1) {
      var ab; do { ab = rnd(10, 98); } while (ab % 11 === 0);
      expr = '0.' + ab + ab + ab + '…';
      var fab = ab + '/99' + (frac(ab, 99) !== ab + '/99' ? ' = ' + frac(ab, 99) : '');
      exp = [T('Let x = ' + expr + ' Two digits repeat, so multiply by 100: 100x = ' + ab + '.' + ab + ab + '…', 'Sea x = ' + expr + ' Se repiten dos cifras, así que se multiplica por 100: 100x = ' + ab + '.' + ab + ab + '…'),
             T('Subtract: 100x − x = ' + ab + ', that is, 99x = ' + ab + '.', 'Se resta: 100x − x = ' + ab + ', es decir, 99x = ' + ab + '.'),
             T('x = ' + fab + '. Two repeating digits go over 99.', 'x = ' + fab + '. Dos cifras que se repiten van sobre 99.')];
      return armar('decimales', tx, expr, frac(ab, 99), [ab + '/100', ab + '/90', ab + '/999'], exp);
    }
    d = rnd(1, 9);
    var irr = '0.' + d + '0' + d + '00' + d + '000' + d + '…';
    var x = rnd(1, 9), y; do { y = rnd(1, 9); } while (y === x);
    var per2 = '0.' + x + y + x + y + x + y + '…';
    var z = rnd(1, 9), term = '0.' + z + rnd(1, 9) + rnd(1, 9) + pick([1, 2, 4, 5, 6, 8]);
    var w = rnd(1, 9), per1 = '0.' + w + w + w + w + w + '…';
    exp = [T('In ' + irr + ' the number of zeros keeps growing: the pattern never repeats the same way, and the decimal does not end. It is irrational.', 'En ' + irr + ' la cantidad de ceros aumenta cada vez: el patrón nunca se repite igual y el decimal no termina. Es irracional.'),
           T(per2 + ' and ' + per1 + ' always repeat the same way: they are repeating decimals, so they are rational.', per2 + ' y ' + per1 + ' se repiten siempre igual: son periódicos y, por lo tanto, racionales.'),
           T(term + ' ends: it is rational too.', term + ' termina: también es racional.')];
    return armar('decimales', T('Which of these decimals is irrational?', '¿Cuál de estos decimales es irracional?'), '?', irr, [per2, term, per1], exp);
  }

  /* ───────── 5. Compare and order ───────── */
  function itemRaiz() { var n = noCuadrado(2, 50); return { t: '√' + n, v: Math.sqrt(n) }; }
  function itemPi() { return { t: 'π', v: Math.PI }; }
  function itemFrac() { var b = pick([2, 3, 4, 5, 6, 8]), a; do { a = rnd(b + 1, 7 * b); } while (a % b === 0); return { t: a + '/' + b, v: a / b }; }
  function itemDec() { var x; do { x = rnd(11, 69); } while (x % 10 === 0); return { t: f1(x / 10), v: x / 10 }; }
  function itemEnt() { var k = rnd(1, 7); return { t: String(k), v: k }; }
  function genComparar() {
    if (Math.random() < 0.45) {
      var n, k, rel, exp;
      if (Math.random() < 0.15) { k = rnd(2, 10); n = k * k; }
      else { n = noCuadrado(3, 120); var a = Math.floor(Math.sqrt(n)); k = pick([a, a + 1]); }
      rel = n < k * k ? '<' : (n > k * k ? '>' : '=');
      exp = [T('Compare the squares: (√' + n + ')² = ' + n + ' and ' + k + '² = ' + (k * k) + '.', 'Se comparan los cuadrados: (√' + n + ')² = ' + n + ' y ' + k + '² = ' + (k * k) + '.'),
             n + ' ' + rel + ' ' + (k * k) + T(', so √', ', por lo tanto √') + n + ' ' + rel + ' ' + k + '.'];
      return armar('comparar', T('Which symbol completes the comparison?', '¿Qué símbolo completa la comparación?'), '√' + n + '  ▢  ' + k, rel, ['<', '>', '='].filter(function (s) { return s !== rel; }), exp, ['<', '>', '=']);
    }
    var fabricas = [itemRaiz, itemPi, itemFrac, itemDec, itemEnt], items, ok;
    do {
      items = [itemRaiz()];
      mezclar([1, 2, 3, 4, 0]).slice(0, 3).forEach(function (t) { items.push(fabricas[t]()); });
      var orden = items.slice().sort(function (p, q) { return p.v - q.v; });
      ok = true;
      for (var i = 1; i < orden.length; i++) if (orden[i].v - orden[i - 1].v < 0.08) ok = false;
      var txt = {}; items.forEach(function (it) { if (txt[it.t]) ok = false; txt[it.t] = 1; });
    } while (!ok);
    var mayor = Math.random() < 0.5;
    var ord = items.slice().sort(function (p, q) { return mayor ? q.v - p.v : p.v - q.v; });
    var exp2 = [T('Approximate each number: ', 'Se aproxima cada número: ') + ord.map(function (it) { return it.t + ' ' + aprox(it.v); }).join(' · ') + '.',
                (mayor ? T('From greatest to least: ', 'De mayor a menor: ') : T('From least to greatest: ', 'De menor a mayor: ')) + ord.map(function (it) { return it.t; }).join(', ') + '.'];
    return armar('comparar', mayor ? T('Which of these numbers is the greatest?', '¿Cuál de estos números es el mayor?') : T('Which of these numbers is the least?', '¿Cuál de estos números es el menor?'),
      ord.map(function (it) { return it.t; }).sort().join('   ·   '), ord[0].t, ord.slice(1).map(function (it) { return it.t; }), exp2);
  }

  /* ───────── Categories ───────── */
  var L33 = T('lesson-3-3.html', 'leccion-3-3.html'), L32 = T('lesson-3-2.html', 'leccion-3-2.html');
  var P33 = T('practice-3-3.html', 'practica-3-3.html'), P32 = T('practice-3-2.html', 'practica-3-2.html');
  var CATS = {
    clasificar: { nombre: T('Classify numbers', 'Clasificar números'), desc: T('Natural, integer, rational, or irrational', 'Natural, entero, racional o irracional'), color: '#00695c', gen: genClasificar, tiempo: 25,
      consejo: T('Review the diagram of the sets: each number goes in the smallest set that contains it. Exact roots (√9, √49) are not irrational.', 'Repase el diagrama de los conjuntos: cada número va en el conjunto más pequeño que lo contiene. Las raíces exactas (√9, √49) no son irracionales.'),
      lec: L33 + T('#s-real-numbers', '#s-numeros-reales'), inter: P33 + T('#classify', '#clasificar') },
    recta: { nombre: T('Place on the number line', 'Ubicar en la recta'), desc: T('Between which two whole numbers √n or π falls', 'Entre qué dos enteros cae √n o π'), color: '#1565c0', gen: genRecta, tiempo: 30,
      consejo: T('Find the two perfect squares that surround the number. It helps to know the squares from 1 to 15 by heart.', 'Busque los dos cuadrados perfectos que encierran al número. Conviene tener en la memoria los cuadrados del 1 al 15.'),
      lec: L33 + T('#s-number-line', '#s-recta'), inter: P33 + T('#number-line', '#recta') },
    aproximar: { nombre: T('Approximate to the tenth', 'Aproximar a la décima'), desc: T('The value of √n with one decimal place', 'El valor de √n con un decimal'), color: '#6a1b9a', gen: genAproximar, tiempo: 45,
      consejo: T('First trap the root between two whole numbers; then square the two neighboring tenths and choose the one closer to the number.', 'Primero acorrale la raíz entre dos enteros; después eleve al cuadrado las dos décimas vecinas y elija la que queda más cerca del número.'),
      lec: L32 + T('#s-approximate', '#s-aproximar'), inter: P32 + T('#approximate', '#aproximar') },
    decimales: { nombre: T('Decimals and fractions', 'Decimales y fracciones'), desc: T('Repeating decimals to fractions; which decimal is irrational', 'Periódicos a fracción; cuál decimal es irracional'), color: '#5C3900', gen: genDecimales, tiempo: 40,
      consejo: T('One repeating digit goes over 9, and two digits go over 99. A decimal is irrational only if it does not end and does not repeat a pattern.', 'Una cifra que se repite va sobre 9 y dos cifras sobre 99. Un decimal es irracional solo si no termina y no repite un patrón.'),
      lec: L33 + T('#s-repeating', '#s-periodicos'), inter: P33 + T('#repeating', '#periodicos') },
    comparar: { nombre: T('Compare and order', 'Comparar y ordenar'), desc: T('Greatest, least, or symbol between real numbers', 'Mayor, menor o símbolo entre números reales'), color: '#ad1457', gen: genComparar, tiempo: 40,
      consejo: T('To compare a root with a whole number, compare their squares. To order several numbers, approximate each one to two decimal places.', 'Para comparar una raíz con un entero, compare sus cuadrados. Para ordenar varios números, aproxime cada uno a dos decimales.'),
      lec: L33 + T('#s-number-line', '#s-recta'), inter: P33 + T('#rational-irrational', '#racional-irracional') }
  };
  var ORDEN = ['clasificar', 'recta', 'aproximar', 'decimales', 'comparar'];

  function construirLista(modo) {
    var lista = [], vistos = {};
    function agregar(cat) {
      for (var t = 0; t < 40; t++) {
        var q = CATS[cat].gen(), clave = q.texto + '|' + q.expr + '|' + q.ops.join(',');
        if (!vistos[clave]) { vistos[clave] = 1; lista.push(q); return; }
      }
      lista.push(CATS[cat].gen());
    }
    if (modo === 'todo') { ORDEN.forEach(function (c) { for (var i = 0; i < 4; i++) agregar(c); }); return mezclar(lista); }
    for (var i = 0; i < 10; i++) agregar(modo);
    return lista;
  }
  window.__rapidez = { CATS: CATS, construirLista: construirLista };

  /* ───────── Interface ───────── */
  function $(id) { return document.getElementById(id); }
  var IDS = { todo: T('all', 'todo'), clasificar: T('classify', 'clasificar'), recta: T('number-line', 'recta'), aproximar: T('approximate', 'aproximar'), decimales: T('decimals', 'decimales'), comparar: T('compare', 'comparar') };
  var MODOS = [{ id: 'todo', nombre: T('All five categories', 'Las cinco categorías'), desc: T('20 mixed questions', '20 preguntas mezcladas'), color: '#004d40' }]
    .concat(ORDEN.map(function (c) { return { id: c, nombre: CATS[c].nombre, desc: CATS[c].desc + T(' · 10 questions', ' · 10 preguntas'), color: CATS[c].color }; }));
  var estado = { modo: 'todo', reloj: true, lista: [], i: 0, aciertos: 0, respuestas: [], restante: 0, temporizador: null, respondida: false, inicio: 0 };

  var ul = $('lista-modos');
  MODOS.forEach(function (m) {
    var li = document.createElement('li'), a = document.createElement('a');
    a.className = 'modo'; a.href = '#' + IDS[m.id]; a.id = 'modo-' + m.id;
    a.style.setProperty('--c', m.color);
    var s = document.createElement('strong'); s.textContent = m.nombre;
    var sp = document.createElement('span'); sp.textContent = m.desc;
    a.appendChild(s); a.appendChild(sp); li.appendChild(a); ul.appendChild(li);
  });

  function elegirModo(id, enfocar) {
    if (!MODOS.some(function (m) { return m.id === id; })) id = 'todo';
    estado.modo = id;
    MODOS.forEach(function (m) { $('modo-' + m.id).setAttribute('aria-current', m.id === id ? 'true' : 'false'); });
    var m = MODOS.filter(function (x) { return x.id === id; })[0], el = $('elegido');
    el.innerHTML = '';
    el.appendChild(document.createTextNode(T('You chose: ', 'Ha elegido: ')));
    var st = document.createElement('strong'); st.textContent = m.nombre + ' (' + m.desc + ')'; el.appendChild(st);
    el.appendChild(document.createTextNode(T('. Press “Start” when you are ready.', '. Pulse «Comenzar» cuando esté listo.')));
    if (enfocar) $('btn-comenzar').focus();
  }
  function leerAncla(enfocar) {
    var h = (location.hash || '').replace('#', ''), id = null;
    Object.keys(IDS).forEach(function (k) { if (IDS[k] === h) id = k; });
    if (id) { mostrar('inicio'); elegirModo(id, enfocar); } else elegirModo(estado.modo, false);
  }
  window.addEventListener('hashchange', function () { detenerReloj(); leerAncla(true); });

  function fijarReloj(conReloj) { estado.reloj = conReloj; $('con-tiempo').setAttribute('aria-pressed', conReloj ? 'true' : 'false'); $('sin-tiempo').setAttribute('aria-pressed', conReloj ? 'false' : 'true'); }
  $('con-tiempo').addEventListener('click', function () { fijarReloj(true); });
  $('sin-tiempo').addEventListener('click', function () { fijarReloj(false); });

  function mostrar(cual) { ['inicio', 'juego', 'resultados'].forEach(function (p) { $('pantalla-' + p).classList.toggle('oculto', p !== cual); }); }

  function comenzar() {
    estado.lista = construirLista(estado.modo);
    estado.i = 0; estado.aciertos = 0; estado.respuestas = []; estado.inicio = Date.now();
    mostrar('juego'); $('reloj').classList.toggle('oculto', !estado.reloj);
    window.scrollTo(0, 0);
    presentar();
  }
  $('btn-comenzar').addEventListener('click', comenzar);

  function presentar() {
    var q = estado.lista[estado.i], cat = CATS[q.cat], n = estado.lista.length;
    estado.respondida = false;
    $('contador').textContent = T('Question ', 'Pregunta ') + (estado.i + 1) + T(' of ', ' de ') + n;
    $('puntos').textContent = T('Correct: ', 'Aciertos: ') + estado.aciertos;
    $('insignia').textContent = cat.nombre; $('insignia').style.background = cat.color;
    $('barra-progreso').style.width = (estado.i / n * 100) + '%';
    $('pregunta-txt').textContent = q.texto;
    var ex = $('expresion');
    if (q.expr === '?') ex.classList.add('oculto'); else { ex.classList.remove('oculto'); ex.textContent = q.expr; }
    var cont = $('opciones'); cont.innerHTML = '';
    q.ops.forEach(function (o, j) {
      var b = document.createElement('button');
      b.type = 'button'; b.className = 'opcion';
      var tk = document.createElement('span'); tk.className = 'tecla'; tk.setAttribute('aria-hidden', 'true'); tk.textContent = j + 1;
      var tx = document.createElement('span'); tx.textContent = o;
      b.appendChild(tk); b.appendChild(tx);
      b.setAttribute('aria-label', T('Option ', 'Opción ') + (j + 1) + ': ' + o);
      b.addEventListener('click', function () { responder(j); });
      cont.appendChild(b);
    });
    $('retro').className = 'retro oculto'; $('retro').innerHTML = '';
    $('btn-siguiente').classList.add('oculto');
    $('aviso-reloj').textContent = '';
    cont.firstChild.focus();
    if (estado.reloj) iniciarReloj(cat.tiempo);
  }

  function iniciarReloj(seg) {
    detenerReloj();
    estado.restante = seg; var total = seg;
    pintarReloj(total);
    estado.temporizador = setInterval(function () {
      estado.restante--;
      pintarReloj(total);
      if (estado.restante === 10) $('aviso-reloj').textContent = T('10 seconds left.', 'Quedan 10 segundos.');
      if (estado.restante <= 0) { detenerReloj(); responder(-1); }
    }, 1000);
  }
  function pintarReloj(total) {
    var urg = estado.restante <= 10;
    $('reloj-num').textContent = estado.restante + ' s';
    $('reloj-num').classList.toggle('urgente', urg);
    $('reloj-barra').style.width = Math.max(0, estado.restante / total * 100) + '%';
    $('reloj-barra').classList.toggle('urgente', urg);
  }
  function detenerReloj() { if (estado.temporizador) { clearInterval(estado.temporizador); estado.temporizador = null; } }

  function responder(j) {
    if (estado.respondida) return;
    estado.respondida = true; detenerReloj();
    var q = estado.lista[estado.i], bien = j === q.correcta;
    if (bien) estado.aciertos++;
    estado.respuestas.push({ q: q, elegida: j, bien: bien });
    Array.prototype.forEach.call($('opciones').querySelectorAll('.opcion'), function (b, k) {
      b.disabled = true;
      if (k === q.correcta) b.classList.add('correcta');
      else if (k === j) b.classList.add('incorrecta');
    });
    var r = $('retro'); r.className = 'retro ' + (bien ? 'ok' : 'no'); r.innerHTML = '';
    var tit = document.createElement('p'); tit.className = 'titulo';
    tit.textContent = bien ? T('Correct!', '¡Correcto!') : (j < 0 ? T('Time is up. The correct answer is: ', 'Se acabó el tiempo. La respuesta correcta es: ') : T('Not quite. The correct answer is: ', 'No es correcto. La respuesta correcta es: ')) + (bien ? '' : q.ops[q.correcta]);
    r.appendChild(tit);
    q.explica.forEach(function (l) { var p = document.createElement('p'); p.textContent = l; r.appendChild(p); });
    $('puntos').textContent = T('Correct: ', 'Aciertos: ') + estado.aciertos;
    var sig = $('btn-siguiente');
    sig.textContent = estado.i + 1 < estado.lista.length ? T('Next', 'Siguiente') : T('See results', 'Ver resultados');
    sig.classList.remove('oculto'); sig.focus();
  }

  function siguiente() {
    if (!estado.respondida) return;
    estado.i++;
    if (estado.i < estado.lista.length) presentar(); else resultados();
  }
  $('btn-siguiente').addEventListener('click', siguiente);
  $('btn-salir').addEventListener('click', function () { detenerReloj(); if (estado.respuestas.length) resultados(); else mostrar('inicio'); });

  document.addEventListener('keydown', function (e) {
    if ($('pantalla-juego').classList.contains('oculto')) return;
    if (!estado.respondida && /^[1-4]$/.test(e.key)) {
      var j = parseInt(e.key, 10) - 1;
      if (j < estado.lista[estado.i].ops.length) { e.preventDefault(); responder(j); }
    } else if (estado.respondida && e.key === 'Enter' && document.activeElement !== $('btn-siguiente') && document.activeElement !== $('btn-salir')) {
      e.preventDefault(); siguiente();
    }
  });

  function resultados() {
    detenerReloj(); mostrar('resultados'); window.scrollTo(0, 0);
    var n = estado.respuestas.length, ac = estado.aciertos, pct = n ? Math.round(ac / n * 100) : 0;
    var min = Math.floor((Date.now() - estado.inicio) / 60000), seg = Math.round((Date.now() - estado.inicio) / 1000) % 60;
    $('marcador').textContent = ac + T(' of ', ' de ') + n + ' (' + pct + ' %)';
    $('mensaje').textContent = (pct >= 90 ? T('Excellent command. ', 'Excelente dominio. ') : pct >= 70 ? T('Good work; just a little left to polish. ', 'Buen trabajo; queda poco por pulir. ') : T('It is worth reviewing and trying again. ', 'Vale la pena repasar y volver a intentarlo. ')) + T('Total time: ', 'Tiempo total: ') + min + ' min ' + seg + ' s.';
    var por = {};
    estado.respuestas.forEach(function (x) { var c = x.q.cat; por[c] = por[c] || { b: 0, t: 0 }; por[c].t++; if (x.bien) por[c].b++; });
    var tb = $('tabla-desglose'); tb.innerHTML = '';
    var peor = null;
    ORDEN.forEach(function (c) {
      if (!por[c]) return;
      var p = Math.round(por[c].b / por[c].t * 100), tr = document.createElement('tr');
      [CATS[c].nombre, por[c].b + T(' of ', ' de ') + por[c].t, p + ' %'].forEach(function (v, k) { var td = document.createElement('td'); td.textContent = v; if (k) td.className = 'n'; tr.appendChild(td); });
      tb.appendChild(tr);
      if (p < 100 && (peor === null || p < peor.p)) peor = { c: c, p: p };
    });
    var cz = $('consejo'); cz.innerHTML = '';
    if (peor) {
      var d = document.createElement('div'); d.className = 'consejo';
      var p1 = document.createElement('p'); p1.style.margin = '0 0 6px';
      var s = document.createElement('strong'); s.textContent = T('To review: ', 'Para repasar: ') + CATS[peor.c].nombre + '. ';
      p1.appendChild(s); p1.appendChild(document.createTextNode(CATS[peor.c].consejo)); d.appendChild(p1);
      var p2 = document.createElement('p'); p2.style.margin = '0';
      function enlace(href, txt) { var a = document.createElement('a'); a.href = href; a.textContent = txt; return a; }
      p2.appendChild(enlace(CATS[peor.c].lec, T('See the explanation in the lesson', 'Ver la explicación en la lección')));
      p2.appendChild(document.createTextNode(' · '));
      p2.appendChild(enlace(CATS[peor.c].inter, T('Practice without the clock', 'Practicar sin reloj')));
      d.appendChild(p2); cz.appendChild(d);
    }
    var zf = $('zona-fallos'); zf.innerHTML = '';
    var fallos = estado.respuestas.filter(function (x) { return !x.bien; });
    if (fallos.length) {
      var det = document.createElement('details'); det.className = 'fallos';
      var sm = document.createElement('summary'); sm.textContent = T('Review the questions you missed (', 'Revisar las preguntas falladas (') + fallos.length + ')';
      det.appendChild(sm);
      fallos.forEach(function (x) {
        var f = document.createElement('div'); f.className = 'fallo';
        var q1 = document.createElement('p'); q1.className = 'q'; q1.textContent = x.q.texto + (x.q.expr !== '?' ? ' ' + x.q.expr : ''); f.appendChild(q1);
        var m = document.createElement('p'); m.className = 'mal'; m.textContent = T('Your answer: ', 'Su respuesta: ') + (x.elegida < 0 ? T('none (time ran out)', 'sin responder (se acabó el tiempo)') : x.q.ops[x.elegida]); f.appendChild(m);
        var b = document.createElement('p'); b.className = 'bien'; b.textContent = T('Correct answer: ', 'Respuesta correcta: ') + x.q.ops[x.q.correcta]; f.appendChild(b);
        x.q.explica.forEach(function (l) { var p = document.createElement('p'); p.textContent = l; f.appendChild(p); });
        det.appendChild(f);
      });
      zf.appendChild(det);
    }
    $('t-res').focus();
  }
  $('btn-repetir').addEventListener('click', comenzar);
  $('btn-inicio').addEventListener('click', function () { mostrar('inicio'); window.scrollTo(0, 0); $('btn-comenzar').focus(); });

  fijarReloj(true);
  leerAncla(false);
})();
