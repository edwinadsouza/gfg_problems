class Solution:
    def segregateElements(self, arr):
        positive = []
        negative = []
        
        for num in arr:
            if num >= 0:
                positive.append(num)
            else:
                negative.append(num)
        
        # Combine positive and negative lists
        arr[:] = positive + negative



#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while (T > 0):
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        ob.segregateElements(a)
        print(*a)

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends