# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:  
    def merge(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:	
        if (list1 is None and list2 is None):
            return None
        if (list1 is None):
            return list2
        if (list2 is None):
            return list1


        node = ListNode()
        if (list1.val < list2.val):
            node = list1
            list1 = list1.next
        else:
            node = list2
            list2 = list2.next

        head = node
        while (list1 is not None and list2 is not None):
            if (list1.val < list2.val):
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next
        if (list1 is not None):
            node.next = list1
        if (list2 is not None):
            node.next = list2
        return head
    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        if n == 0:
            return None
        while n > 1:
            for i in range (0, n // 2):
                lists[i] = self.merge(lists[i], lists[n-i-1])
            n = (n + 1) // 2
        return lists[0]
