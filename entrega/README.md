# Entrega unica para Spyder

Esta carpeta sustituye la practica fragmentada por bloques.

Objetivo:

- que el alumnado trabaje en un unico archivo
- que la correccion docente se haga sobre un unico archivo por alumno
- que el feedback siga separado por bloques del temario

Archivos:

- `entrega_spyder.py`: unico archivo que el alumnado debe editar
- `prueba.py`: comprobador automatico local y base del autograding
- `datos/numbers.txt`: dato auxiliar para B01

## Que es `prueba.py`

`prueba.py` no es la entrega.

`prueba.py` sirve para:

- importar tu codigo desde `entrega_spyder.py`
- ejecutar comprobaciones con `assert`
- decirte en que bloque estas fallando
- dar feedback automatico en GitHub Actions cuando haces push

En claro:

- tu archivo de trabajo es `entrega_spyder.py`
- `prueba.py` es el corrector

## Flujo recomendado

1. Estudia el bloque en `resumen/` y en `cuadernos/`.
2. Abre `entrega/entrega_spyder.py` en Spyder, `github.dev` o VS Code.
3. Ve a la seccion del bloque usando `Ctrl+F` y busca `===== B01 =====`, `===== B02 =====`, etc.
4. Completa solo la parte correspondiente.
5. Ejecuta `python entrega/prueba.py --block B01` o el bloque que toque.
6. Cuando cierres varios bloques, ejecuta `python entrega/prueba.py`.
7. Haz push y revisa `Actions`.

## Bloques dentro del archivo

- `B01`: funciones basicas de Python
- `B02`: clases, objetos y encapsulacion
- `B03`: `Stack` y `Queue`
- `B04`: `deque` y `PriorityQueueOrdenada`
- `B05`: `BufferCircular`
- `B06`: `Node` y `LinkedList`
