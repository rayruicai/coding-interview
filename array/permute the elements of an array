# 5.10 in Elements of Programming Interviews in Python (Sep 15, 2016)
# given an array A of n elements and a permutation P, apply P to A.

import unittest

# time complexity O(i)
# space complexity O(i)

def permute_array_1(arr1, arr2):
    arr3 = [0]*len(arr1)
    for i in range(len(arr1)):
        arr3[arr2[i]] = arr1[i]

    return arr3

# time complexity O(i)
# space complexity O(1)

def permute_array_2(arr1, arr2):
    i = 0
    while i < len(arr1):
        # check the current index is in the correct position,
        # then go to next index.
        if i == arr2[i]:
            i += 1
        # switch the element in the current index with the other element which
        # is in the former element's correct position.
        else:
            tmp1 = arr1[i]
            arr1[i] = arr1[arr2[i]]
            arr1[arr2[i]] = tmp1

            tmp2 = arr2[i]
            arr2[i] = arr2[tmp2]
            arr2[tmp2] = tmp2

    return arr1

class Test(unittest.TestCase):
    def test_permute_array(self):
        arr1 = ['a', 'b', 'c', 'd']
        arr2 = [2, 0, 1, 3]
        self.assertEqual(permute_array_1(arr1, arr2), ['b', 'c', 'a', 'd']);
        self.assertEqual(permute_array_2(arr1, arr2), ['b', 'c', 'a', 'd']);

if __name__ == "__main__":
    unittest.main()
