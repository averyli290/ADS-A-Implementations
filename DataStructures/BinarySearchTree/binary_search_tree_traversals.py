from pretty_print import *


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
        self.delete = self.delete2

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

    def delete1(self, node):
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

    def delete2(self, node):
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

    def traverse(self, node="root"):
        if node == "root":
            node = self.root
        if node is None:
            return
        self.traverse(node.left)
        print(node.key)
        self.traverse(node.right)

    def traverse_2(self, l_asc, node="root"):
        if node == "root":
            node = self.root
        if node is None:
            return
        self.traverse_2(l_asc, node.left)
        l_asc.append(node.key)
        self.traverse_2(l_asc, node.right)


    # traverse_3 doesn't work because output = [] is passed into self.traverse_3 before anything is added
    # not output = True if output = [], so it keeps output as empty list the entire time
    def traverse_3(self, output=None, node="root"):
        if not output:
            output = []
        if node == "root":
            node = self.root
        if not node:
            return
        self.traverse_3(output, node.left)
        output.append(node.key)
        self.traverse_3(output, node.right)
        return(output)

    def traverse_4(self, output=None, node="root"):
        if output is None:
            output = []
        if node == "root":
            node = self.root
        if not node:
            return
        self.traverse_4(output, node.left)
        output.append(node.key)
        self.traverse_4(output, node.right)
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
