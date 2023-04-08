people = int(input())
giftRecieverList = list(map(int, input().strip().split()))
output = []


for i in range(people):
    output.append(list((giftRecieverList[i], (giftRecieverList.index(giftRecieverList[i])) + 1)))
# print(output)
# print(sorted(output))
a = sorted(output)
b = []
for i in a:
    b.append(i[1])
print(' '.join(map(str, b)))