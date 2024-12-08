#!/usr/bin/env python3

import copy
import sys

# https://adventofcode.com/2024/day/6/input
local_file = "06.input"

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

def countMoves(map):
  location = currentLocation(map)
  next = None
  change = None
  direction = 0
  moves = 0

  #print(f"Starting at {location}")

  while True:
    x, y = location

    if direction == 0:
      change = (0, -1)
    elif direction == 90:
      change = (1, 0)
    elif direction == 180:
      change = (0, 1)
    elif direction == 270:
      change = (-1, 0)

    next = (x + change[0], y + change[1])
    #print(f"Location: {location} Next: {next}")

    if next[1] >= len(map) or next[1] < 0 or next[0] >= len(map[next[1]]) or next[0] < 0:
      #print(f"Found edge at {next}")
      break
    elif map[next[1]][next[0]] in ["#","O"]:
      direction = turnNinetyDegrees(direction)
      #print(f"Found wall at {next}. Changing direction to {direction}")
      continue
    elif map[next[1]][next[0]] in [".","X", "^"]:
      if map[next[1]][next[0]] in ["."]:
        moves += 1
      if map[next[1]][next[0]] != "^":
        map[next[1]][next[0]] = 'X'
      #print(f"{state in visitedStates} BEEP")
      #print(f"Moved from {location} to {next}")
      location = next
      continue
    else:
      print(f"Unexpected: {map[next[1]][next[0]]} at {next}")

  return moves

def detectLoop(map):
  location = currentLocation(map)
  next = None
  change = None
  direction = 0
  visitedStates = set()

  # print(f"Starting at {location}")

  while True:
    x, y = location

    if direction == 0:
      change = (0, -1)
    elif direction == 90:
      change = (1, 0)
    elif direction == 180:
      change = (0, 1)
    elif direction == 270:
      change = (-1, 0)

    next = (x + change[0], y + change[1])
    #print(f"Location: {location} Next: {next}")

    if next[1] >= len(map) or next[1] < 0 or next[0] >= len(map[next[1]]) or next[0] < 0:
      #print(f"Found edge at {next}")
      return False
    elif map[next[1]][next[0]] in ["#","O"]:
      direction = turnNinetyDegrees(direction)
      #print(f"Found wall at {next}. Changing direction to {direction}")
      continue
    elif map[next[1]][next[0]] in [".","X", "O", "^"]:
      if map[next[1]][next[0]] != "^":
        map[next[1]][next[0]] = 'X'
      state = (location, direction)
      # print(f"{state} BEEP")
      if state in visitedStates:
        # print(f"Found loop at {next}")
        return True
      visitedStates.add(state)
      #print(f"Moved from {location} to {next}")
      location = next
      continue
    else:
      print(f"Unexpected: {map[next[1]][next[0]]} at {next}")
  return False

def printMap(map):
  for y in range(len(map)):
    for x in range(len(map[y])):
      print(map[y][x], end="")
    print()

# PART ONE
total = 0

lines =  map.split("\n")
mapMatrix = []
for y in range(len(lines)):
  if len(lines[y]) > 0:
    mapMatrix.append([])
    for x in range(len(lines[y])):
      mapMatrix[y].append(lines[y][x])

mapCounts = copy.deepcopy(mapMatrix)
print(f"Moves: {countMoves(mapCounts) + 1}")

# PART TWO
# TODO: Refactor this. It is extremely slow.
mapLoops = copy.deepcopy(mapMatrix)
loops = 0

for y in range(len(mapLoops)):
  for x in range(len(mapLoops[y])):
    if mapLoops[y][x] == ".":
      mapCopy = copy.deepcopy(mapLoops)
      mapCopy[y][x] = "O"
      if detectLoop(mapCopy):
        loops += 1

print(f"Found {loops} loops")
