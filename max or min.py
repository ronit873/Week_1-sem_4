class Solution:
    def getMinMax(self, arr):
        arr.sort()
        a = len(arr)-1
        return arr[0],arr[a]