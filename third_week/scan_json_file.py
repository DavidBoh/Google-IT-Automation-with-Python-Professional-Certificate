#!/usr/bin/env python3
import json

def main():
    with open('car_sales.json') as json_file:
        data = json.load(json_file)

    car_info = []

    for item in data:
        car_info.append({'car_model': item['car']['car_model'], 'total_sales': item['total_sales']})
        
    highest_sales = 0
    highest_sales_model = ""
    
    for d in car_info:
        if d['total_sales'] > highest_sales:
            highest_sales = d['total_sales']
            highest_sales_model = d['car_model']
    
    print("The {} had the most sales: {}".format(highest_sales_model,highest_sales))
main()
