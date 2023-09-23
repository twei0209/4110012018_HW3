# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os

cs_directory = "cs"

file_path = os.path.join(cs_directory, "homework.txt")

with open(file_path, "w") as file:
    file.write("4110012018_鄭婷瑋")