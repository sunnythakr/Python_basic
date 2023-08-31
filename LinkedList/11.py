# Given a Singly Linked List of size N, delete all alternate nodes of the list.
# Input:
# LinkedList: 1->2->3->4->5->6
# Output: 1->3->5
# Explanation: Deleting alternate nodes
# results in the linked list with elements
# 1->3->5.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteAlt(head):
    if not head or not head.next:
        return
    
    current = head
    while current and current.next:
        current.next = current.next.next
        current = current.next
    
# Helper function to print the linked list
def printLinkedList(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Creating the linked list
nodes = [1, 2, 3, 4, 5, 6]
head = ListNode(nodes[0])
current = head
for val in nodes[1:]:
    current.next = ListNode(val)
    current = current.next

print("Original Linked List:")
printLinkedList(head)

deleteAlt(head)
print("\nLinked List after deleting alternate nodes:")
printLinkedList(head)
