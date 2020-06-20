import random
def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def partittion(A):
    i=0
    j=0
    k=len(A)
    mid = 2  # 1,2,3 represents the colors

    while (j<k):
        if (A[j] < mid):
            swap(A, i, j)
            i += 1
            j += 1
        elif (A[j] > mid):
            k -= 1
            swap(A, j, k)
        else:
            j += 1


def main():
    A = []
    size = random.randint(10, 20)
    for i in range(size):
        A.append(random.choice([1,2,3]))

    print(A)
    partittion(A)
    print(A)


main()