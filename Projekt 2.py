import numpy as np
import math

        
class Vector3D():
    
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def display(self):
        print("x="+str(self.x)+", y="+str(self.y) + ", z=" + str(self.z))
        
    def add(self, other):
        self.x = self.x + other.x
        self.y = self.y + other.y
        self.z = self.z + other.z
        
    def substr(self, other):
        self.x = self.x - other.x
        self.y = self.y - other.y
        self.z = self.z - other.z
        
    def multByNumber(self, a):
        self.x = a*self.x
        self.y = a*self.y
        self.z = a*self.z
        
    def dotProd(self, other):
        return self.x*other.x + self.y*other.y + self.z*other.z
        
    def crossProd(self, other):
        new_x = self.y*other.z - self.z*other.y
        new_y = self.z*other.x - self.x*other.z
        new_z = self.x*other.y - self.y*other.x
        
        return Vector3D(new_x, new_y, new_z)
    
    def modulus(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5
        
    def opposite(self):
        self.x = -self.x
        self.y = -self.y
        self.z = -self.z
        
        