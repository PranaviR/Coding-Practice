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
    def return_k(self,k ,head):
        slow=head
        fast=head
        for i in range(k):
            fast=fast.next
        while fast!=None:
            slow=slow.next
            fast=fast.next
        return slow
    

sol=Solution()
result=sol.return_k(3,head)
print(result.data)




        