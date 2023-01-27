#!/usr/bin/env python3
from datetime import datetime
import os
import reports
import json
import emails


def create_json(path):
    # iterate thru every file in the path
    # open each file, save contents in list
    the_list = list()
    for i in os.listdir(path):
        actual_file = os.path.join(path,i)
        if actual_file.endswith('.txt'):
            with open(actual_file, 'r') as file:
                result = file.readlines()
                the_list.append(result)

    #clean the data of the listt of lists
    #extract only the two first elements we need
    first_two_elements = []
    for sublist in the_list:
        #print(sublist[0:2])
        # first 2 elements we need
        for i in sublist:
            j = i.splitlines()
            for k, line in enumerate(j):
                first_two_elements.append(line)
                if k == 1:
                    break

    # my algorithm to remove every 2 element
    iterator = 0 
    indexer = 1
    new_list = list()
    while iterator < len(first_two_elements):
        if indexer > len(first_two_elements):
            break
        new_list.append(first_two_elements[indexer-1])
        indexer += 1
        new_list.append(first_two_elements[indexer-1])
        indexer += 3
        iterator += 1

    ###
    # List dir merger goes here if needed
    ###
    return new_list
def final_organizator(the_dict):
    
    iterator = 0 
    indexer = 1
    my_str = str()

    while iterator < len(the_dict):
        if indexer > len(the_dict):
            break
        my_str += 'name: '+ the_dict[indexer-1] + "<br/>"
        indexer += 1
        my_str += 'weight: '+ the_dict[indexer-1] + "<br/>"
        indexer += 1
        my_str += "<br/>"
        iterator += 1

    return my_str

def main():
    summary = create_json('/path/to/dir')
    time_now = datetime.now()
    formatted_time = time_now.strftime("%B %d, %Y")
    summary_str = final_organizator(summary)

    print(summary_str)

    # Generate PDF 

    reports.generate("/tmp/processed.pdf","Processed Update on " + 
                     formatted_time,
                     summary_str)

    # Send Email

    sender = 'automation@example.com'
    receiver = "{}@example.com".format(os.environ.get('USER'))
    subject = "Upload Completed - Online Fruit Store"
    body = ("All fruits are uploaded to our website successfully." +
    "A detailed list is attached to this email.")

    message = emails.generate(sender,receiver,subject,body,"/tmp/processed.pdf")

    emails.send(message)

    print("Script ran successfully")

if __name__ == "__main__":
    main()

