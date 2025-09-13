"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):
    def flatten(self, head):
        cur = head

        while cur:
            if cur.child:
                old_next = cur.next
                cur.next = self.flatten(cur.child)
                cur.next.prev = cur
                cur.child = None
                

                while cur.next:
                    cur = cur.next
                cur.next = old_next
                if old_next:
                    old_next.prev = cur

            cur = cur.next
        return head
        