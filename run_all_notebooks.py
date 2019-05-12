import os
import sys
import subprocess

DIR = "/home"

count = 0
for dirName, subdirList, fileList in os.walk(DIR):
    if dirName.startswith(DIR + "/student") or dirName.startswith(DIR + "/educator"):
        count += 1
        print("currently :", count)
        for fname in fileList:
            if fname.endswith(".ipynb"):
                subprocess.call("jupyter nbconvert --to notebook --inplace --execute " + dirName + "/" + fname, shell = True)
        if count >= 100:
            sys.exit()
