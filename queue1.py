# Queue implementation using List
# Here we are going to define a class Queue and add methods to perform the below operations:
#
# Enqueue elements to the beginning of the Queue and issue a warning if it's full
# Dequeue elements from the end of the Queue and issue a warning if it’s empty
# Assess the size of the Queue
# Print all the elements of the Queue

class Queue:

    def __init__(self):
        self.queue = list()

    def enqueue(self,data):
        if data not in self.queue:
            self.queue.insert(0,data)
            return True
        return False

    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.pop()
        return ("Empty queue")

    def size(self):
        return len(self.queue)

myQueue = Queue()
print(myQueue.enqueue(5))  # prints True
print(myQueue.enqueue(6))  # prints True
print(myQueue.enqueue(9))  # prints True
print(myQueue.enqueue(5))  # prints False
print(myQueue.enqueue(3))  # prints True
print(myQueue.size())  # prints 4
print(myQueue.dequeue())  # prints 5
print(myQueue.dequeue())  # prints 6
print(myQueue.dequeue())  # prints 9
print(myQueue.dequeue())  # prints 3
print(myQueue.size())  # prints 0
print(myQueue.dequeue())  # prints Queue Empty!

