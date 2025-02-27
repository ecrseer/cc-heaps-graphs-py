class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is not None:
            self.head.prev = new_node
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

    def obter_index(self, value):
        current = self.head
        index = 0
        while current:
            if current.data == value:
                return index
            current = current.next
            index += 1
        return -1

    def inverter(self):
        current = self.head
        new_head = None
        while current:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            new_head = current
            current = current.prev
        if new_head:
            self.head = new_head





def demonstra_lista(dll):
    print("----")
    print("Percorrendo  ")
    dll.traverse_forward()

    print(f"""
     Index 30 {dll.obter_index(30)}
        Index 4  {dll.obter_index(4)}
    """)

    dll.inverter()
    dll.traverse_forward()

def exercicio33():
    lista_um = DoublyLinkedList()

    lista_um.insert_at_beginning(20)
    lista_um.insert_at_beginning(30)
    lista_um.insert_at_end(7)
    lista_um.insert_at_end(40)
    demonstra_lista(lista_um)

    lista_dois = DoublyLinkedList()
    lista_dois.insert_at_beginning(1)
    lista_dois.insert_at_beginning(2)
    lista_dois.insert_at_end(3)
    lista_dois.insert_at_end(4)
    demonstra_lista(lista_dois)

    lista_tres = DoublyLinkedList()
    lista_tres.insert_at_beginning(1)
    lista_tres.insert_at_beginning(2)
    lista_tres.insert_at_end(3)
    lista_tres.insert_at_end(4)
    lista_tres.insert_at_end(5)
    demonstra_lista(lista_tres)


if __name__ == "__main__":
    exercicio33()