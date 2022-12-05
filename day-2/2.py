with open('input.txt') as f:
    lines = f.read().splitlines()

part1 = 0
for i in lines:
    if i == 'A X':
        part1+=1+3
    elif i == 'B X':
        part1+=1+0
    elif i == 'C X':
        part1+=1+6
    elif i == 'A Y':
        part1+=2+6
    elif i == 'B Y':
        part1+=2+3
    elif i == 'C Y':
        part1+=2+0
    elif i == 'A Z':
        part1+=3+0
    elif i == 'B Z':
        part1+=3+6
    elif i == 'C Z':
        part1+=3+3

print("part 1: " + str(part1))

part2=0

for i in lines:
    if i == 'A X':
        part2+=3+0
    elif i == 'B X':
        part2+=1+0
    elif i == 'C X':
        part2+=2+0
    elif i == 'A Y':
        part2+=1+3
    elif i == 'B Y':
        part2+=2+3
    elif i == 'C Y':
        part2+=3+3
    elif i == 'A Z':
        part2+=2+6
    elif i == 'B Z':
        part2+=3+6
    elif i == 'C Z':
        part2+=1+6

print("part 2: " + str(part2))