'''
-- Created solely for the use of a course at Queen's University -- 
This is a simple paylist program that was created for a CISC 101 - Intro to
Programming assignment at Queen's University. This is a simple program designed to get
inputs from the user to determine the cost of shipping one or two packages with Canada Post.
The user is asked to input the number of items they're shipping, location they're shipping to,
the type of item they're shipping and if applicable, the weight of said package. It uses a
series of if, elif, and else functions with Boolean operators to complete the program. 

Name: Hana Chaudhury

'''
'''
Function determines the number of items a user ships
'''
def NumberItems():
    
    #variable defines the number of items the user wants to ship and determines how many items they're shipping
    number_of_items = int(input("\nHow many items are you shipping? Please enter an integer number of '1' or '2': "))

    #if user wants to ship one item call only the first function 
    if number_of_items == 1:
        ItemOne()

    #if user wants to ship items call both functions 
    else:
        ItemOne()
        ItemTwo()

'''
This is the function for the first item and repeats for the second item if applicable. 
'''

def ItemOne():
    
    #asks the user to input the details for the first item being shipped 
    print("\nPrint the details for your first item.") 

    #asks the user to input shipping location 
    shipping_location = input("\nIf shipping to Canada please enter 'C', if shipping internationally please enter 'I': ")

    #asks the user to input what type of item they are shipping 
    item_type = input("\nIs it a letter or a parcel? Please enter 'letter' or 'parcel': ")

    #outputs results for if item is a letter and is shipping to Canada  
    if item_type == 'letter' and shipping_location == 'C':
        print("\nYou pay $1.00")

    #does the same as previous if statement for international location
    elif (item_type == 'letter') and (shipping_location == 'I'): 
        print("\nYou pay $1.75")

    #else function is if the item type is a parcel
        
    else:
        #specifies that the item type is a parcel to prevent it from skipping to the nested else 

        #asks the user to input the weight of the parcel 
        weight = float(input("\nPlease enter the number of how much your parcel weighs to the nearest decimal point: "))

        #nested if functions determine the cost of shipping for parcels
        #cost if weight is less than 1kg and ships in Canada 
        if (weight < 1) and (shipping_location == 'C'):
            print("\nYou pay $5.50")

        #cost if weight is less than 1kg and shipps internationally 
        elif (weight < 1) and (shipping_location == 'I'):
            print("\nYou pay $8.75")

        #cost if weight is between 1kg and 5kg inclusive and ships in Canada 
        elif (weight >= 1) and (shipping_location == 'C'):
            print("\nYou pay $10.00")
            
        #cost if weight is between 1kg and 5kg inclusive and ships internationally 
        elif (weight >= 1 and weight <= 5) and (shipping_location == 'I'):
            print("\nYou pay $18.75")
            
        #cost if weight is more than 5kg and ships in Canada
        elif (weight >5) and (shipping_location == 'C'):
            print("\nYou pay $25.25")

        #else function is specified to if parcel weight is greater than 5 and ships internationally 
        else:
            print("\nYou pay $40.75") 


'''
If user is shipping two items they will be prompted to enter details for their second item here.
It repeats the code from the function ItemOne 
'''

def ItemTwo():
    #asks the user to input the details for the second item being shipped 
    print("\nPrint the details for your second item.") 

    #asks the user to input shipping location 
    shipping_location = input("\nIf shipping to Canada please enter 'C', if shipping internationally please enter 'I': ")

    #asks the user to input what type of item they are shipping 
    item_type = input("\nIs it a letter or a parcel? Please enter 'letter' or 'parcel': ")

    #outputs results for if item is a letter and is shipping to Canada  
    if item_type == 'letter' and shipping_location == 'C':
        print("\nYou pay $1.00")

    #does the same as previous if statement for international location
    elif (item_type == 'letter') and (shipping_location == 'I'): 
        print("\nYou pay $1.75")

    #else function is if the item type is a parcel
        
    else:
        #specifies that the item type is a parcel to prevent it from skipping to the nested else 
        item_type == 'parcel'

        #asks the user to input the weight of the parcel 
        weight = float(input("\nPlease enter the number of how much your parcel weighs to the nearest decimal point: "))

        #nested if functions determine the cost of shipping for parcels
        #cost if weight is less than 1kg and ships in Canada 
        if (weight < 1) and (shipping_location == 'C'):
            print("\nYou pay $5.50")

        #cost if weight is less than 1kg and shipps internationally 
        elif (weight < 1) and (shipping_location == 'I'):
            print("\nYou pay $8.75")

        #cost if weight is between 1kg and 5kg inclusive and ships in Canada 
        elif (weight >= 1 and weight <= 5) and (shipping_location == 'C'):
            print("\nYou pay $10.00")
            
        #cost if weight is between 1kg and 5kg inclusive and ships internationally 
        elif (weight >= 1 and weight <= 5) and (shipping_location == 'I'):
            print("\nYou pay $18.75")
            
        #cost if weight is more than 5kg and ships in Canada
        elif (weight >5) and (shipping_location == 'C'):
            print("\nYou pay $25.25")

        #else function is specified to if parcel weight is greater than 5 and ships internationally 
        else:
            (weight > 5) and (shipping_location == 'I')
            print("\nYou pay $40.75")

'''
The main function that calls the other function and introduces the user to the program and ends it.
'''

def main():
    print ("Thank you for choosing Canada Post to ship your package. To determine the cost of")
    print("shipping your item, please answer the following questions.")

    #calls the starting function 
    NumberItems()

    print("\nThank you for choosing Canada Post!") 

main()
