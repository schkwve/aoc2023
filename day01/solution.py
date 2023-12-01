#!/usr/bin/env python3

input_file = open('input.txt', 'r')
lines = input_file.readlines()

part1_total = 0
part2_total = 0

for line in lines:
	numbers = []
	for j, c in enumerate(line):
		if c.isdigit():
			numbers.append(c)
	if len(numbers) > 0:
		part1_total += int(numbers[0] + numbers[-1])

for line in lines:
	numbers = []
	for j, c in enumerate(line):
		if c.isdigit():
			numbers.append(c)
		for value, name in enumerate(["one", "two", "three","four","five","six","seven","eight","nine"]):
			if line[j:].startswith(name):
				numbers.append(str(value + 1))
	if len(numbers) > 0:
		part2_total += int(numbers[0] + numbers[-1])

print("Part 1 answer: " + str(part1_total))
print("Part 2 answer: " + str(part2_total))