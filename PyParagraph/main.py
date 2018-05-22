import os
import re

with open('paragraph.txt', 'r', encoding = 'utf8') as f:
	paragraph = f.read()

words = paragraph.split()
#sentences = paragraph.split('.')
#sentences = re.split("(?&lt;=[.!?]) +", paragraph)
sentences = re.split("\.|\?|!", paragraph ) # Original regex was too clever IMO
sentences = [x.strip() for x in sentences if len(x) > 2] #clean, remove empty elements if they exist. 

print ("Approximate word count: {}".format(len(words)))
print ("Approximate sentence count: {}".format(len(sentences)))
print ("Approximate letter count (per word): {}".format(len(paragraph)/float(len(words))))
print ("Average sentence length (in words): {}". format(len(words)/float(len(sentences))))

