#A prime number is a natural number greater than 1 that cannot be formed by multiplying two smaller natural numbers. A prime number is only divisible by 1 and itself. The first few prime numbers are 2, 3, 5, 7, 11, 13, 17, 19, 23, and so on.
#So prime number can only be formed by multiplying 1 and itself.

num=int(input("Enter a number: "))
if num<1:
    print("Please enter a number greater than 1")
elif num > 1:
    for i in range(2,num):
        if (num % i) == 0:
            print(num,"is not a prime number")
            break
    else:
        print(num,"is a prime number")