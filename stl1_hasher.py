# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 23:15:05 2021

@author: jefni
"""
import hashlib
import csv

def hasher(plaintext_filename):
    
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
            with open(plaintext_csv) as file:
                csvreader = csv.reader(file)
                next(csvreader)
                generated_md5_txt = plaintext_filename + '_md5_' + add + '_' + suffix + '.txt'
                print('Starting on %s-%s' % (add, generated_md5_txt))
                with open(generated_md5_txt, 'w') as f:
                    for row in csvreader:
                        new_row = row[column]
                        new_row = [hashlib.md5(new_row.encode()).hexdigest()]
                        for new_row_item in new_row:
                            f.write('%s\n' % new_row_item)
                            # print(new_row_item)



# just put filename, will add .csv suffix in fucntion
hasher('stl1_all')



