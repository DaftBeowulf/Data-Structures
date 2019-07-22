class Queue:
    def __init__(self):
        self.size = 0
        # what data structure should we
        # use to store queue elements?
        self.storage = LinkedList()

    def enqueue(self, item):
        pass

    def dequeue(self):
        pass

    def len(self):
        pass


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_tail(self, value):
        new_node = Node(value)

        # list currently has zero items
        if self.head == None and self.tail == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node

    def remove_head(self):
        # list has zero items
        if not self.head and not self.tail:
            return None
        # list has one item (so remove all items from list)
        elif self.head is self.tail:
            removed = self.head
            self.head = None
            self.tail = None
            return removed.get_value()
        # list has more than one item
        else:
            removed = self.head
            self.head = removed.get_next()
            return removed.get_value()


class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, node):
        self.next_node = node
