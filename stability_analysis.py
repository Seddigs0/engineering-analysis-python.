import math
import matplotlib.pyplot as plt


def factor_of_safety(cohesion, friction_angle_deg, unit_weight, slope_angle_deg, height):
    """
    Computes a simplified factor of safety for a slope.
    
    Parameters:
    cohesion (kPa)
    friction_angle_deg (degrees)
    unit_weight (kN/m^3)
    slope_angle_deg (degrees)
    height (m)

    using build in math function to set phi and beta angles to radian,
    and using them to get the resisting and driving forces of the slope, 
    so we can find the factor of safety. 
    """
    phi = math.radians(friction_angle_deg)
    beta = math.radians(slope_angle_deg)

    resisting = cohesion +(unit_weight * height * math.cos(beta)) * math.tan(phi)
    driving = unit_weight * height * math.sin(beta)

    return resisting/driving


# OUr parameters
cohesion = 20          # measured in kPa
unit_weight = 18       # kN/m^3
slope_angle = 35       # degrees
height = 10            # meters

#friction angle
friction_angles = list(range(20, 46, 2))
factors_of_safety = []

for phi in friction_angles:
    fos = factor_of_safety(cohesion, phi, unit_weight, slope_angle, height) #fos --> Factor of Saftey 
    factors_of_safety.append(fos)

# Results
print("Friction Angle (deg) | Factor of Safety")
print("---------------------|------------------")
for phi, fos in zip(friction_angles, factors_of_safety):
    print(f"{phi:>20} | {fos:.2f}")

# Plot results
plt.figure()
plt.plot(friction_angles, factors_of_safety)
plt.xlabel("Friction Angle (degrees)")
plt.ylabel("Factor of Safety")
plt.title("Slope Stability Sensitivity Analysis")
plt.grid(True)
plt.show()
