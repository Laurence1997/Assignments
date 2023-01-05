from flask import Flask,request
import os
import shelve

app = Flask(__name__)
#/binaryfile

@app.route(rule="/create",methods=["POST","PUT","GET"])
def create():
    lisi = {'age':10,'sex':'Male'}
    directory = request.args.get("directory")
    with shelve.open('shelve.dat') as fb:
        fb['demo']=lisi
        print(fb['demo'])
    return "create file successfully"

@app.route(rule="/read",methods=["get"])
def read():
    directory = request.args.get("directory")
    with shelve.open('shelve.dat') as fb:
        print(fb['demo'])
        text = fb['demo']
    return text

@app.route(rule="/update",methods=["PATCH","PUT","POST","GET"])
def update():
    zhangsan = {'age': 20, 'sex': 'Male'}
    directory = request.args.get("directory")
    with shelve.open('shelve.dat') as fb:
        fb['demo']=zhangsan
    return "modify successfully"

@app.route(rule="/delete",methods=["DELETE","GET"])
def delete():
    directory = request.args.get("directory")
    os.remove('shelve.dat.dat')
    return "deleted successfully"

if __name__ =='__main__':
    #app.run(debug=True,host="0.0.0.0",port=8999)
    app.run(debug=True)