class Solution:
    
    def rotate_string(self, s1,s2):
        s2=s2+s2
        if self.isSubstring(s1,s2):
            return True
        else:
            return False
    def isSubstring(self,s1,s2):
        if s1 in s2:
            return True
        else:
            return False
    
sol=Solution()
mat=[[1,2,0,4],[5,6,7,8],[9,10,11,12],[13,0,15,16]]
result=sol.rotate_string("waterbottle","erbottlewat")
print(result)










    



        