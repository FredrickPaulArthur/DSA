class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, newNode):
        newNode = Node(newNode)

        if self.root is None:
            self.root = newNode

        else:
            currNode = self.root
            while currNode is not None:
                if newNode.val <= currNode.val:
                    if currNode.left is None:
                        currNode.left = newNode
                        return
                    currNode = currNode.left

                else:
                    if currNode.right is None:
                        currNode.right = newNode
                        return
                    currNode = currNode.right

    # Binary Search is carried out
    def search(self, findNode):
        findNode = Node(findNode)
        currNode = self.root

        while currNode is not None:
            if findNode.val < currNode.val:
                currNode = currNode.left

            elif findNode.val > currNode.val:
                currNode = currNode.right

            else:
                print("NODE {} IS PRESENT".format(findNode.val))
                return
        else:
            print("NODE {} NOT PRESENT".format(findNode.val))

    def delete(self, rootNode, key):
    # rootNode is returned in this function
    # By returning the rootNode at each step, the structure of the binary search tree is maintained during the deletion process.
    # It ensures that the parent nodes in the path of the deleted node are correctly linked to the modified subtrees after the deletion.
        if rootNode is None:
            return None

        if key < rootNode.val:
            rootNode.left = self.delete(rootNode.left, key)
            return rootNode  # Returns value for

        elif key > rootNode.val:
            rootNode.right = self.delete(rootNode.right, key)
            return rootNode

        else:
            # rootNode is the key to be deleted
            if rootNode.left is None and rootNode.right is None:
                return None

            elif rootNode.left is None:
                temp = rootNode.right
                rootNode = None
                return temp
                # rootNode.right

            elif rootNode.right is None:
                temp = rootNode.left
                rootNode = None
                return temp
                # rootNode.left

            # Both left and right is not None, THERE IS A SUBTREE UNDER THE NODE
            # selecting the smallest element of the right subtree.
            else:
                succParent = rootNode
                succ = rootNode.right
                # until "succ" becomes the least value
                while succ.left is not None:
                    succParent = succ
                    succ = succ.left

                # Delete successor.Since successor is always left child of its parent we can safely make successor's right
                # right child as left of its parent. If there is no succ, then assign succ->right to succParent->right
                if succParent is not rootNode:
                    succParent.left = succ.right    # None
                # this else-statement is executed only when the node(succParent) has only one leaf or no leaf
                else:
                    succParent.right = succ.right
                    # Executed for one level under the rootNode

                rootNode.val = succ.val
                return rootNode

    def minValue(self):
        currNode = self.root
        while currNode.left is not None:
            currNode = currNode.left
        else:
            return currNode.val

    def maxValue(self):
        currNode = self.root
        while currNode.right is not None:
            currNode = currNode.right
        else:
            return currNode.val

    def height(self, node):
        if node is None:
            return 0
        lheight = self.height(node.left)
        rheight = self.height(node.right)

        return max(lheight, rheight) + 1

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


bst = BST()
l = [15, 10, 8, 12, 11, 13, 20, 16, 25]

for i in l:
    bst.insert(i)

print(bst.height(bst.root.right))

bst.levelorder()
print()
print(bst.root.val)
bst.inorder(bst.root)
print()
bst.preorder(bst.root)
print()
bst.postorder(bst.root)
print()

bst.search(8)

print("\nPerforming deletion:")
print(bst.delete(bst.root, 20).val)
print(bst.delete(bst.root, 15).val)

bst.levelorder()