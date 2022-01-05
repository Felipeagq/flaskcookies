from flask import Flask, json, jsonify, make_response,request

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({"msg":"ok",
    "data":"index route"})


@app.route("/cookie/set/<string:cookie_key>/<string:cookie_value>")
def cookie_set(cookie_key,cookie_value):
    response = make_response("Cookie have been set")
    response.set_cookie(cookie_key,cookie_value)
    return response


@app.route("/cookie/get/<string:cookie>")
def cookie_get(cookie):
    cookie_value = request.cookies.get(cookie,None)
    if cookie_value:
        return jsonify({"msg":"ok",
        "data":[{cookie:cookie_value}]})
    return jsonify({"msg":"ok",
    "data":[{"cookie":"NOT FOUND"}]})

if __name__ == "__main__":
    app.run(debug=True)