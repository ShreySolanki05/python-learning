class Shapes:
    def __init__(self, name):
        self.name = name 
    def area(self):
        return 0 
class Rectangle(Shapes):
    def __init__(self,name,height,width ):
        super().__init__(name)
        self.height = height
        self.width = width 
    def area(self):
        return self.width * self.height
        
class Circle(Shapes):
    def __init__(self,name,radius):
        super().__init__(name)
        self.radius = radius
    def area(self):
        return 3.14159 * self.radius ** 2

r = Rectangle("rectangle",4,2)
print(r.name,r.area())
c = Circle("circle",3)
print(c.name,c.area())   