# Rosalind Reference Solutions — Title Page
# Problem: INI2 —  	Variables and Some Arithmetic 
# Repository: Rosalind-Reference-Solutions

# Author: Ted Ngaleu
# Affiliation: NIA Postbac Fellow, Vascular Aging Biology Unit
# Created: 2025-09-15
# Last Updated: 2025-09-15
# License: MIT © 2025 Ted Ngaleu



# Problem:

# Given: Two positive integers a and b each less than 1000.
# Return: The integer corresponding to the square of the hypotenuse of the right triangle 
# whose legs have lengths a and b

# An integer is a whole number without a decimal point (e.g., -3, 0, 42).
# A floating-point number is a number with a decimal place (e.g., -2.5, 0.0, 99.99).

a = 951
b = 895

# In Python, the exponentiation operator is ** (e.g., 5**2), not ^.

# a^2 + b^2 = c^2 = a**2 + b**2 = c**2

a ** 2 + b ** 2 

# Set a variable for the hypotenuse_sqaured

hypotenuse_sqaure = a**2 + b**2

hypotenuse_sqaure