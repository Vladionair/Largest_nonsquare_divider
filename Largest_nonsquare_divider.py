def square_free_part(n):
    if n == 1:
        return n
    values_1 = []
    values_2 = []
    non_square = []
    for i in range(2, n + 1):
        if n % i == 0:
            values_1.append(i)
    while values_1:
        value = values_1.pop(0)
        for j in range(2, value + 1):
            if value % j == 0:
                values_2.append(j)
        for k in range(2, int(value ** (1 / 2)) + 1):
            if k ** 2 in values_2:
                values_2 = []
                break
        if values_2 != []:
            non_square.append(value)
            values_2 = []
    return max(non_square) 

print(square_free_part(1000))