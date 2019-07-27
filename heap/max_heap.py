class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(len(self.storage)-1)

    def delete(self):
        # first swap root and last element
        self.storage[0], self.storage[-1] = self.storage[-1], self.storage[0]
        # delete last element (former root)
        root = self.storage[-1]
        del self.storage[-1]
        # start process for sifting new root down
        self._sift_down(0)
        return root

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        if index:
            p = (index-1)//2
            if self.storage[p] < self.storage[index]:
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
                if self.storage[r] > self.storage[l]:
                    max_child = r

                if self.storage[index] < self.storage[max_child]:
                    self.storage[index], self.storage[max_child] = self.storage[max_child], self.storage[index]
                    self._sift_down(max_child)


h = Heap()
h.insert(2)
h.insert(100)
h.insert(50)
h.delete()
