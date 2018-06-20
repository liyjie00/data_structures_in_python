class Queue(object):
    __slots__ = '__queue'

    def __init__(self):
        self.__queue = []

    def isEmpty(self):
        return len(self.__queue) == 0

    def enqueue(self, value):
        self.__queue.append(value)

    def dequeue(self):
        if self.isEmpty():
            print('The queue is empty.')
        else:
            val = self.__queue[0]
            self.__queue.remove(val)
            return val

    def printQue(self):
        print(self.__queue)


if __name__ == '__main__':
    myQueue = Queue()
    myQueue.isEmpty()
    myQueue.enqueue(11)
    myQueue.enqueue(22)
    myQueue.enqueue(33)
    myQueue.enqueue(44)
    myQueue.enqueue(55)
    myQueue.printQue()
    print('-' * 30)
    myQueue.dequeue()
    myQueue.printQue()