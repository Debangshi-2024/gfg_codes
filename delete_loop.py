class Solution:
    def removeLoop(self, head):
        slow = head
        fast = head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                self._removeLoop(head, slow)
                return
        return

    def _removeLoop(self, head, loop_node):
        ptr1 = head
        ptr2 = loop_node
        if ptr1 == ptr2:
            while ptr2.next != ptr1:
                ptr2 = ptr2.next
            ptr2.next = None
            return
        while ptr1.next != ptr2.next:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        ptr2.next = None


