"""
demo_seed.py — One-click script to initialize ALL demo data.
Seeds categories, locations, inventory, and shopping list for development/demo.
"""

import subprocess

print("---- Pantry Manager Demo Data Seeding ----\n")

# List your seeders in order!
seeder_scripts = [
    "seed_categories.py",
    "seed_locations.py",
    "test_inventory_seed.py",
    "test_shoppinglist_seed.py"
]

for script in seeder_scripts:
    print(f"Running {script} ...")
    result = subprocess.run(["python", script], capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print(f"ERROR running {script}!\n{result.stderr}")
        break
else:
    print("✅ All demo data seeded successfully!")

print("\n----------- Done! -----------\n")