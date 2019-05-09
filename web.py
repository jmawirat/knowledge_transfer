import pycurl
from io import BytesIO
from flask import Flask,jsonify,request

class Web:
    def __init__(self,url):
        buffer = BytesIO()
        c = pycurl.Curl()
        c.setopt(c.URL, url)
        c.setopt(c.WRITEDATA, buffer)
        c.setopt(pycurl.SSL_VERIFYPEER, 0);
        c.perform()

        self.data = {
            "SOURCE" : "172.23.85.60",
            "URL" : url,
            "EFFECTIVE_URL" : c.getinfo(c.EFFECTIVE_URL),
            "HTTP_CODE" : int(c.getinfo(c.HTTP_CODE)),
            "TOTAL_TIME" : float(c.getinfo(c.TOTAL_TIME)),
            "NAMELOOKUP_TIME" : float(c.getinfo(c.NAMELOOKUP_TIME)),
            "CONNECT_TIME" : c.getinfo(c.CONNECT_TIME),
            "PRETRANSFER_TIME" : c.getinfo(c.PRETRANSFER_TIME),
            "REDIRECT_TIME" : c.getinfo(c.REDIRECT_TIME),
            "REDIRECT_COUNT" : c.getinfo(c.REDIRECT_COUNT),
            "SIZE_UPLOAD" : c.getinfo(c.SIZE_UPLOAD),
            "SIZE_DOWNLOAD" : c.getinfo(c.SIZE_DOWNLOAD),
            "SPEED_UPLOAD" : c.getinfo(c.SPEED_UPLOAD),
            "HEADER_SIZE" : c.getinfo(c.HEADER_SIZE),
            "REQUEST_SIZE" : c.getinfo(c.REQUEST_SIZE),
            "CONTENT_LENGTH_DOWNLOAD" : c.getinfo(c.CONTENT_LENGTH_DOWNLOAD),
            "CONTENT_LENGTH_UPLOAD" : c.getinfo(c.CONTENT_LENGTH_UPLOAD),
            "RESPONSE_CODE" : c.getinfo(c.RESPONSE_CODE),
            "SPEED_DOWNLOAD" : c.getinfo(c.SPEED_DOWNLOAD),
            "SSL_VERIFYRESULT" : c.getinfo(c.SSL_VERIFYRESULT),
            "INFO_FILETIME" : c.getinfo(c.INFO_FILETIME),
            "STARTTRANSFER_TIME" : c.getinfo(c.STARTTRANSFER_TIME),
            "REDIRECT_TIME" : c.getinfo(c.REDIRECT_TIME),
            "REDIRECT_COUNT" : c.getinfo(c.REDIRECT_COUNT),
            "HTTP_CONNECTCODE" : c.getinfo(c.HTTP_CONNECTCODE),
            "HTTPAUTH_AVAIL" : c.getinfo(c.HTTPAUTH_AVAIL),
            "PROXYAUTH_AVAIL" : c.getinfo(c.PROXYAUTH_AVAIL),
            "OS_ERRNO" : c.getinfo(c.OS_ERRNO)
        }

        c.close()

    def performance(self):
        return self.data



#from flask import Flask,jsonify,request


app = Flask(__name__)


@app.route('/public/api/v1.0/web/healthcheck/<string:url>')
def public_http(url):
    #try:
    health = Web("http://{}".format(url))
    return jsonify(health.performance(),200)
    #except:
    #    return jsonify({"Status":"Execution Error"},401)


@app.route('/ping')
def health():
        return jsonify({"Status":"Success"},200)


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="3000")
