# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        first = -1
        prev_critical = -1
        min_dist = float('inf')

        prev = head
        curr = head.next
        index = 1

        while curr.next:
            next_node = curr.next

            # Check local maximum or local minimum
            if ((curr.val > prev.val and curr.val > next_node.val) or
                (curr.val < prev.val and curr.val < next_node.val)):

                if first == -1:
                    # First critical point
                    first = index
                    prev_critical = index

                else:
                    # Distance from previous critical point
                    min_dist = min(min_dist, index - prev_critical)

                    prev_critical = index

            prev = curr
            curr = next_node
            index += 1

        # Fewer than 2 critical points
        if min_dist == float('inf'):
            return [-1, -1]

        max_dist = prev_critical - first

        return [min_dist, max_dist]