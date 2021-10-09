# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 13:16:07 2021

@author: jefni
"""
import csv
from collections import Counter

def frequency_checker(plaintext_filename):

    # to iterate over all 6 sources
    counter = 0
    for counter in range(0, 6):
        counter += 1
        if counter == 1:
            add = 'PG'
        elif counter == 2:
            add = 'LP'
        elif counter == 3:
            add = 'BM'
        elif counter == 4:
            add = 'RJ'
        elif counter == 5:
            add = 'PS'
        elif counter == 6:
            add = 'CG'

        # so i can iterate over column by column and output one by one
        column = 0
        for column in range(0, 15):
            column += 1
            plaintext_csv = plaintext_filename + '.csv'
            if column == 1:
                suffix = '8-L'
            elif column == 2:
                suffix = '8-LD'
            elif column == 3:
                suffix = '8-LS' 
            elif column == 4:
                suffix = '8-DS'
            elif column == 5:
                suffix = '8-LDS'
            elif column == 6:
                suffix = '12-L'
            elif column == 7:
                suffix = '12-LD'         
            elif column == 8:
                suffix = '12-LS'
            elif column == 9:
                suffix = '12-DS'         
            elif column == 10:
                suffix = '12-LDS'
            elif column == 11:
                suffix = '20-L'         
            elif column == 12:
                suffix = '20-LD'
            elif column == 13:
                suffix = '20-LS'         
            elif column == 14:
                suffix = '20-DS'
            elif column == 15:
                suffix = '20-LDS' 
            character_list = []
            with open(plaintext_csv) as file:
                csvreader = csv.reader(file)
                next(csvreader)
                generated_frequency_txt = plaintext_filename + '_frequency_' + add + '_' + suffix + '.txt'
                with open(generated_frequency_txt, 'w') as f:
                    for row in csvreader:
                        new_row = row[column]                    
                        for new_row_item in new_row:
                            character_list.append(new_row_item)
                    counter_string = Counter(character_list)
                    for key, value in counter_string.most_common():
                        key_value_pair = str(key) + ':' + str(value)
                        f.write('%s\n' % key_value_pair)


# just put filename, will add .csv suffix in fucntion
frequency_checker('stl1_all')
