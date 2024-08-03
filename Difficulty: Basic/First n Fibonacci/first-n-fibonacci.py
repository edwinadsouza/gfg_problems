#User function Template for python3

class Solution:
    # Function to return list containing first n Fibonacci numbers.
    def printFibb(self, n):
        fib_list = []
        a, b = 0, 1
        
        for i in range(n):
            fib_list.append(b)
            a, b = b, a + b
        
        return fib_list

        # your code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__': 
    t=int(input())
    for tcs in range(t):
        
        n=int(input())
        res = Solution().printFibb(n)
        for i in range (len(res)):
            print (res[i], end = " ") 
        print()
# } Driver Code Ends