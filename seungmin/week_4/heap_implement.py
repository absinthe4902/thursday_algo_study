
class MaxHeap(object):
    def __init__(self):
        self.queue = []

    def parent(self, index):
        return (index-1) // 2

    def left_child(self, index):
        return index * 2 + 1

    def right_child(self, index):
        return (index * 2) + 2

    def insert(self, value):
        self.queue.append(value)
        last_index = len(self.queue) - 1

        while last_index >= 0:
            parent_index = self.parent(last_index)
            if parent_index >= 0 and self.queue[parent_index] < self.queue[last_index]:
                self.swap(last_index, parent_index)
                last_index = parent_index
            else:
                break

    def swap(self, index, parent_index):
        self.queue[index], self.queue[parent_index] = self.queue[parent_index], self.queue[index]

    def print_heap(self):
        print(self.queue)

test = MaxHeap()
test.insert(4)
test.print_heap()
test.insert(1)
test.print_heap()
test.insert(7)
test.print_heap()
test.insert(3)

test.print_heap()