# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        removed = []
        for i, lst in enumerate(lists):
            if not lst:
                removed.append(i)
        for x in removed[::-1]:
            lists.pop(x)
        if len(lists) == 1:
            return lists[0]
        if len(lists) == 0:
            return None
        min_index = min([(x, i) for i, x in enumerate([node.val for node in lists])])[1]
        lists[min_index].next = self.mergeKLists(lists[:min_index] + lists[min_index + 1:] + [lists[min_index].next]) 
        return lists[min_index]