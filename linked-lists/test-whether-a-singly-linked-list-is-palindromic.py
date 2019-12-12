# 7.11 in Elements of Programming Interviews in Python (Sep 15, 2016)
# write a program that tests whether a singly linked list is palindromic.

import unittest

# time complexity O(len(LinkedList))
# space complexity O(1)

class Node():
    def __init__(self, data, next):
        self.data = data
        self.next = next

def is_palindromic(Node):
    # find the start node of the second half list
    slow = Node
    fast = Node
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    if fast is None:
        # odd elements
        second_start = slow.next
    else:
        # even elements
        second_start = slow

    # compare the first half list with the reversed second half list
    first_half = Node
    second_half = reverse_list(second_start)
    while first_half and second_half:
        if first_half.data != second_half.data:
            return False
        else:
            first_half = first_half.next
            second_half = second_half.next

    return True

def reverse_list(Node):
    prev_node = None
    curr_node = Node
    while curr_node is not None:
        next_node = curr_node.next
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = next_node

    return prev_node

class Test(unittest.TestCase):
    def test_is_palindromic(self):
        linked_list_1 = Node(1,Node(2,Node(3,Node(2,Node(1,None)))))
        self.assertEqual(is_palindromic(linked_list_1), True);
        linked_list_2 = Node(1,Node(2,Node(3,Node(3,Node(2,Node(1,None))))))
        self.assertEqual(is_palindromic(linked_list_2), True);

if __name__ == "__main__":
    unittest.main()
