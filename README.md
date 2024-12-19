# Superhero Game

## Overview
The **Superhero Game** is an interactive, turn-based game where two players select superheroes from a CSV dataset and engage in battles to determine the ultimate champion. Each player starts with a fixed score, and the game continues until one of the players reaches the winning score threshold.

## Features
- **Character Selection**: Players choose from a diverse list of superheroes, each with unique attributes.
- **Turn-Based Battles**: Players take turns selecting characters and battling based on predefined stats like damage and health levels.
- **Dynamic Scoring**: Scores are updated in real-time based on the battle outcomes.
- **Win Condition**: A player wins by reaching the winning score first.
- **Fireworks Celebration**: The winner is greeted with a graphical fireworks display using Python's `turtle` module.

---

## Game Rules
1. Each player starts with 100 points.
2. Players take turns choosing a character for battle.
3. Battles are resolved using the following stats from the CSV file:
   - **Damage Level**: Determines the attacking power.
   - **Health Level**: Determines the ability to withstand damage.
4. Points are added or deducted based on the outcome of each battle:
   - A player gains points if their character overpowers the opponent.
   - A player loses points if their character is overpowered.
5. The first player to reach the winning score (default: 500 points) is declared the winner.
6. Players may choose to continue or end the game after each round.

---

## File Requirements
The program requires a CSV file named `superhero_characters.csv` containing the following fields:
- **Character**: The name of the superhero.
- **Damage Level**: An integer representing the character's attack power.
- **Health Level**: An integer representing the character's defense ability.
- **Primary Power**: A brief description of the character's special power.

Ensure the file is in the same directory as the Python script.

---

## How to Play
1. Run the program in a Python environment.
2. Follow the on-screen prompts:
   - View the list of available characters.
   - Enter the name of your chosen character.
3. Observe the battle results and the updated scores.
4. Continue playing until a player reaches the winning score.

---

## Modules Used
- **`csv`**: For reading the superhero data from the CSV file.
- **`turtle`**: For creating a celebratory fireworks display.

---

## Error Handling
- If the required CSV file is not found, the program will terminate with an error message.
- If invalid data is encountered in the CSV file, the program will display a conversion error and terminate.
- Input validation ensures that players can only make valid choices.

---

## Example Gameplay
1. **Game Start**:
   - Players are welcomed and presented with the game rules.
   - Initial scores are displayed.
2. **Character Selection**:
   - Player 1 chooses Spider-Man.
   - Player 2 chooses Batman.
3. **Battle**:
   - Spider-Man uses web-slinging to attack Batman.
   - Scores are updated based on the damage and health levels.
4. **Continue or End**:
   - Players decide whether to continue the game.
5. **Victory**:
   - A player reaches the winning score, and a fireworks display celebrates the victory.

---

## Contributors
- Rosana Casellas
- Abigail Yannetta
- Ryan Petty
- Giselle Mendieta

---

## License
This project is for educational purposes and is governed by the Texas A&M University honor code: "Aggies do not lie, cheat, or steal, or tolerate those who do."

