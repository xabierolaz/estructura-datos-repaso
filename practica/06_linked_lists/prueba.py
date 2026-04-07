"""Pruebas simples para ejecutar desde Spyder."""

from ejercicios import LinkedList


def run_tests() -> None:
    ll = LinkedList()
    assert ll.size() == 0
    assert ll.remove_head() is None
    assert ll.remove_tail() is None

    ll.add_head(4)
    ll.add_head(2)
    ll.add_tail(7)
    assert ll.to_list() == [2, 4, 7]
    assert ll.size() == 3
    assert ll.contains(4) is True
    assert ll.contains(9) is False
    assert ll.remove_head() == 2
    assert ll.to_list() == [4, 7]
    assert ll.remove_tail() == 7
    assert ll.to_list() == [4]
    assert ll.remove_tail() == 4
    assert ll.to_list() == []
    print("B06 OK")


if __name__ == "__main__":
    run_tests()
