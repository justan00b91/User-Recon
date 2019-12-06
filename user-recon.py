import requests
import re
from bs4 import BeautifulSoup

print (" _   _                    ____                       ")
print ("| | | |___  ___ _ __     |  _ \ ___  ___ ___  _ __   ")
print ("| | | / __|/ _ \ '__|____| |_) / _ \/ __/ _ \| '_ \  ")
print ("| |_| \__ \  __/ | |_____|  _ <  __/ (_| (_) | | | | ")
print (" \___/|___/\___|_|       |_| \_\___|\___\___/|_| |_| ")
print ()

user = str(input("USERNAME : "))
print ()

def main():
	if chkfb() != None:
		print ("[+]FaceBook Account Exists.")
	if chktwitter() != None:
		print ("[+]Twitter Account Exists.")
	if chkgit() != None:
		print ("[+]Githb Account Exists. ")
	else:
		print ("Username %s not found on Facebook,Twitter And Github"%(user))

def chkfb():
	link1 = "https://facebook.com/" + (user)
	resp1 = requests.get(link1)
	status = BeautifulSoup(resp1.text, 'html.parser')
	if resp1.status_code == 200:
		return True
	else:
		return None

def chktwitter():
	link2 = "https://twitter.com/" + (user)
	resp2 = requests.get(link2)
	status = BeautifulSoup(resp2.text, 'html.parser')
	if resp2.status_code == 200:
		return True
	else:
		return None

def chkgit():
	link3 = "https://github.com/" + (user)
	resp3 = requests.get(link3)
	status = BeautifulSoup(resp3.text, 'html.parser')
	if resp3.status_code == 200:
		return True
	else:
		return None 

main()
