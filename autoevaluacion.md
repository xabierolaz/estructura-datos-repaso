# Autoevaluacion Rapida

Usa esta hoja para ubicar rapido en que bloques estas flojo antes de abrir ningun cuaderno.

## Como usarla

1. Responde por tu cuenta en papel, en un txt o donde te resulte comodo.
2. No mires las respuestas hasta haber terminado todos los bloques.
3. Marca cada bloque como:
   - `limpio`
   - `con dudas`
   - `no sale`
4. Regla practica:
   - `0-1` fallos en un bloque -> puedes pasar pronto a `entrega_spyder.py`
   - `2` o mas fallos en un bloque -> abre el cuaderno de ese bloque

Flujo oficial:

1. `autoevaluacion.md`
2. `B01...B06.ipynb` segun el bloque flojo
3. `entrega_spyder.py`

---

## B01 - Fundamentos de Python

1. En `first, *middle, last = [10, 20, 30, 40, 50]`, que valores toman `first`, `middle` y `last`?
2. Si quieres escribir al final de un fichero sin borrar lo anterior, que modo usas entre `r`, `w` y `a`?
3. Si una funcion hace `print(x + 1)` pero no usa `return`, que valor devuelve realmente?
4. Que produce `list(enumerate(["a", "b", "c"]))`?

Si este bloque no sale limpio, abre [B01_fundamentos_python.ipynb](B01_fundamentos_python.ipynb).

## B02 - Clases y objetos

1. En OOP, que diferencia hay entre clase y objeto?
2. En `def depositar(self, cantidad):`, que representa `self`?
3. Si una clase usa `__saldo`, que idea de diseno esta marcando?
4. Si `x` y `y` son dos objetos distintos de la misma clase y llamas a un metodo que cambia el estado de `x`, cambia tambien el de `y`?

Si este bloque no sale limpio, abre [B02_clases_y_objetos.ipynb](B02_clases_y_objetos.ipynb).

## B03 - ADT, stacks y queues

1. Que define un ADT y que no fija todavia?
2. En una stack vacia haces `push(4)`, `push(9)`, `x = pop()`, `y = peek()`. Que valen `x` e `y`?
3. En una queue vacia haces `enqueue("A")`, `enqueue("B")`, `enqueue("C")`, `x = dequeue()`. Que valor sale en `x`?
4. Para modelar el boton de volver atras del navegador, pensarias antes en stack o en queue?

Si este bloque no sale limpio, abre [B03_stacks_y_queues.ipynb](B03_stacks_y_queues.ipynb).

## B04 - Deque y priority queue

1. Que hace que una `deque` sea mas general que una queue normal?
2. Si empiezas con una `deque` vacia y haces `append("b")`, `appendleft("a")`, `pop()`, que elemento queda dentro?
3. En una priority queue, que deberia salir antes: el mas antiguo o el de mayor prioridad?
4. Si usas insercion ordenada para una priority queue, en que operacion estas pagando el coste fuerte: al insertar o al extraer?

Si este bloque no sale limpio, abre [B04_deque_priority_queue.ipynb](B04_deque_priority_queue.ipynb).

## B05 - Buffers circulares

1. Que diferencia conceptual importante hay entre una queue y un buffer?
2. Si un buffer circular de capacidad `3` sobrescribe el dato mas antiguo y recibe `1, 2, 3, 4`, que queda dentro?
3. Si `capacidad = 5` e `indice = 4`, cuanto vale `(indice + 1) % capacidad`?
4. Di una politica posible cuando un buffer se llena aparte de sobrescribir el dato mas antiguo.

Si este bloque no sale limpio, abre [B05_buffers_circulares.ipynb](B05_buffers_circulares.ipynb).

## B06 - Linked lists

1. Que guarda un nodo de una singly linked list, como minimo?
2. Si `head` apunta a `9 -> 4 -> 7 -> None` y haces dos veces `current = current.next`, a que dato llegas?
3. Si la lista es `4 -> 7 -> None` y haces `head = Node(2, head)`, que cadena queda accesible desde `head`?
4. Para implementar `remove_tail()`, por que no basta con llegar al ultimo nodo?

Si este bloque no sale limpio, abre [B06_linked_lists.ipynb](B06_linked_lists.ipynb).

---

## Respuestas

### B01

1. `first = 10`, `middle = [20, 30, 40]`, `last = 50`
2. `a`
3. `None`
4. `[(0, "a"), (1, "b"), (2, "c")]`

### B02

1. La clase es la plantilla; el objeto es la instancia concreta
2. El objeto concreto sobre el que se ejecuta el metodo
3. Que el dato es interno y su acceso/modificacion debe controlarse desde la clase
4. No, solo cambia `x`

### B03

1. Define comportamiento y operaciones; no fija la implementacion concreta
2. `x = 9`, `y = 4`
3. `"A"`
4. `stack`

### B04

1. Permite insertar y extraer por ambos extremos
2. Queda `"a"`
3. El de mayor prioridad
4. Al insertar

### B05

1. La queue es un ADT; el buffer es un caso de uso con capacidad y flujo de datos
2. `2, 3, 4`
3. `0`
4. Por ejemplo: descartar el nuevo o bloquear hasta que haya sitio

### B06

1. El dato y la referencia al siguiente nodo
2. A `7`
3. `2 -> 4 -> 7 -> None`
4. Porque hay que hacer que el penultimo nodo apunte a `None`
