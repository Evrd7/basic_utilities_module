import math

def greet_user_name(name):
    print(f"Hey {name}, nice to meet you!")


def calculate_area_of_circle(radius):
    print("Area of circle: " + str(math.pi * float(radius) ** 2))


def convert_celsius_to_fahrenheit(celsius):
    print(f"{float(celsius) * (9/5) + 32} °F")
