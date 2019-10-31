import os
import sys
from IPython.nbformat import v3, v4

DIR = "/home"

for dirName, subdirList, fileList in os.walk(DIR):
    if dirName.startswith(DIR + "/student") or dirName.startswith(DIR + "/educator"):
        for fname in fileList:
            with open(dirName + "/" + fname, 'r') as fpin:
                text = fpin.read()
            nbook = v3.reads_py(text)
            nbook = v4.upgrade(nbook)

            jsonform = v4.writes(nbook) + "\n"
            with open(dirName + "/" + fname[:len(fname)-3] + ".ipynb", 'w') as fpout:
                fpout.write(jsonform)

