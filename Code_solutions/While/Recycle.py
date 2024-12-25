empty = 0
total = 0
full = int(input("Enter the quantity of new bottles:"))

while full:
    # Serve bottles
    total += full
    empty += full
    full = 0

    # Recycle
    full = empty // 3
    empty = empty % 3

print("You can use " + str(total) + " bottles")