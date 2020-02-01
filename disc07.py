class Link:
    empty = ()
    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest
    def __repr__(self):
        if self.rest:
            rest_str = ', ' + repr(self.rest)
        else:
            rest_str = ''
        return 'Link({0}{1})'.format(repr(self.first), rest_str)
    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'
    def __len__(self):
        if self == Link.empty:
            return 0
        return len(self.rest) + 1
    def __getitem__(self, i):
        assert i < len(self)
        if i == 0:
            return self.first
        return self.rest[i-1]
def extend_link(s,t):
    if s is Link.empty:
        return t
    return Link(s.first, extend_link(s.rest, t))
Link.__add__ = extend_link

def sum_nums(lnk):
    """
    >>> a = Link(1, Link(6, Link(7)))
    >>> sum_nums(a)
    14
    """
    if lnk is Link.empty:
        return 0
    return lnk.first + sum_nums(lnk.rest)

def multiply_lnks(lst_of_lnks):
    """
    >>> a = Link(2, Link(3, Link(5)))
    >>> b = Link(6, Link(4, Link(2)))
    >>> c = Link(4, Link(1, Link(0, Link(2))))
    >>> p = multiply_lnks([a, b, c])
    >>> p.first
    48
    >>> p.rest.first
    12
    >>> p.rest.rest.rest is Link.empty
    True
    """
    product = 1
    for lnk in lst_of_lnks:
        if lnk == Link.empty:
            return lnk
    for lnk in lst_of_lnks:
        product = product * lnk.first
    return Link(product, multiply_lnks([lnk.rest for lnk in lst_of_lnks]))

def is_palindrome(seq):
    """ Returns True if the sequence is a palindrome. A palindrome is a sequence
    that reads the same forwards as backwards
    >>> is_palindrome(Link("l", Link("i", Link("n", Link("k")))))
    False
    >>> is_palindrome(["l", "i", "n", "k"])
    False
    >>> is_palindrome("link")
    False
    >>> is_palindrome(Link.empty)
    True
    >>> is_palindrome([])
    True
    >>> is_palindrome("")
    True
    >>> is_palindrome(Link("a", Link("v", Link("a"))))
    True
    >>> is_palindrome(["a", "v", "a"])
    True
    >>> is_palindrome("ava")
    True
    """
    l_seq = len(seq)
    if l_seq <= 1:
        return True
    if seq[0] == seq[l_seq-1]:
        seq_1, i = seq[1], 2
        while i < l_seq-1:
         seq_1 = seq_1 + seq[i]
        return is_palindrome(seq_1)
    return False
