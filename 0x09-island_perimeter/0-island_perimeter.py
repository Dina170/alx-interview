#!/usr/bin/python3
"""Creates a function def island_perimeter(grid): that returns the perimeter of the island described in grid:

 - grid is a list of list of integers:
    - 0 represents water
    - 1 represents land
    - Each cell is square, with a side length of 1
    - Cells are connected horizontally/vertically (not diagonally).
    - grid is rectangular, with its width and height not exceeding 100
 - The grid is completely surrounded by water
 - There is only one island (or nothing).
 - The island doesn’t have “lakes” (water inside that isn’t connected to the water surrounding the island).
"""


def island_perimeter(grid):
    """returns the perimeter of the island described in grid"""
    perimeter = 0
    r, c = len(grid), len(grid[0])
    for i in range(r):
        for j in range(c):
            if grid[i][j] == 1:
                perimeter += 4
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 1
                if i < r - 1 and grid[i + 1][j] == 1:
                    perimeter -= 1
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 1
                if j < c - 1 and grid[i][j + 1] == 1:
                    perimeter -= 1

    return perimeter
