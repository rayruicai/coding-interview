# 12.9 in Elements of Programming Interviews in Python (Sep 15, 2016)
# Write a program which takes as input a set of integers represented by an
# array, and returns the size of a largest subset of integers in the array
# having the property that if two integers are in the subset, then so are all
# integers between them.

import unittest

# time complexity O(len(arr))
# space complexity O(len(arr))

def longest_interval(arr):
    # for each element in the list, check whether the adjacent numbers are also
    # in the list, if yes, remove them, and then calculate the max length,
    # iterate the checking until the list is empty.
    max_interval = 0
    while len(arr) > 0:
        current_value = arr.pop()
        value_before = current_value - 1
        value_after = current_value + 1
        while value_before in arr:
            arr.remove(value_before)
            value_before -= 1
        while value_after in arr:
            arr.remove(value_after)
            value_after += 1
        max_interval = max(max_interval, value_after - value_before - 1)

    return max_interval

class Test(unittest.TestCase):
    def test_longest_interval(self):
        arr = [3,-2,7,9,8,1,2,0,-1,5,8]
        self.assertEqual(longest_interval(arr), 6);

if __name__ == "__main__":
    unittest.main()
