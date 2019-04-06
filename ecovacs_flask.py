#!/usr/bin/python3
#
# 4/2019 - https://github.com/bdwilson/ecovacs-api
#
# sudo apt-get install python3 python3-pip 
# sudo pip3 install sucks 
# sudo pip3 install flask
#
# Set your email, password, country and continent below.
# If you have more than one device on your account, you'll need to 
# determine which device you want to control. Replace 0 with 1 if 
# want to control your 2nd device.
# 
# Usage: /api/[clean|charge|edge|spot|stop|playsound]/0
# 
# If someone can figure out how to get the status of the device,
# that would be good to be able to see what the status is of 
# your device. 
# 
from flask import Flask, render_template, flash, request
from sucks import *

# App config.
DEBUG = False
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '32624076087108375603827608276'

valid_commands = ["clean", "charge", "edge", "spot", "stop", "playsound"]

config = {
    "device_id": EcoVacsAPI.md5(str(time.time())), # value taken from the sucks source
    "email": "your@email.com", # fill in your email
    "password_hash": EcoVacsAPI.md5("MySecureP4ssw0rd"), # fill in your password
    "country": "us", # your ecovacs country e.g. at
    "continent": "na" # your continent e.g. eu
}

def sendCommand(device,command):
	#if (valid_commands[command]):
	if command in str(valid_commands):
		api = EcoVacsAPI(config['device_id'], config['email'], config['password_hash'], config['country'], config['continent'])
		my_vac = api.devices()[device]
		vacbot = VacBot(api.uid, api.REALM, api.resource, api.user_access_token, my_vac, config['continent'])
		vacbot.xmpp.connect_and_wait_until_ready()
		time.sleep(0.5)
		if (command == "clean"):
			vacbot.run(Clean())
		if (command == "charge"):
			vacbot.run(Charge())
		if (command == "edge"):
			vacbot.run(Edge())
		if (command == "spot"):
			vacbot.run(Spot())
		if (command == "stop"):
			vacbot.run(Stop())
		if (command == "playsound"):
			vacbot.run(PlaySound())
		vacbot.xmpp.disconnect()
		return(command, " executed")
		#return(command)

@app.route("/", methods=['GET'])
def info():
	return("/api/[clean|charge|edge|spot|stop|playsound]/[device]")

@app.route("/api/<string:command>/<int:device>", methods=['GET'])
def api(command,device=0):
	val = sendCommand(device,command)
	if val:
		return(val)
 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5050, debug=False)


