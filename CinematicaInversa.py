import numpy as np
import sympy
from sympy import simplify, cos, sin
from sympy.abc import x, y, theta, d

# a=theta + 1 + sin(x) + cos(y)


if __name__ == "__main__":
    a = sympy.symbols('a_1')
    d = sympy.symbols('d_3')
    xe = sympy.symbols('x_e')
    ye = sympy.symbols('y_e')
    t1 = sympy.symbols('theta_1')
    t2 = sympy.symbols('theta_2')
    xe = d * cos(t1) * cos(t2) - d * sin(t1) * sin(t2) + a * cos(t1)
    ye = d * cos(t2) * sin(t1) + d * cos(t1) * sin(t2) + a * sin(t1)
    xe2 = xe ** 2
    ye2 = ye ** 2
    suma = xe2 + ye2
    print(simplify(suma))


    part1 = (-d * sin(t1) * cos(t2) - d * cos(t1) * sin(t2) - a * sin(t1)) * (
            -d * sin(t1) * sin(t2) + d * cos(t1) * cos(t2)) + (
                    -d * cos(t1) * sin(t2) - d * sin(t1) * cos(t2)) * (sin(t1) * cos(t2) + cos(t1) * sin(t2)) + (
                    -d * cos(t1) * cos(t2) - d * sin(t1) * sin(t2) - a * cos(t1)) * (
                    cos(t1) * cos(t2) - sin(t1) * sin(t2))

    part2 = -(-d * sin(t1) * sin(t2) + d * cos(t1) * cos(t2)) * (cos(t1) * cos(t2) - sin(t1) * sin(t2)) - (
                -d * sin(t1) * cos(t2) - d * cos(t1) * sin(t2) - a * sin(t1)) * (
                        sin(t1) * cos(t2) + cos(t1) * sin(t2)) -(-d * cos(t1) * sin(t2) - d * sin(t1) * cos(t2)) * (
                        d * cos(t1) * cos(t2) - d * sin(t1) * sin(t2) + a + cos(t1))
    jacobiana = part1 + part2
    # print(jacobiana)
    jacobiana_simplified = simplify(jacobiana)
    print(jacobiana_simplified)
    expanded = sympy.factor(jacobiana)
    factorized = sympy.factor(jacobiana)
    print(expanded)
    print(factorized)
    trigsim = sympy.trigsimp(jacobiana)
    print(trigsim)


    # print(part1)
    # print(simplify(part1))
