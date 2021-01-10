class CircularQueue:
    __MAX = 5

    def __init__(self):
        self.__front = self.__rear = -1
        self.__arr = [None] * self.__MAX

    @property
    def is_empty(self):
        return self.__front == self.__rear == -1

    @property
    def is_full(self):
        return (self.__rear == self.__MAX - 1 and self.__front == 0) or self.__front == self.__rear + 1

    def insert(self, x):
        if self.is_full:
            print('Full')
            return
        elif self.is_empty:
            self.__front = self.__rear = 0
            self.__arr[self.__rear] = x
        elif self.__rear == self.__MAX - 1:
            self.__rear = 0
            self.__arr[self.__rear] = x
        else:
            self.__rear += 1
            self.__arr[self.__rear] = x
        print('Inserted ', x, ' at ', self.__rear)

    def delete(self):
        if self.is_empty:
            print('Empty')
            return
        elif self.__front == self.__MAX - 1:
            print(self.__arr[self.__front])
            self.__front = 0
        elif self.__front == self.__rear:
            print(self.__arr[self.__front])
            self.__rear = self.__front = -1
        else:
            print(self.__arr[self.__front])
            self.__front += 1

    def display(self):
        if self.__front > 0:
            for index in range(self.__front + 1):
                print(self.__arr[index], end=' ')
        for index in range(self.__front, self.__rear + 1):
            print(self.__arr[index], end=' ')


if __name__ == '__main__':
    cQueue = CircularQueue()
    for i in range(5):
        cQueue.insert(i)
    cQueue.display()
    for i in range(3):
        cQueue.delete()
    cQueue.display()
