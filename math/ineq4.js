/* LearnGED · Level 4 · Topic 7, Lesson 7.1 — linear inequalities in two variables and systems of them.
   Loaded after coord4.js (Plano, sg, par, parVoz). An inequality is {a, b, c, op}: ax + by op c,
   with op one of "<", "<=", ">", ">=". Optional vis: how it is shown (for example "y ≤ x + 1"). */

var COL_DES = ["#1565c0", "#c62828", "#6a1b9a", "#ef6c00"];
var SIMB = {"<": "<", "<=": "≤", ">": ">", ">=": "≥"};
var VOZ_SIMB = {"<": ["is less than", "es menor que"], "<=": ["is less than or equal to", "es menor o igual que"], ">": ["is greater than", "es mayor que"], ">=": ["is greater than or equal to", "es mayor o igual que"]};
var VOLTEA = {"<": ">", "<=": ">=", ">": "<", ">=": "<="};

function D4(a, b, c, op, vis){ return {a: a, b: b, c: c, op: op, vis: vis}; }
function dMcd(a, b){ a = Math.abs(a); b = Math.abs(b); while (b){ var t = a % b; a = b; b = t; } return a; }
function dFr(n, d){ if (d < 0){ n = -n; d = -d; } var g = dMcd(n, d) || 1; n /= g; d /= g; return d === 1 ? sg(n) : (n < 0 ? "−" : "") + Math.abs(n) + "/" + d; }
/* y op mx + k when b ≠ 0 (the symbol turns around when dividing by a negative b); x op k when b = 0 */
function dTxt(D){
  if (D.vis) return D.vis;
  if (!D.b){ var op0 = D.a < 0 ? VOLTEA[D.op] : D.op; return "x " + SIMB[op0] + " " + dFr(D.c, D.a); }
  var op = D.b < 0 ? VOLTEA[D.op] : D.op, mt = dFr(-D.a, D.b), kt = dFr(D.c, D.b), s = "";
  if (D.a) s = (mt === "1" ? "" : mt === "−1" ? "−" : mt.indexOf("/") > 0 ? (mt.charAt(0) === "−" ? "−(" + mt.slice(1) + ")" : "(" + mt + ")") : mt) + "x";
  if (D.c) s += s ? (kt.charAt(0) === "−" ? " − " + kt.slice(1) : " + " + kt) : kt;
  return "y " + SIMB[op] + " " + (s || "0");
}
/* the same inequality written as ax + by op c */
function dStd(D){ var s = "", t = function(k, v, pr){ if (!k) return ""; var a = Math.abs(k); return (k < 0 ? (pr ? "−" : " − ") : (pr ? "" : " + ")) + (a === 1 ? "" : a) + v; };
  s = t(D.a, "x", true); s += t(D.b, "y", !s); return s + " " + SIMB[D.op] + " " + sg(D.c); }
function dVoz(txt){ var op = ["≤", "≥", "<", ">"].filter(function(o){ return txt.indexOf(o) >= 0; })[0], k = {"≤": "<=", "≥": ">=", "<": "<", ">": ">"}[op];
  var pz = txt.split(op), f = function(s){ return s.replace(/−/g, T(" minus ", " menos ")).replace(/\+/g, T(" plus ", " más ")); };
  return f(pz[0]) + " " + T(VOZ_SIMB[k][0], VOZ_SIMB[k][1]) + " " + f(pz[1]); }
function dHTML(D){ var s = dTxt(D); return envuelve(s, dVoz(s)); }
function sisDesHTML(L){ return '<span class="sistema" aria-hidden="true"><span class="llave">{</span><span class="ecs">' + L.map(function(D){ return "<span>" + dTxt(D) + "</span>"; }).join("") + '</span></span><span class="sr-only">' + T("The system: ", "El sistema: ") + L.map(function(D){ return dVoz(dTxt(D)); }).join(T("; and ", "; y ")) + "</span>"; }
function estricta(D){ return D.op === "<" || D.op === ">"; }
function valD(D, x, y){ return D.a * x + D.b * y; }
function enFrontera(D, x, y){ return Math.abs(valD(D, x, y) - D.c) < 1e-9; }
function cumpleD(D, x, y){ var v = valD(D, x, y) - D.c; if (Math.abs(v) < 1e-9) return !estricta(D); return D.op.charAt(0) === "<" ? v < 0 : v > 0; }
/* a written substitution: 2(0) + (0) > 4 → 0 > 4 */
function dSust(D, x, y){
  if (D.vis && D.b && /^y /.test(D.vis)){ /* keep the y = mx + k shape: y op m(x) + k */
    var op = D.b < 0 ? VOLTEA[D.op] : D.op, m = -D.a / D.b, k = D.c / D.b, der = "", px = "(" + sg(x) + ")";
    if (D.a) der = (m === 1 ? "" : m === -1 ? "−" : sg(r4(m))) + px;
    if (k) der += der ? (k < 0 ? " − " + sg(r4(-k)) : " + " + sg(r4(k))) : sg(r4(k));
    return {txt: sg(y) + " " + SIMB[op] + " " + (der || "0"), izq: y, der: r4(m * x + k), op: op}; }
  var s = "", pr = true;
  [[D.a, x], [D.b, y]].forEach(function(p){ if (!p[0]) return; var k = p[0], a = Math.abs(k); s += (pr ? (k < 0 ? "−" : "") : (k < 0 ? " − " : " + ")) + (a === 1 ? "" : a) + "(" + sg(p[1]) + ")"; pr = false; });
  if (!D.b && D.a && D.vis && /^x /.test(D.vis)){ var op2 = D.a < 0 ? VOLTEA[D.op] : D.op; return {txt: sg(x) + " " + SIMB[op2] + " " + dFr(D.c, D.a), izq: x, der: r4(D.c / D.a), op: op2}; }
  return {txt: s + " " + SIMB[D.op] + " " + sg(D.c), izq: valD(D, x, y), der: D.c, op: D.op};
}
function r4(v){ return Math.round(v * 1e4) / 1e4; }
function dVerdad(S){ var v = S.izq - S.der; return Math.abs(v) < 1e-9 ? (S.op === "<=" || S.op === ">=") : (S.op.charAt(0) === "<" ? v < 0 : v > 0); }

/* Half-plane clipping (Sutherland–Hodgman): what remains of a convex polygon inside ax + by op c (closed) */
function recorta(poli, D){
  var dentro = function(p){ var v = valD(D, p[0], p[1]) - D.c; return D.op.charAt(0) === "<" ? v <= 1e-9 : v >= -1e-9; }, out = [];
  for (var i = 0; i < poli.length; i++){
    var A = poli[i], B = poli[(i + 1) % poli.length], ia = dentro(A), ib = dentro(B);
    if (ia) out.push(A);
    if (ia !== ib){ var va = valD(D, A[0], A[1]) - D.c, vb = valD(D, B[0], B[1]) - D.c, t = va / (va - vb); out.push([A[0] + t * (B[0] - A[0]), A[1] + t * (B[1] - A[1])]); }
  }
  return out;
}
function areaPoli(l){ var s = 0; for (var i = 0; i < l.length; i++){ var a = l[i], b = l[(i + 1) % l.length]; s += a[0] * b[1] - b[0] * a[1]; } return Math.abs(s) / 2; }
/* the part of the boundary line inside the box */
function segFrontera(D, R){
  var l = [], add = function(p){ if (p[0] >= R.x0 - 1e-9 && p[0] <= R.x1 + 1e-9 && p[1] >= R.y0 - 1e-9 && p[1] <= R.y1 + 1e-9 && !l.some(function(q){ return Math.abs(q[0] - p[0]) < 1e-7 && Math.abs(q[1] - p[1]) < 1e-7; })) l.push(p); };
  if (D.b){ add([R.x0, (D.c - D.a * R.x0) / D.b]); add([R.x1, (D.c - D.a * R.x1) / D.b]); }
  if (D.a){ add([(D.c - D.b * R.y0) / D.a, R.y0]); add([(D.c - D.b * R.y1) / D.a, R.y1]); }
  if (l.length < 2) return null;
  l.sort(function(u, v){ return u[0] - v[0] || u[1] - v[1]; });
  return [l[0], l[l.length - 1]];
}
/* Graph of one or several inequalities.
   o.rango {x0, x1, y0, y1} (default −8..8); o.cada: shade each half-plane in its own color (default when there is one);
   o.region: shade the intersection in green (default when there are several); o.punto: [x, y] to check;
   o.prueba: [x, y] the test point; o.etiquetas: false to hide the labels; o.ancho. */
function grafDes(L, o){
  o = o || {}; var R = o.rango || {x0: -8, x1: 8, y0: -8, y1: 8}, span = Math.max(R.x1 - R.x0, R.y1 - R.y0);
  var P = Plano({xmin: R.x0, xmax: R.x1, ymin: R.y0, ymax: R.y1, u: Math.floor(440 / span), paso: span > 14 ? 2 : 1}), s = "", caja = [[R.x0, R.y0], [R.x1, R.y0], [R.x1, R.y1], [R.x0, R.y1]];
  var cada = o.cada === undefined ? L.length === 1 : o.cada, region = o.region === undefined ? L.length > 1 : o.region;
  var pts = function(l){ return l.map(function(p){ return P.X(p[0]).toFixed(1) + "," + P.Y(p[1]).toFixed(1); }).join(" "); };
  if (cada) L.forEach(function(D, i){ var h = recorta(caja, D); if (h.length > 2) s += '<polygon points="' + pts(h) + '" fill="' + COL_DES[i % 4] + '" fill-opacity="' + (L.length === 1 ? .2 : .1) + '"/>'; });
  var reg = caja; L.forEach(function(D){ reg = recorta(reg, D); });
  var hayReg = reg.length > 2 && areaPoli(reg) > 1e-6;
  if (region && hayReg && L.length) s += '<polygon points="' + pts(reg) + '" fill="#2e7d32" fill-opacity=".32" stroke="none"/>';
  var usados = [];
  L.forEach(function(D, i){
    var sg2 = segFrontera(D, R); if (!sg2) return;
    s += P.seg(sg2[0], sg2[1], COL_DES[i % 4], 3, estricta(D) ? "9 7" : null);
    if (o.etiquetas === false) return;
    /* label: along the line, on either side; prefer the side that is NOT shaded, away from the other lines, the other labels,
       and the axes with their numbers */
    var txt = dTxt(D), w = txt.length * 8.2, dx = P.X(sg2[1][0]) - P.X(sg2[0][0]), dy = P.Y(sg2[1][1]) - P.Y(sg2[0][1]), lg = Math.hypot(dx, dy), nx = -dy / lg, ny = dx / lg, mejor = null, bd = -1e9;
    var ax = R.x0 <= 0 && R.x1 >= 0 ? P.X(0) : null, ay = R.y0 <= 0 && R.y1 >= 0 ? P.Y(0) : null;
    var franja = function(a0, a1, b0, b1){ return a1 < b0 ? b0 - a1 : b1 < a0 ? a0 - b1 : 0; };
    [1, -1].forEach(function(sd){
      for (var f = .9; f > .05; f -= .1){
        var off = w / 2 * Math.abs(nx) + 9 * Math.abs(ny) + 6, cx = P.X(sg2[0][0]) + f * dx + sd * nx * off, cy = P.Y(sg2[0][1]) + f * dy + sd * ny * off + 5;
        if (cx - w / 2 < P.X(R.x0) + 2 || cx + w / 2 > P.X(R.x1) - 2 || cy - 14 < P.Y(R.y1) || cy + 2 > P.Y(R.y0)) continue;
        var d = 30;
        usados.forEach(function(u){ if (Math.abs(u[0] - cx) < (w + u[2]) / 2 + 6) d = Math.min(d, Math.abs(u[1] - cy) - 16); });
        L.forEach(function(E, j){ for (var k = -.5; k <= .5; k += .25) [cy - 12, cy - 5, cy + 1].forEach(function(yy){ var q = P.desdePx(cx + k * w, yy); d = Math.min(d, Math.abs(valD(E, q[0], q[1]) - E.c) / Math.hypot(E.a, E.b) * P.u + (j === i ? 2 : 0)); }); });
        if (ay !== null) d = Math.min(d, Math.max(franja(cy - 14, cy + 2, ay - 3, ay + 19), 0) - (franja(cy - 14, cy + 2, ay - 3, ay + 19) ? 0 : 10));
        if (ax !== null) d = Math.min(d, Math.max(franja(cx - w / 2, cx + w / 2, ax - 26, ax + 3), 0) - (franja(cx - w / 2, cx + w / 2, ax - 26, ax + 3) ? 0 : 10));
        var q0 = P.desdePx(cx, cy - 5), libre = !cumpleD(D, q0[0], q0[1]);
        var sc = d + (libre ? 3 : 0);
        if (sc > bd){ bd = sc; mejor = [cx, cy]; } } });
    if (mejor){ usados.push([mejor[0], mejor[1], w]); s += '<text x="' + mejor[0].toFixed(1) + '" y="' + mejor[1].toFixed(1) + '" font-size="14" font-weight="700" fill="' + COL_DES[i % 4] + '" text-anchor="middle" paint-order="stroke" stroke="#fff" stroke-width="4">' + txt + "</text>"; }
  });
  var marca = function(p, color, et){ return '<circle cx="' + P.X(p[0]).toFixed(1) + '" cy="' + P.Y(p[1]).toFixed(1) + '" r="7" fill="' + color + '" stroke="#fff" stroke-width="2"/>' +
    '<text x="' + (P.X(p[0]) + (p[0] > (R.x0 + R.x1) / 2 ? -11 : 11)).toFixed(1) + '" y="' + (P.Y(p[1]) + (p[1] > R.y1 - 1 ? 20 : -10)).toFixed(1) + '" font-size="15" font-weight="700" fill="' + color + '" text-anchor="' + (p[0] > (R.x0 + R.x1) / 2 ? "end" : "start") + '" paint-order="stroke" stroke="#fff" stroke-width="4">' + (et || par(p[0], p[1])) + "</text>"; };
  if (o.prueba) s += marca(o.prueba, "#263238", T("test ", "prueba ") + par(o.prueba[0], o.prueba[1]));
  if (o.punto){ var ok = L.every(function(D){ return cumpleD(D, o.punto[0], o.punto[1]); }); s += marca(o.punto, ok ? "#2e7d32" : "#b71c1c"); }
  var voz = T("Graph of ", "Gráfica de ") + L.map(function(D){ return dVoz(dTxt(D)) + " (" + (estricta(D) ? T("dashed line", "línea punteada") : T("solid line", "línea sólida")) + ")"; }).join(T(" and ", " y ")) + ". " +
    (L.length > 1 ? (hayReg ? T("The region that satisfies all of them is shaded in green.", "La región que las cumple todas está sombreada en verde.") : T("No region satisfies all of them.", "Ninguna región las cumple todas.")) : T("The side that satisfies it is shaded.", "Está sombreado el lado que la cumple.")) +
    (o.punto ? " " + T("Marked: ", "Marcado: ") + parVoz(o.punto[0], o.punto[1]) + "." : "") + (o.prueba ? " " + T("Test point: ", "Punto de prueba: ") + parVoz(o.prueba[0], o.prueba[1]) + "." : "");
  return P.svg(s, voz, o.ancho || 460);
}
/* vertices of the feasible region with whole-number coordinates (for the explanations) */
function verticesReg(L, R){ var reg = [[R.x0, R.y0], [R.x1, R.y0], [R.x1, R.y1], [R.x0, R.y1]]; L.forEach(function(D){ reg = recorta(reg, D); }); return reg; }
