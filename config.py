#!/usr/bin/python3
import os
home = os.environ['HOME']
config_file = open(home + '/.config/anonupload', 'w')
print("Hi! I will ask you some questions, read carefully!")
print("What server do you want to use? [anonfile, megaupload, bayfiles, none]")
server = input()
if(server not in ('anonfile', 'megaupload', 'bayfiles')):
	print("I dont know what you typed, using anonfile.")
	server = 'anonfile'

print("Please enter your API key for this server, or if you dont have one, press enter:")
api = input()
if(api == ''):
	api = None

print("Okay, now please enter your public GPG key name (it's case sensitive!), or if you don't have one, press enter")
gpg = input()
if(gpg == ''):
	gpg = None

#print("Cool, do you want to save links to file so later you can download them fast? (y/n)")
#files = input()
#if(files == 'y'):
#	files = True
#else:
#	files = False

print("Fine, now i will write new config...")
config_file.write('SERVER:' + server + '\n')
if(api != None):
	config_file.write('API:' + api + '\n')
if(gpg != None):
	config_file.write('GPG:' + gpg + '\n')

#if(files != False):
#	config_file.write('FILES_LIST:true\n')

print("Done everything! Have a nice day :)")
