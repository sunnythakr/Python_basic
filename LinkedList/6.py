# Given a linked list sorted in ascending order and an integer called data, 
# insert data in the linked list such that the list remains sorted.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def sortedInsert(self, head1,key):
        # code here
        # return head of edited linked list
        newnode=Node(key)
        if head1 is None:
            return newnode
        if head1.data > key:
            newnode.next= head1
            return newnode
        curr=head1
        while curr.next and curr.next.data < key:
            curr=curr.next
        newnode.next=curr.next
        curr.next=newnode
        return head1