#User function Template for python3

class Solution:    
    #Function to return the count of number of elements in union of two arrays.
    def doUnion(self,arr1,arr2):
        s1=set(arr1)
        s2=set(arr2)
        result = s1.union(s2)
        count = 0
        for i in result:
            count+=1
        return count
        #code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]
        ob = Solution()

        print(ob.doUnion(a, b))

# } Driver Code Ends