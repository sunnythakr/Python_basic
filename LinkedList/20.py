# Find length of Loop
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def countNodesinLoop(head):
    if not head:
        return 0

    slow = head
    fast = head
    loop_exists = False

    # Detect the loop using Floyd's algorithm.
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            loop_exists = True
            break

    # If there's no loop, return 0.
    if not loop_exists:
        return 0

    # Count the nodes in the loop.
    count = 1
    current = slow.next
    while current != slow:
        count += 1
        current = current.next

    return count

# Example usage:
# Create a linked list and connect the last node to create a loop.
head = Node(25)
head.next = Node(14)
head.next.next = Node(19)
head.next.next.next = Node(33)
head.next.next.next.next = Node(10)
head.next.next.next.next.next = Node(21)
head.next.next.next.next.next.next = Node(39)
head.next.next.next.next.next.next.next = Node(90)
head.next.next.next.next.next.next.next.next = Node(58)
head.next.next.next.next.next.next.next.next.next = Node(45)
# Connect the last node to the 4th node to form a loop.
head.next.next.next.next.next.next.next.next.next.next = head.next.next.next.next

C = 4  # Position of the node that connects to the last node for the loop.
result = countNodesinLoop(head)
print("Length of the loop:", result)  # Output should be 7
