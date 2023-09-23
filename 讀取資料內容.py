# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 16:03:54 2023

@author: ASUS
"""

import os

cs_directory = "CS"

file_path = os.path.join(cs_directory, "homework.txt")

with open(file_path, "r") as file:
    content = file.read()
    
print(content)