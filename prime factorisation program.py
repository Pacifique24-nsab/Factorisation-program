#welcome to the program of generating all prime number between 2 and n
import time( to know how much time was spent to process the program)

# welcome message from the user ( as a starting message)
print("Welcome to the prime factorization program  made by pacifique!!!")

# define a function that takes a number and returns its prime factors.
def get_prime_factors(num):
    factors = []  # create an empty list to store the factors
    divisor = 2   # start with the first divisor, which is 2
    while divisor <= num**((0.5)+1):   # loop until the divisor is greater than the number of our user
        if num % divisor == 0:  # if the number is divisible by the divisor,
            factors.append(divisor) # add the divisor to the list of factors
            num = num / divisor   # divide the number that we get by the divisor again
        else:
            divisor += 1 # if the number is not divisible by the divisor, try the next divisor
   
    return factors # return the list of factors

# function to check if a number is prime or not prime number
def is_prime(num):
    if num < 2:  # if the number is less than 2, it's not prime
        return False
    #create a new condition which doesn't use the square root of the user input
    for i in range(2, int(num**(0.5))+1):  # loop through all possible divisors of the number
        if num % i == 0:  # if the number is divisible by the divisor,
            return False  # it's not prime 
          
    return True  # otherwise, it's prime

# ask the user to enter a number( which is an integer and that can support float numbers)
num = int(input("Enter an integer greater than 1: "))

# start counting the time
time1 = time.time()

# find all prime factors of the given number using the get_prime_factors function
factors = get_prime_factors(num)


# print the list of prime factors of the given number
print("The prime factors of", num, "are:", factors)

# print all prime numbers between 2 and the user-input number as a list
prime_numbers = []#create an empty list to store all the prime numbers

for i in range(2, num+1): # the for loop that check if the divisors i are in the range of between 2 and the number
    if is_prime(i): # if it founds the number i(divisor) is a prime  number
        prime_numbers.append(i) #add the divisor to the list of prime numbers

print("All prime numbers between 2 and", num, "are:", prime_numbers)

# stop counting the time
time2 = time.time()

# print the time taken by the program to calculate the list of prime factors
print("Time taken:", time2 - time1 , "seconds")


