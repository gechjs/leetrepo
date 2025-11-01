# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        
        seen = set(nums)
        
        curr = head
        dummy = ListNode()
        prev = dummy
        while curr:
            if curr.val in seen:
                curr = curr.next
            else:
                prev.next = curr
                prev = curr
                curr = curr.next
        return dummy.next
