"""Unit tests for the leaver detector."""

import sys
import os
import unittest
from datetime import datetime

# Add parent directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from detector import LeaverDetector


class TestLeaverDetector(unittest.TestCase):
    """Test cases for LeaverDetector class."""

    def setUp(self):
        """Set up test fixtures."""
        self.detector = LeaverDetector(risk_threshold=0.6)

    def test_initialization(self):
        """Test detector initialization."""
        self.assertEqual(self.detector.risk_threshold, 0.6)
        self.assertIsInstance(self.detector.user_profiles, dict)

    def test_risk_score_calculation(self):
        """Test risk score calculation."""
        # Add some test data
        user_id = "TEST_USER_001"
        self.detector.user_profiles[user_id] = {
            'activities': [],
            'risk_scores': [0.8, 0.9, 0.7],
            'anomaly_count': 5,
            'after_hours_count': 3,
            'data_export_count': 2,
            'external_email_count': 4
        }

        risk_score = self.detector.calculate_risk_score(user_id)

        # Risk score should be between 0 and 1
        self.assertGreaterEqual(risk_score, 0.0)
        self.assertLessEqual(risk_score, 1.0)

        # With high risk activities, score should be elevated
        self.assertGreater(risk_score, 0.5)

    def test_empty_user_profile(self):
        """Test risk calculation for user with no activities."""
        user_id = "EMPTY_USER"
        self.detector.user_profiles[user_id] = {
            'activities': [],
            'risk_scores': [],
            'anomaly_count': 0,
            'after_hours_count': 0,
            'data_export_count': 0,
            'external_email_count': 0
        }

        risk_score = self.detector.calculate_risk_score(user_id)
        self.assertEqual(risk_score, 0.0)

    def test_detection_threshold(self):
        """Test that detection respects risk threshold."""
        # Add low-risk user
        self.detector.user_profiles["LOW_RISK"] = {
            'activities': [],
            'risk_scores': [0.1, 0.2, 0.15],
            'anomaly_count': 0,
            'after_hours_count': 0,
            'data_export_count': 0,
            'external_email_count': 0
        }

        # Add high-risk user
        self.detector.user_profiles["HIGH_RISK"] = {
            'activities': [],
            'risk_scores': [0.8, 0.9, 0.85],
            'anomaly_count': 10,
            'after_hours_count': 5,
            'data_export_count': 3,
            'external_email_count': 8
        }

        detections = self.detector.detect_leavers()

        # Only high-risk user should be detected
        self.assertEqual(len(detections), 1)
        self.assertEqual(detections[0]['user_id'], "HIGH_RISK")

    def test_report_generation(self):
        """Test report generation."""
        self.detector.user_profiles["TEST_USER"] = {
            'activities': [],
            'risk_scores': [0.7],
            'anomaly_count': 3,
            'after_hours_count': 2,
            'data_export_count': 1,
            'external_email_count': 2
        }

        detections = self.detector.detect_leavers()
        report = self.detector.generate_report(detections)

        # Report should contain key information
        self.assertIn("LEAVER DETECTION REPORT", report)
        self.assertIn("TEST_USER", report)
        self.assertIsInstance(report, str)

    def test_classification_levels(self):
        """Test HIGH_RISK vs MEDIUM_RISK classification."""
        # Add medium risk user
        self.detector.user_profiles["MEDIUM"] = {
            'activities': [],
            'risk_scores': [0.65],
            'anomaly_count': 2,
            'after_hours_count': 1,
            'data_export_count': 1,
            'external_email_count': 1
        }

        # Add high risk user
        self.detector.user_profiles["HIGH"] = {
            'activities': [],
            'risk_scores': [0.95],
            'anomaly_count': 15,
            'after_hours_count': 10,
            'data_export_count': 5,
            'external_email_count': 12
        }

        detections = self.detector.detect_leavers()

        # Find each detection
        medium_detection = next(d for d in detections if d['user_id'] == "MEDIUM")
        high_detection = next(d for d in detections if d['user_id'] == "HIGH")

        self.assertEqual(medium_detection['classification'], 'MEDIUM_RISK')
        self.assertEqual(high_detection['classification'], 'HIGH_RISK')


if __name__ == '__main__':
    print("Running Leaver Detector Unit Tests...")
    print("="*60)
    unittest.main(verbosity=2)
