class Solution:
    def minRemoval(self, arr):
		
		ln = len(arr)
		
		arr.sort()
		
		
		def bin_search(num):
		    
		    l = 0
		    
		    r = ln-1
		    
		    res = -1
		    
		    
		    while l <=r:
		        
		        m = (l+r)//2
		        
		        tar = arr[m]
		        
		        if tar<=num:
		            
		            l = m+1
		            
		            res = m
		            
		        else:
		            
		            r = m-1
		            
		            
		    return res
		    
		    
		res = float("INF")
		    
		    
		    
		for indl, num in enumerate(arr):
		     
		     
		     indr = bin_search(2*num)
		     
		     res = min(res, ln - (indr-indl+1))
		     
		     
		return res