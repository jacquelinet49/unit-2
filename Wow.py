#Sum of First n Natural Numbers
n = int(input("Enter the value of n:"))
sum = 0
#We will add n to sum so it needs to be set as 0
#Our while loop must run until n becomes 0
while n>0:
    sum += n
    #5 is added to sum value
    n -= 1
    #n decreases by 1 which means 4 is added to sum value
    #n eventually becomes 0 while sum becomes 15
print(sum)

#Infinite while loop
n = 100
while True:
    print(n)
    n-=1

while True:
    line = input("Enter the line(type "q" to quit): ")
    if line == q:
        break