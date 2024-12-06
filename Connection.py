import math


def calculate_beam_and_tower_stresses(load_parallel, bolt_spacing, num_bolts_per_side, thickness_tower, width_tower):
    # Constants
    modulus_elasticity = 29732700  # Elastic modulus of 1040 steel in psi

    # Load distribution
    total_bolts = num_bolts_per_side * 2  # Bolts on both sides of the beam
    shear_force_per_bolt = load_parallel / total_bolts

    # Stress on bolts
    area_bolt = math.pi * (3 / 8) ** 2 / 4  # Cross-sectional area of a 3/4" bolt in square inches
    stress_per_bolt = shear_force_per_bolt / area_bolt

    # Shear stress on the tower
    effective_area_tower = thickness_tower * bolt_spacing * (
                num_bolts_per_side - 1)  # Area resisting shear at one connection
    stress_on_tower = load_parallel / (2 * effective_area_tower)  # Divide by 2 for both sides

    # Deflection of the tower
    moment_tower = load_parallel * (bolt_spacing / 2)  # Moment arm for the connection
    I_tower = width_tower * thickness_tower ** 3 / 12  # Moment of inertia for the tower section
    deflection_tower = ((moment_tower * bolt_spacing ** 2) / (
                2 * modulus_elasticity * I_tower))/2  # Divide by 2 for shared load

    return {
        "Shear_force_per_bolt (lbf)": shear_force_per_bolt,
        "Stress_per_bolt (psi)": stress_per_bolt,
        "Stress_on_tower (psi)": stress_on_tower,
        "Deflection_of_tower (in)": deflection_tower
    }


#inputs
load_parallel = 1508.65 * 12  # Load applied parallel to the tower in lb-in
bolt_spacing = 6  # Distance between bolts in inches
num_bolts_per_side = 4  # Bolts per connection side
thickness_tower = 5 / 16  # Thickness of the tower in inches
width_tower = 6  # Width of the tower section in inches

# Run the calculation
results = calculate_beam_and_tower_stresses(load_parallel, bolt_spacing, num_bolts_per_side, thickness_tower,
                                            width_tower)

# Print results
print(f"""
Results:
- Shear Force per Bolt: {results["Shear_force_per_bolt (lbf)"]:.2f} lbf
- Stress per Bolt: {results["Stress_per_bolt (psi)"]:.2f} psi
- Stress on Tower: {results["Stress_on_tower (psi)"]:.2f} psi
- Deflection of Tower: {results["Deflection_of_tower (in)"]:.2f} in
""")
