#!/usr/bin/env python3

import sys

# https://adventofcode.com/2024/day/10/input
local_file = "10.input"

try:
  with open(local_file, "r") as file:
    data = file.read()
except FileNotFoundError:
  print(f"Error: The file '{local_file}' was not found. Please cache it first.")
  sys.exit(1)

lines = data.strip().split('\n')

map = []
boundsY = (0, len(lines) - 1)
boundsX = (0, len(lines[0]) - 1)
starts = []

def getSteps(x, y, map):
  steps = []
  currentVal = int(map[y][x])

  possibleSteps = [ [x, y - 1], [x, y + 1], [x + 1, y], [x - 1, y]]

  for i, step in enumerate(possibleSteps.copy()):
    if step[0] < boundsX[0] or step[0] > boundsX[1] or step[1] < boundsY[0] or step[1] > boundsY[1]:
      possibleSteps.remove([step[0], step[1]])

  for step in possibleSteps:
    stepVal = int(map[step[1]][step[0]])
    if stepVal - currentVal == 1:
      steps.append([step[0], step[1]])

  return steps

def walkPath(x, y, map, complete = 0):
  steps = getSteps(x, y, map)
  val = int(map[y][x])
  for step in steps:
    stepVal = int(map[step[1]][step[0]])
    if val == 8 and stepVal == 9 and [step[0],step[1]] not in ends:
      ends.append([step[0],step[1]])
      complete += 1
    elif stepVal == val + 1:
      complete = walkPath(step[0], step[1], map, complete)
  return complete


# Build map[y][x] matrix from input
for y, line in enumerate(lines):
  if len(map) <= y:
    map.append([])
  for x, char in enumerate(line):
    map[y].append(char)
    if char == "0":
      starts.append([x,y])

paths = 0
for step in starts:
  ends = []
  paths = walkPath(step[0], step[1], map, paths)

print(paths)


