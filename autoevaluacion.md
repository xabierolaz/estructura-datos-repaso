# Autoevaluacion Dura

Usa esta hoja para repasar preguntas breves por bloques antes de tocar la entrega.

Tiempo objetivo: `15-20` minutos.
Diseno: `30` preguntas en total, `5` por tema.
Formato: `2` preguntas tipo test y `3` abiertas por tema.

## Como usarla

1. Responde por tu cuenta en papel, en un txt o donde te resulte comodo.
2. No mires las respuestas hasta haber terminado todos los bloques.
3. Si una pregunta no sale en unos `30-40` segundos, anota que la has dudado.
4. Compara tus respuestas con las del final.
5. Si quieres revisar un tema, abre su cuaderno correspondiente.

Flujo oficial:

1. `autoevaluacion.md`
2. `B01...B06.ipynb` en cualquier bloque que quieras revisar
3. `entrega_spyder.py`

---

## B01 - Fundamentos de Python

1. Si una funcion hace `print(x + 1)` pero no usa `return`, que valor devuelve realmente?
2. Que produce `list(enumerate(["a", "b", "c"]))`?
3. En `first, *middle, last = [10, 20, 30, 40]`, que valores toman `first`, `middle` y `last`?
4. Tipo test. Si quieres anadir texto al final de un fichero sin borrar lo anterior, que modo es el correcto?
   - A. `r`
   - B. `w`
   - C. `a`
   - D. `r+`
5. Tipo test. Que significa `if __name__ == "__main__":`?
   - A. Que el archivo ha sido importado desde otro modulo
   - B. Que ese bloque se ejecuta cuando el archivo se lanza directamente
   - C. Que Python va a comprobar automaticamente los tipos
   - D. Que la funcion principal debe llamarse exactamente `main`

Para revisar este bloque, abre [B01_fundamentos_python.ipynb](B01_fundamentos_python.ipynb).

## B02 - Clases y objetos

1. En OOP, que diferencia hay entre clase y objeto?
2. Da un ejemplo de atributo y de metodo dentro de una clase `Estudiante`.
3. Si una clase usa `__saldo`, que idea de diseno esta marcando y que invariante basico intentaria proteger?
4. Tipo test. En `def depositar(self, cantidad):`, que representa `self`?
   - A. La clase completa
   - B. El objeto concreto sobre el que se ejecuta el metodo
   - C. El primer argumento que pase el usuario manualmente
   - D. El ultimo objeto creado de esa clase
5. Tipo test. Que hace `__init__`?
   - A. Se llama automaticamente al crear el objeto y fija su estado inicial
   - B. Solo sirve para imprimir el objeto
   - C. Hace privada la clase
   - D. Obliga a usar herencia

Para revisar este bloque, abre [B02_clases_y_objetos.ipynb](B02_clases_y_objetos.ipynb).

## B03 - ADT, stacks y queues

1. Explica en una frase la diferencia entre ADT e implementacion.
2. Que diferencia conceptual hay entre un `list` y un `map` como ADT generales?
3. En una stack vacia haces `push(4)`, `push(9)`, `x = pop()`, `y = peek()`. Que valen `x` e `y`?
4. Tipo test. Que describe un ADT?
   - A. Solo el codigo concreto de una implementacion
   - B. El comportamiento y las operaciones, no la representacion concreta
   - C. Solo la estructura en memoria
   - D. Solo la complejidad temporal
5. Tipo test. Si insertas `A, B, C` y luego extraes hasta vaciar, que salida corresponde a una queue?
   - A. `C, B, A`
   - B. `A, B, C`
   - C. `B, C, A`
   - D. Depende siempre de la implementacion interna

Para revisar este bloque, abre [B03_stacks_y_queues.ipynb](B03_stacks_y_queues.ipynb).

## B04 - Deque y priority queue

1. Que hace que una `deque` sea mas general que una queue normal?
2. Si empiezas con una `deque` vacia y haces `append("b")`, `appendleft("a")`, `append("c")`, `popleft()`, que queda dentro?
3. Explica en una frase la diferencia entre una priority queue y una queue normal.
4. Tipo test. Si usas insercion ordenada para una priority queue, donde pagas el coste fuerte?
   - A. Al insertar
   - B. Al extraer
   - C. Solo al hacer `peek`
   - D. Nunca, porque queda todo O(1)
5. Tipo test. Si insertas sin ordenar y buscas el maximo al extraer, que idea teorica es correcta?
   - A. Insertar es mas barato y extraer es mas caro
   - B. Insertar y extraer pasan a ser O(1) a la vez
   - C. Eso convierte la estructura en una deque
   - D. La prioridad deja de importar

Para revisar este bloque, abre [B04_deque_priority_queue.ipynb](B04_deque_priority_queue.ipynb).

## B05 - Buffers circulares

1. Que diferencia conceptual importante hay entre una queue y un buffer?
2. Si `capacidad = 5` e `indice = 4`, cuanto vale `(indice + 1) % capacidad`?
3. Nombra las tres politicas teoricas que se estudian cuando el buffer esta lleno.
4. Tipo test. En el tema de buffers, por que aparece la idea de productor y consumidor?
   - A. Porque ambos siempre escriben en el mismo extremo
   - B. Porque el buffer amortigua ritmos distintos entre quien produce y quien consume
   - C. Porque un buffer obliga a ordenar por prioridad
   - D. Porque productor y consumidor son dos nodos de una linked list
5. Tipo test. En un buffer circular de capacidad `3` con politica `overwrite`, si llegan `1, 2, 3, 4`, que queda dentro en orden FIFO?
   - A. `1, 2, 3`
   - B. `4, 3, 2`
   - C. `2, 3, 4`
   - D. Solo `4`

Para revisar este bloque, abre [B05_buffers_circulares.ipynb](B05_buffers_circulares.ipynb).

## B06 - Linked lists

1. Que guarda un `Node` y por que `head` es la puerta de entrada a toda la lista?
2. Si `head` apunta a `9 -> 4 -> 7 -> None` y haces dos veces `current = current.next`, a que dato llegas?
3. Que diferencia hay entre `get(index)` en una linked list y acceso por indice en una lista Python?
4. Tipo test. Para implementar `remove_tail()` en una singly linked list, por que no basta con llegar al ultimo nodo?
   - A. Porque tambien necesitas modificar el penultimo para que apunte a `None`
   - B. Porque el ultimo nodo nunca se puede borrar
   - C. Porque `head` siempre apunta al ultimo nodo
   - D. Porque hace falta ordenar la lista antes
5. Tipo test. Que mejora teorica aportan `__len__` y `__str__` en una linked list?
   - A. Permiten que la clase se use mas como una estructura Python legible
   - B. Hacen que `get(index)` pase a ser acceso directo
   - C. Evitan la necesidad de `head`
   - D. Sustituyen a `contains`

Para revisar este bloque, abre [B06_linked_lists.ipynb](B06_linked_lists.ipynb).

---

## Respuestas

### B01

1. `None`.
2. `[(0, "a"), (1, "b"), (2, "c")]`.
3. `first = 10`, `middle = [20, 30]`, `last = 40`.
4. `C` -> `a`, porque anade al final sin borrar el contenido anterior.
5. `B` -> significa que ese bloque solo corre cuando lanzas el archivo directamente; no convierte eso en una certificacion de tipos ni obliga a un nombre especial de funcion.

### B02

1. La clase es la plantilla; el objeto es la instancia concreta creada a partir de ella.
2. Ejemplo correcto: atributo `nota`, metodo `es_aprobado`.
3. Marca encapsulacion: el dato es interno y la clase controla su acceso. Invariante basico tipico: no permitir saldo negativo o cambios arbitrarios desde fuera.
4. `B` -> `self` representa el objeto concreto sobre el que actua el metodo.
5. `A` -> `__init__` se llama automaticamente al crear el objeto y fija su estado inicial.

### B03

1. El ADT define comportamiento y operaciones; la implementacion decide como representarlo por dentro.
2. `list` representa secuencias ordenadas; `map` asociaciones clave-valor.
3. `x = 9`, `y = 4`.
4. `B` -> el ADT no fija una representacion concreta.
5. `B` -> una queue es FIFO, asi que sale `A, B, C`.

### B04

1. Permite insertar y extraer por ambos extremos.
2. Queda `["b", "c"]`.
3. En una queue normal manda la antiguedad; en una priority queue manda el criterio de prioridad.
4. `A` -> con insercion ordenada pagas al insertar para extraer facil despues.
5. `A` -> si no ordenas al insertar, la extraccion del maximo pasa a ser la parte cara.

### B05

1. La queue es un ADT; el buffer es un caso de uso con almacenamiento temporal, capacidad y politica de llenado.
2. `0`.
3. `drop new data`, `overwrite the oldest`, `block insertion until a removal happens`.
4. `B` -> el buffer desacopla ritmos distintos entre quien produce datos y quien los consume.
5. `C` -> al sobrescribir el mas antiguo en capacidad `3`, quedan `2, 3, 4`.

### B06

1. Un `Node` guarda el dato y la referencia al siguiente. `head` permite llegar al resto saltando por `next`.
2. A `7`.
3. En una linked list no hay salto directo: `get(index)` obliga a recorrer desde `head` nodo a nodo.
4. `A` -> hay que rehacer el enlace del penultimo para cerrar la lista en `None`.
5. `A` -> mejoran la integracion con Python: `len(lista)` y una representacion legible al imprimir.
