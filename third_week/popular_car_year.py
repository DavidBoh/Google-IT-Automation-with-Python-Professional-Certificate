#!/usr/bin/env python3
import json

def main():
    with open('car_sales.json') as json_file:
        data = json.load(json_file)

    car_info = []

    for item in data:
        car_info.append({'car_make':item['car']['car_make'],'car_model':item['car']['car_model'],'car_year':item['car']['car_year'],'total_sales':item['total_sales']})

    year_list = list()
    for my_dict in car_info:
        year_list.append(my_dict['car_year'])

    #create a list of dicts with only year and sum of total sales that year 
    unique_years = list(set(year_list))
    total_per_year = list()
    sum_sales = 0
    for i in unique_years:
        for j in car_info:
            if j['car_year'] == i:
                sum_sales = j['total_sales'] + sum_sales
        total_per_year.append({i:sum_sales})
        sum_sales=0
    
    
    winner_year = 0
    winner_year_sales = 0
    for i in unique_years: #iteration over list of unique years
        for v in total_per_year: # iteration over list of dicts
            for key,value in v.items(): # list unpacking
                if value > winner_year_sales:
                    winner_year = key
                    winner_year_sales = value

                    
    print("The most popular year was {} with {} sales.".format(winner_year,winner_year_sales))

main()
