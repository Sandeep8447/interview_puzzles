# Task:
#
# You are given the root of a binary tree, along with two nodes, A and B. Find and return the lowest common ancestor
# of A and B. For this problem, you can assume that each node also has a pointer to its parent, along with its left and
# right child.
#
# class TreeNode:
#   def __init__(self, val):
#     self.left = None
#     self.right = None
#     self.parent = None
#     self.val = val
#
#
# def lowestCommonAncestor(root, a, b):
#   # Fill this in.
#
# #   a
# #  / \
# # b   c
# #    / \
# #   d*  e*
# root = TreeNode('a')
# root.left = TreeNode('b')
# root.left.parent = root
# root.right = TreeNode('c')
# root.right.parent = root
# a = root.right.left = TreeNode('d')
# root.right.left.parent = root.right
# b = root.right.right = TreeNode('e')
# root.right.right.parent = root.right
#
# print lowestCommonAncestor(root, a, b).val
# # c
from typing import Dict


class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.parent = None
        self.val = val


def lowest_common_ancestor(root_node: TreeNode, a_node: TreeNode, b_node: TreeNode) -> TreeNode:
    a_ancestors: Dict[TreeNode] = dict()
    a_ancestors[a_node.val] = a_node
    a_node_to_process: TreeNode = a_node
    while a_node_to_process.parent is not None:
        a_node_to_process = a_node_to_process.parent
        a_ancestors[a_node_to_process.val] = a_node_to_process
    b_node_to_process: TreeNode = b_node
    while b_node_to_process is not None:
        if a_ancestors.__contains__(b_node_to_process.val):
            return b_node_to_process
        else:
            b_node_to_process = b_node_to_process.parent
    return None


#   a
#  / \
# b   c
#    / \
#   d*  e*
root = TreeNode('a')
root.left = TreeNode('b')
root.left.parent = root
root.right = TreeNode('c')
root.right.parent = root
a = root.right.left = TreeNode('d')
root.right.left.parent = root.right
b = root.right.right = TreeNode('e')
root.right.right.parent = root.right

print(lowest_common_ancestor(root, a, b).val)
# c
print(lowest_common_ancestor(root, root.left, b).val)
# a
print(lowest_common_ancestor(root, root.right, b).val)
# c
print(lowest_common_ancestor(root, root, TreeNode('f')))
# None