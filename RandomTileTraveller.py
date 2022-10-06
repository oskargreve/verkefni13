from typing import Tuple
import random

# Constants
NORTH = "n"
EAST = "e"
SOUTH = "s"
WEST = "w"

YES = "y"
NO = "n"

STARTING_LOCATION = (1, 1)
FINAL_DESTINATION = (3, 1)


def main():
    random_game()
    coins_total = 0
    move_total = 0
    previous_location = (0,0)
    location = STARTING_LOCATION
    while location != FINAL_DESTINATION:
        coins_total += pull_lever(location, previous_location, coins_total)
        previous_location = location
        move_total += 1
        location = play_one_move(location)

    print(f"Victory! Total coins {coins_total}. Moves {move_total}.")
    play_again()

def random_game():
    while True:
        try:
            seed = int(input("Input seed: "))
            random.seed(seed)
            return
        except ValueError:
            continue

def play_one_move(location: Tuple[int]) -> Tuple[int]:
    """Plays one move of the game.

    Returns updated location.
    """

    valid_directions = find_directions(location)
    direction = get_direction(valid_directions)

    if direction in valid_directions:
        location = move(direction, location)
    else:
        print("Not a valid direction!")

    return location


def find_directions(location: Tuple[int]) -> Tuple[str]:
    """Returns valid directions as a string given the supplied location."""

    if location == (1, 1):
        valid_directions = (NORTH,)
    elif location == (1, 2):
        valid_directions = NORTH, EAST, SOUTH
    elif location == (1, 3):
        valid_directions = EAST, SOUTH
    elif location == (2, 1):
        valid_directions = (NORTH,)
    elif location == (2, 2):
        valid_directions = SOUTH, WEST
    elif location == (2, 3):
        valid_directions = EAST, WEST
    elif location == (3, 2):
        valid_directions = NORTH, SOUTH
    elif location == (3, 3):
        valid_directions = SOUTH, WEST

    return valid_directions


def get_direction(valid_directions: Tuple[str]) -> str:
    print_directions(valid_directions)
    answer = random.choice([NORTH, EAST, SOUTH, WEST ]).lower()
    print(f"Direction: {answer}")
    return answer


def print_directions(available_directions: Tuple[str]) -> None:
    print("You can travel: ", end="")

    one_done_already = False
    for direction in available_directions:
        if one_done_already:
            print(" or ", end="")

        if direction == NORTH:
            print("(N)orth", end="")
        elif direction == EAST:
            print("(E)ast", end="")
        elif direction == SOUTH:
            print("(S)outh", end="")
        elif direction == WEST:
            print("(W)est", end="")

        one_done_already = True

    print(".")


def move(direction: str, location: Tuple[int]) -> Tuple[int]:
    """Returns updated location given the direction."""

    x, y = location

    if direction == NORTH:
        y += 1
    elif direction == SOUTH:
        y -= 1
    elif direction == EAST:
        x += 1
    elif direction == WEST:
        x -= 1

    return x, y

def pull_lever(location, previous_location, coins_total):
    coins = 0
    total_coins = coins_total + 1
    if previous_location != location:
        if location == (1, 2) or location == (2, 2) or location == (2,3) or location == (3,2):
            yes_or_no = random.choice([YES, NO])
            print(f"Pull a lever (y/n): {yes_or_no}")
            if yes_or_no.lower() == "y":
                coins += 1
                print(f"You received 1 coin, your total is now {total_coins}.")
            else:
                return coins
    return coins


def play_again():
    answer = input("Play again (y/n): ")
    if answer.lower() == "y":
        coins_total = 0
        move_total = 0
        previous_location = (0,0)
        location = STARTING_LOCATION
        while location != FINAL_DESTINATION:
            coins_total += pull_lever(location, previous_location, coins_total)
            previous_location = location
            move_total += 1
            location = play_one_move(location)

        print(f"Victory! Total coins {coins_total}. Moves {move_total}.")
        play_again()


if __name__ == "__main__":
    main()
