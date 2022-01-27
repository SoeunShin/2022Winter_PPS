# LeetCode 206 - Reverse Linked List

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(node: ListNode, prev: ListNode = None ): # 재귀함수
            if not node: # base case
                return prev
            next, node.next = node.next, prev
            return reverse(next, node) # 재귀함수 호출

        return reverse(head)