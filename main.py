x = int(input("Enter x:\n"))

if x < 0:
    y = -4
elif x < 1 and x >= 0:
    y = x * x + 3 * x + 4
elif x >= 1:
    y = 2

print(y)
