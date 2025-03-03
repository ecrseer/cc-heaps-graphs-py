import time


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def remove(self, key):
        current = self.head
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
        if current is None:
            return
        if prev is None:
            self.head = current.next
        else:
            prev.next = current.next

    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("\n")



def demonstracao_tempo(a,b,c,d):
    inicio = time.time()
    linked_list = LinkedList()

    linked_list.insert_at_beginning(a)
    linked_list.insert_at_beginning(b)
    linked_list.insert_at_end(c)
    linked_list.insert_at_end(d)

    print("Lista encadeads:")
    linked_list.traverse()

    linked_list.remove(b)
    print(f"Depois de remoção do nro {b}:")
    linked_list.traverse()

    linked_list.remove(c)
    print(f"Depois de remoção do nro {c}:")
    linked_list.traverse()
    return time.time() - inicio

tempos = [
demonstracao_tempo(10,20,30,40),
demonstracao_tempo(32,45,67,89),
demonstracao_tempo(23,11,67,7) ]

media = sum(tempos) / len(tempos)
print(f"Tempo médio de execução: {media:.6f} milissegundos")