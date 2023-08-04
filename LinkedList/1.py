class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = new_node

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=' ')
            current_node = current_node.next

# Test Example 1
linked_list1 = LinkedList()
linked_list1.append(1)
linked_list1.append(2)
linked_list1.display()
# Output: 1 2

# Test Example 2
linked_list2 = LinkedList()
linked_list2.append(49)
linked_list2.append(10)
linked_list2.append(30)
linked_list2.display()
# Output: 49 10 30
