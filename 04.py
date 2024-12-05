#!/usr/bin/env python3

import re
import sys

# https://adventofcode.com/2024/day/4/input
local_file = "04.input"

try:
  with open(local_file, "r") as file:
    data = file.read()
except FileNotFoundError:
  print(f"Error: The file '{local_file}' was not found. Please cache it first.")
  sys.exit(1)

def getWord(matrix, x, y, direction, length):
  if direction == "up":
    return "".join([matrix[y-i][x] for i in range(0, length)])
  elif direction == "down":
    return "".join([matrix[y+i][x] for i in range(0, length)])
  elif direction == "left":
    return "".join([matrix[y][x-i] for i in range(0, length)])
  elif direction == "right":
    return "".join([matrix[y][x+i] for i in range(0, length)])
  elif direction == "up-left":
    return "".join([matrix[y-i][x-i] for i in range(0, length)])
  elif direction == "up-right":
    return "".join([matrix[y-i][x+i] for i in range(0, length)])
  elif direction == "down-left":
    return "".join([matrix[y+i][x-i] for i in range(0, length)])
  elif direction == "down-right":
    return "".join([matrix[y+i][x+i] for i in range(0, length)])
  return ""

matrix = [list(line) for line in data.strip().split("\n")]

count = 0
words = ["XMAS", "SAMX"]
for y in range(0, len(matrix)):
  for x in range(0, len(matrix[y])):
    directions = []
    # if x >= 4:
      # directions.append("left")
      # if y >= 4:
      #   directions.append("up-left")
      # if y <= len(matrix) - 4:
      #   directions.append("down-left")
    if x + 4 <= len(matrix[0]):
      directions.append("right")
      if y >= 4:
        directions.append("up-right")
      if y + 4 <= len(matrix):
        directions.append("down-right")
    # if y >= 4:
    #   directions.append("up")
    if y + 4 <= len(matrix):
      directions.append("down")

    for direction in directions:
      word = getWord(matrix, x, y, direction, 4)
      if word in words:
        print(f"word: {word}")
        count += 1
      else:
        print(f"*** word: {word}")

print(f"count: {count}")
