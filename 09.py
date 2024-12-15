#!/usr/bin/env python3

import itertools
import sys

# https://adventofcode.com/2024/day/9/input
local_file = "09.input"

try:
  with open(local_file, "r") as file:
    data = file.read()
except FileNotFoundError:
  print(f"Error: The file '{local_file}' was not found. Please cache it first.")
  sys.exit(1)

line = data.split('\n')[0]

blocks = []
disk_id = 0

for i in range(len(line)):
  if i % 2 == 0:
    blocks.extend([disk_id] * int(line[i]))
    disk_id += 1
  else:
    blocks.extend(["."] * int(line[i]))

# print(f"expanded: {blocks}")

for i in (i for i, x in enumerate(blocks) if x == "."):
  while blocks[-1] == ".":

    blocks.pop()

  if len(blocks) <= i:
    break

  blocks[i] = blocks.pop()

# print(f"defragged: {blocks}")

checksum = sum(i * int(x) for i, x in enumerate(blocks) if x != ".")
print(f"checksum: {checksum}")


# part two

line = data.split('\n')[0]
end = len(line)
disk = []

def isData(list):
  if len(list) < 1:
    return False
  for i in list:
    if i == -1:
      return False
  return True

for i in range(end):
  if i % 2 == 0:
    disk.append([i//2] * int(line[i]))
  else:
    disk.append([-1] * int(line[i]))

# TODO: Terribly slow, refactor to speed up
for end in range(len(disk) - 1, -1, -1):
  if isData(disk[end]):
    data = disk[end]
    for start in range(len(disk)):
      if end > start and not isData(disk[start]):
        space = disk[start]
        if len(space) >= len(data):
          data = disk.pop(end)
          space = disk.pop(start)

          for i in range(len(data)):
            space.pop()

          if len(space) > 0:
            disk.insert(start, space)

          disk.insert(start, data)

          offset = [-1] * (len(data))
          if len(offset) > 0:
            disk.insert(end, offset)

          break

flattened_disk = list(itertools.chain.from_iterable(disk))

checksum = sum(i * int(x) for i, x in enumerate(flattened_disk) if x != -1)
print(f"checksum: {checksum}")

