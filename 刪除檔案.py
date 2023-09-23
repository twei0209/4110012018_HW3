# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 16:07:27 2023

@author: ASUS
"""

import os

cs_directory = 'CS'
file_path = os.path.join(cs_directory, 'homework.txt')

if os.path.exists(file_path):
    os.remove(file_path)