#!/usr/bin/env python3

import argparse
import os
import subprocess

# convert entire directories of heic images to jpg format
parser = argparse.ArgumentParser()
parser.add_argument("relpath", help="the relative path of the directory containing heic files")
args = parser.parse_args()
relpath = args.relpath

abspath = os.path.abspath('.')
fullpath = os.path.join(abspath, relpath)

imglist = os.listdir(fullpath)
# filter out the heic files only
imglist = filter(lambda x: x[-4:].lower() == "heic", imglist)
imglist = [os.path.join(fullpath, x) for x in imglist]

for img in imglist:
    print("processing image: " + img)
    name = os.path.basename(img).split('.')[0]
    subprocess.run(['heif-convert', img, os.path.join(fullpath, name) + '.jpg'])