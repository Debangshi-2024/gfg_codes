def deleteNode(head, x):
    if head is None:
        return None
    if x == 1:
        return head.next
    
    curr = head
    for _ in range(x - 2):
        if curr.next is None:
            return head
        curr = curr.next
    
    if curr.next:
        curr.next = curr.next.next
    
    return head

