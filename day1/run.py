with open("input.txt") as input:
    row1 = []
    row2 = []
    for line in input:
        lineArr = line.split()
        row1.append(int(lineArr[0]))
        row2.append(int(lineArr[1]))

    row1.sort()
    row2.sort()

    sum = 0
    for iter in range(len(row1)):
        count = row2.count(row1[iter])
        sum += row1[iter] * count

    print(sum)
