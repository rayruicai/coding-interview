# 11.7 in Elements of Programming Interviews in Python (Sep 15, 2016)
# design an algorithm to find the min and max elements in an array with
# less than the 2(n-1) comparisons

import unittest

# time complexity O(n)
# space complexity O(1)

def find_min_max(arr):
    n = len(arr)
    minimum = arr[0]
    maximum = arr[0]
    if n == 0:
        return None
    elif n == 1:
        return (minimum, maximum)
    else:
        # split array to pairs, compare each pair first, then compare the larger
        # one with the max and compare the smaller one with the min, total
        # 3/2*n - 2 times comparisons
        for i in range(n//2):
            if arr[i*2] <= arr[i*2+1]:
                min_tmp, max_tmp = arr[i*2], arr[i*2+1]
            else:
                min_tmp, max_tmp = arr[i*2+1], arr[i*2]
            if min_tmp < minimum:
                minimum = min_tmp
            if max_tmp > maximum:
                maximum = max_tmp
        # if the length of the array is an odd number, we need to compare
        # 3/2*(n-1) times
        if n % 2 == 1:
            if arr[-1] < minimum:
                minimum = arr[-1]
            if arr[-1] > maximum:
                maximum = arr[-1]

    return (minimum, maximum)

class Test(unittest.TestCase):
    def test_find_min_max(self):
        arr1 = [3,2,5,1,2,4]
        arr2 = [3,2,5,1,2]
        arr3 = [3,2]
        self.assertEqual(find_min_max(arr1), (1, 5));
        self.assertEqual(find_min_max(arr2), (1, 5));
        self.assertEqual(find_min_max(arr3), (2, 3));

if __name__ == "__main__":
    unittest.main()
