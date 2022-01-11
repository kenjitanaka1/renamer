import sys
import os
import random
import string

"""
Renames all the files in a folder and subfolders to random names.
"""
if (len(sys.argv) is not 2):
    raise ValueError('Usage: renamer.py /path/to/folder')

dir = sys.argv[1]
letters = string.ascii_lowercase

for subdir, dirs, files in os.walk(dir):
    for filename in files:
        filepath = subdir + os.sep + filename

        if (filepath.endswith('.jpg') or filepath.endswith('.png') or
            filepath.endswith('.jpeg') or filepath.endswith('.gif') or
            filepath.endswith('.jfif') or filepath.endswith('.tiff')):
            ext = os.path.splitext(filename)[-1]
            newname = ''.join(random.choice(letters) for i in range(32))
            newpath = subdir + os.sep + newname + ext

            os.rename(filepath, newpath)