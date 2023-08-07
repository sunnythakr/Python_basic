# Given two Singly Linked List of N and M nodes respectively.
#  The task is to check whether two linked lists are identical or not. 
# Two Linked Lists are identical when they have same data and with
#  same arrangement too.

# Node class definition
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Function to check if two linked lists are identical
def areIdentical(head1, head2):
    current1 = head1
    current2 = head2
    
    while current1 is not None and current2 is not None:
        if current1.data != current2.data:
            return False
        
        current1 = current1.next
        current2 = current2.next
    
    if current1 is not None or current2 is not None:
        return False
    
    return True

# Helper function to create a linked list from a list of values
def createLinkedList(values):
    if not values:
        return None
    
    head = Node(values[0])
    current = head
    for value in values[1:]:
        current.next = Node(value)
        current = current.next
    
    return head

# Test cases
list1 = createLinkedList([1, 2, 3, 4, 5, 6])
list2 = createLinkedList([99, 59, 42, 20])
print(areIdentical(list1, list2))  # Output: False

list3 = createLinkedList([1, 2, 3, 4, 5])
list4 = createLinkedList([1, 2, 3, 4, 5])
print(areIdentical(list3, list4))  # Output: True