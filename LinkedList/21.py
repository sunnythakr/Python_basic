# Intersection of two sorted Linked lists
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def findIntersection(head1, head2):
    dummy = Node(0)
    tail = dummy
    
    while head1  is not None and head2 is not None:
        if head1.data < head2.data:
            head1 = head1.next
        elif head1.data > head2.data:
            head2 = head2.next
        else:
            new_node = Node(head1.data)
            tail.next = new_node
            tail = new_node
            head1 = head1.next
            head2 = head2.next
    
    return dummy.next

# Helper function to print linked list
def printLinkedList(head):
    current = head
    while current is not None:
        print(current.data, end=" ")
        current = current.next
    print()

# Test case 1
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node6 = Node(6)
node8 = Node(8)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node6

node2_2 = Node(2)
node4_2 = Node(4)
node6_2 = Node(6)
node8.next = node2_2
node2_2.next = node4_2
node4_2.next = node6_2

intersection_head = findIntersection(node1, node8)
print("Test Case 1:")
print("Intersection: ", end="")
printLinkedList(intersection_head)

# Test case 2
node10 = Node(10)
node20 = Node(20)
node40 = Node(40)
node50 = Node(50)

node10.next = node20
node20.next = node40

node15 = Node(15)
node40_2 = Node(40)

node15.next = node40_2

intersection_head = findIntersection(node10, node15)
print("\nTest Case 2:")
print("Intersection: ", end="")
printLinkedList(intersection_head)
