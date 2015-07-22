# -*- coding: utf-8 -*-
# !/usr/bin/env python

from __future__ import print_function
import os
import shutil
import fnmatch


def replace_text(file_path, find_text, replacetext, file_regexp="", backup=False):
    if type(file_path) != str or type(find_text) != str or type(replacetext) != str:
        raise Exception("Arguments should be of type String only")
    if type(backup) != bool:
        raise Exception("backup parameter should be of type Boolean")

    if not os.path.isfile(file_path) and os.path.isdir(file_path):
        for root, dirs, file_names in os.walk(os.path.abspath(file_path), topdown=False):
            for file_name in file_names:
                if fnmatch.fnmatch(file_name, file_regexp):
                    a=os.path.abspath(os.path.join(root, file_name))
                    replace_text(a,find_text,replacetext,file_regexp = file_regexp,backup = backup)
    elif os.path.isfile(file_path):
        open_file = open(file_path, 'r')
        all_lines = open_file.readlines()
        edited_lines = []
        for line in all_lines:
            replace_line = line.replace(find_text, replacetext)
            edited_lines.append(replace_line)
        open_file.close()
        if backup == True:
            shutil.copyfile(file_path, file_path + ".back")
        write_file = open(file_path, 'w')
        for line in edited_lines:
            write_file.write(line)
        write_file.close()

replace_text(".","@@test@@","shantanu",file_regexp="*.txt")