
class Solution:
    def seriesSum(self, n : int) -> int:
        if n == 0:
            return 0
        elif n ==1:
            return 1
        else:
            sum = (n*(n+1)//2)
            return sum
        # code here
        



#{ 
 # Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        n = int(input())

        obj = Solution()
        res = obj.seriesSum(n)

        print(res)

# } Driver Code Ends