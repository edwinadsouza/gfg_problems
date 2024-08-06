#User function Template for python3

class Solution:
    def removeConsecutiveCharacter(self, S):
        result = []
        for i in range(len(S)):
            if not result or S[i] != result[-1]:
                result.append(S[i])
        return ''.join(result)

                
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        s = input()
        ob = Solution()
        print(ob.removeConsecutiveCharacter(s))

# } Driver Code Ends