class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(value)

    def delete(self):
        pass

    def get_max(self):
        pass

    def get_size(self):
        pass

    def _bubble_up(self, index):
        p = (index-1)//2
        if self.storage[p] > self.storage[index]:
            self.storage[p], self.storage[index] = self.storage[index], self.storage[p]
            self._bubble_up(index)

    def _sift_down(self, index):
        l = 2*index+1
        r = 2*index+2
