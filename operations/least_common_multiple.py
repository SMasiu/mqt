def least_common_multiple(x, y):
    greater = x if x > y else y

    while True:
        if (greater % x == 0) and (greater % y == 0):
            lcm = greater
            break
        greater += 1

    return lcm
