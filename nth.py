class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def nth_from_end(head, n):
    fast = slow = head
    for _ in range(n):
        if not fast:
            return None
        fast = fast.next
    while fast:
        slow = slow.next
        fast = fast.next
    return slow.val if slow else None


head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print(nth_from_end(head, 2))  
