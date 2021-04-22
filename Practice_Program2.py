#Find second smallest number in the list.

li = []
n = int(input("Enter number of element"))

for i in range(1, n+1):
    elem = int(input("Enter elements"))
    li.append(elem)
li.sort()

print(li)
print("Second largest is", li[n-2])