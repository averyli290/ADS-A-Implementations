from random import shuffle
from profiler import profile_time, get_random_lists


def separate(L, start, end, p_index):
    # i keeps track of the rightmost element of set less than p
    # i + 1 is next available spot for element less than p
    L[-1], L[p_index] = L[p_index], L[-1]
    p = L[-1]
    i = start - 1
    for j in range(start, end):
        if L[j] <= p:
            i += 1
            L[i], L[j] = L[j], L[i]

    # Swap the element to right of all elements <= p and p
    # all elements to right of p now greater than p
    L[i + 1], L[end] = L[end], L[i + 1]

    # returns index before pivot index
    return i


def magicmedian(L, k="default"):
    # This works for 0-indexing on k
    if k == "default":
        k = (len(L) - 1) // 2

    if len(L) <= 120:
        return sorted(L)[k]

    # Getting median of medians
    groups = [L[i * 5:(i + 1) * 5] for i in range(len(L) // 5 + 1)]
    if groups[-1] == []:
        groups.remove([])

    medians = [sorted(group)[len(group) // 2] for group in groups]

    median_of_medians = magicmedian(medians, len(medians) // 2)

    # Getting index before pivot position
    m = separate(L, 0, len(L) - 1, L.index(median_of_medians))

    if k < m + 1:
        return magicmedian(L[:m + 1], k)
    if k == m + 1:
        return L[k]
    return magicmedian(L[m + 2:], k - (m + 2))

# I get a coefficient of about 1.3, though it is inconsistent and tends to
# increase a bit for larger test cases
#profile_time(magicmedian, get_random_lists([1000, 10000, 50000, 100000]), complexity=lambda n: n, num_trials=5)


