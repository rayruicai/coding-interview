import unittest

# time complexity O(n*n)
# space complexity O(log(n))

def quick_sort(arr):
    n = len(arr)
    quick_sort_helper(arr,0,n-1)

def quick_sort_helper(arr,first,last):
    if first < last:
        splitpoint = partition(arr,first,last)

        quick_sort_helper(arr,first,splitpoint-1)
        quick_sort_helper(arr,splitpoint+1,last)

def partition(arr,first,last):
    pivotvalue = arr[first]
    leftmark = first+1
    rightmark = last

    done = False

    while not done:

        while leftmark <= rightmark and arr[leftmark] <= pivotvalue:
            leftmark += 1

        while leftmark <= rightmark and pivotvalue <= arr[rightmark]:
            rightmark -= 1

        if rightmark < leftmark:
            done = True
        else:
            arr[leftmark], arr[rightmark] = arr[rightmark], arr[leftmark]

    arr[rightmark], arr[first] = arr[first], arr[rightmark]

    return rightmark

class Test(unittest.TestCase):
    def test_quick_sort(self):
        arr = [3,6,9,7,8,4,2,5,1,9,6]
        quick_sort(arr)
        self.assertEqual(arr, [1,2,3,4,5,6,6,7,8,9,9]);

if __name__ == "__main__":
    unittest.main()
