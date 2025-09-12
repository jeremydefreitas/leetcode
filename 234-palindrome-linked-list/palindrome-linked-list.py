# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        test = []
        
        while head:
            test.append(head.val)
            head = head.next
        
        l, r = 0, len(test) - 1

        while l < r:
            if test[l] != test[r]:
                return False
            l += 1
            r -= 1
        return True