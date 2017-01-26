#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 13:05:03 2017

@author: dionisis
"""

file='example'

from numpy import zeros, ones

def read_input():
    from numpy import zeros

    f = open('input_files/'+ file + '.in','r')

    line = f.readline()

    noOfIngredients = 2
    
    fline = line
    fline.replace('\n','')
    words = fline.split(" ")  
    rSize = int(words[0])
    cSize = int(words[1])
    minItem = int(words[2])
    maxCells = int(words[3]) 
    
    pizza=zeros(rSize*cSize).reshape(rSize,cSize)
    
    for row in range(0,rSize):
        line = f.readline()
        line=line.replace('\n','')
        line=line.replace('T','0')
        line=line.replace('M','1')
        pizza[row][:]=[char for char in line]

    f.close()
    
    print("-------------------------------------------")
    print("OUR PIZZA HAS THE FOLLOWING CHARACTERISTICS")
    print("-------------------------------------------")
    print("Cell Rows: " + str(rSize))
    print("Cell Colums: " + str(cSize))
    print("Number of Ingredients: " + str(noOfIngredients) )
    print("Min number of each ingredient: " + str(minItem))
    print("Max Cells/Slice: " + str(maxCells))
    
    print("AND OUR GLORIOUS PIZZA")
    print(pizza)
    
    
    return minItem, maxCells, pizza, rSize, cSize
    

minItem,maxCells,pizza,R,C=read_input()
if maxCells%2!=0:
    maxCells=maxCells-1
possible_comps=range(2*minItem,maxCells+1)
listA=[]
for size in possible_comps:
    a=1
    if size%2!=0:
        continue
    while a<=size:
        b=int(size/a)
        if a*b==size:
            listA.append([a,b])
        a=a+1
        
import numpy

eaten_pizza=zeros(R*C).reshape(R,C)
r1=0
r2=0
c1=0
c2=0

SLICES=[]

x=0
y=0
while x<=R-1:
    while y<=C-1:       

        if eaten_pizza[x,y]==1:
            y=y+1
            continue
        #print (x,y)
        for size in listA:
            #print(size)
            r1=x
            r2=x+size[0]-1
            c1=y
            c2=y+size[1]-1
            #none of the cells has already been used
            #the slise has at least numItem of Ts
            #the slice has at least numItems of Ms
            if r2>R-1 or c2>C-1:
                #print('out of bound')
                continue
            
            curr_eaten=sum(sum(eaten_pizza[r1:r2+1,c1:c2+1]))
            curr_pizza=sum(sum(pizza[r1:r2+1,c1:c2+1]))
            counter=numpy.where(curr_pizza==0)
            counter=len(counter[0][:])
            
            if curr_eaten == 0 and \
                  curr_pizza >= minItem and \
                      curr_pizza <= ((size[0]*size[1])-minItem):
                      #counter >= minItem:    
                             flag=1
                             SLICES.append([r1,c1,r2,c2])
                             #eaten_pizza[r1:r2,c1:c2]=ones(size[0]*size[1]).reshape(size[0],size[1])
                             eaten_pizza[r1:r2+1,c1:c2+1]=1
                             #print('found a slice')           
                             break           
        y=y+1
    x=x+1
    y=0  

A=sum(sum(eaten_pizza))
B=R*C

results=[[len(SLICES)]] + SLICES

import csv
export_file= file + '.csv'
with open(export_file, 'w', newline='') as fp:
    a = csv.writer(fp, delimiter=' ')
    a.writerows(results)

print('\n' + str(A) +' out of ' + str(B) + ' used.')  