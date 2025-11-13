from collections import deque

my_queue = deque()

my_queue.append(2)

my_queue.append(3)
my_queue.append(1)


print(my_queue)


my_queue.popleft() #pop elemnet from left


print(my_queue)

my_queue.pop() # pop elemnet from right

print(my_queue)