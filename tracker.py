def calculate_macros(weight_kg, daily_protein_per_kg=2.2):
    return {"target_protein_g": round(weight_kg * daily_protein_per_kg, 1)}

if __name__ == "__main__":
    print("Macro Tracker initialized.")
