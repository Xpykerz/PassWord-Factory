#!/usr/bin/python

import itertools

print " ____             __        __            _   _____          _                   "
print "|  _ \ __ _ ___ __\ \      / /__  _ __ __| | |  ___|_ _  ___| |_ ___  _ __ _   _ "
print "| |_) / _` / __/ __\ \ /\ / / _ \| '__/ _` | | |_ / _` |/ __| __/ _ \| '__| | | |"
print "|  __/ (_| \__ \__  \ V  V / (_) | | | (_| | |  _| (_| | (__| || (_) | |  | |_| |"
print "|_|   \__,_|___/___/ \_/\_/ \___/|_|  \__,_| |_|  \__,_|\___|\__\___/|_|   \__, |"
print "                                                                           |___/ "
print "                                                      https://github.com/Xpykerz "
print "                                                      Ask: https://t.me/MQ_XZ"
print "\n"

char=raw_input('Enter charachters used for password : ')
passlen=input('Enter length of password : ')

res=itertools.product(char,repeat=passlen) 

with open('password.txt', 'a') as file:
	for i in res:
		wlist=''.join(i)
		file.write(wlist)
		file.write('\n')
		print wlist