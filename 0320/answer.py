

def query(startTime,endTime,query):
    sum=0
    for i in range(len(startTime)):
        if query>=startTime[i] and query<=endTime[i]:
            sum+=1
    return sum


def swap(a,b):
    a=a+b
    b=a-b
    a=a-b
    print(a)
    print(b)
swap(2,4)