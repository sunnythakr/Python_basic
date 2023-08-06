# Given head, the head of a singly linked list, find if the linked list is
#  circular or not. A linked list is called circular if it not NULL
#  terminated and all nodes are connected in the form of a cycle.
#  An empty linked list is considered as circular.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def isCircular(head):
    if not head:
        return True  # An empty linked list is considered circular

    slow = head
    fast = head.next

    while fast and fast.next:
        if slow == fast:
            return True  # If the pointers meet, it is a circular linked list
        slow = slow.next
        fast = fast.next.next

    return False  # If the loop completes, it is not a circular linked list

# Test Example 1
head1 = Node(1)
head1.next = Node(2)
head1.next.next = Node(3)
head1.next.next.next = Node(4)
head1.next.next.next.next = Node(5)
head1.next.next.next.next.next = head1  # The last node points back to the first node

print(isCircular(head1))  # Output: True

# Test Example 2
head2 = Node(2)
head2.next = Node(4)
head2.next.next = Node(6)
head2.next.next.next = Node(7)
head2.next.next.next.next = Node(5)
head2.next.next.next.next.next = Node(1)

print(isCircular(head2))  # Output: False
