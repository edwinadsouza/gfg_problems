#User function Template for python3

class Solution:    
    #Complete this function
    def printNos(self,N):
        #Your code here
        self._printNoshelp(1, N)
    def _printNoshelp(self, current: int, N: int) -> None:
        if current > N:
            return
        print(current, end=" ")
        self._printNoshelp(current+1,N)
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math




def main():
    
    T=int(input())
    
    while(T>0):
        
        
        N=int(input())
        
        ob=Solution()
        
        ob.printNos(N)
        print()
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends