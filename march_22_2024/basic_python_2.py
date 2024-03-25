# You may uncomment print lines below to observe what's going on step by step

"""
TR 1 - İlk iki elemanı 1'e eşit olan, en az 20 elemanlı bir fibonacci serisini liste halinde oluşturan döngü yazalım.
***
EN 1 - Write a loop that generates a fibonacci series of at least 20 elements with the first two elements equal to 1 as a list.
*****
"""

# The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones. 

def fibonacci(n):

    while n < 22:
        n = int(input("\nPlease enter a minimum value of 22: "))

    a, b = 1, 1

    fibonacci_list = [a, b]

    for i in range(n - 2):
        a, b = b, a + b
        fibonacci_list.append(b)

    return fibonacci_list

n = int(input("\nEnter the number for Fibonacci numbers list (minimum 22): "))
fibonacci_list = fibonacci(n)
print(f"\nFibonacci numbers: {fibonacci_list}\n")



"""
TR 2 - Kullanıcıdan aldığı sayının mükemmel olup olmadığını söyleyen bir program yazınız.
***
EN 2 - Write a program that tells whether the number received from the user is perfect or not.
*****
"""

"""
In number theory, a perfect number is a positive integer that's special because it's equal to the sum of its positive divisors, excluding the number itself.
"""
def is_perfect_number(n):
    sum_of_divisors = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            #print("divisor (i): ", i)
            sum_of_divisors += i + n // i
            #print("sum: ", sum_of_divisors)
    return sum_of_divisors == n

number = int(input("\nPlease enter a number: "))

if is_perfect_number(number):
    print(f"\nExcellent! {number} is a perfect number.\n")
else:
    print(f"\nSorry! {number} is not a perfect number.\n")



"""
TR 3 - Kullanıcıdan girilen sayının EBOB ve EKOK'unu bulan programı yazınız.
***
EN 3 - Write a program that finds the EBOB and EKOK of the number entered from the user.
*****
"""

def gcd(a, b):
    while b:
        #print (f"\n a, b: {a}, {b} \n")
        a, b = b, a % b
        #print("a: ", a)
        #print("b: ", b)
        #print("***************\n")
    return a

def lcm(a, b):
    #print("a x b: ", a * b)
    return (a * b) // gcd(a, b)


a = int(input("\n first_number: "))
b = int(input("\n second_number: ")) 


print(f"\ngcd({a}, {b}) = {gcd(a, b)}\n")
print(f"\nlcm({a}, {b}) = {lcm(a, b)}\n")



"""
TR 4 - Kullanıcıdan girilen sayının asal sayı olup olmadığını söyleyen bir program yazınız.
***
EN 4 - Write a program that tells whether the number entered from the user is a prime number or not.
*****
"""

print("\n ***Reminder: 1 is not a prime number...\n")
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

number = int(input("\nPlease enter a number: "))

if is_prime(number):
    print(f"\n{number} is a prime number.\n")
else:
    print(f"\n{number} is not a prime number.\n")



"""
TR 5 - Kullanıcıdan girilen sayının asal çarpanlarını bulan bir program yazınız.
***
EN 5 - Write a program that finds the prime factors of the number entered from the user.
*****
"""

def prime_factors(n):
    prime_factors_list = []
    for i in range(2, int(n ** 0.5) + 1):
        while n % i == 0:
            if i not in prime_factors_list:  # Check if i is not already in the list
                prime_factors_list.append(i)
            n //= i
    if n > 1 and n not in prime_factors_list:  # Check if the remaining factor is not already in the list
        prime_factors_list.append(n)
    return prime_factors_list

n = int(input("\nPlease enter a number\nto see its prime factors: "))
print("\nRemember 1 will never appear...\n")
print(f"Prime factors of {n}: {prime_factors(n)}\n")