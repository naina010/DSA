# Stack using singly LL

class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

class Stack:
    def __init__(self):
        self.head=None

    def push(self,node):  # O(1)
        if self.head is None:
            self.head=node
        else:
            node.next=self.head.next
            self.head=node

    def pop(self):      # O(1)
        if self.head is None:
            print('underflow')
        else:
            self.head=self.head.next

    def display(self):
        p=self.head
        while p:
            print(p.val)
            p=p.next
