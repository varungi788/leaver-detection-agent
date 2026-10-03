"""Main simulator orchestrating data generation, detection, and AI analysis."""

import os
from datetime import datetime
from data_generator import UserBehaviorGenerator
from detector import LeaverDetector
from agent import LeaverDetectionAgent


class LeaverDetectionSimulator:
    """Complete leaver detection simulation system."""

    def __init__(self, output_dir: str = "../data"):
        self.output_dir = output_dir
        self.data_file = os.path.join(output_dir, "simulation_data.csv")
        self.generator = UserBehaviorGenerator()
        self.detector = LeaverDetector(risk_threshold=0.6)
        self.agent = LeaverDetectionAgent(model_type="rule-based")

        # Ensure output directory exists
        os.makedirs(output_dir, exist_ok=True)

    def run_full_simulation(self, num_normal: int = 20, num_leavers: int = 5) -> dict:
        """
        Run complete simulation: generate data, detect, and analyze.

        Args:
            num_normal: Number of normal users to simulate
            num_leavers: Number of potential leavers to simulate

        Returns:
            dict: Simulation results including detections and AI analysis
        """
        print("="*60)
        print("LEAVER DETECTION SIMULATOR")
        print("="*60)
        print(f"Start Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print()

        # Step 1: Generate synthetic data
        print("[1/4] Generating synthetic user behavior data...")
        dataset = self.generator.generate_dataset(
            num_normal=num_normal,
            num_leavers=num_leavers
        )
        self.generator.save_to_csv(dataset, self.data_file)
        print(f"      Generated {len(dataset)} activities for {num_normal + num_leavers} users")
        print()

        # Step 2: Load data and detect leavers
        print("[2/4] Running statistical detection analysis...")
        self.detector.load_data(self.data_file)
        detections = self.detector.detect_leavers()
        print(f"      Detected {len(detections)} potential leavers")
        print()

        # Step 3: AI Agent analysis
        print("[3/4] Running AI agent analysis...")
        ai_results = {}

        for detection in detections:
            user_id = detection['user_id']
            user_activities = self.detector.get_user_timeline(user_id)

            # Convert to dict format for agent
            activities = []
            for act in user_activities:
                activities.append({
                    'activity_type': act['activity_type'],
                    'timestamp': act['timestamp'],
                    'risk_score': float(act['risk_score'])
                })

            ai_analysis = self.agent.analyze_user(activities)
            ai_results[user_id] = ai_analysis

        print(f"      Completed AI analysis for {len(ai_results)} users")
        print()

        # Step 4: Generate comprehensive report
        print("[4/4] Generating final report...")
        report = self._generate_comprehensive_report(detections, ai_results)

        # Save report
        report_file = os.path.join(self.output_dir, "detection_report.txt")
        with open(report_file, 'w') as f:
            f.write(report)

        print(f"      Report saved to: {report_file}")
        print()
        print("="*60)
        print("SIMULATION COMPLETE")
        print("="*60)

        return {
            'total_users': num_normal + num_leavers,
            'detections': detections,
            'ai_analysis': ai_results,
            'report': report,
            'data_file': self.data_file,
            'report_file': report_file
        }

    def _generate_comprehensive_report(self, detections: list, ai_results: dict) -> str:
        """Generate comprehensive report combining statistical and AI analysis."""
        report = []

        # Header
        report.append("="*80)
        report.append("COMPREHENSIVE LEAVER DETECTION REPORT")
        report.append("="*80)
        report.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append(f"Detection Method: Hybrid (Statistical + AI Agent)")
        report.append("="*80)
        report.append("")

        # Executive Summary
        report.append("EXECUTIVE SUMMARY")
        report.append("-" * 80)
        report.append(f"Total Potential Leavers Detected: {len(detections)}")

        high_risk = [d for d in detections if d['classification'] == 'HIGH_RISK']
        medium_risk = [d for d in detections if d['classification'] == 'MEDIUM_RISK']

        report.append(f"  - High Risk: {len(high_risk)}")
        report.append(f"  - Medium Risk: {len(medium_risk)}")
        report.append("")

        # Detailed Findings
        report.append("DETAILED FINDINGS")
        report.append("-" * 80)

        for i, detection in enumerate(detections, 1):
            user_id = detection['user_id']
            ai_analysis = ai_results.get(user_id, {})

            report.append(f"\n{i}. {user_id}")
            report.append("   " + "="*76)

            # Statistical Analysis
            report.append(f"   Statistical Risk Score: {detection['risk_score']:.2%}")
            report.append(f"   Classification: {detection['classification']}")
            report.append(f"   Total Activities: {detection['total_activities']}")
            report.append(f"   Key Indicators:")
            report.append(f"     - Anomalies: {detection['anomaly_count']}")
            report.append(f"     - After Hours Access: {detection['after_hours_count']}")
            report.append(f"     - Data Exports: {detection['data_export_count']}")
            report.append(f"     - External Emails: {detection['external_email_count']}")

            # AI Analysis
            if ai_analysis:
                report.append(f"\n   AI Agent Confidence: {ai_analysis['ai_confidence']:.1%}")
                report.append(f"   Detected Patterns: {', '.join(ai_analysis['detected_patterns']) if ai_analysis['detected_patterns'] else 'None'}")
                report.append(f"   AI Reasoning: {ai_analysis['reasoning']}")
                report.append(f"   Recommendation: {ai_analysis['recommendation']}")

            report.append("")

        # Recommendations
        report.append("\nRECOMMENDATIONS")
        report.append("-" * 80)

        if high_risk:
            report.append("IMMEDIATE ACTION REQUIRED:")
            for detection in high_risk:
                report.append(f"  - {detection['user_id']}: Escalate to security team for investigation")

        if medium_risk:
            report.append("\nMONITORING REQUIRED:")
            for detection in medium_risk:
                report.append(f"  - {detection['user_id']}: Increase monitoring frequency and review access")

        report.append("\n" + "="*80)
        report.append("END OF REPORT")
        report.append("="*80)

        return "\n".join(report)

    def quick_demo(self):
        """Run a quick demo with fewer users."""
        print("Running Quick Demo...")
        return self.run_full_simulation(num_normal=10, num_leavers=3)


if __name__ == "__main__":
    # Run simulation
    simulator = LeaverDetectionSimulator()
    results = simulator.run_full_simulation(num_normal=20, num_leavers=5)

    # Print summary
    print("\nSIMULATION RESULTS:")
    print(f"Total Users: {results['total_users']}")
    print(f"Detections: {len(results['detections'])}")
    print(f"Data saved to: {results['data_file']}")
    print(f"Report saved to: {results['report_file']}")
