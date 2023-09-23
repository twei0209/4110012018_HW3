# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os

cs_directory = "CS"

file_path = os.path.join(cs_directory, "homework.txt")

with open(file_path, "r") as file:
    content = file.read()
    
print(content)