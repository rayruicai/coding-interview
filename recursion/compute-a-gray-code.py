# 15.10 in Elements of Programming Interviews in Python (Sep 15, 2016)
# write a program which takes n as input and returns an n-bit Gray code.

import unittest

# time complexity O(2**n)
# space complexity O(2**n)

def gray_code(n):
    def gray_code_helper(n):
        if n == 0:
            return [0]

        # use recursion to find the gray code for n - 1
        # generate list 1: add 0 at the front to each number in binary format
        # generate list 2: add 1 at the front to each number in binary format
        # gray code for n: list 1 + reversed(list 2)
        # this approach is provided by the book, although I don't know why
        # it works. lol.
        previous_gray_code = gray_code_helper(n-1)
        leading_bit_one = 1 << (n - 1)
        result = previous_gray_code + \
                    [leading_bit_one | i for i in reversed(previous_gray_code)]
        return result
    return [('{0:0'+str(n)+'b}').format(i) for i in gray_code_helper(n)]

class Test(unittest.TestCase):
    def test_gray_code(self):
        result = ['000', '001', '011', '010', '110', '111', '101', '100']
        self.assertEqual(gray_code(3), result);

if __name__ == "__main__":
    unittest.main()
