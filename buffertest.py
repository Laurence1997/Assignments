import pickle
class Queue:

    def __init__(self):
        self.queue = list()

    def add(self, item):
        if item not in self.queue:
            self.queue.insert(0, item)
            return True
        return False

# edit your queue & add elements as you wish
my_queue = Queue()
my_queue.add(2)
my_queue.add(3)

# save
with open("my_saved_queue.obj","wb+") as myqueue_save_file:
    pickle.dump(my_queue, myqueue_save_file)

print(f"> saved queue: {my_queue.queue}")

# load
with open("my_saved_queue.obj","rb") as myqueue_save_file:
    my_loaded_queue: Queue = pickle.load(myqueue_save_file)

print(f"> loaded queue: {my_loaded_queue.queue}")