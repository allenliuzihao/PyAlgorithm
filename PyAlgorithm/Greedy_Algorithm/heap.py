'''
Contains array implementation of heap.
'''


import random


class Heap:
    def __init__(self, option):
        self.minHeap = option
        self.array = [-99]
        self.index = {}     # keeping the index of a node in the heap

    def isEmpty(self):
        return len(self.array) == 1

    def remove(self, value):
        to_be_removed_index = self.index[value.getValue()]
        return_value = value
        leaf = self.array[-1]
        self.array[to_be_removed_index] = leaf
        self.array.pop(-1)
        self.index[leaf.getValue()] = to_be_removed_index
        remove_index = to_be_removed_index
        if self.minHeap:
            while to_be_removed_index * 2 < len(self.array):
                if to_be_removed_index * 2 + 1 < len(self.array) and (self.array[to_be_removed_index] > self.array[2 * to_be_removed_index] or self.array[to_be_removed_index] > self.array[2 * to_be_removed_index + 1]):
                    min_index_of_children = 2 * to_be_removed_index if self.array[2 * to_be_removed_index] < self.array[2 * to_be_removed_index + 1] else 2 * to_be_removed_index + 1
                    child = self.array[min_index_of_children]
                    parent = self.array[to_be_removed_index]
                    self.index[child.getValue()] = to_be_removed_index
                    self.index[parent.getValue()] = min_index_of_children
                    self.array[to_be_removed_index], self.array[min_index_of_children] = self.array[min_index_of_children], self.array[to_be_removed_index]
                    to_be_removed_index = min_index_of_children
                elif to_be_removed_index * 2 + 1 >= len(self.array) and self.array[to_be_removed_index] > self.array[2 * to_be_removed_index]:
                    child = self.array[2 * to_be_removed_index]
                    parent = self.array[to_be_removed_index]
                    self.index[child.getValue()] = to_be_removed_index
                    self.index[parent.getValue()] = 2 * to_be_removed_index
                    self.array[to_be_removed_index], self.array[2 * to_be_removed_index] = self.array[2 * to_be_removed_index], self.array[to_be_removed_index]
                    to_be_removed_index = 2 * to_be_removed_index
                else:
                    break
            while remove_index < len(self.array) and remove_index / 2 != 0 and self.array[remove_index] < self.array[remove_index / 2]:
                self.index[self.array[remove_index].getValue()] = remove_index / 2
                self.index[self.array[remove_index / 2].getValue()] = remove_index
                self.array[remove_index], self.array[remove_index / 2] = self.array[remove_index / 2], self.array[remove_index]
                remove_index /= 2
        else:
            while to_be_removed_index * 2 < len(self.array):
                if to_be_removed_index * 2 + 1 < len(self.array) and (self.array[to_be_removed_index] < self.array[2 * to_be_removed_index] or self.array[to_be_removed_index] < self.array[2 * to_be_removed_index + 1]):
                    min_index_of_children = 2 * to_be_removed_index if self.array[2 * to_be_removed_index] > self.array[2 * to_be_removed_index + 1] else 2 * to_be_removed_index + 1
                    child = self.array[min_index_of_children]
                    parent = self.array[to_be_removed_index]
                    self.index[child.getValue()] = to_be_removed_index
                    self.index[parent.getValue()] = min_index_of_children
                    self.array[to_be_removed_index], self.array[min_index_of_children] = self.array[min_index_of_children], self.array[to_be_removed_index]
                    to_be_removed_index = min_index_of_children
                elif to_be_removed_index * 2 + 1 >= len(self.array) and self.array[to_be_removed_index] < self.array[2 * to_be_removed_index]:
                    child = self.array[2 * to_be_removed_index]
                    parent = self.array[to_be_removed_index]
                    self.index[child.getValue()] = to_be_removed_index
                    self.index[parent.getValue()] = 2 * to_be_removed_index
                    self.array[to_be_removed_index], self.array[2 * to_be_removed_index] = self.array[2 * to_be_removed_index], self.array[to_be_removed_index]
                    to_be_removed_index = 2 * to_be_removed_index
                else:
                    break
            while remove_index < len(self.array) and remove_index / 2 != 0 and self.array[remove_index] > self.array[remove_index / 2]:
                self.index[self.array[remove_index].getValue()] = remove_index / 2
                self.index[self.array[remove_index / 2].getValue()] = remove_index
                self.array[remove_index], self.array[remove_index / 2] = self.array[remove_index / 2], self.array[remove_index]
                remove_index /= 2
        return return_value

    # don't use this as it brings down the running time of heap operation to linear time
    def contains(self, value):
        for item in self.array:
            if item is value:
                return True
        return False

    def size(self):
        return len(self.array) - 1

    def insert(self, value):
        self.array.append(value)
        index = len(self.array) - 1
        self.index[value.getValue()] = index
        if self.minHeap:
            while index / 2 != 0:
                if self.array[index] < self.array[index / 2]:
                    child = self.array[index]
                    parent = self.array[index / 2]
                    self.index[child.getValue()] = index / 2
                    self.index[parent.getValue()] = index
                    self.array[index], self.array[index / 2] = self.array[index / 2], self.array[index]
                else:
                    break
                index /= 2
        else:
            while index / 2 != 0:
                if self.array[index] > self.array[index / 2]:
                    child = self.array[index]
                    parent = self.array[index / 2]
                    self.index[child.getValue()] = index / 2
                    self.index[parent.getValue()] = index
                    self.array[index], self.array[index / 2] = self.array[index / 2], self.array[index]
                else:
                    break
                index /= 2

    def extract(self):
        if len(self.array) == 1:
            raise Exception("Heap is empty!")
        return_value = self.array[1]
        leaf = self.array[-1]
        self.array[1] = leaf
        self.array.pop(-1)
        self.index[leaf.getValue()] = 1
        index = 1
        if self.minHeap:
            while index * 2 < len(self.array):
                if index * 2 + 1 < len(self.array) and (self.array[index] > self.array[2 * index] or self.array[index] > self.array[2 * index + 1]):
                    min_index_of_children = 2 * index if self.array[2 * index] < self.array[2 * index + 1] else 2 * index + 1
                    child = self.array[min_index_of_children]
                    parent = self.array[index]
                    self.index[child.getValue()] = index
                    self.index[parent.getValue()] = min_index_of_children
                    self.array[index], self.array[min_index_of_children] = self.array[min_index_of_children], self.array[index]
                    index = min_index_of_children
                elif index * 2 + 1 >= len(self.array) and self.array[index] > self.array[2 * index]:
                    child = self.array[2 * index]
                    parent = self.array[index]
                    self.index[child.getValue()] = index
                    self.index[parent.getValue()] = 2 * index
                    self.array[index], self.array[2 * index] = self.array[2 * index], self.array[index]
                    index = 2 * index
                else:
                    break
        else:
            while index * 2 < len(self.array):
                if index * 2 + 1 < len(self.array) and (self.array[index] < self.array[2 * index] or self.array[index] < self.array[2 * index + 1]):
                    min_index_of_children = 2 * index if self.array[2 * index] > self.array[2 * index + 1] else 2 * index + 1
                    child = self.array[min_index_of_children]
                    parent = self.array[index]
                    self.index[child.getValue()] = index
                    self.index[parent.getValue()] = min_index_of_children
                    self.array[index], self.array[min_index_of_children] = self.array[min_index_of_children], self.array[index]
                    index = min_index_of_children
                elif index * 2 + 1 >= len(self.array) and self.array[index] < self.array[2 * index]:
                    child = self.array[2 * index]
                    parent = self.array[index]
                    self.index[child.getValue()] = index
                    self.index[parent.getValue()] = 2 * index
                    self.array[index], self.array[2 * index] = self.array[2 * index], self.array[index]
                    index = 2 * index
                else:
                    break
        return return_value

    def __str__(self):
        string = "This is a min heap?: " + str(self.minHeap) + "     size of heap: " + str(len(self.array) - 1) + "\n"
        #string += str(self.array)
        for item in self.array:
            string += str(item) + " \n"
        return string[0:-1]

    def getIndexList(self):
        return self.index

if __name__ == '__main__':
    #a = random.sample(range(100000), 9)
    a = [1, 5, 6, 2, 3, 10, 9, 8, 7, 21, 14, 13]
    heap = Heap(True)
    for i in a:
        heap.insert(i)
    print heap.getIndexList()
    heap.extract()
    print heap.getIndexList()
    heap.remove(13)
    print heap.getIndexList()
    heap.remove(21)
    print heap.getIndexList()
    heap.remove(2)
    print heap.getIndexList()
    #b = []
    #for i in xrange(0, 9):
    #    b.append(heap.extract())
    #print b
    #print heap
    #heap.remove(14)
    #print heap