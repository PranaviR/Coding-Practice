class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
head = Node(3)

node1=Node(5)
head.next=node1
node2=Node(8)
node1.next=node2
node3=Node(5)
node2.next=node3
node4=Node(10)
node3.next=node4
node5=Node(2)
node4.next=node5
node6=Node(1)
node5.next=node6

class Solution:
    def partition(self, node, x):
        head=Node(None)
        tail=Node(None)
        end=tail
        first=head
        while node!=None:
            next=node.next
            if node.data < x:
                head.next=node
                head=node
            else:
                tail.next=node
                tail=node
            node=next
        tail.next=None
        head.next=end.next
        return first.next
                
sol=Solution()
result=sol.partition(head, 5)
while result!=None:
    print(result.data)
    result=result.next