# Metadata del repaso

Esta carpeta contiene solo la trazabilidad minima del sistema activo.

Archivos principales:

- `autotest_topics.json`: anclas del autotest diagnostico.
- `build_autotest.py`: genera `autotest.ipynb`.
- `validate_autotest.py`: valida la estructura minima del autotest.
- `taxonomy.json`: bloques teoricos y subhabilidades del repaso.
- `theory_source_map.json`: correspondencia entre cada bloque y su fuente teorica principal.

Reglas:

- `resumen/` sigue la misma taxonomia que `taxonomy.json`
- `autotest.ipynb` apunta a esos mismos bloques
- la teoria es la fuente primaria; practicas y examenes no organizan el repaso
