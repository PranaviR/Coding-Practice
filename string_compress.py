class Solution:
    def string_compress(self, str):
        compressed=""
        count=0
        for i in range(0,len(str)):
            count=count+1
            if (i+1)>=len(str) or str[i+1]!=str[i]:
                compressed=compressed+str[i]+"{0}".format(count)
                count=0
        return compressed
                                                       
sol=Solution()
result=sol.string_compress("aabbbccc")
print(result)
