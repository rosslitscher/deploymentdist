#!/usr/bin/env python

'''
Created on Jan 14, 2016

@author: newrelic
'''
import logging
import time
import argparse
import json



from newrelic import deployer, nrcomm, getConfig



pid = "/tmp/nrproc.pid"

def main():
       
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--revision","-r", dest="revision", help="set the revision (optional)")
    parser.add_argument("--changelog","-c", dest="changelog", help="set the changelog (optional)")
    parser.add_argument("--description","-d", dest="description", help="set the revision (optional)")
    parser.add_argument("--user","-u", dest="user", help="set the revision (optional)")
    parser.add_argument("--appid","-a", dest="appid", help="id number of the application")
    

    args = parser.parse_args()
    
    
    config = {}
    config = getConfig.parseConfig("nrDeployConfig.conf")
    logging.basicConfig(filename='nrproc.log', level=logging.INFO)
    systemLog = logging.getLogger("NewRelic")
    logging.info("Start")

    response = deployer.setdeploy(args.revision,args.changelog,args.description,args.user)
         

#    print response

    NRUrl = config['nrurl'] + '/' + args.appid + "/deployments.json"

#    print(NRUrl)

    response = nrcomm.nrPost(response, NRUrl, config['nrapikey'],systemLog,config)
#    print(response)
    logging.info("NR_Response" + response)   
    

    

main()