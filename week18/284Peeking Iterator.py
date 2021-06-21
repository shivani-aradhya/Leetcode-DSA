# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.i = iterator
        self.peeked = False
        self.tmp = None  # Storing peeked values

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if not self.peeked:
            self.tmp = self.i.next()
            self.peeked = True
            return self.tmp
        else:
            return self.tmp

    def next(self):
        """
        :rtype: int
        """
        if self.peeked:
            self.peeked = False
            return self.tmp
        else:
            return self.i.next()

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.peeked or self.i.hasNext():
            return True
        else:
            return False
