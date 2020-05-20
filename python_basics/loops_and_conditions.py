

i = 0

while i < 10:
    print(i)
    i += 1  # i++, e.g. i *= n

a_list = [1, 2, 3]
a_dict = {
    "2nd": 2,
    "1st": 1,
    "3rd": 3
}

for a in a_list:
    print(a)

for key, value in a_dict.items():
    print(key, value)

b_list = []
for i in range(1, 11):
    b_list.append(i)

print(b_list)

a, b = 1, 2
if a == b:
    print("A={} equal to B={}".format(a, b))
elif a != b:
    print("A={} not equal to B={}".format(a, b))
else:
    print("Sth went wrong")

if a:
    print("a exists {}".format(a))

if 1 not in b_list:
    print("1 in b_list={}".format(b_list))

c_list = [i for i in range(1, 11) if i % 2 == 0]
print(c_list)
