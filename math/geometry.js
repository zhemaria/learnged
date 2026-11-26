/* LearnGED · Level 2 · shared helpers for area and circles (Topic 7).
   Needs practice.js and rates.js first. π ≈ 3.14 in all work; answers with the calculator's π are also accepted. */
var TXG = ES ? {
  numero: "Escriba solo el número, por ejemplo 43.96. También puede escribirlo en términos de π, como 14π.",
  numero2: "Escriba solo el número, por ejemplo 30.",
  enPi: "Correcto, en términos de π.", kPi: "El número que acompaña a π no es el correcto."
} : {
  numero: "Type only the number, for example 43.96. You may also write it in terms of π, like 14π.",
  numero2: "Type only the number, for example 30.",
  enPi: "Correct, in terms of π.", kPi: "The number in front of π is not right."
};
function r2(x){ return Math.round(x * 100) / 100; }
function rad(g){ return g * Math.PI / 180; }
/* SVG text with a chosen anchor ("start", "middle", "end") */
function textoA(p, t, tam, color, peso, anc){ return '<text x="' + f1(p[0]) + '" y="' + f1(p[1]) + '" text-anchor="' + (anc || "middle") + '" dominant-baseline="middle" font-size="' + (tam || 16) + '" font-weight="' + (peso || 700) + '" fill="' + (color || "#222") + '">' + t + '</text>'; }
function lineaD(p, q, color, ancho){ return '<line x1="' + f1(p[0]) + '" y1="' + f1(p[1]) + '" x2="' + f1(q[0]) + '" y2="' + f1(q[1]) + '" stroke="' + (color || "#b71c1c") + '" stroke-width="' + (ancho || 2) + '" stroke-dasharray="6 4"/>'; }

/* Answer = k·π (k = coefficient of π). Accepts k·3.14, k·π (calculator), or "kπ". */
function evaluaPiK(k, pistas){
  return function(t){
    var s = String(t).replace(/\s+/g, "").replace(/pi$/i, "π").replace(/,/g, "");
    var m = s.match(/^(\d+(?:\.\d+)?)π$/);
    if (m) return Math.abs(parseFloat(m[1]) - k) < 1e-6 ? { estado: "bien", msg: TXG.enPi } : { estado: "mal", msg: TXG.kPi };
    var v = leeD(s);
    if (v === null) return { estado: "invalido", msg: TXG.numero };
    var tol = 0.011 + Math.abs(k * 3.14) * 0.0005;
    if (Math.abs(v - k * 3.14) <= tol || Math.abs(v - k * Math.PI) <= tol) return { estado: "bien" };
    for (var i = 0; i < (pistas || []).length; i++){ var pk = pistas[i].k; if (Math.abs(v - pk * 3.14) <= tol || Math.abs(v - pk * Math.PI) <= tol) return { estado: "mal", msg: pistas[i].msg }; }
    return { estado: "mal", msg: TXR.revise };
  };
}
/* Answer found with π ≈ 3.14 (v3) or with the calculator's π (vpi) */
function evaluaInvPi(v3, vpi, pistas){
  return function(t){
    var v = leeD(String(t).trim());
    if (v === null) return { estado: "invalido", msg: TXG.numero2 };
    var tol = 0.011 + Math.abs(v3) * 0.0005;
    if (Math.abs(v - v3) <= tol || Math.abs(v - vpi) <= tol) return { estado: "bien" };
    for (var i = 0; i < (pistas || []).length; i++) if (Math.abs(v - pistas[i].v) <= tol) return { estado: "mal", msg: pistas[i].msg };
    return { estado: "mal", msg: TXR.revise };
  };
}

/* Flat figures with dimension labels.
   polis: [{pts, fill, stroke, sw, dash, txt, c}] in units (y up).
   cotas: [[p, q, "label", side]] — the label goes outside, to the right of the segment p→q.
   extras: {linea, pts} dashed red line · {arco, c, r, abajo, pts} half disc · {txt, p, col} label */
function figuraSVG(polis, cotas, voz, extras, alto){
  var xs = [], ys = [];
  polis.forEach(function(P){ P.pts.forEach(function(p){ xs.push(p[0]); ys.push(p[1]); }); });
  (extras || []).forEach(function(E){ (E.pts || []).forEach(function(p){ xs.push(p[0]); ys.push(p[1]); }); });
  var minX = Math.min.apply(null, xs), maxX = Math.max.apply(null, xs), minY = Math.min.apply(null, ys), maxY = Math.max.apply(null, ys);
  var H = alto || 300, esc = Math.min(480 / (maxX - minX || 1), (H - 90) / (maxY - minY || 1)), ox = 320 - (minX + maxX) / 2 * esc, oy = H / 2 + (minY + maxY) / 2 * esc;
  function T(p){ return [ox + p[0] * esc, oy - p[1] * esc]; }
  var s = '<svg class="figura" viewBox="0 0 640 ' + H + '" role="img" aria-label="' + voz + '">';
  polis.forEach(function(P){
    s += '<polygon points="' + P.pts.map(function(p){ var q = T(p); return f1(q[0]) + "," + f1(q[1]); }).join(" ") + '" fill="' + (P.fill || "#eceff1") + '" stroke="' + (P.stroke || "#37474f") + '" stroke-width="' + (P.sw || 3) + '"' + (P.dash ? ' stroke-dasharray="7 5"' : '') + '/>';
    if (P.txt) s += textoA(T(P.c), P.txt, 16, P.col || "#1c2a30", 700);
  });
  (extras || []).forEach(function(E){
    if (E.arco){ var c0 = T(E.c), r = E.r * esc; s += '<path d="M' + f1(c0[0] - r) + ' ' + f1(c0[1]) + ' A' + f1(r) + ' ' + f1(r) + ' 0 0 ' + (E.abajo ? 0 : 1) + ' ' + f1(c0[0] + r) + ' ' + f1(c0[1]) + ' Z" fill="' + (E.fill || "#cfd8dc") + '" stroke="#37474f" stroke-width="3"/>'; }
  });
  (extras || []).forEach(function(E){
    if (E.linea) s += lineaD(T(E.pts[0]), T(E.pts[1]), E.color);
    if (E.txt) s += textoA(T(E.p), E.txt, 16, E.col || "#1c2a30", 700);
  });
  (cotas || []).forEach(function(k){
    var a = T(k[0]), b = T(k[1]), mx = (a[0] + b[0]) / 2, my = (a[1] + b[1]) / 2, dx = b[0] - a[0], dy = b[1] - a[1], L = Math.hypot(dx, dy) || 1, nx = dy / L, ny = -dx / L, sg = -(k[3] || 1), ux = nx * sg, uy = ny * sg;
    var anc = ux > 0.5 ? "start" : (ux < -0.5 ? "end" : "middle"), d = anc === "middle" ? 16 : 9;
    s += textoA([mx + ux * d, my + uy * d], k[2], 18, "#222", 700, anc);
  });
  return s + '</svg>';
}
