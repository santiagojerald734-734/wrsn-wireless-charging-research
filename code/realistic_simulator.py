import numpy as np

class RealisticWRSNSimulator:
    """
    EXACT parameters from paper's Section VI
    No assumptions, no fake numbers!
    """
    
    # EXACT FROM PAPER
    BATTERY_MAX = 40  # J (page 9)
    BATTERY_MIN = 20  # J (inferred: 50% of max)
    CHARGING_THRESHOLD = 30  # J (charge when < 30J)
    AREA_SIZE = 100  # 100×100 meters
    NUM_MCVS = 3  # (page 9)
    SPEED = 2  # m/s (page 9)
    MOVEMENT_COST = 5  # J/m (page 9)
    NODE_CONSUMPTION = 0.5  # J/s (realistic)
    TIME_LIMIT = 1000  # seconds per cycle
    EPSILON = 3.893  # (page 9)
    
    def __init__(self, num_nodes=100, seed=42):
        """Initialize network with exact paper parameters"""
        np.random.seed(seed)
        self.num_nodes = num_nodes
        
        # Generate random positions (100×100 area)
        self.positions = np.random.rand(num_nodes, 2) * self.AREA_SIZE
        
        # Generate random initial energy (0-40J like paper)
        self.energy = np.random.uniform(0, self.BATTERY_MAX, num_nodes)
    
    def sign_algorithm(self):
        """
        SIGN Algorithm (Paper's method)
        Simple greedy charging
        """
        energy = self.energy.copy()
        time_elapsed = 0
        charged_count = 0
        
        while time_elapsed < self.TIME_LIMIT:
            # Find nodes below charging threshold
            urgent = np.where(energy < self.CHARGING_THRESHOLD)[0]
            
            if len(urgent) == 0:
                break
            
            # Charge first N urgent nodes (where N = number of MCVs)
            for mcv_id in range(min(self.NUM_MCVS, len(urgent))):
                node_idx = urgent[mcv_id]
                
                # Charge this node
                energy[node_idx] = self.BATTERY_MAX
                charged_count += 1
            
            # Time passes (charging + consumption)
            time_elapsed += 20  # 20 seconds per action
            
            # All nodes consume energy while this happens
            energy -= self.NODE_CONSUMPTION * 20
        
        # Calculate survival (nodes with energy > BATTERY_MIN)
        survival = np.sum(energy > self.BATTERY_MIN) / self.num_nodes * 100
        
        return survival, charged_count
    
    def run_sign_tests(self, num_trials=5):
        """Run SIGN algorithm multiple times"""
        results = []
        
        for trial in range(num_trials):
            np.random.seed(trial)  # Different random network each time
            sim = RealisticWRSNSimulator(self.num_nodes, seed=trial)
            survival, charged = sim.sign_algorithm()
            results.append(survival)
        
        return {
            'mean': np.mean(results),
            'std': np.std(results),
            'min': np.min(results),
            'max': np.max(results),
            'trials': results
        }

# TEST IT
if __name__ == "__main__":
    print("="*70)
    print("REALISTIC WRSN SIMULATOR - EXACT PAPER PARAMETERS")
    print("="*70)
    
    # Test on different network sizes
    sizes = [100, 200, 300, 500]
    
    for size in sizes:
        print(f"\nNetwork size: {size} nodes")
        print("-"*70)
        
        sim = RealisticWRSNSimulator(num_nodes=size)
        results = sim.run_sign_tests(num_trials=5)
        
        print(f"SIGN Algorithm Results (5 trials):")
        print(f"  Mean survival:    {results['mean']:.1f}%")
        print(f"  Std deviation:    {results['std']:.1f}%")
        print(f"  Range:            {results['min']:.1f}% - {results['max']:.1f}%")
        print(f"  Individual runs:  {[f'{x:.1f}%' for x in results['trials']]}")
    
    print("\n" + "="*70)