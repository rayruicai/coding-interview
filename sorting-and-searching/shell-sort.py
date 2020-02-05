import unittest

# time complexity O(n**2)
# space complexity O(1)

def shell_sort(arr):
    n = len(arr)
    gap = n//2
    while gap >= 1:
        for start in range(gap):
            gap_insertion_sort(arr, start, gap)
        gap = gap//2
    return arr

def gap_insertion_sort(arr, start, gap):
    n = len(arr)
    for i in range(start, n, gap):
        j = i - gap
        while (j >= start) and (arr[i] < arr[j]):
            arr[i], arr[j] = arr[j], arr[i]
            i = j
            j -= gap

class Test(unittest.TestCase):
    def test_shell_sort(self):
        arr = [3,6,9,7,8,4,2,5,1,9,6]
        self.assertEqual(shell_sort(arr), [1,2,3,4,5,6,6,7,8,9,9]);

if __name__ == "__main__":
    unittest.main()
