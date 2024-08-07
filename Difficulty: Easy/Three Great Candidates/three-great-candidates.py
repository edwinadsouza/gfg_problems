#User function Template for python3
class Solution:
    def maxProduct(self, arr):
        # Sort the array in ascending order
        arr = sorted(arr)
        
        # Calculate the maximum product of three numbers
        # 1. Product of the three largest numbers
        # 2. Product of the two smallest (most negative) numbers and the largest number
        return max(
            arr[-1] * arr[-2] * arr[-3],  # Product of the three largest numbers
            arr[0] * arr[1] * arr[-1]     # Product of two smallest and the largest number
        )


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.maxProduct(arr)
        print(ans)
        tc -= 1
# } Driver Code Ends