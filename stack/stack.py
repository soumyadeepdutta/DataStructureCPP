MAX = 10


class Stack:
    __top = None
    __arr = None

    def __init__(self):
        self.__top = -1
        self.__arr = [None] * MAX

    @property
    def is_empty(self):
        return self.__top < 0

    def push(self, x):
        if self.__top >= MAX - 1:
            print('Overflow')
        else:
            self.__top += 1
            self.__arr[self.__top] = x
            print('Pushed ', x, ' Top ', self.__top)

    def pop(self):
        if self.is_empty:
            print('Underflow')
            return
        else:
            print('Pop ', self.__arr[self.__top], 'Top ', self.__top)
            self.__arr[self.__top] = None
            self.__top -= 1

    def traverse(self):
        if self.is_empty:
            print('Empty')
        else:
            for item in range(self.__top + 1):
                print(self.__arr[item], end=' ')

    def size(self):
        print(self.__top + 1)


if __name__ == '__main__':
    S = Stack()
    print(S.is_empty)
    for i in range(11):
        S.push(i)
    S.size()
    for i in range(10):
        S.pop()
    S.traverse()
    S.size()

