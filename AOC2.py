import re

with open("AOC2.txt") as f:
    s = f.read()

input_red = 12
input_blue = 14
input_green = 13

valid_games = []

games = s.strip().split("\n")

for game in games:
    game_id, game_data = game.split(":")
    sets = game_data.split(";")
    cube = game_data.split(",")
    cubes = {'red': 0, 'blue': 0, 'green': 0}
    valid = True

    for set_info in sets:
        colors = re.findall(r'(\d+) (\w+)', set_info)

        for count, color in colors:
            cubes[color] += int(count)

        if cubes['red'] > input_red or cubes['blue'] > input_blue or cubes['green'] > input_green:
            valid = False
            break

    if valid and cubes['red'] <= input_red and cubes['blue'] <= input_blue and cubes['green'] <= input_green:
        valid_games.append(game_id.strip())
        print("Valid game:", game_id.strip(), "Cubes:", cubes)

print("Possible games:", valid_games)
print("Sum of IDs:", sum(map(int, [game.split()[1] for game in valid_games])))
