import math

def s(p, q, r):
    d = q**2 - 4*p*r

    if d > 0:
        x1 = (-q + math.sqrt(d)) / (2*p)
        x2 = (-q - math.sqrt(d)) / (2*p)
        return x1, x2
    elif d == 0:
        x = -q / (2*p)
        return x
    else:
        return None

def get_something(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid numeric value.")

d = get_something("Enter coefficient a: ")
e = get_something("Enter coefficient b: ")
f = get_something("Enter coefficient c: ")

roots = s(d, e, f)

if roots is None:
    print("No real roots exist.")
elif isinstance(roots, tuple):
    print("The quadratic equation has two distinct real roots:")
    print("Root 1:", roots[0])
    print("Root 2:", roots[1])
else:
    print("The quadratic equation has one repeated real root:")
    print("Root:", roots)
