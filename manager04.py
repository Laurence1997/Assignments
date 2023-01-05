from flask import Flask,request
from queue import Queue
import os
import pickle
class Queue:

    def __init__(self):
        self.queue = list()

    def add(self, item):
        if item not in self.queue:
            self.queue.insert(0, item)
            return True
        return False

    def empty(self):
        if not self.queue:
            return True
        return False

    def get(self):
        return self.queue.pop()


app = Flask(__name__)

@app.route(rule="/create",methods=["POST","PUT","GET"])
def create():
    directory = request.args.get("directory")
    fileName = request.args.get("fileName")
    context = request.args.get("context")
    queue_obj = Queue()
    queue_obj.add(context)

    with open("{0}/{1}.obj".format(directory , fileName), "wb+") as f:
        pickle.dump(queue_obj, f)
    return "create file successfully"

@app.route(rule="/read",methods=["get"])
def read():
    directory = request.args.get("directory")
    fileName = request.args.get("fileName")

    with open("{0}/{1}.obj".format(directory , fileName), "rb") as f:
        queue_obj: Queue = pickle.load(f)
        while not queue_obj.empty():
            return queue_obj.get()

@app.route(rule="/update",methods=["PATCH","PUT","POST","GET"])
def update():
    directory = request.args.get("directory")
    fileName = request.args.get("fileName")
    context = request.args.get("context")

    queue_obj = Queue()
    queue_obj.add(context)
    with open("{0}/{1}.obj".format(directory, fileName), "wb+") as f:
        pickle.dump(queue_obj, f)
    return "modify successfully"

@app.route(rule="/delete",methods=["DELETE","GET"])
def delete():
    directory = request.args.get("directory")
    fileName = request.args.get("fileName")
    os.remove("{0}/{1}.obj".format(directory , fileName))
    return "deleted successfully"

if __name__ =='__main__':
    #app.run(debug=True,host="0.0.0.0",port=8999)
    app.run(debug=True)