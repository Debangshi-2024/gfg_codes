class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    dummy = curr = Node()
    carry = 0
    while l1 or l2 or carry:
        x = l1.val if l1 else 0
        y = l2.val if l2 else 0
        total = x + y + carry
        carry = total // 10
        curr.next = Node(total % 10)
        curr = curr.next
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    return dummy.next

def printList(node):
    while node:
        print(node.val, end=" ")
        node = node.next
    print()


l1 = Node(2, Node(4, Node(3)))  
l2 = Node(5, Node(6, Node(4)))  

result = addTwoNumbers(l1, l2)
printList(result)  
