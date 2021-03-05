#question1
def equals(word1,word2):
    word3=''
    word4=''
    for i in range(len((word1))):
        word3+=word1[i]
        # word4+=word2[i]
    for i in range(len((word2))):
        word4+=word2[i]
    return word3==word4

print(equals(["ab", "c"],["abc"]))

#question2
def cal(n):
    result=0
    for i in range(1,n+1):
        result+=i
    return result

    # return n*(n+1)//2
print(cal(100))

#question3
def steps(x):
    step=1
    distance=0
    while(1):
        distance+=(2*(0.98**(step-1)))
        if distance<x:
            step+=1
        else:
            break
    return step
print(steps(2.1))
