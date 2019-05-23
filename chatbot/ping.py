import pyping

class Ping:
    def __init__(self,url):

        try:
            r = pyping.ping(url)

            if r.ret_code == 0:
                self.data = {
                    "SOURCE" : "172.23.85.60",
                    "URL" : url,
                    "ret_code" : r.ret_code,
                    "destination" : r.destination,
                    "max_rtt" : float(r.max_rtt),
                    "avg_rtt" : float(r.avg_rtt),
                    "min_rtt" : float(r.min_rtt),
                    "destination_ip" : r.destination_ip
                }
            else:
                self.data = {
                    "SOURCE" : "172.23.85.60",
                    "URL" : url,
                    "ret_code" : r.ret_code,
                    "destination" : r.destination,
                    "max_rtt" : float(-1),
                    "avg_rtt" : float(-1),
                    "min_rtt" : float(-1),
                    "destination_ip" : r.destination_ip
                }
        except:
            self.data = False

    def performance(self):
        return self.data
