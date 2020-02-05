import unittest

# time complexity O(n**2)
# space complexity O(1)

def insertion_sort(arr):
    for i in range(1,len(arr)):
        j = i - 1
        while (j >= 0) and (arr[i] < arr[j]):
            j -= 1
        tmp = arr[i]
        arr[j+2:i+1] = arr[j+1:i]
        arr[j+1] = tmp
    return arr

class Test(unittest.TestCase):
    def test_insertion_sort(self):
        arr = [3,6,9,7,8,4,2,5,1,9,6]
        self.assertEqual(insertion_sort(arr), [1,2,3,4,5,6,6,7,8,9,9]);

if __name__ == "__main__":
    unittest.main()
