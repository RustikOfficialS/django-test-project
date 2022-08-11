size = 10
array = [[0]*size for i in range(size)]
i = 1
x = 0
y = -1
x_change = 0
y_change = 1
length = len(str(size**2))

while i <= size**2:
    if 0 <= x + x_change < size and 0 <= y + y_change < size and array[x+x_change][y+y_change] == 0:
        x += x_change
        y += y_change
        array[x][y] = i
        i += 1
    else:
        if y_change == 1:
            y_change = 0
            x_change = 1
        elif x_change == 1:
            x_change = 0
            y_change = -1
        elif y_change == -1:
            y_change = 0
            x_change = -1
        elif x_change == -1:
            x_change = 0
            y_change = 1

for m in array:
    for el in m:
        print(str(el).rjust(length),end=' ')
    print()