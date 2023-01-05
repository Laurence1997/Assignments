from flask import Flask,request
import os
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
    print(directory)
    os.mkdir(directory)
    return "create directory successfully"

@app.route(rule="/read",methods=["get"])
def read():
    directory = request.args.get("directory")
    return "directory is："+directory

@app.route(rule="/update",methods=["PATCH","PUT","POST","GET"])
def update():
    directory = request.args.get("directory")
    newDirectory = request.args.get("newDirectory")
    os.rename(directory,newDirectory)
    return "modify directory successfully"

@app.route(rule="/delete",methods=["DELETE","GET"])
def delete():
    directory = request.args.get("directory")
    os.rmdir(directory)
    return "deleted directory successfully"

if __name__ =='__main__':
    #app.run(debug=True,host="0.0.0.0",port=8999)
    app.run(debug=True)