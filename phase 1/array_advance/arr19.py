class Node:
    def __init__(self,data):
        self.data=data
        self.next=None 
def traverseAndPrint(head):
    currentNode = head
    while currentNode:
        print(currentNode.data, end=" -> ")
        currentNode = currentNode.next
    print("null") 
node1=Node(13)
node2=Node(130)
node3=Node(12)
node4=Node(11)
node1.next=node2
node2.next=node3
node3.next=node4


traverseAndPrint(node1)
