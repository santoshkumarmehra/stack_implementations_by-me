# 1 method with module
import collections
stack1 = collections.deque()
# print(stack1)
stack1.append(10)
stack1.append(20)
stack1.append(10)
# print(stack1)
stack1.pop()
stack1.pop()
stack1.pop()
# print(stack1)

# 2 method with module

import queue

stack3 = queue.LifoQueue(3)
stack3.put(10)
stack3.put(20)
stack3.put(30)
# stack3.put(40, timeout=1)
# print(stack3)
# for i in stack3:
#     print(i)
stack3.get()
stack3.get()
stack3.get()
stack3.get(timeout=1)
# print(stack3)