# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 08:54:02 2021

@author: jefni
"""
import operator
from time import time
import numpy as np
import string


import hashlib
import subprocess

def rcrack(string, points):
    string_md5 = hashlib.md5(string.encode()).hexdigest()
    string_md5_text = string + '.txt'
    with open(string_md5_text, 'w') as f:
        f.write('%s' % string_md5)
    subprocess.run('rcrack . -l %s' % string_md5_text, shell=True)
    output = (subprocess.check_output('rcrack . -l %s' % string_md5_text, shell=True)).decode('utf-8')
    if '1 of 1' in output:
        print('[0 / 1 points]')
        print('Password cracked in rainbow table.')
    else:
        points.append(1)
        print('[1 / 1 points]')
        print('Password not found in rainbow table.')
    
def combination_count(string, points):
    islower = 0
    isupper = 0
    isdigit = 0
    isspecial = 0
    character_counter = 0
    
    for char in string:
        if char.islower():
            islower += 1
        elif char.isupper():
            isupper += 1
        elif char.isdigit():
            isdigit += 1
        elif not char.isalnum():
            isspecial += 1
            
            
    if islower > 0:
        character_counter += 26
    if isupper > 0:
        character_counter += 26
    if isdigit > 0:
        character_counter += 10
    if isspecial > 0:
        character_counter += 34

    password_length = len(string)
    password_permutations = character_counter ** password_length
    
    # passwords per second
    bruteforce_rate = 100000000000 
    time_to_bruteforce = password_permutations / bruteforce_rate / 86400
    if 365 <= time_to_bruteforce <= 36500:
        points.append(1)
        print('[1 / 2 points]')
    elif time_to_bruteforce > 36500:
        points.append(1)
        points.append(1)
        print('[2 / 2 points]')
    else:
        print('[0 / 2 points]')
    print("Time needed to crack your password:", time_to_bruteforce, 'days')



def distance(s, t, points, ratio_calc = False):
    """ levenshtein_ratio_and_distance:
        Calculates levenshtein distance between two strings.
        If ratio_calc = True, the function computes the
        levenshtein distance ratio of similarity between two strings
        For all i and j, distance[i,j] will contain the Levenshtein
        distance between the first i characters of s and the
        first j characters of t
    """
    # Initialize matrix of zeros
    rows = len(s)+1
    cols = len(t)+1
    distance = np.zeros((rows,cols),dtype = int)

    # Populate matrix of zeros with the indeces of each character of both strings
    for i in range(1, rows):
        for k in range(1,cols):
            distance[i][0] = i
            distance[0][k] = k

    # Iterate over the matrix to compute the cost of deletions,insertions and/or substitutions    
    for col in range(1, cols):
        for row in range(1, rows):
            if s[row-1] == t[col-1]:
                cost = 0 # If the characters are the same in the two strings in a given position [i,j] then the cost is 0
            else:
                # In order to align the results with those of the Python Levenshtein package, if we choose to calculate the ratio
                # the cost of a substitution is 2. If we calculate just distance, then the cost of a substitution is 1.
                if ratio_calc == True:
                    cost = 2
                else:
                    cost = 1
            distance[row][col] = min(distance[row-1][col] + 1,      # Cost of deletions
                                 distance[row][col-1] + 1,          # Cost of insertions
                                 distance[row-1][col-1] + cost)     # Cost of substitutions
    if ratio_calc == True:
        # Computation of the Levenshtein Distance Ratio
        Ratio = ((len(s)+len(t)) - distance[row][col]) / (len(s)+len(t))
        return Ratio
    elif distance[row][col] > 10:
        # print(distance) # Uncomment if you want to see the matrix showing how the algorithm computes the cost of deletions,
        # insertions and/or substitutions
        # This is the minimum number of edits needed to convert string a to string b
        points.append(1)
        points.append(1)
        print('[2 / 2 points]')
        return "Your password is hard to guess being {} edits away from the closest looking password.".format(distance[row][col])
    elif 5 <= distance[row][col] <= 10:
        points.append(1)
        print('[1 / 2 points]')
        return "Your password is guessable being {} edits away from the closest looking password.".format(distance[row][col])
    elif distance[row][col] < 5:
        print('[0 / 2 points]')
        return "Your password is easily guessable being only {} edits away from the closest looking password.".format(distance[row][col])


def closest_password(s1, s2, ratio_calc = False):
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    distances = range(len(s1) + 1)
    for i2, c2 in enumerate(s2):
        distances_ = [i2+1]
        for i1, c1 in enumerate(s1):
            if c1 == c2:
                distances_.append(distances[i1])
            else:
                distances_.append(1 + min((distances[i1], distances[i1 + 1], distances_[-1])))
        distances = distances_
    return distances[-1]


points = []

scores = {}
start  = time()

string = input("Test your password: ")

with open('rockyou.txt', 'r', encoding='latin1') as f:
    line = f.readlines()
    rockyou_list = [x.rstrip() for x in line]

#string = 'pizza'
# matchings = ['ewfrwesv4454', 'pizza fries', 'pichhha', 'pilllls', 'sdfsdf']



    for m in rockyou_list:
        scores[m] = 1 - closest_password(string,m)
    
    end = time()    
    # print(scores)
    print('\n')
    #print('Time taken:', end - start)
    distance = distance(string, max(scores.items(), key=operator.itemgetter(1))[0], points)
    print(distance)
    print('The closest looking password from the ''RockYou'' data breach:', max(scores.items(), key=operator.itemgetter(1))[0])
    
    print('\n')
    combination_count(string, points)
    
    print('\n')
    rcrack(string, points)

print('\n')
print("Password Score:", "[" + str(len(points)), "/ 5 points]")

if len(points) == 5:
    print("Your password is cryptographically secure!")
elif 3 <= len(points) <= 4:
    print("Your password is only moderately secure. You should strengthen password.")
elif len(points) < 3:
    print("Password not safe for use! Please strengthen password.")
