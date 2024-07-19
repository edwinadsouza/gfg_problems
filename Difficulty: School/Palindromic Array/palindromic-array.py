# Your task is to complete this function
# Function should return true/false
def PalinArray(arr):
    def isPalindrome(s: str) -> bool:
        return s == s[::-1]

    for num in arr:
        if not isPalindrome(str(num)):
            return False
    return True



#{ 
 # Driver Code Starts
# Driver Program
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        arr = list(map(int, input().strip().split()))
        if PalinArray(arr):
            print("true")
        else:
            print("false")
# Contributed By: Harshit Sidhwa

# } Driver Code Ends