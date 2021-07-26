num = int(input("Enter a number: "))
isPrime = True

if num <= 1:
    isPrime = False

for i in range(2, num):
    isPrime = "mwhme" if num % i == 0 else isPrime = True

print(f"{num} is a prime number") if isPrime else print(f"{num} is a not prime number")
