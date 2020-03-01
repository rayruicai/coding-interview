# 17.8 in Elements of Programming Interviews in Python (Sep 15, 2016)
# design an algorithm to compute the area of the largest rectangle contained in
# this skyline.

import unittest

# brute force
# time complexity O(n**2)
# space complexity O(n)
def longest_one(arr):
    width = 0
    max_width = 0
    n = len(arr)
    for i in range(n):
        if arr[i] == 1:
            width += 1
        else:
            max_width = max(max_width, width)
            width = 0
    max_width = max(max_width, width)
    return max_width

def largest_rectangle_1(arr):
    height_scanned = []
    n = len(arr)
    max_area = 0
    for height in arr:
        if height not in height_scanned:
            arr_above = [arr[i] >= height for i in range(n)]
            max_width = longest_one(arr_above)
            area = height * max_width
            max_area = max(max_area, area)
            height_scanned.append(height)

    return max_area

# stack
# time complexity O(n)
# space complexity O(n)
def largest_rectangle_2(arr):
    blocks = []
    max_area = 0
    # add [0] to the end in order to calculate the last block
    arr = arr + [0]
    for i, height in enumerate(arr):
        while blocks != [] and height <= blocks[-1][1]:
            (i_tmp, height_tmp) = blocks.pop()
            if blocks == []:
                area_tmp = i * height_tmp
            else:
                area_tmp = (i - blocks[-1][0] - 1) * height_tmp
            max_area = max(max_area, area_tmp)
        blocks.append((i, arr[i]))

    return max_area

class Test(unittest.TestCase):
    def test_largest_rectangle_1(self):
        arr = [1, 4, 2, 5, 6, 3, 2, 6, 6, 5, 2, 1, 3]
        self.assertEqual(largest_rectangle_1(arr), 20);
    def test_largest_rectangle_2(self):
        arr = [1, 4, 2, 5, 6, 3, 2, 6, 6, 5, 2, 1, 3]
        self.assertEqual(largest_rectangle_2(arr), 20);

if __name__ == "__main__":
    unittest.main()
