class Solution:
def preGreaterEle(self, arr):
ans = []
s = []
l = len(arr)
for i in range(l):
    if len(s) == 0:
        ans.append(-1)
    elif s[-1] > arr[i]:
        ans.append(s[-1])
    else:
        while len(s) > 0 and s[-1] <= arr[i]:
            s.pop()
        if len(s) == 0:
            ans.append(-1)
        else:
            ans.append(s[-1])
    s.append(arr[i])
    return ans