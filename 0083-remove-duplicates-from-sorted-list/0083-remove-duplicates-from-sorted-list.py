# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        curr = head 
        front = head

        while front!= None:
            if ( curr.val == front.val):
                if ( front.next == None):
                    curr.next = None
                front = front.next
            else :
                curr.next = front
                curr = front
                front = front.next
        return head
