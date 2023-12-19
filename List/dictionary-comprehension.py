# Dictionary comprehension

# Problem 1
# l1 = [1, 3, 4, 2, 5]
# d1 = {x: x**3 for x in l1}
# print(d1)

# output
# {1: 1, 3: 27, 4: 64, 2: 8, 5: 125}

# Problem 2
# d2 = {x : f"ID{x}" for x in range(5)}
# print(d2)

# output
# {0: 'ID0', 1: 'ID1', 2: 'ID2', 3: 'ID3', 4: 'ID4'}

# Problem 3
l2 = [101, 103, 102]
l3 = ['gfg', 'ide', 'courses']
d3 = {l2[i] : l3[i] for i in range(len(l3))}
print(d3)

# Output
# {101: 'gfg', 103: 'ide', 102: 'courses'}