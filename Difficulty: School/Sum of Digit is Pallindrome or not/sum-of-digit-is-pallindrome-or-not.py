#User function Template for python3
class Solution:
    def isDigitSumPalindrome(self, n):
        digit_sum = sum(int(digit) for digit in str(n))
        digit_sum_str = str(digit_sum)
        if digit_sum_str == digit_sum_str[::-1]:
            return 1
        else:
            return 0



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        ob=Solution()
        print(ob.isDigitSumPalindrome(N))
# } Driver Code Ends