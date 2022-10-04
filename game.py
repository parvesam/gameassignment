import role1, role2

# Setup
yes_no = ["yes", "no"]
char1 = "role 1"
char2 = "role 2"
directions = ["left", "right", "forward", "backward"]

#Introduction
name= input("What is your name? ")
print("Welcome, " + name + ". Let's go solve a mystery game!")
print("You are a detective solving a murder case.")
print("Can you solve this murder mystery and identify the criminal?")

#Start of the game
roll = input("Which character would you like to choose? Role 1: Detective Grace or Role 2: Detective Mike? Please choose role 1 or role 2. " )
print("one morning you wake up on the ringing of your phone.")
print("you get up to see who's calling and see that it is Detective Albert.")
print("you pick up the call and he asks you to reach immediately to the crime spot.")
print("you leave the house all dressed up and get into your car.")
print("you are driving to the crime spot. Upon approach you see a few people trying to look inside the house to see what's happeining inside.")
print("you get inside the house and see that there is a dead body laying on the floor and it looks like it was hit by an axe.")
print("you are searching the house to see if you can find any evidence that could lead you to the criminal.")
print("you enter into a room and notice that the wall has something written on it.")
print("it looks like a riddle.")

#challenge no.1
name1 = input ("I have two bodies joined together as one. When standing still, I ran and ran. What am I?")
print ("Hint: it is something you see on the table, it sometimes holds your papers from flying away when the windows are open on a windy day.")
answer = hourglass
Tries = 3 
while Tries > 0: 
    Tries = Tries - 1 
    if question : answer
    print(“Yay!”)
    else: 
          print(“So sad! You are not ready for the mystery.”)
print("you find the hourglass on top of the table.")
print("you go near the table and catch your eyes on a letter underneath the hourglass.")
print("you open the letter and see that it is a map showing you directions to a place you have never been before.")

#challenge no.2
response = ""
while response not in directions:
    print("To your left, you see a bear.")
    print("To your right, there is more forest.")
    print("There is a rock wall directly in front of you.")
    print("Behind you is the forest exit.\n")
    response = input("What direction do you move?\nleft/right/forward/backward\n")
    if response == "left":
        print("The bear eats you. Farewell, " + name + ".")
        quit()
    elif response == "right":
        print("You head deeper into the forest.\n")
    elif response == "forward":
        print("You cannot scale the wall.\n")
        response = "" 
    elif response == "backward":
        print("You leave the forest. Goodbye, " + name + ".")
        quit()
    else:
        print("I didn't understand that.\n")

#challenge no.3
print("you see there was something inside the ground so you start digging.")
print("you found an axe in the ground near the tree with blood on it and a t-shirt with blood stains on it.")
print("you look around and you see a small house near by.")
print("you walk towards it and peek inside the window.")
print("you see someone's shadow.")
response = ""
while response not in yes_no:
    response = input("Would you like to enter inside the house?\nyes/no\n")
    if response == "yes":
        print("You enter into the house, catch the criminal, send the criminal to jail and you got promoted.\n")
    elif response == "no":
        print("You are not ready for this mystery case. Goodbye, " + name + ".")
        quit()
    else: 
        print("I didn't understand that.\n")
