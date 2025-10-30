# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        curr = head
        end = ListNode()
        prev = end
        dummy = ListNode()
        n_prev = dummy
        while curr:
            if curr.val>=x:
                node = ListNode(curr.val)
                prev.next = node
                prev = node
            else:
                n_prev.next = curr
                n_prev = curr
            curr = curr.next
        n_prev.next = end.next
        return dummy.next

   