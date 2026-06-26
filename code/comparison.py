# Your Greedy Results (from previous code output)
greedy_results = {
    1: 100.0,
    3: 100.0,
    5: 100.0
}

# Paper's SIGN Algorithm Results (from Figure 7 in PDF)
# They tested with 500 nodes, 3 MCVs
sign_results = {
    100: 95.0,   # Estimated for 100 nodes
    500: 95.0    # From paper
}

# Baseline algorithms from paper
nn_results = {
    500: 82.3    # From Figure 7
}

map_results = {
    500: 92.8    # From Figure 7
}

print("\n" + "="*80)
print("COMPARISON: YOUR GREEDY vs PAPER'S ALGORITHMS")
print("="*80)

print("\n1. YOUR GREEDY ALGORITHM (100 nodes, 3 MCVs):")
print(f"   Survival Rate: {greedy_results[3]:.2f}%")

print("\n2. PAPER'S ALGORITHMS (500 nodes, 3 MCVs):")
print(f"   SIGN Algorithm: {sign_results[500]:.2f}%")
print(f"   MAP Algorithm: {map_results[500]:.2f}%")
print(f"   NN Algorithm: {nn_results[500]:.2f}%")

print("\n" + "="*80)
print("ANALYSIS:")
print("="*80)
print("""
✓ Your greedy achieves 100% with 100 nodes (simpler scenario)
✓ Paper's SIGN achieves 95% with 500 nodes (more complex)

Trade-off:
- Greedy: Simple, fast, but may not be optimal at scale
- SIGN: Complex algorithm, better optimized, handles larger networks

Next step: Implement Clustering + GA to improve on greedy
while staying simpler than SIGN
""")
print("="*80 + "\n")