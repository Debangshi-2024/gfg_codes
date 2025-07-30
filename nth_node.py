class Solution:
    def getKthFromLast(self, head, k):
        slow = head
        fast = head
        for _ in range(k):
            if fast is None:
                return -1
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        return slow.data if slow else -1


