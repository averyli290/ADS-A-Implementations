from math import floor, log
from random import randint


class BinaryHeap:
    def __init__(self):
        self.heap = []

    def __swap_values(self, index1, index2):
        temp = self.heap[index1]
        self.heap[index1] = self.heap[index2]
        self.heap[index2] = temp

    def __str__(self):
        return str(self.heap)

    def __parent_index(self, index):
        if not index:
            return None
        return floor((index + 1) / 2)

    def __left_index(self, index):
        return (index + 1) * 2 - 1

    def __right_index(self, index):
        return (index + 1) * 2

    def __heapify_up(self, index):
        if index != 0:
            p_index = self.__parent_index(index)
            if self.heap[index] < self.heap[p_index]:
                temp = self.heap[p_index]
                self.heap[p_index] = self.heap[index]
                self.heap[index] = temp
                self.__heapify_up(p_index)

    def __heapify_down(self, index):
        left_val = None
        right_val = None
        l_index = self.__left_index(index)
        r_index = self.__right_index(index)
        if l_index < len(self.heap):
            left_val = self.heap[l_index]
        if r_index < len(self.heap):
            right_val = self.heap[r_index]
        if (left_val is not None) and (right_val is not None):
            if self.heap[index] > left_val:
                if left_val < right_val:
                    self.__swap_values(index, l_index)
                    self.__heapify_down(l_index)
                else:
                    self.__swap_values(index, r_index)
                    self.__heapify_down(r_index)
            elif self.heap[index] > right_val:
                self.__swap_values(index, r_index)
                self.__heapify_down(r_index)
        elif left_val is not None:
            if self.heap[index] > left_val:
                self.__swap_values(index, l_index)
                self.__heapify_down(l_index)

    def insert_num(self, num):
        self.heap.append(num)
        self.__heapify_up(len(self.heap) - 1)

    def get_min(self):
        return self.heap[0]

    def delete_min(self):
        last_element = self.heap[-1]
        del self.heap[-1]
        if len(self.heap):
            self.heap[0] = last_element
            self.__heapify_down(0)

    def is_empty(self):
        return self.heap == []

    def initialize(self, nums):
        self.heap = nums
        for i in range(len(self.heap) - 1, -1, -1):
            self.__heapify_down(i)


def heapsort(nums):
    sorted_nums = []
    temp_heap = BinaryHeap()
    temp_heap.initialize(nums)
    while not temp_heap.is_empty():
        sorted_nums.append(temp_heap.get_min())
        temp_heap.delete_min()
    return sorted_nums
