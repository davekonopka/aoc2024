#!/usr/bin/env python3

from itertools import product
import sys

# https://adventofcode.com/2024/day/7/input
local_file = "07.input"

try:
  with open(local_file, "r") as file:
    data = file.read()
except FileNotFoundError:
  print(f"Error: The file '{local_file}' was not found. Please cache it first.")
  sys.exit(1)

def sumWorkingResults(values, answer):
  total = 0
  # Generate all combinations of operations
  operations = list(product(["+", "*"], repeat=len(values) - 1))

  # Evaluate each combination
  for ops in operations:
    result = int(values[0])
    expression = f"{values[0]}"
    for i, op in enumerate(ops):
        if op == "+":
            result += int(values[i + 1])
        elif op == "*":
            result *= int(values[i + 1])
        expression += f" {op} {values[i + 1]}"
    print(f"Combination: {expression}, Result: {result}")
    if result == int(answer):
      total += result
      break
  return total

totes = 0
for line in data.split("\n"):
  if len(line) > 0:
    parts = line.split(":")
    answer = parts[0].strip()
    values = parts[1].strip().split(" ")
    print(f"Answer: {answer} Values: {values}")

    totes += sumWorkingResults(values, answer)

print(f"Total: {totes}")
