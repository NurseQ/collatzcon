# this code is an example of the Collatz conjecture

# n is the number to apply the conjecture on
n = 20

# 1 will be take the program out of the loop
while n != 1:
    print(n)
    # to check if the n is even
    if n % 2 == 0:
        n = n // 2
    
    # if n is not even
    else:
        n = (n * 3) + 1


print(n)       