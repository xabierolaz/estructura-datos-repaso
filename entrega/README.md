# Entrega unica para Spyder

Esta carpeta contiene la unica entrega manual del alumnado.

Archivos:

- `entrega_spyder.py`: unico archivo que el alumnado debe editar y entregar
- `prueba.py`: corrector local opcional
- `datos/numbers.txt`: dato auxiliar para B01

## Que es `prueba.py`

`prueba.py` no es la entrega.

`prueba.py` sirve para:

- importar tu codigo desde `entrega_spyder.py`
- ejecutar comprobaciones con `assert`
- decirte en que bloque estas fallando

En claro:

- tu archivo de trabajo es `entrega_spyder.py`
- `prueba.py` es el corrector

## Flujo recomendado

1. Haz primero `autotest.ipynb`.
2. Estudia en `resumen/` solo los bloques flojos.
3. Abre `entrega/entrega_spyder.py` en Spyder, `github.dev` o VS Code.
4. Ve a la seccion del bloque usando `Ctrl+F` y busca `===== B01 =====`, `===== B02 =====`, etc.
5. Completa solo la parte correspondiente.
6. Si quieres autocontrol local, ejecuta `python entrega/prueba.py --block B01` o el bloque que toque.
7. Cuando cierres varios bloques, puedes ejecutar `python entrega/prueba.py`.
8. Entrega `entrega_spyder.py` para correccion manual del docente.

## Bloques dentro del archivo

- `B01`: funciones basicas de Python
- `B02`: clases, objetos y encapsulacion
- `B03`: `Stack` y `Queue`
- `B04`: `deque` y `PriorityQueueOrdenada`
- `B05`: `BufferCircular`
- `B06`: `Node` y `LinkedList`
