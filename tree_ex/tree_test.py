from tree import Queue, Element, Node, BinaryTree

def test_tree_empty():
    tree = BinaryTree()
    assert tree.getHead() == None

def test_tree_add_head():
    tree = BinaryTree()
    tree.add(1)
    assert tree.getHead() == 1

def test_tree_add_three():
    tree = BinaryTree()
    tree.add(1)
    tree.add(2)
    left_child = tree.head.left_child
    assert left_child.getValue() == 2
    tree.add(3)
    right_child = tree.head.right_child
    assert right_child.getValue() == 3

def test_tree_add_multiple():
    arr = [1, 2, 3, 4, 5]
    tree = BinaryTree()
    for el in arr:
        tree.add(el)
    queue = Queue()
    queue.add(tree.head)
    i = 0
    while queue.notEmpty():
        current = queue.getHeadValue()
        assert current.getValue() == arr[i]
        i += 1
        if current.hasLeftChild():
            queue.add(current.left_child)
        if current.hasRightChild():
            queue.add(current.right_child)
        queue.pop()
