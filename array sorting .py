class Solution:
    def isSorted(self, arr) -> bool:
        # code here
        if sorted(arr)==arr:
            return True
        else:
            return False
