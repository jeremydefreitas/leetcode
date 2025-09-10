# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        if not head.next:
            head = None
            return head
        length = 0
        pointer = head
        while pointer:
            length += 1
            pointer = pointer.next
        print(length)
        target = length - n

        if target == 0:
            head = head.next
            
            return head
       
        i = 1
        head1 = head
        while i < target:
            head1 = head1.next
            i += 1

        tmp = head1.next.next
        head1.next = tmp

        return head
     


        