print("Example pattern: ")
res = []
for i in range(1, 7):
    if i < 6:
        res.append(i * "*")
        print(i * "*")
    else:
        res.pop(-1)
        res.reverse()
        print(*res, sep='\n')

print("Now you choose the size!")

res = []

pattern = False
while pattern == False:
    try:
        limit = int(input("Please enter a number to specify the widest point in the pattern: ")) + 2
        pattern = True
    except ValueError:
        print("Please enter a valid entry")
        continue

for i in range(1, limit):
    if i < (limit - 1):
        res.append(i * "*")
        print(i * "*")
    else:
        res.pop(-1)
        res.reverse()
        print(*res, sep='\n')