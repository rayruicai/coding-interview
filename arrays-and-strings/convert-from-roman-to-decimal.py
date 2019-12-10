# 6.9 in Elements of Programming Interviews in Python (Sep 15, 2016)
# write a program which takes as input a valid Roman number string s
# and retums the integer it corresponds to.

import unittest

# time complexity O(len(string))
# space complexity O(1)

def roman_to_decimal(string):
    rtd_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    rtd_map_exc = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
    num = 0
    i = 0

    while i < len(string):
        if string[i:i+2] in ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']:
            num += rtd_map_exc[string[i:i+2]]
            i += 2
        else:
            num += rtd_map[string[i]]
            i += 1
        
    return num

class Test(unittest.TestCase):
    def test_roman_to_decimal(self):
        self.assertEqual(roman_to_decimal("XXXXXIIIIIIIII"), 59);
        self.assertEqual(roman_to_decimal("LVIIII"), 59);
        self.assertEqual(roman_to_decimal("LIX"), 59);

if __name__ == "__main__":
    unittest.main()
