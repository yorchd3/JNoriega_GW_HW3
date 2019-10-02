# -*- coding: UTF-8 -*-
"""Employee Email Script.

This module allows us to create an email address using employee data from
a csv file.

Example:
    $ python employee_email.py

"""
import os
import csv

filepath = os.path.join("employees.csv")

new_employee_data = []


# Read data into dictionary and create a new email field
with open(filepath) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # YOUR CODE HERE
        first_name = row['first_name']
        last_name = row['last_name']
        ssn = row['ssn']
        email = first_name + "." + last_name + "@email.com"
        #Create a new dictionary with the data
        my_dict = {"first_name":first_name, "last_name":last_name,"SSN":ssn,"Email":email}
        #Save/append dictionary information per row into the new_employee_data
        new_employee_data.append(my_dict)
        #print(new_employee_data)


# Grab the filename from the original path
output_file = os.path.join("jorge.csv")

# Write updated data to csv file
csvpath = os.path.join(output_file)
with open(csvpath, "w") as csvfile:
    # YOUR CODE HERE
    fieldnames = ['first_name', 'last_name', 'SSN', 'Email']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(new_employee_data)

    
    
    
    
    
    
    