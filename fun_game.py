# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do"
# "I have not given or received any unauthorized aid on this assignment."
#
# Names:
# Rosana Casellas
# Abigail Yannetta
# Ryan Petty
# Giselle Mendieta
# Section: 565
# Assignment: Team Lab 13
# Date: 7 November 2024

#   _____
#  /     \
# |  O O  |
# |   ^   |    <-- can we get extra credit for our artwork please?
# |  \_/  |         We had about 1,000 points in mind.
#  \_____/


#    / \__
#   (    @\___ 
#   /         O   <-- Frodo
#  /   (_____/
# /     |   

import csv
import turtle

characters_data = []  # initialize data list

# open file to read
try:
    with open('superhero_characters.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # convert to integers
            row['Damage Level'] = int(row['Damage Level'])
            row['Health Level'] = int(row['Health Level'])
            characters_data.append(row)
except FileNotFoundError:
    print("Error: File 'superhero_characters.csv' not found.")
    exit()
except ValueError as e:
    print(f"Error in data conversion: {e}")
    exit()

# initial variables
player_scores = {"Player 1": 100, "Player 2": 100}
winning_score = 500

# display rules
def display_rules(bullet_point='\u2022'):
    """
    Display the game rules for players.
    """
    print('Welcome to the Marvel & D.C. Battle Game!')
    print(f'    {bullet_point} Each player starts with 100 points.')
    print(f'    {bullet_point} Take turns choosing a character to battle.')
    print(f'    {bullet_point} The damage and health levels of the characters determine the outcome.')
    print(f'    {bullet_point} Your goal is to reach {winning_score} points before the other player.')
    print(f'    {bullet_point} Select a character and fight!')
    print(f'    {bullet_point} You\'ll see an updated score for each player after each round.')
    return None  # Explicit return

# current scores function
def display_score(player_scores):
    """
    Display the current score for players. 
    """
    print("\nCurrent Scores:")
    for player, score in player_scores.items():
        print(f"{player}: {score} points")
    return player_scores  # Explicit return

# list of available characters for reference
available_characters = [char['Character'] for char in characters_data]

# Function for player to select character
def select_character(player, characters_data, available_characters):
    """Allow the player to choose a character for the battle.
    Returns selected character's stats.
    """

    while True:
        print(f"\n{player}, would you like to view the list of characters or enter a name directly?")
        print("1. View list of characters")
        print("2. Enter character name")

        choice = input("Enter 1 or 2: ")
        if choice == "1":
            for index, name in enumerate(available_characters):
                print(f"{index + 1}. {name}")
        elif choice == "2":
            character_name = input("Enter the name of your chosen character: ").strip()
            for character in characters_data:
                if character['Character'].lower() == character_name.lower():
                    print(f"\n{player} chose {character['Character']}!")
                    return character  # Return character data
            print("Sorry, that character does not exist. Try again!")
        else:
            print("Invalid choice. Please select 1 or 2.")

# Function to simulate a battle and update scores
def battle(player1, player2, character1, character2, player_scores):
    """Battle between two chosen characters based on their stats.
    Updates player scores based on the outcome and provides descriptive messages.
    """
    
    # Retrieve powers for each character
    player1_power = character1['Primary Power']
    player2_power = character2['Primary Power']
    
    # Calculate battle results based on Damage and Health Levels
    player1_damage = character1['Damage Level']
    player2_health = character2['Health Level']
    player2_damage = character2['Damage Level']
    player1_health = character1['Health Level']
    
    # Descriptive battle messages based on powers
    print(f"\n{player1}'s {character1['Character']} unleashes {player1_power}!")
    print(f"{player2}'s {character2['Character']} retaliates with {player2_power}!")
    
    # Player 1's attack on Player 2
    if player1_damage > player2_health:
        points_earned = player1_damage - player2_health
        player_scores[player1] += points_earned
        print(f"{character1['Character']} lands a crushing blow, overpowering {character2['Character']} with {player1_power}!")
        print(f"{player1} earns {points_earned} points!")
    else:
        points_lost = player2_health - player1_damage
        player_scores[player1] = max(0, player_scores[player1] - points_lost)
        print(f"{character2['Character']} withstands the attack, countering {character1['Character']} with {player2_power}!")
        print(f"{player1} loses {points_lost} points.")
    
    # Player 2's attack on Player 1
    if player2_damage > player1_health:
        points_earned = player2_damage - player1_health
        player_scores[player2] += points_earned
        print(f"{character2['Character']} retaliates fiercely, striking back with {player2_power}!")
        print(f"{player2} earns {points_earned} points!")
    else:
        points_lost = player1_health - player2_damage
        player_scores[player2] = max(0, player_scores[player2] - points_lost)
        print(f"{character1['Character']} absorbs the damage, defending with {player1_power}!")
        print(f"{player2} loses {points_lost} points.")
    
    # Display updated scores
    return display_score(player_scores)  # Explicit return of updated scores

# Function to draw fireworks and display "You Win" message using Turtle
def draw_fireworks_and_message(message="You Win!"):
    """Draw fireworks and display 'You Win' message using Turtle graphics.
    """
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("black")
    
    # Create the turtle object for fireworks
    firework = turtle.Turtle()
    firework.shape("turtle")
    firework.color("yellow")
    firework.speed(10)
    
    # Function to draw a firework burst
    def draw_firework(radius):
        """"
        Draws fireworks.
        """
        firework.penup()
        firework.goto(0, 0)
        firework.pendown()
        for _ in range(36):  # 36 points for a full circle
            firework.forward(radius)
            firework.backward(radius)
            firework.left(10)
    
    # Draw multiple fireworks
    for radius in range(50, 200, 50):
        draw_firework(radius)
    
    # Create another turtle for text
    text_turtle = turtle.Turtle()
    text_turtle.hideturtle()
    text_turtle.color("white")
    text_turtle.penup()
    text_turtle.goto(0, -250)
    text_turtle.write(message, align="center", font=("Arial", 36, "bold"))
    
    # Hide the firework turtle after drawing
    firework.hideturtle()
    
    # Keep window open until clicked
    screen.exitonclick()

# Main game function with turn-based logic
def play_game(characters_data, player_scores, winning_score):
    """
    Main function to run the game, handling player turns and game logic.
    """
    display_rules()
    
    while True:
        # Player 1 chooses character
        print("\nPlayer 1's turn to choose a character:")
        character1 = select_character("Player 1", characters_data, available_characters)
        
        # Player 2 chooses character
        print("\nPlayer 2's turn to choose a character:")
        character2 = select_character("Player 2", characters_data, available_characters)
        
        if character1 and character2:
            # Run the battle with chosen characters
            updated_scores = battle("Player 1", "Player 2", character1, character2, player_scores)
            
            # Check for winning condition
            if updated_scores["Player 1"] >= winning_score:
                print(f"\nPlayer 1 wins the game by reaching {winning_score} points!")
                draw_fireworks_and_message("Player 1 Wins!")
                break
            elif updated_scores["Player 2"] >= winning_score:
                print(f"\nPlayer 2 wins the game by reaching {winning_score} points!")
                draw_fireworks_and_message("Player 2 Wins!")
                break
    
        while True:
            continue_game = input("\nDo you want to continue? (yes/no): ").lower()
            if continue_game == "yes":
                break
            elif continue_game == "no":
                print('Thanks for playing!')
                return
            else:
                print('Invalid input. Please enter yes or no.')

# Run the game
play_game(characters_data, player_scores, winning_score)