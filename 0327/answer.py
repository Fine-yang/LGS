
def numWays(n):
    if n==1 or n==0:
        return 1
    else:
        return numWays(n-1)+numWays(n-2)

print(numWays(5))