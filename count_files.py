#!/usr/bin/python
import os
import sys

def get_files(d):
	content=[]
	for path,sub,files in os.walk(d):
		content.extend(files)
	if content:
		count(content)
			
def count(files):
	print("number of files in this directory:")
	print(len(files))


if __name__=='__main__': 
	get_files(os.path.expanduser(sys.argv[1]))
	
