from math import floor

def rank(T,A):
    L = 0
    R = len(A) - 1
    while L <= R:
        m = int(floor((L+R)/2))
        if A[m] < T:
            L = m + 1
        elif A[m] > T:
            R = m - 1
        else:
            return m
    return -1

if __name__ == '__main__':
    print(rank(8,[1,2,3,4,5,7,8]))
