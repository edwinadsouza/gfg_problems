#User function Template for python3
class Solution:
	def _sum(self,arr):
	    add=0
	    for i in arr:
	        add = add+i
	    return add
   		# code here



#{ 
 # Driver Code Starts
# Driver code
if __name__ == "__main__":
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob._sum(arr)
        print(ans)
        tc = tc - 1

# } Driver Code Ends