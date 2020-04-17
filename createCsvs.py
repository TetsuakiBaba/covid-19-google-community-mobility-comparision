# coding: utf-8
import csv
import os
import glob
import argparse
import csv
import json
import matplotlib.pyplot as plt
import numpy as np

search_name = [
    ['JP', 'Japan',''],
    ['ES', 'Spain',''],
    ['GB', 'United Kingdom', ''],
    ['FR', 'France',''],
    ['IT', 'Italy', ''],
    ['US', 'United States',''],
    ['KR', 'South Korea',''],
    ['SG', 'Singapore', ''],
    ['TW', 'Taiwan', ''],
    ['IN', 'India', ''],
    ['DE', 'Germany', ''],
    ['TR', 'Turkey', ''],
    ['CH', 'Switzerland', ''],
    ['BE', 'Belgium', ''],
    ['NL', 'Netherlands', ''],
    ['CA', 'Canada', '' ],
    ['AT', 'Austria', ''],
    ['PT', 'Portugal', ''],
    ['BR', 'Brazil', ''],
    ['IL', 'Israel', ''],
    ['SE', 'Sweden', ''],
    ['AU', 'Australia', ''],
    ['NO', 'Norway', ''],
    ['IE', 'Ireland',''],
    ['CZ', 'Czechia', ''],
    ['MY', 'Malaysia', ''],
    ['EC', 'Ecuador', ''],
    ['PL', 'Poland', ''],
    ['PH', 'Philippines', ''],
    ['ID', 'Indonesia', ''],
    ['TH', 'Thailand', ''],
    ['PE', 'Peru', '']    
]
'''
search_name = [
    'Japan', 
    'Spain','United States', 
    'France',
    'Italy',
    'England',
    'South Korea',
    'Singapore',
    'Taiwan',
    'India',
    'Germany',
    'Iran',
    'The United Kingdom',
    'Turkey',
    'Switzerland',
    'Belgium',
    'Netherland',
    'Canada',
    'Austria',
    'Republic of Korea',
    'Portugal',
    'Brazil',
    'Israel',
    'Sweden',
    'Australia',
    'Norway',
    'Ireland',
    'Czecha',
    'Chile',
    'Russian Fedderation',
    'Malaysia',
    'Ecuador',
    'Poland',
    'Romania',
    'Philippines',
    'Pakistan',
    'Indonesia',
    'Thailand',
    'Finland',
    'Peru',
    'South Africa']
'''
category_name = ['Retail & recreation', 'Grocery & pharmacy', 'Parks', 'Transit stations', 'Workplace', 'Residential']
category_retail = []
category_grocery = []
category_parks = []
category_transit = []
category_workplace = []
category_residential = []
header = []

def createHeader(filename):
    f = open(filename, 'r')
    all_data = csv.reader(f,delimiter=",")
    header.append('Country_region')

    for data in all_data:
        if( data[0] == 'AE' and data[1] == 'United Arab Emirates' and data[2] == ''):
            header.append(data[4])
    f.close()


def createRankingBarGraph(title, category, data):
    x = []
    y = []
    labels = []
    for r in data:
        y.append(r[-1])
        x.append(r[0])
        labels.append(r[0])
    fig = plt.figure(figsize=(8.0, 4.0))
    plt.bar(x,y)
    plt.title(title)
    plt.ylabel('Percentage')
    plt.xlabel('City / Country')
    plt.subplots_adjust(left=0.1, right=0.95, bottom=0.3, top=0.85)
    plt.xticks(x,labels,rotation='vertical')
    plt.tick_params(labelsize=8)
    #plt.show()
    plt.savefig('result_images/'+category+'.png')



createHeader('Global_Mobility_Report.csv')
for name in search_name:
    retail = []
    grocery = []
    parks = []
    transit = []
    workplace = []
    residential = []
    
    f = open('Global_Mobility_Report.csv', 'r')
    all_data = csv.reader(f,delimiter=",")
    for data in all_data:
        if( name[0] == data[0] and name[1] == data[1] and name[2] == data[2]):            
            retail.append(data[5])
            grocery.append(data[6])
            parks.append(data[7])
            transit.append(data[8])
            workplace.append(data[9])
            residential.append(data[10])
    retail.insert(0, name[1])
    grocery.insert(0, name[1])
    parks.insert(0, name[1])
    transit.insert(0, name[1])
    workplace.insert(0, name[1])
    residential.insert(0, name[1])
    category_retail.append(retail)
    category_grocery.append(grocery)
    category_parks.append(parks)
    category_transit.append(transit)
    category_workplace.append(workplace)
    category_residential.append(residential)
    f.close()


f = open('result_csvs/retail.csv', "w")
print(*header, file=f, sep=",")
for r in category_retail:
    print(*r, file=f, sep=',')
f.close();    
f = open('result_csvs/grocery.csv', "w")
print(*header, file=f, sep=",")
for r in category_grocery:
    print(*r, file=f, sep=',')
f.close();    
f = open('result_csvs/parks.csv', "w")
print(*header, file=f, sep=",")
for r in category_parks:
    print(*r, file=f, sep=',')
f.close();    
f = open('result_csvs/transit.csv', "w")
print(*header, file=f, sep=",")
for r in category_transit:
    print(*r, file=f, sep=',')
f.close();    
f = open('result_csvs/workplace.csv', "w")
print(*header, file=f, sep=",")
for r in category_workplace:
    print(*r, file=f, sep=',')
f.close();    
f = open('result_csvs/residential.csv', "w")
print(*header, file=f, sep=",")
for r in category_residential:
    print(*r, file=f, sep=',')
f.close();    
