#!/usr/bin/env python3

from collections import defaultdict

input_file = open('input.txt', 'r')
lines = input_file.readlines()

part1_ans=0
part2_ans=0

for line in lines:
	ok = True
	id_, line = line.split(':')
	dict = defaultdict(int)
	for event in line.split(';'):
		for balls in event.split(','):
			n,color = balls.split()
			n = int(n)
			if n > {'red':12, 'green':13, 'blue':14}.get(color, 0):
				ok = False
			dict[color] = max(dict[color], n)
	if ok:
		part1_ans += int(id_.split()[-1])
	power = 1
	for val in dict.values():
		power *= val
	part2_ans += power

print("Part 1 answer: " + str(part1_ans))
print("Part 2 answer: " + str(part2_ans))