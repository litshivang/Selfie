import os
import shutil
import pandas as pd

# Read CSV file
df = pd.read_csv('G:/Selfie.csv')

# Path to the folder containing selfies
selfie_folder = 'G:/shivangPC/New folder/Selfies'

# Create a new folder to store organized images
output_folder = 'G:/Organized'
os.makedirs(output_folder, exist_ok=True)

# Get a list of already organized employees
organized_employees = set(os.listdir(output_folder))

# Iterate through the DataFrame and organize remaining images
for index, row in df.iterrows():
    employee_name = row['name']

    # Skip if employee is already organized
    if employee_name in organized_employees:
        print(f"Skipping {employee_name} as already organized.")
        continue

    # Check if filenames are not NaN
    if not pd.isna(row['in_selfie_file']):
        in_selfie_file = str(row['in_selfie_file'])
        in_selfie_src = os.path.join(selfie_folder, in_selfie_file)
        in_selfie_dst = os.path.join(output_folder, employee_name, in_selfie_file)

        # Create the destination directory if it doesn't exist
        os.makedirs(os.path.join(output_folder, employee_name), exist_ok=True)

        shutil.copy2(in_selfie_src, in_selfie_dst)

    if not pd.isna(row['out_selfie_file']):
        out_selfie_file = str(row['out_selfie_file'])
        out_selfie_src = os.path.join(selfie_folder, out_selfie_file)
        out_selfie_dst = os.path.join(output_folder, employee_name, out_selfie_file)

        # Create the destination directory if it doesn't exist
        os.makedirs(os.path.join(output_folder, employee_name), exist_ok=True)

        shutil.copy2(out_selfie_src, out_selfie_dst)

    print(f"Organized images for {employee_name}.")

print("Images organized successfully.")
