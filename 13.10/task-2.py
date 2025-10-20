vector = [1, 5, 8, 3, 10, 7, 2]
A = 3
B = 8

count = sum(1 for x in vector if A <= x <= B)

print(f"Количество элементов в интервале [{A}, {B}] = {count}")
