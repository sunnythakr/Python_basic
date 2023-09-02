# Given a linked list of N nodes. The task is to check if the linked list has
#  a loop. Linked list can contain self loop.

class Solution:
    # Function to check if the linked list has a loop.
    def detectLoop(self, head):
        # Initialize two pointers: slow (tortoise) and fast (hare).
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next  # Move slow one step.
            fast = fast.next.next  # Move fast two steps.

            # If slow and fast pointers meet, there is a loop.
            if slow == fast:
                return True

        # If fast pointer reaches the end of the list, there is no loop.
        return False
