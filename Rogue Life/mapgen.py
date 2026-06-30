import random
from tiles import WALL, FLOOR
from room import Room

def create_empty_map(width, height):
    return [[WALL for _ in range(width)] for _ in range(height)]

def carve_room(game_map, room):
    for y in range(room.y, room.y + room.h):
        for x in range(room.x, room.x + room.w):
            game_map[y][x] = FLOOR

def place_door(game_map, x, y):
    if game_map[y][x] == WALL:
        game_map[y][x] = '+'

def carve_h_tunnel(game_map, x1, x2, y):
    start = min(x1, x2)
    end = max(x1, x2)

    # carve the corridor
    for x in range(start, end + 1):
        game_map[y][x] = FLOOR

    # door at left entrance
    if start - 1 >= 0 and game_map[y][start - 1] == WALL:
        place_door(game_map, start - 1, y)

    # door at right entrance
    if end + 1 < len(game_map[0]) and game_map[y][end + 1] == WALL:
        place_door(game_map, end + 1, y)




def carve_v_tunnel(game_map, y1, y2, x):
    start = min(y1, y2)
    end = max(y1, y2)

    # carve the corridor
    for y in range(start, end + 1):
        game_map[y][x] = FLOOR

    # door at top entrance
    if start - 1 >= 0 and game_map[start - 1][x] == WALL:
        place_door(game_map, x, start - 1)

    # door at bottom entrance
    if end + 1 < len(game_map) and game_map[end + 1][x] == WALL:
        place_door(game_map, x, end + 1)



def generate_map(width=60, height=25, max_rooms=10, min_size=5, max_size=12):
    game_map = create_empty_map(width, height)
    rooms = []

    for _ in range(max_rooms):
        w = random.randint(min_size, max_size)
        h = random.randint(min_size, max_size)
        x = random.randint(1, width - w - 1)
        y = random.randint(1, height - h - 1)

        new_room = Room(x, y, w, h)

        if any(new_room.intersects(other) for other in rooms):
            continue

        carve_room(game_map, new_room)

        if rooms:
            prev_center = rooms[-1].center()
            new_center = new_room.center()

            carve_h_tunnel(game_map, prev_center[0], new_center[0], prev_center[1])
            carve_v_tunnel(game_map, prev_center[1], new_center[1], new_center[0])

        rooms.append(new_room)

    return game_map

