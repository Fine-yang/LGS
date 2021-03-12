def getNum(J, S):
    # return sum([S.count(x) for x in J])
    output = 0
    for s in S:
        if s in J:
            output += 1

    return output

def good(nums):
    sum=0
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            if nums[i]==nums[j] and i<=j:
                sum+=1
    return sum

# print(good([1,1,1,1]))

def leftRotate(s,k):
    a=s[0:k]
    b=s[k:]
    return b+a

print(leftRotate("dafdas",3))