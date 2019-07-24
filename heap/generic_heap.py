class Heap:
    def __init__(self, comparator=None):
        self.storage = []
        if comparator == None:
            self.comparator = lambda parent, child: parent > child
        else:
            self.comparator = comparator

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(len(self.storage)-1)

    def delete(self):
        self.storage[0], self.storage[-1] = self.storage[-1], self.storage[0]
        root = self.storage[-1]
        del self.storage[-1]
        self._sift_down(0)
        return root

    def get_priority(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        if index:
            p = (index-1)//2
            if not self.comparator(self.storage[p], self.storage[index]):
                self.storage[p], self.storage[index] = self.storage[index], self.storage[p]
                self._bubble_up(p)

    def _sift_down(self, index):
        l = 2*index+1
        r = 2*index+2

        # only execute if left child index actually exists in storage, else end
        if l < self.get_size():
            # find greatest child value
            max_child = l
            # set max as right child if index exists and greater than left child
            if r < self.get_size():
                if self.comparator(self.storage[r], self.storage[l]):
                    max_child = r

                if not self.comparator(self.storage[index], self.storage[max_child]):
                    self.storage[index], self.storage[max_child] = self.storage[max_child], self.storage[index]
                    self._sift_down(max_child)
