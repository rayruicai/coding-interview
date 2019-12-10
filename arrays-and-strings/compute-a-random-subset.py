# 5.15 in Elements of Programming Interviews in Python (Sep 15, 2016)
# design an algorithm that returns any one of k-size subsets in n-size set
# with equal probability.

import unittest
import random

# time complexity O(k)
# space complexity O(n)

def compute_random_subset_1(n, k):
    if k > n:
        return None

    # randomly select a sample from remaining arr1 for k times.
    arr1 = list(range(n))
    arr2 = []
    random.seed(1)
    while k > 0:
        i = random.randint(0, n - 1)
        arr2.append(arr1.pop(i))
        k -= 1
        n -= 1

    return arr2

# time complexity O(k)
# space complexity O(k)

def compute_random_subset_2(n, k):
    if k > n:
        return None

    # generate a random k-size subset by swapping first k elements with another
    # k elements in n-size set.
    # use a hash table to store index-element, assume the original index of each
    # element is A[i] = i.
    swap_positions = {}
    for i in range(k):
        new_index = random.randint(0, n - 1)
        element_1 = swap_positions.get(i, i)
        element_2 = swap_positions.get(new_index, new_index)
        swap_positions[i] = element_2
        swap_positions[new_index] = element_1

    return [swap_positions[i] for i in range(k)]

class Test(unittest.TestCase):
    def test_compute_random_subset(self):
        random.seed(1)
        self.assertEqual(compute_random_subset_1(100, 5), [17, 73, 99, 8, 34]);
        self.assertEqual(compute_random_subset_2(100, 5), [15, 63, 97, 57, 60]);

if __name__ == "__main__":
    unittest.main()
