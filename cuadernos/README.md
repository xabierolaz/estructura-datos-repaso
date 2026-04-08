# Cuadernos activos por tema

Esta capa convierte cada bloque en una secuencia de estudio ejecutable y queda preparada para Google Colab como capa principal de estudio.

Objetivo:

- leer la idea minima del tema
- predecir antes de ejecutar
- correr ejemplos pequenos
- completar un mini ejercicio dentro del cuaderno
- cerrar el bloque pasando luego a `../practica/`

Flujo recomendado:

- abrir cada `.ipynb` en Google Colab desde GitHub
- si vienes desde GitHub Classroom, usar Colab para estudiar y volver luego a tu repo para resolver `practica/`
- ejecutar la celda inicial si quieres tener tambien `resumen/` y `practica/` dentro del runtime
- si solo quieres estudiar un cuaderno suelto, puedes abrirlo en Colab sin clonar nada

Repo canonico:

- GitHub: [xabierolaz/estructura-datos-repaso](https://github.com/xabierolaz/estructura-datos-repaso)
- rama: `main`
- carpeta del proyecto: raiz del repo
- despliegue docente: [CLASSROOM_SETUP.md](../CLASSROOM_SETUP.md)

Importante:

- los enlaces de Colab de abajo apuntan al repo canonico de estudio
- esa sesion de Colab no entrega nada automaticamente a GitHub Classroom
- la entrega real vive en `practica/**/ejercicios.py` dentro de tu repo individual

Reglas zero-trust:

- no ejecutes una celda de prediccion sin escribir antes tu respuesta
- no des por entendido un ejemplo solo porque "sale bien"
- usa `Restart & Run All` al final del bloque para evitar estado oculto
- si pasas el cuaderno pero no puedes resolver `ejercicios.py`, el tema no esta cerrado

Uso recomendado:

1. Lee una pasada corta del bloque en `../resumen/`.
2. Abre el cuaderno del tema en Google Colab con uno de los enlaces de abajo.
3. En Colab, ejecuta la celda inicial para clonar el repo si quieres usar tambien `resumen/` y `practica/`.
4. Completa todas las celdas `TODO`.
5. Haz `Restart & Run All`.
6. Vuelve a tu repo de GitHub Classroom.
7. Abre `github.dev` con `.` o trabaja en local.
8. Pasa a `../practica/` y resuelve `ejercicios.py`.
9. Haz commit y push para lanzar el autograding.
10. Si trabajas en local, ejecuta `prueba.py`.
11. Si algo falla, vuelve al punto exacto del cuaderno o del resumen.

Bloques:

- B01 - Fundamentos de Python: [local](01_fundamentos_python/cuaderno.ipynb) | [GitHub](https://github.com/xabierolaz/estructura-datos-repaso/blob/main/cuadernos/01_fundamentos_python/cuaderno.ipynb) | [Colab](https://colab.research.google.com/github/xabierolaz/estructura-datos-repaso/blob/main/cuadernos/01_fundamentos_python/cuaderno.ipynb)
- B02 - Clases y objetos: [local](02_clases_y_objetos/cuaderno.ipynb) | [GitHub](https://github.com/xabierolaz/estructura-datos-repaso/blob/main/cuadernos/02_clases_y_objetos/cuaderno.ipynb) | [Colab](https://colab.research.google.com/github/xabierolaz/estructura-datos-repaso/blob/main/cuadernos/02_clases_y_objetos/cuaderno.ipynb)
- B03 - ADT, stacks y queues: [local](03_stacks_y_queues/cuaderno.ipynb) | [GitHub](https://github.com/xabierolaz/estructura-datos-repaso/blob/main/cuadernos/03_stacks_y_queues/cuaderno.ipynb) | [Colab](https://colab.research.google.com/github/xabierolaz/estructura-datos-repaso/blob/main/cuadernos/03_stacks_y_queues/cuaderno.ipynb)
- B04 - Deque y priority queue: [local](04_deque_priority_queue/cuaderno.ipynb) | [GitHub](https://github.com/xabierolaz/estructura-datos-repaso/blob/main/cuadernos/04_deque_priority_queue/cuaderno.ipynb) | [Colab](https://colab.research.google.com/github/xabierolaz/estructura-datos-repaso/blob/main/cuadernos/04_deque_priority_queue/cuaderno.ipynb)
- B05 - Buffers circulares: [local](05_buffers_circulares/cuaderno.ipynb) | [GitHub](https://github.com/xabierolaz/estructura-datos-repaso/blob/main/cuadernos/05_buffers_circulares/cuaderno.ipynb) | [Colab](https://colab.research.google.com/github/xabierolaz/estructura-datos-repaso/blob/main/cuadernos/05_buffers_circulares/cuaderno.ipynb)
- B06 - Linked lists: [local](06_linked_lists/cuaderno.ipynb) | [GitHub](https://github.com/xabierolaz/estructura-datos-repaso/blob/main/cuadernos/06_linked_lists/cuaderno.ipynb) | [Colab](https://colab.research.google.com/github/xabierolaz/estructura-datos-repaso/blob/main/cuadernos/06_linked_lists/cuaderno.ipynb)
