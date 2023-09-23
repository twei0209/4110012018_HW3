# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os

cs_directory = 'CS'
file_path = os.path.join(cs_directory, 'homework.txt')

if os.path.exist(file_path):
    os.remove(file_path)