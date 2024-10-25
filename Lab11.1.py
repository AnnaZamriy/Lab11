import csv
import math

def func(x):
    return math.exp(x) + 0.1 * x**2

x1 = float(input("Введіть початок:"))
x2 = float(input("Введіть кінець:"))

filename = "func.csv"

with open(filename, "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["x", "f(x)"])
    
    x = x1
    while x <= x2:
        writer.writerow([x, func(x)])
        x += 1

