# -*- coding: utf-8 -*-
"""
Created on Mon May 11 19:57:50 2020

@author: BİLAL
Color-Blind-"T"este

ColorBlind 1.0
Family tree color-blind basic test.
Maybe, i will color-blind update.

"""
x = int(input("Female : "))
y = int(input("Male : "))

def colorBlind(x,y):
    #rr = 0
    #Rr = 1
    #RR = 2
    print("""
          0 = Diseased
          1 = Disease Carrier
          2 = Healthy
          """)
    if x == 0 and y == 2:
        print("\n%50 Diseased %50 Disease Carrier")
    elif x == 1 and y == 2:
        print("\n%25 Diseased %25 Disease Carrier %50 Healthy  ")
    elif x == 1 and y == 0:
        print("\n%25 Diseased %25 Disease Carrier %50 Healthy  ")    
    elif x == 2 and y == 0:
        print("\n%50 Disease Carrier %50 Healthy")  
    elif x == 2 and y == 2:
        print("\n%100 Healthy")
    elif x == 0 and y == 0:
        print("\n%100 Diseased")
    else:
        print("Error")
    return x,y    

print(colorBlind(x, y))        


