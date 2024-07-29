#User function Template for python3
class Solution:
    def getPairsCount(self, arr, sum):
        d = {}
        count = 0
        for num in arr:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1

        for num in arr:
            x = sum - num
            if x in d:
                count += d[x]
              
                if x == num:
                    count -= 1

        return count // 2





#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input().strip())

    while tc > 0:
        k = int(input().strip())
        arr = list(map(int, input().strip().split()))

        ob = Solution()
        ans = ob.getPairsCount(arr, k)
        print(ans)

        tc -= 1

# } Driver Code Ends