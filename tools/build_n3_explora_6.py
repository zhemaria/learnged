"""Level 3 · Topic 6 · Explore pages, imported from the repository interactivos and rebuilt for LearnGED
(English and Spanish, LearnGED styles, two tries, screen-reader text, US units):
  interactivos/sec_paralela      → math/level-3/explore-angles.html      · es/matematicas/nivel-3/explorar-angulos.html
  interactivos/teorema_pitagoras → math/level-3/explore-pythagoras.html  · es/matematicas/nivel-3/explorar-pitagoras.html
  interactivos/semejanza         → math/level-3/explore-similar.html     · es/matematicas/nivel-3/explorar-semejanza.html
Run it before the lesson builders of Topic 6 (the lessons link to these pages)."""
import os
import bilingue as B
from bilingue import t
from es.traduce import Traductor
import n3

B.NIVEL = 3
ROOT = B.ROOT
TEMA = ("Geometry: angles, the Pythagorean theorem, and similarity", "Geometría: ángulos, teorema de Pitágoras y semejanza")

ESTILO = n3.ESTILO_RAD + """
  .estado{text-align:center;font-size:18px;margin:6px 0 10px;}
  .estado .grande{font-size:1.6rem;font-weight:700;color:var(--acento);}
  input[type=range]{width:100%;accent-color:var(--tema);}
  .geo-svg{width:100%;max-width:640px;height:auto;display:block;margin:8px auto;touch-action:none;}
  .ang-btn{cursor:pointer;}
  .ang-btn:focus{outline:none;}
  .ang-btn:focus-visible .ang-num{stroke:#0d47a1;stroke-width:4;}
  .leyenda-geo{display:flex;flex-wrap:wrap;gap:8px 16px;justify-content:center;font-size:15px;margin:4px 0 10px;}
  .leyenda-geo span{display:inline-flex;align-items:center;gap:6px;}
  .leyenda-geo i{display:inline-block;width:16px;height:16px;border-radius:4px;border:1px solid #555;}
  .datos-geo{background:#f7f9fc;border:1px solid #d7dee8;border-radius:10px;padding:10px 14px;margin:10px 0;}
  .datos-geo p{margin:4px 0;}
  .btn-sec[aria-pressed=true]{background:var(--tema);color:#fff;border-color:var(--tema);}
  .vertice{cursor:grab;}
  .vertice:focus{outline:none;}
  .vertice:focus-visible{stroke:#0d47a1;stroke-width:5;}
"""

# =====================================================================
# 1 · Angles formed by parallel lines and a transversal (sec_paralela)
# =====================================================================
JS_ANGULOS = r'''
/* Positions: 1 top-left, 2 top-right, 3 bottom-left, 4 bottom-right at line r; 5–8 the same at line s.
   phi is the angle of the transversal (measure of angle 2). */
var AN = {phi: 60, sel: null};
var POS = {1: ["r", "TL"], 2: ["r", "TR"], 3: ["r", "BL"], 4: ["r", "BR"], 5: ["s", "TL"], 6: ["s", "TR"], 7: ["s", "BL"], 8: ["s", "BR"]};
var NOMBRE = {
  corr: T("corresponding", "correspondientes"), vert: T("vertical", "opuestos por el vértice"), lin: T("a linear pair", "adyacentes (par lineal)"),
  aint: T("alternate interior", "alternos internos"), aext: T("alternate exterior", "alternos externos"),
  sint: T("same-side interior", "internos del mismo lado"), sext: T("same-side exterior", "externos del mismo lado")};
var CONGRUENTE = {corr: true, vert: true, aint: true, aext: true, lin: false, sint: false, sext: false};
function medida(a){ var p = POS[a][1]; return (p === "TR" || p === "BL") ? AN.phi : 180 - AN.phi; }
function interior(a){ var l = POS[a][0], p = POS[a][1]; return (l === "r" && p.charAt(0) === "B") || (l === "s" && p.charAt(0) === "T"); }
function lado(a){ return POS[a][1].charAt(1); }
function relacion(a, b){
  var A = POS[a], Bp = POS[b];
  if (A[0] === Bp[0]) return (A[1].charAt(0) !== Bp[1].charAt(0) && A[1].charAt(1) !== Bp[1].charAt(1)) ? "vert" : "lin";
  if (A[1] === Bp[1]) return "corr";
  if (interior(a) && interior(b)) return lado(a) !== lado(b) ? "aint" : "sint";
  if (!interior(a) && !interior(b)) return lado(a) !== lado(b) ? "aext" : "sext";
  return null;
}
function frase(k){ return NOMBRE[k] + (CONGRUENTE[k] ? T(" (congruent: equal measures)", " (congruentes: miden lo mismo)") : T(" (supplementary: they add up to 180°)", " (suplementarios: suman 180°)")); }
var COLOR = {sel: "#0d47a1", igual: "#c8e6c9", supl: "#ffe0b2"};
function geom(){
  var phi = AN.phi * Math.PI / 180, yr = 110, ys = 250, cx = 320, dx = (ys - yr) / Math.tan(phi);
  return {phi: phi, yr: yr, ys: ys, xr: cx + dx / 2, xs: cx - dx / 2};
}
function punto(x, y, ang, r){ return [x + r * Math.cos(ang), y - r * Math.sin(ang)]; }
function sector(x, y, a1, a2, r){ var p = punto(x, y, a1, r), q = punto(x, y, a2, r); return "M" + x + " " + y + " L" + p[0] + " " + p[1] + " A" + r + " " + r + " 0 0 0 " + q[0] + " " + q[1] + " Z"; }
function rango(a){ var g = geom(), f = g.phi, P = POS[a][1]; return P === "TR" ? [0, f] : (P === "TL" ? [f, Math.PI] : (P === "BL" ? [Math.PI, Math.PI + f] : [Math.PI + f, 2 * Math.PI])); }
function dibujaAngulos(resalta){
  var g = geom(), s = "", ext = 300;
  var tA = punto(g.xr, g.yr, g.phi, 110), tB = punto(g.xs, g.ys, g.phi + Math.PI, 110);
  s += '<line x1="30" y1="' + g.yr + '" x2="610" y2="' + g.yr + '" stroke="#37474f" stroke-width="3"/><line x1="30" y1="' + g.ys + '" x2="610" y2="' + g.ys + '" stroke="#37474f" stroke-width="3"/>';
  s += '<line x1="' + tA[0] + '" y1="' + tA[1] + '" x2="' + tB[0] + '" y2="' + tB[1] + '" stroke="#6a1b9a" stroke-width="3"/>';
  s += '<text x="616" y="' + (g.yr + 6) + '" font-size="20" font-style="italic">r</text><text x="616" y="' + (g.ys + 6) + '" font-size="20" font-style="italic">s</text><text x="' + (tA[0] + 8) + '" y="' + (tA[1] + 4) + '" font-size="20" font-style="italic" fill="#6a1b9a">t</text>';
  for (var a = 1; a <= 8; a++){
    var x = POS[a][0] === "r" ? g.xr : g.xs, y = POS[a][0] === "r" ? g.yr : g.ys, R = rango(a), bis = (R[0] + R[1]) / 2, L = punto(x, y, bis, 50);
    var fill = "#ffffff", borde = "#90a4ae";
    if (resalta && resalta[a]){ fill = resalta[a]; borde = "#37474f"; }
    var voz = T("Angle " + a, "Ángulo " + a) + (AN.verMedidas ? ", " + medida(a) + "°" : "");
    s += '<g class="ang-btn" tabindex="0" role="button" data-a="' + a + '" aria-label="' + voz + '"><path d="' + sector(x, y, R[0], R[1], 30) + '" fill="' + fill + '" stroke="' + borde + '" stroke-width="1.5"/>' +
         '<circle class="ang-num" cx="' + L[0] + '" cy="' + L[1] + '" r="16" fill="' + (resalta && resalta[a] === COLOR.sel ? COLOR.sel : "#fff") + '" stroke="#37474f" stroke-width="2"/>' +
         '<text x="' + L[0] + '" y="' + (L[1] + 6) + '" text-anchor="middle" font-size="17" font-weight="700" fill="' + (resalta && resalta[a] === COLOR.sel ? "#fff" : "#222") + '">' + a + "</text>";
    if (AN.verMedidas){ var M = punto(x, y, bis, 82); s += '<text x="' + M[0] + '" y="' + (M[1] + 5) + '" text-anchor="middle" font-size="14" fill="#37474f">' + medida(a) + "°</text>"; }
    s += "</g>";
  }
  return '<svg class="geo-svg" viewBox="0 0 640 360" role="group" aria-label="' + T("Two parallel lines r and s cut by a transversal t, forming angles 1 to 8. Choose an angle.", "Dos rectas paralelas r y s cortadas por una transversal t, que forman los ángulos 1 a 8. Elija un ángulo.") + '">' + s + "</svg>";
}
function pintaExplora(){
  var res = {}, txt;
  if (AN.sel){
    var a = AN.sel; res[a] = COLOR.sel;
    var grupos = {};
    for (var b = 1; b <= 8; b++) if (b !== a){ var k = relacion(a, b); if (k){ (grupos[k] = grupos[k] || []).push(b); res[b] = CONGRUENTE[k] ? COLOR.igual : COLOR.supl; } }
    txt = "<p><strong>" + T("Angle " + a, "Ángulo " + a) + " = " + medida(a) + "°.</strong></p><ul>";
    ["corr", "aint", "aext", "vert", "lin", "sint", "sext"].forEach(function(k){ if (grupos[k]) txt += "<li>" + T("Angle", "Ángulo") + (grupos[k].length > 1 ? "s " : " ") + grupos[k].join(T(" and ", " y ")) + ": " + frase(k) + "</li>"; });
    txt += "</ul><p>" + T("Green angles measure " + medida(a) + "°; orange angles measure " + (180 - medida(a)) + "°.", "Los ángulos verdes miden " + medida(a) + "°; los anaranjados miden " + (180 - medida(a)) + "°.") + "</p>";
  } else txt = "<p>" + T("Choose any numbered angle to see how it is related to the others.", "Elija cualquier ángulo numerado para ver su relación con los demás.") + "</p>";
  $("an-svg").innerHTML = dibujaAngulos(res);
  $("an-info").innerHTML = txt;
  Array.prototype.forEach.call($("an-svg").querySelectorAll(".ang-btn"), function(gr){
    function elegir(){ AN.sel = +gr.getAttribute("data-a"); pintaExplora(); var f = $("an-svg").querySelector('[data-a="' + AN.sel + '"]'); if (f) f.focus(); }
    gr.addEventListener("click", elegir);
    gr.addEventListener("keydown", function(ev){ if (ev.key === "Enter" || ev.key === " "){ ev.preventDefault(); elegir(); } });
  });
}
/* Quiz: two tries */
var QZ = {a: 0, b: 0, k: "", intentos: 0, resuelto: false, primero: 0, pista: 0, total: 0};
function nuevoQZ(){
  var a, b, k;
  do { a = aleatorio(1, 8); b = aleatorio(1, 8); k = a !== b ? relacion(a, b) : null; } while (!k);
  QZ.a = a; QZ.b = b; QZ.k = k; QZ.intentos = 0; QZ.resuelto = false;
  var res = {}; res[a] = "#d1c4e9"; res[b] = "#d1c4e9";
  $("qz-svg").innerHTML = dibujaAngulos(res).replace('role="group"', 'role="img"');
  $("qz-enun").innerHTML = T("What is the relationship between angle " + a + " and angle " + b + "?", "¿Qué relación hay entre el ángulo " + a + " y el ángulo " + b + "?");
  var otros = baraja(Object.keys(NOMBRE).filter(function(x){ return x !== k; })).slice(0, 3), ops = baraja([k].concat(otros)), cont = $("qz-opciones");
  cont.innerHTML = "";
  ops.forEach(function(x){
    var bt = document.createElement("button"); bt.type = "button"; bt.className = "opcion"; bt.textContent = NOMBRE[x].charAt(0).toUpperCase() + NOMBRE[x].slice(1);
    bt.addEventListener("click", function(){ respondeQZ(x, bt); }); cont.appendChild(bt);
  });
  $("qz-fb").className = "fb"; $("qz-fb").innerHTML = "";
}
function pistaQZ(){
  var mismo = POS[QZ.a][0] === POS[QZ.b][0];
  if (mismo) return T("Both angles are at the same intersection: are they across from each other, or side by side?", "Los dos ángulos están en la misma intersección: ¿están enfrentados o uno al lado del otro?");
  if (POS[QZ.a][1] === POS[QZ.b][1]) return T("They are at different intersections, in the same position.", "Están en intersecciones distintas, en la misma posición.");
  return T("Are the angles between the parallel lines (interior) or outside them (exterior)? Are they on the same side of the transversal?", "¿Los ángulos están entre las paralelas (internos) o fuera de ellas (externos)? ¿Están del mismo lado de la transversal?");
}
function respondeQZ(x, bt){
  if (QZ.resuelto) return;
  var fb = $("qz-fb"); QZ.intentos++;
  var exp = T("Angles " + QZ.a + " and " + QZ.b + " are ", "Los ángulos " + QZ.a + " y " + QZ.b + " son ") + frase(QZ.k) + ".";
  if (x === QZ.k){ QZ.resuelto = true; QZ.total++; if (QZ.intentos === 1) QZ.primero++; else QZ.pista++; bt.classList.add("correcta"); fb.className = "fb bien"; fb.innerHTML = TX.bien + exp; }
  else if (QZ.intentos >= 2){ QZ.resuelto = true; QZ.total++; bt.classList.add("incorrecta"); fb.className = "fb mal"; fb.innerHTML = TX.asi + exp + TX.nuevo;
    Array.prototype.forEach.call($("qz-opciones").children, function(o){ if (o.textContent.toLowerCase() === NOMBRE[QZ.k].toLowerCase()) o.classList.add("correcta"); }); }
  else { bt.classList.add("incorrecta"); bt.disabled = true; fb.className = "fb pista"; fb.innerHTML = TX.todavia + pistaQZ() + TX.unoMas; }
  if (QZ.resuelto) Array.prototype.forEach.call($("qz-opciones").children, function(o){ o.disabled = true; });
  $("qz-marcador").textContent = QZ.total ? TX.resueltos(QZ.primero + QZ.pista, QZ.primero, QZ.total) : "";
}
$("an-phi").addEventListener("input", function(){ AN.phi = +this.value; $("an-phi-val").textContent = (180 - AN.phi) + "°"; pintaExplora(); });
$("an-medidas").addEventListener("change", function(){ AN.verMedidas = this.checked; pintaExplora(); });
pintaExplora();
$("qz-nuevo").addEventListener("click", nuevoQZ);
nuevoQZ();
'''

def pagina_angulos():
    tabla = "".join(f"<tr><td>{a}</td><td>{b}</td><td>{c}</td></tr>" for a, b, c in [
        (t("Corresponding", "Correspondientes"), t("Same position at each intersection (1 and 5)", "Misma posición en cada intersección (1 y 5)"), t("Congruent", "Congruentes")),
        (t("Alternate interior", "Alternos internos"), t("Between the parallels, on opposite sides of t (3 and 6)", "Entre las paralelas, a lados opuestos de t (3 y 6)"), t("Congruent", "Congruentes")),
        (t("Alternate exterior", "Alternos externos"), t("Outside the parallels, on opposite sides of t (1 and 8)", "Fuera de las paralelas, a lados opuestos de t (1 y 8)"), t("Congruent", "Congruentes")),
        (t("Vertical", "Opuestos por el vértice"), t("Across from each other at the same intersection (1 and 4)", "Enfrentados en la misma intersección (1 y 4)"), t("Congruent", "Congruentes")),
        (t("Linear pair", "Adyacentes (par lineal)"), t("Side by side on a straight line (1 and 2)", "Uno al lado del otro sobre una recta (1 y 2)"), t("Supplementary (180°)", "Suplementarios (180°)")),
        (t("Same-side interior", "Internos del mismo lado"), t("Between the parallels, on the same side of t (3 and 5)", "Entre las paralelas, del mismo lado de t (3 y 5)"), t("Supplementary (180°)", "Suplementarios (180°)"))])
    mods = [
     (t("explore", "explorar"), t("Explore the eight angles", "Explore los ocho ángulos"),
      f'''      <p>{t("Two parallel lines, r and s, are cut by a transversal t. Eight angles are formed: four at each intersection. Choose an angle to see which angles are equal to it and which ones add up to 180° with it. Move the slider to tilt the transversal: the relationships do not change.", "Dos rectas paralelas, r y s, están cortadas por una transversal t. Se forman ocho ángulos: cuatro en cada intersección. Elija un ángulo para ver cuáles son iguales a él y cuáles suman 180° con él. Mueva el deslizador para inclinar la transversal: las relaciones no cambian.")}</p>
      <div class="panel">
        <div class="campo"><label for="an-phi">{t("Measure of angle 1:", "Medida del ángulo 1:")} <span id="an-phi-val">120°</span></label><input type="range" id="an-phi" min="35" max="145" step="5" value="60"></div>
        <label class="casilla" style="margin-top:8px;"><input type="checkbox" id="an-medidas"> {t("Show the measure of every angle", "Mostrar la medida de cada ángulo")}</label>
        <div class="leyenda-geo" aria-hidden="true"><span><i style="background:#0d47a1"></i>{t("chosen angle", "ángulo elegido")}</span><span><i style="background:#c8e6c9"></i>{t("congruent", "congruente")}</span><span><i style="background:#ffe0b2"></i>{t("supplementary", "suplementario")}</span></div>
        <div id="an-svg"></div>
        <div class="datos-geo" id="an-info" aria-live="polite"></div>
      </div>
      <table class="reglas"><caption>{t("The angle relationships", "Las relaciones entre los ángulos")}</caption><thead><tr><th scope="col">{t("Name", "Nombre")}</th><th scope="col">{t("Where they are", "Dónde están")}</th><th scope="col">{t("Measures", "Medidas")}</th></tr></thead><tbody>{tabla}</tbody></table>'''),
     (t("quiz", "comprension"), t("Check your understanding", "Compruebe su comprensión"),
      f'''      <p>{t("Two angles are highlighted. Choose their relationship. If you make a mistake, you get a hint and another try.", "Hay dos ángulos resaltados. Elija su relación. Si se equivoca, recibe una pista y otra oportunidad.")}</p>
      <div class="practica" id="qz">
        <div id="qz-svg"></div>
        <div class="enun" id="qz-enun"></div>
        <div class="opciones" id="qz-opciones"></div>
        <div class="fb" id="qz-fb" role="status"></div>
        <div class="fila-btn"><button type="button" class="btn" id="qz-nuevo">New exercise</button></div>
        <p class="marcador" id="qz-marcador"></p>
      </div>''')]
    return mods, JS_ANGULOS

# =====================================================================
# 2 · The Pythagorean theorem in real life (teorema_pitagoras)
# =====================================================================
JS_PITAGORAS = r'''
/* Each scenario names its two legs and the hypotenuse; drawn as an SVG with the right triangle in color. US units. */
var ESC = [
  {id: "escalera", nombre: T("Ladder against a wall", "Escalera apoyada en una pared"), u: T("feet", "pies"),
   lados: [T("height on the wall", "altura en la pared"), T("distance from the wall to the foot of the ladder", "distancia de la pared al pie de la escalera"), T("length of the ladder", "largo de la escalera")],
   txt: T("A ladder leans against a wall.", "Una escalera está apoyada contra una pared."), rango: [[8, 24], [3, 9]]},
  {id: "rampa", nombre: T("Wheelchair ramp", "Rampa de acceso"), u: T("feet", "pies"),
   lados: [T("height of the ramp", "altura de la rampa"), T("horizontal distance the ramp covers", "distancia horizontal que cubre la rampa"), T("length of the ramp", "largo de la rampa")],
   txt: T("A ramp is built so a wheelchair can reach a door.", "Se construye una rampa para que una silla de ruedas llegue a una puerta."), rango: [[1, 4], [12, 40]]},
  {id: "torre", nombre: T("Tower with a guy wire", "Torre con cable tensor"), u: T("feet", "pies"),
   lados: [T("height where the wire is tied to the tower", "altura donde el cable se sujeta a la torre"), T("distance from the base of the tower to the stake", "distancia de la base de la torre a la estaca"), T("length of the wire", "largo del cable")],
   txt: T("A wire runs from a point on a radio tower to a stake in the ground.", "Un cable va de un punto de una torre de radio a una estaca en el suelo."), rango: [[30, 90], [15, 50]]},
  {id: "techo", nombre: T("Roof of a house", "Techo de una casa"), u: T("feet", "pies"),
   lados: [T("rise of the roof (height of the peak)", "altura del techo (de la base a la cumbrera)"), T("half the width of the house", "mitad del ancho de la casa"), T("length of the rafter (from the edge to the peak)", "largo de la viga (del borde a la cumbrera)")],
   txt: T("A house has a roof with two equal sides.", "Una casa tiene un techo de dos aguas iguales."), rango: [[4, 12], [10, 20]]},
  {id: "rio", nombre: T("Boat crossing a river", "Barco que cruza un río"), u: T("yards", "yardas"),
   lados: [T("width of the river", "ancho del río"), T("distance the current carries the boat downstream", "distancia que la corriente arrastra el barco río abajo"), T("distance the boat actually travels", "distancia que el barco recorre en realidad")],
   txt: T("A boat heads straight across a river, but the current carries it downstream.", "Un barco cruza un río en línea recta, pero la corriente lo arrastra río abajo."), rango: [[40, 120], [15, 60]]},
  {id: "tv", nombre: T("TV screen", "Pantalla de televisor"), u: T("inches", "pulgadas"),
   lados: [T("height of the screen", "alto de la pantalla"), T("width of the screen", "ancho de la pantalla"), T("diagonal of the screen (the size on the box)", "diagonal de la pantalla (la medida de la caja)")],
   txt: T("TV sizes are measured along the diagonal of the screen.", "El tamaño de un televisor se mide por la diagonal de la pantalla."), rango: [[18, 36], [32, 64]]}
];
var TRIPLES = [[3, 4, 5], [5, 12, 13], [8, 15, 17], [7, 24, 25], [6, 8, 10], [9, 12, 15], [12, 16, 20], [20, 21, 29]];
var PT = {e: null, a: 0, b: 0, c: 0, falta: 2, verTri: false, intentos: 0, resuelto: false, primero: 0, pista: 0, total: 0, d: [0, 0, 0]};
function r1(x){ return Math.round(x * 10) / 10; }
function f1(x){ return (Math.round(x * 10) / 10).toString(); }
function nuevoPT(){
  var e = PT.e = elige(ESC), a, b;
  if (Math.random() < 0.45){
    var tr, k = 0, n = 0;
    while (!k && n++ < 40){ tr = baraja(elige(TRIPLES).slice(0, 2)); for (var i = 1; i <= 12; i++){ var aa = tr[0] * i, bb = tr[1] * i;
      if (aa >= e.rango[0][0] && aa <= e.rango[0][1] && bb >= e.rango[1][0] && bb <= e.rango[1][1]){ k = i; break; } } }
    if (k){ a = tr[0] * k; b = tr[1] * k; } else { a = aleatorio(e.rango[0][0], e.rango[0][1]); b = aleatorio(e.rango[1][0], e.rango[1][1]); }
  } else { a = aleatorio(e.rango[0][0], e.rango[0][1]); b = aleatorio(e.rango[1][0], e.rango[1][1]); }
  PT.a = a; PT.b = b; PT.c = Math.sqrt(a * a + b * b);
  PT.falta = elige([0, 1, 2, 2]);
  /* the numbers the student sees: the hypotenuse is rounded to a tenth when it is given */
  PT.d = [a, b, r1(PT.c)];
  var d = PT.d;
  PT.resp = PT.falta === 2 ? r1(Math.sqrt(d[0] * d[0] + d[1] * d[1])) : r1(Math.sqrt(d[2] * d[2] - d[1 - PT.falta] * d[1 - PT.falta]));
  PT.intentos = 0; PT.resuelto = false;
  pintaPT();
  $("pt-r").value = ""; $("pt-r").disabled = false; $("pt-comprobar").disabled = false;
  $("pt-fb").className = "fb"; $("pt-fb").innerHTML = ""; $("pt-sol").innerHTML = ""; $("pt-sol").style.display = "none";
}
function etiqueta(i){ return PT.falta === i ? "?" : f1(PT.d[i]); }
function dibujoPT(){
  var e = PT.e, s = "", col = PT.verTri ? ["#c62828", "#1565c0", "#2e7d32"] : ["#37474f", "#37474f", "#37474f"], w = PT.verTri ? 6 : 3;
  function seg(x1, y1, x2, y2, i){ return '<line x1="' + x1 + '" y1="' + y1 + '" x2="' + x2 + '" y2="' + y2 + '" stroke="' + col[i] + '" stroke-width="' + w + '" stroke-linecap="round"/>'; }
  function lab(x, y, i, ancla){ return '<text x="' + x + '" y="' + y + '" text-anchor="' + (ancla || "middle") + '" font-size="18" font-weight="700" fill="' + col[i] + '">' + etiqueta(i) + " " + (PT.falta === i ? "" : e.u.split(" ")[0]) + "</text>"; }
  function recto(x, y, dx, dy){ return '<path d="M' + (x + dx) + " " + y + " V" + (y + dy) + " H" + x + '" fill="none" stroke="#37474f" stroke-width="2"/>'; }
  if (e.id === "escalera"){
    s += '<rect x="420" y="40" width="40" height="260" fill="#d7ccc8" stroke="#6d4c41"/><line x1="60" y1="300" x2="560" y2="300" stroke="#6d4c41" stroke-width="4"/>';
    s += seg(420, 300, 420, 70, 0) + seg(250, 300, 420, 300, 1) + seg(250, 300, 420, 70, 2) + recto(420, 300, -16, -16);
    for (var k = 1; k < 8; k++){ var tt = k / 8; s += '<line x1="' + (250 + 170 * tt - 6) + '" y1="' + (300 - 230 * tt) + '" x2="' + (250 + 170 * tt + 6) + '" y2="' + (300 - 230 * tt + 5) + '" stroke="#8d6e63" stroke-width="3"/>'; }
    s += lab(480, 190, 0, "start") + lab(335, 330, 1) + lab(300, 170, 2, "end");
  } else if (e.id === "rampa"){
    s += '<rect x="440" y="150" width="140" height="150" fill="#e0e0e0" stroke="#757575"/><rect x="500" y="80" width="40" height="70" fill="#a1887f"/><line x1="40" y1="300" x2="600" y2="300" stroke="#6d4c41" stroke-width="4"/>';
    s += seg(440, 300, 440, 150, 0) + seg(80, 300, 440, 300, 1) + seg(80, 300, 440, 150, 2) + recto(440, 300, -16, -16);
    s += lab(430, 230, 0, "end") + lab(260, 330, 1) + lab(240, 205, 2, "end");
  } else if (e.id === "torre"){
    s += '<rect x="290" y="30" width="20" height="270" fill="#b0bec5" stroke="#546e7a"/><line x1="40" y1="300" x2="600" y2="300" stroke="#6d4c41" stroke-width="4"/>';
    s += seg(300, 300, 300, 60, 0) + seg(300, 300, 520, 300, 1) + seg(300, 60, 520, 300, 2) + recto(300, 300, 16, -16) + '<circle cx="520" cy="300" r="7" fill="#5d4037"/>';
    s += lab(280, 190, 0, "end") + lab(410, 330, 1) + lab(430, 160, 2, "start");
  } else if (e.id === "techo"){
    s += '<rect x="120" y="190" width="400" height="120" fill="#ffe0b2" stroke="#8d6e63"/><polygon points="120,190 320,70 520,190" fill="#bcaaa4" stroke="#6d4c41"/>';
    s += seg(320, 190, 320, 70, 0) + seg(320, 190, 520, 190, 1) + seg(320, 70, 520, 190, 2) + recto(320, 190, 16, -16);
    s += lab(310, 140, 0, "end") + lab(420, 220, 1) + lab(440, 115, 2, "start");
  } else if (e.id === "rio"){
    s += '<rect x="40" y="70" width="560" height="200" fill="#bbdefb"/><rect x="40" y="40" width="560" height="30" fill="#a5d6a7"/><rect x="40" y="270" width="560" height="30" fill="#a5d6a7"/>';
    s += '<path d="M480 170 l40 0 m-12 -8 l12 8 l-12 8" stroke="#1565c0" stroke-width="3" fill="none"/>';
    s += seg(180, 270, 180, 70, 0) + seg(180, 70, 420, 70, 1) + seg(180, 270, 420, 70, 2) + recto(180, 70, 16, 16);
    s += '<path d="M168 282 h24 l-12 -18 z" fill="#5d4037"/>' + lab(170, 175, 0, "end") + lab(300, 60, 1) + lab(320, 200, 2, "start");
  } else {
    s += '<rect x="150" y="50" width="340" height="210" rx="8" fill="#263238"/><rect x="165" y="64" width="310" height="182" fill="#455a64"/><rect x="295" y="260" width="50" height="30" fill="#37474f"/>';
    s += seg(165, 246, 165, 64, 0) + seg(165, 246, 475, 246, 1) + seg(165, 246, 475, 64, 2) + recto(165, 246, 16, -16);
    s += lab(150, 160, 0, "end") + lab(320, 312, 1) + '<text x="330" y="140" text-anchor="middle" font-size="18" font-weight="700" fill="' + (PT.verTri ? col[2] : "#fff") + '">' + etiqueta(2) + " " + (PT.falta === 2 ? "" : e.u) + "</text>";
  }
  var voz = e.nombre + ". " + e.lados.map(function(l, i){ return l + ": " + (PT.falta === i ? T("unknown", "desconocido") : f1(PT.d[i]) + " " + e.u); }).join("; ") + ".";
  return '<svg class="geo-svg" viewBox="0 0 640 340" role="img" aria-label="' + voz + '">' + s + "</svg>";
}
function pintaPT(){
  var e = PT.e;
  $("pt-svg").innerHTML = dibujoPT();
  $("pt-enun").innerHTML = "<strong>" + e.nombre + ".</strong> " + e.txt + " " + T("Find the ", "Halle la medida: ") + "<strong>" + e.lados[PT.falta] + "</strong>" + T(", to the nearest tenth.", ", a la décima más cercana.");
  $("pt-datos").innerHTML = e.lados.map(function(l, i){ return "<p>" + l.charAt(0).toUpperCase() + l.slice(1) + ": " + (PT.falta === i ? "<strong>?</strong>" : f1(PT.d[i]) + " " + e.u) + (PT.verTri ? ' <span class="nota">(' + (i === 2 ? T("hypotenuse", "hipotenusa") : T("leg", "cateto")) + ")</span>" : "") + "</p>"; }).join("");
  $("pt-rlab").textContent = e.lados[PT.falta].charAt(0).toUpperCase() + e.lados[PT.falta].slice(1) + " (" + e.u + ")";
}
function pasosPT(){
  var d = PT.d, e = PT.e, h = [];
  h.push(T("Step 1. The right angle is where the two legs meet. The hypotenuse is the side across from it: the ", "Paso 1. El ángulo recto está donde se unen los dos catetos. La hipotenusa es el lado opuesto a él: la ") + e.lados[2] + ".");
  if (PT.falta === 2){
    var s2 = d[0] * d[0] + d[1] * d[1];
    h.push(T("Step 2. You want the hypotenuse, so add the squares of the legs: ", "Paso 2. Se busca la hipotenusa, así que se suman los cuadrados de los catetos: ") + "c² = " + f1(d[0]) + "² + " + f1(d[1]) + "² = " + f1(d[0] * d[0]) + " + " + f1(d[1] * d[1]) + " = " + f1(s2) + ".");
    h.push(T("Step 3. Take the square root: ", "Paso 3. Se saca la raíz cuadrada: ") + "c = √" + f1(s2) + " ≈ " + f1(PT.resp) + " " + e.u + ".");
  } else {
    var o = d[1 - PT.falta], dif = d[2] * d[2] - o * o;
    h.push(T("Step 2. You want a leg, so subtract: hypotenuse squared minus the other leg squared: ", "Paso 2. Se busca un cateto, así que se resta: la hipotenusa al cuadrado menos el otro cateto al cuadrado: ") + f1(d[2]) + "² − " + f1(o) + "² = " + f1(d[2] * d[2]) + " − " + f1(o * o) + " = " + f1(dif) + ".");
    h.push(T("Step 3. Take the square root: ", "Paso 3. Se saca la raíz cuadrada: ") + "√" + f1(dif) + " ≈ " + f1(PT.resp) + " " + e.u + ".");
  }
  return h.map(function(p){ return "<p>" + p + "</p>"; }).join("");
}
function compruebaPT(){
  if (PT.resuelto) return;
  var v = leeDecimal($("pt-r").value), fb = $("pt-fb"), d = PT.d;
  if (v === null){ fb.className = "fb pista"; fb.innerHTML = T("Type a number, for example 12.5.", "Escriba un número, por ejemplo 12.5."); return; }
  PT.intentos++;
  var ok = Math.abs(v - PT.resp) <= 0.051;
  if (ok){ PT.resuelto = true; PT.total++; if (PT.intentos === 1) PT.primero++; else PT.pista++; fb.className = "fb bien"; fb.innerHTML = TX.bien + f1(PT.resp) + " " + PT.e.u + "."; }
  else if (PT.intentos >= 2){ PT.resuelto = true; PT.total++; fb.className = "fb mal"; fb.innerHTML = TX.asi + T("The answer is ", "La respuesta es ") + f1(PT.resp) + " " + PT.e.u + "." + TX.nuevo; }
  else {
    var msg = T("Check which side is the hypotenuse: it is always the longest side, across from the right angle.", "Revise cuál es la hipotenusa: siempre es el lado más largo, opuesto al ángulo recto.");
    var o = PT.falta === 2 ? null : d[1 - PT.falta];
    if (PT.falta === 2 && Math.abs(v - (d[0] + d[1])) < 0.06) msg = T("You added the legs. Add their squares, then take the square root.", "Sumó los catetos. Hay que sumar sus cuadrados y después sacar la raíz.");
    else if (PT.falta === 2 && Math.abs(v - (d[0] * d[0] + d[1] * d[1])) < 0.06) msg = T("You still need to take the square root.", "Falta sacar la raíz cuadrada.");
    else if (o !== null && Math.abs(v - r1(Math.sqrt(d[2] * d[2] + o * o))) < 0.06) msg = T("To find a leg, subtract the squares; do not add them.", "Para hallar un cateto se restan los cuadrados; no se suman.");
    else if (o !== null && Math.abs(v - (d[2] * d[2] - o * o)) < 0.06) msg = T("You still need to take the square root.", "Falta sacar la raíz cuadrada.");
    else if (o !== null && Math.abs(v - (d[2] - o)) < 0.06) msg = T("You subtracted the sides. Subtract their squares, then take the square root.", "Restó los lados. Hay que restar sus cuadrados y después sacar la raíz.");
    fb.className = "fb pista"; fb.innerHTML = TX.todavia + msg + TX.unoMas;
  }
  if (PT.resuelto){ $("pt-r").disabled = true; $("pt-comprobar").disabled = true; $("pt-sol").innerHTML = pasosPT(); $("pt-sol").style.display = "block"; }
  $("pt-marcador").textContent = PT.total ? TX.resueltos(PT.primero + PT.pista, PT.primero, PT.total) : "";
}
$("pt-tri").addEventListener("click", function(){ PT.verTri = !PT.verTri; this.setAttribute("aria-pressed", PT.verTri ? "true" : "false"); this.textContent = PT.verTri ? T("Hide the triangle", "Ocultar el triángulo") : T("Show the triangle", "Mostrar el triángulo"); pintaPT(); });
$("pt-ver").addEventListener("click", function(){ $("pt-sol").innerHTML = pasosPT(); $("pt-sol").style.display = "block"; });
$("pt-comprobar").addEventListener("click", compruebaPT);
$("pt-r").addEventListener("keydown", function(ev){ if (ev.key === "Enter") compruebaPT(); });
$("pt-nuevo").addEventListener("click", nuevoPT);
nuevoPT();
'''

def pagina_pitagoras():
    mods = [
     (t("problems", "problemas"), t("Pythagorean problems from everyday life", "Problemas de Pitágoras de la vida diaria"),
      f'''      <p>{t("Ladders, ramps, roofs, cables, rivers, and TV screens all hide a right triangle. In each problem, find the triangle, decide whether you are looking for the hypotenuse or a leg, and use a² + b² = c².", "Escaleras, rampas, techos, cables, ríos y pantallas de televisor esconden un triángulo rectángulo. En cada problema, encuentre el triángulo, decida si busca la hipotenusa o un cateto y use a² + b² = c².")}</p>
{n3.formula("a² + b² = c²")}
      <div class="practica" id="pt">
        <div class="enun" id="pt-enun"></div>
        <div id="pt-svg"></div>
        <div class="fila-btn" style="justify-content:center;"><button type="button" class="btn-sec" id="pt-tri" aria-pressed="false">{t("Show the triangle", "Mostrar el triángulo")}</button></div>
        <div class="datos-geo" id="pt-datos"></div>
        <div class="campos"><div class="campo"><label for="pt-r" id="pt-rlab"></label><input type="text" inputmode="decimal" autocomplete="off" class="ancho" id="pt-r"></div></div>
        <p class="nota">{t("Use a calculator and round to the nearest tenth.", "Use la calculadora y redondee a la décima.")}</p>
        <div class="fila-btn"><button type="button" class="btn" id="pt-comprobar">Check</button><button type="button" class="btn-sec" id="pt-ver">{t("See the solution", "Ver la solución")}</button><button type="button" class="btn-sec" id="pt-nuevo">{t("New exercise", "Otro ejercicio")}</button></div>
        <div class="fb" id="pt-fb" role="status"></div>
        <div class="datos-geo" id="pt-sol" aria-live="polite" style="display:none"></div>
        <p class="marcador" id="pt-marcador"></p>
      </div>
      <div class="caja-tip"><strong>{t("Hypotenuse or leg?", "¿Hipotenusa o cateto?")}</strong> {t("If you are looking for the longest side (across from the right angle), add the squares. If you are looking for one of the shorter sides, subtract the squares. Either way, take the square root at the end.", "Si busca el lado más largo (opuesto al ángulo recto), se suman los cuadrados. Si busca uno de los lados cortos, se restan los cuadrados. En los dos casos, al final se saca la raíz cuadrada.")}</div>''')]
    return mods, JS_PITAGORAS

# =====================================================================
# 3 · Congruent and similar triangles (semejanza)
# =====================================================================
JS_SEMEJANZA = r'''
var SE = {modo: "igual", k: 1.5, P: [{x: 70, y: 260}, {x: 150, y: 90}, {x: 250, y: 260}], arrastra: -1, sel: 0};
var ESCALA = 20; /* 20 px = 1 unit */
function dist(p, q){ return Math.sqrt((p.x - q.x) * (p.x - q.x) + (p.y - q.y) * (p.y - q.y)); }
function lados(P){ return [dist(P[1], P[2]), dist(P[0], P[2]), dist(P[0], P[1])]; } /* side across from A, B, C */
function angulos(P){ var l = lados(P); return [0, 1, 2].map(function(i){ var a = l[i], b = l[(i + 1) % 3], c = l[(i + 2) % 3]; return Math.acos(Math.max(-1, Math.min(1, (b * b + c * c - a * a) / (2 * b * c)))) * 180 / Math.PI; }); }
function copia(){
  var k = SE.modo === "igual" ? 1 : SE.k, ox = 330, minx = Math.min.apply(null, SE.P.map(function(p){ return p.x; })), maxy = Math.max.apply(null, SE.P.map(function(p){ return p.y; }));
  return SE.P.map(function(p){ return {x: ox + (p.x - minx) * k, y: 300 - (maxy - p.y) * k}; });
}
function tri(P, col, nombres){ var s = '<polygon points="' + P.map(function(p){ return p.x + "," + p.y; }).join(" ") + '" fill="' + col + '" fill-opacity="0.25" stroke="' + col + '" stroke-width="3"/>';
  var c = {x: (P[0].x + P[1].x + P[2].x) / 3, y: (P[0].y + P[1].y + P[2].y) / 3};
  P.forEach(function(p, i){ var dx = p.x - c.x, dy = p.y - c.y, m = Math.sqrt(dx * dx + dy * dy) || 1; s += '<text x="' + (p.x + dx / m * 20) + '" y="' + (p.y + dy / m * 20 + 6) + '" text-anchor="middle" font-size="18" font-weight="700" fill="' + col + '">' + nombres[i] + "</text>"; });
  return s; }
function pintaSE(){
  var Q = copia(), lb = lados(SE.P), lr = lados(Q), ab = angulos(SE.P), ar = angulos(Q), s = "";
  s += tri(SE.P, "#1565c0", ["A", "B", "C"]) + tri(Q, "#c62828", ["A′", "B′", "C′"]);
  SE.P.forEach(function(p, i){ s += '<circle class="vertice" data-i="' + i + '" tabindex="0" role="slider" aria-label="' + T("Vertex ", "Vértice ") + "ABC".charAt(i) + T(" of the blue triangle. Use the arrow keys to move it.", " del triángulo azul. Use las flechas para moverlo.") + '" aria-valuetext="x ' + Math.round(p.x / ESCALA) + ", y " + Math.round((320 - p.y) / ESCALA) + '" cx="' + p.x + '" cy="' + p.y + '" r="11" fill="#fff" stroke="#1565c0" stroke-width="3"/>'; });
  var voz = T("Blue triangle ABC and red triangle A′B′C′. ", "Triángulo azul ABC y triángulo rojo A′B′C′. ") + (SE.modo === "igual" ? T("The red one is an exact copy.", "El rojo es una copia exacta.") : T("The red one is the blue one scaled by " + SE.k + ".", "El rojo es el azul a escala " + SE.k + "."));
  $("se-svg").innerHTML = '<svg class="geo-svg" id="se-lienzo" viewBox="0 0 640 330" role="group" aria-label="' + voz + '">' + s + "</svg>";
  var n = ["BC", "AC", "AB"], np = ["B′C′", "A′C′", "A′B′"], f = function(x){ return (Math.round(x / ESCALA * 10) / 10).toFixed(1); };
  var h = '<table class="comparar"><caption>' + T("Sides and angles of the two triangles (1 unit = 1 square of the grid)", "Lados y ángulos de los dos triángulos (1 unidad = 1 cuadro)") + '</caption><thead><tr><th scope="col">' + T("Blue", "Azul") + '</th><th scope="col">' + T("Red", "Rojo") + '</th><th scope="col">' + T("Red ÷ blue", "Rojo ÷ azul") + "</th></tr></thead><tbody>";
  for (var i = 0; i < 3; i++) h += "<tr><td>" + n[i] + " = " + f(lb[i]) + "</td><td>" + np[i] + " = " + f(lr[i]) + "</td><td>" + (Math.round(lr[i] / lb[i] * 100) / 100).toFixed(2) + "</td></tr>";
  for (i = 0; i < 3; i++) h += "<tr><td>∠" + "ABC".charAt(i) + " = " + Math.round(ab[i]) + "°</td><td>∠" + "ABC".charAt(i) + "′ = " + Math.round(ar[i]) + "°</td><td>" + (Math.round(ab[i]) === Math.round(ar[i]) ? T("equal", "iguales") : "—") + "</td></tr>";
  $("se-tabla").innerHTML = h + "</tbody></table>";
  $("se-res").innerHTML = SE.modo === "igual" ? T("<strong>The triangles are congruent:</strong> same shape and same size. Every side ratio is 1 and the angles are equal.", "<strong>Los triángulos son congruentes (iguales):</strong> misma forma y mismo tamaño. Cada razón entre lados es 1 y los ángulos son iguales.")
    : T("<strong>The triangles are similar:</strong> same shape, different size. The angles are equal and every side of the red one is " + SE.k + " times the matching blue side: the scale factor is " + SE.k + ".", "<strong>Los triángulos son semejantes:</strong> misma forma, distinto tamaño. Los ángulos son iguales y cada lado del rojo mide " + SE.k + " veces el lado azul que le corresponde: el factor de escala es " + SE.k + ".");
  enganchaSE();
}
function aSVG(ev){ var svg = $("se-lienzo"), r = svg.getBoundingClientRect(); return {x: (ev.clientX - r.left) * 640 / r.width, y: (ev.clientY - r.top) * 330 / r.height}; }
function limita(p){ return {x: Math.max(20, Math.min(300, p.x)), y: Math.max(20, Math.min(310, p.y))}; }
function enganchaSE(){
  Array.prototype.forEach.call(document.querySelectorAll("#se-svg .vertice"), function(c){
    var i = +c.getAttribute("data-i");
    c.addEventListener("pointerdown", function(ev){ ev.preventDefault(); SE.arrastra = i; });
    c.addEventListener("keydown", function(ev){
      var d = {ArrowLeft: [-10, 0], ArrowRight: [10, 0], ArrowUp: [0, -10], ArrowDown: [0, 10]}[ev.key];
      if (!d) return; ev.preventDefault();
      SE.P[i] = limita({x: SE.P[i].x + d[0], y: SE.P[i].y + d[1]}); pintaSE();
      var f = document.querySelector('#se-svg .vertice[data-i="' + i + '"]'); if (f) f.focus();
    });
  });
}
document.addEventListener("pointermove", function(ev){ if (SE.arrastra < 0) return; SE.P[SE.arrastra] = limita(aSVG(ev)); pintaSE(); });
document.addEventListener("pointerup", function(){ SE.arrastra = -1; });
function modoSE(m){
  SE.modo = m;
  $("se-igual").setAttribute("aria-pressed", m === "igual" ? "true" : "false"); $("se-sem").setAttribute("aria-pressed", m === "sem" ? "true" : "false");
  $("se-escala").style.display = m === "sem" ? "block" : "none";
  pintaSE();
}
$("se-igual").addEventListener("click", function(){ modoSE("igual"); });
$("se-sem").addEventListener("click", function(){ modoSE("sem"); });
$("se-k").addEventListener("input", function(){ SE.k = +this.value; $("se-kval").textContent = SE.k; pintaSE(); });
modoSE("igual");

/* Practice: congruent, similar, or neither? */
function genCSN(){
  var base = elige([[3, 4, 5], [5, 5, 8], [4, 6, 7], [6, 8, 10], [5, 7, 9], [2, 3, 4]]), tp = aleatorio(1, 3), otro, k = elige([2, 3, 1.5, 0.5]);
  if (tp === 1) otro = baraja(base.slice());
  else if (tp === 2) otro = baraja(base.map(function(x){ return x * k; }));
  else { do { otro = base.map(function(x){ return x * k; }); var j = aleatorio(0, 2); otro[j] = otro[j] + elige([1, 2, -1]); otro.sort(function(p, q){ return p - q; }); } while (otro[0] <= 0 || otro[0] + otro[1] <= otro[2]); otro = baraja(otro); }
  var fmt = function(l){ return l.map(function(x){ return String(x); }).join(", "); };
  var exp = tp === 1 ? T("The sides are the same numbers, only in a different order: the triangles are congruent.", "Los lados son los mismos números, solo en otro orden: los triángulos son congruentes.")
          : (tp === 2 ? T("Order both lists from smallest to largest: every side of the second is " + k + " times the first. Similar, with scale factor " + k + ".", "Ordene las dos listas de menor a mayor: cada lado del segundo es " + k + " veces el del primero. Semejantes, con factor de escala " + k + ".")
                      : T("Order both lists from smallest to largest and divide: the ratios are not all the same, so the triangles are neither congruent nor similar.", "Ordene las dos listas de menor a mayor y divida: las razones no son todas iguales, así que los triángulos no son ni congruentes ni semejantes."));
  return {enun: T("Triangle 1 has sides " + fmt(base) + ". Triangle 2 has sides " + fmt(otro) + ". How are they related?", "El triángulo 1 tiene lados " + fmt(base) + ". El triángulo 2 tiene lados " + fmt(otro) + ". ¿Qué relación tienen?"), enOrden: true,
    opciones: [{html: T("Congruent", "Congruentes"), clave: "c"}, {html: T("Similar, but not congruent", "Semejantes, pero no congruentes"), clave: "s"}, {html: T("Neither", "Ninguna de las dos"), clave: "n"}],
    correcta: ["c", "s", "n"][tp - 1], porClave: {}, pista: T("Order the sides of each triangle from smallest to largest and divide matching sides.", "Ordene los lados de cada triángulo de menor a mayor y divida los lados que se corresponden."), bien: exp, mal: exp};
}
OMR("p1", genCSN);
'''

def pagina_semejanza():
    mods = [
     (t("explore", "explorar"), t("Congruent and similar triangles", "Triángulos congruentes y semejantes"),
      f'''      <p>{t("Two triangles are <strong>congruent</strong> when they have the same shape and the same size: equal sides and equal angles. They are <strong>similar</strong> when they have the same shape but maybe a different size: equal angles and proportional sides.", "Dos triángulos son <strong>congruentes</strong> (iguales) cuando tienen la misma forma y el mismo tamaño: lados iguales y ángulos iguales. Son <strong>semejantes</strong> cuando tienen la misma forma, aunque pueden tener distinto tamaño: ángulos iguales y lados proporcionales.")}</p>
      <p>{t("Drag the white points of the blue triangle (or focus them and use the arrow keys). The red triangle follows. Switch between the two modes and, in similar mode, change the scale factor.", "Arrastre los puntos blancos del triángulo azul (o selecciónelos con el tabulador y use las flechas). El triángulo rojo lo sigue. Cambie entre los dos modos y, en el modo de semejanza, cambie el factor de escala.")}</p>
      <div class="panel">
        <div class="fila-btn" style="justify-content:center;"><button type="button" class="btn-sec" id="se-igual" aria-pressed="true">{t("Congruent", "Congruentes")}</button><button type="button" class="btn-sec" id="se-sem" aria-pressed="false">{t("Similar", "Semejantes")}</button></div>
        <div class="campo" id="se-escala" style="display:none"><label for="se-k">{t("Scale factor:", "Factor de escala:")} <span id="se-kval">1.5</span></label><input type="range" id="se-k" min="0.5" max="2" step="0.1" value="1.5"></div>
        <div id="se-svg"></div>
        <div class="datos-geo" id="se-res" aria-live="polite"></div>
        <div class="tabla-scroll" id="se-tabla"></div>
      </div>
{B.om("p1", t("Practice: congruent, similar, or neither?", "Practique: ¿congruentes, semejantes o ninguna?"))}''')]
    return mods, JS_SEMEJANZA

PAGINAS = [
 ("6-1", "explore-angles", "explorar-angulos", t, pagina_angulos, ("Explore: angles, parallel lines, and a transversal", "Explorar: ángulos, paralelas y una transversal"), ("Angles formed by parallel lines and a transversal", "Ángulos entre paralelas y una transversal")),
 ("6-2", "explore-pythagoras", "explorar-pitagoras", t, pagina_pitagoras, ("Explore: the Pythagorean theorem in real life", "Explorar: el teorema de Pitágoras en la vida real"), ("The Pythagorean theorem in real life", "El teorema de Pitágoras en la vida real")),
 ("6-3", "explore-similar", "explorar-semejanza", t, pagina_semejanza, ("Explore: congruent and similar triangles", "Explorar: triángulos congruentes y semejantes"), ("Congruent and similar triangles", "Triángulos congruentes y semejantes")),
]

def construye():
    for n, en, es, _, hacer, tit, corto in PAGINAS:
        num = n.replace("-", ".")
        html = {}
        for lang in ("en", "es"):
            B.L = lang
            mods, js = hacer()
            meta = t("An interactive activity to explore what you learned in Lesson " + num + ". It goes with the lesson and its practice page.", "Una actividad interactiva para explorar lo aprendido en la Lección " + num + ". Acompaña a la lección y a su página de práctica.")
            s = B.pagina_practica(n, 6, t(*TEMA), t(*corto), meta, mods, js, estilo=ESTILO, scripts=("/math/radicals.js",))
            s = s.replace(f'<h1>{t("Lesson", "Lección")} {num} · {t(*corto)}</h1>', f'<h1>{t(*tit)}</h1>')
            s = s.replace(f'<title>{t("Practice · Lesson", "Práctica · Lección")} {num} · ', f'<title>{t("Explore", "Explorar")} · {t("Lesson", "Lección")} {num} · ')
            s = s.replace('<a class="lg-link" href="./">Math · Level 3 lessons</a>', f'<a class="lg-link" href="{t("lesson-" + n, "leccion-" + n)}.html">{t("← Back to Lesson " + num, "← Volver a la Lección " + num)}</a>')
            s = s.replace("practice (English) — built by", "explore page (English) — built by")
            html[lang] = s
        B.L = "en"
        ruta_en = f"math/level-3/{en}.html"
        open(os.path.join(ROOT, ruta_en), "w", encoding="utf-8").write(html["en"]); print("ok", ruta_en)
        tr = Traductor(ruta_en, texto=html["es"], nivel=3); tr.frecuentes()
        tr.cabecera(f"<!-- LearnGED · Nivel 3 · Lección {num} · {corto[1]} — página para explorar (español) — construida con tools/build_n3_explora_6.py\n     José M. Fernández · CC BY-NC-SA 4.0 -->")
        ruta_es = f"es/matematicas/nivel-3/{es}.html"
        tr.guarda(ruta_es)
        s = open(os.path.join(ROOT, ruta_es), encoding="utf-8").read()
        for frase in ["New exercise", "Back to contents", "On this page", "Open all", "Check<"]:
            if frase in s: print("  ¡OJO! queda en inglés en", ruta_es, ":", frase)

if __name__ == "__main__":
    construye()
