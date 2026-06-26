# WRSN Wireless Charging Optimization Research

## Overview
Hybrid approach combining Clustering, PSO, and Priority Scheduling 
for wireless sensor network charging optimization.

## Problem
- Wireless Rechargeable Sensor Networks (WRSNs) need efficient charging
- Paper's SIGN algorithm: 95% survival, 8 MCVs (500 nodes)
- Goal: Same/better survival with FEWER MCVs

## Solution
4-step hybrid approach:
1. **Clustering** - Divide area into zones
2. **PSO** - Optimize charging sequence
3. **Priority Scheduling** - Charge urgent nodes first
4. **Adaptive Learning** - Improve over iterations

## Results
- Using exact parameters from paper
- Hybrid approach achieves better efficiency
- Aiming for 37% fewer MCVs

## Files
- `code/` - Python implementation
- `results/` - Test results and graphs
- `docs/` - Documentation
- `papers/` - Research papers

## Usage
```bash
python3 code/comparison.py
```

## Author
Santiago Jerald
SRM University-AP, NIT Goa Research Internship

## Based On
"Enhancing WRSN Sustainability Through On-Demand Directional 
Wireless Charging With Multiple Green-Powered Mobile Vehicles"
by Xiongbo Ma et al. (2025)
