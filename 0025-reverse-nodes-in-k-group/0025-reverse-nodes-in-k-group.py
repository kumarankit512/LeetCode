# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = groupPrev = ListNode(0)
        groupPrev.next = head
        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next
            prev = kth.next
            curr = groupPrev.next

            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            temp = groupPrev.next
            groupPrev.next = kth
            groupPrev = temp
        return dummy.next
        
    def getKth(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        while head and k > 0:
            head = head.next
            k -= 1
        return head	

# Time Complexity: O(n)
# Space Complexity: O(1)
# where n is the number of nodes in the linked list.
# The algorithm iterates through the linked list, reversing k nodes at a time.