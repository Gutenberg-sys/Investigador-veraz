---
name: investigador-veraz
description: Investigación intensiva de información reciente con fuentes verificables y fiables. Úsala siempre que el usuario pida verificar datos, contrastar hechos, buscar "la verdad" sobre algo, comprobar si una noticia o afirmación es real, o pida explícitamente fuentes fiables/verificables. Dispara también con la palabra clave "verdad" en cualquier parte del mensaje, con peticiones de fact-checking, o cuando el tema es sensible a desinformación (salud, ciencia, política, noticias de última hora, cifras económicas). No es para preguntas triviales de cultura general ya asentada.
---

# Investigador Veraz

Skill para hacer búsquedas intensas de información **reciente**, contrastarla entre varias fuentes independientes y entregar una respuesta con **citas verificables** — nunca una afirmación suelta sin respaldo.

## Cuándo usarla

- El usuario escribe la palabra **"verdad"** en cualquier parte del mensaje.
- Pide comprobar si algo es cierto, está actualizado, o "suena a bulo".
- Pide datos recientes (cifras, fechas, eventos, declaraciones, estado actual de algo).
- Pide explícitamente fuentes, enlaces o referencias fiables.

## Principios no negociables

1. **Nunca una sola fuente.** Mínimo 3 fuentes independientes que coincidan antes de dar un dato por confirmado. Si solo hay 1-2, se dice explícitamente que el dato está poco contrastado.
2. **Prioriza fuentes primarias y fiables**: medios de referencia, organismos oficiales, papers revisados por pares, documentación oficial, comunicados directos de la entidad implicada. Evita blogs sin firma, foros, agregadores SEO y webs sin fecha de publicación.
3. **Prioriza lo reciente.** Si el tema puede haber cambiado, busca con filtros de fecha y descarta resultados obsoletos salvo que el usuario pida contexto histórico.
4. **Cita siempre con enlace verificable**, nunca inventes una fuente ni una cita textual larga (ver reglas de copyright del sistema: máx. 15 palabras por cita, una cita por fuente).
5. **Si las fuentes se contradicen**, dilo explícitamente y explica el desacuerdo en vez de elegir una versión y callar la otra.
6. **Si no se encuentra nada fiable**, se dice sin rodeos "no he encontrado fuentes fiables que lo confirmen" — nunca se rellena con una suposición.
7. Al final de la respuesta, incluye una sección **"Fuentes"** con enlace, nombre del medio/organismo y fecha de publicación de cada una.

## Flujo de trabajo

1. **Descompón la pregunta** en las afirmaciones concretas que hay que verificar (una pregunta puede contener varias afirmaciones).
2. **Busca de forma intensa**: lanza varias búsquedas con ángulos distintos (no repitas la misma query reformulada). Usa `mode: "extended"` cuando el tema sea difícil de encontrar, muy reciente o propenso a desinformación.
3. **Abre las páginas** (no te quedes solo con el snippet) para confirmar fecha, autoría y contexto real.
4. **Contrasta**: agrupa lo que dicen las fuentes y marca consensos y discrepancias.
5. **Redacta la respuesta**: directa, sin ambigüedad innecesaria, indicando el grado de certeza de cada afirmación.
6. **Lista las fuentes** usadas, con fecha.

Ver `references/checklist-fiabilidad.md` para el criterio detallado de qué cuenta como fuente fiable.

## Script de apoyo

`scripts/check_sources.py` valida mecánicamente una lista de fuentes antes de presentarlas: comprueba que cada una tenga URL con esquema http(s), que no esté duplicada, y que haya un mínimo de 3 fuentes independientes (dominios distintos) para poder marcar una afirmación como "confirmada". Úsalo como última comprobación antes de responder cuando el usuario haya escrito "verdad".

```bash
python3 scripts/check_sources.py sources.json
```

`sources.json` es una lista de objetos `{"url": "...", "title": "...", "date": "YYYY-MM-DD"}`.

## Tests

En `tests/` hay casos que verifican el comportamiento esperado de esta skill (formato de salida, mínimo de fuentes, manejo de contradicciones). Ejecutar con:

```bash
python3 -m pytest tests/ -v
```
