## FIFO
# import queue as qu
# 
# q = qu.Queue()
# 
# numbers = [10,20,30,40,50,60,70]
# 
# for number in numbers:
#     q.put(number)
# 
# while not q.empty():
#     print(q.get())

## LIFO
#import queue as qu
#
#q = qu.LifoQueue()
#
#numbers = [10,20,30,40,50,60,70]
#
#for number in numbers:
#    q.put(number)
#
#while not q.empty():
#    print(q.get())

## Priority Queues
# Passed as tuples
import queue as qu

q = qu.PriorityQueue()

numbers = [10,20,30,40,50,60,70]

i = 0

for number in numbers:
    q.put((i, number))
    i += 1

while not q.empty():
    print(q.get()[1])