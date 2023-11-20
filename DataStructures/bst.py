class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def findmin(self):
        currNode = self.root
        while currNode.left is not None:
            currNode = currNode.left
        else:
            return currNode

    def findmax(self):
        currNode = self.root
        while currNode.right is not None:
            currNode = currNode.right
        else:
            return currNode

    def height(self, node):#postorder
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


    def insert(self, newVal):
        newNode = Node(newVal)

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
        if rootNode is None:
            return None

        if key < rootNode.val:
            rootNode.left = self.delete(rootNode.left, key)
            return rootNode

        elif key > rootNode.val:
            rootNode.right = self.delete(rootNode.right, key)
            return rootNode

        else:
            if rootNode.left is None:
                return rootNode.right
            elif rootNode.right is None:
                return rootNode.left
            else:
                succ = rootNode.right
                while succ.left is not None:
                    succ = succ.left
                
                rootNode.val = succ.val
                rootNode.right = self.delete(rootNode.right, succ.val)
                return rootNode
               
                



bst = BST()
l = [15, 10, 8, 12, 11, 13, 20, 16, 25]

for i in l:
    bst.insert(i)

bst.preorder(bst.root)

print("\nPerforming deletion:")
bst.delete(bst.root, 20)
bst.preorder(bst.root)
print()

bst.delete(bst.root, 15)
bst.preorder(bst.root)
print()