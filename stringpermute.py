class Solution:
    def stringpermute(self, str1, str2):
        dict={}
        if len(str1)!=len(str2):
            return False
        for i in range(0,len(str1)):
            if dict.get(str1[i]):
                dict[str1[i]] = dict[str1[i]]+1
            else:
                dict[str1[i]] = 1
        for i in range(0,len(str2)):
            if dict.get(str2[i]):
                if dict.get(str2[i])>1:
                    dict[str2[i]] = dict[str2[i]]-1
                else:
                    del dict[str2[i]] 
            else: 
                return False
        return True
sol=Solution()
result=sol.stringpermute("helo","ehol")
print(result)

#class Solution:
#     def stringpermute(self, str1, str2):
#         str1=sorted(str1)
#         str2=sorted(str2)
#         if str1==str2:
#             return True
#         else:
#             return False
# sol=Solution()
# result=sol.stringpermute("helo","ehil")
# print(result)


    



        