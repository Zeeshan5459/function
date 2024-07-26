# Write a function call max_of_three that takes three parameters
# as input an returns the largest of the three. The function  
# use conditional statements to compare the values and 
# determine the greatest.

def max_of_three(x, y, z):
    if x >= y and x >= z:
        return x
    elif y >= x and y >= z:
        return y
    else:
        return z

print(max_of_three(50, 66, 90))