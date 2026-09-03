import math
import fractions
from decimal import Decimal, getcontext

getcontext().prec = 100

def calc_discrete_pi_2d(r):
    # 1. Define Hardware Boundaries (Orthotropic Constraint)
    A = 4 * r - 1  # Minor axis
    B = 4 * r + 1  # Major axis
    
    # 2. Lattice Point Count via Integer Math
    AB_sq = (A * B)**2
    max_x_y0 = A // 2
    total_points = (2 * max_x_y0) + 1
    
    count = 0
    max_y = B // 2
    for y in range(1, max_y + 1):
        rem = AB_sq - (2 * y * A)**2
        if rem >= 0:
            max_x = math.isqrt(rem) // (2 * B)
            count += (2 * max_x) + 1
            
    total_points += 2 * count
    
    # 3. Rational Fraction Extraction
    numerator = total_points * 4
    denominator = A * B
    exact_fraction = fractions.Fraction(numerator, denominator)
    decimal_expansion = Decimal(numerator) / Decimal(denominator)
    
    return exact_fraction, decimal_expansion, total_points, A, B

# Example Audit Execution
r_val = 2000
fraction, dec_pi, points, minor, major = calc_discrete_pi_2d(r_val)
print(f"Radius (r)       : {r_val:,}")
print(f"Lattice Points   : {points:,}")
print(f"Exact Fraction   : {fraction.numerator:,} / {fraction.denominator:,}")
print(f"100-Digit Decimal: {dec_pi}")
