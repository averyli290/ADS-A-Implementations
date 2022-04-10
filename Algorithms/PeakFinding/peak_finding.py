def find_peaks(arr, j_index=0):
    # find max in current middle column,
    # choose left or right, choose max of that etc
    i = len(arr) // 2
    max_in_col = arr[i][0]
    j = 0
    for k in range(len(arr)):
        if arr[k][j] > max_in_col:
            max_in_col = arr[k][j]
            i = k

    left = None if j == 0 else arr[i][j - 1]
    right = None if j == len(arr[0]) - 1 else arr[i][j + 1]

    peak = True
    for height in [left, right]:
        if height is not None:
            if height > max_in_col:
                peak = False
    if peak:
        return (i, j + j_index)

    if left is None:
        return find_peaks(
            [arr[a][j + 1:] for a in range(len(arr))],
            j_index + j + 1)
    if right is None:
        return find_peaks(
            [arr[a][:j] for a in range(len(arr))],
            j_index + j)
