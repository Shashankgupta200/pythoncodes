# interchanging the elements at different location
def swap(b, p1, p2):
    t = b[p1]
    b[p1] = b[p2]
    b[p2] = t
    return b

a = [1, 2, 3, 4, 5, 6]
print(a)
print(swap(a, 1, 2))