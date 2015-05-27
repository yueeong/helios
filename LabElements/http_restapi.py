__author__ = 'yueeong'

import requests
import json
import logging

from .http import HTTP

class HTTP_restapi(HTTP):
    CONNTIMEOUT = 4

    def __init__(self,systemname,config):

        self.config = config
        self.systemname = systemname

        self.host = config[systemname]['host']
        self.port = config[systemname]['port']
        self.server = 'http://' + self.host + ':' + self.port




    def getHTTP(self, path):
        url = self.server + path

        response = requests.get(url)

        return response

    def postHTTP(self,path,payload):
        #payload is some dict
        url = self.server + path

        response = requests.post(url,data=json.dumps(payload))

        return response





