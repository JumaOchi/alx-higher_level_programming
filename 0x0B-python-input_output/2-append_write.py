#!/usr/bin/python3


'''Function to append text to a file'''

def append_write(filename="", text=""):
with open('filename', encoding="utf-8") as f:
	return f.write(str(text))
