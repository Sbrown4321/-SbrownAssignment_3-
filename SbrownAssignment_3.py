#Steven Brown
#Assignment_3
# 25 FEB 2016

from __future__ import print_function
import unittest
import sys

trace = False

'''A dictionary class implemented by hasing and chaing. The set
is represented internally by as list of lists. The outer list is
initialized to all None's. When multiple values hash to the same location
(collision), new values are appened to the list at that location. The
list is rehashed when @75%max and trial of reshash @25%min. The size
starts at 10 and doubles with each rehash. The first value of a sublist is the
key, the second the value.

The initial list is:
[None, None, None, None, None, None, None, None, None, None]

After 0, "zero" 1, "one" 10, "ten" have been inserted, it will be:
[[[0, "zero"],[10, "ten"]],[[1, "one"]], None, None,...]'''

class my_hash_set:
    def __init__(self, init=None):
        self.__limit = 10
        self.__none = None
        self.__items = [None] * self.__limit
        self.__count = 0

        if init:
            for i in init:
                self.__setitem__(i[0], i[1])

    def __len__(self): return(self.__count)

    #Set iterator
    def __flattened(self):
        flattened = filter(lambda x: x != None, self.__items)
        flattened = [item for inner in flattened for item in inner]
        return(flattened)

    def __iter__(self): return(iter(self.__flattened()))
    def __str__(self): return(str(self.__flattened()))

    #Add helper
    '''def __add(self, item):
        assert item != self.__none

        h = self.__hash(item)
        if self.__items[h] == self.__none:
            self.__items[h] = [item]
        else:
            self.__items[h].append(item)'''

    def __rehash(self):
        #if trace: print("rehasing before:", self.__items)
        value = self.__flattened()

        self.__limit *= 2
        self.__items =[self.__none] * self.__limit

        for i in value: self.__setitem__(i)

    '''def add(self, item):
        if item in self: return

        self.__add(item)
        self.__count += 1

        if (0.0 + self.__count) / self.__limit > .75:
            self.__rehash()'''

    def __setitem__(self, key, value):
        h = hash(key) % self.__limit

        if not self.__items[h]:
            self.__items[h] = [[key, value]]
        else:
            self.__items[h].append([key, value])

        self.__count += 1

        if (0.0 + self.__count) / self.__limit > 0.75: self.__rehash()

    def __hash(self, item): return(hash(item) % self.__limit)

    def __delitem__(self, key):
        if key not in self: raise KeyError ("Item not in hash_set")

        h = self.__hash(key)
        self.__items[h].remove(key)

        if self.__items[h] == []:
            self.__items[h] = self.__none

        self.__count -= 1

    def __contains__(self, key):
        h = self.__hash(key)
        if  self.__items[h] != self.__none:
            for i in self.__items[h]:
                if i == key:return True
        return False

    def __getitem__(self, key):
        if not h:
            raise KeyError(key)
        #What item is being fetched and what is unfetchable
        if key >= 0 and key < self.__items:
            return self.__items[key]
        raise IndexError('Key out of range')

        '''if self.__hash(key) is None:
            raise TypeError('not indexable')
        h = []
        for item in self.__items:
            if h == key:
                h.append(item)
        if not h:
            raise KeyError(key)
        if len(h) == 1:
            return h[0]
        else: return h

        key = self.__hash(key) % len(self.__items)
        h = []
        while self.__items != None:
            if self.__items[h] == key:
                return self.__items[h]
            h = (h + 1) % len(self.__items)
        return None'''


class test_my_hash_set(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(len(my_hash_set()), 0)
    def test_len_one(self):
        s = my_hash_set()
        s[1] = "one"
        self.assertEquals(len(s), 1)
    def test_add_one(self):
        s = my_hash_set()
        s[1] = "one"
        self.assertEquals(s[1], "one")
    def test_add_two(self):
        s = my_hash_set()
        s[1] = "one"
        s[2] = "two"
        self.assertEquals(len(s), 2)
    def test_add_twice(self):
        s = my_hash_set()
        s[1] = "one"
        s[1] = "one"
        self.assertEquals(len(s), 1)


if __name__ == '__main__':
    unittest.main()