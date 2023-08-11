# delete note from doubly linkedList 
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def deleteNode(self, x):
        if x <= 0:
            return
        
        current = self.head
        position = 1

        while current is not None and position < x:
            current = current.next
            position += 1
        
        if current is None:
            return
        
        if current.prev:
            current.prev.next = current.next
        else:
            self.head = current.next
        
        if current.next:
            current.next.prev = current.prev
        
        del current

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

# Example usage
ll = LinkedList()

# Input values
values = [1, 3, 4]
for value in values:
    ll.insert(value)

print("Original Linked List:")
ll.display()

pos = 3
ll.deleteNode(pos)
print(f"Linked List after deleting node at position {pos}:")
ll.display()
