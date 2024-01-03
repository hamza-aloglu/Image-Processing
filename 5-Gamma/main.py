# Python code to demonstrate
# factorial() vs gamma()
import math
import time

# initializing argument
gamma_var = 6

# checking performance
# gamma() vs factorial()
start_fact = time.time()
res_fact = math.factorial(gamma_var - 1)

print("The gamma value using factorial is : "
      + str(res_fact))

print("The time taken to compute is : "
      + str(time.time() - start_fact))

print('\n')

start_gamma = time.time()
res_gamma = math.gamma(gamma_var)

print("The gamma value using gamma() is : "
      + str(res_gamma))

print("The time taken to compute is : "
      + str(time.time() - start_gamma))