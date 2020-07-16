# Reverse a Linkedlist

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head=None

    def insertion_at_end(self, val):
        temp=Node(val)
        if self.head == None:
            self.head = temp
        else:
            p=self.head
            while p.next != None:
                p = p.next
            p.next = temp

    def reverse(self):
        ptr = self.head
        prev = None
        q = self.head
        while ptr != None:
            q = q.next
            ptr.next = prev
            prev = ptr
            ptr = q
        self.head = prev

    def display(self):
        p = self.head
        while p != None:
            print(p.val, end=' ')
            p = p.next
        print()

ll = Linkedlist()
ll.insertion_at_end(1)
ll.insertion_at_end(2)
ll.insertion_at_end(3)
ll.insertion_at_end(4)
ll.insertion_at_end(8)
ll.display()
ll.reverse()
ll.display()