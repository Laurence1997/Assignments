from flask import Flask,request
import os

app = Flask(__name__)

#create /logtextfile

@app.route(rule="/create",methods=["POST","PUT","GET"])
def create():
    directory = request.args.get("directory")
    fileName = request.args.get("fileName")
    context = request.args.get("context")
    with open("{0}/{1}.txt".format(directory , fileName), "w") as f:
        f.write(context)

    return "create txtfile successfully"

@app.route(rule="/read",methods=["get"])
def read():
    directory = request.args.get("directory")
    fileName = request.args.get("fileName")
    with open("{0}/{1}.txt".format(directory , fileName), "r") as f:
        context = f.read()
    return "The txtfile content is："+context

@app.route(rule="/update",methods=["PATCH","PUT","POST","GET"])
def update():
    directory = request.args.get("directory")
    fileName = request.args.get("fileName")
    context = request.args.get("context")
    with open("{0}/{1}.txt".format(directory , fileName), "w") as f:
        f.write(context)
    return "modify successfully"

@app.route(rule="/delete",methods=["DELETE","GET"])
def delete():
    directory = request.args.get("directory")
    fileName = request.args.get("fileName")
    os.remove("{0}/{1}.txt".format(directory , fileName))
    return "deleted successfully"

if __name__ =='__main__':
    #app.run(debug=True,host="0.0.0.0",port=8999)
    app.run(debug=True)