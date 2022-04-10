class BinaryHeapForEdges():
    # Main attribute:
    # self.heap is the array that holds the heap.

    def __init__(self):
        self.heap = []

    def insert(self, edge):
        self.heap.append(edge)
        self.__heapify_up(len(self.heap) - 1)

    def get_min(self):
        if self.is_empty():
            raise ValueError
        return self.heap[0]

    def delete_min(self):
        if self.is_empty():
            raise ValueError
        if len(self.heap) == 1:
            self.heap.pop()
            return

        self.heap[0] = self.heap.pop()
        self.__heapify_down(0)

    def is_empty(self):
        return len(self.heap) == 0

    def initialize(self, nums):
        self.heap = nums
        for i in range(len(self.heap) - 1, -1, -1):
            self.__heapify_down(i)

    def __heapify_up(self, index):
        parent_index = self.__parent(index)
        if (index > 0) and (self.heap[index].weight < self.heap[parent_index].weight):
            self.heap[index], self.heap[parent_index] = \
                self.heap[parent_index], self.heap[index]
            self.__heapify_up(parent_index)

    def __heapify_down(self, index):
        left_index = self.__left_child(index)
        right_index = self.__right_child(index)

        # special cases for zero or one child.
        if not self.__in_tree(left_index):
            return
        if not self.__in_tree(right_index):
            min_child = left_index
        else:
            min_child = left_index if self.heap[left_index].weight < \
                self.heap[right_index].weight else right_index
        if (self.heap[min_child].weight < self.heap[index].weight):
            self.heap[index], self.heap[min_child] = \
                self.heap[min_child], self.heap[index]
            self.__heapify_down(min_child)

    def __parent(self, index):
        return ((index + 1) // 2) - 1

    def __left_child(self, index):
        return (2 * (index + 1)) - 1

    def __right_child(self, index):
        return (2 * (index + 1))

    def __in_tree(self, index):
        return index < len(self.heap)
