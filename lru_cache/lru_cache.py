class Element(object):
    def __init__(self, key):
        self.key = key
        self.prev = None
        self.next = None

    def get_key(self):
        return self.key

class PriorityList(object):
    def __init__(self, max_size=0):
        self.head = None
        self.tail = self.head
        self.size = 0
        self.max_size = max_size

    def isEmpty(self):
        return not bool(self.size)

    def pop(self):
        if self.head == self.tail:
            self.head = None
            self.size = 0
            return
        next_el = self.head.next
        next_el.prev = None
        self.head = next_el
        self.size -= 1

    def add(self, key):
        if self.max_size <= 0:
            raise Exception("invalid max size of the cache")
        el = Element(key)
        if self.isEmpty():
            self.head = el
            self.tail = self.head
        else:
            if self.size == self.max_size:
                self.pop()
            prev = self.tail
            next_el = el
            next_el.prev = prev
            prev.next = next_el
            self.tail = next_el
        self.size += 1
        return el

    def prioritize(self, el):
        if el == self.tail:
            return
        next_el = el.next
        next_next = next_el.next
        prev = el.prev
        if el != self.head:
            prev.next = next_el
        next_el.next = el
        next_el.prev = el.prev
        el.prev = next_el
        el.next = next_next
        if next_next is not None:
            next_next.prev = el
        if next_el == self.tail:
            self.tail = el
        if el == self.head:
            self.head = el.prev


class Cache(object):
    def __init__(self, max_size):
        self.max_size = max_size
        self.dict = dict()
        self.priority_list = PriorityList(max_size)

    def isEmpty(self):
        return not bool(self.dict)

    def notEmpty(self):
        return not self.isEmpty()

    def add(self, key, value):
        if key not in self.dict:
            if self.priority_list.size == self.max_size:
                lru_prev = self.priority_list.head.get_key()
                del self.dict[lru_prev]
            el = self.priority_list.add(key)
            self.dict[key] = {
                "value": value,
                "el": el
            }
        el = self.dict[key]["el"]
        self.priority_list.prioritize(el)
        self.dict[key]["value"] = value
