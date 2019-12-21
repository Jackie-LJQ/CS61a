def height(t):
    """return the length of the longest path from the root to a leaf
    >>> t = tree(3, [tree(5, [tree(1)]), tree(2)])
    >>> height(t)
    2
    """
    if is_leaf(t):
        return 0
    return 1 + max([height(x) for x in branches(t)])

def square_tree(t):
    """take a tree and square every value"""
    if is_leaf(t):
        return tree(label(t)**2)
    return tree(label(t)**2, [square_tree(x) for x in branches(t)])

def find_path(tree, x):
    if label(tree) == x:
        return [x]
    for b in branches(tree):
        path = find_path(b, x)
        if path:
            return [label(tree)] + path

def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

def label(tree):
    """Return the label value of a tree."""
    return tree[0]

def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]

def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)

def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root."""
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)

def copy_tree(t):
    """Returns a copy of t. Only for testing purposes."""
    return tree(label(t), [copy_tree(b) for b in branches(t)])

def make_withdraw(balance):
    def withdraw(amount):
        nonlocal balance
        balance = balance - amount
        return balance
    return withdraw

def add_this_many(x, el, lst):
    def add_lst():
        nonlocal x
        nonlocal lst
        while x > 0:
            lst = lst + [el]
            x = x - 1
        return lst
    return add_lst

def group_by(s, fn):
    grouped = {}
    for x in s:
        key = fn(x)
        if key in grouped:
            grouped[key].append(x)
        else:
            grouped[key] = [x]
    return grouped

def memory(n):
    def update(fn):
        nonlocal n
        n = fn(n)
        return n
    return update
f = memory(10)
a = lambda x: x * 2
b = lambda x: x - 7
c = lambda x: x > 5
