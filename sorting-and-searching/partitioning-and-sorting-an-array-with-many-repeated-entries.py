# 13.8 in Elements of Programming Interviews in Python (Sep 15, 2016)
# You are given an array of student objects. Each student has an integer-valued
# age field that is to be treated as a key. Rearrange the elements of the array
# so that students of equal age appear together.

import unittest

# not sorted
# time complexity O(n+m)
# space complexity O(m)

def rearrange_elements_1(arr):
    n = len(arr)
    age_dict = {}

    for i in range(n):
        age = arr[i][0]
        name = arr[i][1]
        if age in age_dict:
            age_dict[age].append(name)
        else:
            age_dict[age] = [name]

    m = len(age_dict)

    i = 0
    for key in age_dict:
        while age_dict[key] != []:
            arr[i] = (key, age_dict[key].pop(0))
            i += 1

    return arr

# sorted
# time complexity O(n+k)
# space complexity O(n+k)

def rearrange_elements_2(arr):
    n = len(arr)
    k = 120
    age_dict = {}
    arr_rearranged = []

    for i in range(k):
        age_dict[i] = []
    
    for i in range(n):
        age = arr[i][0]
        name = arr[i][1]
        age_dict[age].append(name)
    
    for i in range(k):
        while age_dict[i] != []:
            arr_rearranged.append((i, age_dict[i].pop(0)))

    return arr_rearranged

class Test(unittest.TestCase):
    def test_rearrange_elements_1(self):
        arr = [(27, 'Courtois'), (30, 'Bale'), (33, 'Ramos'), (31, 'Marcelo'), \
        (27, 'Casemiro'), (27, 'Isco'), (30, 'Kroos')]
        arr_rearranged = [(27, 'Courtois'), (27, 'Casemiro'), (27, 'Isco'), \
        (30, 'Bale'), (30, 'Kroos'), (33, 'Ramos'), (31, 'Marcelo')]
        self.assertEqual(rearrange_elements_1(arr), arr_rearranged);
    def test_rearrange_elements_2(self):
        arr = [(27, 'Courtois'), (30, 'Bale'), (33, 'Ramos'), (31, 'Marcelo'), \
        (27, 'Casemiro'), (27, 'Isco'), (30, 'Kroos')]
        arr_rearranged = [(27, 'Courtois'), (27, 'Casemiro'), (27, 'Isco'), \
        (30, 'Bale'), (30, 'Kroos'), (31, 'Marcelo'), (33, 'Ramos')]
        self.assertEqual(rearrange_elements_2(arr), arr_rearranged);

if __name__ == "__main__":
    unittest.main()
