#taking multiple inputs
input_lst=[int(x) for x in input("Enter a value: ").split()]
a, b, c, d, e = input_lst
print(f"{a}+{b}+{c}+{d}+{e} is: ", sum(input_lst))
d = {2:1, 3:2, 1:4}
x, y, z=d
print(x, y, z)