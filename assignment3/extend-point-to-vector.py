# Task 5: Extending a Class
import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, point):
        return self.x == point.x and self.y == point.y

    def euclidean(self, point):
        dx = self.x - point.x
        dy = self.y - point.y
        return math.sqrt(dx**2 + dy**2)
    
    def __str__(self):
        return f"Point({self.x}, {self.y})"
    

class Vector(Point):  # Inherits from Point
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
    # Override + operator
    def __add__(self, point):
        return Vector(self.x + point.x, self.y + point.y)
    

# Print the results of the classes
point1 = Point(5, 10)

print(f"point1: {point1}")

print(f"point1 x: {point1.x} point1 y: {point1.y}")

point2 = Point(3, 9)

print(f"Euclidean: {point1.euclidean(point2)}")

print(f"Are point1 and point2 equal: {point1.__eq__(point2)}")

vector1 = Vector(5, 7)

print(f"vector1: {vector1}")

print(f"vector1 x: {vector1.x} vector1 y: {vector1.y}")

vector2 = Vector(5, 7)

print(f"Euclidian: {vector1.euclidean(vector2)}")

print(f"Are vector1 and vector2 equal: {vector1.__eq__(vector2)}")

new_vector = vector1 + vector2

print(f"new_vector: {new_vector}")
