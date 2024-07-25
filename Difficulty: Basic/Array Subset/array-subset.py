#User function Template for python3
#User function Template for python3
def isSubset( a1, a2, n, m):
    d1={}
    for i in a2:
        if i in d1:
            d1[i]+=1
        else:
            d1[i]=1
    for i in a1:
        if i in d1:
            d1[i]-=1
            if d1[i]==0:
                del d1[i]
    if d1:
        return "No"
    else:
        return "Yes"
    
    
    
    


    
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, m = sz[0], sz[1]
        a1 = [int(x) for x in input().strip().split()]
        a2 = [int(x) for x in input().strip().split()]
        
        print(isSubset( a1, a2, n, m))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends