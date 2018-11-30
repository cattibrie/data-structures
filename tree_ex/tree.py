class Element(object):
    def __init__(self, el):
        self.value = el
        self.next = None

class QueueIterator(object):
    def __init__(self, queue):
        self.el = queue.head if queue.notEmpty() else None

    def __iter__(self):
        return self

    def next(self):
        if self.el is None:
            raise StopIteration
        next_val, self.el = self.el.value, self.el.next
        return next_val

class Queue(object):
    _sentinel = object()

    def __init__(self, arr=None):
        self.head = Element(self._sentinel)
        self.tail = self.head
        if arr is not None:
            for el in arr:
                self.add(el)

    def __nonzero__(self):
        return self.notEmpty()

    def __iter__(self):
        # return QueueIterator(self)
        def _iter():
            if self.notEmpty():
                el = self.head
                while el is not None:
                    yield el.value
                    el = el.next
        return _iter()

    def __len__(self):
        return reduce(lambda a, _: a+1, self, 0)

    def add(self, el):
        if self.isEmpty():
            self.head.value = el
            return
        prev = self.tail
        prev.next = Element(el)
        self.tail = prev.next

    def pop(self):
        if self.head == self.tail:
            self.head.value = self._sentinel
            return
        prev = self.head
        next_el = prev.next
        self.head = next_el

    def get(self):
        return self.head

    def getHeadValue(self):
        return self.head.value

    def getTailValue(self):
        return self.tail.value

    def notEmpty(self):
        return not self.isEmpty()

    def isEmpty(self):
        return self.getHeadValue() == self._sentinel


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def hasLeftChild(self):
        return self.left_child is not None

    def hasRightChild(self):
        return self.right_child is not None

    def getValue(self):
        return self.value


class BinaryTree(object):
    def __init__(self):
        self.head = Node(None)

    def getHead(self):
        return self.head.getValue()

    def add(self, value):
        if not self.head.value:
            self.head.value = value
            return
        queue = Queue()
        head = self.head
        queue.add(head)
        # value_not_assigned = True
        while queue.notEmpty():
            current = queue.getHeadValue()
            if current.hasLeftChild():
                queue.add(current.left_child)
            else:
                current.left_child = Node(value)
                # value_not_assigned = False
                return
            if current.hasRightChild():
                queue.add(current.right_child)
            else:
                current.right_child = Node(value)
                # value_not_assigned = False
                return
            queue.pop()
