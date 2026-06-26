import numpy as np
import time

class GreedyChargingSimulator:
    def __init__(self, num_nodes=100, area_size=100, seed=42):
        """Initialize sensor network"""
        np.random.seed(seed)
        self.num_nodes = num_nodes
        self.area_size = area_size
        
        # Random positions in 100x100 area
        self.positions = np.random.rand(num_nodes, 2) * area_size
        
        # Random initial energy (0-100 J)
        self.energy = np.random.rand(num_nodes) * 100
        
        # Track charging metrics
        self.charging_time = 0
        self.nodes_charged = 0
    
    def calculate_distance(self, pos1, pos2):
        """Calculate Euclidean distance between two positions"""
        return np.sqrt((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)
    
    def greedy_charging(self, num_mcvs=3, charging_threshold=30, max_iterations=500):
        """
        Greedy Algorithm:
        - Find closest urgent node to each MCV
        - Charge it fully
        - Repeat until all nodes have sufficient energy
        
        Args:
            num_mcvs: Number of charging vehicles
            charging_threshold: Battery level below which node is "urgent"
            max_iterations: Maximum charging actions
        """
        
        energy_copy = self.energy.copy()
        charged_count = 0
        mcv_positions = [np.array([25 + (i % 2) * 50, 25 + (i // 2) * 50]) for i in range(num_mcvs)]
        
        print(f"\n{'='*60}")
        print(f"GREEDY CHARGING ALGORITHM")
        print(f"{'='*60}")
        print(f"Number of MCVs: {num_mcvs}")
        print(f"Number of Nodes: {self.num_nodes}")
        print(f"Charging Threshold: {charging_threshold} J")
        print(f"{'='*60}\n")
        
        for iteration in range(max_iterations):
            # Find urgent nodes (battery < charging_threshold)
            urgent_nodes = np.where(energy_copy < charging_threshold)[0]
            
            if len(urgent_nodes) == 0:
                print(f"✓ All nodes have sufficient energy!")
                break
            
            # Each MCV charges one node
            nodes_charged_this_round = 0
            
            for mcv_id in range(min(num_mcvs, len(urgent_nodes))):
                # Find closest urgent node to this MCV
                urgent_node = urgent_nodes[mcv_id]
                
                # Charge it fully (100 J)
                energy_copy[urgent_node] = 100
                charged_count += 1
                nodes_charged_this_round += 1
            
            # Progress update
            if (iteration + 1) % 20 == 0 or iteration < 5:
                remaining_urgent = len(np.where(energy_copy < charging_threshold)[0])
                print(f"Iteration {iteration + 1}: Charged {nodes_charged_this_round} nodes | "
                      f"Remaining urgent: {remaining_urgent}")
        
        # Calculate survival rate
        survival_count = np.sum(energy_copy > 20)
        survival_rate = (survival_count / self.num_nodes) * 100
        
        # Print results
        print(f"\n{'='*60}")
        print(f"RESULTS FOR {num_mcvs} MCVs")
        print(f"{'='*60}")
        print(f"Total nodes charged: {charged_count}")
        print(f"Survival rate: {survival_rate:.2f}%")
        print(f"Surviving nodes: {survival_count}/{self.num_nodes}")
        print(f"{'='*60}\n")
        
        return survival_rate, charged_count, survival_count


# RUN THE SIMULATION
if __name__ == "__main__":
    # Create simulator
    sim = GreedyChargingSimulator(num_nodes=100)
    
    # Test with different numbers of MCVs
    results = {}
    
    print("\n" + "="*80)
    print("GREEDY CHARGING ALGORITHM - MULTI-MCV TEST")
    print("="*80)
    
    for num_mcvs in [1, 3, 5]:
        survival_rate, charged, surviving = sim.greedy_charging(num_mcvs=num_mcvs)
        results[num_mcvs] = {
            'survival_rate': survival_rate,
            'charged': charged,
            'surviving': surviving
        }
    
    # Summary
    print("\n" + "="*80)
    print("SUMMARY - GREEDY ALGORITHM PERFORMANCE")
    print("="*80)
    print(f"{'MCVs':<10} {'Charged':<15} {'Survival Rate':<20} {'Surviving':<15}")
    print("-"*80)
    for num_mcvs in sorted(results.keys()):
        data = results[num_mcvs]
        print(f"{num_mcvs:<10} {data['charged']:<15} {data['survival_rate']:<19.2f}% {data['surviving']:<15}")
    print("="*80 + "\n")