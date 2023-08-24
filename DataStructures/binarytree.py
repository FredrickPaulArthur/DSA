class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None
        # self.latestNode = None

    # Only insert at the first position available in the Level Order
    def insert(self, node, key):
        if self.root is None:
            self.root = Node(key)

        else:
            queue = []
            queue.append(self.root)
            while len(queue) > 0:
                node = queue.pop(0)
                if node.left is not None:
                    queue.append(node.left)
                else:
                    node.left = Node(key)
                    return
                if node.right is not None:
                    queue.append(node.right)
                else:
                    node.right = Node(key)
                    return

    def search(self, node, key):
        if self.root is None:
            return

        else:
            if node is None:
                # print('node is None')
                return
            if node.val == key:
                print("Node with value {} is present".format(key))
                return node
            else:
                self.search(node.left, key)
                self.search(node.right, key)

    # The node is deleted and replaced by the latest added value
    def delete(self, key):  # Not fully working
        if self.root is None:
            return
        else:
            queue = []
            queue.append(self.root)
            del_node = None
            while len(queue) > 0:
                last_node = queue.pop(0)
                if last_node.val == key:
                    del_node = last_node
                if last_node.left is not None:
                    queue.append(last_node.left)
                if last_node.right is not None:
                    queue.append(last_node.right)
            # When the while loop exits, last_node will be the last and rightmost node of the tree
            # Now the tree is traversed to find the key

            del_node.val = last_node.val
            last_node = None  # To delete the last node from the tree

    def levelorder(self):
        if self.root is None:
            return
        queue = []
        queue.append(self.root)
        while len(queue) > 0:
            node = queue.pop(0)
            print(node.val, end="\t")
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        print()
        # print(list(v.val for v in queue))

    def inorder(self, node):
        if node is None:
            return
        self.inorder(node.left)
        print(node.val, end="\t")
        self.inorder(node.right)

    def preorder(self, node):
        if node is None:
            return
        print(node.val, end="\t")
        self.preorder(node.left)
        self.preorder(node.right)

    def postorder(self, node):
        if node is None:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.val, end="\t")

    def height(self, node):
        if self.root is None:
            return
        if node is None:
            return 0
        lheight = self.maxHeight(node.left)
        rheight = self.maxHeight(node.right)
        return max(lheight, rheight) + 1


# Driver's Code
btree = BinaryTree()
l = ["A", "B", "C", "D", "E", "F", "G", "H"]

for i in l:
    btree.insert(btree.root, i)


print(btree.root.val)

btree.search(btree.root, "D")
btree.search(btree.root, "J")  # Doesnt print that J is not present

btree.levelorder()


btree.delete("F")

print("After deletion of F:")
btree.levelorder()
