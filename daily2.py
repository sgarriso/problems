import random
import cv2
import numpy as np

img = np.zeros((400, 400, 3), dtype = "uint8") 
  
# Creating rectangle 
cv2.rectangle(img, (50, 50), (350, 350), (0, 255, 0), 1) 
cv2.circle(img, (200, 200), 150, (0, 255, 0), 1) 
cv2.imshow('dark', img)
cv2.waitKey(0)

def check(answer,guess):
    check = round(answer,3)
    return check - guess  != 0.0
def pointincircle(x,y):
    left = (x-200) ** 2 + (y - 200) ** 2
    right = (150  ** 2)
    return  left <  right
def findpi(guess  = 3.141):
    answer = 0
    total = 0
    inner = 0
    pairs = set()
    #pi = 4 * (inner / total)
    while check(answer,guess):
        while True:
            x = random.randint(50, 351)
            y = random.randint(50, 351)
            if (x,y) not in pairs:
                pairs.add((x,y))
                #print(pairs)
                total = total + 1
                break
        img[x][y] = [255,255,255]
        
        #cv2.imshow('dark', img)
        #cv2.waitKey(0)
          
        if pointincircle(x,y):
            inner = inner + 1
        answer =  4 * (inner / total)
        print(answer)
            
        
        
        
        
    return answer
print(findpi())
