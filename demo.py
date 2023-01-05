from flask import Flask

app = Flask(__name__)

from flask import make_response,jsonify

@app.route(rule="/user",methods=["get","post"])
def user():
    with open("pic.jpg","rb") as f:
        content =f.read()
        response=make_response(content)
        response.headers["Content-Type"]="image/jpeg"
    return response

if __name__ =='__main__':
    #app.run(debug=True,host="0.0.0.0",port=8999)
    app.run(debug=True)