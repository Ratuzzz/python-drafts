#!/usr/bin/python

from pathlib import Path
import re
import sys

# Get the current dir
currentPath = Path('.')

def rename_file(path):
    name = path.name
    print('Name was : ' + name)
    newName = re.sub(sys.argv[1], sys.argv[2], name) 
    print('New name is : ' + newName)
    path.rename(newName)

for fileName in currentPath.iterdir():
    rename_file(Path(fileName))

