num = int(input("Enter a number: "))
isPrime = True

if num <= 1:
    isPrime = False

for i in range(2, num):
    if num % i == 0:
        isPrime = False
        break

if isPrime:
    print(f"{num} is a prime number")
else:
    print(f"{num} is a not prime number")
