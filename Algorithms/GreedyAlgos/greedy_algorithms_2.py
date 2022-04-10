prices = [0, 1, 1, 2, 2, 4, 5, 5, 5, 10,
          12, 13, 16, 21, 21, 21, 21, 24,
          25, 25, 25, 25, 25, 26, 26, 26,
          27, 27, 27, 28, 28]


def rod_top_down(n, values=None):
    if values is None:
        values = {}
    value = 0
    if n in values:
        return values[n]
    for i in range(0, n):
        new_value = rod_top_down(i, values) + prices[n - i]
        value = max(value, new_value)
    values[n] = value
    return value


def rod_bottom_up(n):
    values = {0: 0}
    for length in range(1, n + 1):
        value = 0
        for i in range(0, length):
            new_value = values[i] + prices[length - i]
            value = max(value, new_value)
        values[length] = value
    return values[n]


def rod_with_instructions(n, splits=None):
    if splits is None:
        splits = {}
    split = []
    if n in splits:
        return splits[n]
    for i in range(0, n):
        new_split = rod_with_instructions(i, splits) + [n - i]
        if (sum([prices[k] for k in split])
                < sum([prices[k] for k in new_split])):
            split = new_split
    splits[n] = split
    return split


def max_sublist_sum(my_list):
    cur = to_ret = 0

    for n in my_list:
        cur = max(cur + n, 0)
        to_ret = max(to_ret, cur)

    return to_ret


def LIS(my_list):
    # Least in Set
    # greatest has (key, value) pairs of (num, length of LIS ending in num)
    greatest = {}
    to_ret = 1

    for i in range(len(my_list)):
        if my_list[i] not in greatest:
            greatest[my_list[i]] = 1
        for key in greatest:
            if my_list[i] > key:
                greatest[my_list[i]] = max(
                    greatest[key] + 1,
                    greatest[my_list[i]])
        if to_ret < greatest[my_list[i]]:
            to_ret = greatest[my_list[i]]

    return to_ret
