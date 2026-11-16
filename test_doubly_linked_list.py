# NOTE: do not modify the contents of this file
import pytest
from doubly_linked_list import DoublyLinkedList, _Node, Empty


# NOTE: order is actual/received student value, expected/solution
def test_str():
    # note that tail string is on its own new line
    # empty list
    dll = DoublyLinkedList()
    assert str(dll) == "head->None\ntail->None"

    # single node list
    dll = DoublyLinkedList()
    node = _Node(10)
    dll._head = node
    dll._tail = node
    assert str(dll) == "head->10<->None\ntail->10"

    # multi-node list
    dll = DoublyLinkedList()
    n1 = _Node(10)
    n2 = _Node(20)
    n3 = _Node(30)

    n1._next = n2
    n2._prev = n1
    n2._next = n3
    n3._prev = n2

    dll._head = n1
    dll._tail = n3
    assert str(dll) == "head->10<->20<->30<->None\ntail->30"

def test_len():
    # empty list
    dll = DoublyLinkedList()
    assert len(dll) == 0

    # single node list
    dll = DoublyLinkedList()
    dll._head = _Node(10)
    dll._tail = dll._head
    assert len(dll) == 1

    # multi-node list
    dll = DoublyLinkedList()
    n1 = _Node(10)
    n2 = _Node(20)
    n3 = _Node(30)

    n1._next = n2
    n2._prev = n1
    n2._next = n3
    n3._prev = n2

    dll._head = n1
    dll._tail = n3
    assert len(dll) == 3

def test_is_empty():
    # empty list
    dll = DoublyLinkedList()
    assert dll.is_empty() is True

    # non-empty list
    dll = DoublyLinkedList()
    dll._head = _Node(10)
    dll._tail = dll._head
    assert dll.is_empty() is False
    
def test_clear():
    # multi-node list
    dll = DoublyLinkedList()
    n1 = _Node(10)
    n2 = _Node(20)
    n3 = _Node(30)

    n1._next = n2
    n2._prev = n1
    n2._next = n3
    n3._prev = n2

    dll._head = n1
    dll._tail = n3

    dll.clear()
    assert dll._head is None
    assert dll._tail is None

def test_add_to_back():
    # empty list
    dll = DoublyLinkedList()
    dll.add_to_back(10)
    assert dll._head is not None
    assert dll._tail is not None
    assert dll._head is dll._tail
    assert dll._head._item == 10
    assert dll._head._prev is None
    assert dll._head._next is None

    # adding again
    dll.add_to_back(20)
    assert dll._head._item == 10
    assert dll._tail._item == 20

    assert dll._head._next is dll._tail
    assert dll._tail._prev is dll._head

    assert dll._head._prev is None
    assert dll._tail._next is None

    # adding again
    dll.add_to_back(30)
    assert dll._head._item == 10
    assert dll._tail._item == 30

    second = dll._head._next
    third = dll._tail

    assert second is not None
    assert second._item == 20

    # check forward links
    assert dll._head._next is second
    assert second._next is third
    assert third._next is None

    # check backward links
    assert second._prev is dll._head
    assert third._prev is second
    assert dll._head._prev is None

def test_delete_at_front():
    # empty list
    dll = DoublyLinkedList()
    with pytest.raises(Empty):
        dll.delete_at_front()

    # single node list
    node = _Node(10)
    dll._head = node
    dll._tail = node

    val = dll.delete_at_front()
    assert val == 10
    assert dll._head is None
    assert dll._tail is None

    # multi-node list
    dll = DoublyLinkedList()
    n1 = _Node(10)
    n2 = _Node(20)
    n3 = _Node(30)

    n1._next = n2
    n2._prev = n1
    n2._next = n3
    n3._prev = n2

    dll._head = n1
    dll._tail = n3

    val = dll.delete_at_front()
    assert val == 10
    assert dll._head is n2
    assert dll._head._item == 20
    assert dll._head._prev is None
    assert dll._head._next is n3

    assert dll._tail is n3
    assert dll._tail._prev is n2
    assert dll._tail._next is None

def test_delete():
    # empty list: should do nothing
    dll = DoublyLinkedList()
    dll.delete(99)
    assert dll._head is None
    assert dll._tail is None

    # delete first node from multi-node list
    dll = DoublyLinkedList()
    n1 = _Node(10)
    n2 = _Node(20)
    n3 = _Node(30)

    n1._next = n2
    n2._prev = n1
    n2._next = n3
    n3._prev = n2

    dll._head = n1
    dll._tail = n3

    dll.delete(10)

    assert dll._head is n2
    assert dll._tail is n3
    assert dll._head._item == 20
    assert dll._head._prev is None
    assert dll._head._next is n3
    assert dll._tail._prev is n2
    assert dll._tail._next is None

    # delete middle node from multi-node list
    dll = DoublyLinkedList()
    n1 = _Node(10)
    n2 = _Node(20)
    n3 = _Node(30)
    n4 = _Node(40)

    n1._next = n2
    n2._prev = n1
    n2._next = n3
    n3._prev = n2
    n3._next = n4
    n4._prev = n3

    dll._head = n1
    dll._tail = n4

    dll.delete(30)

    assert dll._head is n1
    assert dll._tail is n4
    assert n1._next is n2
    assert n2._prev is n1
    assert n2._next is n4
    assert n4._prev is n2
    assert n4._next is None

    # delete last node in multi-node list
    dll = DoublyLinkedList()
    n1 = _Node(10)
    n2 = _Node(20)
    n3 = _Node(30)

    n1._next = n2
    n2._prev = n1
    n2._next = n3
    n3._prev = n2

    dll._head = n1
    dll._tail = n3

    dll.delete(30)

    assert dll._head is n1
    assert dll._tail is n2
    assert dll._head._prev is None
    assert dll._head._next is n2
    assert dll._tail._prev is n1
    assert dll._tail._next is None

    # delete only node in single node list
    dll = DoublyLinkedList()
    node = _Node(10)
    dll._head = node
    dll._tail = node

    dll.delete(10)

    assert dll._head is None
    assert dll._tail is None

    # item not found: list should not change
    dll = DoublyLinkedList()
    n1 = _Node(10)
    n2 = _Node(20)
    n3 = _Node(30)

    n1._next = n2
    n2._prev = n1
    n2._next = n3
    n3._prev = n2

    dll._head = n1
    dll._tail = n3

    dll.delete(99)

    assert dll._head is n1
    assert dll._tail is n3
    assert dll._head._item == 10
    assert dll._head._next is n2
    assert n2._prev is n1
    assert n2._next is n3
    assert dll._tail._prev is n2
    assert dll._tail._next is None

# BONUS
def test_add_to_front():
    # empty list
    dll = DoublyLinkedList()
    dll.add_to_front(10)
    assert dll._head is not None
    assert dll._tail is not None
    assert dll._head._item == 10
    assert dll._tail._item == 10
    assert dll._head is dll._tail
    assert dll._head._prev is None
    assert dll._head._next is None

    # adding again
    dll.add_to_front(20)
    assert dll._head._item == 20
    assert dll._tail._item == 10
    assert dll._head._prev is None
    assert dll._head._next is not None
    assert dll._head._next._item == 10
    assert dll._head._next._prev is dll._head
    assert dll._tail._prev is dll._head
    assert dll._tail._next is None

    # adding again
    dll.add_to_front(30)
    assert dll._head._item == 30
    assert dll._tail._item == 10
    assert dll._head._prev is None
    assert dll._head._next._item == 20
    assert dll._head._next._prev is dll._head
    assert dll._head._next._next._item == 10
    assert dll._head._next._next._prev._item == 20
    assert dll._tail._prev._item == 20
    assert dll._tail._next is None

# BONUS
def test_delete_at_back():
    # empty list
    dll = DoublyLinkedList()
    with pytest.raises(Empty):
        dll.delete_at_back()

    # delete only node in single-node list
    node = _Node(10)
    dll._head = node
    dll._tail = node

    val = dll.delete_at_back()
    assert val == 10
    assert dll._head is None
    assert dll._tail is None

    # multi-node list
    dll = DoublyLinkedList()
    n1 = _Node(10)
    n2 = _Node(20)
    n3 = _Node(30)

    n1._next = n2
    n2._prev = n1
    n2._next = n3
    n3._prev = n2

    dll._head = n1
    dll._tail = n3

    val = dll.delete_at_back()
    assert val == 30

    assert dll._tail is n2
    assert dll._tail._item == 20
    assert dll._tail._next is None
    assert dll._tail._prev is n1

    assert dll._head is n1
    assert dll._head._item == 10
    assert dll._head._prev is None
    assert dll._head._next is n2

    # deleting again
    val = dll.delete_at_back()
    assert val == 20

    assert dll._head is dll._tail
    assert dll._head is n1
    assert dll._head._prev is None
    assert dll._head._next is None