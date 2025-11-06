import threading as td

#def helloworld():
#    print("hello world")

#t1 = threading.Thread(target=helloworld)
#t1.start()

def function1():
    for i in range(500):
        print("ONE")

def function2():
    for i in range(500):
        print("TWO")

t1 = td.Thread(target=function1)
t2 = td.Thread(target=function2)

t1.start()
t2.start()

# Waiting for Threads to Finish
# If for someone reason i want thread1 to finish then print thread2
# I use t1.join() [Do not confuse with String function .join(), both are different)
# Example:
# import threading
# def hello(:
#   for x in range(50):
#        print("Hello")
#
# t1 = threading.Thread(target=hello)
# t1.start()
# t1.join()
# print("Another text")     #### Waits for the thread to finish to print this,
#                           #### otherwise, it immediately prints "Another text",
#                           #### and then the thread
