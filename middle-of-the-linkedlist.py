# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        size = 0
        temp = head
        while temp is not None:
            temp = temp.next
            size += 1

        for i in range(math.floor(size / 2)):
            head = head.next

        return head
