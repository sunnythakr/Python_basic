# Remove duplicate element from sorted Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def removeDuplicates(head):
    current = head  # Initialize the current node as the head of the list

    # Traverse the list
    while current is not None and current.next is not None:
        if current.data == current.next.data:
            # If the current node and the next node have the same value, skip the next node
            current.next = current.next.next
        else:
            # If values are different, move to the next node
            current = current.next

    return head  # Return the head of the updated linked list

# Helper function to print the linked list
def printLinkedList(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

# Example 1
# Input: 2 -> 2 -> 4 -> 5
head1 = Node(2)
head1.next = Node(2)
head1.next.next = Node(4)
head1.next.next.next = Node(5)

print("Original Linked List:")
printLinkedList(head1)

new_head1 = removeDuplicates(head1)

print("Linked List after removing duplicates:")
printLinkedList(new_head1)

# Example 2
# Input: 2 -> 2 -> 2 -> 2 -> 2
head2 = Node(2)
head2.next = Node(2)
head2.next.next = Node(2)
head2.next.next.next = Node(2)
head2.next.next.next.next = Node(2)

print("\nOriginal Linked List:")
printLinkedList(head2)

new_head2 = removeDuplicates(head2)

print("Linked List after removing duplicates:")
printLinkedList(new_head2)
