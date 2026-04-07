"""Pruebas simples para ejecutar desde Spyder."""

from ejercicios import Queue, Stack


def probar_stack() -> None:
    s = Stack()
    assert s.is_empty() is True
    s.push(4)
    s.push(9)
    s.push(2)
    assert s.size() == 3
    assert s.peek() == 2
    assert s.pop() == 2
    assert s.peek() == 9
    assert s.size() == 2


def probar_queue() -> None:
    q = Queue()
    assert q.is_empty() is True
    q.enqueue("A")
    q.enqueue("B")
    q.enqueue("C")
    assert q.size() == 3
    assert q.peek() == "A"
    assert q.dequeue() == "A"
    assert q.peek() == "B"
    assert q.size() == 2


def run_tests() -> None:
    probar_stack()
    probar_queue()
    print("B03 OK")


if __name__ == "__main__":
    run_tests()
