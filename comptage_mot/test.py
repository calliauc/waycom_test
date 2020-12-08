d1 = {'a': 1, 'b': 15, 'c': 3, 'd': 7, 'a1': 5, 'b1': 10, 'c1': 8, 'd1': 6}

print(f"{d1}")

d1= sorted(d1.items(), key=lambda t: t[1])

print(f"{d1}")
