class Linkedlist(object):
    def __init__(self):
        self.head = None
        self.size = 0

    def __str__(self):
        s = ""
        currentNode = self.head
        while currentNode is not None:
            s = s + str(currentNode.data)
            currentNode = currentNode.next
            if currentNode is not None:
                s += " -> "
        return s

    def insertHead(self, data):
        self.size += 1
        newNode = Node(data)
        if not self.head:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def insertEnd(self, data):
        self.size += 1
        newNode = Node(data)
        if not self.head:
            self.head = newNode
            return
        currentNode = self.head
        while currentNode.next is not None:
            currentNode = currentNode.next
        currentNode.next = newNode

    def removeHead(self):
        self.head = self.head.next

    def remove(self, data):
        preNode = None
        currentNode = self.head
        while currentNode is not None:
            if currentNode.data == data:
                break

            elif currentNode.next is None:
                print('can not find the node')
                return
            else:
                preNode = currentNode
                currentNode = currentNode.next
        if preNode is None:
            self.removeHead()
        else:
            preNode.next = currentNode.next

    def getHead(self):
        print(self.head)

    def getSize(self):
        return self.size


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return self.data


if __name__ == '__main__':
    ll = Linkedlist()

    # ll.insertHead(1)
    # ll.insertHead(2)
    # ll.insertHead(231)

    ll.insertEnd(111)
    ll.insertEnd(222)
    ll.insertEnd(333)
    print(ll)
    print('-' * 30)
    # ll.getHead()
    # ll.removeHead()
    # ll.remove(222)
    ll.remove(111)
    print(ll)
