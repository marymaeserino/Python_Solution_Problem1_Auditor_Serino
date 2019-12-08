# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 21:46:26 2019

@author: Mary Mae
"""

#Importing libraries
import matplotlib.pyplot as plt

def f(n):
    if n <= 9: #First condition where n is less than or equal to 9
       return ((n**2) - 7)
    return f(n - 10) #Second condition where n is reduced by 10 if n>9; returns the main function f(n)
def X(): #New main function
#Empty arrays for the x and y values
    x = [] 
    y = [] 
    
    for i in range(1, 100): #Value of n is ranged from 0 to 99
        x.append(i) #Appending the values of m t array x
        y.append(f(i)) #Appending the values of f(i) to array y
        
        print(x) #Output value of x
        print(y) #Output value of y
        plt.stem(x, y,use_line_collection=True) #Plot the function using stem
        plt.xlabel('x - axis') #Label the x-axis
        plt.ylabel('y - axis') #Label tbe y-axis
        plt.title('The Graph for f(n) ') #Shows the title of the graph



    

