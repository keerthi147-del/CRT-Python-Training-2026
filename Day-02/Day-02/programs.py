# CRT Python Training - Day 02
# Date: 1 September 2026

# 1. Using sep attribute
print("a", "b", "c")
print("a", "b", "c", sep="*")


# 2. Using end attribute
print("a", end="*")
print("b", end="*")
print("c", end="*")
print()


# 3. Printing INDIA using multiple print() functions
print("I", end="-")
print("N", end="-")
print("D", end="-")
print("I", end="-")
print("A")


# 4. Using for loop with a string
name = "keerthi"

for temp in name:
    print(temp, end=" ")


# 5. Printing a character with sep
for x in "abc":
    print(x, x, sep="*")


# 6. Basic data types
string_value = "India"
integer_value = 12
float_value = 14.3
complex_value = 10 + 4j
boolean_value = True

print(string_value)
print(integer_value)
print(float_value)
print(complex_value)
print(boolean_value)


# 7. Boolean values
print(True + True)


# 8. Complex number
c = 10 + 4j

print(c)
print(c.real)
print(c.imag)
