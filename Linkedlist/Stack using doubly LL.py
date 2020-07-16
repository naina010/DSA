
class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
        self.prev=None

class Stack:
    def __init__(self):
        self.head=None
        self.top=None

    def push(self,node):
        if self.head is None:
            self.head=node
            self.top=self.head
        else:
            self.top.next=node
            node.prev=self.top
            self.top=node

    def pop(self):
        if self.head is None:
            print('underflow')
        else:
            self.top=self.top.prev
            self.top.next=None

    def display(self):
        p=self.head
        while p:
            print(p.val)
            p=p.next
