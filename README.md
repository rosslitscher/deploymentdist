This application will send an application deployment discriptor 

# NRCONFIG
NRURL: https://api.newrelic.com/v2/applications is default and should not to be changed

NRAPIKEY: * ~~~~~~~~~~~~~~~~~ * is the API key found in account settings API key.  You must have Admin access to see key.

LOGFILE: nrproc.log name of logfile


HOSTNAME:  (optional) Hostname is pick up from OS but this will override that action

PROXYSERVER: Name or IP of proxy server

PROXYPORT: Port for Proxy Server

PROXYUSER: username of User for proxy

PROXYPASS: Password for Proxy

# Install Directions
Install is simple unzip in directory execute nrdeploy.py.  


It does require urllib2

# Run It

nrdeploy.py --revision xxxxx --user xxxxxxx --changelog xxxxxxxxx --description xxxxxxx --appid 32113231





