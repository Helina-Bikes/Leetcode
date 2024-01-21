# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to simplify code
        dummy = ListNode()
        dummy.next = head
        current = dummy

        while current.next and current.next.next:
            # Nodes to be swapped
            first = current.next
            second = current.next.next

            # Swapping nodes
            current.next = second
            first.next = second.next
            second.next = first

            # Move to the next pair
            current = first

        return dummy.next
