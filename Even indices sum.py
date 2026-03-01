class Solution:
    def EvenOddSum(self,N,Arr):
        even = 0
        odd = 0
        for i in range (0,N,2):
            even += Arr[i]
        for j in range(1,N,2):
            odd += Arr[j]
        return [even, odd] 

