#!/usr/bin/python3

""" making a linked list in python """

"""
store data
store the next value


node -> data , location of the next 

head -> the starting point 


you have head you roll
       ______
      |      |
{2, next}, {3, next}

when I creat a linked list I need location of n , which is self, that


to add values to a linked list

head(data -> next(data, next())) 

traveersl - print self head -> go next -> print next head

when making a linked list -> add the first data

when deleting an item
=======================

check the next
if next data is what I want , connect its next to me 
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def traversal(self):
        print(self.head.data)
        first = self.head.next
        while first:
            print(first.data)
            first = first.next
    def insert_new_header(self, data):
        temp = self.head
        self.head = Node(data)
        self.head.next = temp

    def delete_node(self, data):
        first = self.head
        while first:
            if first.next.data is not None and  first.next.data == data:
                first.next = first.next.next
                break
            first = first.next



            

family = LinkedList()
family.head = Node("Vitalis")
wife = Node("Alexia")
first_kid = Node("kiptum")
second_kid = Node("Ngosh")

family.head.next = wife
wife.next = first_kid
first_kid.next = second_kid

# LinkedList.traversal(family)

family.insert_new_header("Ngelechei")
LinkedList.traversal(family)

print("===================================")

family.traversal()