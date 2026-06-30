from mapgen import generate_map

def print_map(game_map):
    for row in game_map:
        print("".join(row))

if __name__ == "__main__":
    dungeon = generate_map()
    print_map(dungeon)
    