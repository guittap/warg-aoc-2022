with open('input.txt') as f:
    lines = f.read().splitlines()

calories = []
total = 0
for i in lines:
    if i=="":
        calories.append(total)
        total = 0
    else:
        total += int(i)

calories.sort()
print("part 1: " + str(max(calories)))
print("part 2: " + str(sum(calories[len(calories)-3:])))