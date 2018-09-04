class Solution:
    def string_edit(self, str1, str2):
        if str1==str2:
            return True
        len1 = len(str1)
        len2 = len(str2)
        if len1 == len2:
            diff = 0
            for i in range(0,len1):
                if str1[i] != str2[i]:
                    if diff == 1:
                        return False
                    diff = 1
            return True
        elif abs(len1-len2)==1:
            if len1<len2:
                str1,str2=str2,str1
            i,j = 0,0
            while i<len1 and j<len2:
                if str1[i]!=str2[j]:
                    if i!=j:
                        return False
                    i=i+1
                else:
                    i=i+1
                    j=j+1
            return True
        return False
                  
                            
sol=Solution()
result=sol.string_edit("pale","bake")
print(result)