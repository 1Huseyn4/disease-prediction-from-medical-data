import os
from ucimlrepo import fetch_ucirepo

# Download dataset
heart_disease = fetch_ucirepo(id=45)

# Get original data
data = heart_disease.data.original

print("Dataset successfully downloaded!")
print("Shape:", data.shape)

# Create directory if it doesn't exist
os.makedirs("data/raw", exist_ok=True)

# Save dataset
data.to_csv("data/raw/heart_disease.csv", index=False)

print("Dataset saved successfully!")