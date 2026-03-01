class Solution:
    def checkEqual(self, a, b) -> bool:
        #code here
        f={}
        for i in a:
            f[i]=f.get(i,0)+1
        for i in b:
            if i not in f or f[i]==0:
                return False
            f[i]-=1
        return True
