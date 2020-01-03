# 11.6 in Elements of Programming Interviews in Python (Sep 15, 2016)
# design an algorithm that takes a 2D sorted array and a number
# and checks whether that number appears in the array.

import unittest
from numpy import array

# time complexity O(i + j)
# space complexity O(1)

def search_2D_array(arr, num):
    # search from the upper-left corner to bottom-right corner
    i = 0
    j = len(arr[0]) - 1

    while i <= (len(arr[:,0]) - 1) and j >= 0:
        if arr[i][j] == num:
            return True
        elif arr[i][j] > num:
            j -= 1
        else:
            i += 1

    return False

class Test(unittest.TestCase):
    def test_search_2D_array(self):
        arr = [ [-1, 2, 4, 4, 6],
                [1, 5, 5, 9, 21],
                [3, 6, 6, 9, 22],
                [3, 6, 8, 10, 24],
                [6, 8, 9, 12, 25],
                [8, 10, 12, 13, 40] ]
        arr = array(arr)
        self.assertEqual(search_2D_array(arr, 8), True);
        self.assertEqual(search_2D_array(arr, 7), False);

if __name__ == "__main__":
    unittest.main()
