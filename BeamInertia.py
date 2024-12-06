# Define the initial parameters of the beam and material properties
import sympy as sp

# Constants
height_initial = 12  # Initial height of the beam in inches
width = 6  # Width of the beam in inches
thickness = 0.675  # Flange and web thickness in inches
yield_strength = 76870  # Yield strength in psi
bending_moment = 1508.65 * 12  # Maximum bending moment in lb-in
shear_force = 715.21  # Maximum shear force in lbf

# Reduction parameters
height_reduction_factor = 0.5  # Reduction by 50%
height_new = height_initial * height_reduction_factor

# Calculate initial and new moments of inertia
def moment_of_inertia(b, h, t):
    outer = b * h**3 / 12
    inner = (b - t) * (h - 2*t)**3 / 12
    return outer - inner

I_initial = moment_of_inertia(width, height_initial, thickness)
I_new = moment_of_inertia(width, height_new, thickness)

# Calculate maximum bending stress for initial and new designs
def bending_stress(M, c, I):
    return M * c / I

stress_bending_initial = bending_stress(bending_moment, height_initial / 2, I_initial)
stress_bending_new = bending_stress(bending_moment, height_new / 2, I_new)

# Calculate shear stress for initial and new designs
def shear_stress(V, I, t, b, h):
    Q = (b * h**2) / 8  # Approximation of Q for rectangular sections
    return V * Q / (I * t)

stress_shear_initial = shear_stress(shear_force, I_initial, thickness, width, height_initial)
stress_shear_new = shear_stress(shear_force, I_new, thickness, width, height_new)

# Combined stress
def combined_stress(bending_stress, shear_stress):
    return sp.sqrt(bending_stress**2 + shear_stress**2)

combined_stress_initial = combined_stress(stress_bending_initial, stress_shear_initial)
combined_stress_new = combined_stress(stress_bending_new, stress_shear_new)

# Calculate factors of safety
FoS_initial = yield_strength / combined_stress_initial
FoS_new = yield_strength / combined_stress_new

# Create a print statement for the given data
print(f"""
Moment of Inertia:
- Initial Moment of Inertia : {I_initial:.2f} in^4
- New Moment of Inertia : {I_new:.2f} in^4

Bending Stress:
- Initial Bending Stress : {stress_bending_initial:.2f} psi
- New Bending Stress : {stress_bending_new:.2f} psi

Shear Stress:
- Initial Shear Stress: {stress_shear_initial:.2f} psi
- New Shear Stress : {stress_shear_new:.2f} psi

Combined Stress:
- Initial Combined Stress : {combined_stress_initial:.2f} psi
- New Combined Stress : {combined_stress_new:.2f} psi

Factor of Safety:
- Initial Factor of Safety : {FoS_initial:.2f}
- New Factor of Safety : {FoS_new:.2f}
""")


