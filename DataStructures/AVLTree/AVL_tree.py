from pretty_print import *

class AVLTreeNode:
    # attributes:
    # key
    # value (optional, use when storing key-value pairs)
    # left: a TreeNode
    # right: a TreeNode
    # parent: a TreeNode
    # height: length of longest path of children

    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.height = 0


class AVLTree:
    # attribute:
    # root: a TreeNode

    def __init__(self):
        self.root = None

        # delete func
        self.delete = self.delete1

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

        # balancing
        if node.parent is not None:
            self.balance(node)

        assert(self.is_balanced())

    def __insert_rec(self, cur_node, to_insert):
        # Checks which side of cur_node to put to_insert
        if to_insert.key < cur_node.key:
            # inserts if there is no node on left
            if cur_node.left is None:
                cur_node.left = to_insert
                to_insert.parent = cur_node
                cur_node.height = 1
            else:
                self.__insert_rec(cur_node.left, to_insert)
        elif to_insert.key > cur_node.key:
            # inserts if there is no node on right
            if cur_node.right is None:
                cur_node.right = to_insert
                to_insert.parent = cur_node
                cur_node.height = 1
            else:
                self.__insert_rec(cur_node.right, to_insert)

    def delete1(self, node):
        # Finding smallest node greater than given one
        orig_node = node
        if node.right is not None:
            node = node.right
            while node.left:
                node = node.left

        # Swapping values, keys
        orig_node.key = node.key
        orig_node.value = node.value

        # Check if node to remove is root
        if node == self.root:
            self.root = None
        # Checks if it is itself
        elif node == orig_node:
            # Detaches node
            child_type = "left" if node.parent.left == node else "right"
            setattr(node.parent, child_type, node.left)
            if node.left is not None:
                node.left.parent = node.parent
                node.parent.height = node.left.height + 1
            else:
                self.fix_node_height(node.parent)
        else:
            # Detaches node
            child_type = "left" if node.parent.left == node else "right"
            # Attach right subtree (traversed as far as can left already)
            setattr(node.parent, child_type, node.right)
            if node.right is not None:
                node.right.parent = node.parent
                node.parent.height = node.right.height + 1
            else:
                self.fix_node_height(node.parent)

        # balancing
        if node.parent is not None:
            self.balance(node.parent)

        assert(self.is_balanced())

    def traverse_heights(self, output=None, node="root"):
        if output is None:
            output = []
        if node == "root":
            node = self.root
        if not node:
            return
        self.traverse_heights(output, node.left)
        output.append([node.key, node.height])
        self.traverse_heights(output, node.right)
        return(output)

    def is_bst(self, node="root", min_range=None, max_range=None):
        # Use traversal for keeping range of numbers code can be in
        # if min_range or max_range is None, no restriction on that side
        if node == "root":
            node = self.root
        if node is None:
            return True

        # Check if the node is in the range specified
        if min_range is not None:
            if node.key <= min_range:
                return False
        if max_range is not None:
            if node.key >= max_range:
                return False

        return (self.is_bst(node.left, min_range, node.key)
                and self.is_bst(node.right, node.key, max_range))

    def rotate(self, node):
        #   A            C
        #  / \          / \
        # B   C   ->   A   E
        #    / \      / \
        #   D   E    B   D

        # Checking if rotating child of root (C=node)
        child_of_root = node.parent == self.root

        # Getting nodes and their types (what kind of children)
        a_parent = node.parent.parent
        a_node = node.parent
        a_type = None
        if a_parent:
            a_type = "left" if a_parent.left == a_node else "right"
        c_type = "left" if a_node.left == node else "right"
        d_type = "left" if c_type == "right" else "right"
        b_node = getattr(a_node, d_type)
        d_node = getattr(node, d_type)
        e_node = getattr(node, c_type)

        # Getting heights
        b_height = -1 if b_node is None else b_node.height
        d_height = -1 if d_node is None else d_node.height
        e_height = -1 if e_node is None else e_node.height

        # Setting heights (A, C, A's parent)
        a_node.height = max(b_height, d_height) + 1
        node.height = max(a_node.height, e_height) + 1
        if a_parent is not None:
            c_height = node.height
            other_height = -1
            other_type = "left" if a_type == "right" else "right"
            if getattr(a_parent, other_type) is not None:
                other_height = getattr(a_parent, other_type).height
            a_parent.height = max(c_height, other_height) + 1

        # Setting parents/children
        setattr(a_node, c_type, d_node)
        if d_node is not None:
            d_node.parent = a_node
        setattr(node, d_type, a_node)
        a_node.parent = node
        node.parent = a_parent
        if a_parent is not None:
            setattr(a_parent, a_type, node)

        # Reassigning root if rotating child of it
        if child_of_root:
            self.root = node

        # Check
        assert(self.is_bst())

    def is_balanced(self, node="root"):
        if node == "root":
            node = self.root
        if node is None:
            return True

        l_height = -1
        if node.left:
            l_height = node.left.height
        r_height = -1
        if node.right:
            r_height = node.right.height
        if abs(l_height - r_height) >= 2:
            return False

        # Checking if both right and left subtrees are balanced
        left_balanced = self.is_balanced(node.left)
        right_balanced = self.is_balanced(node.right)

        return left_balanced and right_balanced

    def balance(self, node):
        # corrects node height first to make balance check valid
        # balances current node
        # fixes height of node.parent
        # calls balance on node.parent

        self.fix_node_height(node)
        parent_node = node.parent

        if not self.is_balanced(node):
            # balancing
            l_height = -1 if node.left is None else node.left.height
            r_height = -1 if node.right is None else node.right.height
            rotating_side = "right" if r_height > l_height else "left"
            inner_side = "left" if r_height > l_height else "right"
            outer_side = rotating_side

            inner_child = getattr(getattr(node, rotating_side), inner_side)
            outer_child = getattr(getattr(node, rotating_side), outer_side)

            # rotating
            i_height = -1 if inner_child is None else inner_child.height
            o_height = -1 if outer_child is None else outer_child.height

            if i_height <= o_height:
                self.rotate(getattr(node, rotating_side))
            else:
                self.rotate(inner_child)
                self.rotate(inner_child)

        # Fix height of parent node
        if parent_node is not None:
            self.fix_node_height(parent_node)

        # Balance parent node
        if parent_node is not None:
            self.balance(parent_node)

    def fix_node_height(self, node):
        # fixes height of current node based on children heights
        l_height = -1
        r_height = -1
        if node.left is not None:
            l_height = node.left.height
        if node.right is not None:
            r_height = node.right.height

        node.height = max(l_height, r_height) + 1

    def fix_heights(self, node):
        # fixes current node and ancestor heights
        if node is not None:
            self.fix_node_height(node)
            self.fix_heights(node.parent)

