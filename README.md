# Ecovacs Robotic Vacuum API
This flask API uses the [sucks](https://github.com/wpietri/sucks) python
library and is loosely based off of [ecovacs-aws](https://github.com/bamminger/ecovacs-aws). 

If you're into MQTT, you might want to use [openhab-sucks](https://github.com/guillebot/openhab-sucks) instead.

I am not a Python programmer; this is really bad code. Please fix it. If you
know how to get the status information without being able to subscribe to the
events, please fix this. It gets the job done for my needs by starting cleaning
when someone leaves the house via API call from Hubitat, then sends it home
when someone returns. 

# Installation
1. Install sucks and flask python modules
<code>
# pip3 install sucks
# pip3 install flask
</code>
2. Change your login/password in the ecovacs_flask.py
3. Change directory in the .service file to match where your ecovacs_flask.py file is.
4. Copy service file to /lib/systemd/system/ then enable it.
<code>
# systemctl enable ecovacs-api.service
# systemctl start ecovacs-api.service
</code>
5. Use it. 
<code>
# curl -s http://yourip:5050/api/clean/0 
# curl -s http://yourip:5050/api/charge/0 
# curl -s http://yourip:5050/api/playsound/0 
</code>

# Troubleshooting
1. If you have multiple vacuums, you may need to change the number to 1, or 2
if you have 3 vacuums on your account. 
2. You should make sure sucks works before configuring this script. 
<code>
# sucks login
# sucks --debug stop
</code> 
3. You can always enable debug in the ecovacs_flask.py script and run it from
the commandline. 

Bugs/Contact Info
-----------------
Bug me on Twitter at [@brianwilson](http://twitter.com/brianwilson) or email me [here](http://cronological.com/comment.php?ref=bubba).
