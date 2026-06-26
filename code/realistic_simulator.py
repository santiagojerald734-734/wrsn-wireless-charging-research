import numpy as np

class BetterWRSNSimulator:
    """
    WRSN Simulator - Mimics paper's SIGN algorithm
    Key insight: SIGN cycles repeatedly, charging nodes multiple times
    """
    
    # EXACT FROM PAPER
    BATTERY_MAX = 40  # J
    BATTERY_MIN = 5   # J (nodes die below this)
    CHARGING_THRESHOLD = 20  # J (charge when < 20J)
    AREA_SIZE = 100
    NUM_MCVS = 3
    SPEED = 2  # m/s
    MOVEMENT_COST = 5  # J/m
    NODE_CONSUMPTION = 0.2  # J/s (slow consumption)
    TIME_LIMIT = 3000  # seconds (IMPORTANT: longer cycle)
    EPSILON = 3.893
    
    def __init__(self, num_nodes=100, seed=42):
        np.random.seed(seed)
        self.num_nodes = num_nodes
        self.positions = np.random.rand(num_nodes, 2) * self.AREA_SIZE
        self.energy = np.random.uniform(15, self.BATTERY_MAX, num_nodes)
    
    def sign_algorithm_cyclical(self):
        """SIGN Algorithm - CYCLICAL VERSION"""
        energy = self.energy.copy()
        time_elapsed = 0
        dead_nodes = set()
        
        while time_elapsed < self.TIME_LIMIT:
            # Find alive nodes below threshold
            alive = np.where(energy > self.BATTERY_MIN)[0]
            urgent = alive[energy[alive] < self.CHARGING_THRESHOLD]
            
            if len(urgent) == 0:
                # No urgent nodes - but keep cycling
                energy[energy > self.BATTERY_MIN] -= self.NODE_CONSUMPTION * 10
                time_elapsed += 10
                newly_dead = np.where((energy <= self.BATTERY_MIN) & 
                                      (np.arange(self.num_nodes) not in dead_nodes))[0]
                dead_nodes.update(newly_dead)
                if len(alive) == len(dead_nodes):
                    break
                continue
            
            # Sort urgent by battery level (lowest first)
            urgent = urgent[np.argsort(energy[urgent])]
            
            # Charge with 3 MCVs in parallel
            for mcv_id in range(min(self.NUM_MCVS, len(urgent))):
                node_idx = urgent[mcv_id]
                energy[node_idx] = self.BATTERY_MAX
            
            # Time and consumption
            time_elapsed += 20
            energy[energy > self.BATTERY_MIN] -= self.NODE_CONSUMPTION * 20
            energy[energy < 0] = 0
            
            # Track dead nodes
            newly_dead = np.where((energy <= self.BATTERY_MIN) & 
                                  (np.arange(self.num_nodes) not in dead_nodes))[0]
            dead_nodes.update(newly_dead)
        
        # Survival = alive nodes
        alive = np.sum(energy > self.BATTERY_MIN)
        survival = (alive / self.num_nodes) * 100
        return survival
    
    def run_tests(self, num_trials=10):
        """Run multiple trials"""
        results = []
        for trial in range(num_trials):
            sim = BetterWRSNSimulator(self.num_nodes, seed=trial + 100)
            survival = sim.sign_algorithm_cyclical()
            results.append(survival)
        
        return {
            'mean': np.mean(results),
            'std': np.std(results),
            'min': np.min(results),
            'max': np.max(results),
            'trials': results
        }

# TEST
if __name__ == "__main__":
    print("="*80)
    print("BETTER WRSN SIMULATOR - CYCLICAL CHARGING")
    print("="*80)
    
    sizes = [100, 200, 300, 500]
    
    for size in sizes:
        print(f"\nNetwork size: {size} nodes")
        print("-"*80)
        
        sim = BetterWRSNSimulator(num_nodes=size)
        results = sim.run_tests(num_trials=10)
        
        print(f"SIGN Algorithm Results (10 trials):")
        print(f"  Mean survival:        {results['mean']:.1f}%")
        print(f"  Std deviation:        {results['std']:.1f}%")
        print(f"  Range:                {results['min']:.1f}% - {results['max']:.1f}%")
        print(f"  Individual runs:      {[f'{x:.1f}%' for x in results['trials']]}")
    
    print("\n" + "="*80)
