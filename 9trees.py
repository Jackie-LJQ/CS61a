def tree(lable, branches=[]):
    for branch in branches:
        assert is_tree(branch) , 'branch should also be a tree'
    return [lable] + list(branches)

def lable(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(t):
    if type(t) != list or len(t) < 1:
        return False
    for branch in branches(t):
        if not is_tree(branch):
            return False
    return True

def is_leaf(t):
    return len(t)==1

def fib_tree(n):
    if n <= 1:
        return tree(n)
    else:
        left = fib_tree(n-2)
        right = fib_tree(n-1)
        return tree(lable(left)+lable(right), [left,right])

def count_leaf(t):
    if is_leaf(t):
        return 1
    else:
        return sum(count_leaf(branch) for branch in branches(t))

def leaves(tree):
    if is_leaf(tree):
        return tree
    else:
        return sum([leaves(branch) for branch in branches(tree)], [])

def increment_leaves(t):
    """return a tree like t but all leaves add1"""
    if is_leaf(t):
        return tree(lable(t)+1)
    else:
        return tree(lable(t),[increment_leaves(branch) for branch in branches(t)])

a  = tree(1,[tree(2,[tree(1),tree(2)]),tree(3)])

def increment_lable(t):
    """return a tree like t but all lables add 1"""
    if is_leaf(t):
        return tree(lable(t)+1)
    else:
        br = [increment_lable(branch) for branch in branches(t)]
        return tree(lable(t)+1,br)

def print_tree(t, indent = 0):
    print(' ' * indent + str(lable(t)))
    for a in branches(t):
        print_tree(a, indent + 1)
