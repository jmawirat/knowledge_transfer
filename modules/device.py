class Device:
	def get(self):
		device = {
			"DEVICE1" : {
				"ip" : "192.168.1.1",
				"device_type" : "ios_xe" 
			},
			"DEVICE2" : {
				"ip" : "192.168.2.1",
				"device_type" : "ios_xe" 
			}
		}
		return device