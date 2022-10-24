# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # A fast pointer and a slow pointer - both start at the head of the linked list
        fast = head
        slow = head

        # find middle (slow)
        while fast and fast.next:
        # almost the same as -while fast != null and fast.next != null
        # ie keep looking till we are at null or at the last node 
            fast = fast.next.next
            slow = slow.next

        # reverse second half
        prev = None
        while slow:
            tmp = slow.next
            prev = slow
            slow = tmp

        # check palindrome
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True