# Remove duplicates from an unsorted linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    # Function to remove duplicates from unsorted linked list.
    def removeDuplicates(self, head):
        # Create an empty set to store unique values.
        unique_values = set()

        # Initialize pointers to the current node and its previous node.
        current = head
        prev = None

        # Traverse the linked list.
        while current is not None:
            # If the current node's value is already in the set, it's a duplicate.
            # So, skip this node by updating the previous node's next pointer.
            if current.data in unique_values:
                prev.next = current.next
            else:
                # Otherwise, add the value to the set and move the previous pointer.
                unique_values.add(current.data)
                prev = current
            current = current.next

        return head

# Function to print the linked list.
def printLinkedList(head):
    current = head
    while current:
        print(current.data, end=" ")
        current = current.next
    print()

# Test cases
if __name__ == "__main__":
    # Test case 1
    head1 = Node(5)
    head1.next = Node(2)
    head1.next.next = Node(2)
    head1.next.next.next = Node(4)
    solution = Solution()
    result1 = solution.removeDuplicates(head1)
    print("Test Case 1:")
    print("Expected Output: 5 2 4")
    print("Actual Output: ", end="")
    printLinkedList(result1)

    # Test case 2
    head2 = Node(2)
    head2.next = Node(2)
    head2.next.next = Node(2)
    head2.next.next.next = Node(2)
    head2.next.next.next.next = Node(2)
    result2 = solution.removeDuplicates(head2)
    print("\nTest Case 2:")
    print("Expected Output: 2")
    print("Actual Output: ", end="")
    printLinkedList(result2)
