from math import log

class Node:
    def __init__(self, value=None):
        self.value = value
        self.children = []

    def __str__(self):
        return ("Value: %i, num_children: %s"
                % (self.value, str(len(self.children))))


class BinomialTree:
    def __init__(self):
        self.root = None

    def get_k(self):
        return len(self.root.children)

    def __str__(self):
        self.to_ret = ""

        def __print_help(node, tabs):
            self.to_ret += tabs * "    " + node.__str__() + '\n'
            for node_child in node.children:
                __print_help(node_child, tabs + 1)
        __print_help(self.root, 0)
        return self.to_ret


class BinomialHeap:
    def __init__(self):
        self.heap = []

    def __str__(self):
        to_print = ""
        for tree in self.heap:
            to_print += tree.__str__() + '\n'
        return to_print

    def __order_trees(self):
        self.heap = sorted(self.heap, key=lambda tree: tree.get_k())

    def get_min(self):
        if not self.is_empty():
            min_num = self.heap[0].root.value
            for i in range(0, len(self.heap)):
                min_num = min(min_num, self.heap[i].root.value)
            return min_num
        raise AssertionError("There is no minimum of an empty heap!")

    def delete_min(self):
        if not len(self.heap):
            raise AssertionError("There is no minimum of an empty heap!")

        temp_heap = BinomialHeap()
        min_index = 0
        min_value = self.heap[0].root.value
        for i in range(len(self.heap)):
            if self.heap[i].root.value < min_value:
                min_value = self.heap[i].root.value
                min_index = i
        for i in range(self.heap[min_index].get_k()):
            temp_tree = BinomialTree()
            temp_tree.root = self.heap[min_index].root.children[i]
            temp_heap.heap.append(temp_tree)
        self.heap.pop(min_index)
        self.merge(temp_heap)

    def insert(self, v):
        to_insert = BinomialHeap()
        temp_tree = BinomialTree()
        temp_node = Node()
        temp_node.value = v
        temp_tree.root = temp_node
        to_insert.heap.append(temp_tree)
        self.merge(to_insert)

    def __combine_trees(self, binom_tree_1, binom_tree_2):
        if binom_tree_1.root.value <= binom_tree_2.root.value:
            binom_tree_1.root.children.append(binom_tree_2.root)
            return binom_tree_1
        binom_tree_2.root.children.append(binom_tree_1.root)
        return binom_tree_2

    def merge(self, bin_heap_2):
        # Iterating through heaps and the finished heap
        counter = 0

        # The trees need to be in ascending order of size
        self.__order_trees()
        bin_heap_2.__order_trees()

        while (len(bin_heap_2.heap)) and (counter < len(self.heap)):
            # Check if can combine current trees and combine
            # into self.heap if can combine
            if (self.heap[counter].get_k()
                    == bin_heap_2.heap[0].get_k()):
                self.heap[counter] = self.__combine_trees(
                    self.heap[counter], bin_heap_2.heap.pop(0))

                # After combining tree, check to see if
                # it can be combined with next trees
                combine_in_heap = counter + 1 < len(self.heap)
                while combine_in_heap:
                    if (self.heap[counter].get_k()
                            == self.heap[counter + 1].get_k()):
                        self.heap[counter] = self.__combine_trees(
                            self.heap[counter], self.heap[counter + 1])
                        self.heap.pop(counter + 1)
                        combine_in_heap = counter + 1 < len(self.heap)
                    else:
                        # If can't combine, stop checking
                        combine_in_heap = False

            # Check whether to add tree from bin_heap_2
            # or move to next tree in self.heap
            elif (self.heap[counter].get_k()
                    > bin_heap_2.heap[0].get_k()):
                # Add tree to heap since it is not affected
                self.heap.append(bin_heap_2.heap.pop(0))
                counter += 1
            else:
                counter += 1

        # Add rest of trees to heap
        for i in range(len(bin_heap_2.heap)):
            self.heap.append(bin_heap_2.heap[i])

    def is_empty(self):
        return self.heap == []


def binomial_heapsort(nums):
    # Add nums one by one into heap, then remove them one by one into list
    to_sort = BinomialHeap()
    for num in nums:
        to_sort.insert(num)
    sorted_nums = []
    for i in range(len(nums)):
        sorted_nums.append(to_sort.get_min())
        to_sort.delete_min()
    return sorted_nums



'''
The binomial_heapsort had a much higher coefficient at around
30 times for each trial. This may be because it takes log n time
to find the minimum.
'''
