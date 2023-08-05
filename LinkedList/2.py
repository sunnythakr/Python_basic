# Given a singly linked list. The task is to find the length of the
#  linked list, where length is defined as the number of nodes 
# in the linked list.
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

    def getCount(self, head_node):
        count = 0
        current_node = head_node
        while current_node:
            count += 1
            current_node = current_node.next
        return count

# Test Example 1
linked_list1 = LinkedList()
linked_list1.append(1)
linked_list1.append(2)
linked_list1.append(3)
linked_list1.append(4)
linked_list1.append(5)
print(linked_list1.getCount(linked_list1.head))  # Output: 5

# Test Example 2
linked_list2 = LinkedList()
linked_list2.append(2)
linked_list2.append(4)
linked_list2.append(6)
linked_list2.append(7)
linked_list2.append(5)
linked_list2.append(1)
linked_list2.append(0)
print(linked_list2.getCount(linked_list2.head))  # Output: 7
