import unittest

# time complexity O(n**2)
# space complexity O(1)

def bubble_sort(arr):
    n = len(arr)
    while n >= 2:
        for i in range(n-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        n -= 1

    return arr

class Test(unittest.TestCase):
    def test_bubble_sort(self):
        arr = [3,6,9,7,8,4,2,5,1,9,6]
        self.assertEqual(bubble_sort(arr), [1,2,3,4,5,6,6,7,8,9,9]);

if __name__ == "__main__":
    unittest.main()
