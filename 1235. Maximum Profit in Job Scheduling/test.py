from operator import itemgetter,attrgetter,methodcaller
from functools import cmp_to_key

def mycmp(t1, t2):
    if t1[0] != t2[0]:
        return t1[0] - t2[0]
    elif t1[1] != t2[1]:
        return t1[1] - t2[1]
    else:
        return t1[2] - t2[2]

if __name__ == "__main__":
    A = [(1,2,3),(2,3,2),(2,2,1),(2,2,3)]
    # A.sort(key=itemgetter(0,1))
    A.sort(key=cmp_to_key(mycmp))
    print(A)