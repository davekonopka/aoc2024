#!/usr/bin/env python3

import copy
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
