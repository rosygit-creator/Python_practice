# implement stack using queue
# idea is to use 1 queue and push and pop elemnet from front of queue

from collections import deque

class stack_using_queue:
    def __init__(self):
        self.q = deque()

    def push(self,y):
        self.q.append(y) # add element on right , LIFO

    def pop_element(self):
        self.q.pop() # pop from right



        # return top element
    def return_top_element(self):

        l=self.q.maxlen()
        self.q[l]

    def return_q(self):
        return self.q


if __name__ == '__main__':
    st = stack_using_queue()
    st.push(1)
    st.push(2)
    st.push(3)
    print(st.pop_element())
    print(st.return_top_element())
    print(st.return_q())






