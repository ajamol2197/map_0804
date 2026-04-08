# 1
a = [2]
print(a)

b = list(map(lambda g: g * g, a))
print(b)

# 2
x = ["salom123", 'hello345']
print(x)

a = list(map(lambda d: d.isalpha(), x))
print(a)

# 3
x = [6, 7, 8]

a = list(map(lambda d: d * d, x))
print(a)

# 4
a = ['salom', 'hello']
print(a)

h = list(map(lambda v: f"{v}!", a))
print(h)

# 5
a = [8, 9 , 7]
print(a)

c = list(map(lambda f: f + f + f, a,))
print(c)


# 6
a = ["ALI", 'VALI']
print(a)

v = list(map(lambda b: b.lower(), a))
print(v)

# 7
a = [8, 9, 7]
print(a)

c = list(map(lambda f: f * 100, a,))
print(c)

# 8
a = ['ali', 'vali']
print(a)

c = list(map(lambda f: f[-1], a,))
print(c)

# 9
a = [8, 9, 7]
print(a)

c = list(map(lambda f: f * f, a,))
print(c)
