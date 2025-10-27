"""
Emergent Consciousness in Artificial Swarms - Main Simulation
==============================================================

This module implements the core agent-based swarm simulation for studying
emergent consciousness-like properties in artificial systems.

Author: [Your Name]
Date: 2025
License: MIT
"""

import numpy as np
from typing import List, Dict, Tuple
import time

class SwarmSimulation:
    """
    Main simulation class for artificial swarm experiments.
    
    Parameters
    ----------
    n_agents : int
        Number of agents in the swarm (20-200)
    grid_size : tuple
        Size of 2D toroidal grid (default: 50x50)
    random_seed : int
        Random seed for reproducibility (default: 42)
    """
    
    def __init__(self, n_agents: int = 50, grid_size: Tuple[int, int] = (50, 50), 
                 random_seed: int = 42):
        self.n_agents = n_agents
        self.grid_size = grid_size
        self.random_seed = random_seed
        np.random.seed(random_seed)
        
        # Initialize agents
        self.agents = []
        self.initialize_agents()
        
        # Initialize environment
        self.resources = []
        self.obstacles = []
        self.threats = []
        self.initialize_environment()
        
        # Tracking
        self.timestep = 0
        self.metrics_history = []
        
    def initialize_agents(self):
        """Initialize agent population with random positions and velocities."""
        for i in range(self.n_agents):
            position = np.random.rand(2) * self.grid_size[0]
            velocity = np.random.randn(2) * 0.5
            agent = {
                'id': i,
                'position': position,
                'velocity': velocity,
                'energy': 100.0,
                'memory': [],
                'signals_received': 0
            }
            self.agents.append(agent)
    
    def initialize_environment(self):
        """Set up resources, obstacles, and threats."""
        # Resources scale with agent count
        n_resources = max(int(self.n_agents * 0.8), 5)
        for _ in range(n_resources):
            pos = np.random.rand(2) * self.grid_size[0]
            self.resources.append({'position': pos, 'value': 35.0})
        
        # 25 obstacles
        for _ in range(25):
            pos = np.random.rand(2) * self.grid_size[0]
            self.obstacles.append({'position': pos, 'radius': 2.0})
        
        # 2 threats
        for _ in range(2):
            pos = np.random.rand(2) * self.grid_size[0]
            vel = np.random.randn(2) * 0.8
            self.threats.append({'position': pos, 'velocity': vel})
    
    def step(self):
        """Execute one simulation timestep."""
        self.timestep += 1
        
        # Update agents
        for agent in self.agents:
            if agent['energy'] > 0:
                self.update_agent(agent)
        
        # Update environment
        self.update_threats()
        
        # Compute metrics
        metrics = self.compute_metrics()
        self.metrics_history.append(metrics)
        
        return metrics
    
    def update_agent(self, agent: Dict):
        """Update single agent state."""
        # Energy decay
        agent['energy'] -= 0.25
        
        # Movement logic here (simplified)
        agent['position'] += agent['velocity']
        
        # Wrap toroidal boundaries
        agent['position'] = agent['position'] % self.grid_size[0]
    
    def update_threats(self):
        """Update threat positions."""
        for threat in self.threats:
            threat['position'] += threat['velocity']
            threat['position'] = threat['position'] % self.grid_size[0]
    
    def compute_metrics(self) -> Dict:
        """Compute consciousness proxy metrics."""
        active_agents = [a for a in self.agents if a['energy'] > 0]
        n_active = len(active_agents)
        
        if n_active == 0:
            return {
                'information_flow': 0.0,
                'group_coherence': 0.0,
                'behavioral_diversity': 0.0,
                'exploitation_efficiency': 0.0,
                'consciousness_score': 0.0
            }
        
        # Information flow (simplified)
        info_flow = sum(1 for a in active_agents if a['signals_received'] > 0) / n_active
        
        # Group coherence (simplified)
        velocities = np.array([a['velocity'] for a in active_agents])
        coherence = 1.0 - np.mean(np.std(velocities, axis=0))
        coherence = max(0, min(1, coherence))
        
        # Behavioral diversity (simplified)
        diversity = 0.5  # Placeholder
        
        # Exploitation efficiency (simplified)
        exploitation = 0.8  # Placeholder
        
        # Composite consciousness score
        consciousness = (info_flow + coherence + diversity + exploitation) / 4.0
        
        return {
            'timestep': self.timestep,
            'information_flow': info_flow,
            'group_coherence': coherence,
            'behavioral_diversity': diversity,
            'exploitation_efficiency': exploitation,
            'consciousness_score': consciousness,
            'n_active': n_active
        }
    
    def run(self, n_timesteps: int = 1000) -> List[Dict]:
        """
        Run simulation for specified timesteps.
        
        Parameters
        ----------
        n_timesteps : int
            Number of timesteps to simulate
            
        Returns
        -------
        metrics_history : list
            List of metric dictionaries for each timestep
        """
        print(f"Running simulation: {self.n_agents} agents, {n_timesteps} timesteps")
        start_time = time.time()
        
        for t in range(n_timesteps):
            self.step()
            
            if (t + 1) % 100 == 0:
                print(f"  Timestep {t+1}/{n_timesteps}")
        
        elapsed = time.time() - start_time
        print(f"Simulation complete in {elapsed:.2f} seconds")
        
        return self.metrics_history


if __name__ == "__main__":
    # Example usage
    print("Emergent Consciousness Simulation - Example Run")
    print("=" * 50)
    
    sim = SwarmSimulation(n_agents=50, random_seed=42)
    results = sim.run(n_timesteps=100)
    
    print(f"\nFinal consciousness score: {results[-1]['consciousness_score']:.3f}")
    print(f"Final information flow: {results[-1]['information_flow']:.3f}")
