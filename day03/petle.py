
i = 0

while i <= 3:
    print(i)
    i += 1


while True:
    i += 1
    print(i)
    if i >= 3:
        break

for x in range(1,100):
    print(x)
    if x >= 4:
        break

for x in range(1,3):
    for y in range(1,3):
        print('x', x, 'y', y)
