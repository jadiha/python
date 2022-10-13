#Author: Jadiha Aruleswaran
#Date: Nov 27 2020
#Program: TwoNumbers
#What Do I Need To Do: Declare and initialize two variables to hold two different numbers.
#Welcome message for user
print("Welcome! This program provides two numbers and shows you what mathematical solutions can be derived from the specific numbers.")
print('')
#Declare variables
num1 = 3.14
num2 = 6
sum = (float(num1 + num2))
difference = (float(num1 - num2))
product = (float(num1 * num2))
quotient = (float(num1 / num2))
power = (float(num1**num2))

#Show the user the numbers provided
print("The first number is: " + str(num1))
print("The second number is: " + str(num2))

#Output the results of the arithmetic of the two variables
print("")
print ("The sum of the two numbers is: " + str(sum))
print("")
print ("The difference of the two numbers is: " + str(difference))
print("")
print ("The product of the two numbers is: " + str(product))
print("")
print ("The quotient of the two numbers is: " + str(quotient))
print("")
print("The power of the two numbers is: " + str(power))
