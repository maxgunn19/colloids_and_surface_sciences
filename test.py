def calculate_porosity(m_green, m_final, rho_composite, rho_material, rho_epoxy):
    """
    Calculates the remaining void volume and porosity of an infiltrated part.

    This function assumes that the volume of the binder in the green part is negligible.

    Args:
        m_green (float): The mass of the "green" part before infiltration (e.g., in grams).
        m_final (float): The mass of the final part after infiltration (e.g., in grams).
        rho_composite (float): The measured bulk density of the final composite part (e.g., in g/cm^3).
        rho_material (float): The theoretical density of the base build material (e.g., in g/cm^3).
        rho_epoxy (float): The density of the cured epoxy (e.g., in g/cm^3).

    Returns:
        dict: A dictionary containing the calculated 'void_volume' (in cm^3 or equivalent)
              and 'porosity_percentage'. Returns an error message if inputs are invalid.
    """
    # --- Input validation ---
    if not all(isinstance(arg, (int, float)) and arg > 0 for arg in [m_green, m_final, rho_composite, rho_material, rho_epoxy]):
        return {"error": "All inputs must be positive numbers."}
    if m_final <= m_green:
        return {"error": "Final mass must be greater than green mass."}

    # Step 1: Calculate the Total Volume of the Final Part
    v_total = m_final / rho_composite

    # Step 2: Calculate the Volume of the Base Material
    v_material = m_green / rho_material

    # Step 3: Calculate the Volume of the Infiltrated Epoxy
    v_epoxy = (m_final - m_green) / rho_epoxy

    # Step 4: Calculate the Remaining Void Volume
    v_voids = v_total - v_material - v_epoxy
    
    # Ensure void volume is not negative, which can happen with measurement errors
    if v_voids < 0:
        v_voids = 0

    # Step 5: Calculate the Void Percentage (Porosity)
    if v_total > 0:
        porosity_percentage = (v_voids / v_total) * 100
    else:
        porosity_percentage = 0


    return {
        "void_volume": v_voids,
        "porosity_percentage": porosity_percentage
    }

# --- Example Usage ---
if __name__ == "__main__":
    # --- Provide your data here ---
    # Sample data for a hypothetical stainless steel part
    # Units used: grams (g) and cubic centimeters (cm^3)
    
    mass_green_part = 1.0136                # Mass of the green part (before epoxy)
    mass_final_part = 1.64                  # Mass of the final part (after epoxy)
    density_composite_part = 1.6718         # Measured density of the final composite part
    density_base_material = 2.5             # Theoretical density of the base material 
    density_cured_epoxy = 1.08              # Density of the cured epoxy
    
    # --- Perform the calculation ---
    results = calculate_porosity(
        m_green=mass_green_part,
        m_final=mass_final_part,
        rho_composite=density_composite_part,
        rho_material=density_base_material,
        rho_epoxy=density_cured_epoxy
    )

    # --- Print the results ---
    if "error" in results:
        print(f"Error: {results['error']}")
    else:
        print("--- Porosity Calculation Results ---")
        print(f"Void Volume       : {results['void_volume']:.4f} cm^3")
        print(f"Porosity Percentage : {results['porosity_percentage']:.2f}%")