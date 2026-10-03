"""Example script demonstrating how to use the leaver detection simulator."""

import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from simulator import LeaverDetectionSimulator


def main():
    """Run example simulation."""
    print("Leaver Detection Simulator - Example Run")
    print()

    # Create simulator instance
    simulator = LeaverDetectionSimulator(output_dir="../data")

    # Run full simulation
    # Adjust these numbers to simulate more or fewer users
    results = simulator.run_full_simulation(
        num_normal=20,  # Normal users
        num_leavers=5   # Potential leavers
    )

    # Print results summary
    print("\n" + "="*60)
    print("RESULTS SUMMARY")
    print("="*60)
    print(f"Total Users Simulated: {results['total_users']}")
    print(f"Potential Leavers Detected: {len(results['detections'])}")
    print()

    if results['detections']:
        print("Top 3 High-Risk Users:")
        for i, detection in enumerate(results['detections'][:3], 1):
            print(f"  {i}. {detection['user_id']}")
            print(f"     Risk Score: {detection['risk_score']:.1%}")
            print(f"     Classification: {detection['classification']}")

    print()
    print(f"📊 Full report available at: {results['report_file']}")
    print(f"📁 Raw data available at: {results['data_file']}")
    print()


if __name__ == "__main__":
    main()
