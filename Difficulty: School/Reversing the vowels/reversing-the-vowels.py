#User function Template for python3
class Solution:
    def modify(self, s):
        vow = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        s = list(s)
        left, right = 0, len(s) - 1
        
        while left < right:
            if s[left] not in vow:
                left += 1
            elif s[right] not in vow:
                right -= 1
            else:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        
        return ''.join(s)

        
        
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        ans = ob.modify(s)
        print(ans)
# } Driver Code Ends