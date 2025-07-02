#!/usr/bin/python3
class Node:
    def __init__ (self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    """
    self.head -> new node
    if self.head is there , check is there is next, if there is go there and check if next is null, ifits null add the new node there 

    1(none) 

    1 next is node(data)

    1 (next),2 ()
    """
    def append(self, data):
        if not self.head:
            self.head = Node(data)
        nxt = self.head
        while nxt.next:
            nxt = nxt.next
        nxt.next =  Node(data)
    
    def traverse(self):
        # print(self.head.data)
        next = self.head
        while next:
            print(next.data)
            next = next.next

cll = LinkedList()
cll.append("sailes")
cll.append("abhji")
cll.append("ceas")

cll.traverse()
