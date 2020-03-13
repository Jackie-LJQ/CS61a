#iterator
p = [1,2,3,4]
iterator = iter(p)
next(iterator)
next(iterator)
next(iterator)
next(iterator)
try:
    next(iterator)
except StopIteration:
    print('No more values')

s = iter(p)
next(s) #1
next(s) #2

# two different iterators track differernt position
t = iter(p) 
next(t) #1
next(t) #2


# two names of same iterator share the same position
u = s
print(next(u))

# map function
def double_and_print(x):
    print(str(x) + ' ==> ' + str(2*x))
s = iter(range(10))
doubled = map(double_and_print, s)

# implement 'for' using 'while' 'try' and 'except'
count = range(10)
count = iter(count)
try:
    while True:
#        print(next(count))
        next(count)
except StopIteration:
    pass


# genertor
def letter_generator():
    yield('a')
    yield('b')
    yield('c')

for x in letter_generator():
    print(x)

# manually iterate
x = letter_generator()
next(x) # 'a'
next(x) # 'b'


class Stream:
    """A lazily computed linked list."""
    class empty:
        def __repr__(self):
            return 'Stream.empty'
    empty = empty()
    
    def __init__(self, first, compute_rest=lambda:empty):
        assert callable(compute_rest), 'compute_rest must be callable.'
        self.first = first
        self._compute_rest = compute_rest
    @property
    def rest(self):
        """Return the rest of the stream, computing it if necessary."""
        if self._compute_rest is not None:
            self._rest = self._compute_rest() # _compute_rest take no argument return a stream or empty
            self._compute_rest = None
        return self._rest
    def __repr__(self):
            return 'Stream({0}, <...>)'.format(repr(self.first))

# infinite sequence
def integer_stream(x):
    def compute_rest():
        return integer_stream(x+1)
    return Stream(x, compute_rest)

# map for stream
def map_Stream(f, s):
    if s is Stream.empty:
        return s
    def compute_rest():
        return map_Stream(f, s.rest)
    return Stream(f(s.first), compute_rest)

s = Stream(1, lambda:Stream(2,lambda:Stream(3, lambda:Stream(4))))
s1 = map_Stream(lambda x:x**2, s)


# filter Stream
def filter_stream(f, s):
    print(s)
    if s is empty:
        return s
    def compute_rest():
        return filter_stream(f, s.rest)
    if f(s.first):
        return Stream(s.first, compute_rest)
    else:
        return compute_rest()


def first_k_to_list(s, k):
    first_k = []
    while s is not empty and k > 0:
        first_k.append(s.first)
        s, k = s.rest, k-1
    return first_k


first_k_to_list(s, 20) # [1,2,3,4]
test = filter_stream(lambda x:x%2 == 0, s) 
first_k_to_list(s, 20) # [2,4]





#