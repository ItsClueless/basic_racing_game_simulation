# Racing Game Simulation
* By: Dwayne Kirby

# Details
* This is a multi-program project that starts off in C++ and calls python in two several cases, in which both have different functions
* The program starts off by asking if the user has played before (in that case grab the user's progress ie coins) and if the user hasn't played before, the program adds the user to the file with starting coins
* The program then calls the main python program that simulates the game. It restricts the user to certain cars and mods depending on the coins the user has, and deducts coins after the user selects something they want like a car or a mod
* Once user has done that, then the opponent can select their car (using the user's coins) if it's a secondary user or enter a difficulty if the user wants to play against the computer
* If so, the computer, depending on the difficulty, chooses a car and a certain number of mods (randomized). 
* Once user/computer picks their cars, the cars are displayed with their stats.
* Then the game simulates in which the winner is calculated by Hane's formula but is race is simulated through the graphics program
* If user wins they will get a certain amount of coins added to their total amount
* Then displaying the records for the chosen game mode if there are any.
* The program then writes to the user's progress and updates the coins. 


# To run the game
* Need to have C++ and Python installed, along with cv2 for pictures of the cars and glut/openGL installed for the graphics simulation. 
* This program works best if ran on windows

# How to play
* Start the program. If you have played before enter 'y', and enter your username and password. If wrong password, it'll ask for your password again until its enter correctly. If wrong username then it creates a new user
* If have not played before, then enter 'n' and it'll create a new user
* The program will then go into python where it'll ask for the game mode you want to play, repeats until correct mode is chosen (Note even if user enters lowercase/uppercase, it will still work)
    * Enter 'Drag' for Drag racing
    * Enter 'Drift' for drifting
    * Enter 'Street' for street racing
    * Enter 'Track' for a track race
    * Or enter 'Exit game' to exit the game
* The game will then ask user for a second player, who to play against or chose a different game mode
    * Enter 'computer' to play against AI
    * Enter 'another player' to have the option to have another person pick a car
* It'll then ask for the brand the user wants for the car, repeats until correct brand is chosen (Again not case-sensitive)
* Once brand is chosen, the image of the first car in that brand will pop up, and the user has to open the image and click 'y' and 'n' for the car
* If 'n', the next car will appear, until all cars have been shown.
* If all cars have been shown, it'll ask to either go to different brand or stay with the current one, in which the process repeats
* If a car has been chosen and the user has the coins to buy it, then it'll ask the user if they want any modifications, in which answer 'yes' or 'no'
* Similar process as chosen cars, but user can choose a modification from each category (if they want and if they have the coins to do so)
* If the computer option is chosen:
    Enter 'Easy', 'Medium' or 'Hard' for the difficulty, which is how many mods the computer gets
* If another player is chosen, then the above process will repeat
* Once done, the simulation will start.
    - The simulation will require the user to press the left arrow button (->) to move to the finish. Hold the arrow button to reach maximum speed
    - The simulation will end once the user or the AI has reached the finish
* The user will then see the winner of race and then the records (if any are available) for the game mode played. Then the game ends
