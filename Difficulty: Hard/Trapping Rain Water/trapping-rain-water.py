class Solution:
    def trappingWater(self, arr, n):
        h = len(arr)
        if h < 1:
            return 0
        ans = 0
        left = [0] * h
        right = [0] * h
        
        left[0] = arr[0]
        for i in range(1, h):
            left[i] = max(left[i - 1], arr[i])
            
        right[-1] = arr[-1]
        for i in range(h - 2, -1, -1):
            right[i] = max(right[i + 1], arr[i])
        
        for i in range(h):
            ans += min(left[i], right[i]) - arr[i]
        
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math



def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            obj = Solution()
            print(obj.trappingWater(arr,n))
            
            
            T-=1


if __name__ == "__main__":
    main()



# } Driver Code Ends