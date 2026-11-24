# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        curr = node
        front = node

        curr.val = curr.next.val
        front = front.next.next
        curr.next = front
        
        