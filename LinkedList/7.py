# Given a linked list of size N and a key. 
# The task is to insert the key in the middle of the linked list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insertInMid(head, node):
    if head is None:  # If the list is empty, make the new node the head
        head = node
        return head
    
    # Initialize two pointers: slow and fast
    slow = head
    fast = head
    
    # Traverse the list using the fast pointer with two steps and the slow pointer with one step
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    
    # Now 'slow' points to the middle node
    # Insert the new node after the middle node
    node.next = slow.next
    slow.next = node
    
    return head

# Helper function to print the linked list
def printList(head):
    current = head
    while current:
        print(current.data, end=" ")
        current = current.next
    print()

# Example usage
if __name__ == "__main__":
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(40)
    head.next.next.next = Node(50)
    
    new_node = Node(30)
    head = insertInMid(head, new_node)
    
    printList(head)
