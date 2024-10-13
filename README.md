0x00. Python - Variable Annotations
Python, variable annotation is a feature that allows you to specify the expected data type of a variable

Syntax:
x: int = 10  # x is expected to be an integer
y: str = "Hello"  # y is expected to be a string
z: float  # z is expected to be a float (no value assigned yet)

def add(a: int, b: int) -> int:
    return a + b

examples
0. Write a type-annotated function add that takes a float a and a float b as arguments and returns their sum as a float.