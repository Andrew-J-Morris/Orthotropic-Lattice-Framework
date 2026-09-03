import math
import fractions
from decimal import Decimal, getcontext

getcontext().prec = 100

def calc_discrete_pi_3d(r):
    A = 4 * r - 1  # Minor axis constraint
    B = 4 * r + 1  # Major axis constraint
    AB_sq = (A * B)**2
    
    total_points = 0
    max_z = B // 2  # Depth boundary
    
    # 3D Spatial Audit Loop (O(r^2) Row-Collapse Sweep)
    for z in range(-max_z, max_z + 1):
        rem_z0 = AB_sq - (2 * z * A)**2
        if rem_z0 < 0: 
            continue
            
        max_x_y0 = math.isqrt(rem_z0) // (2 * B)
        slice_points = (2 * max_x_y0) + 1
        
        max_y = B // 2
        count_y = 0
        for y in range(1, max_y + 1):
            rem = AB_sq - (2 * y * A)**2 - (2 * z * A)**2
            if rem >= 0:
                max_x = math.isqrt(rem) // (2 * B)
                count_y += (2 * max_x) + 1
                
        slice_points += 2 * count_y
        total_points += slice_points

    # Rational 3D Extraction Engine
    numerator = total_points * 6
    denominator = A * (B**2)
    exact_fraction = fractions.Fraction(numerator, denominator)
    decimal_expansion = Decimal(numerator) / Decimal(denominator)
    
    return total_points, exact_fraction, decimal_expansion

# Example Audit Execution
r_val = 2000
points, exact_frac, dec_expansion = calc_discrete_pi_3d(r_val)
print(f"3D Radius (r)    : {r_val:,}")
print(f"Lattice Points   : {points:,}")
print(f"Exact Fraction   : {exact_frac.numerator:,} / {exact_frac.denominator:,}")
print(f"Decimal Output   : {dec_expansion}")
