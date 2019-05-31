

import sys
# generator
g = (i * 2 for i in range(10000) if i % 3 == 0 or i % 5 == 0)
print(sys.getsizeof(g))
# list comprehension
l = [i * 2 for i in range(10000) if i % 3 == 0 or i % 5 == 0]
print(sys.getsizeof(l))