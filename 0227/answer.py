# Q1:
class Solution:
    def game(self, guess: List[int], answer: List[int]) -> int:
        # return sum(guess[i]==answer[i] for i in range(len(guess)))
        sum = 0
        for i in range(len(guess)):
            if guess[i] == answer[i]:
                sum += 1
        return sum


# Q2:
class Solution:
    def minCount(self, coins: List[int]) -> int:
        sum = 0
        for i in coins:
            if (i % 2 != 0):
                sum += int(i / 2) + 1
            else:
                sum += int(i / 2)
        return sum


# Q3：
def leap(x, y):
    m = input()
    m = m.split(' ')
    x = int(m[0])
    y = int(m[1])
    count = 0
    result = []
    for i in range(x, y + 1):
        if (i % 4 == 0 and i % 100 != 0) or i % 400 == 0:
            count += 1
            result.append(i)

    print(count)
    s = ''
    for j in result:
        s = s + str(j) + ' '

    print(s)

#Q4:

m=input()
m=m.split(" ")
a=m.index('0')
n=m[0:a]
n.reverse()
l=''
for i in n:
    l+=i+' '
print(l)

#Q5:
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cost, profit = float("+inf"), 0
        for price in prices:
            cost = min(cost, price)
            profit = max(profit, price - cost)
        return profit
