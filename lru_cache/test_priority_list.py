from lru_cache import PriorityList, Element

def test_empty():
    l = PriorityList(1)
    assert l.isEmpty()

def test_add_pop():
    l = PriorityList(1)
    tail = l.add("a")
    assert tail.get_key() == "a"
    tail = l.add("b")
    assert tail.get_key() == "b"

def test_add_multi():
    l = PriorityList(2)
    tail = l.add("a")
    assert tail.get_key() == "a"
    assert l.head.key == "a"
    tail = l.add("b")
    assert tail.get_key() == "b"
    assert l.head.key == "a"
    tail = l.add("c")
    assert tail.get_key() == "c"
    assert l.head.key == "b"

def test_add_ret():
    l = PriorityList(3)
    l.add("a")
    el = l.add("b")
    l.add("c")
    assert el.get_key() == "b"

def test_prioritize():
    l = PriorityList(3)
    l.add("a")
    el = l.add("b")
    l.add("c")
    assert l.tail.get_key() == "c"
    l.prioritize(el)
    assert l.tail.get_key() == "b"
    assert l.tail.prev.key == "c"
