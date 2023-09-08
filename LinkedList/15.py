# Reverse a linked list
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class Solution:
    # Function to reverse a linked list.
    def reverseList(self, head):
        prev_node = None
        current_node = head
        while current_node is not None:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        return prev_node

# Test Case 1
# Input: 1->2->3->4->5->6
# Output: 6 5 4 3 2 1
head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
solution = Solution()
new_head1 = solution.reverseList(head1)
reversed_elements1 = []
current = new_head1
while current:
    reversed_elements1.append(current.value)
    current = current.next
print("Test Case 1:", reversed_elements1)  # Output: [6, 5, 4, 3, 2, 1]

# Test Case 2
# Input: 2->7->8->9->10
# Output: 10 9 8 7 2
head2 = ListNode(2, ListNode(7, ListNode(8, ListNode(9, ListNode(10)))))
new_head2 = solution.reverseList(head2)
reversed_elements2 = []
current = new_head2
while current:
    reversed_elements2.append(current.value)
    current = current.next
print("Test Case 2:", reversed_elements2)  # Output: [10, 9, 8, 7, 2]

# Test Case 3
# Input: 1
# Output: 1
head3 = ListNode(1)
new_head3 = solution.reverseList(head3)
reversed_elements3 = []
current = new_head3
while current:
    reversed_elements3.append(current.value)
    current = current.next
print("Test Case 3:", reversed_elements3)  # Output: [1]

# Test Case 4
# Input: None
# Output: None
new_head4 = solution.reverseList(None)
print("Test Case 4:", new_head4)  # Output: None

# Test Case 5
# Input: 1->2->3->4->5
# Output: 5 4 3 2 1
head5 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
new_head5 = solution.reverseList(head5)
reversed_elements5 = []
current = new_head5
while current:
    reversed_elements5.append(current.value)
    current = current.next
print("Test Case 5:", reversed_elements5)  # Output: [5, 4, 3, 2, 1]
