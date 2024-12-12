#!/usr/bin/env python3

import copy
import sys

# https://adventofcode.com/2024/day/9/input
local_file = "09.input"

def checksum(line):
  checksum = 0
  for i in range(len(line)):
    if line[i] != ".":
      checksum += int(line[i]) * i
  return checksum

try:
  with open(local_file, "r") as file:
    data = file.read()
except FileNotFoundError:
  print(f"Error: The file '{local_file}' was not found. Please cache it first.")
  sys.exit(1)

line = data.split('\n')[0]
values = [int(x) for x in line]

checksum = 0
block = 0
end = len(values) - 1

for i, value in enumerate(values):
  if i % 2==0:
    for _ in (range(value)):
      checksum += ((i // 2)*block)
      block += 1
      print((i // 2), end='')
  elif end > i:
    for _ in range(value):
      while end > i and values[end] == 0:
          end -= 2
      if end <= i:
          break
      checksum += ((end // 2) * block)
      print((end // 2), end='')
      block += 1
      values[end] -= 1

print()
print(checksum)
