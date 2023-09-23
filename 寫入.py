# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 16:00:14 2023

@author: ASUS
"""

import os

cs_directory = "CS"

file_path = os.path.join(cs_directory, "homework.txt")

with open(file_path, "w") as file:
    file.write("4110012018_鄭婷瑋")