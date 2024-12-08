#!/usr/bin/env python3

import copy
import sys

# https://adventofcode.com/2024/day/8/input
local_file = "08.input"

try:
  with open(local_file, "r") as file:
    data = file.read()
except FileNotFoundError:
  print(f"Error: The file '{local_file}' was not found. Please cache it first.")
  sys.exit(1)

total = 0

antenae = {}
map = []
mapHeight = len(data.split("\n"))
mapWidth = len(data.split("\n")[0])

for y, line in enumerate(data.split("\n")):
  if y not in map:
    map.append([])
  if len(line) > 0:
    for x, point in enumerate(line):
      map[y].append(point)
      if point != '.':
        if point not in antenae:
          antenae[point] = []
        antenae[point].append((x, y))

mapTwo = copy.deepcopy(map)

antinodes = set()

for signal in antenae:
  for i, hit in enumerate(antenae[signal]):
    for j in range(i+1, len(antenae[signal])):
      ptOne = antenae[signal][i]
      ptTwo = antenae[signal][j]
      yDist = ptOne[1] - ptTwo[1]
      xDist = ptOne[0] - ptTwo[0]
      antOne = (ptOne[0] + xDist, ptOne[1] + yDist)
      antTwo = (ptTwo[0] - xDist, ptTwo[1] - yDist)
      # print(f"Signal {signal} Points {ptOne} {ptTwo} xdist {xDist} ydist {yDist} Antinodes {antOne} {antTwo} MapHeight {mapHeight} MapWidth {mapWidth}")
      if antOne[0] >= 0 and antOne[1] >= 0 and antOne[0] < mapWidth and antOne[1] < mapHeight - 1:
        antinodes.add(antOne)
        map[antOne[1]][antOne[0]] = "#"
      if antTwo[0] >= 0 and antTwo[1] >= 0 and antTwo[0] < mapWidth and antTwo[1] < mapHeight - 1:
        map[antTwo[1]][antTwo[0]] = "#"
        antinodes.add(antTwo)

# Print map with antinodes
for line in map:
  for point in line:
    print(point, end="")
  print("")


antinodesTwo = set()
for signal in antenae:
  for i, hit in enumerate(antenae[signal]):
    for j in range(i+1, len(antenae[signal])):
      ptOne = antenae[signal][i]
      ptTwo = antenae[signal][j]
      antinodesTwo.add(ptOne)
      antinodesTwo.add(ptTwo)
      yDist = ptOne[1] - ptTwo[1]
      xDist = ptOne[0] - ptTwo[0]

      while True:
        antOne = (ptOne[0] + xDist, ptOne[1] + yDist)
        if antOne[0] >= 0 and antOne[1] >= 0 and antOne[0] < mapWidth and antOne[1] < mapHeight - 1:
          antinodesTwo.add(antOne)
          mapTwo[antOne[1]][antOne[0]] = "#"
          ptOne = antOne
        else:
          break

      while True:
        antTwo = (ptTwo[0] - xDist, ptTwo[1] - yDist)
        if antTwo[0] >= 0 and antTwo[1] >= 0 and antTwo[0] < mapWidth and antTwo[1] < mapHeight - 1:
          antinodesTwo.add(antTwo)
          mapTwo[antTwo[1]][antTwo[0]] = "#"
          ptTwo = antTwo
        else:
          break

# Print map with antinodes
for line in mapTwo:
  for point in line:
    print(point, end="")
  print("")

print(f"Part one antinode count: {len(antinodes)}")
print(f"Part two antinode count: {len(antinodesTwo)}")
