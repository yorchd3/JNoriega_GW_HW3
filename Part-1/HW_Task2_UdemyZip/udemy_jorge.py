import os
import csv

udemy_csv = os.path.join("web_starter.csv")

title = []
price = []
subscribers = []
reviews = []
length = []
percent_reviewers = []


with open(udemy_csv, encoding = 'utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
   
    # loop through
    for row in csvreader:
        
        title.append(row[1])
        price.append(row[4])
        subscribers.append(row[5])
        reviews.append(row[6])
        #length.append(row[9])

        result = round((int(row[6]) / int(row[5]) )*100,2)
        percent_reviewers.append(result)
        #print(percent_reviewers)
        
        new_length = row[9].split(" ")
        length.append(float(new_length[0]))
                
zipped_data = zip(title, price, subscribers, reviews, length, percent_reviewers) 

output_file = os.path.join("jorge_web_final.csv")

with open(output_file, "w", newline='') as datafile:
        writer = csv.writer(datafile)
        
        writer.writerow(["Title","Price","Subscribers","Reviews","Length","PercentReviewers"])
        writer.writerows(zipped_data)


#jorge_csv = os.path.join("jorge_web_final.csv")
        
#def percentage_function(row_data):
#    subs = int(row_data[2])
#    revs = int(row_data[3])
#    percent_reviewers = (revs / subs)*100
#    #print(percent_reviewers)
#    
#with open(jorge_csv, 'r') as csvfile:
#    csvreader2 = csv.reader(csvfile, delimiter=",")
#    heater = next(csvreader2)
#    # loop through
#    for row in csvreader2:
#         percentage_function(row)


        