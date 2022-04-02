
def main():
    game_recs = []
    read_game_files(game_recs)
    # Display the winner with the stats

    if game_recs[8] == 'bot':
        print()
        print('The winner is:', game_recs[0], 'with a time of', game_recs[1], 'seconds and a final speed of', game_recs[2], 'MPH')
        print()
        if game_recs[0] == game_recs[3]:

            # Call compile rec with the stats from race
            compile_rec(game_recs[3], game_recs[1], game_recs[2], game_recs[4],game_recs[5])

            if game_recs[9] == 'easy':
                game_recs[6] = update_coins(int(game_recs[6]),0,1000)
            # If user enter medium run this part
            elif game_recs[9] == 'medium':
                game_recs[6] = update_coins(int(game_recs[6]),0,2000)
            elif game_recs[9] == 'hard':
                game_recs[6] = update_coins(int(game_recs[6]),0,5000)
    else:
        # As long as it was not a tie
        if game_recs[0] != 'Tie':

            print()
            print('The winner is:', game_recs[0], 'with a time of', game_recs[1], 'seconds and a final speed of', game_recs[2], 'MPH')
            print()

            # Call compile rec with the stats from race
            compile_rec(game_recs[3], game_recs[1], game_recs[2], game_recs[4],game_recs[5])

            game_recs[6] = update_coins(int(game_recs[6]),0,2000)
        else:
            print("It was a tie")

    # Call show_records with the game mode
    print()
    print("Game Records For " + game_recs[4])
    show_records(game_recs[4])

    update_coin_records(game_recs[6], game_recs[7])

def read_game_files(records):
    # Use Try/Except clause
    try:
        game_files = '../game_file' + '.txt.'

        # Opens/Writes the file in append mode
        file = open(game_files, 'r')

        # Then get the first line
        line = file.readline()

        # Strip \n from it
        line = line.rstrip('\n')

    # If there is an error, print no records
    except IOError:
        print()
        print('No Game Files')

    except FileNotFoundError:
        print()
        print('No Game Files')


    # Set place to 1
    placement = 0

    # Use try statement
    try:
        # Use While loop to keep running until no more files
        while line != '':

            # Assign record to the line
            records.append(line)

            # Move onto the next line
            line = file.readline()

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
        file.close()

    # If wins is not defined
    except UnboundLocalError:

        # Set to False
        False

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

def update_coins(coins, deductionCoins, addedCoins):
    if deductionCoins > 0:
        coins = coins - deductionCoins
    if addedCoins > 0:
        coins = coins + addedCoins
    return coins

def update_coin_records(coins,ocoin):
    with open("../racing_game_users.txt", "r") as f:
        lines = f.readlines()
    with open("../racing_game_users.txt", "w") as f:
        for line in lines:
            if line.strip("\n") == ocoin:
                f.write(str(coins) + "\n")
            if line.strip("\n") != ocoin:
                f.write(line)

main()