#ifndef MYVECTOR_H
#define MYVECTOR_H

class MyVector { 
    private:
        int* data;
        int capacity;
        int length;

    public:
        MyVector();
        ~MyVector();

        void push_back(int value);
        void pop_back();
        int size() const;

        int& operator[](int index);
};


#endif