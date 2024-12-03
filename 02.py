#!/usr/bin/env python3

import sys

# https://adventofcode.com/2024/day/2/input
local_file = "02.input"

def getTrend(reading, lastReading):
  if reading > lastReading:
    return 1
  elif reading < lastReading:
    return -1
  else:
    return 0

def isSafe(line, dampen=False):
  readings = line.split(' ')
  fails = 0
  for index, reading in enumerate(readings):
    if index >= 1:
      # Change is more than 3 or less than 1
      if not (1 <= abs(int(readings[index-1]) - int(reading)) <= 3):
        fails += 1
      if index > 1:
        # Trend is different from the last trend
        trend = getTrend(int(reading), int(readings[index-1]))
        lastTrend = getTrend(int(readings[index-1]), int(readings[index-2]))
        if trend != lastTrend:
          fails += 1
    if fails > 0:
      if dampen:
        for i in range(0, len(readings)):
          dampenedReadings = readings[:i] + readings[i + 1:]
          if isSafe(' '.join(dampenedReadings), False):
            return True
      return False
  return True

try:
  with open(local_file, "r") as file:
    data = file.read()
except FileNotFoundError:
  print(f"Error: The file '{local_file}' was not found. Please cache it first.")
  sys.exit(1)


safeCount = 0
unsafeCount = 0
for line in data.strip().split('\n'):
  if isSafe(line, True):
    safeCount += 1
  else:
    unsafeCount += 1

print(f"Safe lines: {safeCount}")
print(f"Unsafe lines: {unsafeCount}")

