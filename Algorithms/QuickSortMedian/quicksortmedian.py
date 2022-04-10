from random import shuffle
from math import log


def quicksort(L, start="default", end="default"):
    if start == "default":
        start = 0
        end = len(L) - 1

    if end <= start:
        return

    m = separate(L, start, end)
    quicksort(L, start, m)
    quicksort(L, m + 2, end)

    # No need to return because edits list in place


def separate(L, start, end):
    # i keeps track of the rightmost element of set less than p
    # i + 1 is next available spot for element less than p
    p = L[end]
    i = start - 1
    for j in range(start, end):
        if L[j] <= p:
            i += 1
            L[i], L[j] = L[j], L[i]

    # Swap the element to right of all elements <= p and p
    # all elements to right of p now greater than p
    L[i + 1], L[end] = L[end], L[i + 1]

    # returns pivot index
    return i

'''
Pseudocode
run m = separate
base case: m = k, return L[k]
if k > m, run median on right sublist
otherwise run median on left sublist


'''


def quickmedian(L, start, end, k):
    m = separate(L, start, end)
    if k == m + 2:
        return L[k - 1]
    if k > m + 2:
        return quickmedian(L, m + 2, end, k)
    return quickmedian(L, start, m, k)

