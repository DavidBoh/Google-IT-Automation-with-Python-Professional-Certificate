#!/usr/bin/env python3
import os
import shutil
from PIL import Image

def conversion(full_path,ext):

    for filename in os.listdir(full_path):
        f = os.path.join(full_path, filename)
        if os.path.isfile(f):
            try:
                im = Image.open(f).convert('RGB')
                im.save(f + ext)
            except OSError:
                print("cannot convert", f)

def resizing(full_path):
    for filename in os.listdir(full_path):
        f = os.path.join(full_path,filename)
        if os.path.isfile(f):
            try:
                im = Image.open(f)
                im.resize((600,400)).save(f)
            except OSError:
                print("cannot resize", f)

def rename_file(path):
    for filename in os.listdir(path):
        f = os.path.join(path,filename)
        # would be nice to avoid deleteing the .tiff from the original tiffs
        if f.find(".tiff") != -1:
            new_file_name = f.replace('.tiff',"")
            os.rename(f,new_file_name)

def main():
    ext = ".jpeg"
    directory = "/home/user/supplier-data/images/"

    conversion(directory,ext)
    resizing(directory) 
    rename_file(directory)

main()

