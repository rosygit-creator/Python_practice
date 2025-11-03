from queue import Queue

def queue1(l1):
    q=Queue()
    print(f" len is {len(l1)}")
    for e in l1:
        q.put(e)
    while q.empty()==False:
        print(q.get())



    return



a=[2,3,4]
queue1(a)