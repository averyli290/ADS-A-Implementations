import random


def has_sum_printing(L, goal, candidate=None):
    if candidate is None:
        candidate = []

    if sum(candidate) == goal:
        print("True")

    else:
        for i in range(len(L)):
            candidate.append(L[i])
            has_sum_printing(L.pop(i), goal, candidate)
            candidate.pop()


def has_sum(L, goal, accum=None, candidate=None):
    if candidate is None:
        candidate = []

    if accum is None:
        accum = False

    if sum(candidate) == goal:
        return True

    else:
        for i in range(len(L)):
            candidate.append(L[i])
            temp = L.pop(i)
            accum = accum or has_sum(L, goal, accum, candidate)
            L.insert(temp, i)
            candidate.pop()

    return accum


def eight_queens(n, candidate=None):

    def print_board(n, positions):
        print("Valid board")
        print('\n'.join([' '.join(['Q' if (i, j) in positions else '.' for i in range(n)]) for j in range(n)]), '\n')

    # candidate is a list of pairs representing positions
    if candidate is None:
        candidate = []

    # printing board if valid
    if len(candidate) == n:
        print_board(n, candidate)
        return "done"

    else:
        for i in range(n):
            valid = True
            for queen in candidate:
                if queen[1] == i:
                    valid = False
                if abs(queen[1] - i) == abs(queen[0] - len(candidate)):
                    valid = False
            if valid:
                candidate.append((len(candidate), i))
                if eight_queens(n, candidate) == "done":
                    return "done"
                candidate.pop()


boggle_dice = [
    ['A', 'E', 'A', 'N', 'E', 'G'],
    ['A', 'H', 'S', 'P', 'C', 'O'],
    ['A', 'S', 'P', 'F', 'F', 'K'],
    ['O', 'B', 'J', 'O', 'A', 'B'],
    ['I', 'O', 'T', 'M', 'U', 'C'],
    ['R', 'Y', 'V', 'D', 'E', 'L'],
    ['L', 'R', 'E', 'I', 'X', 'D'],
    ['E', 'I', 'U', 'N', 'E', 'S'],
    ['W', 'N', 'G', 'E', 'E', 'H'],
    ['L', 'N', 'H', 'N', 'R', 'Z'],
    ['T', 'S', 'T', 'I', 'Y', 'D'],
    ['O', 'W', 'T', 'O', 'A', 'T'],
    ['E', 'R', 'T', 'T', 'Y', 'L'],
    ['T', 'O', 'E', 'S', 'S', 'I'],
    ['T', 'E', 'R', 'W', 'H', 'V'],
    ['N', 'U', 'I', 'H', 'M', 'Qu']]


def generate_boggle_board():
    dice = [random.choice(die) for die in boggle_dice]
    random.shuffle(dice)
    return [dice[0:4], dice[4:8], dice[8:12], dice[12:16]]


def is_valid_boggle_cell(i, j):
    return i in range(4) and j in range(4)


def find_word(word, board, candidate=None):
    if candidate is None:
        candidate = []

    if len(candidate) == len(word):
        return True

    else:

        extensions = []
        if len(candidate) == 0:
            for i in range(4):
                for j in range(4):
                    if board[i][j] == word[0]:
                        extensions.append((i, j))

        else:
            last_pos = candidate[-1]

            for offset in [
                    (-1, -1), (-1, -0), (-1, 1), (0, -1),
                    (0, 1), (1, -1), (1, 0), (1, 1)]:

                new_pos = (last_pos[0] + offset[0], last_pos[1] + offset[1])

                if is_valid_boggle_cell(new_pos[0], new_pos[1]):
                    if ((board[new_pos[0]][new_pos[1]] == word[len(candidate)])
                            and (new_pos[0], new_pos[1]) not in candidate):
                        extensions.append((new_pos[0], new_pos[1]))

        for extension in extensions:
            candidate.append(extension)

            # This part makes it a DFS (returns True
            # down tree if one returns True)
            if find_word(word, board, candidate):
                return True

            candidate.pop()

    return False

# Example run:
# find_word("happy", generate_boggle_board())