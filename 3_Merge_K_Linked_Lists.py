# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from queue import PriorityQueue
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # if not lists: return []
        if len(lists) == 1: return lists[0]

        pq = PriorityQueue()
        ans = ListNode(None)
        curr = ans

        for index, node in enumerate(lists):
            if node:
                pq.put((node.val, index, node))

        while not pq.empty():
            temp, index, curr.next = pq.get()
            curr = curr.next
            if curr.next:
                pq.put((curr.next.val, index, curr.next))
        
        return ans.next
