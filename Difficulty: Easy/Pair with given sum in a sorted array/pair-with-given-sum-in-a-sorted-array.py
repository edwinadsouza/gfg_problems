#User function Template for python3


class Solution:
    def countPair(self,k, arr):
        count = 0
        seen = set()
        for num in arr:
            target = k - num
            if target in seen:
                count += 1
            seen.add(num)
        return count
        #Complete the function



#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    import sys
    input = sys.stdin.read
    data = input().split('\n')

    t = int(data[0].strip())
    index = 1

    for _ in range(t):
        k = int(data[index].strip())
        index += 1
        arr = list(map(int, data[index].strip().split()))
        index += 1

        res = Solution().countPair(k, arr)
        print(res)


if __name__ == "__main__":
    main()

# } Driver Code Ends