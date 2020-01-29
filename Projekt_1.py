import numpy as np
import math

class Vector2D():
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def display(self):
        print("x="+str(self.x)+", y="+str(self.y))
  
    def add(self, other):
        self.x = self.x + other.x
        self.y = self.y + other.y
        
    def substr(self, other):
        self.x = self.x - other.x
        self.y = self.y - other.y
        
    def multByNumber(self, a):
        self.x = a*self.x
        self.y = a*self.y
        
    def dotProd(self, other):
        return self.x*other.x + self.y*other.y 
    
    def rotate(self, alfa):
        alfaDeg = alfa*math.pi/180
        sinus = math.sin(alfaDeg)
        cosinus = math.cos(alfaDeg)
        x = self.x
        y = self.y       
        self.x = x*cosinus - y*sinus
        self.y = x*sinus + y*cosinus
        
    def modulus(self):
        return (self.x**2 + self.y**2)**0.5
    
    def opposite(self):
        self.x = -self.x
        self.y = -self.y
        
