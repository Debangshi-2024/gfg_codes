class Solution:
    def delete_node(self, head, x):
        if head is None:
            return head

        if x == 1:
            head = head.next
            if head:
                head.prev = None
            return head

        curr = head
        count = 1
        while curr is not None and count < x:
            curr = curr.next
            count += 1

        if curr is None:
            return head

        if curr.prev:
            curr.prev.next = curr.next

        if curr.next:
            curr.next.prev = curr.prev

        return head
