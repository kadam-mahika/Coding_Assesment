#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 01:43:59 2019

@author: kadam
"""


import pandas as pd

ch=input("Enter Chromosome: ")
coor=input("Enter start coordinate: ")
coor=int(coor)

#reading the annotation file
gene_data = pd.read_csv("/Users/kadam/Desktop/hg19_annotations.gtf", sep='\t',
                   names=["Chromosome","refFlat","Region","start_Coordinate","end_Coordinate",
                          "a","b","c","d","e"])

gene_data["Info"] = gene_data["a"] + gene_data["b"] + gene_data["c"] + gene_data["d"]

gene_data = gene_data.drop(['a','b','c','d','e'], axis = 1)
gene_data.head()

#shows the row/s of the particular chromosome t
reduced_data = gene_data[gene_data['Chromosome'].str.match(ch)]

#prints row of the information about given chromosome and coordinate
reduced_data.loc[reduced_data['start_Coordinate'] == coor]





