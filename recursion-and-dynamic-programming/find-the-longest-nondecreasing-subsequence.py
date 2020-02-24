# 16.12 in Elements of Programming Interviews in Python (Sep 15, 2016)
# write a program that takes as input an array of numbers and returns the length
# of a longest nondecreasing subsequence in the array.

import unittest

# time complexity O(n**2)
# space complexity O(n)

# brute force
def longest_subsequence_1(arr):
    max_length = 0
    n = len(arr)

    for i in range(n):
        arr_tmp = [arr[i]]
        j = i + 1
        while j <= (n - 1):
            if arr_tmp[-1] <= arr[j]:
               arr_tmp.append(arr[j])
            j += 1
        if len(arr_tmp) > max_length:
            max_length = len(arr_tmp)

    return max_length

# dynamic programming
def longest_subsequence_2(arr):
    n = len(arr)
    max_length = [1] * n
    for i in range(n):
        max_length[i] = max((1 + max([max_length[j] for j in range(i) if arr[j] <= arr[i]], default = 0)), max_length[i])

    return max(max_length)

class Test(unittest.TestCase):
    def test_longest_subsequence_1(self):
        arr = [0, 8, 4, 72, 2, 10, 5, 74, 1, 9]
        self.assertEqual(longest_subsequence_1(arr), 4);
    def test_longest_subsequence_2(self):
        arr = [0, 8, 4, 72, 2, 10, 5, 74, 1, 9]
        self.assertEqual(longest_subsequence_2(arr), 4);

if __name__ == "__main__":
    unittest.main()
