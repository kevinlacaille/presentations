"""
This script extracts 10 random image URIs from the Vancouver NADIR dataset with altitudes between 78 and 82 meters.
It then generates a bash script to download the images from the URIs and writes the script to a file in a new batch directory.
The script also prints instructions on how to execute the bash script to download the images.
"""

import pandas as pd
import random
import os
import subprocess

# Load the CSV file
data = pd.read_csv('./data/vancouver_nadir.csv')

# Filter URIs with altitude between 78 and 82
filtered_data = data[(data['altitude'] >= 78) & (data['altitude'] <= 82)]

# Extract the URIs
image_uris = filtered_data['image_uri'].tolist()

# Check if there are enough URIs to sample from
if len(image_uris) < 10:
    raise ValueError(
        "Not enough image URIs with altitude between 78 and 82 to sample 10.")

# Select 10 random URIs
random_uris = random.sample(image_uris, 10)

# Determine the next batch number
batch_prefix = 'batch_'
base_dir = './data'
batch_dirs = [
    d for d in os.listdir(base_dir)
    if d.startswith(batch_prefix) and os.path.isdir(os.path.join(base_dir, d))
]
if batch_dirs:
    latest_batch_num = max(int(d[len(batch_prefix):]) for d in batch_dirs)
    next_batch_num = latest_batch_num + 1
else:
    next_batch_num = 0

batch_dir = os.path.join(base_dir, f"{batch_prefix}{next_batch_num:03d}")
os.makedirs(batch_dir)

# Generate the bash script content
bash_script_content = ""
for uri in random_uris:
    parts = uri.split('/')
    h3_hash = parts[-3]
    flight_id = parts[-2]
    filename = parts[-1]
    local_path = os.path.join(batch_dir, h3_hash, flight_id, filename)
    os.makedirs(os.path.dirname(local_path), exist_ok=True)
    bash_script_content += f"aws s3 cp {uri} {local_path} --profile kevin\n"

# Write the bash script to a file in the batch directory
bash_script_path = os.path.join(batch_dir, 'download_images.sh')
with open(bash_script_path, 'w') as f:
    f.write(bash_script_content)

# Change the permissions of the script to be executable
os.chmod(bash_script_path, 0o755)

print(
    f"Bash script '{bash_script_path}' generated successfully and made executable."
)
print(f"Images will be downloaded to the '{batch_dir}' directory.")

# To execute the download script manually
print(f"Run './{bash_script_path}' to download the images.")
