# Investigador-veraz
Investigación intensiva de información reciente con fuentes verificables y fiables. Úsala siempre que el usuario pida verificar datos, contrastar hechos, buscar "la verdad" sobre algo, comprobar si una noticia o afirmación es real, o pida explícitamente fuentes fiables/verificables.
Este proyecto contiene scripts/check_sources.py, un validador sin dependencias externas para comprobar la lista de fuentes antes de presentar una afirmación como confirmada.

Valida que:

•
el JSON raíz sea una lista;

•
cada fuente tenga url, title y date;

•
las URLs usen http o https;

•
las fechas usen el formato ISO YYYY-MM-DD;

•
no haya URLs repetidas, incluso si cambia la barra final;

•
existan al menos tres dominios independientes;

•
se marquen posibles contradicciones cuando se usa el campo opcional supports.

Requisitos

•
Python 3.10 o posterior.

•
pytest únicamente para ejecutar las pruebas.

El script de producción usa solo la biblioteca estándar de Python.

Formato de entrada

supports es opcional y debe ser booleano. Si algunas fuentes tienen true y otras false, el resultado será contradictory y aparecerá una advertencia. El script no interpreta el contenido de los artículos: solo valida los metadatos y la posición declarada por quien prepara la lista.

Uso

Desde la raíz del proyecto:

Bash


python3 scripts/check_sources.py sources.json

Códigos de salida:

•
0: tres o más dominios independientes y sin errores ni contradicciones.

•
1: entrada válida como JSON, pero no confirmable o con errores de validación.

•
2: archivo inexistente o JSON mal formado.

Puedes cambiar el mínimo de dominios para un caso concreto:

Bash


python3 scripts/check_sources.py sources.json --minimum 4



Tests

Instala pytest si hace falta y ejecuta:

Bash


python3 -m pytest tests/ -v



Limitaciones

La independencia se estima por nombre de host, eliminando solo el prefijo www.. El validador no puede determinar si dos medios pertenecen a la misma empresa, si un artículo es fiable o si una afirmación es verdadera; esas comprobaciones requieren investigación y criterio editorial.

