class Solution:
    def URLify(self, str):
        array = [0] * 128
        for i in range(0,len(str)):
            if str[i].isalpha():   
                if array[ord(str[i])]:
                    array[ord(str[i])] = array[ord(str[i])] + 1
                else:
                    array[ord(str[i])] = 1
            else:
                    array[ord(str[i])] = 2
        foundOdd = False
        for i in range(0,len(str)):
            if array[ord(str[i])] %2 == 1:
                if foundOdd:
                    return False
                foundOdd = True
        return True
            
sol=Solution()
result=sol.URLify("taccat")
print(result)


class Solution:
#     def URLify(self, str):
#         checker = 0
#         for i in range(0,len(str)):
#             if str[i].lower().isalpha():
#                 val = ord(str[i]) - ord('a')
#                 if (checker & (1<<val)) > 0:
#                     checker =  checker ^ (1<<val)
#                 else:
#                     checker = checker|(1<<val)
#         if (checker&(checker-1))==0:
#             return True
#         return False
        
                
            
# sol=Solution()
# result=sol.URLify("tacopcat")
# print(result)







    



        