# 14.7 in Elements of Programming Interviews in Python (Sep 15, 2016)
# Design an algorithm for efficiently computing the k smallest numbers of the
# form a + b * sqrt(2) for nonnegative integers a and b.

import unittest
import math
from sortedcontainers import SortedList

# time complexity O(k*log(k))
# space complexity O(k)

def form(a, b):
    return round(a + b * math.sqrt(2), 2)

def k_smallest_numbers(a, b, k):
    if (a + 1) * (b + 1) < k:
        raise ValueError('k should be less than all possible combinations!')

    i = 0
    j = 0
    v = form(i, j)

    # use SortedList to represent BST
    candidates = SortedList([(v, i, j)])
    arr = []

    while len(arr) < k:
        v, i, j = candidates.pop(0)
        arr.append(v)
        if ((i + 1) <= a) and ((form(i + 1, j), i + 1, j) not in candidates):
            candidates.add((form(i + 1, j), i + 1, j))
        if ((j + 1) <= b) and ((form(i, j + 1), i, j + 1) not in candidates):
            candidates.add((form(i, j + 1), i, j + 1))

    return arr

class Test(unittest.TestCase):
    def test_k_smallest_numbers(self):
        a, b, k = 3, 2, 7
        arr = [0.0, 1.0, 1.41, 2.0, 2.41, 2.83, 3.0]
        self.assertEqual(k_smallest_numbers(a, b, k), arr);

if __name__ == "__main__":
    unittest.main()
