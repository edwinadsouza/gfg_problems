class Solution:
    def nthFibonacci(self, n: int) -> int:
        MOD = 10**9 + 7
        a, b = 0, 1
        for _ in range(n - 1):
            a, b = b, (a + b) % MOD
        return b



#{ 
 # Driver Code Starts
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        obj = Solution()
        res = obj.nthFibonacci(n)
        
        print(res)
        

# } Driver Code Ends