#User function Template for python3

def isValid(s):
    parts = s.split('.')
    if len(parts) !=4:
        return False
    for part in parts:
        if not part.isdigit() or not 0 <= int(part) <= 255 or (part[0]=='0' and len(part)>1):
            return False
    return True
        
    
    #code here



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        s = input()
        if (isValid(s)):
            print("true")
        else:
            print("false")

# } Driver Code Ends