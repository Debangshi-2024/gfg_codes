class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class Solution:
    def reverseList(self, head):
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev



