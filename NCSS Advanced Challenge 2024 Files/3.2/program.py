import math

def is_prime(x):
  for i in range(2, x):
    print(f"Checking if {x} is evenly divisible by {i}")
    if x % i == 0:
      return False
  return True

num = int(input("Enter the number: "))
if is_prime(num):
  print(f"{num} is a prime number.")
else:
  print(f"{num} is not a prime number.")
