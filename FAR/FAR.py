# -*- coding: utf-8 -*-
#!/usr/bin/env python

from __future__ import print_function
import os
import shutil

def replace_text(file_path,find_text,replace_text,backup=False):
	if type(file_path)!=str or type(find_text)!=str or type(replace_text)!=str:
		raise Exception("Arguments should be of type String only")
	if type(backup)!=bool:
		raise Exception("backup parameter should be of type Boolean") 

	if not os.path.isfile(file_path):
		raise Exception("No such file found "+file_path)
	open_file = open(file_path,'r')
	all_lines = open_file.readlines()
	edited_lines=[]
	for line in all_lines:
		replace_line=line.replace(find_text,replace_text)
		edited_lines.append(replace_line)
	open_file.close()
	if backup == True:
		shutil.copyfile(file_path,file_path+".back")
	write_file = open(file_path,'w')
	for line in edited_lines:
		write_file.write(line)
	write_file.close()

			

