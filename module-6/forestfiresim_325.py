"""Forest Fire Simulation for CSD-325
Modified by Jared Morris and team
Based on forestfiresim.py by Sue Sampson and Al Sweigart.

Module 6 changes:
1. Added a permanent lake near the center of the display.
2. Added the WATER character, shown in blue.
3. Prevented trees, fire, and new growth from replacing water.
4. Made the lake act as a firebreak because fire spreads only to TREE cells.

Press Ctrl-C to stop the simulation.
"""

import random
import sys
import time

try:
    import bext
except ImportError:
    print("This program requires the bext module.")
    print("Install it with: python -m pip install bext")
    sys.exit()

WIDTH = 79
HEIGHT = 22

TREE = "A"
FIRE = "@"
EMPTY = " "
WATER = "~"

INITIAL_TREE_DENSITY = 0.20
GROW_CHANCE = 0.01
FIRE_CHANCE = 0.01
PAUSE_LENGTH = 0.5

LAKE_CENTER_X = WIDTH // 2
LAKE_CENTER_Y = HEIGHT // 2
LAKE_RADIUS_X = 10
LAKE_RADIUS_Y = 4


def is_lake_position(x, y):
    """Return True when the coordinate belongs to the oval-shaped lake."""
    horizontal = ((x - LAKE_CENTER_X) ** 2) / (LAKE_RADIUS_X ** 2)
    vertical = ((y - LAKE_CENTER_Y) ** 2) / (LAKE_RADIUS_Y ** 2)
    return horizontal + vertical <= 1


def main():
    """Run the simulation until Ctrl-C is pressed."""
    forest = create_new_forest()
    bext.clear()

    while True:
        display_forest(forest)

        next_forest = {
            "width": forest["width"],
            "height": forest["height"],
        }

        for x in range(forest["width"]):
            for y in range(forest["height"]):
                if (x, y) in next_forest:
                    continue

                current_pixel = forest[(x, y)]

                if current_pixel == WATER:
                    next_forest[(x, y)] = WATER

                elif current_pixel == EMPTY and random.random() <= GROW_CHANCE:
                    next_forest[(x, y)] = TREE

                elif current_pixel == TREE and random.random() <= FIRE_CHANCE:
                    next_forest[(x, y)] = FIRE

                elif current_pixel == FIRE:
                    for ix in range(-1, 2):
                        for iy in range(-1, 2):
                            neighbor = (x + ix, y + iy)
                            if forest.get(neighbor) == TREE:
                                next_forest[neighbor] = FIRE

                    next_forest[(x, y)] = EMPTY

                else:
                    next_forest[(x, y)] = current_pixel

        forest = next_forest
        time.sleep(PAUSE_LENGTH)


def create_new_forest():
    """Create the initial forest and place the permanent lake."""
    forest = {"width": WIDTH, "height": HEIGHT}

    for x in range(WIDTH):
        for y in range(HEIGHT):
            if is_lake_position(x, y):
                forest[(x, y)] = WATER
            elif (random.random() * 100) <= INITIAL_TREE_DENSITY:
                forest[(x, y)] = TREE
            else:
                forest[(x, y)] = EMPTY

    return forest


def display_forest(forest):
    """Display trees, fire, empty spaces, and blue water."""
    bext.goto(0, 0)

    for y in range(forest["height"]):
        for x in range(forest["width"]):
            pixel = forest[(x, y)]

            if pixel == TREE:
                bext.fg("green")
                print(TREE, end="")
            elif pixel == FIRE:
                bext.fg("red")
                print(FIRE, end="")
            elif pixel == WATER:
                bext.fg("blue")
                print(WATER, end="")
            else:
                print(EMPTY, end="")

        print()

    bext.fg("reset")
    print(f"Grow chance: {GROW_CHANCE * 100}%  ", end="")
    print(f"Lightning chance: {FIRE_CHANCE * 100}%  ", end="")
    print("Press Ctrl-C to quit.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        bext.fg("reset")
        print("\nSimulation ended.")
        sys.exit()
