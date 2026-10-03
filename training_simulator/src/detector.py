"""Core leaver detection logic using statistical and ML approaches."""

import csv
from collections import defaultdict
from datetime import datetime
from typing import List, Dict, Tuple
import statistics


class LeaverDetector:
    """Detect potential leavers based on behavior analysis."""

    def __init__(self, risk_threshold: float = 0.6):
        self.risk_threshold = risk_threshold
        self.user_profiles = defaultdict(lambda: {
            'activities': [],
            'risk_scores': [],
            'anomaly_count': 0,
            'after_hours_count': 0,
            'data_export_count': 0,
            'external_email_count': 0
        })

    def load_data(self, csv_file: str):
        """Load activity data from CSV."""
        with open(csv_file, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                user_id = row['user_id']
                self.user_profiles[user_id]['activities'].append(row)
                self.user_profiles[user_id]['risk_scores'].append(float(row['risk_score']))

                # Count specific risky behaviors
                if row['is_anomaly'] == 'True':
                    self.user_profiles[user_id]['anomaly_count'] += 1
                if 'after_hours' in row['activity_type']:
                    self.user_profiles[user_id]['after_hours_count'] += 1
                if 'data_export' in row['activity_type']:
                    self.user_profiles[user_id]['data_export_count'] += 1
                if 'external_email' in row['activity_type']:
                    self.user_profiles[user_id]['external_email_count'] += 1

    def calculate_risk_score(self, user_id: str) -> float:
        """Calculate overall risk score for a user."""
        profile = self.user_profiles[user_id]

        if not profile['risk_scores']:
            return 0.0

        # Weighted scoring
        avg_risk = statistics.mean(profile['risk_scores'])
        anomaly_weight = min(profile['anomaly_count'] / 10.0, 1.0) * 0.3
        after_hours_weight = min(profile['after_hours_count'] / 5.0, 1.0) * 0.2
        data_export_weight = min(profile['data_export_count'] / 3.0, 1.0) * 0.3
        external_email_weight = min(profile['external_email_count'] / 10.0, 1.0) * 0.2

        total_risk = (
            avg_risk * 0.4 +
            anomaly_weight +
            after_hours_weight +
            data_export_weight +
            external_email_weight
        )

        return min(total_risk, 1.0)

    def detect_leavers(self) -> List[Dict]:
        """Identify potential leavers based on risk analysis."""
        detections = []

        for user_id, profile in self.user_profiles.items():
            risk_score = self.calculate_risk_score(user_id)

            if risk_score >= self.risk_threshold:
                detection = {
                    'user_id': user_id,
                    'risk_score': round(risk_score, 3),
                    'total_activities': len(profile['activities']),
                    'anomaly_count': profile['anomaly_count'],
                    'after_hours_count': profile['after_hours_count'],
                    'data_export_count': profile['data_export_count'],
                    'external_email_count': profile['external_email_count'],
                    'classification': 'HIGH_RISK' if risk_score > 0.8 else 'MEDIUM_RISK',
                    'timestamp': datetime.now().isoformat()
                }
                detections.append(detection)

        # Sort by risk score descending
        detections.sort(key=lambda x: x['risk_score'], reverse=True)
        return detections

    def get_user_timeline(self, user_id: str) -> List[Dict]:
        """Get activity timeline for a specific user."""
        return self.user_profiles[user_id]['activities']

    def generate_report(self, detections: List[Dict]) -> str:
        """Generate a human-readable detection report."""
        report = []
        report.append("=" * 60)
        report.append("LEAVER DETECTION REPORT")
        report.append("=" * 60)
        report.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append(f"Total Users Analyzed: {len(self.user_profiles)}")
        report.append(f"Potential Leavers Detected: {len(detections)}")
        report.append("=" * 60)
        report.append("")

        if not detections:
            report.append("No high-risk users detected.")
        else:
            for i, detection in enumerate(detections, 1):
                report.append(f"{i}. User: {detection['user_id']}")
                report.append(f"   Risk Score: {detection['risk_score']} ({detection['classification']})")
                report.append(f"   Total Activities: {detection['total_activities']}")
                report.append(f"   Anomalies: {detection['anomaly_count']}")
                report.append(f"   After Hours Access: {detection['after_hours_count']}")
                report.append(f"   Data Exports: {detection['data_export_count']}")
                report.append(f"   External Emails: {detection['external_email_count']}")
                report.append("")

        return "\n".join(report)


if __name__ == "__main__":
    detector = LeaverDetector(risk_threshold=0.6)
    detector.load_data("../data/sample_data.csv")
    detections = detector.detect_leavers()
    print(detector.generate_report(detections))
