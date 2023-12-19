## Set comprehension

l = [10, 20, 3, 4, 10, 10, 20, 7, 3]

s1 = {x for x in l if x%2==0}

s2 = {x for x in l if x%2!=0}

print(s1)

print(s2)

# output
# {10, 20, 4}
# {3, 7}