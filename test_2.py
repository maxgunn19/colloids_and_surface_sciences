# --- Input Data ---
# All mass values are in grams (g)
# Density is in grams per cubic centimeter (g/cm^3)

# Mass of the dry sample in air
m_dry = 1.6292

# Apparent mass of the sample while suspended in water
m_suspended = 0.6523

# Mass of the sample after being soaked in water (saturated surface-dry condition)
m_saturated = 1.6305

# Density of the fluid (water)
rho_fluid = 0.99717

# --- Method 1: Simple 2-Weight Method (Incorrect for Porous Materials) ---

# This method calculates an "apparent volume" which does not account for open pores
# that fill with water, leading to an underestimation of the true volume.
v_apparent = (m_dry - m_suspended) / rho_fluid

# This results in an "apparent density," which is artificially high.
rho_apparent = m_dry / v_apparent

# --- Method 2: Correct 3-Weight Method (ASTM C20 Standard) ---

# This method calculates the true bulk volume by using the saturated mass.
# The buoyant force on the saturated sample accounts for the total volume boundary.
v_total = (m_saturated - m_suspended) / rho_fluid

# The bulk density is the true dry mass divided by the true total volume.
rho_bulk = m_dry / v_total

# --- Comparison of Results ---
print("--- Comparison of Density Measurement Methods ---")
print(f"Input Values:")
print(f"  - Dry Mass: {m_dry} g")
print(f"  - Suspended Mass: {m_suspended} g")
print(f"  - Saturated Mass: {m_saturated} g")
print("-" * 25)
print("Method 1: Simple 2-Weight Method (Apparent Density)")
print(f"  - Calculated Volume: {v_apparent:.4f} cm^3")
print(f"  - Resulting Density: {rho_apparent:.4f} g/cm^3")
print("-" * 25)
print("Method 2: Corrected 3-Weight Method (Bulk Density)")
print(f"  - Calculated Volume: {v_total:.4f} cm^3")
print(f"  - Resulting Density: {rho_bulk:.4f} g/cm^3")
print("-" * 25)

# --- Calculating Porosity ---
# The difference in volume between the two methods reveals the volume of the open pores
v_open_pores = v_total - v_apparent

# We can also calculate open pore volume from the mass gain during saturation
v_open_pores_from_mass = (m_saturated - m_dry) / rho_fluid

# Porosity is the ratio of pore volume to the total volume of the sample
porosity = (v_open_pores / v_total) * 100

print("Derived Porosity Information:")
print(f"  - Volume of Open Pores (from mass gain): {v_open_pores_from_mass:.4f} cm^3")
print(f"  - Percentage of Open Porosity: {porosity:.4f}%")