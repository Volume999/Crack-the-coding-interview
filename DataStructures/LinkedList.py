class Node:
    def __init__self(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node(None)
    
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
    
    def appendleft(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def append(self, new_data):
        tail = self.head
        new_node = Node(new_data)
        while tail.next:
            tail = tail.next
        tail.next = new_node

    def popleft(self):
        temp = self.head
        self.head = self.head.next
        temp.next = None
    
    def pop(self):
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None

    def delete(self, data):
        temp = self.head
        while temp.next:
            if temp.next.data == data:
                temp.next = temp.next.next
                break
            temp = temp.next