# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        current = head
        while current:
            if hasattr(current, "visited"):
                return True
            current.visited = True
            current = current.next
        return False