from lru_cache import Element, PriorityList, Cache

def test_add_value():
    c = Cache(3)
    c.add(key="a", value="abc")
    assert c.dict["a"]["value"] == "abc"

def test_add_el():
    c = Cache(3)
    c.add(key="a", value="abc")
    assert c.dict["a"]["el"].get_key() == "a"

def test_add():
    c = Cache(2)
    c.add(key="a", value="abc")
    assert "a" in c.dict
    c.add(key="b", value="bcd")
    assert "a" in c.dict
    c.add(key="d", value="def")
    assert "a" not in c.dict
