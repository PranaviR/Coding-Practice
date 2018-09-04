class Solution:
    def palindrome_permute(self, str):
        arr=[0]*128
        for i in range(0,len(str)):
            if str[i].isalpha():
                val=ord(str[i])
                if arr[val]>0:
                    arr[val]=arr[val]+1
                else:
                    arr[val]=1
            else:
                arr[val]=-1
        foundOdd=False
        for i in range(0,len(str)):
            val=ord(str[i])
            if arr[val]%2==1:
                if foundOdd:
                    return False
                foundOdd=True
        return True
                    
            
sol=Solution()
result=sol.palindrome_permute("tacppcat")
print(result)

#USING BIT OPERATOR
# class Solution:
#     def palindrome_permute(self, str):
#         checker=0
#         for i in range(0,len(str)):
#             val=ord(str[i].lower())-ord('a')
#             if (checker&(1<<val)) > 0:
#                 checker=checker^(1<<val)
#             else:
#                 checker=checker|(1<<val)
#         for i in range(0,len(str)):
#             if checker&(checker-1)==0:
#                 return True
#         return False
            
                                          
# sol=Solution()
# result=sol.palindrome_permute("tacopcat")
# print(result)







    



        