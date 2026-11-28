# -*- coding: utf-8 -*-
"""Artes del lenguaje, camino en español: marco de las lecciones de LearnGED.

Usa el mismo marco que Ciencias y Estudios Sociales (tools/ciencia.py: pagina_leccion,
pagina_practica, Practicas, caja, ejemplo, tabla, om, huecos…), pero
  · solo construye en español (el camino en inglés es otro curso, no una traducción);
  · las páginas van en es/artes-del-lenguaje/nivel-N/ (leccion-T-N.html, practica-T-N.html);
  · los estándares salen de tools/rla.py (indicadores del GED® de RLA y CCR);
  · cargan además /rla/rla.css (color del nivel) y /rla/leng.js (voz, abecedario, guía de
    lectura, cronómetro, teatro leído, sonidos grabados).

Cada constructor (tools/build_leng1_T_N.py) hace:
    from leng_es import C, t, R, nivel
    nivel(1)
    ...
    construye(N, leccion, practica, horas="Unas 3 horas")
Después: python3 tools/build_leng_indices.py (índice del nivel y plan del curso).
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ciencia as C
import rla as R
from ciencia import t

C.MAT.update({"nombre": ("Language arts", "Artes del lenguaje"), "carpeta": ("rla", "es/artes-del-lenguaje/nivel-1"),
              "builder": "build_leng1_", "css": ["/science/science.css", "/rla/rla.css"], "icono": "📖"})

NIVELES = {
    1: ("Iniciación a la lectura y la escritura", {
        1: "El alfabeto y la dirección de la lectura",
        2: "Conciencia fonológica y fluidez",
        3: "La oración: sustantivo, adjetivo, verbo y puntuación",
        4: "Estrategias de comprensión y vocabulario",
        5: "El texto narrativo y las relaciones entre ideas",
        6: "Información visual: imágenes, mapas, tablas y gráficas",
        7: "El párrafo y los tipos de texto",
        8: "Comunicación, tecnología y proyecto final"}),
}

# Lecciones del Nivel 1 (las mismas de GEDparaHispanos; la 1.3 corresponde a la fluidez lectora)
LECCIONES = {
    1: {
        "1-1": "El alfabeto: letras mayúsculas y minúsculas",
        "1-2": "La dirección de la lectura y la estructura de la oración",
        "1-3": "Fluidez lectora: precisión, ritmo y expresión",
        "2-1": "Conciencia fonológica: rimas, sílabas y fonemas",
        "2-2": "Decodificación de palabras de una y dos sílabas",
        "2-3": "Palabras de uso frecuente y fluidez inicial",
        "3-1": "Conociendo los sustantivos y los adjetivos",
        "3-2": "La regla de oro: la concordancia",
        "3-3": "El corazón de la oración: el verbo",
        "3-4": "Los tiempos verbales: presente, pasado y futuro",
        "3-5": "Oración completa frente a fragmento",
        "3-6": "Puntuación básica y uso de mayúsculas",
        "4-1": "Predecir y preguntar antes de leer",
        "4-2": "Aclarar y resumir lo leído",
        "4-3": "A la caza de la idea principal",
        "4-4": "Los detalles que sostienen la idea",
        "4-5": "Descubrir significados con claves de contexto",
        "4-6": "La anatomía de las palabras: raíces y afijos",
        "5-1": "Los personajes y sus conflictos",
        "5-2": "El escenario y su impacto en la historia",
        "5-3": "El orden de los eventos: palabras de secuencia",
        "5-4": "Seguir instrucciones paso a paso",
        "5-5": "La relación de causa y efecto",
        "5-6": "Comparar y contrastar información",
        "6-1": "El poder de las ilustraciones para comprender",
        "6-2": "Las características del texto informativo visual",
        "6-3": "La anatomía de los mapas",
        "6-4": "Organización de datos en tablas",
        "6-5": "El duelo de las gráficas: barras y pastel",
        "6-6": "Vocabulario de dominio y aplicación",
        "7-1": "El párrafo y la técnica de la hamburguesa",
        "7-2": "Cualidades del párrafo y conectores básicos",
        "7-3": "Tres tipos de texto: narrativo e informativo",
        "7-4": "El texto de opinión y la comparación de los tres tipos",
        "7-5": "Escribir sobre información visual",
        "7-6": "El proceso de revisión",
        "8-1": "Fundamentos de la comunicación y escucha activa",
        "8-2": "Leer y conversar: la técnica 1-2-4",
        "8-3": "Alfabetización tecnológica y vocabulario digital",
        "8-4": "Presentación oral breve",
        "8-5": "Proyecto final: «Mi historia, mis metas»",
        "8-6": "Evaluación final y camino al GED",
    },
}

NIVEL = 1


def nivel(n):
    """Prepara el marco para el nivel n del camino en español."""
    global NIVEL
    NIVEL = n
    nombre, temas = NIVELES[n]
    C.MAT["carpeta"] = ("rla", f"es/artes-del-lenguaje/nivel-{n}")
    C.MAT["builder"] = f"build_leng{n}_"
    C.MAT["nombre"] = ("Language arts", f"Artes del lenguaje · Nivel {n}")
    C.TEMAS = {k: ((v, v), f"leng{n}") for k, v in temas.items()}
    C.COLOR = {"leng1": "#0b679c", "leng2": "#00695c", "leng3": "#6d28d9", "leng4": "#b42318"}


def titulo(n):
    return LECCIONES[NIVEL][n]


def estandares(cods, base=(), fund=()):
    R.L = "es"
    return R.estandares(cods, base, camino="es", fund=fund)


def escuchar(texto, etiqueta="Escuchar", vel=None):
    v = f' data-vel="{vel}"' if vel else ""
    al = "" if etiqueta else f' aria-label="Escuchar: {texto}"'
    return f'<button type="button" class="btn-voz{"" if etiqueta else " mini"}" data-hablar="{texto}"{v}{al}><span aria-hidden="true">🔊</span>{" " + etiqueta if etiqueta else ""}</button>'


AVISO_VOZ = '<p class="aviso-voz" hidden>Su navegador no tiene una voz en español, así que los botones 🔊 no van a sonar. Puede hacer las actividades leyendo usted en voz alta.</p>'


def _ajusta(html, horas):
    html = re.sub(r'<link rel="alternate" hreflang="[^"]*" href="[^"]*"/?>\n?', "", html)
    html = html.replace("Unas 4 horas con la práctica y la tarea · tome descansos", horas + " con la práctica y la tarea · tome descansos")
    html = html.replace('<script src="/science/sci.js"></script>', '<script src="/science/sci.js"></script>\n<script src="/rla/leng.js"></script>')
    if "/rla/leng.js" not in html:
        html = html.replace('<script src="/math/lesson.js"></script>', '<script src="/math/lesson.js"></script>\n<script src="/rla/leng.js"></script>')
    return html


def construye(n, hacer_leccion, hacer_practica, horas="Unas 3 horas"):
    C.L = "es"
    R.L = "es"
    carpeta = os.path.join(C.ROOT, C.carpeta())
    os.makedirs(carpeta, exist_ok=True)
    for nombre, f in ((C.lec(n), hacer_leccion), (C.prac(n), hacer_practica)):
        ruta = os.path.join(carpeta, nombre)
        open(ruta, "w", encoding="utf-8").write(_ajusta(f(), horas))
        print("ok", os.path.relpath(ruta, C.ROOT))


def marcar(pid, intro):
    """Módulo de práctica «toque las palabras» (creaMarcar de /rla/leng.js)."""
    return f"      <p>{intro}</p>\n" + C.huecos(pid)


def oracion(suj, pred, extra=""):
    """Oración con el sujeto (subrayado recto) y el predicado (ondulado) marcados."""
    return f'<p class="oracion-ej"><span class="suj">{suj}</span> <span class="pred">{pred}</span>{extra}</p>'
