from flask import Flask
from flask import send_file
from flask_basicauth import BasicAuth

app = Flask(__name__)

basic_auth = BasicAuth(app)
app.config['BASIC_AUTH_USERNAME'] = 'api'
app.config['BASIC_AUTH_PASSWORD'] = 'jonel'



@app.route('/download/<string:device_name>')
@basic_auth.required
def downloadFile(device_name):
    path = "data/{}.txt".format(device_name)
    return send_file(path, as_attachment=True)


if __name__ == '__main__':
    app.run(port=5000,debug=True)