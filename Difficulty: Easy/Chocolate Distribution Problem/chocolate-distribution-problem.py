#User function Template for python3

class Solution:

    def findMinDiff(self, A,N,M):
        A = sorted(A)
        if (N==0 or M==0):
            return 0
        if (M>N):
            return -1
        diff = A[-1] - A[0]
        for i in range(N-M+1):
            diff = min(diff, A[i+M-1]-A[i])
        return diff

        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        N = int(input())
        A = [int(x) for x in input().split()]
        M = int(input())


        solObj = Solution()

        print(solObj.findMinDiff(A,N,M))
# } Driver Code Ends