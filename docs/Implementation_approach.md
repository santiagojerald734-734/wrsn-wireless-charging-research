# Implementation Approach

## WHAT IS MY RESEARCH ABOUT?

I'm improving wireless sensor network charging by combining 
4 different optimization techniques.

---

## THE 5 CONCEPTS I'M USING

### 1. SIGN ALGORITHM (Paper's baseline method)
**What it does:**
- Looks at which nodes are dying (low battery)
- Sends 3 MCVs to charge the most urgent ones
- Cycles repeatedly for 3000 seconds
- Charges as many nodes as possible

**Result:** ~72% of nodes survive

**My role:** This is the BASELINE. I need to beat this!

---

### 2. CLUSTERING (My improvement #1)
**What it does:**
- Divides the 100×100 meter area into 4 zones
- Each zone is 50×50 meters
- Each MCV focuses on only 1 zone
- No overlap, no wasted travel

**Why it helps:**
- Shorter distances between nodes in same zone
- Less time traveling = more time charging
- MCVs work efficiently in parallel

**Expected benefit:** 5-10% better survival

---

### 3. PSO - Particle Swarm Optimization (My improvement #2)
**What it does:**
- Tries 20 different charging ORDERS
- Order = which node to charge first, second, third...
- Tests each order and calculates survival rate
- Picks the order that gives BEST survival

**Why it helps:**
- Random charging order = suboptimal
- Smart order = more nodes survive
- PSO finds the smart order automatically

**Expected benefit:** 5-10% better survival

---

### 4. PRIORITY SCHEDULING (My improvement #3)
**What it does:**
- Sorts nodes by urgency (battery level)
- Charges DYING nodes first (5% battery = highest priority)
- Charges healthy nodes last (80% battery = lowest priority)
- This prevents nodes from dying while waiting

**Why it helps:**
- Without priority: Healthy nodes get charged first, dying ones die
- With priority: Dying nodes rescued, more survive
- Simple but effective

**Expected benefit:** 5-10% better survival

---

### 5. ADAPTIVE LEARNING (My improvement #4)
**What it does:**
- Runs the charging cycle multiple times
- After each run, learns what worked best
- Uses this knowledge in next run
- Each run = better than previous

**Why it helps:**
- Run 1: Try random strategies = 82% survival
- Run 2: Learn from Run 1, try better strategies = 85% survival
- Run 3: Learn from Run 2, try even better = 87% survival
- Run 4: Keep improving = 88% survival

**Expected benefit:** 5-10% better survival

---

## MY HYBRID APPROACH

**Combining all 4:**
