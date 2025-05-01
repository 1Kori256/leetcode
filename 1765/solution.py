# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        current = list1
        indx = 0
        a_node = b_node = None
        while current:
            if indx == a-1:
                a_node = current
            if indx == b+1:
                b_node = current
            indx+=1
            current = current.next
        a_node.next = list2
        current = list2
        while current.next:
            current = current.next
        current.next = b_node
        return list1