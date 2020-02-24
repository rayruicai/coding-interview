
# 15.6 in Elements of Programming Interviews in Python (Sep 15, 2016)
# write a program that takes as input a number and returns all the strings with
# that number of matched pairs of parens.

import unittest

# time complexity O((2n)!/(n!*(n+1)!))
# space complexity O((2n)!/(n!*(n+1)!))

def generate_matched_parens(n):

    def generate_matched_parens_helper(left_parens, right_parens, valid_prefix, result=[]):
        # a valid case for adding left paren is when the number of remaining
        # left parens is greater than zero
        if left_parens > 0:
            generate_matched_parens_helper(left_parens - 1, right_parens, valid_prefix + '(')
        # a valid case for adding right paren is when the number of remaining
        # right parens is greater than the number of remaining left parens
        if left_parens < right_parens:
            generate_matched_parens_helper(left_parens, right_parens - 1, valid_prefix + ')')
        # base case
        if right_parens == 0:
            result.append(valid_prefix)
        return result

    return generate_matched_parens_helper(n, n, '')


class Test(unittest.TestCase):
    def test_generate_matched_parens(self):
        arr3 = ['((()))', '(()())', '(())()', '()(())', '()()()']
        arr4 = ['(((())))', '((()()))', '((())())', '((()))()', '(()(()))', \
                '(()()())', '(()())()', '(())(())', '(())()()', '()((()))', \
                '()(()())', '()(())()', '()()(())', '()()()()']
        self.assertEqual(generate_matched_parens(3), arr3);
        self.assertEqual(generate_matched_parens(4), arr4);

if __name__ == "__main__":
    unittest.main()
