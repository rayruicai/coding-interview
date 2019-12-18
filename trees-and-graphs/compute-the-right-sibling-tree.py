# 9.16 in Elements of Programming Interviews in Python (Sep 15, 2016)
# Write a program that takes a perfect binary tree, and sets each node's
# level-next field to the node on its right, if one exists.

import unittest

# time complexity O(number of nodes)
# space complexity O(number of nodes)

class BinaryTreeNode():
    def __init__(self, data=None, left=None, right=None, level_next=None):
        self.data = data
        self.left = left
        self.right = right
        self.level_next = level_next

def set_right_sibling_1(rootNode):
    # since it's perfect binary tree, the left childs will always have
    # right siblings
    if rootNode.left != None:
        rootNode.left.level_next = rootNode.right
        if rootNode.level_next != None:
            rootNode.right.level_next = rootNode.level_next.left
        set_right_sibling_1(rootNode.left)
        set_right_sibling_1(rootNode.right)

# time complexity O(number of nodes)
# space complexity O(1)

def set_right_sibling_helper(rootNode):
        # since it's perfect binary tree, the left childs will always have
        # right siblings
        while rootNode != None and rootNode.left != None:
            rootNode.left.level_next = rootNode.right
            if rootNode.level_next != None:
                rootNode.right.level_next = rootNode.level_next.left
            rootNode = rootNode.level_next

def set_right_sibling_2(rootNode):
    while rootNode.left != None:
        set_right_sibling_helper(rootNode)
        rootNode = rootNode.left

class Test(unittest.TestCase):
    def test_set_right_sibling(self):

        A = BinaryTreeNode('A')
        B = BinaryTreeNode('B')
        C = BinaryTreeNode('C')
        D = BinaryTreeNode('D')
        E = BinaryTreeNode('E')
        F = BinaryTreeNode('F')
        G = BinaryTreeNode('G')
        H = BinaryTreeNode('H')
        I = BinaryTreeNode('I')
        J = BinaryTreeNode('J')
        K = BinaryTreeNode('K')
        L = BinaryTreeNode('L')
        M = BinaryTreeNode('M')
        N = BinaryTreeNode('N')
        O = BinaryTreeNode('O')
        
        A.left, A.right = B, I
        B.left, B.right = C, F
        C.left, C.right = D, E
        F.left, F.right = G, H
        I.left, I.right = J, M
        J.left, J.right = K, L
        M.left, M.right = N, O

        set_right_sibling_1(A)
        self.assertEqual(D.level_next.data, 'E');
        self.assertEqual(E.level_next.data, 'G');
        self.assertEqual(H.level_next.data, 'K');

        A.level_next = None
        B.level_next = None
        C.level_next = None
        D.level_next = None
        E.level_next = None
        F.level_next = None
        G.level_next = None
        H.level_next = None
        I.level_next = None
        J.level_next = None
        K.level_next = None
        L.level_next = None
        M.level_next = None
        N.level_next = None
        O.level_next = None

        set_right_sibling_2(A)
        self.assertEqual(D.level_next.data, 'E');
        self.assertEqual(E.level_next.data, 'G');
        self.assertEqual(H.level_next.data, 'K');

if __name__ == "__main__":
    unittest.main()
