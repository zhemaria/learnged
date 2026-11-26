/* LearnGED · Level 2 · shared helpers for ratios, rates, percents, and money (Topics 4–6).
   Needs practice.js first. Numbers use a comma for thousands and a point for decimals in both languages. */
var TXR = ES ? {
  numero: "Escriba solo el número. Puede llevar decimales (1.25) y, si es dinero, el signo $.",
  revise: "Revise el cálculo."
} : {
  numero: "Type only the number. It may have decimals (1.25) and, for money, a $ sign.",
  revise: "Check your work."
};
/* 1234.5 → "1,234.5"; up to 3 decimals; minus sign − */
function nd(x){
  var r = Math.round(x * 1000) / 1000, neg = r < 0, p = String(Math.abs(r)).split(".");
  return (neg ? "−" : "") + com(p[0]) + (p[1] ? "." + p[1] : "");
}
/* money: $7.50, $1,200.00 */
function dinero(x){
  var neg = x < 0, c = Math.round(Math.abs(x) * 100), e = Math.floor(c / 100), d = c % 100;
  return (neg ? "−" : "") + "$" + com(e) + "." + (d < 10 ? "0" : "") + d;
}
/* "$1,200.50", "−3.5", "12" → number, or null */
function leeD(t){
  var s = String(t).trim().replace(/[−–—]/g, "-").replace(/\$/g, "").replace(/\s+/g, "");
  if (/^-?\d{1,3}(,\d{3})+(\.\d+)?$/.test(s)) s = s.replace(/,/g, "");
  return /^-?(\d+\.?\d*|\.\d+)$/.test(s) ? parseFloat(s) : null;
}
/* Evaluator for creaPracticaLibre with decimals: tol = allowed error (default 0.005) */
function numD(res, pistas, general, tol){
  var tl = tol === undefined ? 0.005 : tol;
  return function(t){
    var v = leeD(t);
    if (v === null) return { estado: "invalido", msg: TXR.numero };
    if (Math.abs(v - res) <= tl) return { estado: "bien" };
    for (var i = 0; i < (pistas || []).length; i++) if (Math.abs(v - pistas[i].v) <= tl) return { estado: "mal", msg: pistas[i].msg };
    return { estado: "mal", msg: general || TXR.revise };
  };
}
function mcdR(a, b){ a = Math.abs(a); b = Math.abs(b); while (b){ var x = a % b; a = b; b = x; } return a; }
