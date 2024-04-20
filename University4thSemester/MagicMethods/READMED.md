# Iterative Maze Solver

## Description

This project provides an iterative implementation of an algorithm for traversing a maze. It simulates a program stack using a list. Additionally, it includes a function `printMaze` to visualize the maze with walls represented by '#' characters, the necessary path by empty spaces ' ', the path traversed in the forward direction by '.' characters, in the backward direction by 'x', and the goal by 'g'. When the goal is reached, this function can be used to print the current state of the maze.

## Problem Statement

Given a maze represented as a 2D list where '#' represents walls and ' ' represents paths, along with the starting coordinates `(x, y)` and the goal coordinates `(goal_x, goal_y)`, the task is to find a path from the starting point to the goal point using an iterative algorithm.

## Functionality

- **Function Name**: `solveMaze(x, y)`
- **Description**: This function solves the maze starting from the specified initial coordinates `(x, y)`.
- **Parameters**:
  - `x`: The x-coordinate of the starting point.
  - `y`: The y-coordinate of the starting point.

## Usage

### Example

```python
# Define your maze
maze = [
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#'],
    ['#', '#', '#', ' ', '#', ' ', '#', '#', '#', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
]

# Example usage of solveMaze function
solveMaze(1, 1)  # Start solving maze from coordinates (1, 1)
