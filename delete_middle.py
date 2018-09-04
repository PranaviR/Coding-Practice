class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
head = Node(1)

node1=Node(2)
head.next=node1
node2=Node(3)
node1.next=node2
node3=Node(4)
node2.next=node3
node4=Node(5)
node3.next=node4

class Solution:
    def delete_middle(self, node):
        if node==None or node.next==None:
            return node
        node.data=node.next.data
        node.next=node.next.next
        return node
    

sol=Solution()
result=sol.delete_middle(node2)
print(result.data)






        