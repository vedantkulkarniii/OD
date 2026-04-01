
# *7. Geometry Tool *
# 📌 Question:
# Creating a geometry tool: Implement method overloading in a class Shape to calculate the area of a circle, rectangle, and triangle based on different parameters. Then, use method overriding in a derived class 3DShape to calculate the volume of a sphere, cylinder, and cone.

# 📖 Explanation:
# Overloading using parameters; overriding in derived class.

class Shape:
    def area(self, a, b=None):
        if b is None:
            return 3.14*a*a      # circle
        else:
            return a*b           # rectangle

    def triangle(self, b,h):
        return 0.5*b*h

class Shape3D(Shape):
    def area(self, r):
        return (4/3)*3.14*r**3   # overriding

    def cylinder(self, r,h):
        return 3.14*r*r*h

    def cone(self, r,h):
        return (1/3)*3.14*r*r*h

s = Shape()
print("Circle:", s.area(5))
print("Rectangle:", s.area(5,4))
print("Triangle:", s.triangle(4,5))

s3 = Shape3D()
print("Sphere:", s3.area(3))
print("Cylinder:", s3.cylinder(3,5))
print("Cone:", s3.cone(3,5))
