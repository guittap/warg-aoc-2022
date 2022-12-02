with open('input.txt') as f:
    lines = f.read().splitlines()

answer=0

# for i in range(1,len(lines)):
#     if int(lines[i])>int(lines[i-1]):
#         answer+=1


for i in range(3,len(lines)):
    if int(lines[i])+int(lines[i-1])+int(lines[i-2]) > int(lines[i-1])+int(lines[i-2])+int(lines[i-3]):
         answer+=1


print(answer)