T = int(input("Enter a number :"))
numbers = []
for i in range(0,T):
    n = int(input())
    temp = 0
    for j in range(T):
        temp = temp + (n%10)
        n = int(n/10)
    numbers.append(temp)
for k in range(T):
    print(numbers[k])