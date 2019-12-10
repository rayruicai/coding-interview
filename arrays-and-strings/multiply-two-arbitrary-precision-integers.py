# 5.3 in Elements of Programming Interviews in Python (Sep 15, 2016)
# write a program that takes two arrays representing integers, and returns
# an integer representing their product.
# time complexity O(ij)
# space complexity O(i+j)

import unittest

def multiply_integers(arr1, arr2):

    len_arr1 = len(arr1)
    len_arr2 = len(arr2)
    arr3 = [0] * (len_arr1 + len_arr2)

    # convert both integers to absolute values, add back the sign in the end
    sign = 1

    if arr1[0] < 0:
        arr1[0] *= -1
        sign *= -1

    if arr2[0] < 0:
        arr2[0] *= -1
        sign *= -1

    # multiply each digit one by one and add up to final list
    for i in range(len_arr1):
        for j in range(len_arr2):
            product = arr1[len_arr1 - 1 - i] * arr2[len_arr2 - 1 - j]
            arr3[len_arr1 + len_arr2 - 1 - j - i] += product

    # adjust overflow
    for n in range(len_arr1 + len_arr2):
        if arr3[len_arr1 + len_arr2 - 1 - n] >= 10:
            first_digit = arr3[len_arr1 + len_arr2 - 1 - n] % 10
            second_digit = arr3[len_arr1 + len_arr2 - 1 - n] // 10
            arr3[len_arr1 + len_arr2 - 1 - n] = first_digit
            arr3[len_arr1 + len_arr2 - 1 - n - 1] += second_digit

    # remove first digit if it is zero
    if arr3[0] == 0:
        arr3 = arr3[1:]

    # add back the sign
    arr3[0] = arr3[0] * sign

    return arr3

class Test(unittest.TestCase):
    def test_multiply_integers(self):
        arr1 = [1, 2, 3, 4]
        arr2 = [5, 6, 7]
        self.assertEqual(multiply_integers(arr1, arr2), [6, 9, 9, 6, 7, 8]);
        arr1 = [-1, 2, 3, 4]
        arr2 = [5, 6, 7]
        self.assertEqual(multiply_integers(arr1, arr2), [-6, 9, 9, 6, 7, 8]);
        arr1 = [-1, 2, 3, 4]
        arr2 = [-5, 6, 7]
        self.assertEqual(multiply_integers(arr1, arr2), [6, 9, 9, 6, 7, 8]);

if __name__ == "__main__":
    unittest.main()
