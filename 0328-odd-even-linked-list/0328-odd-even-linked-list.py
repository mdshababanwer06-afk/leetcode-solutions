# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode | None) -> ListNode | None:
        if head is None or head.next is None:
            return head

        values = []

        # Odd-positioned nodes
        temp = head
        while temp:
            values.append(temp.val)
            if temp.next is None:
                break
            temp = temp.next.next

        # Even-positioned nodes
        temp = head.next
        while temp:
            values.append(temp.val)
            if temp.next is None:
                break
            temp = temp.next.next

        # Update the linked list
        temp = head
        index = 0

        while temp:
            temp.val = values[index]
            index += 1
            temp = temp.next

        return head
