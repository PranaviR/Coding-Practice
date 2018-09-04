
class Solution:
    def stringUnique(self, str):
        dict = {}
        for i in range(0,len(str)):
            if dict.get(str[i]):
                return 0
            else:
                dict[str[i]]=1
        return 1
        
sol=Solution()
result=sol.stringUnique("helo")
print(result)
