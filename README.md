# Ecovacs Robotic Vacuum API
This flask API uses the [sucks](https://github.com/wpietri/sucks) python
library and is loosely based off of [ecovacs-aws](https://github.com/bamminger/ecovacs-aws). 

If you're into MQTT, you might want to use [openhab-sucks](https://github.com/guillebot/openhab-sucks) instead.

I am not a Python programmer; this is really bad code. Please fix it. There is
no authentication because the expectation is that you're running this on your
internal, trusted home network. You've been warned.

If you know how to get the status information without being able to subscribe to the
events, please fix this. It gets the job done for my needs by starting cleaning
when someone leaves the house via API call from Hubitat, then sends it home
when someone returns. 

# Installation (manual)
1. Install sucks and flask python modules
<pre>
# pip3 install sucks
# pip3 install flask
</pre>
2. Change the login/password/country/continent/service port variables in the ecovacs_flask.py. My port in the example is 5050.
3. Change directory in the .service file to match where your ecovacs_flask.py file is.
4. Copy service file to /lib/systemd/system/ then enable it.
<pre>
# systemctl enable ecovacs-api.service
# systemctl start ecovacs-api.service
</pre>

# Installation (Docker)
1. Grab the
[Dockerfile](https://raw.githubusercontent.com/bdwilson/ecovacs-api/master/Dockerfile)
via wget and put it in a directory on your Docker server. Then run the commands
below from that directory
2. <code> # docker build -t ecovacs-api --build-arg ECOVACS_USER='your@email.address' --build-arg ECOVACS_PASS='your_password' .</code>CTRL-C out of it when it's complete
Optional arguments are ECOVACS_COUNTRY, ECOVACS_CONTINENT, ECOVACS_PORT. These will default to us, na, and 5050. If you're not in the US, you can leave them
then connect in via step 3 and determine the correct variables via <code>sucks login</code>
3. Run your newly created image: <code> # docker run -p 5050:5050 --name ecovacs-api -t ecovacs-api</code>
4. That's it. If you need to troubleshoot your docker image, you can get into
it via:
<code> # docker exec -it ecovacs-api /bin/bash</code> or 
<code># docker run -it ecovacs-api /bin/bash</code> and then poke around and run the commands below in the troubleshooting section "sucks". 

# Usage
<pre>
# curl -s http://yourip:5050/api/clean/0 
# curl -s http://yourip:5050/api/charge/0 
# curl -s http://yourip:5050/api/playsound/0 
</pre>

# Troubleshooting
1. If you have multiple vacuums, you may need to change the number above in the usage to 1, or 2 if you have 3 vacuums on your account. 
2. You should make sure sucks works before configuring this script. 
<pre>
# sucks login
# sucks --debug stop
</pre> 
3. You can always enable debug in the ecovacs_flask.py script and run it from the commandline. 

Bugs/Contact Info
-----------------
Bug me on Twitter at [@brianwilson](http://twitter.com/brianwilson) or email me [here](http://cronological.com/comment.php?ref=bubba).
