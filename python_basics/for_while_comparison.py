import time


start_time = time.time()
i_while = 0

while time.time() - start_time < 1:
    i_while += 1

for_start_time = time.time()

j = 0
for _ in range(i_while):
    j += 1

for_time = time.time() - for_start_time

assert for_time > 1, "While loop time: 1s, iterations: {}, For loop time {}".format(i_while, for_time)

# print("While loop time: 1s, iterations: {}, For loop time {}".format(i_while, for_time))
