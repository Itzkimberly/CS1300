# Step-by-step assignment demonstration
# Assignment 1: Create object 42, bind name 'x' to it
x = 42
print(f"x = {x}")
print(f"x points to object at: {id(x)}")
# Assignment 2: Create object 100, bind name 'y' to it

y = 100
print(f"y = {y}")
print(f"y points to object at: {id(y)}")

# Assignment 3: Bind name 'z' to the SAME object as x
z = x
print(f"z = {z}")
print(f"z points to object at: {id(z)}")
print(f"x and z same object? {id(x) == id(z)}") # True!

