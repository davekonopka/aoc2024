#!/usr/bin/env python3

import re
import sys

# https://adventofcode.com/2024/day/3/input
local_file = "06.input"

sys.setrecursionlimit(10000)

try:
  with open(local_file, "r") as file:
    map = file.read()
except FileNotFoundError:
  print(f"Error: The file '{local_file}' was not found. Please cache it first.")
  sys.exit(1)

def currentLocation(map):
  for y, line in enumerate(map):
    for x, char in enumerate(line):
      if char == "^":
        return (x, y)
  return None

def turnNinetyDegrees(direction):
  return (direction + 90) % 360

def move(map, location, direction):
  x, y = location
  next = None
  if direction == 0:
    next = (x, y - 1)
  elif direction == 90:
    next = (x + 1, y)
  elif direction == 180:
    next = (x, y + 1)
  elif direction == 270:
    next = (x - 1, y)

  if next[1] >= len(map) or next[0] >= len(map[next[1]]):
    print(f"Found edge at {next}")
    next = location
  elif map[next[1]][next[0]] == "#":
    print(f"Found wall at {next}")
    return move(map, location, turnNinetyDegrees(direction))
  elif map[next[1]][next[0]] in [".","X"]:
    print(f"Moved from {location} to {next}")
    map[next[1]][next[0]] = 'X'
    next = move(map, next, direction)
    return(next)
  else:
    print(f"Unexpected: {map[next[1]][next[0]]} at {next}")

  return (next)


total = 0

lines =  map.split("\n")
mapMatrix = []
for y in range(len(lines)):
  if len(lines[y]) > 0:
    mapMatrix.append([])
    for x in range(len(lines[y])):
      mapMatrix[y].append(lines[y][x])

startingPoint = currentLocation(mapMatrix)
mapMatrix[startingPoint[1]][startingPoint[0]] = 'X'

print(f"{move(mapMatrix, startingPoint, 0)}")

count = 0
for y in range(len(mapMatrix)):
  if len(mapMatrix[y]) > 0:
    for x in range(len(mapMatrix[y])):
      if mapMatrix[y][x] == 'X':
        count += 1
      print(mapMatrix[y][x], end="")
  print()

print(f"Total: {count}")
