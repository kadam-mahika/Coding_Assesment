#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 01:43:59 2019

@author: kadam
"""


list_headers = [] 
list_seqs = [] 
currentSeq = ''

fh = open("/Users/kadam/Desktop/sample.fasta","r")

for line in fh:
    if line.startswith(">"):
        line = line.strip() 
        list_headers.append(line)
        
        if currentSeq != '': 
            list_seqs.append(currentSeq) 
            currentSeq = ''

#concatenates the lines by stripping the end of line character
    else:
        currentSeq += line.strip()

SeqCount = {}

for i in list_seqs:
    if i in SeqCount: 
        SeqCount[i] +=1
    else:
        SeqCount[i] =1

sorted(SeqCount, key=SeqCount.get, reverse=True)[:10]