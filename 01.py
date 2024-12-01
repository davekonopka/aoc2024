#!/usr/bin/env python3

import sys

# https://adventofcode.com/2024/day/1/input
local_file = "01.input"

try:
  with open(local_file, "r") as file:
    data = file.read()

  # Parse the data into two lists
  listOne = []
  listTwo = []

  for line in data.strip().split('\n'):
    num1, num2 = map(int, line.split())
    listOne.append(num1)
    listTwo.append(num2)

except FileNotFoundError:
  print(f"Error: The file '{local_file}' was not found. Please cache it first.")
  sys.exit(1)

listOne.sort()
listTwo.sort()

distance = 0
similarity = 0

for index, value in enumerate(listOne):
  distance += abs(value - listTwo[index])
  similarity += value * listTwo.count(value)

print(f"Distance: {distance}")
print(f"Similarity: {similarity}")
