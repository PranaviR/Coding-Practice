class Node:
    def __init__(self, data):
        self.data = data
        self.next = None



class Solution:
    def remove_dups(self, head):
        if head is None or head.next is None:
            return head
        current=head.next
        dict={}
        dict[head.data]=1
        prev=head
        while current!=None:
            if dict.get(current.data):
                prev.next=current.next
            else:
                dict[current.data]=1
                previous=current
            current=current.next
        return head
                 
sol=Solution()
head = Node(5)

node1=Node(3)
head.next=node1
node2=Node(2)
node1.next=node2
node3=Node(3)
node2.next=node3
node4=Node(5)
node3.next=node4


result=sol.remove_dups(head)
print(result.data)
while result!=None:
    print(result.data)
    result=result.next
        