#!/usr/bin/python
import socket,sys,requests

print "\n| <------------------------------> |"
print "| <-----Web Directory Buster-----> |"
print "| <------------------------------> |\n"
if len(sys.argv) <= 2:
	print "Sintax: python Directory_Buster.py http://example.com/ wordlist.txt\n" 

else:
	
	with open(sys.argv[2]) as file:
		for line in file:
			for word in line.split():
				response = requests.get(sys.argv[1] + word)
				status = response.status_code
				if (status == 200):
					print (sys.argv[1]+ word +"--->VALID PATH")
