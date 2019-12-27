# 10.6 in Elements of Programming Interviews in Python (Sep 15, 2016)
# design an algorithm that computes the k largest elements stored in the
# max-heap.

import unittest

# time complexity O(k*logk)
# space complexity O(k)

def k_largest_elements(arr, k):
    if k <= 0:
        raise ValueError('k should be a positive integer!')
    if k > len(arr):
        raise ValueError('k should not be larger than length of the array!')

    # track the index of current largest node in heap
    i = 0
    # insert node i's children to a sorted list
    ordered_children = []
    # pop out the next largest node from ordered_children
    # and append to k_largest
    k_largest = []
 
    # max heap is represented by a list
    # the first item in the list is 0, which is a place holder
    while i < len(arr):
        if 2*i < len(arr):
            insert_child(ordered_children, (2*i, arr[2*i]))
        if (2*i + 1) < len(arr):
            insert_child(ordered_children, (2*i + 1, arr[2*i + 1]))
        current_largest = ordered_children.pop(0)
        k_largest.append(current_largest[1])
        if len(k_largest) >= k:
            break
        i = current_largest[0]

    return k_largest

def insert_child(ordered_children, child):
    if ordered_children == []:
        ordered_children.append(child)
    
    i = 0
    while i < len(ordered_children):
        if child[1] <= ordered_children[i][1]:
            i += 1
        else:
            break
    ordered_children.insert(i, child)

class Test(unittest.TestCase):
    def test_k_largest_elements(self):
        heap = [0, 561,314,401,28,156,359,271,11,3]
        self.assertEqual(k_largest_elements(heap, 4), [561,401,359,314]);

if __name__ == "__main__":
    unittest.main()
