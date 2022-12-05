with open('input.txt') as f:
    lines = f.read().splitlines()

#print(lines)
print(lines[0])
print(lines[0][:int(len(lines[0])/2)])
for i in lines[0][:int(len(lines[0])/2)]:
    if i in lines[0][int(len(lines[0])/2):]:
        print(i)

count=0
amount=0

for i in lines:
    for j in i[:int(len(i)/2)]:
        if j in i[int(len(i)/2):]:
            if j.isupper():
                count+=ord(j)-38
            else:
                count+=ord(j)-96
            amount+=1
            break

print(count)
print(amount)
print(ord("A")-38)

part2=0
for i in range (int(len(lines)/3)):
    j = list(set(lines[i*3])&set(lines[i*3+1])&set(lines[i*3+2]))[0]
    if j.isupper():
        part2+=ord(j)-38
    else:
        part2+=ord(j)-96

print(part2)