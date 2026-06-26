import numpy as np
import matplotlib.pyplot as plt

# Step 1: Create 100 random sensor nodes
num_nodes = 100
positions = np.random.rand(num_nodes, 2) * 100  # 100x100 area
energy = np.random.rand(num_nodes) * 100        # 0-100 J battery

print("=== WRSN Charging Simulator ===")
print(f"Created {num_nodes} sensor nodes")
print(f"Area: 100 x 100 meters")
print(f"\nFirst 5 nodes:")
for i in range(5):
    print(f"  Node {i}: Position ({positions[i][0]:.1f}, {positions[i][1]:.1f}), Battery: {energy[i]:.1f} J")

# Step 2: Find urgent nodes (battery < 30 J)
urgent_nodes = np.where(energy < 30)[0]
print(f"\nUrgent nodes (battery < 30 J): {len(urgent_nodes)} out of {num_nodes}")

# Step 3: Simple charging - charge all urgent nodes fully
energy[urgent_nodes] = 100
survival_rate = (np.sum(energy > 20) / num_nodes) * 100

print(f"\nAfter charging urgent nodes:")
print(f"Survival rate: {survival_rate:.1f}%")
print(f"Nodes with battery > 20 J: {np.sum(energy > 20)}/{num_nodes}")  