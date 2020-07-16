class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

class Queue:
    def __init__(self):
        self.head=None
        self.rear=None
        self.front=None

    def enqueue(self,data):
        if self.head is None:
            self.head=Node(data)
            self.front=self.head
            self.rear=self.head
        else:
            node=Node(data)
            self.rear.next=node
            self.rear=self.rear.next

    def dequeue(self):
        if self.front is None:
            print('underflow')
        else:
            self.front=self.front.next

    def display(self):
        if self.front:
            f=self.front
            while f:
                print(f.val)
                f=f.next
        else:
            print('queue empty')
