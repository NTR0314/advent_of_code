import copy

a = 1
b = lambda x: print(copy.copy(a))
a = 2
b(None)