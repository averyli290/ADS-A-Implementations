import time
import random
from guppy import hpy


# Given a list of sizes, return a list of random lists of those sizes.
# (Each list is a permutation of the numbers 0...n for some n;
# i.e. there are no repetitions.)
def get_random_lists(sizes):
    lists = []
    for size in sizes:
        li = list(range(size))
        random.shuffle(li)
        lists.append(li)
    return lists


# Sample usage:
# profile_time(merge_sort, get_random_lists([10, 100, 1000]),
#              complexity=lambda n: n * math.log(n, 2))
#
# num_trials gives the number of trials that will be averaged together
#            per input size.
#
# The default value of display_factor displays time in microseconds.
#
# The printed output shows the average time taken, and the "complexity factor",
# which should be roughly a constant if you have the right complexity function.
def profile_time(time_fn, inputs, complexity=lambda x: 1, num_trials=5,
                 display_factor=10**6):
    for data in inputs:
        N = len(data)
        total_time = 0
        for i in range(num_trials):
            start_time = time.time()
            time_fn(data)
            elapsed_time = time.time() - start_time
            total_time += elapsed_time
            avg_time = (total_time * display_factor) / num_trials
        print("input %s:" % len(data), avg_time, avg_time / complexity(N))


# sample usage:
# ...[code]...
# before = profile_space_1()
# ...[more code]...
# profile_space_2(before)         (prints memory difference in bytes)
def profile_space_1():
    h = hpy()
    return (h, h.heap().size)


def profile_space_2(before_data):
    h = before_data[0]
    before_size = before_data[1]
    after_size = h.heap().size
    print("memory footprint: ", after_size - before_size)
