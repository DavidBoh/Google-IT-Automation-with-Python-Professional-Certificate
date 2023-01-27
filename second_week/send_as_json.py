#!/usr/bin/env python3
import requests
import json

def main():

    categories_dict = {'title':'',
                       'name':'',
                       'date':'',
                       'feedback':''}

    url = "http://0.1.1.1/feedback/"
    #headers to send with the post request
    headers={'Content-type':'application/json','Accept':'application/json'}
    #convert dict to JSON
    json_data = json.dumps(categories_dict)

    try:
        #the BIG important line
        response = requests.post(url,data=json_data,headers=headers)
        print("posting to this url {}".format(url))
        print("this {}".format(json_data))
        print("GET status code {}".format(response.status_code))
    except:
        print("GET status code {}".format(response.status_code))

main()
