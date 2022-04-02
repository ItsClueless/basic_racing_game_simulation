'''
Racing game simulation
With an option for two players
or play against a computer
With different race modes and cars and mods
Displaying who wins
And recording the records
'''

from display import *
import sys

# Define main
# Main will create the dictionaries of cars and mods
# Will create loops and if statements to have program to run correctly
# Call all functions in the order they are need
# Responsible for passing arguments into those functions
# And display when they want to exit the game
def main():


    user = sys.argv[1]
    play_again = sys.argv[2]
    ocoins = sys.argv[3]
    coins = int(ocoins)


    # Create file/constant of all cars in game and stats
    # Horsepower, Torque, Weight, and Top Speed
    CARS = {'Subaru':
            [{'WRX': ['268', '258', '3455', '146', '400']},
            {'STi': ['341', '330', '3391', '162', '650']},
            {'BRZ': ['197', '151', '2690', '140', '300']}],
            'Mitsubishi':
            [{'Evolution X': ['276', '275', '3131', '155', '400']},
              {'Eclipse GSX Turbo': ['194', '220', '3093', '140','300']},
              {'Eclipse Spyder GTS': ['210', '205', '3329', '148','350']}],
            'Toyota':
            [{'Supra MK4': ['320', '315', '2800', '177','500']},
             {'Supra MK5': ['335', '363', '3397', '155','400']}],
            'Ford':
            [{'Mustang GT': ['310', '365', '3523', '155','350']},
             {'SVT Cobra': ['320', '317', '3125' , '152','400']},
             {'GT 500': ['662', '631', '4225', '180','550']},
             {'GT': ['647', '550', '2385', '216','800']}],
            'Chevrolet':
            [{'Corvette': ['495', '470', '3535', '184','800']},
             {'Camaro ZL1': ['650', '455', '3907', '190','950']}],
            'Dodge':
            [{'Hellcat': ['707', '650', '4448', '199','950']},
             {'Redeye': ['797', '707', '4443', '203','1000']},
             {'Demon': ['808', '770', '4280', '164','800']},
             {'Viper': ['645', '600', '3389', '208','1000']}],
            'Honda':
            [{'Civic Type R': ['306', '295', '2762', '169','500']},
             {'NSX': ['500', '406', '3878 ', '191','800']}],
            'Nissan':
            [{'GTR': ['600', '481', '3836', '195','900']},
             {'Skyline R34': ['276', '320', '3440', '155','450']},
             {'370Z': ['350', '276', '3232', '155','300']},
             {'S15': ['250', '203', '2756', '155','250']}],
            'Audi':
            [{'R8': ['562', '406', '3439', '196','900']},
             {'TTS': ['228', '280', '3164', '155','400']},
             {'RS': ['444', '443', '3968', '174','650']}],
            'Bmw':
            [{'M3': ['453', '443', '3494', '183','550']},
            {'M5': ['617', '553', '4370', '189','650']}],
            'Tesla':
            [{'Roadster': ['248', '7400', '1836', '250','1000']},
             {'Model 3': ['346', '376', '4883', '155','700']}],
            'Lamborghini':
            [{'Aventador': ['759', '531', '3472', '217','1100']},
             {'Huracan': ['602', '413', '3424', '199','750']},
             {'Veneno': ['740', '507', '4281', '221','1250']}],
            'Ferrari':
            [{'448 GTB': ['661', '561', '3054', '205','800']},
             {'SF90': ['769', '590', '3461', '217','1000']},
             {'LaFerrari': ['949', '664', '3494', '217','1100']},
             {'FXX-K': ['1036', '664', '2658', '249','1500']}],
            'Mclaren':
            [{'720S': ['710', '568', '2937', '212','900']},
             {'P1 Supercar': ['903', '664', '3411', '217','1100']},
             {'Senna': ['789', '590', '2886', '208','1000']}]}
             
            
    # Create file/constants of all mods in game and stats
    # Horsepower, Torque, Weight, and Top Speed
    MODS = {'Turbo':
            [{'30mm Turbo': ['70', '60', '30', '4','50']},
             {'50mm Turbo': ['130', '100', '46', '7','100']},
             {'76mm Turbo': ['200' ,'120', '52', '10','200']}],
            'Supercharger':
            [{'Kraftwerks SuperCharger': ['135', '70', '50', '6','50']},
             {'Wieland SuperCharger': ['210', '110', '58', '9','150']},
             {'Hennessy SuperCharger': ['300', '180', '70', '11','250']}],
            'Spoiler':
            [{'GT Wing': ['0', '8', '20', '1','50']},
             {'VRX Style Wing': ['0', '12', '50', '3','100']},
             {'Saleen Style Wing':['0', '8', '30', '2','50']},
             {'Drag Wing': ['0', '20', '10', '5','300']}],
            'Tune':
            [{'Stage 1 Tune': ['71', '93', '0', '3','50']},
             {'Stage 2 Tune': ['122', '113', '0', '4','100']},
             {'Stage 3 Tune': ['183', '126', '0', '5','200']},
             {'Stage 4 Tune': ['221', '160', '0', '7','400']}],
            'Fuel system':
            [{'Fuel Injectors': ['5', '7', '0', '1','50']},
             {'Fuel Pump': ['2', '0', '0', '2','100']},
             {'E85 Fuel': ['80', '0', '0', '5','200']}],
            'Air induction':
            [{'Cold Air Intake': ['5', '0', '0', '1','25']},
             {'Intake Filter': ['1', '0', '0', '0','25']}],
            'Exterior':
            [{'Carbon Fiber Body Kit': ['0', '0', '-500', '3','800']},
             {'Aero Style Body Kit': ['0', '50', '300', '2','500']},
             {'Enkei RPF1 Wheels': ['0', '0', '-100', '0','200']}],
            'Suspension':
            [{'Ohlins Road and Track Coilovers': ['0', '0', '-10', '-1','50']},
             {'Autosport Control Arms': ['0', '50', '30', '0','50']},
             {'Sway Bar Kit': ['0', '17', '20', '0','50']},
             {'Bag Suspension System': ['0', '0', '200', '0','50']},
             {'Lowering Springs': ['0', '2', '10', '0','50']}],
            'Cooling':
            [{'Radiator Shrouds': ['0', '0', '10', '0','20']},
             {'Front Mount Intercooler Kit': ['30', '0', '70', '3','150']},
             {'Coolant Overflow Tank': ['0', '0', '20', '0','100']},
             {'Silicone Radiator Hoses': ['0', '0', '-2', '0','25']}],
            'Drivetrain':
            [{'Stage 1 Drivetrain': ['5', '0', '-4', '0','50']},
             {'Stage 2 Clutch': ['7', '0', '-7', '1','150']},
             {'Short Throw Shifters': ['0', '0', '-8', '2','200']},
             {'Shifter Bushings': ['0', '0', '2', '3','150']}],
            'Brakes':
            [{'Stoptech Sport Brake Rotors': ['0', '0', '20', '0','50']},
             {'Hawk Performance Brake Pads': ['0', '0', '12', '0','50']},
             {'Stoptech Stainless Steel Brake Lines': ['0', '0', '5', '0','25']}],
            'Exhaust systems':
            [{'Cat-Back Exhaust System': ['7', '0', '10', '2','75']},
             {'Straight Pipe Exhaust': ['9', '0', '-2', '2','125']},
             {'Exhaust Heat Shields': ['0', '0', '20', '0','25']}],
            'Tires':
            [{'Drag Slicks': ['0', '100', '50', '4','500']},
             {'Performance Tires': ['0', '20', '10', '3','200']},
             {'Touring Tires': ['0', '10', '12', '2', '2','150']}]}

            
    # Display intro messages 
    print('Welcome to the game')
    print('Race to win')
    print()

    # Loop to control if user wants to play again
    while play_again == 'yes':

        # If no then game mode will be set to exit
        if play_again == 'no':
            game_mode = 'Exit game'

        else:
            # Have user select the mode
            game_mode = select_mode()

        # If statement for user input
        if game_mode == 'Exit game':

            # Display exiting game and quit the program
            print()
            print('Exiting Game')
            return False

        # If user input is not 5 then run game
        else:

                # As long as the mode is not exit game
                while game_mode != 'Exit game':

                    # Ask user who they want to play against
                    play_against = other_player()

                    # If statement if user enters 3
                    if play_against == 'Exit to main menu':

                        # Display exit to main menu
                        print()
                        print('Exiting to main menu')

                        # Then call select mode again and ask user for mode
                        game_mode = select_mode()

                        # If mode is exit game then exit the game
                        if game_mode == 'Exit game':
                            play_again = 'no'
                            print()
                            print('Ending Game')
                            return False
                            
                        else:
                            # Ask user who they want to play against
                            play_against = other_player()
                            
                    # Once user has chosen  opponent and game mode
                    # Continue the program
                    else:

                        # Call pick car function with the cars list in it
                        # And assign chosen car and brand to the results
                        chosen_car, chosen_brand, coins = pick_car(CARS, coins)

                        # Call any_mods function and assign it to mod_car
                        mod_car = any_mods()

                        # If user wants to mod their car
                        if mod_car == 'yes':

                            # Then call mods function and assign it to stats and mods chosen
                            chosen_car_stats, chosen_mods, coins = mods(chosen_car, chosen_brand, CARS, MODS,coins)

                        # If user does not want any mods
                        else:

                            # Assign values as the brand user chose
                            values = CARS.get(chosen_brand)

                            # use for loop for all values
                            for val in values:

                                # Use if statement if the car is in values
                                if chosen_car in val:

                                    # Assign stats chosen to the value of the key.
                                    chosen_car_stats = val.get(chosen_car)

                        # Then print the user's car and stats of their car
                        print()
                        print('Your car is', chosen_car)
                        print('Stats of your car are; Power:', chosen_car_stats[0], 'Horsepower,', 'Torque:', chosen_car_stats[1], 'lb-fts,',
                              'Weight:', chosen_car_stats[2], 'lbs,', 'and a top speed of:', chosen_car_stats[3], 'MPH.')

                        # If user wants to play against the computer, run this part
                        if play_against == 'Computer':

                            # Print computer is choosing car
                            print()
                            print('Computer is choosing car')
                            
                            # Ask user for difficulty of the bot
                            diff = input('Enter difficulty(Easy, Medium, Hard): ')

                            # Lower the input
                            diff = diff.lower()

                            # Strip the input
                            diff = diff.strip()

                            # Use while loop to validate input
                            while diff != 'easy' and diff != 'medium' and diff != 'hard':
                                
                                # Ask user for difficulty of the bot
                                diff = input('Please enter difficulty(Easy, Medium, Hard): ')

                                # Lower the input
                                diff = diff.lower()

                                # Strip the input
                                diff = diff.strip()
                                
                            # Assign statement to False to run loop 
                            statement = False

                            # Use while loop for different variants
                            while statement == False:

                                # Use try statement to make sure nothing crashes
                                try:

                                    # Use if statement for each starting with easy
                                    if diff == 'easy':

                                        # Call bot_car and get just the car and stats
                                        bot_cars, bot_stats = bot_car(CARS)

                                        # Set the statement to true to end the loop
                                        statement = True

                                    # If user enter medium run this part
                                    elif diff == 'medium':

                                        # Assign bot cars and stats the the result of bot car mods
                                        bot_cars, bot_stats = bot_car_mods(CARS, MODS, diff)

                                        # Set the statement to true to end the loop
                                        statement = True

                                    # If user has entered hard, run this part
                                    elif diff == 'hard':

                                        # Assign bot cars and stats the the result of bot car mods
                                        bot_cars, bot_stats = bot_car_mods(CARS, MODS, diff)

                                        # Set the statement to true to end the loop
                                        statement = True
                                    
                                # If there is an error in the program, keep statement to false and run the loop
                                except IndexError:
                                    
                                    statement = False
                                    
                            # Display the computer's car and stats
                            print()
                            print("Computer's Car is", bot_cars)
                            print("Computer's stats are; Power:",  bot_stats[0], 'Horsepower,', 'Torque:',  bot_stats[1], 'lb-fts,',
                              'Weight:',  bot_stats[2], 'lbs,', 'and a top speed of:',  bot_stats[3], 'MPH.')

                            winner, time, final_speed = race(chosen_car, chosen_car_stats, bot_cars, bot_stats, game_mode)
                            # PASS THE NAMES TO THE FILE
                            game_file(winner,time,final_speed,chosen_car,game_mode,user, coins, ocoins, 'bot', diff)

                            print()
                            print('Entering Simulation')
                            return True
                        # If user wants another player instead of computer
                        else:

                            # Display user's 2 turn
                            print()
                            print("Player 2's turn to pick a car")
                            print()
                            player2coins = int(ocoins)

                            # Call pick car function and assign player 2's car and stats as result
                            p2_chosen_car, p2_chosen_brand, coins = pick_car(CARS,player2coins)

                            # Call any_mods function to ask user if they want mods
                            mod_car = any_mods()

                            # If they want mods
                            if mod_car == 'yes':

                                # Assign chosen stats and mods to the resulting of mods function
                                p2_chosen_car_stats, p2_chosen_mods, coins = mods(p2_chosen_car, p2_chosen_brand, CARS, MODS,player2coins)

                            # If user does not want mods, get the stock car stats
                            else:

                                # Assign values to the keys of the brand
                                values = CARS.get(p2_chosen_brand)

                                # for the keys in values run for loop
                                for val in values:

                                    # If the car is in values loop
                                    if p2_chosen_car in val:

                                        # Assign the stats to the values of the car
                                        p2_chosen_car_stats = val.get(p2_chosen_car)

                            # Display the player 2's cars and stats
                            print()
                            print("Player 2's Car is", p2_chosen_car)
                            print("Player 2's stats are; Power:", p2_chosen_car_stats[0], 'Horsepower,', 'Torque:', p2_chosen_car_stats[1], 'lb-fts,',
                              'Weight:', p2_chosen_car_stats[2], 'lbs,', 'and top speed of:', p2_chosen_car_stats[3], 'MPH.')

                            # Call the race function and get the winner and time and speed as results
                            winner, time, final_speed = race(chosen_car, chosen_car_stats, p2_chosen_car, p2_chosen_car_stats, game_mode)
                            game_file(winner,time,final_speed,chosen_car,game_mode,user, coins, ocoins, 'player_2','N/A')

                            print()
                            print('Entering Simulation')
                            return True

# Select mode will be called and ask user
# To select a game mode based on options displayed
# Then return the game mode selected
def select_mode():

    # Print the race modes
    print('Race modes are:')
    print('1. Drag')
    print('2. Drift')
    print('3. Street')
    print('4. Track')
    print('5. Exit game')
    print()

    # Ask user for what mode they want
    mode = input('Select race mode: ')

    # Make sure no case sensitive
    mode = mode[0].upper() + mode[1:].lower()
        
    # As long as user does not enter a valid option
    while mode != 'Drag' and mode != 'Drift' and mode != 'Street' and mode != 'Track' and mode != 'Exit game':
          
        # Ask user for what mode they want
        mode = input('Select correct race mode: ')

        # Make sure no case sensitive
        mode = mode[0].upper() + mode[1:].lower()

            
    # Return user input
    return mode



# Other player function will ask user
# For who they want to play against
# And will return the option
def other_player():

    # Display the menu
    print()
    print('Menu of options')
    print('1. Another player')
    print('2. Computer')
    print('3. Exit to main menu')
    print()

    # Ask user for the option
    player = input('Select player option: ')

    # Make sure its not case sensitive
    player = player[0].upper() + player[1:].lower()

    # Verify user input if its not valid
    while player != 'Another player' and player != 'Computer' and player != 'Exit to main menu' :
        
        # Ask user for the option
        player = input('Select player option: ')

        # Make sure its not case sensitive
        player = player[0].upper() + player[1:].lower()

            
    # Return what user wants
    return player


def update_coins(coins, deductionCoins, addedCoins):
    if deductionCoins > 0:
        coins = coins - deductionCoins
    if addedCoins > 0:
        coins = coins + addedCoins
    return coins

# Pick Car function will take in CARS dictionary
# Then display all the brands
# Have user pick a brand
# Then Have user pick a car in that brand
# Or chose a different brand
# Returns the brand and car chosen
def pick_car(CARS,coins):

    # Print empty space
    print()
    
    # Set n to 1 for loop
    n = 1

    # For all the keys in CARS
    for key in CARS.keys():

        # Print the options of brands
        print(str(n) + '. ' + key)

        # Increase n by 1
        n += 1

    # Ask user to pick a brand
    user_brand = input('Enter Brand Name: ')

    # Make sure it is not case sensitive
    user_brand = user_brand[0].upper() + user_brand[1:].lower()

    # Validate what user wants and ask until it is valid
    while user_brand not in CARS:

        # Will ask user to enter correct name
        user_brand = input('Enter Correct Brand Name: ')

        # Make sure it is not case sensitive
        user_brand = user_brand[0].upper() + user_brand[1:].lower()
        
    # Assign values to the values of the brand
    values = CARS.get(user_brand)

    # Set i to 0
    i = 0

    # Set car to no
    car = 'no'

    # Set diff car to no
    diff_car = 'no'

    # Set user car to False
    user_car = False

    # Enter loop as long as user car is false
    while user_car == False:

        # If i equals the amount of things in values
        if i == len(values):

            # Set i back to 0
            i = 0

            # Ask user if they want a different car
            diff_car = input('Do you want a different car: ')

            # Validate the input
            while diff_car != 'yes' and diff_car != 'no':

                # Ask if they want a different car
                diff_car = input('Do you want a different car, valid answers only(yes/no): ')

            # If they want a different car
            if diff_car == 'yes':

                # Set i to 1
                n = 1
                
                print()
                
                # Display all the cars
                for key in CARS.keys():
                    
                    print(str(n) + '. ' + key)

                    # Increase n by 1
                    n += 1
                    
                # Ask user for brand names
                user_brand = input('Enter Brand Name: ')

                # Make sure it is not case sensitive
                user_brand = user_brand[0].upper() + user_brand[1:].lower()

                # Validate what user wants and ask until it is valid
                while user_brand not in CARS:

                    # Will ask user to enter correct name
                    user_brand = input('Enter Correct Brand Name: ')

                    # Make sure it is not case sensitive
                    user_brand = user_brand[0].upper() + user_brand[1:].lower()
                    
                # Reset values to the values of the brand
                values = CARS.get(user_brand)

                # Reset diff car to no
                diff_car = 'no'

        # While i is less than values, car is no, and diff car is no
        while i < len(values) and car == 'no' and diff_car == 'no':

            # Lst is set to the values of brand
            lst = values[i]

            # For keys in list of keys
            for key in lst.keys():

                # Print the car
                print()
                print(key)

                # Display the car
                car = displayCar(key)



            # Increase i by 1
            i += 1

        # If user wants the car
        if car == 'yes':

            carStats= lst[key]
            carCoins = int(carStats[4])
            if coins >= carCoins:
                # Assign user car to that car
                coins = update_coins(coins, carCoins, 0)
                print("Coins remaining: " + str(coins))
                user_car = key
            else:
                print("Not enough coins for this car")
                # User car will still be false
                car = 'no'
                user_car = False



        # If not
        else:

            # User car will still be false
            user_car = False

    # Return the car and brand to main
    return user_car, user_brand, coins


# Ant mods is to ask user if they want to mod the car
# Then validate it and return it
def any_mods():
    
    # Ask user for any mods
    want_mods = "" #str(input('Do you want any mods(yes/no): '))

    # Lower the input
    #want_mods = want_mods.lower()

    # Validate answer to yes or no
    while want_mods != 'yes' and want_mods != 'no':

        # Ask again
        want_mods = str(input('Do you want any mods,valid answers only(yes/no): '))

        # Lower the input
        want_mods = want_mods.lower()

    # Return what user wants
    return want_mods


# Pick mods accepts the MODS dictionary
# Ask user for what mods they from the menu
# Then pick a certain mod from each menu
# Ask until user wants no more
# Then return the mods and the stats
def pick_mods(MODS,coins):

    # Set mods to empty dictionary
    mods = {}

    # Use for loop for all the keys in MODS
    for key in MODS:

        # Copy the mods to the new list
        mods[key] = MODS.get(key)

    # Set mods_general to empty list
    mods_general = []

    # Set mod_stats to empty list
    mod_stats = []

    # Set mod list to empty list
    mod_list = []

    # Set mod again to  yes
    mod_again = 'yes'

    # Use while loop as long as mod again is yes
    while mod_again == 'yes':

        # Set n to 1
        n = 1

        # For all the keys in mods
        for key in mods.keys():

                # Display all the mods keys
                print(str(n) + '. ' + key)

                # Increase n by 1
                n += 1

        # Ask user for mod name
        user_mod_menu = input('Enter Mod Name: ')

        # Make sure it is not case sensitive
        user_mod_menu = user_mod_menu[0].upper() + user_mod_menu[1:].lower()

        # Validate the input if not in mods
        while user_mod_menu not in mods:

                # Ask user again
                user_mod_menu = input('Enter Correct Mod Name: ')

                # Make sure it is not case sensitive
                user_mod_menu = user_mod_menu[0].upper() + user_mod_menu[1:].lower()
                
        # Set values to the values of mods menu
        values = mods.get(user_mod_menu)


        # Set i to 0
        i = 0

        # Set count to 0
        count = 0

        # Set mod to no
        mod = 'no'

        # Set diff mod to no
        diff_mod = 'no'

        # Set user mod to false
        user_mod = False

        # Use while loop as long as user mod if false
        while user_mod == False:

                # If i equals the values in values
                if i == len(values):

                    # Reset i to -
                    i = 0

                    # Ask if want different mod
                    diff_mod = input('Would you like to go to a different mod(yes/no): ')

                    # If they want a different mod
                    if diff_mod == 'yes':

                        # Set n to 1
                        n = 1

                        print()
                        
                        # For all values in mods
                        for key in mods.keys():

                            # Print the mods
                            print(str(n) + '. ' + key)

                            # Increase n by 1
                            n += 1

                        # Ask user for mod name
                        user_mod_menu = input('Enter Mod Name: ')

                        # Make sure it is not case sensitive
                        user_mod_menu = user_mod_menu[0].upper() + user_mod_menu[1:].lower()

                        # Use while loop to validate mod
                        while user_mod_menu not in mods:

                            # Ask again
                            user_mod_menu = input('Enter Correct Mod Name: ')

                            # Make sure it is not case sensitive
                            user_mod_menu = user_mod_menu[0].upper() + user_mod_menu[1:].lower()

                        # Assign values to new mod
                        values = mods.get(user_mod_menu)

                        # Reset mod to no
                        mod = 'no'

                        # Reset diff mod to no
                        diff_mod = 'no'

                # While i is not equal to keys in values and mod is no and diff mod is no                      
                while i < len(values) and mod == 'no' and diff_mod == 'no':

                    # Lst is the values of i
                    lst = values[i]


                    # Run for loop in lst for keys
                    for key in lst.keys():

                        # Print each mod one by one
                        print()
                        print(key)

                        # Display
                        mod = displayMod(key)

                    # Increase i by 1
                    i += 1


                # If user wants that mod
                if mod == 'yes':
                    modStats= lst[key]
                    modCoins = int(modStats[4])
                    if coins < modCoins:
                        print("Not enough coins for this mod")
                        # mod car will still be false
                        mod = 'no'
                    else:
                        # Assign user car to that car
                        coins = update_coins(coins, modCoins,0)
                        print("\nCoins remaining: " + str(coins))

                        # Set user mod to the key to exit loop
                        user_mod = key

                        # Append it to mod list
                        mod_list.append(user_mod)

                        # Append to mod general
                        mods_general.append(user_mod)

                        # Use for loop to run through mods general
                        for mod in mods_general:

                            # Mod will be equal to the element in general
                            mod = mods_general.pop()

                            # Mods in mods will get that of the user menu
                            mod_in_mods = MODS.get(user_mod_menu)

                            # Set wanted to empty
                            wanted = ''

                            # Set j to 0
                            j = 0

                            # Use while loop as long as mod is not wanted
                            while wanted != mod:

                                # Wanted mod is in mod in mod of j
                                wanted_mod = mod_in_mods[j]

                                # Use for loop to run through keys
                                for key in wanted_mod.keys():

                                    # Wanted will be equal to key
                                    wanted = key

                                # Increase j by 1
                                j += 1

                            # The stat will be to of the wanted mod of wanted
                            stat = wanted_mod.get(wanted)

                        # Add the stats of mod to to mod stats
                        mod_stats.append(stat)

                        # Delete that mod menu from the list
                        del mods[user_mod_menu]
                    
        # As long as lens of mod is not 0    
        if len(mods) != 0:

            # Another mod will be empty
            another_mod = ''

            print()
            
            # While it is not yes or no run loop and validate
            while another_mod != 'no' and another_mod != 'yes':

                # Ask if they want another mod
                another_mod = input('Do you want another mod(yes/no): ')

                # Lower the input
                another_mod.lower()
                

                # If they say no, exists the loop
                if another_mod == 'no':

                    # And mod again will be no and exits the outer loop
                    mod_again = 'no'

        # If len of mods is 0, mod again will be no          
        else:
            mod_again = 'no'

    # Return the mod list and stats
    return mod_list, mod_stats,coins
    


# mods function will take in the user car, brand
# CARS and MODS dictionary
# Will call pick mods and assign get the mods and stats
# Then apply the mod stats to car stats
# Return the car stats and mods
def mods(user_car, brand, CARS, MODS,coins):

    # Call pick mods with MODS into it and passing it to wanted and the stats
    mods_wanted, mod_stats, coins = pick_mods(MODS,coins)


    # Assign values to values in brand
    values = CARS.get(brand)

    # Run for loop for values
    for val in values:

        # If the user car is in val
        if user_car in val:

            # Then assign car stat to the values
            car_stat = val.get(user_car)
            
    # Set modded car stats to empty list
    modded_car_stats = []

    # Set count to 0
    count = 0

    # Set count mod to 0
    count_mod = 0

    # Set while loop as count is not equal to car stats
    while count != len(car_stat):

        # element will be car stat of count 
        element = car_stat[count]

        # Put that as int
        element = int(element)

        # Get the mod stats of first mod
        number = mod_stats[count_mod]

        # Put number to the first mod stat
        number = number[count]

        # Put it into int
        number = int(number)

        # Have updated as the addition of both
        updated = element + number

        # Append updated to mod car stats
        modded_car_stats.append(updated)

        # Increase count by 1
        count += 1

    # Increase count mod by 1
    count_mod +=1

    # Set while loop as long as the count is not equal to the lens of mods
    while count_mod != len(mods_wanted):

        # Reset count 
        count = 0

        # Set while loop as count is not 4
        while count != 4:

            # Get the element of modded car stats of the count
            element = modded_car_stats.pop(count)
            element = (element)

            # Get the mod of the count mod
            number = mod_stats[count_mod]

            # Get the stat of that mod
            number = number[count]

            # Turn it into an int
            number = int(number)

            # Have updated of element and number
            updated = element + number

            # Append modded car stats of count and updated
            modded_car_stats.insert(count, updated)

            # Count goes up by 2
            count += 1

        # Count mod increase by 1
        count_mod += 1
    
    # Return the car and mod stats
    return modded_car_stats, mods_wanted, coins



# Bot Car will take in CARS dictionary
# Chosen a random brand from that
# Then chose a random car from that brand
# Then return the car and its stats
def bot_car(CARS):

    # Import random module
    import random

    # Assign rand_num to a random number of 0 and 1 minus of cars
    rand_num = random.randint(0, len(CARS)-1)

    # Brands will be an empty list
    brands = []

    # Use for loop to run through keys of CARS
    for key in CARS.keys():

        # append the keys to brands
        brands.append(key)

    # Assign bot brands to the brand of random
    bot_brand = brands[rand_num]

    # Assign car types to the values of bot brand
    car_types = CARS.get(bot_brand)

    # Bot car number will be random number from 0 to 1 minus the cars
    bot_car_num = random.randint(0, len(car_types)-1)

    # Get the key of bot car number
    for key in car_types[bot_car_num].keys():

        # Bot car will be equal to key
        bot_car = key

    # Assign values to the keys of bot brand
    values = CARS.get(bot_brand)

    # For the values in values
    for val in values:

            # If the car is in val
            if bot_car in val:

                # The car stat will be the values of val
                car_stat = val.get(bot_car)

    # Return bot car and the stats
    return bot_car, car_stat


# Bot car mods will take in CARS and MODS dictionary and diff
# It will chose random mods appropriate for the difficulty
# Add the mods to the stats
# Then return the bot car and its stats
def bot_car_mods(CARS,MODS,diff):

    # Important random module
    import random

    # Set mods to empty dictionary
    mods = {}

    # Use for loop of keys in MODS
    for key in MODS:

            # mods will append each key to the dictionary
            mods[key] = MODS.get(key)

    # bot mods set to 0
    bot_mods = 0

    # count is set to 0
    count = 0

    # i is set to 0
    i = 0

    # Count mods is set to 0
    count_mods = 0

    # Set mod stats to empty list
    mod_stats = []

    # Set mods list to empty list
    mod_list = []

    # Set modding to empty list
    modding = []

    # Set key list to empty list
    key_lst = []

    # If difficulty is medium
    if diff == 'medium':

        # The number of mods will only be half
        num_mods = len(MODS) // 2

    # If not medium
    else:

        # Then the number of mods will be amount of mods
        num_mods = len(MODS) - 1

    # Run while loop as long as count mods is less than num mods
    while count_mods < num_mods:

            # Run for loop of keys in mods
            for key in mods.keys():

                    # Append the key to modding
                    modding.append(key)

            # Set mod menu to random number from 0 to 1 less than modding
            mod_num_menu = random.randint(0, len(modding)-1)

            # Get the mod of mod menu
            bot_mod_menu = modding[mod_num_menu]

            # Clear modding list
            modding.clear()

            # Assign values to the values of mod menu
            values = mods.get(bot_mod_menu)

            # Run for loop of all values
            for val in values:

                    # Append the vals to key lst
                    key_lst.append(val)

            # Set mod number to random number from 0 to 1 les than the key lst
            mod_num = random.randint(0, len(key_lst)-1)

            # Bot mod will be the mod chosen from the list
            bot_mod = key_lst[mod_num]

            # The key in bot mod
            for key in bot_mod.keys():

                    # mod list to append mod list
                    mod_list.append(key)
                    
            # Clear key lst
            key_lst.clear()

            # Run for loop for all mods in mod list
            for mod in mod_list:

                    # Set mod to the mod list of count
                    mod = mod_list[count]

                    # Mods in mods will be mods of bot menu
                    mod_in_mods = MODS.get(bot_mod_menu)

                    # J set to 0
                    j = 0

                    # Set wanted to empty
                    wanted = ''

                    # While loop as long as wanted is not mod
                    while wanted != mod:

                            # Wanted_mod is mod in mods of j
                            wanted_mod = mod_in_mods[j]

                            # Run through keys of wanted mod
                            for key in wanted_mod.keys():

                                    # Set wanted to the key
                                    wanted = key
                                    
                            # Increase j by 1
                            j += 1
                            
                    # Stat will be equal to the values of wanted 
                    stat = wanted_mod.get(wanted)

            # for each stat append it to mod stats
            mod_stats.append(stat)

            # Then delete the mod off from the menu
            del mods[bot_mod_menu]

            # Increase count by 1
            count += 1

            # Increase count mod by 1
            count_mods += 1


    # Assign ran num back to random number from 0 to cars minus 1
    rand_num = random.randint(0, len(CARS)-1)

    # Get the brands
    brands = []

    # Run through the keys
    for key in CARS.keys():

        # Append each to brand
        brands.append(key)
        
    # bot brand will be random of brands
    bot_brand = brands[rand_num]

    # Get the values of bot brand of cars
    car_types = CARS.get(bot_brand)

    # Get a random number
    bot_car_num = random.randint(0, len(car_types)-1)

    # For the key in the car types
    for key in car_types[bot_car_num].keys():

        # Assign bot car as the key
        bot_car = key

    # Assign mods_wanted to mod list
    mods_wanted = mod_list

    # Mod stats as mod stats
    mod_stats = mod_stats

    # Assign values of bot brand of car
    values = CARS.get(bot_brand)

    # For the values in values
    for val in values:

            # If the both car is in val
            if bot_car in val:

                # Then the cars stat will be value of bot car
                car_stat = val.get(bot_car)

    # Set modded car stats to empty lit
    modded_car_stats = []

    # Set count to 0
    count = 0

    # Set count mod to 0
    count_mod = 0

    # Use while loop as long as its less than car stat
    while count != len(car_stat):

            # Set element to car stat of the count
            element = car_stat[count]

            # Turn element into int
            element = int(element)

            # Set number of mod stats of mod count
            number = mod_stats[count_mod]

            # Set number to count of number
            number = number[count]

            # Turn number into int
            number = int(number)

            # Set updated as element add to number
            updated = element + number

            # Append updated to modded car stats
            modded_car_stats.append(updated)

            # Increase count by 1
            count += 1

    # Count_mod increase by 1
    count_mod +=1

    # Use while loop as count mod is not equal to mods wanted
    while count_mod != len(mods_wanted):

            # Reset count to 0
            count = 0

            # Run loop while count is not 4
            while count != 4:

                # Element will be the count of modded stats variable
                element = modded_car_stats.pop(count)

                # Element is element
                element = (element)

                # Number is mod stats of count mod
                number = mod_stats[count_mod]

                # Number is number of count
                number = number[count]

                # Number turns into int
                number = int(number)

                # Updated will be element plus number
                updated = element + number

                # Appended it to modded stats count
                modded_car_stats.insert(count, updated)

                # Count increases by 1
                count += 1

            # Count mod increases by 1
            count_mod += 1

    # Returns the bot car and the modded car stats
    return bot_car, modded_car_stats
    



# Race will take in cars 1 and 2 and their stats and the mode
# Will use mode to use correct race formula and car stats
# To get the correct numbers and cars to determine winners
# And will return the winners, their final time and the final speed
def race(car_1, car_1_stat, car_2, car_2_stat, mode):

    # If mode is drag, determine the winner of Drag
    if mode == 'Drag':
    
        # By using Hane's Equation
        # Determine quarter mile and speed
        # Get the cars hp
        car_1_hp = int(car_1_stat[0])

        # Get the cars weight
        car_1_weight = int(car_1_stat[2])

        # Get cars 2 hp
        car_2_hp = int(car_2_stat[0])

        # Get cars 2 weight
        car_2_weight = int(car_2_stat[2])

        # Calculate time 1 by using equation
        time_1 = 5.825 * ((car_1_weight / car_1_hp)**(1/3))

        # Get time 1 to 2 decimals
        time_1 = format(time_1, '.2f')

        # Determine final speed using equation
        final_speed_1 = 234 * ((car_1_hp / car_1_weight)**(1/3))

        # Turn final speed 1 to 2 decimals
        final_speed_1 = format(final_speed_1, '.2f')

        # Calculate time 2 using equation
        time_2 = 5.825 * ((car_2_weight / car_2_hp)**(1/3))

        # Turn time 2 into 2 decimals
        time_2 = format(time_2, '.2f')

        # Get final speed using equation
        final_speed_2 = 234 * ((car_2_hp / car_2_weight)**(1/3))

        # Turn final speed 2 into 2 decimals
        final_speed_2 = format(final_speed_2, '.2f')
        
        # If time 1 is less than time 2
        if time_1 > time_2:

            # The winner is car 1
            winner = car_1

            # Will return the winner, time 1, and final speed
            return winner, time_1, final_speed_1

        # If time 2 is less than time 1
        elif time_2 > time_1:

            # The winner is car 2
            winner = car_2

            # Will return winner, time 2, and final speed
            return winner, time_2, final_speed_2

        # If neither of these are true
        else:

            # The winner is set to tie
            winner = 'Tie'

            # Thus final speed is N/A
            final_speed = 'N/A'

            # Returns the winner, time 1, and final speed variable
            return winner, time_1, final_speed
    
    elif mode == 'Drift':
        # Determine the winner of Drift
        # Because top speed isn't used on a drift track, divide it by 4
        # To get rough average speed

        # Get car's 1 hp
        car_1_hp = int(car_1_stat[0])

        # Get car's 1 torque
        car_1_torque = int(car_1_stat[1])

        # Get car's 1 weight
        car_1_weight = int(car_1_stat[2])

        # Get car's 1 top speed
        car_1_top_speed = int(car_1_stat[3])

        # Get the total power of car 1
        power_1 = (car_1_hp + (car_1_top_speed / 4)+ (car_1_torque / 6))

        # Get car's 2 hp
        car_2_hp = int(car_2_stat[0])

        # Get car's 2 torque
        car_2_torque = int(car_2_stat[1])

        # Get car's 2 weight
        car_2_weight = int(car_2_stat[2])

        # Get car's 2 top speed
        car_2_top_speed = int(car_2_stat[3])
        
        # Get total power of car 1
        power_2 = (car_2_hp + (car_2_top_speed / 4) + (car_2_torque / 6))

        
        # Track length is length of a formula 1 drift track over quarter mile
        TRACK_LENGTH = 1.6 / .25


        # Calculate time 1 based on modified equation
        time_1 = 8.2 * ((car_1_weight / power_1)**(1/3))

        # Multiply that by the track length
        time_1 *= TRACK_LENGTH

        # Turn time 1 to 2 decimals
        time_1 = format(time_1, '.2f')

        # Get the final speed
        final_speed_1 = 108 * ((power_1 / car_1_weight)**(1/3))

        # Turn final speed into 2 decimals
        final_speed_1 = format(final_speed_1, '.2f')
        
        # Get time 2
        time_2 = 8.2 * ((car_2_weight / power_2)**(1/3))

        # Multiply by track length
        time_2 *= TRACK_LENGTH

        # Turn it into 2 decimals
        time_2 = format(time_2, '.2f')

        # Get the final speed of 2
        final_speed_2 = 108 * ((power_2 / car_2_weight)**(1/3))

        # Turn final speed into 2 decimals
        final_speed_2 = format(final_speed_2, '.2f')


        # If time 1 is less than time 2
        if time_1 > time_2:

            # The winner is car 1
            winner = car_1

            # Will return the winner, time 1, and final speed
            return winner, time_1, final_speed_1

        # If time 2 is less than time 1
        elif time_2 > time_1:

            # The winner is car 2
            winner = car_2

            # Will return winner, time 2, and final speed
            return winner, time_2, final_speed_2

        # If neither of these are true
        else:

            # The winner is set to tie
            winner = 'Tie'

            # Thus final speed is N/A
            final_speed = 'N/A'

            # Returns the winner, time 1, and final speed variable
            return winner, time_1, final_speed

    
    elif mode == 'Street':
        # Determine the winner of Street
        # Adding torque as a value to differ than drag
        # Due to conditions on the street of no prep

        
        # Get car's 1 hp
        car_1_hp = int(car_1_stat[0])

        # Get car's 1 torque
        car_1_torque = int(car_1_stat[1])

        # Get car's 1 weight
        car_1_weight = int(car_1_stat[2])

        # Get car's 1 top speed
        car_1_top_speed = int(car_1_stat[3])

        # Get car's 2 hp
        car_2_hp = int(car_2_stat[0])

        # Get car's 2 torque
        car_2_torque = int(car_2_stat[1])

        # Get car's 2 weight
        car_2_weight = int(car_2_stat[2])

        # Get car's 2 top speed
        car_2_top_speed = int(car_2_stat[3])

        
        # Get time 1 by equation of Hane's modified
        time_1 = 6.290 * ((car_1_weight / (car_1_hp + (car_1_torque/6)))**(1/3))

        # Turn it into 2 decimals
        time_1 = format(time_1, '.2f')

        # Get final speed of 1
        final_speed_1 = 224 * (((car_1_hp +(car_1_torque/6)) / car_1_weight) **(1/3))

        # Turn it into 2 decimals
        final_speed_1 = format(final_speed_1, '.2f')
        
        # Get time of 2
        time_2 = 6.290 * ((car_2_weight / (car_2_hp + (car_2_torque/6)))**(1/3))

        # Turn it into 2 decimals
        time_2 = format(time_2, '.2f')

        # Get speed of 2
        final_speed_2 = 224 * (((car_2_hp + (car_2_torque/6)) / car_2_weight)**(1/3))

        # Turn it into 2 decimals
        final_speed_2 = format(final_speed_2, '.2f')


        # If time 1 is less than time 2
        if time_1 > time_2:

            # The winner is car 1
            winner = car_1

            # Will return the winner, time 1, and final speed
            return winner, time_1, final_speed_1

        # If time 2 is less than time 1
        elif time_2 > time_1:

            # The winner is car 2
            winner = car_2

            # Will return winner, time 2, and final speed
            return winner, time_2, final_speed_2

        # If neither of these are true
        else:

            # The winner is set to tie
            winner = 'Tie'

            # Thus final speed is N/A
            final_speed = 'N/A'

            # Returns the winner, time 1, and final speed variable
            return winner, time_1, final_speed
    
    else:
        # Determine the winner of Track
        # Top speed can be on a track and also have to take it for the times
        # Top speed is not usable
         
        # Get car's 1 hp
        car_1_hp = int(car_1_stat[0])

        # Get car's 1 torque
        car_1_torque = int(car_1_stat[1])

        # Get car's 1 weight
        car_1_weight = int(car_1_stat[2])

        # Get car's 1 top speed
        car_1_top_speed = int(car_1_stat[3])

        # Get total power of 1
        power_1 = (car_1_hp + (car_1_torque / 6) + (car_1_top_speed / 4) + car_1_top_speed)

        # Get car's 2 hp
        car_2_hp = int(car_2_stat[0])

        # Get car's 2 torque
        car_2_torque = int(car_2_stat[1])

        # Get car's 2 weight
        car_2_weight = int(car_2_stat[2])

        # Get car's 2 top speed
        car_2_top_speed = int(car_2_stat[3])

        # Get total power of 2
        power_2 = (car_2_hp + (car_2_torque / 6) + (car_2_top_speed / 4) + car_2_top_speed)

        # Taking a regular formula 1 track length of 3.25 miles over quarter mile
        TRACK_LENGTH = 3.25 / .25

        # Get time 1 using equation
        time_1 = 6.89 * ((car_1_weight / power_1)**(1/3))

        # Multiply it by track length
        time_1 *= TRACK_LENGTH

        # Turn it into 2 decimals
        time_1 = format(time_1, '.2f')

        # Get final speed of 1
        final_speed_1 = 160 * ((power_1 / car_1_weight)**(1/3))

        # Turn it into 2 decimals
        final_speed_1 = format(final_speed_1, '.2f')

        
        # Get time 2 using equation
        time_2 = 6.89 * ((car_1_weight / power_2)**(1/3))

        # Multiply by track length
        time_2 *= TRACK_LENGTH

        # Turn into 2 decimals
        time_2 = format(time_2, '.2f')

        # Get final speed of 2
        final_speed_2 =  160 * ((power_2 / car_2_weight)**(1/3))

        # Turn it into 2 decimals
        final_speed_2 = format(final_speed_2, '.2f')


        # If time 1 is less than time 2
        if time_1 > time_2:

            # The winner is car 1
            winner = car_1

            # Will return the winner, time 1, and final speed
            return winner, time_1, final_speed_1

        # If time 2 is less than time 1
        elif time_2 > time_1:

            # The winner is car 2
            winner = car_2

            # Will return winner, time 2, and final speed
            return winner, time_2, final_speed_2

        # If neither of these are true
        else:

            # The winner is set to tie
            winner = 'Tie'

            # Thus final speed is N/A
            final_speed = 'N/A'

            # Returns the winner, time 1, and final speed variable
            return winner, time_1, final_speed



# Will compile all the records into a file
# File will depend on the game mode, and create that file if needed
# Takes in the car, time, speed, and the game mode
# Appends the arguments to the file then closes the file
def compile_rec(car, time, speed, mode,user):
    # Assign game records to the mode and records of the mode as txt
    game_records = '../' + mode.lower() + '_' + 'game_records' + '.txt.'

    # Opens/Writes the file in append mode
    wins = open(game_records, 'a')

    # Ask user for their name
    winner = user
    
    # Put user's name and stats into the file
    wins.write('User: ' + winner + ', ' +
               'Car Used: ' + car + ', ' +
                'Time Finished: ' + str(time) + ' ' +'Seconds' + ', ' +
               'Speed Recorded: ' + str(speed) + ' ' 'MPG' + '\n')

    # Close the file
    wins.close()


# Show records will take in the game mode
# Then read the file that the game mode is with
# And it will the the game records to the user
# As long as the file exists
# Then closes the file
def show_records(mode):
    
    # Use Try/Except clause
    try:

        # Assign game records to the file created of the game mode
        game_records = '../' + mode.lower() + '_' + 'game_records' + '.txt'

        # Try to open the file if it exists
        wins = open(game_records, 'r')

        # Then get the first line
        line = wins.readline()

        # Strip \n from it
        line = line.rstrip('\n')

    # If there is an error, print no records
    except IOError:
        print()
        print('No Game Records Available')
        
    except FileNotFoundError:
        print()
        print('No Game Records Available')
    

    # Set place to 1
    placement = 1

    # Use try statement 
    try:
        # Use While loop to keep running until no more files
        while line != '':

            # Assign record to the line
            record = line

            # Reassign record to have numbers in front of each
            record = str(placement) + '. ' + record

            # Display the record
            print(record)

            # Move onto the next line
            line = wins.readline()

            # Strip the line of \n
            line = line.rstrip('\n')

            # Increase n by 1
            placement += 1

    # If error comes up from line being not defined
    except UnboundLocalError:

        # Set to False
        False

    # Use try statement
    try:
    
        # Closes the file
        wins.close()

    # If wins is not defined
    except UnboundLocalError:

        # Set to False
        False

def game_file(winner,time,final_speed,chosen_car,game_mode,user, coins, original_coins, player, difficulty):
    # Assign game records to the mode and records of the mode as txt
    game_files = '../game_file' + '.txt.'

    # Opens/Writes the file in append mode
    file = open(game_files, 'w')

    # Put user's name and stats into the file
    file.write(winner + '\n' + str(time) + '\n' + str(final_speed) + '\n'
               + chosen_car + '\n' + game_mode + '\n' + user + '\n' + str(coins) + '\n' + str(original_coins) + '\n'
               + player + '\n' + difficulty)


# Another game function will ask the user
# If they want to play again
# And validate the input so it will force
# A correct answer then return it
def another_game():
    
    # Ask user if they want to play again
    print()
    again = input('Do you want to play again (yes/no): ')

    # Lower the input
    again = again.lower()

    # Strip the input
    again = again.strip()

    # Valid the answer
    while again != 'yes' and again != 'no':
         # Ask user if they want to play again
        again = input("Do you want to play again, please enter 'yes' or 'no': ")

        # Lower the input
        again = again.lower()
        # Strip the input
        again = again.strip()
        

    # Return answer
    return again

def update_coin_records(coins,ocoin):
    with open("../racing_game_users.txt", "r") as f:
        lines = f.readlines()
    with open("../racing_game_users.txt", "w") as f:
        for line in lines:
            if line.strip("\n") == ocoin:
                f.write(str(coins) + "\n")
            if line.strip("\n") != ocoin:
                f.write(line)

# Call main
main()
