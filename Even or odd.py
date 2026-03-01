class Solution:
    def countOddEven(self, arr):
        even = len([ele for ele in arr if ele % 2 == 0])
        odd = len(arr) - even
        
        return odd, even