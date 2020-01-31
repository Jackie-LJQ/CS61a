class Link:
    empty = ()
    def __init__(self, first, rest = empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest
    def __getitem__(self, i):
        if i == 0:
            return self.first
        else:
            return self.rest[i-1]
    def __len__(self):
        return 1+len(self.rest)
    def __repr__(self):
        return link_expression(self)
    def __add__(self,t):
        return extend_link(self,t)

def link_expression(s):
    if s.rest == Link.empty:
        rest = ''
    else:
        rest = ',' + link_expression(s.rest)
    return 'Link({0}{1})'.format(s.first, rest)
def extend_link(s,t):
    if s is Link.empty:
        return t
    else:
        return Link(s.first, extend_link(s.rest, t))
def map_link(s,f):
    if s is Link.empty:
        return s
    else:
        return Link(f(s.first), map_link(s.rest,f))
def join_link(s, separator):
    if s is Link.empty:
        return ''
    if s.rest is Link.empty:
        return str(s.first)
    else:
        return str(s.first) + separator + join_link(s.rest, separator)




#
# class Tree:
#     def __init__(self, label, branches = ()):
#         self.label = label
#         for branch in branches:
#             assert isinstance(branch, Tree)
#         self.branches = branches
#     def __repr__(self):
#         if self.branches:
#             return 'Tree({0},{1})'.format(self.label, repr(self.branches))
#         else:
#             return 'Tree({0})'.format(self.label)
#     def is_leaf(self):
#         return not self.branches
# Tree(3,(Tree(3,Tree(2)),Tree(2)))
class Tree:
        def __init__(self, label, branches=()):
            self.label = label
            for branch in branches:
                assert isinstance(branch, Tree)
            self.branches = branches
        def __repr__(self):
            if self.branches:
                return 'Tree({0}, {1})'.format(self.label, repr(self.branches))
            else:
                return 'Tree({0})'.format(repr(self.label))
        def is_leaf(self):
            return not self.branches

def fib_tree(n):
    if n == 1:
        return Tree(0)
    elif n == 2:
        return Tree(1)
    else:
        left = fib_tree(n - 2)
        right = fib_tree(n - 1)
        return Tree(left.label + right.label, (left,right))
