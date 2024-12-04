#!/usr/bin/env python3

import re
import sys

# https://adventofcode.com/2024/day/3/input
local_file = "03.input"

try:
  with open(local_file, "r") as file:
    data = file.read()
except FileNotFoundError:
  print(f"Error: The file '{local_file}' was not found. Please cache it first.")
  sys.exit(1)

total = 0
pattern = r"mul\((\d+),(\d+)\)"
for match in re.finditer(pattern, data):
  total += int(match.group(1)) * int(match.group(2))

print(f"Total: {total}")
