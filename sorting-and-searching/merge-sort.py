import unittest

# time complexity O(n*log(n))
# space complexity O(n)

def merge_sort(arr):
    n = len(arr)
    if n > 1:
        mid = n//2

        lefthalf = arr[:mid]
        righthalf = arr[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i = 0
        j = 0
        k = 0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                arr[k] = lefthalf[i]
                k += 1
                i += 1
            else:
                arr[k] = righthalf[j]
                k += 1
                j += 1

        while i < len(lefthalf):
            arr[k] = lefthalf[i]
            k += 1
            i += 1

        while j < len(righthalf):
            arr[k] = righthalf[j]
            k += 1
            j += 1

class Test(unittest.TestCase):
    def test_merge_sort(self):
        arr = [3,6,9,7,8,4,2,5,1,9,6]
        merge_sort(arr)
        self.assertEqual(arr, [1,2,3,4,5,6,6,7,8,9,9]);

if __name__ == "__main__":
    unittest.main()
