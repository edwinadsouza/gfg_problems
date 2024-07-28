#User function Template for python3

class Solution:
	def reverse_digit(self, n):
	    reversed_num = 0
        
        while n > 0:
            reversed_num = reversed_num * 10 + n % 10
            n = n // 10
        return reversed_num
	    
		# Code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.reverse_digit(n)
		print(ans)
# } Driver Code Ends