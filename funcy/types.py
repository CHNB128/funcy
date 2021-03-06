from .compat import range, Mapping, Set, Sequence, Iterator, Iterable
from .funcs import compose

__all__ = ('isa', 'is_mapping', 'is_set', 'is_seq', 'is_list', 'is_tuple',
           'is_seqcoll', 'is_seqcont',
           'iterable', 'is_iter', 'is_empty', '_not')


def isa(*types):
    """
    Creates a function checking if its argument
    is of any of given types.
    """
    return lambda x: isinstance(x, types)

is_mapping = isa(Mapping)
is_set = isa(Set)
is_seq = isa(Sequence)
is_list = isa(list)
is_tuple = isa(tuple)

is_seqcoll = isa(list, tuple)
is_seqcont = isa(list, tuple, Iterator, range)

iterable = isa(Iterable)
is_iter = isa(Iterator)

equal = lambda a, b: a == b

_not = lambda x: not x
is_empty = compose(_not, bool)
