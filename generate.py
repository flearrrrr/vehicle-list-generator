import os
import tkinter as tk
from tkinter import filedialog, messagebox

# Hide the main tkinter window
root = tk.Tk()
root.withdraw()

# Prompt the user to select the vehicle folder
folder_selected = filedialog.askdirectory(title="Select the Civ Cars folder (e.g., [Civ])")

if not folder_selected:
    print("❌ No folder selected. Exiting.")
    input("\nPress ENTER to close")
    exit()

vehicle_path = folder_selected
print(f"\n📁 Selected folder: {vehicle_path}")

# Output file for Lua vehicle list
output_file = os.path.join(vehicle_path, "vehicles_output.lua")

# Remove output file if it exists
if os.path.exists(output_file):
    os.remove(output_file)
    print("🗑️ Removed existing output file.")

# Get folders in selected directory
items = [f for f in os.listdir(vehicle_path) if os.path.isdir(os.path.join(vehicle_path, f))]

if not items:
    print("⚠ No folders found in selected directory!")
else:
    print(f"\n🚗 Scanning path: {vehicle_path}")
    print(f"📝 Will write to: {output_file}\n")

    for item in items:
        model = item
        name = model.upper()
        brand = "Dev Testing"
        price = 10000
        category = "imports"
        type_ = "automobile"
        shop = "luxury"
        lua_line = f"{{ model = '{model}', name = '{name}', brand = '{brand}', price = {price}, category = '{category}', type = '{type_}', shop = '{shop}' }},"

        with open(output_file, "a", encoding="utf-8") as f:
            f.write(lua_line + "\n")
        print(f"✔ Added: {model}")

    print("\n✅ Vehicle list generated successfully!")
    print(f"📄 Output saved to: {output_file}")

input("\nPress ENTER to exit")