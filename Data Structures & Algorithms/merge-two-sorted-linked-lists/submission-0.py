# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        dummy = ans
        l, r = list1, list2
        while l or r:
            if l and r:
                if l.val < r.val:
                    dummy.next = ListNode(l.val)
                    l = l.next
                else:
                    dummy.next = ListNode(r.val)
                    r = r.next
                dummy = dummy.next
            elif l:
                dummy.next = l
                l = None
            else:
                dummy.next = r
                r = None
        return ans.next

            