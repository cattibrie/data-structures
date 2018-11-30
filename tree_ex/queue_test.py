from itertools import izip_longest
from tree import Queue, Element

def test_bool_cast():
    q = Queue()
    assert not bool(q)
    q.add(7)
    assert bool(q)
    q.pop()
    assert not bool(q)

def test_queue_1():
    arr = [1, 2, 3, 4, 5]
    q = Queue(arr)
    head, tail = arr[0], arr[-1]
    assert q.getHeadValue() == head
    assert q.getTailValue() == tail
    q.add(7)
    assert q.getTailValue() == 7
    q.pop()
    assert q.getHeadValue() == arr[1]

def test_queue_add():
    q = Queue()
    assert q.isEmpty()
    assert q.getTailValue() == q._sentinel
    q.add(7)
    assert q.getHeadValue() == 7
    assert q.getTailValue() == 7

def test_queue_add_multi():
    q = Queue()
    q.add(7)
    assert q.getHeadValue() == 7
    assert q.getTailValue() == 7
    q.add(3)
    assert q.getHeadValue() == 7
    assert q.getTailValue() == 3

def test_queue_pop():
    q = Queue()
    q.add(7)
    assert q.getHeadValue() == 7
    assert q.getTailValue() == 7
    q.pop()
    assert q.getHeadValue() == q._sentinel
    assert q.getTailValue() == q._sentinel
    assert q.head == q.tail

def test_queue_pop_multi():
    q = Queue()
    q.add(7)
    assert q.getHeadValue() == 7
    assert q.getTailValue() == 7
    q.add(3)
    assert q.getHeadValue() == 7
    assert q.getTailValue() == 3
    q.pop()
    assert q.getHeadValue() == 3
    assert q.getTailValue() == 3
    assert q.head == q.tail

def test_queue_notEmpty():
    q = Queue()
    assert not q.notEmpty()
    q.add(7)
    assert q.notEmpty()

def test_iterator():
    arr = [1, 2, 3, 4, 5]
    q = Queue(arr)
    sentinel = object()
    for q, a in izip_longest(q, arr, fillvalue=sentinel):
        assert q == a

def test_iterator():
    q = Queue()
    temp = list(q)
    assert len(temp) == 0

def test_len():
    q = Queue()
    assert len(q) == 0
    q.add(10)
    assert len(q) == 1
    q.pop()
    assert len(q) == 0
