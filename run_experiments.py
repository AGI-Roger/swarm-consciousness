"""
Experiment Runner for Swarm Consciousness Studies
=================================================

This script runs the baseline and scaling experiments described in the manuscript.
"""

import argparse
from swarm_simulation import SwarmSimulation
import json
import os

def run_baseline_experiments():
    """Run baseline comparison experiments."""
    print("\n" + "="*60)
    print("BASELINE EXPERIMENTS")
    print("="*60)
    
    conditions = {
        'standard': {'n_agents': 50, 'n_timesteps': 2000},
        'random': {'n_agents': 50, 'n_timesteps': 2000},
        'boids': {'n_agents': 50, 'n_timesteps': 2000},
        'greedy': {'n_agents': 50, 'n_timesteps': 2000}
    }
    
    results = {}
    
    for name, config in conditions.items():
        print(f"\nRunning {name} condition...")
        sim = SwarmSimulation(n_agents=config['n_agents'])
        metrics = sim.run(n_timesteps=config['n_timesteps'])
        results[name] = metrics
        
        # Save results
        os.makedirs('data', exist_ok=True)
        with open(f'data/baseline_{name}.json', 'w') as f:
            json.dump(metrics, f, indent=2)
    
    print("\n✅ Baseline experiments complete!")
    return results

def run_scaling_experiments():
    """Run complexity scaling experiments."""
    print("\n" + "="*60)
    print("SCALING EXPERIMENTS")
    print("="*60)
    
    swarm_sizes = [20, 50, 100, 200]
    results = {}
    
    for size in swarm_sizes:
        print(f"\nRunning swarm size: {size} agents...")
        sim = SwarmSimulation(n_agents=size)
        metrics = sim.run(n_timesteps=1000)
        results[f'size_{size}'] = metrics
        
        # Save results
        os.makedirs('data', exist_ok=True)
        with open(f'data/scaling_{size}.json', 'w') as f:
            json.dump(metrics, f, indent=2)
    
    print("\n✅ Scaling experiments complete!")
    return results

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run swarm consciousness experiments')
    parser.add_argument('--experiment', choices=['baseline', 'scaling', 'all'],
                       default='all', help='Which experiment to run')
    
    args = parser.parse_args()
    
    if args.experiment in ['baseline', 'all']:
        run_baseline_experiments()
    
    if args.experiment in ['scaling', 'all']:
        run_scaling_experiments()
    
    print("\n" + "="*60)
    print("ALL EXPERIMENTS COMPLETE!")
    print("="*60)
    print("\nResults saved in data/ directory")
