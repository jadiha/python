#Author: Jadiha Aruleswaran
#Name of Program: Guess Number
#Purpose of Program: Create a number guessing game that uses repetition.

#Import random module.
import random

#Variable for number of guesses.
num_of_guess = 0

#Welcome statement.
print("Welcome to Guess the Number game! The computer will generate a secret number within the range of your desire. Do you think you can guess it? Continue if you'd like to take up the challenge. ")
print()

#Name input.
name = input("What is your name? ")
print()

#Print name.
print("Welcome " + name + "!")
print()

#Main while loop.
while True:
  #User input for desired range.
  variable1 = int(input("What would you like the minimum number of your range to be? "))
  variable2 = int(input("What would you like the maximum number of your range to be? "))
  #Generate random number within range.
  num = random.randint(variable1,variable2)
  print()
  #Guess the number prompt.
  guess = int(input('Guess what the secret number is from ' + str(variable1) + ' to ' + str(variable2) + ': '))
  #Add 1 to variable to account for number of guesses.
  num_of_guess += 1
  
  #While loop for numbers that do not equal the secret number.
  while guess != num : 
      #If statement if guess is less than secret number.
      if guess < num:
        print("Your guess is low. Try again!")
        print()
        #Re-ask guess the number question.
        guess = int(input('Guess what the secret number is from ' + str(variable1) + ' to ' + str(variable2) + ': '))
         #Add 1 to variable to account for number of guesses.
        num_of_guess += 1

      #Elif statement if guess is higher than secret number.
      elif guess > num:
        print("Your guess is high. Try again!")
        print()
        #Re-ask guess the number question.
        guess = int(input('Guess what the secret number is from ' + str(variable1) + ' to ' + str(variable2) + ': '))
         #Add 1 to variable to account for number of guesses.
        num_of_guess += 1

  print()
  #Congrats output if user guessed the right answer.
  print("Congratulations. You guessed it!")
  #Number of tries output.
  print("It took you " + str(num_of_guess) + " tries!")
  
  #User prompt to play again.
  print()  
  again=str(input("Do you want to play again? Type yes or no: "))
  print()

  #If user enters yes, game will continue.
  if again == "yes":
    continue
  #If user enters yes, game will end.
  else:
    print("Thank you for playing!")
    break
