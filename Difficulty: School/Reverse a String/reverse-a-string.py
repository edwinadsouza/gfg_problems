#User function Template for python3
class Solution:
    def revStr (self, s : str) -> str :
        return s[::-1]
        # code here 


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        s = input()
        
        ob = Solution()
        print(ob.revStr(s))
# } Driver Code Ends