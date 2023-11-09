#Phase 1

# labyrinth = [
#    "███████",
#    "█     █",
 #   "█   ███",
 #   "█ ███ █",
 #   "█     █",
 #   "███████"]

# def print_labyrinth(lab: list[str]):
    #for rows in lab:
        #print(rows)

#print_labyrinth(labyrinth)


#Phase 2

def prompt_integer(message: str) -> int:
    while True:
        user_input = input(message)
        if user_input.isdigit():
            return int(user_input)
        else:
            print("Please enter a valid integer.")

def prompt_user_for_location(name: str) -> tuple[int, int]:
    row = prompt_integer(f"Row of {name}: ")
    column = prompt_integer(f"Column of {name}: ")
    return row, column

#Phase 3

from collections import deque

def bfs(lab: list[str], start: tuple[int, int], end: tuple[int, int]) -> list[tuple[int, int]]:
    queue = deque([[start]])
    visited = set()
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while queue:
        path = queue.popleft()
        last = path[-1]
        if last == end:
            return path

        if last not in visited:
            visited.add(last)

            for move in moves:
                next_location = (last[0] + move[0], last[1] + move[1])

                if is_traversable(lab, next_location):
                    new_path = path + [next_location]
                    queue.append(new_path)

    return []

def is_traversable(lab: list[str], location: tuple[int, int]) -> bool:
    row, col = location
    return 0 <= row < len(lab) and 0 <= col < len(lab[0]) and lab[row][col] != '█'

def print_labyrinth(lab: list[str], path: list[tuple[int, int]] = None):
    if path:
        for row, line in enumerate(lab):
            for element in path:
                if element[0] == row:
                    lab[row] = replace_at_index(line, "X", element[1])
    for line in lab:
        print(line)

def replace_at_index(s: str, r: str, idx: int) -> str:
    return s[:idx] + r + s[idx + len(r):]


labyrinth = [
    "███████",
    "█     █",
    "█   ███",
    "█ ███ █",
    "█     █",
    "███████"]


start_location = prompt_user_for_location("start")
end_location = prompt_user_for_location("end")
path = bfs(labyrinth, start_location, end_location)

example_path = [(1, 1), (2, 1), (3, 1), (4, 1), (4, 2), (4, 3)]
print_labyrinth(labyrinth, example_path)