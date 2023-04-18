def sum(n):
    if n==1:
        return 0
    else:
        return sum(pow((n-1), 2))+pow(n, 2)
sum(int(input("Enter the value of n: ")))                