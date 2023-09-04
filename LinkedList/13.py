# Move Last Element to Front of a Linked List
class Solution:
    def moveToFront(self, head):
        if not head or not head.next:
            return head  # The list is empty or has only one element, no change needed
        
        # Initialize pointers to traverse the list
        prev = None
        current = head
        
        # Traverse the list to find the last and second-to-last nodes
        while current.next:
            prev = current
            current = current.next
        
        # Disconnect the last node from the list
        prev.next = None
        
        # Move the last node to the front
        current.next = head
        head = current
        
        return head
