class Solution:
    def reverseDLL(self, head):
        if head is None or head.next is None:
            return head

        curr = head
        prev_node = None

        while curr:
            prev_node = curr.prev
            curr.prev = curr.next
            curr.next = prev_node
            curr = curr.prev

        if prev_node:
            head = prev_node.prev

        return head
