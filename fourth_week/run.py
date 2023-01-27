#!/usr/bin/env python3
import os
import requests
import json

def create_list(files_path,list_of_files):
    """
    Function that creates a list of the lines of all files
    """
    lines_list = []
    for item in list_of_files:
        my_join = os.path.join(files_path,item)
        with open(my_join, 'r') as my_fh:
            for line in my_fh:
                if "lbs" in line:
                    line = line.replace("lbs","")
                    int(line)
                if type(line) == int:
                    lines_list.append(line)
                    continue
                line = line.replace("\n","")
                lines_list.append(line)
    return lines_list

def prepare_and_send(final_list):
    """
    Function that sends dictionaries as post requests, 
    one by one
    """
    categories_dict = {'name':'',
                       'weight':'',
                       'description':'',
                       'image_name':''}

    url = "http://0.9.9.8/fruits/"
    list_mover = 0
    headers={'Content-type':'application/json','Accept':'application/json'}
    for i in range(0,10):
        for key in categories_dict:
            categories_dict[key] = final_list[list_mover]
            list_mover += 1
            json_data = json.dumps(categories_dict)
            print(json_data)
        try:
            response = requests.post(url,data=json_data,headers=headers)
            print("posting to url {}".format(url))
            print("this {}".format(json_data))
            print("GET status code {}".format(response.status_code))
        except:
            print("GET status code {}".format(response.status_code))

def main():
    my_path = ("./supplier-data/descriptions/")
    path_list = os.listdir(my_path)

    final_list = create_list(my_path,path_list)
    prepare_and_send(final_list)
    print(final_list)

main()

