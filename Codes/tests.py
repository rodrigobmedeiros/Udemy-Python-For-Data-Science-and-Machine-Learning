# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 18:08:08 2020

@author: Rodrigo Bernardo Medeiros
"""


numero = 1000
numero_str = str(numero)
count=0

for i in range(1000,10000):
    
    numero_str = str(i)
    if i%5==0 and i%7==0 and int(numero_str[-1])==0:
        
        count +=1
    
    
    
print(count)