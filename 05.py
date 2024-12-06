#!/usr/bin/env python3

import copy
import sys

# https://adventofcode.com/2024/day/5/input
order_file = "05.input"
print_file = "05-prints.input"

try:
  with open(order_file, "r") as file:
    order = file.read()
except FileNotFoundError:
  print(f"Error: The file '{order_file}' was not found. Please cache it first.")
  sys.exit(1)

try:
  with open(print_file, "r") as file:
    prints = file.read()
except FileNotFoundError:
  print(f"Error: The file '{print_file}' was not found. Please cache it first.")
  sys.exit(1)

ordering = {}
for line in order.split("\n"):
  rule = line.split("|")
  if len(rule) == 2:
    if not rule[0] in ordering:
      ordering[rule[0]] = []
    ordering[rule[0]].append(rule[1])

count = 0

def checkOrder(numbers, ordering):
  for number in numbers:
    if number in ordering:
      for second in ordering[number]:
        if second in numbers:
          if numbers.index(number) > numbers.index(second):
            return False
  return True

def fixOrder(numbers, ordering):
  for number in numbers:
    if number in ordering:
      for second in ordering[number]:
        if second in numbers:
          if numbers.index(number) > numbers.index(second):
            to_move = numbers.pop(numbers.index(number))
            numbers.insert(numbers.index(second), to_move)
  return numbers

secondCount = 0

for line in prints.split("\n"):
  prints = line.split(",")
  # part one
  if len(line) > 0 and checkOrder(prints, ordering):
    count += int(prints[len(prints)//2])

  # part two
  if len(line) > 0:
    printsCopy = copy.deepcopy(prints)
    fixed = fixOrder(printsCopy, ordering)
    if fixed != prints:
      secondCount += int(fixed[len(fixed)//2])

print(f"first count: {count}")
print(f"second count: {secondCount}")
