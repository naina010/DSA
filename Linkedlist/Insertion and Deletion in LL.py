class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class Linkedlist:
    def __init__(self):
        self.head=None
    def insertion_at_end(self, data):
        temp=Node(data)
        if self.head == None:
            self.head = temp
        else:
            p=self.head
            while p.next != None:
                p = p.next
            p.next = temp

    def insertion_at_front(self, data):
        temp = Node(data)
        temp.next = self.head
        self.head = temp

    def display(self):
        p = self.head
        while p != None:
            print(p.data, end=' ')
            p = p.next
        print()

    def delete_from_end(self):
        p = self.head
        prev = None
        while p.next != None:
            prev = p
            p = p.next
        prev.next = None

    def delete_from_front(self):
        p = self.head
        if p:
            self.head = p.next
        else:
            print('ll empty')

    def insertion_before_value(self,val,data):
        p = self.head
        prev = None
        while p != None:
            if p.data == val:
                temp = Node(data)
                temp.next=p
                prev.next=temp
                break
            prev=p
            p = p.next

    def insertion_after_value(self,val,data):
        p = self.head
        while p != None:
            if p.data == val:
                temp = Node(data)
                temp.next=p.next
                p.next=temp
                break
            p=p.next

    def delete_val(self,val):
        p=self.head
        prev=None
        if p:
            while p!=None:
                if p.data==val:
                    prev.next=p.next
                    break
                prev=p
                p=p.next
        else:
            print('ll empty')

    def delete_before_value(self,val):
        p=self.head
        prev=None
        prev_prev=None
        while p!=None:
            if p.data==val:
                if prev_prev != None:
                    prev_prev.next=prev.next
                else:
                    self.head=prev.next
                break
            prev_prev=prev
            prev=p
            p=p.next

    def delete_after_value(self,val):
        p=self.head
        while p!=None:
            if p.data==val:
                p.next=p.next.next
                break
            p=p.next
