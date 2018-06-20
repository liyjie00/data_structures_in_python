class Node(object):
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def insert(self, data):
        if self.data == data:
            return False
        elif self.data > data:
            if self.leftChild:
                return self.leftChild.insert(data)
            else:
                self.leftChild = Node(data)
                return True
        else:
            if self.rightChild:
                return self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)
                return True

    def inorder(self):
        if self:
            if self.leftChild:
                self.leftChild.inorder()
            print(self.data, end=' ')
            if self.rightChild:
                self.rightChild.inorder()

    def preorder(self):
        if self:
            print(self.data, end=' ')
            if self.leftChild:
                self.leftChild.preorder()
            if self.rightChild:
                self.rightChild.preorder()

    def postorder(self):
        if self:
            if self.leftChild:
                self.leftChild.preorder()
            if self.rightChild:
                self.rightChild.preorder()
            print(self.data, end=' ')


class Tree(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True

    def inorder(self):
        print('Inorder:')
        return self.root.inorder()

    def preorder(self):
        print('Preorder:')
        return self.root.preorder()

    def postorder(self):
        print('Postorder:')
        return self.root.postorder()


if __name__ == '__main__':
    bst = Tree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(4)
    bst.insert(6)
    bst.insert(1)
    bst.inorder()
    print('')
    bst.preorder()
    print('')
    bst.postorder()