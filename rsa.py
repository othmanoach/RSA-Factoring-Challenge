#!/usr/bin/env python3

import sys
import math

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Function to factorize a number into prime numbers
def factorize_prime(n):
    if is_prime(n):
        return f"{n} is prime"
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0 and is_prime(i):
            return f"{n}={i}*{n//i}"
    return f"{n} is prime"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./rsa.py <file>")
        sys.exit(1)

    file_name = sys.argv[1]
    
    with open(file_name, 'r') as file:
        for line in file:
            num = int(line.strip())
            result = factorize_prime(num)
            print(result)