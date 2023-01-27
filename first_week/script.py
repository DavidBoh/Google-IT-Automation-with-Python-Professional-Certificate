#!/usr/bin/env python3
import os
import shutil
from PIL import Image

def conversion(full_path,ext):

    for filename in os.listdir(full_path):
        #filename is a string of the file names in 
        # current dir, f is created combining tthat with the full path
        # determined in the directory variable
        # we must pass "f" to function because
        # it has the full path. 
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
        if os.path.isfile(f) and f.endswith('.jpeg'):
            try:
                im = Image.open(f)
                im.resize((128,128)).save(f)
            except OSError:
                print("cannot resize", f)

def rotation(full_path):
    files = list()
    for filename in os.listdir(full_path):
        f = os.path.join(full_path,filename)
        if os.path.isfile(f) and f.endswith('.jpeg'):
            files.append(f) 
    ######
    new_dir = "new_dir"
    path = os.path.join(".",new_dir)
    os.mkdir(path) 

    #####

    destination = "/path/to/dir/"
    for i in files:
        path_name, file_name = os.path.split(i)
        #we are separating the file name from the full path
        try:
           im = Image.open(i)
           im.rotate(-90).save(i)
        except OSError:
            print("cannot rotate", i)

        shutil.move(i, destination + file_name)
        #if I dont move it to a different directory
        #there are goin to be inconsistencies in the rotation
        #because of the for loop. 
        # I do not yet fully understand why. 
        # must work on this 

def main():
    ext = ".jpeg"
    directory = "/path/to/dir"

    conversion(directory,ext)
    resizing(directory) 
    rotation(directory)

main()
