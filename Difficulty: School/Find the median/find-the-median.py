#User function Template for python3

class Solution:
	def find_median(self, v):
	    v.sort()
	    n = len(v)
	    mid = n//2
	    
	    if n % 2 == 0:
	        return (v[mid - 1] + v[mid])//2
	    else:
	        return (v[mid])
	       
	    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		v = list(map(int,input().split())) 
		ob = Solution();
		ans = ob.find_median(v)
		print(ans)
# } Driver Code Ends