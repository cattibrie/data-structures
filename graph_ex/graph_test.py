from graph import Graph

def test_empty():
    g = Graph()
    assert not g

def test_has_vertix():
    g = Graph()
    assert not g.has_vertix("A")

def test_add_vertix():
    g = Graph()
    g.add_vertix("A")
    assert g.has_vertix("A")
    assert not g.has_vertix("B")

def test_add_edges():
    d = {
        "A": ["B", "C"],
        "B": "D"
    }
    g = Graph()
    for key, values in d.items():
        g.add_edge(key, *values)
    assert "A" in g.graph["B"]
    assert "A" in g.graph["C"]
    assert "B" in g.graph["A"]
    assert "B" in g.graph["D"]
    assert "C" in g.graph["A"]
    assert "D" in g.graph["B"]

def test_edge_exist():
    d = {
        "A": "B",
        "B": "D"
    }
    g = Graph()
    for key, values in d.items():
        g.add_edge(key, *values)
    assert g.edge_exist("A", "B")
    assert g.edge_exist("D", "B")
    assert not g.edge_exist("A", "D")

def test_get_edges():
    d = {
        "A": "B",
        "B": "D"
    }
    g = Graph()
    for key, values in d.items():
        g.add_edge(key, *values)
    assert g.get_edges("A") == set("B")
    assert g.get_edges("B") == set(["A", "D"])
    assert g.get_edges("D") == set("B")

def test_connected_vert_dfs():
    d = {
        "A": ["B", "C"],
        "B": "D"
    }
    g = Graph()
    for key, values in d.items():
        g.add_edge(key, *values)
    res = g.find_connected_vert_dfs("A")
    assert res == ["A", "B", "D", "C"] or res == ["A", "C", "B", "D"]

def test_connected_vert_bfs():
    d = {
        "A": ["B", "C"],
        "B": "D"
    }
    g = Graph()
    for key, values in d.items():
        g.add_edge(key, *values)
    res = g.find_connected_vert_bfs("A")
    assert res == ["A", "B", "C", "D"] or res == ["A", "C", "B", "D"]
