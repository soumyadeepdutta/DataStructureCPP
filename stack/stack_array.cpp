/*
Stack is a Linear data structure 
order: LIFO
properties: top, isEmpty
operations: push, pop
*/

#include <iostream>
using namespace std;

// maximum capacity of stack
#define MAX 10

// stack array implementation
class Stack
{
    // private
    int top;
    int arr[MAX];

public:
    Stack()
    {
        top = -1;
    }
    bool isEmpty();
    void push(int x);
    int pop();
    void print();
};

bool Stack::isEmpty()
{
    return (top < 0);
}

void Stack::print()
{
    if (isEmpty())
    {
        cout << "Empty stack \n";
    }
    else
    {
        for (int i = 0; i <= top; i++)
            cout << arr[i] << " ";
        cout << endl;
    }
}

void Stack::push(int x)
{
    if (top >= MAX - 1)
        cout << "Overflow";
    else
    {
        arr[++top] = x;
        cout << "Pushed " << x << endl;
    }
}

int Stack::pop()
{
    if (isEmpty())
    {
        cout << "Underflow \n";
        return 0;
    }
    else
    {
        int x = arr[top--];
        return x;
    }
}

int main(void)
{
    Stack s;
    cout << s.isEmpty() << endl;
    s.print();
    s.pop();
    s.push(5);
    cout << s.pop() << endl;
    s.print();
    return 0;
}
