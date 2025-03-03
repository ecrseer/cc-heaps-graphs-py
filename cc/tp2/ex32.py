import time


class DNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = DNode(data)
        if self.head is not None:
            self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = DNode(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current

    def remove(self, key):
        current = self.head
        while current and current.data != key:
            current = current.next
        if current is None:
            return
        if current.prev:
            current.prev.next = current.next
        if current.next:
            current.next.prev = current.prev
        if current == self.head:
            self.head = current.next

    def traverse_forward(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def traverse_backward(self):
        current = self.head
        if not current:
            print("None")
            return
        while current.next:
            current = current.next
        while current:
            print(current.data, end=" -> ")
            current = current.prev
        print("None")



def demonstracao_tempo(a,b,c,d):
    inicio = time.time()
    dll = DoublyLinkedList()

    dll.insert_at_beginning(a)
    dll.insert_at_beginning(b)
    dll.insert_at_end(c)
    dll.insert_at_end(d)

    print("Percorrendo da frente para trás:")
    dll.traverse_forward()

    print("Percorrendo de trás para frente:")
    dll.traverse_backward()

    dll.remove(20)
    print("Lista após remoção de 20 (frente para trás):")
    dll.traverse_forward()
    return time.time() - inicio

tempos = [
demonstracao_tempo(10,20,30,40),
demonstracao_tempo(32,45,67,89),
demonstracao_tempo(23,11,67,7) ]

media = sum(tempos) / len(tempos)
print(f"Tempo médio de execução: {media:.6f} milissegundos")