#####Backward direction###########

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
head1 = Node(7)
node1=Node(1)
head1.next=node1
node2=Node(6)
node1.next=node2

head2 = Node(5)
node3=Node(9)
head2.next=node3
node4=Node(2)
node3.next=node4

class Solution:
    def sum(self,head1,head2):
        prev=Node(0)
        temp=prev
        carry=0
        while head1!=None or head2!=None:
            sum=0
            if head2 is not None:
                sum=sum+head2.data
                head2=head2.next
            if head1 is not None:
                sum=sum+head1.data
                head1=head1.next
            sum=sum+carry
            carry=int(sum/10)
            new=Node(sum%10)
            prev.next=new
            prev=new  
        if carry>0:
            new=Node(carry)
            prev.next=new
        return temp.next
            
                          
sol=Solution()
result=sol.sum(head1,head2)
while result!=None:
    print(result.data)
    result=result.next
	
	
	
	
#####Forward direction###########	
	
	
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
head1 = Node(6)
node1=Node(1)
head1.next=node1
node2=Node(7)
node1.next=node2

head2 = Node(2)
node3=Node(9)
head2.next=node3
node4=Node(5)
node3.next=node4

class Solution:
    head=None
    def pad(self,list1,n):
        head=list1
        for i in range(0,n):
            newNode=Node(0)
            newNode.next=head
            head=newNode
        return head
        
    def length(self,list):
        count=0
        while(list!=None):
            count=count+1
            list=list.next
        return count
    def save(self,data):
        if self.head == None:
            self.head = Node(data)
        else:
            node = Node(data)
            node.next = self.head
            self.head =node
        return self.head
    def addRecursive(self,h1,h2):
        if h1==None and h2==None:
            return 0
        carry=self.addRecursive(h1.next,h2.next)
        sum=carry
        if h1:
            sum=sum+h1.data
        if h2:
            sum=sum+h2.data
        self.save(sum%10)
        
        return 1 if sum>=10 else 0
        
    def sum(self,head1,head2):
        if head1==None and head2==None:
            return None
        elif head1==None:
            return head2
        elif head2==None:
            return head1
        len1=self.length(head1)
        len2=self.length(head2)
        if len1<len2:
            head1=pad(head1,len2-len1)     
        elif len2<len1:
            head2=pad(head2,len1-len2)
        self.addRecursive(head1,head2)
        return self.head
                          
sol=Solution()
result=sol.sum(head1,head2)
while result!=None:
    print(result.data)
    result=result.next
        
        