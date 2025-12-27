class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
def traversal(head):
    a=[]
    current=head
    while current:
        a.append(current.data)
        
        current=current.next
    print(a[::-1]) 
node1=Node(11)
node2=Node(21)
node3=Node(31)
node4=Node(31)
node1.next=node2
node2.next=node3
node3.next=node4
traversal(node1)
 