# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None
        prev = None

        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        firstHalf, secondHalf = head, prev
        while secondHalf:
            tmp1, tmp2 = firstHalf.next, secondHalf.next
            firstHalf.next = secondHalf
            secondHalf.next = tmp1
            firstHalf, secondHalf = tmp1, tmp2
            
        

        
        
        