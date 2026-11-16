from typing import Any


class Empty(Exception):
    """Error attempting to access an element from an empty container.
    """
    pass

class DoublyLinkedQueue():  # TODO: fix this... DoublyLinkedQueue is-a DoublyLinkedList
    """FIFO Queue implementation using a doubly linked list w/tail pointer as underlying storage
    by inheriting from DoublyLinkedList.
    """
    def __init__(self) -> None:
        pass # TODO: finish this

    def __str__(self) -> str:
        return "" # TODO: finish this
    
    def enqueue(self, e: Any) -> None:
        pass # TODO: finish this

    def peek(self) -> Any:
        return None # TODO: fix this
    
    def dequeue(self) -> Any:
        return None # TODO: fix this
    
    def remove_divisible_by(self, p: int) -> None:
        pass # TODO: finish this