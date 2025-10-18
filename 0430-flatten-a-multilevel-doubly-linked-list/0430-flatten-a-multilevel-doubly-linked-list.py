"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        def recurse(node):
            while node:
                # if child exists
                if node.child:
                    # recurse and get the last node of that child
                    last_node = recurse(node.child)
                    # next node of curr
                    next_node = node.next
                    # curr next becomes the child
                    node.next = node.child
                    # prev of child becomes the curr
                    node.child.prev = node
                    # curr child becomes None
                    node.child = None
                    # if next node exists
                    if next_node:
                        # prev of next node becomes last_node recursed and vice versa
                        next_node.prev, last_node.next = last_node, next_node
                        node = last_node
                # if not, loop through the curr until None
                # return if None
                else:
                    if node.next is None:
                        return node
                    node = node.next
        # start with head and it will recursively do for each child until None
        recurse(head)
        # return head
        return head
        
#Time Complexity: O(n)
#Space Complexity: O(n)