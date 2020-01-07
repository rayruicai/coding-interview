import unittest

# time complexity O(n**2)
# space complexity O(1)

def selection_sort(arr):
    n = len(arr)
    while n >= 2:
        value_max = arr[0]
        index_max = 0
        for i in range(1, n):
            if arr[i] > value_max:
                value_max = arr[i]
                index_max = i

        arr[n-1], arr[index_max] = arr[index_max], arr[n-1]
        n -= 1

    return arr

class Test(unittest.TestCase):
    def test_selection_sort(self):
        arr = [3,6,9,7,8,4,2,5,1,9,6]
        self.assertEqual(selection_sort(arr), [1,2,3,4,5,6,6,7,8,9,9]);

if __name__ == "__main__":
    unittest.main()
