  var HTML_FORMULAS =
    '<h3>Area</h3>' +
    '<table><caption>Area of a shape</caption><thead><tr><th scope="col">Shape</th><th scope="col">Formula</th></tr></thead><tbody>' +
    '<tr><td>Parallelogram</td><td><i>A</i> = <i>bh</i></td></tr>' +
    '<tr><td>Trapezoid</td><td><i>A</i> = ' + fr('1', '2') + '<i>h</i>(<i>b</i><sub>1</sub> + <i>b</i><sub>2</sub>)</td></tr>' +
    '</tbody></table>' +
    '<h3>Surface area and volume</h3>' +
    '<table class="gti-sv"><caption>Surface area (SA) and volume (V) of solids</caption><thead><tr><th scope="col">Solid</th><th scope="col">Surface area</th><th scope="col">Volume</th></tr></thead><tbody>' +
    '<tr><td>Rectangular or right prism</td><td><i>SA</i> = <i>ph</i> + 2<i>B</i></td><td><i>V</i> = <i>Bh</i></td></tr>' +
    '<tr><td>Cylinder</td><td><i>SA</i> = 2π<i>rh</i> + 2π<i>r</i><sup>2</sup></td><td><i>V</i> = π<i>r</i><sup>2</sup><i>h</i></td></tr>' +
    '<tr><td>Pyramid</td><td><i>SA</i> = ' + fr('1', '2') + '<i>ps</i> + <i>B</i></td><td><i>V</i> = ' + fr('1', '3') + '<i>Bh</i></td></tr>' +
    '<tr><td>Cone</td><td><i>SA</i> = π<i>rs</i> + π<i>r</i><sup>2</sup></td><td><i>V</i> = ' + fr('1', '3') + 'π<i>r</i><sup>2</sup><i>h</i></td></tr>' +
    '<tr><td>Sphere</td><td><i>SA</i> = 4π<i>r</i><sup>2</sup></td><td><i>V</i> = ' + fr('4', '3') + 'π<i>r</i><sup>3</sup></td></tr>' +
    '</tbody></table>' +
    '<p class="gti-nota"><i>p</i> = perimeter of base, <i>B</i> = area of base, <i>s</i> = slant height, π ≈ 3.14</p>' +
    '<h3>Algebra</h3>' +
    '<table><caption>Algebra formulas</caption><thead><tr><th scope="col">Concept</th><th scope="col">Formula</th></tr></thead><tbody>' +
    '<tr><td>Slope of a line</td><td><i>m</i> = ' + fr('<i>y</i><sub>2</sub> − <i>y</i><sub>1</sub>', '<i>x</i><sub>2</sub> − <i>x</i><sub>1</sub>') + '</td></tr>' +
    '<tr><td>Slope-intercept form of the equation of a line</td><td><i>y</i> = <i>mx</i> + <i>b</i></td></tr>' +
    '<tr><td>Point-slope form of the equation of a line</td><td><i>y</i> − <i>y</i><sub>1</sub> = <i>m</i>(<i>x</i> − <i>x</i><sub>1</sub>)</td></tr>' +
    '<tr><td>Standard form of a quadratic equation</td><td><i>y</i> = <i>ax</i><sup>2</sup> + <i>bx</i> + <i>c</i></td></tr>' +
    '<tr><td>Quadratic formula</td><td><i>x</i> = ' + fr('−<i>b</i> ± ' + rz('<i>b</i><sup>2</sup> − 4<i>ac</i>'), '2<i>a</i>') + '</td></tr>' +
    '<tr><td>Pythagorean theorem</td><td><i>a</i><sup>2</sup> + <i>b</i><sup>2</sup> = <i>c</i><sup>2</sup></td></tr>' +
    '<tr><td>Simple interest</td><td><i>I</i> = <i>prt</i><br><small>(<i>I</i> = interest, <i>p</i> = principal, <i>r</i> = rate, <i>t</i> = time)</small></td></tr>' +
    '<tr><td>Distance</td><td><i>d</i> = <i>rt</i><br><small>(<i>d</i> = distance, <i>r</i> = rate, <i>t</i> = time)</small></td></tr>' +
    '<tr><td>Total cost</td><td>total cost = (number of units) × (price per unit)</td></tr>' +
    '</tbody></table>';

  var SECCIONES_GUIA = [
    ['basicas', 'Basic keys',
      '<p class="gti-paso">' + kb('2nd') + ' is green: after you press it, the next key does the function written in green above it.</p>' +
      '<p class="gti-paso">' + kb('enter') + ' calculates. ' + kb('clear') + ' erases the line; if the line is already empty, it erases the screen. ' + kb('delete') + ' erases what is at the cursor.</p>' +
      '<p class="gti-paso">If you start a calculation with an operation (' + kb('+') + ' ' + kb('−') + ' ' + kb('×') + ' ' + kb('x<sup>2</sup>') + '…), the calculator writes <b>ans</b> (the last answer) in front. If you press ' + kb('clear') + ' until the screen is empty, ans goes back to 0.</p>' +
      '<p class="gti-paso">' + kb('▲') + ' ' + kb('▼') + ' move through earlier calculations; ' + kb('enter') + ' copies the one that is selected.</p>'],
    ['fracciones', 'Fractions',
      '<p class="gti-paso">' + kb('n/d') + ' opens the fraction template. Type the numerator, go down with ' + kb('▼') + ', type the denominator, and leave with ' + kb('►') + '.</p>' +
      '<div class="gti-ej">' + fr('3', '4') + ' + ' + fr('1', '6') + ': ' + kb('n/d') + nums('3') + kb('▼') + nums('4') + kb('►') + kb('+') + kb('n/d') + nums('1') + kb('▼') + nums('6') + kb('►') + kb('enter') + ' ' + ver('11/12') + '</div>' +
      '<p class="gti-paso">You can also type the numerator first: ' + nums('3') + kb('n/d') + nums('4') + ' does the same.</p>'],
    ['mixtos', 'Mixed numbers',
      '<p class="gti-paso">Type the whole number and press ' + k2('n/d') + ' (U n/d). The cursor moves to the numerator; go down with ' + kb('▼') + ' to the denominator and leave with ' + kb('►') + '.</p>' +
      '<div class="gti-ej">2 ' + fr('1', '3') + ' + 1 ' + fr('1', '2') + ':<br>' + nums('2') + k2('n/d') + nums('1') + kb('▼') + nums('3') + kb('►') + kb('+') + nums('1') + k2('n/d') + nums('1') + kb('▼') + nums('2') + kb('►') + kb('enter') + ' ' + ver('23/6') + '</div>' +
      '<p class="gti-paso">The calculator gives the answer as an improper fraction. To see it as a mixed number, press ' + k2('x<sup>−1</sup>') + ' (n/d◂▸Un/d) and ' + kb('enter') + ' ' + ver('3 5/6') + '. To see it as a decimal, press ' + kb('⟷') + '.</p>'],
    ['negativos', 'Negative numbers',
      '<p class="gti-paso">For a negative number, use ' + kn('(−)') + ', not the subtraction key ' + kb('−') + '. If you mix them up, the calculator shows <b>SYNTAX ERROR</b>, just like the one on the test. And if you start with subtraction, it writes <b>ans</b> in front: −5 becomes ans−5.</p>' +
      '<div class="gti-ej">−5 − 10 − (−5) + (−6): ' + kn('(−)') + nums('5') + kb('−') + nums('1 0') + kb('−') + kb('(') + kn('(−)') + nums('5') + kb(')') + kb('+') + kb('(') + kn('(−)') + nums('6') + kb(')') + kb('enter') + ' ' + ver('−16') + '</div>' +
      '<div class="gti-ej">−8 + 3: ' + kn('(−)') + nums('8') + kb('+') + nums('3') + kb('enter') + ' ' + ver('−5') + '</div>' +
      '<p class="gti-paso">Watch out: −3<sup>2</sup> gives −9. To square −3, use parentheses: ' + kb('(') + kn('(−)') + nums('3') + kb(')') + kb('x<sup>2</sup>') + ' ' + ver('9') + '.</p>'],
    ['porcentajes', 'Percents',
      '<p class="gti-paso">The % key is ' + k2('(') + '.</p>' +
      '<div class="gti-ej">15% of 80: ' + nums('1 5') + k2('(') + kb('×') + nums('8 0') + kb('enter') + ' ' + ver('12') + '</div>' +
      '<p class="gti-paso">To show an answer as a percent: ' + k2(')') + ' (▸%) and ' + kb('enter') + '. Example: ' + fr('1', '5') + ' ▸% ' + ver('20%') + '.</p>'],
    ['potencias', 'Powers and roots',
      '<p class="gti-paso">' + kb('x<sup>2</sup>') + ' squares a number. ' + kb('^') + ' opens the exponent: type the exponent and leave with ' + kb('►') + ' before you go on.</p>' +
      '<div class="gti-ej">2<sup>5</sup> + 1: ' + nums('2') + kb('^') + nums('5') + kb('►') + kb('+') + nums('1') + kb('enter') + ' ' + ver('33') + '</div>' +
      '<p class="gti-paso">Square root: ' + k2('x<sup>2</sup>') + ' (√), the number, and ' + kb('►') + '. The calculator gives the exact root (for example, 2√2); ' + kb('⟷') + ' changes it to a decimal.</p>' +
      '<p class="gti-paso">Another root: type the index and press ' + k2('^') + ' (<sup>x</sup>√). Cube root of 27: ' + nums('3') + k2('^') + nums('2 7') + kb('►') + kb('enter') + ' ' + ver('3') + '</p>'],
    ['cientifica', 'Scientific notation',
      '<p class="gti-paso">' + kb('×10<sup>n</sup>') + ' opens the exponent of 10.</p>' +
      '<div class="gti-ej">4.5 × 10<sup>6</sup>: ' + nums('4 . 5') + kb('×10<sup>n</sup>') + nums('6') + kb('►') + '</div>' +
      '<p class="gti-paso">For a negative exponent, use ' + kn('(−)') + ' inside the exponent.</p>'],
    ['probabilidad', 'Probability (nPr, nCr, !)',
      '<p class="gti-paso">Type <b>n</b> first, press ' + kb('prb') + ', and choose with the option number. Then type <b>r</b>. The screen shows the whole <b>nPr</b> or <b>nCr</b>, so you know which one you chose.</p>' +
      '<div class="gti-ej">Permutations of 5 taken 2 at a time: ' + nums('5') + kb('prb') + nums('1') + nums('2') + kb('enter') + ' → 5 nPr 2 ' + ver('20') + '<br>' +
      'Combinations of 5 taken 2 at a time: ' + nums('5') + kb('prb') + nums('2') + nums('2') + kb('enter') + ' → 5 nCr 2 ' + ver('10') + '<br>' +
      'Factorial of 5: ' + nums('5') + kb('prb') + nums('3') + kb('enter') + ' → 5! ' + ver('120') + '</div>' +
      '<p class="gti-paso">nPr: order matters (a podium, passwords). nCr: order does not matter (committees, groups).</p>'],
    ['toggle', 'Fraction or decimal',
      '<p class="gti-paso">' + kb('⟷') + ' switches the last answer between fraction and decimal (or between exact root and decimal).</p>' +
      '<p class="gti-paso">' + k2('table') + ' (f◂▸d) changes a decimal to a fraction: 0.75 ' + k2('table') + kb('enter') + ' ' + ver('3/4') + '.</p>' +
      '<p class="gti-paso">Dividing with ' + kb('÷') + ' gives a decimal; the ' + kb('n/d') + ' template gives a fraction.</p>'],
    ['variables', 'Variables (sto→)',
      '<p class="gti-paso">To store a number: type it (or do the calculation), press ' + kb('sto→') + ', and then ' + kb('x<sub>abc</sub><sup>yzt</sup>') + '. Each time you press ' + kb('x<sub>abc</sub><sup>yzt</sup>') + ' the letter changes: x, y, z, t, a, b, c.</p>' +
      '<div class="gti-ej">Store 12 in x: ' + nums('1 2') + kb('sto→') + kb('x<sub>abc</sub><sup>yzt</sup>') + kb('enter') + '<br>Use it: ' + kb('x<sub>abc</sub><sup>yzt</sup>') + kb('×') + nums('3') + kb('enter') + ' ' + ver('36') + '</div>' +
      '<p class="gti-paso">' + k2('x<sub>abc</sub><sup>yzt</sup>') + ' (recall) shows the value of each variable. ' + k2('sto→') + ' (clear var) sets all of them to 0.</p>' +
      '<p class="gti-paso"><b>The quadratic formula with variables.</b> For 2<i>x</i><sup>2</sup> + 3<i>x</i> − 2 = 0, store 2 in <b>a</b>, 3 in <b>b</b>, and −2 in <b>c</b>. Then type the formula once, with the letters:</p>' +
      '<div class="gti-ej">' + kb('n/d') + kn('(−)') + '<b>b</b>' + kb('+') + k2('x<sup>2</sup>') + '<b>b</b>' + kb('x<sup>2</sup>') + kb('−') + nums('4') + '<b>a</b>' + kb('×') + '<b>c</b>' + kb('►') + kb('▼') + nums('2') + '<b>a</b>' + kb('►') + kb('enter') + ' ' + ver('1/2') + '<br>' +
      'For the other solution, change + to − ' + ver('−2') + '.</div>' +
      '<p class="gti-paso">Watch out: between two letters, press ' + kb('×') + ', because pressing the variable key twice in a row changes the letter.</p>'],
    ['estadistica', 'Data and statistics',
      '<p class="gti-paso">' + kb('data') + ' opens the lists L1, L2, and L3. Type each value and press ' + kb('enter') + '; ' + kb('◄') + ' ' + kb('►') + ' change lists. To clear a list, press ' + kb('data') + ' again and choose Clear.</p>' +
      '<p class="gti-paso">' + k2('data') + ' (stat) → <b>1-Var Stats</b>: choose the list (DATA), leave FRQ at ONE, go down to CALC, and press ' + kb('enter') + '.</p>' +
      '<div class="gti-ej">Data 2, 4, 4, 5, 7: n = 5, x̄ = 4.4 (mean), Med = 4 (median), minX = 2 and maxX = 7 (the range is 7 − 2 = 5).</div>' +
      '<p class="gti-paso">FRQ is for when a list tells how many times each value repeats. <b>2-Var Stats</b> uses two lists (x and y) and gives the regression line <i>y</i> = <i>ax</i> + <i>b</i> and the correlation <i>r</i>.</p>' +
      '<p class="gti-paso">▲ ▼ move through the results; ' + kb('enter') + ' takes the value you chose to the main screen. ' + k2('mode') + ' (quit) goes back to the main screen.</p>'],
    ['tabla', 'Table of values',
      '<p class="gti-paso">' + kb('table') + ' asks for the function: type it using ' + kb('x<sub>abc</sub><sup>yzt</sup>') + ' for <i>x</i> and press ' + kb('enter') + '.</p>' +
      '<p class="gti-paso">In TABLE SETUP, <b>Start</b> is the first value of <i>x</i>, and <b>Step</b> is how much it goes up each time. <b>Auto</b> fills the table for you; <b>Ask-x</b> lets you type each <i>x</i>. Go down to OK and press ' + kb('enter') + '.</p>' +
      '<div class="gti-ej">f(<i>x</i>) = <i>x</i><sup>2</sup> + 1 with Start = 2 and Step = 1: <i>x</i> = 2, 3, 4 → f(<i>x</i>) = 5, 10, 17.</div>'],
    ['clasico', 'CLASSIC mode',
      '<p class="gti-paso">In ' + kb('mode') + ' you can choose CLASSIC: everything is typed on one line, with no templates. Fractions look like 3/4, and mixed numbers like 2u1/3.</p>' +
      '<p class="gti-paso">In CLASSIC the exponent has no template: if it has operations, put it in parentheses, for example 2^(1+2). The root is typed √( … ).</p>' +
      '<p class="gti-paso">The test uses MATHPRINT, which is the recommended mode.</p>'],
    ['otras', 'Constant K, angles, and more',
      '<p class="gti-paso"><b>Constant K</b>: ' + k2('÷') + ', type the operation that repeats (for example ' + kb('+') + nums('3') + ') and ' + kb('enter') + '. From then on, every number you enter with ' + kb('enter') + ' gets that operation. ' + k2('÷') + ' turns it off.</p>' +
      '<p class="gti-paso"><b>Angles</b>: ' + k2('prb') + ' (angle) has °, \', ", radians, and ▸DMS, and the R▸P and P▸R conversions.</p>' +
      '<p class="gti-paso"><b>Random number</b>: ' + kb('prb') + ' ► RAND. randint(1,6) gives a whole number from 1 to 6; the comma is ' + k2('.') + '.</p>' +
      '<p class="gti-paso"><b>Hyperbolic functions</b>: ' + k2('π') + ' (hyp) and then sin, cos, or tan.</p>'],
    ['modos', 'Modes and errors',
      '<p class="gti-paso">' + kb('mode') + ' opens the modes: angles (DEG, RAD, GRAD), notation (NORM, SCI, ENG), decimals (FLOAT or 0 to 9), and display (CLASSIC or MATHPRINT). The usual settings for the GED are <b>DEG</b>, <b>NORM</b>, <b>FLOAT</b>, and <b>MATHPRINT</b>. ' + k2('0') + ' (reset) puts everything back the way it came.</p>' +
      '<p class="gti-paso">If you see <b>SYNTAX ERROR</b> or another error, press ' + kb('clear') + ' to go back to your calculation and fix it.</p>']
  ];
