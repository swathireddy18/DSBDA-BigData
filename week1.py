#linear search
l = list()
n = int(input("Enter number of elements to be inserted into list : "))
print("Enter",n,"values")
for i in range(n):
    l.append(int(input()))
s = int(input("Enter element to be searched : "))
for i in range(len(l)):
    if l[i] == s:
        print(s, "is found at position", i+1)
        break
else:
    print("Element is not found")

#binary search
l = list()
n = int(input("Enter number of elements : "))
print("Enter",n,"values")
for i in range(n):
    l.append(int(input()))
l.sort()
s = int(input("Enter element to be searched : "))
low = 0
high = len(l) - 1
found = False
while low <= high:
    mid = (low+high) // 2
    if l[mid] == s:
        print(s, "is found at position", mid+1)
        found = True
        break
    elif l[mid] < s:
        low = mid + 1
    else:
        high = mid - 1
if not found:
    print(s,"Element is not found in list")
        
