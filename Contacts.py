#Author: Jadiha Aruleswaran
#Name of Program: ListContacts
#Purpose of Program: Create a program that uses lists that allows user to input, store, and retrieve contact information.

first_name = []
last_name = []
phone_number = []

# While Loop
while True:

  # Define Functions

  # Add function for user to add contacts.
  def add():
    # Prompt user for amount of contacts they would like to add.
    num = input("Enter how many contacts would you like to add (numerical digits only): ")
    print()

    if type(num) != int:
      print("Sorry, please enter a numerical value only. Try again.")
      print()
      num = input("Enter how many contacts would you like to add in numerical digits only: ")
    print()
    
    # Prompt contact info for how many they had wanted to input.
    for i in range (0,int(num)):
          value1 = input("Enter the first name of contact: ")
          value2 = input("Enter the last name of contact: ")
          value3 = input("Enter the phone number of contact: ")
          print()
          #Use append function to add info into lists.
          first_name.append(value1)
          last_name.append(value2)
          phone_number.append(value3)

        # Go to questions function where user will be able to switch between options for what they'd like to do with their contact info.
    question()
  
  # Check function for user to check existing contacts.
  def check():
    # Prompt user to enter first/last name or number of contact.
    person = input("Enter First Name/Last Name/Phone Number: ")
    print()

    # If statement to check if contact inputted exists.
    if person in first_name:
      print("Yes, they are number " + str(first_name.index(person) + 1) + " in your contacts.")
      print()
    elif person in last_name:
      print("Yes, they are number " + str(last_name.index(person) + 1) + " in your contacts.")
      print()
    elif person in phone_number:
      print("Yes, they are number " + str(phone_number.index(person) + 1) + " in your contacts.")
      print()
    # Else user has not inputted info that isn't in stored contact info.
    else:
      print("Sorry, it seems they are not in your contact list.")
      print()

    # Go to questions function where user will be able to switch between options for what they'd like to do with their contact info.
    question()
  
  # Remove function for user to remove contacts.
  def remove():
    # Prompt user for how many contacts they would like to remove.
    remove = input("How many contacts would you like to remove?: ")

    if type(remove) != int:
      print("Sorry, please enter a numerical value only. Try again.")
      print()
      remove = input("How many contacts would you like to remove?: ")
    print()

    # For loop to make sure to remove contact info for as many user has indicated.
    for i in range (0,remove):
      print()
      person_remove= input("Enter the first name of contact you would like to remove: ")
      print()

      # If statement whether contact inputted is in stored contact info.
      if person_remove in first_name:
        # Retrieve index of first name inputted and use index to remove info in other two lists.
        index_remove = first_name.index(person_remove)
        first_name.pop(index_remove)
        last_name.pop(index_remove)
        phone_number.pop(index_remove)
        # Print revised list after removal of contacts.
        print("You're revised contact list is..")
        print(first_name)
        print(last_name)
        print(phone_number)
        print()
      else:
       print("Sorry, it seems what you have inputted is not in our list.")

    # Go to questions function where user will be able to switch between options for what they'd like to do with their contact info.
    question()
    
  #Output function for user to see their contacts.
  def output():
    print(first_name)
    print(last_name)
    print(phone_number)
    print()
    
    # Go to questions function where user will be able to switch between options for what they'd like to do with their contact info.
    question()

  # Sort function for user to output names alphabetically.
  def sort():
    # Prompt user for if they would like to sort first/last name. 
    sort_name = input("Would you like to see the sorted alphabetical list for first/last name?: (first/last) ")
    print()

    #Within if statments, original list has been copied and outputed with sort function.
    if sort_name == 'first':
      first_name2 = []
      first_name2 = first_name.copy()
      first_name2.sort()
      print(first_name2)
      print()
    elif sort_name == 'last':
      last_name2 = []
      last_name2 = last_name.copy()
      last_name2.sort()
      print(last_name2)
      print()

    # Go to questions function where user will be able to switch between options for what they'd like to do with their contact info.
    question()
  
  #Question function that prompts for user to chose what they would like to do with their contacts.
  def question():
    name = input('Would you like to..\nOutput all contact information (enter "O")\nCheck whether a name has been inputted (enter "C")\nAdd new contact information (enter "A")\nRemove existing contact information (enter "R")\nSort contacts in alphabetical order (enter "S")\nIf you are satisfied, enter 0 to end program: ').lower()
    print()
    if name == 'c':
      check()
    elif name == 'o':
      output()
    elif name == 'a':
      add()
    elif name == 'r':
      remove()
    elif name == 's':
      sort()
    elif name == '0':
      print("Thank you for using this program. Have a great day!")
    else:
      print("You have entered an invalid entry.")
    
  #Main Program

  #User Introduction
  print("Welcome! In this program, you are able to store your contacts information by First Name, Last Name and Phone Number.")
  print()
  #Ask user whether they would like to continue with program.
  person = input("Would you like to enter contacts information?: (yes/no) ").lower()
  print()
  if person == "yes":
    add()
  #If answer is anything other than yes, program ends.
  else:
    print("Sorry, it is not possible to do anything else without initial input. Have a good day! ")
  break
    