
# Input: lengths of three sides of a triangle
edge1 = float(input("Enter the length of the first side: "))
edge2 = float(input("Enter the length of the second side: "))
edge3 = float(input("Enter the length of the third side: "))

# Check the type of triangle
if edge1 == edge2 == edge3:
    print("The triangle is Equilateral (all sides are equal).")
elif edge1 == edge2 or edge1 == edge1 or edge2 == edge3:
    print("The triangle is Isosceles (two sides are equal).")
else:
    print("The triangle is Scalene (all sides are different).")
