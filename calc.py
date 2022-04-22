def add(x, y):
    return x + y

def subtract(x,y):
    return x -y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y


class Rectangle:
    def __init__(self,width,length):
        self.width = width
        self.length = length

    def get_area(self):
        return self.width*self.length

    def set_width(self):
        return self.width
    
    def set_length(self):
        return self.length