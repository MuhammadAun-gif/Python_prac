import threading 

event = threading.Event()

def myfuction():
    print("Waiting for the event to trigger....")
    event.wait()
    for i in range(10):
        print (i)
    
    print("Performing XYZ action since event was triggered !")

t1 = threading.Thread(target=myfuction)
t1.start()
t1.join()

x = input("Do you want to trigger the event? (y/n)\n")
if x == "y":
    event.set()