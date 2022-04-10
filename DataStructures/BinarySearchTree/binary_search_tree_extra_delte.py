from profiler import *
from math import log


class TreeNode:
    # attributes:
    # key
    # value (optional, use when storing key-value pairs)
    # left: a TreeNode
    # right: a TreeNode
    # parent: a TreeNode

    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


class BinarySearchTree:
    # attribute:
    # root: a TreeNode

    def __init__(self):
        self.root = None

        # delete func
        self.delete = self.delete_2

    def height(self):
        if self.root is None:
            return None
        if self.root.left is None and self.root.right is None:
            return 0
        return self.__height_rec(self.root)

    def __height_rec(self, node):
        if node is None or (node.right is None and node.left is None):
            return 0
        return 1 + max(
            self.__height_rec(node.left),
            self.__height_rec(node.right))

    def find(self, key):
        if self.root is None:
            return None
        return self.__find_rec(self.root, key)

    def __find_rec(self, node, key):
        # Returns node if key matches
        if node.key == key:
            return node

        # left or right node checked based on key
        if key < node.key:
            if node.left is not None:
                return self.__find_rec(node.left, key)
            return None
        elif key > node.key:
            if node.right is not None:
                return self.__find_rec(node.right, key)
            return None

    def insert(self, node):
        if self.root is None:
            self.root = node
        self.__insert_rec(self.root, node)

    def __insert_rec(self, cur_node, to_insert):
        # Checks which side of cur_node to put to_insert
        if to_insert.key < cur_node.key:
            # inserts if there is no node on left
            if cur_node.left is None:
                cur_node.left = to_insert
                to_insert.parent = cur_node
            else:
                self.__insert_rec(cur_node.left, to_insert)
        elif to_insert.key > cur_node.key:
            # inserts if there is no node on right
            if cur_node.right is None:
                cur_node.right = to_insert
                to_insert.parent = cur_node
            else:
                self.__insert_rec(cur_node.right, to_insert)

    def delete_1(self, node):
        # Finding smallest node greater than given one
        orig_node = node
        if node.right is not None:
            node = node.right
            while node.left:
                node = node.left

        orig_node.key = node.key
        orig_node.value = node.value

        # Check if node to remove is root
        if node == self.root:
            self.root = None
        else:
            # Detaches node
            child_type = "left" if node.parent.left == node else "right"
            setattr(node.parent, child_type, None)

    def delete_2(self, node):
        num_children = 0
        if node.left:
            num_children += 1
        if node.right:
            num_children += 1

        # Case 1 (0 children)
        if num_children == 0:
            if node.parent:
                child_type = "left" if node.parent.left == node else "right"
                setattr(node.parent, child_type, None)
            else:
                # root case
                self.root = None

        # Case 2 (1 child)
        # (mostly same code as Case 3, just wanted to split them up to make it clearer when coding)
        elif num_children == 1:
            if node.left:
                # Attach child of node to node's parent
                if node.parent:
                    child_type = "left" if node.parent.left == node else "right"
                    setattr(node.parent, child_type, node.left)

                node.left.parent = node.parent

                # assigns root if removing root
                if node == self.root:
                    self.root = node.left

            else:
                # Finding smallest node greater than node
                orig_node = node
                if node.right is not None:
                    node = node.right
                    while node.left:
                        node = node.left

                # Detaching node, attaching node.right
                child_type = "left" if node.parent.left == node else "right"
                setattr(node.parent, child_type, node.right)
                if node.right:
                    node.right.parent = node.parent
                    node.parent.child_type = node.right

                # Attaching node at orig_node's location
                if orig_node.parent:
                    child_type = "left" if orig_node.parent.left == orig_node else "right"
                    setattr(orig_node.parent, child_type, node)
                node.parent = orig_node.parent
                node.left = orig_node.left
                node.right = orig_node.right

                # Reassigns parent if orig_node.right is not node itself
                if orig_node.right:
                    orig_node.right.parent = node

                # reassigns root if removing root
                if orig_node == self.root:
                    self.root = node

        # Case 3 (2 children)
        else:
            # Finding smallest node greater than node
            orig_node = node
            if node.right is not None:
                node = node.right
                while node.left:
                    node = node.left

            # Detaching node, attaching node.right
            child_type = "left" if node.parent.left == node else "right"
            setattr(node.parent, child_type, node.right)
            if node.right:
                node.right.parent = node.parent
                node.parent.child_type = node.right

            # Attaching node at orig_node's location
            if orig_node.parent:
                child_type = "left" if orig_node.parent.left == orig_node else "right"
                setattr(orig_node.parent, child_type, node)
            node.parent = orig_node.parent
            node.left = orig_node.left
            node.right = orig_node.right

            # Assigning parents
            if orig_node.left:
                orig_node.left.parent = node
            if orig_node.right:
                orig_node.right.parent = node

            # reassigns root if removing root
            if orig_node == self.root:
                self.root = node

    def delete_3(self, node):
        num_children = 0
        if node.left:
            num_children += 1
        if node.right:
            num_children += 1

        # Case 1 (0 children)
        if num_children == 0:
            if node.parent:
                child_type = "left" if node.parent.left == node else "right"
                setattr(node.parent, child_type, None)
            else:
                # root case
                self.root = None

        # Case 2 (1 child)
        # (mostly same code as Case 3, just wanted to split them up to make it clearer when coding)
        elif num_children == 1:
            if node.left:
                # Attach child of node to node's parent
                if node.parent:
                    child_type = "left" if node.parent.left == node else "right"
                    setattr(node.parent, child_type, node.left)

                node.left.parent = node.parent

                # assigns root if removing root
                if node == self.root:
                    self.root = node.left

            else:
                # Finding smallest node greater than node
                orig_node = node
                if node.right is not None:
                    node = node.right
                    while node.left:
                        node = node.left

                # Detaching node, attaching node.right
                child_type = "left" if node.parent.left == node else "right"
                setattr(node.parent, child_type, node.right)
                if node.right:
                    node.right.parent = node.parent
                    node.parent.child_type = node.right

                # Attaching node at orig_node's location
                if orig_node.parent:
                    child_type = "left" if orig_node.parent.left == orig_node else "right"
                    setattr(orig_node.parent, child_type, node)
                node.parent = orig_node.parent
                node.left = orig_node.left
                node.right = orig_node.right

                # Reassigns parent if orig_node.right is not node itself
                if orig_node.right:
                    orig_node.right.parent = node

                # reassigns root if removing root
                if orig_node == self.root:
                    self.root = node

        # Case 3 (2 children)
        else:
            # Finding smallest node greater than node
            orig_node = node
            if node.right is not None:
                node = node.right
                while node.left:
                    node = node.left

            # Moving left subtree over to successor
            node.left = orig_node.left
            orig_node.left.parent = node

            # Removing orig_node
            if orig_node.parent:
                orig_node.right = orig_node.parent
                child_type = "left" if orig_node.parent.left == orig_node else "right"
                setattr(orig_node.parent, child_type, orig_node.right)

            # reassigns root if removing root
            if orig_node == self.root:
                self.root = orig_node.right

'''
# Problem 2
# The heights are about twice as much as log n

tests = get_random_lists([10, 100, 1000, 10000, 50000])
for test in tests:
    bst = BinarySearchTree()
    for n in test:
        bst.insert(TreeNode(n))
    print("log:", log(len(test), 2), "height:", bst.height())
'''

'''
# Problem 3 (Ivan gave me his code to help me test my functions, I read through it and understand it)
# The heights are still about twice as much as log n
random_lists = get_random_lists([200, 2000, 20000, 200000])
for lists in random_lists:
    bst = BinarySearchTree()
    num_delete = len(lists) // 2
    keys_to_delete = sample(lists, num_delete)
    nodes_to_delete = []
    index_to_delete = 0
    for i in lists:
        j = TreeNode(i)
        bst.insert(j)
        if index_to_delete < num_delete:
            if i == keys_to_delete[index_to_delete]:
                nodes_to_delete.append(j)
                index_to_delete += 1
    for dying_nodes in nodes_to_delete:
        bst.delete_1(dying_nodes)
    tree_height = bst.height()
    length = len(lists) // 2
    print("Expected height: log", length, "=", log(length, 2))
    print("Actual height: ", tree_height)
'''