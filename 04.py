#!/usr/bin/env python3

import copy
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

def checkMatrixPoint(matrix, x, y, length):
  words = ["XMAS"]
  # up
  if y >= 3:
    if "".join([matrix[y-i][x]["char"] for i in range(0, length)]) in words:
      for i in range(0, length):
        matrix[y-i][x]["hit"] = True
  # down
  if y + 4 <= len(matrix):
    if "".join([matrix[y+i][x]["char"] for i in range(0, length)]) in words:
      for i in range(0, length):
        matrix[y+i][x]["hit"] = True
  # left
  if x >= 3:
    if "".join([matrix[y][x-i]["char"] for i in range(0, length)]) in words:
      for i in range(0, length):
        matrix[y][x-i]["hit"] = True
    # up-left
    if y >= 3:
      if y == 9 and x == 3:
        print("".join([matrix[y-i][x-i]["char"] for i in range(0, length)]))
      if "".join([matrix[y-i][x-i]["char"] for i in range(0, length)]) in words:
        for i in range(0, length):
          matrix[y-i][x-i]["hit"] = True
    # down-left
    if y + 4 <= len(matrix):
      if "".join([matrix[y+i][x-i]["char"] for i in range(0, length)]) in words:
        for i in range(0, length):
          matrix[y+i][x-i]["hit"] = True
  # right
  if x + 4 <= len(matrix[y]):
    if "".join([matrix[y][x+i]["char"] for i in range(0, length)]) in words:
      for i in range(0, length):
        matrix[y][x+i]["hit"] = True
    # up-right
    if y >= 3:
      if "".join([matrix[y-i][x+i]["char"] for i in range(0, length)]) in words:
        for i in range(0, length):
          matrix[y-i][x+i]["hit"] = True
    # down-right
    if y + 4 <= len(matrix):
      if "".join([matrix[y+i][x+i]["char"] for i in range(0, length)]) in words:
        for i in range(0, length):
          matrix[y+i][x+i]["hit"] = True
  return matrix

def printMatrix(matrix):
  matrixCopy = copy.deepcopy(matrix)

  # Build visual matrix
  for y in range(0, len(matrixCopy)):
    for x in range(0, len(matrixCopy[y])):
      matrixCopy[y][x] = { "char": matrixCopy[y][x], "hit": False }

  for y in range(0, len(matrixCopy)):
    for x in range(0, len(matrixCopy[y])):
      processedMatrix = checkMatrixPoint(matrixCopy, x, y, 4)

  for y in range(0, len(matrixCopy)):
    for x in range(0, len(matrixCopy[y])):
      if matrixCopy[y][x]["hit"]:
        color = "31m"
      else:
        color = "32m"
      print(f"\033[{color}{matrixCopy[y][x]["char"]}\033[0m", end="")
    print()

matrix = [list(line) for line in data.strip().split("\n")]

# Count the number of times the word "XMAS" appears in the matrix
count = 0
words = ["XMAS"]
for y in range(0, len(matrix)):
  for x in range(0, len(matrix[y])):
    directions = []
    if x >= 3:
      directions.append("left")
      if y >= 3:
        directions.append("up-left")
      if y + 4 <= len(matrix):
        directions.append("down-left")
    if x + 4 <= len(matrix[0]):
      directions.append("right")
      if y >= 3:
        directions.append("up-right")
      if y + 4 <= len(matrix):
        directions.append("down-right")
    if y >= 3:
      directions.append("up")
    if y + 4 <= len(matrix):
      directions.append("down")

    for direction in directions:
      word = getWord(matrix, x, y, direction, 4)
      if word in words:
        count += 1

printMatrix(matrix)
print(f"count: {count}")
