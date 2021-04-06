import math
import sys


class PriorityQueue:
    # Based on Min Heap
    def __init__(self):
        self.cur_size = 0
        self.array = []
        self.pos = {}  # To store the pos of node in array

    def __str__(self):
        return str(self.array)

    def isEmpty(self):
        return self.cur_size == 0

    def min_heapify(self, idx):
        lc = self.left(idx)
        rc = self.right(idx)
        if lc < self.cur_size and self.array(lc)[0] < self.array(idx)[0]:
            smallest = lc
        else:
            smallest = idx
        if rc < self.cur_size and self.array(rc)[0] < self.array(smallest)[0]:
            smallest = rc
        if smallest != idx:
            self.swap(idx, smallest)
            self.min_heapify(smallest)

    def insert(self, tup):
        # Inserts a node into the Priority Queue
        self.pos[tup[1]] = self.cur_size
        self.cur_size += 1
        self.array.append((sys.maxsize, tup[1]))
        self.reduce_key((sys.maxsize, tup[1]), tup[0])

    def pop_min(self):
        # Removes and returns the min element at top of priority queue
        min_node = self.array[0][1]
        self.array[0] = self.array[self.cur_size - 1]
        self.cur_size -= 1
        self.min_heapify(1)
        del self.pos[min_node]
        return min_node

    def left(self, i):
        # returns the index of left child
        return 2 * i + 1

    def right(self, i):
        # returns the index of right child
        return 2 * i + 2

    def par(self, i):
        # returns the index of parent
        return math.floor(i / 2)

    def swap(self, i, j):
        # swaps array elements at indices i and j
        # update the pos{}
        self.pos[self.array[i][1]] = j
        self.pos[self.array[j][1]] = i
        temp = self.array[i]
        self.array[i] = self.array[j]
        self.array[j] = temp

    def reduce_key(self, tup, new_d):
        idx = self.pos[tup[1]]
        # assuming the new_d is atmost old_d
        self.array[idx] = (new_d, tup[1])
        while idx > 0 and self.array[self.par(idx)][0] > self.array[idx][0]:
            self.swap(idx, self.par(idx))
            idx = self.par(idx)
