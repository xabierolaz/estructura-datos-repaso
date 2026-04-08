# Autoevaluacion Rapida

Usa esta hoja para ubicar rapido en que bloques estas flojo antes de abrir ningun cuaderno.

Tiempo objetivo: `10` minutos.
Diseno: `18` preguntas en total, `3` por tema.
Formato: `1` pregunta tipo test por tema y `2` abiertas por tema.

## Como usarla

1. Responde por tu cuenta en papel, en un txt o donde te resulte comodo.
2. No mires las respuestas hasta haber terminado todos los bloques.
3. No te pares demasiado: si una pregunta no sale en unos `30-35` segundos, cuentala como fallo.
4. Corrige al final y marca cada bloque asi:
   - `3/3`: listo para pasar a `entrega_spyder.py`
   - `2/3`: repaso breve si has dudado; si has ido muy limpio puedes pasar
   - `0-1/3`: cuaderno obligatorio
5. En las preguntas tipo test, marca solo la letra. Estan puestas en puntos donde la intuicion suele fallar.

Flujo oficial:

1. `autoevaluacion.md`
2. `B01...B06.ipynb` segun el bloque flojo
3. `entrega_spyder.py`

---

## B01 - Fundamentos de Python

1. Tipo test. Si quieres escribir al final de un fichero sin borrar lo anterior, que modo es el correcto?
   - A. `r`
   - B. `w`
   - C. `a`
   - D. `r+`
2. Si una funcion hace `print(x + 1)` pero no usa `return`, que valor devuelve realmente?
3. Que produce `list(enumerate(["a", "b", "c"]))`?

Si este bloque no sale limpio, abre [B01_fundamentos_python.ipynb](B01_fundamentos_python.ipynb).

## B02 - Clases y objetos

1. En OOP, que diferencia hay entre clase y objeto?
2. Tipo test. En `def depositar(self, cantidad):`, que representa `self`?
   - A. La clase completa
   - B. El objeto concreto sobre el que se ejecuta el metodo
   - C. El primer argumento que pase el usuario manualmente
   - D. El ultimo objeto creado de esa clase
3. Si una clase usa `__saldo`, que idea de diseno esta marcando?

Si este bloque no sale limpio, abre [B02_clases_y_objetos.ipynb](B02_clases_y_objetos.ipynb).

## B03 - ADT, stacks y queues

1. Tipo test. Que describe un ADT?
   - A. Solo el codigo concreto de una implementacion
   - B. El comportamiento y las operaciones, no la representacion concreta
   - C. Solo la estructura en memoria
   - D. Solo la complejidad temporal
2. En una stack vacia haces `push(4)`, `push(9)`, `x = pop()`, `y = peek()`. Que valen `x` e `y`?
3. En una queue vacia haces `enqueue("A")`, `enqueue("B")`, `enqueue("C")`, `x = dequeue()`. Que valor sale en `x`?

Si este bloque no sale limpio, abre [B03_stacks_y_queues.ipynb](B03_stacks_y_queues.ipynb).

## B04 - Deque y priority queue

1. Que hace que una `deque` sea mas general que una queue normal?
2. Si empiezas con una `deque` vacia y haces `append("b")`, `appendleft("a")`, `pop()`, que elemento queda dentro?
3. Tipo test. Si usas insercion ordenada para una priority queue, donde pagas el coste fuerte?
   - A. Al insertar
   - B. Al extraer
   - C. Solo al hacer `peek`
   - D. Nunca, porque queda todo O(1)

Si este bloque no sale limpio, abre [B04_deque_priority_queue.ipynb](B04_deque_priority_queue.ipynb).

## B05 - Buffers circulares

1. Tipo test. Que diferencia conceptual importante hay entre una queue y un buffer?
   - A. Ninguna; son exactamente lo mismo
   - B. La queue es un ADT y el buffer es un caso de uso con capacidad y flujo de datos
   - C. El buffer siempre ordena por prioridad y la queue no
   - D. La queue tiene capacidad fija y el buffer no
2. Si un buffer circular de capacidad `3` sobrescribe el dato mas antiguo y recibe `1, 2, 3, 4`, que queda dentro?
3. Si `capacidad = 5` e `indice = 4`, cuanto vale `(indice + 1) % capacidad`?

Si este bloque no sale limpio, abre [B05_buffers_circulares.ipynb](B05_buffers_circulares.ipynb).

## B06 - Linked lists

1. Si `head` apunta a `9 -> 4 -> 7 -> None` y haces dos veces `current = current.next`, a que dato llegas?
2. Si la lista es `4 -> 7 -> None` y haces `head = Node(2, head)`, que cadena queda accesible desde `head`?
3. Tipo test. Para implementar `remove_tail()` en una singly linked list, por que no basta con llegar al ultimo nodo?
   - A. Porque tambien necesitas modificar el penultimo para que apunte a `None`
   - B. Porque el ultimo nodo nunca se puede borrar
   - C. Porque `head` siempre apunta al ultimo nodo
   - D. Porque hace falta ordenar la lista antes

Si este bloque no sale limpio, abre [B06_linked_lists.ipynb](B06_linked_lists.ipynb).

---

## Respuestas

### B01

1. `C` -> `a`
2. `None`
3. `[(0, "a"), (1, "b"), (2, "c")]`

### B02

1. La clase es la plantilla; el objeto es la instancia concreta
2. `B` -> el objeto concreto sobre el que se ejecuta el metodo
3. Que el dato es interno y su acceso/modificacion debe controlarse desde la clase

### B03

1. `B` -> define comportamiento y operaciones; no fija la implementacion concreta
2. `x = 9`, `y = 4`
3. `"A"`

### B04

1. Permite insertar y extraer por ambos extremos
2. Queda `"a"`
3. `A` -> al insertar

### B05

1. `B` -> la queue es un ADT; el buffer es un caso de uso con capacidad y flujo de datos
2. `2, 3, 4`
3. `0`

### B06

1. A `7`
2. `2 -> 4 -> 7 -> None`
3. `A` -> porque hay que hacer que el penultimo nodo apunte a `None`
