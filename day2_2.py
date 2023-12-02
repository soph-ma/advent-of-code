"""
--- Part Two ---
The Elf says they've stopped producing snow because they aren't getting any water! He isn't sure why the water stopped; however, he can show you how to get to the water source to check it out for yourself. It's just up ahead!

As you continue your walk, the Elf poses a second question: in each game you played, what is the fewest number of cubes of each color that could have been in the bag to make the game possible?

Again consider the example games from earlier:

Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
In game 1, the game could have been played with as few as 4 red, 2 green, and 6 blue cubes. If any color had even one fewer cube, the game would have been impossible.
Game 2 could have been played with a minimum of 1 red, 3 green, and 4 blue cubes.
Game 3 must have been played with at least 20 red, 13 green, and 6 blue cubes.
Game 4 required at least 14 red, 3 green, and 15 blue cubes.
Game 5 needed no fewer than 6 red, 3 green, and 2 blue cubes in the bag.
The power of a set of cubes is equal to the numbers of red, green, and blue cubes multiplied together. The power of the minimum set of cubes in game 1 is 48. In games 2-5 it was 12, 1560, 630, and 36, respectively. Adding up these five powers produces the sum 2286.

For each game, find the minimum set of cubes that must have been present. What is the sum of the power of these sets?
"""
import re

def get_sum_of_powers(input: str) -> int: 
    games = input.split("\n")
    powers_sum = 0
    for game in games: 
        max_values = {
            "red": 0, 
            "green": 0, 
            "blue": 0
        }
        game_sets = re.split("[:,;]", game)[1:]
        for s in game_sets: 
            number = int(s.split()[0])
            color = s.split()[1]
            max_values[color] = max(number, max_values[color])
        power = max_values["red"] * max_values["green"] * max_values["blue"]
        powers_sum += power
    return powers_sum
            
        

if __name__ == "__main__": 
    with open("day2_input.txt", mode="r", encoding="utf-8") as file: 
        input = file.read()
        powers_sum = get_sum_of_powers(input=input)
        print(powers_sum)