'''
--- Property of Queen's University --- 
This is a simple text-based adventure game that was created for a CISC 101 - Intro to Programming assignment at Queen's University. 
It is a text based adventure game that asks users a series of questions and poses several choices they must make in order to 'play'
along. The game primarily uses if and else statements to accomplish this. Each location is a different function that is called when a user
makes a choice.

Author: Hana Chaudhury 
'''

#this function describes the choice made in the Great Hall where the user starts
def GreatHall():
    
    #welcomes the user to the program, situates them and asks them to make their first choice 
    print("\nWelcome to Hogwarts! You are currently in the Great Hall. On your left")
    print("you see a group of students with red scarves heading down the hallway,")
    print("and on your right is a group of students with green scarves heading the")
    print("other way. Which way would you like to go?")

    #variable defines the first chocie that the user must make to go forward 
    choice_first = input("\nEnter 'L' to go left or 'R' to go right: ")

    #if the user goes left they will enter the Gryffindor Common Room defined by the GCommonRoom() function
    #this if statement calls the Gryffindor Common Room function
    if choice_first == 'L':
        GCommonRoom()
        
    #assumes the user enters the correct input
    #they are directed to the Slytherin Common Room if they go right

    else: 
        SCommonRoom()

'''
These are the functions from the first main branch from the user's first choice.
Some functions are repeated in the second branch.
'''

#function for the Gryffindor Common Room
def GCommonRoom():
    
    #orients user to location 
    print("\nTurns out you followed the Gryffindors to their Common Room. They're ")
    print("going to the  Defense Against the Dark Arts classroom or the")
    print("Transfiguration classroom. Where would you like to go?")
    
    #choice_classroom represents the variable name for choosing which class to go to 
    choice_two = input("\nEnter D for the DADA classroom or T for Transfiguration: ")

    #if user inputs D they go to the Defense Against the Dark Arts classroom 
    if choice_two == 'D':
        DADAClass()

    #if user inputs anything else they go to the Transfiguration classroom
    else:
        TransfigurationClass()

'''
First branch from Gryffindor Common Room 
'''

#the user enters the Defense Against the Dark Arts classroom
        
def DADAClass():

    #prints statement for the user to orient them 
    print("\nYou chose to go to the DADA classroom. You explore and find all sorts")
    print("of artifacts and then have the living daylights scared out of you by Peeves.")
    print("You decide to leave. You step outside and see a tall tower you can go up")
    print("to or large doors leading to the courtyard. Where would you like to go?")

    #this is the last choice the user will face in this branch 
    choice_last = input("\nEnter T for the tower or C to go to the courtyard: ")

    #if they enter T they are directed to the tower --- the tower function is called 
    if choice_last == 'T': 
        Tower()

    #if they enter C they go to the courtyard --- the courtyard function is called 
    else:
        Courtyard()
        
#the following 2 functions are the last choices from DADA class
#both of these choices are later referenced in the second main branch 

#function for the tower -- this function is used twice in the program
def Tower():
    
    print("\nWelcome to the Astronomy tower --- you've found one of the most special places")
    print("at Hogwarts. A popular haunt for students looking for some quiet time.")
    print("You admire the view and decide to call it a day, having had enough")
    print("adventure for the day.")

#function for the courtyard -- this function is used twice in the program
def Courtyard():
    
    print("\nWelcome to the courtyard. Here you meet some fellow students playing")
    print("a game of pick-up Quidditch. You make some new friends and decide")
    print("you've had enough adventure for the day and decided to stay outside")
    print("with your new friends.")
    
    
'''
Second branch from Gryffindor Common Room
'''


#the transfiguration function is the second choice the user could make from the Gryffindor Common Room
def TransfigurationClass():
    
    print("\nYou enter the Transfiguration classroom and run into Professor McGonagall who")
    print("turns you into a rabbit for fun. Traumatized, you decide to go far far away.")
    print("You spot Hagrid who invites you to tea in his cottage, but your friend wants")
    print("you to go with her to find the kitchens. Where do you want to go?")

    #this is last choice they face in this branch 
    choice_last = input("\nPlease enter H for Hagrid's cottage or K for the kitchen: ")

    #if user inputs H then the user is directed to Hagrid's cottage  
    if choice_last == 'H':
        HagridsCottage()

    #if user enters K (or anything else) they are directed to the kitchen 
    else:
        Kitchen()    

#the next two functions lead to the user's final destination in this branch
        
#function for Hagrid's cottage 
def HagridsCottage():
    
    print("\nYou follow Hagrid to his cottage and enjoy a nice, if slightly odd smelling")
    print("concoction. Hagrid shows you some questionable pictures of his so-called")
    print("pets who he claims are kind. You decide to say goodbye and return to the")
    print("common room before Hagrid tries to invite you into the Forbidden Forest.")


#function for the kitchen 
def Kitchen():
    
    print("\nYou successfully find the kitchen! The house elves are delighted with their")
    print("new visitors and give you and your friend more than enough food for three days.")
    print("You decide to stay in the kitchen and get an early dinner.")
    
    
'''
This is the second main branch leading from the user's first choice to go left or right. 
'''


#this is the function that gets called if the user goes right in their first decision 
def SCommonRoom():
    
    #orients the user to their location 
    print("\nYou followed the Slytherins to their Common Room. Half are going to visit the Potions dungeon",
              "the other half are going to see the Herbology greenhouses. Where do you want to go?")

    #asks the user to input a letter to indicate where they want to go 
    choice_two = input("\nPlease enter P for the Potions dungeon or H for the greenhouses: ")

    #this is the second choice that the user faces in this branch
    #if they choose P the Potions dungeon function is called 
    if choice_two == 'P':
        PotionsDungeon()

    #otherwise the herbology greenhouse function is called 
    else:
        HerbologyGreenhouses()

'''
This is the first branch from the Slytherin Common Room
'''
#function if user enters the Potions dungeon 
def PotionsDungeon():
    
    print("\nYou decide to brave the Potions dungeon ... which ends up being a poor life choice")
    print("as you run into the terrifyingly greasy Professor Snape who ends up taking 10 points")
    print("from your house for loitering. You decide it's time to leave before you end up poisoned.")
    print("You can go up the stairs to your left or open the oddly shaped door ahead of you.")

    #this is the last choice the user will face in this branch and the variable is named as such
    choice_last = input("\nEnter S to go up the stairs or D to open the doors: ")

    #uses if function to lead the user to the tower if they go up the stairs
    #reuses the tower function if they choose to go up the stairs 
    if choice_last == 'S':
        Tower()

    #calls the room of requirement function if user opens the doors 
    else:
        RoomofRequirement() 

#this is unique to the Slytherin common room branch if user goes chooses to open the doors
def RoomofRequirement():

    #prints the last statement for the user signifying its the end! 
    print("Congratulations! You found one of the most sacred and secret places at Hogwarts!")
    print("This is the Room of Requirement - it appears in times of need for worthy students.")
    print("Inside is a warm library with a roaring fire. You decide to stay and read a book.")

'''
This is the second branch from the Slytherin Common Room
'''

#this function executes if user chooses H from Slytherin Common Room 
def HerbologyGreenhouses():

    #prints the last statement for the user signifying its the end! 
    print("\nYou decide to opt for the warm and airy greenhouses and run into a group of")
    print("Hufflepuffs who are more than happy to show you around the greenhouse.")
    print("Unfortunately you nearly burst your eardrums when a fellow student")
    print("decides to pull on a mandrake. Traumatized, you decide you need to leave.")

    #this is the last choice and the variable name is named as such 
    choice_last = input("\nEnter I to go to the Infirmary or C to go to the Courtyard.")

    #if the user inputs I the infirmary function is called 
    if choice_last == 'I':
        Infirmary()
        
    #courtyard function is called again if they choose C 
    else:
        Courtyard()

#this function is unique to the greenhouse and executes if user chooses to go to infirmary from greenhouse
def Infirmary():
    
    #prints the last statement for the user signifying its the end! 
    print("\nYou meet Madame Pomfrey at the doors of the infirmary and she seems to know")
    print("what has happened before you even say anything. She gives you a small vial")
    print("and tells you to rest on the bed. You follow her advice and fall right asleep.")


'''
This is the main function that calls the first location function and thanks the player for playing.
'''

def main():
    GreatHall()

    #thanks the user for playing and signifies the end of the program 
    print("\nThanks for playing! Come again!") 

main() 
