
a = 3
a += 9
# make the "a" variable's value bigger by 10

print(a)



b = 100
b -=92
# make b smaller by 7



print(b)



c = 44
c *=2
# please double c's value



print(c)



d = 125
d /= 5
# please divide by 5 d's value



print(d)



e = 8
e = e**3
# please cube of e's value



print(e)



f1 = 123

f2 = 345

f = f1 > f2
print("f1 is bigger than f2: {}".format(f))

# tell if f1 is bigger than f2 (pras a boolean)



g1 = 350

g2 = 200
g = g1*2 > g1
# tell if the double of g2 is bigger than g1 (pras a boolean)
print("if the double of g2 is bigger than g1: {}".format(g))


h = 1357988018575474

# tell if 11 is a divisor of h (pras a boolean)
h1 = (h %11 == 0)
print("if 11 is a divisor of h: {}".format(h1))


i1 = 10

i2 = 3

# tell if i1 is higher than i2 squared and smaller than i2 cubed (pras a boolean)

i = ((i1 > (i2*i2)) and (i1 < (i2**3)))

print("if i1 is higher than i2 squared and smaller than i2 cubed: {}".format(i))

j = 1521

# tell if j is divisible by 3 or 5 (pras a boolean)

j1 = ((j%3 == 0) or (j%5 ==0))
print("If j is divisible by 3 or 5: {}".format(j1))

