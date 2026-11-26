/* LearnGED · math/radicals.js — shared engine for Level 3 · Topic 3 (radicals and the real numbers).
   Radicals are kept as k√r with k and r whole numbers, so every simplification is exact.
   Works in English and Spanish (practice.js sets ES from <html lang>). Load after practice.js.
   Ported from GEDparaHispanos (algebra/n3-l3-*.html). José M. Fernández · CC BY-NC-SA 4.0 */

function T(en, es){ return ES ? es : en; }
function mcd(a, b){ a = Math.abs(a); b = Math.abs(b); while (b){ var t = a % b; a = b; b = t; } return a; }
function esCuadrado(n){ if (n < 0) return false; var s = Math.round(Math.sqrt(n)); return s * s === n; }
/* √n = k√r with the largest possible perfect square */
function simplRad(n){ for (var s = Math.floor(Math.sqrt(n)); s >= 1; s--) if (n % (s * s) === 0) return {k: s, r: n / (s * s)}; return {k: 1, r: n}; }
function cuadradosQueDividen(n){ var l = []; for (var s = 2; s * s <= n; s++) if (n % (s * s) === 0) l.push(s); return l; }
function aprox(x, d){ return (Math.round(x * Math.pow(10, d)) / Math.pow(10, d)).toFixed(d).replace("-", "−"); }
function supH(k){ return "<sup>" + k + "</sup>"; }
function menos(t){ return String(t).replace("-", T("negative ", "menos ")); }
function envuelve(vis, voz){ return '<span class="ex" aria-hidden="true">' + vis + '</span><span class="sr-only">' + voz + "</span>"; }
var RAIZ = T("the square root of ", "raíz cuadrada de ");

/* Radical k√r */
function radVis(k, r){
  if (r === 1) return String(k).replace("-", "−");
  if (k === 0) return "0";
  return (k === 1 ? "" : (k === -1 ? "−" : String(k).replace("-", "−"))) + '<span class="rad">√<span class="rc">' + r + "</span></span>";
}
function radVoz(k, r){
  if (r === 1) return menos(k);
  if (k === 0) return "0";
  return (k === 1 ? "" : (k === -1 ? T("negative ", "menos ") : menos(k) + T(" times ", " por "))) + RAIZ + r;
}
function radHTML(k, r){ return envuelve(radVis(k, r), radVoz(k, r)); }
function radClave(k, r){ return k + "r" + r; }
function opRad(k, r){ return {html: radHTML(k, r), clave: radClave(k, r)}; }

/* Fractions */
function reduce(p, q){ if (q < 0){ p = -p; q = -q; } var g = mcd(p, q) || 1; return {p: p / g, q: q / g}; }
function fracVis(p, q){ if (q === 1) return String(p).replace("-", "−"); return (p < 0 ? "−" : "") + '<span class="fracc"><span class="fa">' + Math.abs(p) + '</span><span class="fb2">' + q + "</span></span>"; }
function fracVoz(p, q){ return q === 1 ? menos(p) : (p < 0 ? T("negative ", "menos ") : "") + Math.abs(p) + T(" over ", " sobre ") + q; }
function fracHTML(p, q){ return envuelve(fracVis(p, q), fracVoz(p, q)); }
function leeFraccion(t){
  var m = String(t).trim().replace(/\s+/g, "").replace(/[−–]/g, "-").match(/^(-?\d+)(?:\/(\d+))?$/); if (!m) return null;
  var q = m[2] === undefined ? 1 : parseInt(m[2], 10); if (q === 0) return null;
  return {p: parseInt(m[1], 10), q: q};
}
function leeDecimal(t){
  var s = String(t).trim().replace(/\s+/g, "").replace(/[−–]/g, "-");
  if (s.indexOf(".") < 0 && /^-?\d+,\d+$/.test(s)) s = s.replace(",", ".");
  return /^-?(\d+\.?\d*|\.\d+)$/.test(s) ? parseFloat(s) : null;
}
function periodicoHTML(ent, noRep, per){
  return envuelve(ent + "." + noRep + per + per + per + "…",
    ent + T(" point ", " punto ") + (noRep ? noRep.split("").join(" ") + T(", and then ", ", y después ") : "") + T("the group ", "el grupo ") + per.split("").join(" ") + T(" repeating forever", " repetido sin fin"));
}

/* Expressions with several terms: a list of {k, r}; r = 1 is a whole number */
function TM(k, r){ return {k: k, r: r}; }
function exprVis(t){ if (!t.length) return "0"; return t.map(function(x, i){ return i === 0 ? radVis(x.k, x.r) : (x.k < 0 ? " − " : " + ") + radVis(Math.abs(x.k), x.r); }).join(""); }
function exprVoz(t){ if (!t.length) return "0"; return t.map(function(x, i){ return i === 0 ? radVoz(x.k, x.r) : (x.k < 0 ? T(" minus ", " menos ") : T(" plus ", " más ")) + radVoz(Math.abs(x.k), x.r); }).join(""); }
function exprHTML(t){ return envuelve(exprVis(t), exprVoz(t)); }
function exprClave(t){ return t.map(function(x){ return x.k + "r" + x.r; }).join("|") || "0"; }
function opExpr(t){ return {html: exprHTML(t), clave: exprClave(t)}; }
function combina(t){
  var orden = [], sm = {};
  t.forEach(function(x){ if (!(x.r in sm)){ sm[x.r] = 0; orden.push(x.r); } sm[x.r] += x.k; });
  return orden.filter(function(r){ return sm[r] !== 0; }).map(function(r){ return TM(sm[r], r); });
}
function simplTermino(x){ var s = simplRad(x.r); return TM(x.k * s.k, s.r); }
function valor(t){ return t.reduce(function(a, x){ return a + x.k * Math.sqrt(x.r); }, 0); }

var LIBRES = [2, 3, 5, 6, 7, 10, 11, 13, 14, 15];
function radicandoAzar(maximo){
  maximo = maximo || 300;
  for (var i = 0; i < 100; i++){ var s = aleatorio(2, 10), n = s * s * elige(LIBRES); if (n <= maximo) return n; }
  return 72;
}
function yLista(l){ return l.length <= 1 ? l.join("") : l.slice(0, -1).join(", ") + T(", and ", " y ") + l[l.length - 1]; }

/* Number line in SVG: from a to b, ticks every 'paso', labels on the whole numbers */
function rectaSVG(a, b, paso, marcas, titulo){
  var W = 640, H = 150, x0 = 30, x1 = W - 30, y = 92;
  function X(v){ return x0 + (v - a) * (x1 - x0) / (b - a); }
  var s = '<svg class="recta-svg" viewBox="0 0 ' + W + " " + H + '" role="img" aria-label="' + titulo + '"><line x1="' + x0 + '" y1="' + y + '" x2="' + x1 + '" y2="' + y + '" stroke="#424242" stroke-width="2"/>';
  var n = Math.round((b - a) / paso);
  for (var i = 0; i <= n; i++){
    var v = a + i * paso, ent = Math.abs(v - Math.round(v)) < 1e-9, xv = X(v);
    s += '<line x1="' + xv + '" y1="' + (y - (ent ? 10 : 5)) + '" x2="' + xv + '" y2="' + (y + (ent ? 10 : 5)) + '" stroke="#424242" stroke-width="' + (ent ? 2 : 1) + '"/>';
    if (ent) s += '<text x="' + xv + '" y="' + (y + 38) + '" text-anchor="middle" font-size="24" fill="#222">' + String(Math.round(v)).replace("-", "−") + "</text>";
  }
  (marcas || []).forEach(function(m){
    var xm = X(m.v), col = m.color || "#004d40";
    s += '<path d="M' + xm + " " + (y - 4) + ' l-11 -18 h22 z" fill="' + col + '"/><text x="' + xm + '" y="' + (y - (m.alto ? 58 : 28)) + '" text-anchor="middle" font-size="22" font-weight="700" fill="' + col + '">' + m.txt + "</text>";
  });
  return s + "</svg>";
}

/* Multiple choice with two tries (practice.js). gen() returns {enun, opciones: [{html, clave}], correcta, porClave, bien, mal} */
function OMR(pre, gen){
  creaPracticaOM(pre, function(){
    var q = gen();
    q.pistas = q.porClave || {};
    q.pista = q.pista || T("Look again and try once more.", "Revise otra vez y vuelva a intentarlo.");
    return q;
  });
}

/* Typed radical k √ r with two tries: gen() returns {enun, k, r, explica} */
function creaPracticaRad(pre, gen){
  var est = {primero: 0, pista: 0, total: 0, actual: null, resuelta: false, intentos: 0};
  function marcador(){ $(pre + "-marcador").textContent = est.total ? TX.resueltos(est.primero + est.pista, est.primero, est.total) : ""; }
  function pinta(){
    est.actual = gen(); est.resuelta = false; est.intentos = 0;
    $(pre + "-enun").innerHTML = est.actual.enun;
    [pre + "-k", pre + "-r"].forEach(function(id){ $(id).value = ""; $(id).disabled = false; $(id).classList.remove("error"); });
    $(pre + "-comprobar").disabled = false; $(pre + "-fb").className = "fb"; $(pre + "-fb").innerHTML = "";
  }
  function bloquea(){ $(pre + "-k").disabled = true; $(pre + "-r").disabled = true; $(pre + "-comprobar").disabled = true; }
  function comprueba(){
    if (est.resuelta) return;
    var q = est.actual, fb = $(pre + "-fb"), kt = $(pre + "-k").value.trim(), rt = $(pre + "-r").value.trim();
    if (kt === "") kt = "1";
    var okK = /^\d+$/.test(kt), okR = /^\d+$/.test(rt);
    $(pre + "-k").classList.toggle("error", !okK); $(pre + "-r").classList.toggle("error", !okR);
    if (!okK || !okR){ fb.className = "fb pista"; fb.innerHTML = T("Type whole numbers: the coefficient (outside the radical) and the radicand (inside). If there is no coefficient, leave it blank or type 1.", "Escriba números enteros: el coeficiente (fuera del radical) y el radicando (dentro). Si no hay coeficiente, déjelo vacío o escriba 1."); return; }
    var k = parseInt(kt, 10), r = parseInt(rt, 10);
    est.intentos++;
    if (k === q.k && r === q.r){
      est.resuelta = true; est.total++; if (est.intentos === 1) est.primero++; else est.pista++;
      fb.className = "fb bien"; fb.innerHTML = TX.bien + radHTML(q.k, q.r) + ". " + (q.explica || "") + " <em>" + (est.intentos === 1 ? elige(ELOGIO) : elige(ELOGIO2)) + "</em>"; bloquea();
    } else {
      var msg;
      if (k * k * r === q.k * q.k * q.r) msg = T("It has the same value, but it can still be simplified: ", "Tiene el mismo valor, pero todavía se puede simplificar: ") + radHTML(1, r) + T(" contains a perfect square.", " contiene un cuadrado perfecto.");
      else if (r === q.r) msg = T("The radicand is right; check the coefficient.", "El radicando está bien; revise el coeficiente.");
      else if (k === q.k) msg = T("The coefficient is right; check what stays inside the radical.", "El coeficiente está bien; revise lo que queda dentro del radical.");
      else msg = T("Look for the largest perfect square that divides the radicand.", "Busque el mayor cuadrado perfecto que divide al radicando.");
      if (est.intentos >= 2){ est.resuelta = true; est.total++; fb.className = "fb mal"; fb.innerHTML = TX.asi + msg + " " + T("The answer is ", "La respuesta es ") + radHTML(q.k, q.r) + ". " + (q.explica || "") + TX.nuevo; bloquea(); }
      else { fb.className = "fb pista"; fb.innerHTML = TX.todavia + msg + TX.unoMas; }
    }
    marcador();
  }
  $(pre + "-comprobar").addEventListener("click", comprueba);
  [pre + "-k", pre + "-r"].forEach(function(id){ $(id).addEventListener("keydown", function(ev){ if (ev.key === "Enter") comprueba(); }); });
  $(pre + "-nuevo").addEventListener("click", pinta);
  pinta(); marcador();
}
