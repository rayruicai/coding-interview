# 9.13 in Elements of Programming Interviews in Python (Sep 15, 2016)
# Design an algorithm for reconstructing a binary tree from a preorder traversal
# visit sequence that uses null to mark empty children.

import unittest

# time complexity O(len(sequence))
# space complexity O(len(sequence))

class BinaryTreeNode():
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def reconstruct_preorder(sequence):
    def reconstruct_preorder_helper(sequence_iter):
        node = next(sequence_iter)
        if node == None:
            return None

        left_subtree = reconstruct_preorder_helper(sequence_iter)
        right_subtree = reconstruct_preorder_helper(sequence_iter)
        return BinaryTreeNode(node, left_subtree, right_subtree)

    return reconstruct_preorder_helper(iter(sequence))

class Test(unittest.TestCase):
    def test_reconstruct_preorder(self):

        sequence = ['H', 'B', 'F', None, None, 'E', 'A', None, None, None, \
                    'C', None, 'D', None, 'G', 'I', None, None, None]

        tree = reconstruct_preorder(sequence)

        def preorder_w_markers(tree):
        
            sequence = []
            preorder_w_markers_helper(tree, sequence)
            return sequence
        
        def preorder_w_markers_helper(tree, sequence):
        
            if tree:
                sequence.append(tree.data)
        
                if tree.left == None:
                    sequence.append(None)
                else:
                    preorder_w_markers_helper(tree.left, sequence)
        
                if tree.right == None:
                    sequence.append(None)
                else:
                    preorder_w_markers_helper(tree.right, sequence)

        sequence_2 = preorder_w_markers(tree)

        self.assertEqual(sequence, sequence_2);

if __name__ == "__main__":
    unittest.main()
