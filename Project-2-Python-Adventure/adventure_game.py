print("Adventure Game Setup Succesfull")
def start_game():
    print("Welcome, adventurer!")
    print("You are on a quest to find the legendary treasure.")
    
    # Ask for player's name
    player_name = input("What is your name, brave explorer? ")
    print(f"Good luck, {player_name}!")
    
    # Present choices
    print("You have two paths ahead:")
    print("1. Explore the dark forest")
    print("2. Enter the mysterious cave")
    
    choice = input("Enter 1 or 2 to choose your path: ")
    
    if choice == "1":
        forest_path()
    elif choice == "2":
        cave_path()
    else:
        print("Invalid choice. Please restart the game and select 1 or 2.")

def forest_path():
    print("You step into the dark forest, searching for the legendary treasure.")
    print("You have two choices:")
    print("1. Follow the river")
    print("2. Climb a tree")
    
    choice = input("Enter 1 or 2 to choose your path: ")
    
    if choice == "1":
        print("You follow the river, and after a long journey, you discover a hidden cave.")
        print("Inside the cave, you find the legendary treasure shining brightly!")
        print("Congratulations, brave explorer! You have won the game!")
    else:
        print("You climb the tree, but slip and fall. Game over!")

def cave_path():
    print("You enter the mysterious cave, searching for the legendary treasure.")
    print("You have two choices:")
    print("1. Light a torch")
    print("2. Proceed in the dark")
    
    choice = input("Enter 1 or 2 to choose your path: ")
    
    if choice == "1":
        print("You light the torch, and the cave walls glow to reveal the legendary treasure. You win!")
    else:
        print("You proceed in the dark, lose your way, and never find the treasure. Game over!")
        
def main():
    while True:
        start_game()
        
        restart = input("Do you want to play again? (yes/no): ").lower()
        if restart == "yes":
            continue
        elif restart == "no":
            print("Thanks for playing! Goodbye!")
            break
        else:
            print("Invalid input. Exiting the game.")
            break
main()  