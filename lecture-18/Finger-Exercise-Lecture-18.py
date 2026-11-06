class Circle():
    def __init__(self, radius):
        """ Initializes self with radius """
        # your code here
        self.radius = radius

    def get_radius(self):
        """ Returns the radius of self """
        # your code here
        return self.radius

    def __add__(self, c):
        """ c is a Circle object 
        Returns a new Circle object whose radius is 
        the sum of self and c's radius """
        # your code here
        return Circle(self.radius + c.radius)

    def __str__(self):
        """ A Circle's string representation is the radius """
        # your code here
        return str(self.radius)
    

c1 = Circle(5)
c2 = Circle(10)

add = c1 + c2
# print(Circle.__add__(c1, c2))
# print(add)
print(add.get_radius())
    
# # Test 1: Creating Circle objects
# c1 = Circle(5)
# c2 = Circle(10)

# # Test 2: get_radius()
# print(c1.get_radius())       # Expected: 5
# print(c2.get_radius())       # Expected: 10

# # Test 3: __str__()
# print(c1)                    # Expected: 5
# print(c2)                    # Expected: 10

# # Test 4: __add__()
# c3 = c1 + c2
# print(c3)                    # Expected: 15

# # Test 5: Check the returned object's type
# print(type(c3))              # Expected: <class '__main__.Circle'>

# # Test 6: Check the new object's radius
# print(c3.get_radius())       # Expected: 15

# # Test 7: Adding a Circle to itself
# c4 = c1 + c1
# print(c4)                    # Expected: 10

# # Test 8: Check original objects remain unchanged
# print(c1)                    # Expected: 5
# print(c2)                    # Expected: 10