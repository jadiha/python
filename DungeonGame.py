room_list = []
current_room = 0 
done= False
print("*****")
print('WELCOME TO THE DUNGEON')
print('*****')
room = ["\nYou are currently in BEDROOM 2. You may move to the North or East.\n",3,1,None,None]
room_list.append(room)
room = ["\nYou are currently in the SOUTH HALL. You may move to the North, East, or West.\n",4,2,None,0]
room_list.append(room)
room = ["\nYou are currently in the DINING ROOM. You may move th the North or West.\n",5,None,None,1]
room_list.append(room)
room = ["\nYou are currently in BEDROOM 1. You may move to the East or South.\n",None,4,0,None]
room_list.append(room)
room = ["\nYou are currently in the NORTH HALL. You may move to the North, East, South, or West.\n",6,5,1,3]
room_list.append(room)
room = ["\nYou are currently in the KITCHEN. You may move to the South or West.\n",None,None,2,4]
room_list.append(room)
room = ["\nYou are currently on the BALCONY. You may move to the South.\n",None,None,4,None]
room_list.append(room)
print()
while done == False:
    print(room_list[current_room][0]) 
    print ("If you would ever like to quit, please enter R.")
    user_input=input ("Where would you like to move next? Please enter N(North), E(East), S(South), or W(West): ")
    print()
    if user_input.lower()=="n" or user_input.lower()== "north":
        next_room=room_list[current_room][1]
        if next_room ==None:
             print("\nYou cannot go that way.")
        else: 
            current_room=next_room
    elif user_input.lower()=="e" or user_input.lower()== "east":
        next_room=room_list[current_room][2]
        if next_room==None:
             print("You cannot go that way.")
        else:
            current_room=next_room
    elif user_input.lower()=="s" or user_input.lower()== "south":
        next_room=room_list[current_room][3]
        if next_room==None:
             print("You cannot go that way.")
        else:
            current_room=next_room
    elif user_input.lower()=="w" or user_input.lower()== "west":
        next_room=room_list[current_room][4]
        if next_room==None:
             print("You cannot go that way.")
        else:
            current_room=next_room
    elif user_input.lower()=="r":
        print("Thank you for playing!")
        break
    else:
        print("Please do not enter anything else but N, E, S, W.")
    








