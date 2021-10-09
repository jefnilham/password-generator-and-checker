#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 21:10:31 2021

@author: chief
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from time import time
from time import sleep
import csv
import os
import json
import requests
import random
import string
import secrets




# set how many passwords to generate
passwords_to_generate = 5
filename = 'stl1_all.csv'
a = os.getcwd()





# function for PG, LP, BM
def save_to(website_shortform_x, char_x, classes, generated_password_list_x):
    df = pd.read_csv(filename)
    df['%s_%s-%s' % (website_shortform_x, char_x, classes)] = pd.DataFrame(generated_password_list_x)
    df.to_csv(filename, index=False)
  
    
  


# functions for PG    
def gen_copy_loop_1(generated_password_list_x):
    passwords_generated = 0
    while passwords_generated < passwords_to_generate:
        driver.find_element_by_css_selector('div.button:nth-child(1)').click()
        generated_password = driver.find_element_by_id('final_pass').get_attribute("value")
        generated_password_list_x.append(generated_password)
        passwords_generated = passwords_generated + 1
        
def character_classes_1(char_x):
    classes = 'L'
    driver.find_element_by_css_selector('#Symbols').click()
    driver.find_element_by_css_selector('#Numbers').click()
    driver.find_element_by_css_selector('#Nosimilar').click()
    generated_password_list_a = []
    gen_copy_loop_1(generated_password_list_a)
    save_to(website_shortform_1, char_x, classes, generated_password_list_a)
    
    classes = 'LD'
    driver.find_element_by_css_selector('#Numbers').click()
    generated_password_list_b = []
    gen_copy_loop_1(generated_password_list_b)
    save_to(website_shortform_1, char_x, classes, generated_password_list_b)

    classes = 'LS'
    driver.find_element_by_css_selector('#Numbers').click()
    driver.find_element_by_css_selector('#Symbols').click()
    generated_password_list_c = []
    gen_copy_loop_1(generated_password_list_c)
    save_to(website_shortform_1, char_x, classes, generated_password_list_c)

    classes = 'DS'
    driver.find_element_by_css_selector('#Numbers').click()
    driver.find_element_by_css_selector('#Lowercase').click()
    driver.find_element_by_css_selector('#Uppercase').click()
    generated_password_list_d = []
    gen_copy_loop_1(generated_password_list_d)
    save_to(website_shortform_1, char_x, classes, generated_password_list_d)

    classes = 'LDS'
    driver.find_element_by_css_selector('#Lowercase').click()
    driver.find_element_by_css_selector('#Uppercase').click()
    generated_password_list_e = []
    gen_copy_loop_1(generated_password_list_e)
    save_to(website_shortform_1, char_x, classes, generated_password_list_e)






# functions for LP
def gen_copy_loop_2(generated_password_list_x):
    passwords_generated = 0
    while passwords_generated < passwords_to_generate:
        generated_password = driver.find_element_by_id('GENERATED-PASSWORD').get_attribute("value")
        driver.find_element_by_css_selector('button.lp-pg-generated-password__icon:nth-child(2)').click()
        generated_password_list_x.append(generated_password)
        passwords_generated = passwords_generated + 1
      
    
def character_classes_2(char_x):
    classes = 'L'
    driver.find_element_by_css_selector('div.lp-checkbox:nth-child(3) > label:nth-child(2)').click()
    driver.find_element_by_css_selector('div.lp-checkbox:nth-child(4) > label:nth-child(2)').click()
    generated_password_list_a = []
    
    # call the generation and copy function
    gen_copy_loop_2(generated_password_list_a)
    save_to(website_shortform_2, char_x, classes, generated_password_list_a)
    
    classes = 'LD'
    driver.find_element_by_css_selector('div.lp-checkbox:nth-child(3) > label:nth-child(2)').click()
    generated_password_list_b = []
    gen_copy_loop_2(generated_password_list_b)
    save_to(website_shortform_2, char_x, classes, generated_password_list_b)

    classes = 'LS'
    driver.find_element_by_css_selector('div.lp-checkbox:nth-child(3) > label:nth-child(2)').click()
    driver.find_element_by_css_selector('div.lp-checkbox:nth-child(4) > label:nth-child(2)').click()
    generated_password_list_c = []
    gen_copy_loop_2(generated_password_list_c)
    save_to(website_shortform_2, char_x, classes, generated_password_list_c)

    classes = 'DS'
    driver.find_element_by_css_selector('div.lp-checkbox:nth-child(3) > label:nth-child(2)').click()
    driver.find_element_by_css_selector('div.lp-checkbox:nth-child(2) > label:nth-child(2)').click()
    driver.find_element_by_css_selector('div.lp-checkbox:nth-child(1) > label:nth-child(2)').click()
    generated_password_list_d = []
    gen_copy_loop_2(generated_password_list_d)
    save_to(website_shortform_2, char_x, classes, generated_password_list_d)

    classes = 'LDS'
    driver.find_element_by_css_selector('div.lp-checkbox:nth-child(1) > label:nth-child(2)').click()
    driver.find_element_by_css_selector('div.lp-checkbox:nth-child(2) > label:nth-child(2)').click()
    generated_password_list_e = []
    gen_copy_loop_2(generated_password_list_e)
    save_to(website_shortform_2, char_x, classes, generated_password_list_e)

    


website_1 = 'https://passwordsgenerator.net/'
website_shortform_1 = 'PG'
website_2 = 'https://www.lastpass.com/features/password-generator'
website_shortform_2 = 'LP'

    

# create csv file and index so can use pandas
f = open(filename, 'w')
writer = csv.writer(f)
index_list = []
i = 1
while i < (passwords_to_generate + 1):
    index_list.append(i)
    i += 1
header = ['Index']
writer.writerow(header)
for w in range(passwords_to_generate):
    writer.writerow([index_list[w]])
f.close() 

# open chrome browser
driver = webdriver.Chrome(ChromeDriverManager().install())



# source 1, PG
start = time()   
driver.get(website_1)
generated_password_list_x = []
char_8 = '8'
char_12 = '12'
char_20 = '20'

driver.execute_script("window.scrollTo(0, 1000)")
# 8 char
driver.find_element_by_css_selector('#pgLength').click()
driver.find_element_by_css_selector('#pgLength > optgroup:nth-child(1) > option:nth-child(3)').click()
driver.find_element_by_css_selector('#sec_btn > div.button.GenerateBtn').click()
character_classes_1(char_8)


# 12 char
driver.refresh()
driver.find_element_by_css_selector('#pgLength').click()
driver.find_element_by_css_selector('#pgLength > optgroup:nth-child(1) > option:nth-child(7)').click()
driver.find_element_by_css_selector('div.button:nth-child(1)').click()
character_classes_1(char_12)

# 20 char
driver.refresh()
driver.find_element_by_css_selector('#pgLength').click()
driver.find_element_by_css_selector('#pgLength > optgroup:nth-child(2) > option:nth-child(5)').click()
driver.find_element_by_css_selector('div.button:nth-child(1)').click()
character_classes_1(char_20)

end = time()
time_taken = end - start
print('Source:', website_1)
print('Time taken:', time_taken, 'seconds')
print((passwords_to_generate / time_taken), 'passwords per second', '\n')







# source 2, LP
start = time()   
driver.get(website_2)
generated_password_list_x = []
char_8 = '8'
char_12 = '12'
char_20 = '20'

# close cookies iframe
def close_popup_2():
    sleep(3)
    iframe = driver.find_element_by_id('LPST_trustarc')
    driver.switch_to.frame(iframe)
    driver.find_element_by_xpath('//*[@id="truste-consent-close"]').click()
    sleep(3)
    driver.switch_to.default_content()
    


# 8 char
close_popup_2()
driver.find_element_by_css_selector('#lp-pg-password-length').send_keys(Keys.DELETE, Keys.DELETE, '8')
character_classes_2(char_8)

# 12 char
driver.refresh()
close_popup_2()
driver.find_element_by_css_selector('#lp-pg-password-length').send_keys(Keys.DELETE, Keys.DELETE, '12')
character_classes_2(char_12)

# 20 char
driver.refresh()
close_popup_2()
driver.find_element_by_css_selector('#lp-pg-password-length').send_keys(Keys.DELETE, Keys.DELETE, '20')
character_classes_2(char_20)


end = time()
time_taken = end - start
print('Source:', website_2)
print('Time taken:', time_taken, 'seconds')
print((passwords_to_generate / time_taken), 'passwords per second', '\n')






# source 3, BM
website_shortform_3 = 'BM'
website_3 = 'http://www.thebitmill.com/tools/password.html'
start = time()   
driver.get(website_3)
generated_password_list_x = []
char_8 = '8'
char_12 = '12'
char_20 = '20'


    
def gen_copy_loop_3(generated_password_list_x):
    passwords_generated = 0
    while passwords_generated < passwords_to_generate:
        driver.find_element_by_css_selector('#pgen > tbody > tr:nth-child(5) > td > p:nth-child(1) > input[type=button]:nth-child(1)').click()
        generated_password = driver.find_element_by_id('outbox').get_attribute("value")
        generated_password_list_x.append(generated_password)
        passwords_generated = passwords_generated + 1

        
def character_classes_3(char_x):
    classes = 'L'
    generated_password_list_a = []
    gen_copy_loop_3(generated_password_list_a)
    save_to(website_shortform_3, char_x, classes, generated_password_list_a)
    
    classes = 'LD'
    driver.find_element_by_css_selector('#dg').click()
    generated_password_list_b = []
    gen_copy_loop_3(generated_password_list_b)
    save_to(website_shortform_3, char_x, classes, generated_password_list_b)

    classes = 'LS'
    driver.find_element_by_css_selector('#dg').click()
    driver.find_element_by_css_selector('#pn').click()
    generated_password_list_c = []
    gen_copy_loop_3(generated_password_list_c)
    save_to(website_shortform_3, char_x, classes, generated_password_list_c)

    classes = 'DS'
    driver.find_element_by_css_selector('#dg').click()
    driver.find_element_by_css_selector('#up').click()
    driver.find_element_by_css_selector('#lo').click()
    generated_password_list_d = []
    gen_copy_loop_3(generated_password_list_d)
    save_to(website_shortform_3, char_x, classes, generated_password_list_d)

    classes = 'LDS'
    driver.find_element_by_css_selector('#up').click()
    driver.find_element_by_css_selector('#lo').click()
    generated_password_list_e = []
    gen_copy_loop_3(generated_password_list_e)
    save_to(website_shortform_3, char_x, classes, generated_password_list_e)
    
    
# 8 char
driver.execute_script("window.scrollTo(0, 1000)")
driver.find_element_by_css_selector('#dg').click()
driver.find_element_by_css_selector('#pn').click()
driver.find_element_by_css_selector('#le').click()
driver.find_element_by_css_selector('#le').send_keys(Keys.BACKSPACE, Keys.BACKSPACE, '8')
driver.find_element_by_css_selector('#pgen > tbody > tr:nth-child(5) > td > p:nth-child(1) > input[type=button]:nth-child(1)').click()
character_classes_3(char_8)


# 12 char
driver.refresh()
driver.execute_script("window.scrollTo(0, 1000)")
driver.find_element_by_css_selector('#dg').click()
driver.find_element_by_css_selector('#pn').click()
driver.find_element_by_css_selector('#le').send_keys(Keys.BACKSPACE, Keys.BACKSPACE, '12')
driver.find_element_by_css_selector('#pgen > tbody > tr:nth-child(5) > td > p:nth-child(1) > input[type=button]:nth-child(1)').click()
character_classes_3(char_12)

# 20 char
driver.refresh()
driver.execute_script("window.scrollTo(0, 1000)")
driver.find_element_by_css_selector('#dg').click()
driver.find_element_by_css_selector('#pn').click()
driver.find_element_by_css_selector('#le').send_keys(Keys.BACKSPACE, Keys.BACKSPACE, '20')
driver.find_element_by_css_selector('#pgen > tbody > tr:nth-child(5) > td > p:nth-child(1) > input[type=button]:nth-child(1)').click()
character_classes_3(char_20)

end = time()
driver.close()

time_taken = end - start
print('Source:', website_3)
print('Time taken:', time_taken, 'seconds')
print((passwords_to_generate / time_taken), 'passwords per second', '\n')







# source 4, RJ
def RJ_merged_url(chars, b):
    url = 'https://random.justyy.workers.dev/api/random/?cached&n=' + str(chars) + '&x=' + str(b) 
    return url


def RJ_gen(chars, b, combi):
    passwords_list = []
    i = 0
    while i < passwords_to_generate:
        url = RJ_merged_url(chars, b)
        response = requests.get(url)
        decoded_data = json.loads(response.content.decode('utf-8'))
        #if decoded_data[0] == '=':
        #    continue
        #print(i + 1, decoded_data)
        passwords_list.append(decoded_data)
        i += 1
    df = pd.read_csv(filename)
    df['RJ_%s-%s' % (chars, combi)] = pd.DataFrame(passwords_list)
    df.to_csv(filename, index=False)
   
start = time()

RJ_gen(8, 3, 'L')
RJ_gen(8, 7, 'LD')
RJ_gen(8, 11, 'LS')
RJ_gen(8, 12, 'DS')
RJ_gen(8, 15, 'LDS')

RJ_gen(12, 3, 'L')
RJ_gen(12, 7, 'LD')
RJ_gen(12, 11, 'LS')
RJ_gen(12, 12, 'DS')
RJ_gen(12, 15, 'LDS')

RJ_gen(20, 3, 'L')
RJ_gen(20, 7, 'LD')
RJ_gen(20, 11, 'LS')
RJ_gen(20, 12, 'DS')
RJ_gen(20, 15, 'LDS')

end = time()
time_taken = end - start
print('Source:', 'https://random.justyy.workers.dev/api/')
print('Time taken:', time_taken, 'seconds')
print((passwords_to_generate / time_taken), 'passwords per second', '\n')







# for source 5 and 6

L = string.ascii_letters
LD = string.ascii_letters + string.digits
LS = string.ascii_letters + string.punctuation
DS = string.digits + string.punctuation
LDS = string.ascii_letters + string.digits + string.punctuation


# source 5, ps
def gen_password_secrets(length, combi, combi_string):
    passwords_list = []
    n = 0
    counter = 0
    while n < passwords_to_generate:
        
         #Get an instance of the secure random generator
         secrets_gen = secrets.SystemRandom()
         password = ''.join(secrets_gen.choice(combi) for i in range(length))
         #if password[0] == '=':
         #    continue
         # print(n + 1, password)
         n += 1
         counter += 1
         passwords_list.append(password)
         if counter == 10000:
             print('Current PS_%s-%s:' % (length, combi_string), n)
             counter = 0
         df = pd.read_csv(filename)
         df['PS_%s-%s' % (length, combi_string)] = pd.DataFrame(passwords_list)
         df.to_csv(filename, index=False)




def gen_passwords_secrets_overall(length):
    gen_password_secrets(length, L, 'L')
    gen_password_secrets(length, LD, 'LD')
    gen_password_secrets(length, LS, 'LS')
    gen_password_secrets(length, DS, 'DS')
    gen_password_secrets(length, LDS, 'LDS')

start = time()

gen_passwords_secrets_overall(8)
gen_passwords_secrets_overall(12)
gen_passwords_secrets_overall(20)

end = time()
time_taken = end - start
print('Source: Python Secrets Module')
print('Time taken:', time_taken, 'seconds')
print((passwords_to_generate / time_taken), 'passwords per second', '\n')







# source 6, cg 
def gen_password_urandom(length, combi, combi_string):
    passwords_list = []
    n = 0
    while n < passwords_to_generate:
         random.seed = (os.urandom(1024))
         password = ''.join(random.choice(combi) for i in range(length))
         n += 1
         passwords_list.append(password)
         df = pd.read_csv(filename)
         df['WC_%s-%s' % (length, combi_string)] = pd.DataFrame(passwords_list)
         df.to_csv(filename, index=False)

def gen_passwords_urandom_overall(length):
    gen_password_urandom(length, L, 'L')
    gen_password_urandom(length, LD, 'LD')
    gen_password_urandom(length, LS, 'LS')
    gen_password_urandom(length, DS, 'DS')
    gen_password_urandom(length, LDS, 'LDS')

start = time()

gen_passwords_urandom_overall(8)
gen_passwords_urandom_overall(12)
gen_passwords_urandom_overall(20)

end = time()
time_taken = end - start
print('Source: Windows CryptGenRandom')
print('Time taken:', time_taken, 'seconds')
print((passwords_to_generate / time_taken), 'passwords per second', '\n')


print(filename, 'saved in', a)

