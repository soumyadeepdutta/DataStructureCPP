class Queue:
    __MAX = 10

    def __init__(self):
        self.__front = self.__rear = 0
        self.__arr = [None] * self.__MAX

    @property
    def is_empty(self):
        return self.__front == self.__rear

    @property
    def __is_full(self):
        return self.__rear == self.__MAX

    def enqueue(self, x):
        if not self.__is_full:
            print('Enqueue ', x)
            self.__arr[self.__rear] = x
            self.__rear += 1
        else:
            print('Full')
            return

    def dequeue(self):
        if not self.is_empty:
            print('Dequeue ', self.__arr[self.__front])
            for index in range(self.__front, self.__rear - 1):
                self.__arr[index] = self.__arr[index + 1]
            self.__rear -= 1
        else:
            print('Empty')
            return

    def traverse(self):
        if not self.is_empty:
            for item in range(self.__front, self.__rear):
                print(self.__arr[item], end=' ')
            print('\n')
        else:
            print('Empty')


if __name__ == '__main__':
    Q = Queue()
    for i in range(12):
        Q.enqueue(i)
    Q.traverse()
    for i in range(5):
        Q.dequeue()
    Q.traverse()
