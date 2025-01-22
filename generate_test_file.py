import numpy as np
import pandas as pd

# Define the number of points in the point cloud
num_points = 100

# Generate random coordinates for x, y, z within a given range
x = np.random.uniform(-10, 10, num_points)
y = np.random.uniform(-10, 10, num_points)
z = np.random.uniform(-10, 10, num_points)

# Generate random sizes for each point
lj = np.random.uniform(0.1, 5.0, num_points)

# Combine the data into a pandas DataFrame
data = pd.DataFrame({
    'x': x,
    'y': y,
    'z': z,
    'lj': lj
})

# Save the data to a CSV file
data.to_csv('data/pointcloud.csv', index=False)

print("Point cloud with x, y, z, lj has been created and saved to 'pointcloud.csv'.")
