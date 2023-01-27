#!/usr/bin/env python3
import os

#run this bash script to determine the num of lines of each file
#for file in $(ls); do echo "$file: $(wc -l < $file)"; done

def delete_blanks(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r') as file:
                lines = file.readlines()
                if lines and not lines[-1].strip(): #chck if line extists and if it's empty
                    lines.pop()
                    with open(filepath, 'w') as file:
                        file.writelines(lines)

def create_list(path):
    list_of_imgs = list()
    for i in os.listdir(path):
        if i == 'README' or i == 'LICENSE':
            continue
        if not i.endswith(".jpeg"):
            continue
        list_of_imgs.append(i)

    return(list_of_imgs)

def append_jpeg(list_of_img,txt_path):
    indexer = 0
    for filename in os.listdir(txt_path):
        if filename.endswith(".txt"): 
            path_and_name = os.path.join(txt_path, filename)
            #print("appending {} into {}".format(list_of_img[indexer],path_and_name))
            with open(path_and_name, 'a') as file:
                file.write(list_of_img[indexer])
        indexer += 1

def main():
    descrip_directory = '/home/user/supplier-data/descriptions/'
    imgs_directory = '/home/user/supplier-data/images/'

    my_list = create_list(imgs_directory)
    my_list.sort()
    delete_blanks(descrip_directory)
    append_jpeg(my_list,descrip_directory)
    
      
main()

