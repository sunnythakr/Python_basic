# reverse a doubly Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def reverseDLL(head):
    # Base case: If the list is empty or has only one node, return head
    if not head or not head.next:
        return head
    
    prev_node = None
    current_node = head
    while current_node:
        next_node = current_node.next
        current_node.next = prev_node
        current_node.prev = next_node
        prev_node = current_node
        current_node = next_node
    
    # After the loop, prev_node will be the new head of the reversed list
    return prev_node

# Helper function to print the linked list
def printDLL(head):
    current = head
    while current:
        print(current.data, end=" ")
        current = current.next
    print()

# Create the linked list for testing
nodes = [Node(3), Node(4), Node(5)]
for i in range(len(nodes) - 1):
    nodes[i].next = nodes[i+1]
    nodes[i+1].prev = nodes[i]

# Call the reverseDLL function
head = nodes[0]
print("Original linked list:")
printDLL(head)

reversed_head = reverseDLL(head)
print("Reversed linked list:")
printDLL(reversed_head)