# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os

cs_directory = "CS"
file_path = os.path.join(cs_directory, "homework.txt")

file_size = os.path.join(file_path)
print(f'文件大小:{file_size} 字節')

modification_time = os.path.getatime(file_path)
print(f'最後修改時間:{modification_time}')

formatted_time = time.ctime(modification_time)
print(f'最後修改時間(人類可讀格式):{formatted_time}')