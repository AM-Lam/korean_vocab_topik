# import os
# import time
import pandas as pd
import numpy as np
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

# A dictionary of korean word from the Topik and Go database by Julien Shim(https://github.com/julienshim/combined_korean_vocabulary_list) by using pandas
# Can be based on frequency or korean alphabet
inputfPath = './output/combined_topik_go.tsv'
# mode = input("Enter your Mode: (alphabet or all by entering 1) ")

# load the database from tsv file
tsv_body = pd.read_table(inputfPath)

# Edge Case: combine the word with double meaning(with a number after the korean word)
# Make a filter of the row of 'korean word' with digital number
pattern = tsv_body['korean'].str.contains(r'(\d+)')
# pattern = tsv_body['korean'].str.extract(r'([ab])?(\d+)')
# Remove the number from the target word
tsv_body['merged'] = tsv_body['korean'].str.replace(r'(\d+)', '')

# Combine the korean word with hint if the target word has number after it
tsv_body.loc[pattern, 'merged'] = tsv_body.loc[pattern, 'merged'].str.cat(tsv_body['hint'], na_rep = '')
tsv_body['merged'] = tsv_body['merged'].str.replace('~', '')
tsv_body.loc[~pattern, 'merged'] = tsv_body['korean']

# print(tsv_body['merged'].tolist())
# print(tsv_body['merged'])

# type: 'pandas.core.frame.DataFrame'
# sort the df by the frequency(int type) in descending order
sort = tsv_body.sort_values(["frequency"], ascending = False)
# # Drop the nan value in frequency column
# tsv_body = tsv_body.dropna(subset=['merged'])
# print(sort)
korean_dict = {}

# Create a dictionary for all the alphabet in 'korean' column
for s in sort['merged']:
  if (s[0] not in korean_dict.keys()):
    korean_dict[s[0]] = []
    korean_dict[s[0]].append(s)
 
  else:
    if (s not in korean_dict[s[0]]):
      korean_dict[s[0]].append(s)

print(korean_dict)  
# print(korean_dict[mode])
# print(tsv_body['merged'].tolist())

