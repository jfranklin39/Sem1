#Name Judah
#Date 11/21/2024
#Pokemon Evolution Game

#Init
#Global Variables
Pokemon_level = 0
Pokemon_name = "name_of_pokemon"
#Functions
def train():
    global Pokemon_level
    Pokemon_level = Pokemon_level + 1
    print(Pokemon_level)
def GymBattle():
    global Pokemon_level
    import random
    outcome = random.randint(1,2) #50% chance to win or lose
    if outcome == 1:
        print("Pokemon Lost battle")

    if outcome == 2:
        Pokemon_level = Pokemon_level + 2
        print("Pokemon won Battle!")

print("Welcome to pokemon Evolution")
while True:
    print("Choose Today's activity: ")
    print("""1.Train
2.Gym Batte
3.Rest(Display info
4.Quit""")
    activity = int(input("Activity: "))
    if activity == 1:
        train()
    if activity == 2:
        GymBattle()
    if activity == 3:
        print(Pokemon_level)
    if activity == 4:
        print("Thanks for playing the Pokemon Evolution Game")
        break
    if Pokemon_level == 5:
        Pokemon_name = "Pichu"
        print("Pokemon's name is")
        print(Pokemon_name)
        print("""⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀
⣿⣧⠈⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠉⢸⣿⣿
⣿⣿⡄⠘⣷⣤⡉⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢉⣥⣶⠇⢠⣿⣿⣿
⣿⣿⣿⣦⠈⠻⣿⣷⣄⠻⡿⠋⠙⠉⠋⠛⢿⡟⢡⣶⣿⡿⠃⣰⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣦⣈⠻⠿⠃⠀⠀⠀⠀⠀⠀⠀⠐⢿⠿⢋⣤⣾⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣶⠀⡤⠄⠀⠀⠀⢀⠤⡀⢰⣿⡿⠛⢿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣷⡾⠀⠀⠀⢸⣶⡇⢸⠟⠁⠀⠈⢿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠈⠁⠤⠬⠤⠄⠉⠀⢀⠀⠀⠀⠀⠸⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡿⢟⣵⢄⣀⡀⠀⠀⣀⣠⣰⣿⡶⣆⡄⣀⠀⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣟⣾⡏⣿⣿⣿⣿⣿⣿⣿⡷⣿⣯⣿⣿⣿⣇⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣤⡈⢷⢹⣿⣿⣿⣿⣿⣿⠁⡿⢟⣿⣿⣿⣹⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠁⠉⠻⣿⣿⠟⠀⠘⢸⣿⣿⡿⣡⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠘⠀⠀⠀⢠⣭⣭⣵⣾⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣀⠀⠀⠀⠀⠀⣀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠙⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠓⠒⠛⠓⠚⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠋⠀""")
    if Pokemon_level == 10:
        Pokemon_name = "Pikachu"
        print("Pokemon's name is")
        print(Pokemon_name)
        print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠿⠛⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⡸⠁⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⡀⢀⠀⠀⠀⠀⠀⠀⢀⠔⠋⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⠇⠀⠀⢰⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠤⠒⠊⠉⠉⠁⣽⣿⣿⡿⠋⠀⠀⠀⠀⣠⠖⠁⠀⠀⠈⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⢀⠇⢀⣀⣀⣀⣀⣀⠀⠀⠀⢀⡠⠔⠊⠁⠀⠀⠀⠀⠀⠀⢠⣿⡿⠋⠁⠀⠀⠀⣠⠞⠁⠀⠀⠀⠀⠀⡄⠀
⠀⠀⠀⠀⠀⠀⠀⢸⣀⠴⠋⠉⠁⠀⠀⠀⠀⠀⠉⠙⠖⠉⠀⠀⠀⠀⠀⠀⠀⠀⣀⠴⠛⠁⠀⠀⠀⠀⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⢠⠀
⠀⠀⠀⠀⠀⠀⢀⠞⠁⠀⠀⠀⠀⠀⠀⣾⢙⣶⡄⠀⠀⠰⢤⣠⡤⠤⠔⠒⠂⠉⠀⠀⠀⠀⠀⠀⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠀
⠀⠀⠀⠀⠀⠀⣮⣞⣹⠀⠀⠀⠀⠀⠀⠙⠿⠿⠃⠀⠀⠀⠀⠈⢳⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠜⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠼⠃
⠀⠀⠀⠀⠀⢰⠛⠿⠁⣈⣀⣀⣀⣤⠀⠀⠀⢠⠖⠒⠲⡄⠀⠀⠀⡆⠀⠀⠀⠀⠀⠀⠀⢰⠧⠤⠔⠂⠐⠈⠈⠀⠀⠀⣠⠔⠊⠁⠀⠀
⠀⠀⠀⠀⢠⡟⣇⠀⠉⢿⣿⣿⣿⣿⠀⠀⠀⢯⡐⠲⣠⡇⠀⠀⠀⢳⠀⠀⠀⠀⠀⠀⠀⠘⡄⠀⠀⠀⠀⠀⠀⣠⠔⠋⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠸⣦⡟⠀⠀⠈⢿⠟⠛⢻⠀⠀⠀⠀⠙⠚⠋⠀⠀⠀⠀⠀⢇⠀⠀⠀⠀⠀⠀⠀⠘⡄⠀⠀⠀⠔⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠹⣄⠀⠀⠀⠀⠳⣄⡼⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⡀⠈⢆⠀⠀⠀⠀⠀⠀⠀⠹⡀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣀⠬⠷⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⠚⠃⠢⢄⠀⠈⢣⡀⠀⠀⠀⠀⠀⢀⡽⠀⠀⢸⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣤⠔⠊⠁⠀⠀⠀⠈⠳⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⢿⠁⠀⠀⠀⠈⠀⠀⠘⡿⢆⠀⠀⣠⠔⠉⠀⠀⣀⠜⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠐⡏⠸⠀⠀⠀⠀⠀⠀⠀⢢⠀⠈⠳⢄⣀⠀⠀⠀⠀⠈⢧⡀⠀⠀⠀⣀⡀⠀⠀⠀⠱⡈⠣⡀⠀⢠⠚⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠻⠦⢤⣀⠀⠀⠀⠀⠀⠀⢣⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠤⠼⠛⠁⠀⠀⠀⠀⠘⣆⠙⢶⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠉⠉⠙⠒⠒⠒⠒⢣⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⠳⣾⣿⣿⡿⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⠿⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⡘⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠱⡀⠀⠀⠀⣀⡤⠔⠲⣶⣆⣀⡀⠀⠐⠤⠤⠔⠒⠉⠀⣰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠒⠤⣥⠤⢴⠚⠉⠀⠀⠀⠈⠉⠒⠂⠤⠤⢤⡤⠞⢻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣾⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢧⣀⣸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢋⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⢿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")
    if Pokemon_level == 15:
        Pokemon_name = "Raichu"
        print("Pokemon's name is")
        print(Pokemon_name)
        print("""⬜⬜⬜⬜⬜⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬛🏿⬛⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬛🏿🏿⬛⬜⬜⬜⬜⬛⬛🏿🏿⬛⬜⬜⬜⬜⬜⬛⬜⬜
⬜⬜⬜⬛🏿⬛⬜⬜⬜⬜⬛🏿🟨🟨🟨⬜⬜⬜⬜⬜⬜⬛⬜⬜
⬜⬜⬜⬛🏿⬛⬛⬛⬛⬛🏿🟨🟨🟨🟨⬛⬜⬜⬜⬜⬛🟨⬛⬜
⬜⬜⬛🟧🟧🟧🟧🟧⬛🏿🏿🟨🟨⬛⬛⬛⬜⬜⬜⬜⬛🟨⬛⬜
⬜⬛🟧🟧🟧🟧🟧🟧🟧🏿🏿🟨⬛⬜⬜⬛⬜⬜⬜⬜⬛🟨⬛⬛
⬛⬜🟧🟧🟧🟧🟧🟧🟧🟧🟧⬛⬛⬜⬜⬜⬜⬜⬜⬜⬛🟨🟨⬛
⬛⬛🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧⬛⬜⬜⬜⬜⬜⬜⬜⬛🟨🟨⬛
⬛🟧🟧🟧🟧⬜⬛🟧🟧🟧🟧🟧🏿⬛⬜⬜⬜⬛⬛⬛🟨🟨🟨⬛
⬜⬛🟧🟧🟧⬛⬛🟨🟨🟧🟧🟧🟧⬛⬜⬜⬛🏿🟨🟨🟨⬛⬛⬜
⬜⬜⬛🟧🟧🟧🟧🟨🟨🟧🟧🟧🟧🏿⬛⬜⬛⬛⬛🟨🟨⬛⬜⬜
⬜⬛🏿🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🏿⬛⬜⬛⬜⬜⬛🟨⬛⬜⬜
⬜⬜⬛⬛⬜⬜🟧🟧🟧🟧🟧🟧⬛🟧⬛⬜⬛⬛⬛⬜⬛⬜⬜⬜
⬜⬜⬜⬜⬛⬜⬜⬜🟧⬛🟧🟧⬛🟧⬛⬜⬜⬜⬛⬛⬜⬜⬜⬜
⬜⬜⬜⬜⬛⬜⬜⬜⬜⬛🏿⬛🟧🟧⬛⬛⬛⬜⬜⬛⬜⬜⬜⬜
⬜⬜⬜⬛🏿⬛⬜⬜⬜⬜⬛🟧🟧🟧⬛⬜⬛⬛⬛⬛⬜⬜⬜⬜
⬜⬜⬜⬛⬛⬛⬛⬛⬜⬜🟧🟧🟧⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛🟧⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🏿🟧🟧⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜""")

# The name of the file where the game data will be saved
save_file = "pokemon_game_save.txt"

# Function to save the current game state
def save_game():
    with open(save_file, "w") as file:  # Open the save file in write mode
        file.write(pokemon_name + "\n")  # Write the Pokémon's name
        file.write(str(pokemon_level) + "\n")  # Write the Pokémon's level (converted to string), followed by a newline
    print("Game saved successfully!")

# Function to load a previously saved game state
def load_game():
    global pokemon_name, pokemon_level  # Declare these as global
    try:
        with open(save_file, "r") as file:  # Open the save file in read mode
            pokemon_name = file.readline().strip()  # Read the Pokémon's name and remove any extra whitespace
            pokemon_level = int(file.readline().strip())  # Read the Pokémon's level and convert it to an integer
        print("Game loaded successfully!")
    except FileNotFoundError:
        # If the save file doesn't exist, display this message
        print("No save file found. Start a new game!")
    except ValueError:
        # If the file data is corrupted, display this message
        print("Save file is corrupted. Start a new game!")


