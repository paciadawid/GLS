a_int = 1  # integer, no upper limit
b_int = a_int
b_int = 2
print(a_int, b_int)

a_float = 1.0  # float, no upper limit

print(1/2)  # -> float
print(1//2)  # -> int

a_string = "1.0"  # string -> list of chars
print(a_string[0])

a_list = [1, "2", 3, 4]  # list
print(a_list[0])  # first element
print(a_list[-1])  # last element
print(a_list[1:2])  # 2nd & 3rd element
print(a_list[1:])  # all elements from 2nd

b_list = a_list  # reference to a_list
b_list[0] = 2
print(a_list, b_list)

c_list = list(a_list)  # new object

a_dict = {
    "2nd": 2,
    "1st": 1
}

print(a_dict["1st"])

a_bool = True
a_bool2 = -1  # anything else than 0, None, [] & {} is True
print(bool(a_bool2))

a_tuple = (1, 2)  # tuple -> krotka, immutable, e.g not allowed del a_tuple[0], a_tuple[0] = 1

# a = [x for x in range(10) if xyz]