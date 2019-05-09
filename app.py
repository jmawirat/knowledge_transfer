import web
from flask import Flask,jsonify,request


app = Flask(__name__)


@app.route('/public/api/v1.0/web/healthcheck/<string:url>')
def public_http(url):
    #try:
    health = Web("http://{}".format(url))
    return jsonify(health.performance("null"),200)
    #except:
    #    return jsonify({"Status":"Execution Error"},401)


@app.route('/ping')
def health():
        return jsonify({"Status":"Success"},200)


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="3000")
