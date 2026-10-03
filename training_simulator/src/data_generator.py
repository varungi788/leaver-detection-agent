"""Generate synthetic user behavior data for leaver detection testing."""

import random
import csv
from datetime import datetime, timedelta
from typing import List, Dict


class UserBehaviorGenerator:
    """Generate realistic user activity patterns."""

    def __init__(self, seed=42):
        random.seed(seed)
        self.activities = [
            'login', 'file_access', 'file_download', 'file_upload',
            'email_sent', 'external_email', 'usb_usage', 'print_job',
            'after_hours_access', 'vpn_connection', 'failed_login',
            'data_export', 'config_change', 'permission_change'
        ]

    def generate_normal_user(self, user_id: str, days: int = 30) -> List[Dict]:
        """Generate normal user behavior baseline."""
        activities = []
        start_date = datetime.now() - timedelta(days=days)

        for day in range(days):
            current_date = start_date + timedelta(days=day)

            # Normal working hours (9am-5pm weekdays)
            if current_date.weekday() < 5:  # Monday-Friday
                num_activities = random.randint(15, 40)

                for _ in range(num_activities):
                    hour = random.randint(9, 17)
                    minute = random.randint(0, 59)
                    timestamp = current_date.replace(hour=hour, minute=minute)

                    activity = {
                        'user_id': user_id,
                        'timestamp': timestamp.isoformat(),
                        'activity_type': random.choice(self.activities[:8]),  # Normal activities
                        'risk_score': random.uniform(0, 0.3),
                        'location': random.choice(['Office', 'Home']),
                        'device': f'DEVICE_{random.randint(1, 3)}',
                        'is_anomaly': False
                    }
                    activities.append(activity)

        return activities

    def generate_leaver_behavior(self, user_id: str, days_before_leaving: int = 14) -> List[Dict]:
        """Generate behavior pattern of a potential leaver with anomalies."""
        activities = []
        start_date = datetime.now() - timedelta(days=days_before_leaving)

        # Escalating risky behavior as leaving date approaches
        for day in range(days_before_leaving):
            current_date = start_date + timedelta(days=day)
            risk_multiplier = 1 + (day / days_before_leaving) * 2  # Increases over time

            # More activities, including after hours
            num_activities = random.randint(20, 60)

            for _ in range(num_activities):
                # Include after-hours access
                if random.random() < 0.3:  # 30% after hours
                    hour = random.choice([22, 23, 0, 1, 2, 6, 7])
                else:
                    hour = random.randint(9, 17)

                minute = random.randint(0, 59)
                timestamp = current_date.replace(hour=hour, minute=minute)

                # More risky activities
                risky_activities = [
                    'file_download', 'external_email', 'usb_usage',
                    'data_export', 'after_hours_access', 'vpn_connection'
                ]

                activity_type = random.choice(
                    risky_activities if random.random() < 0.6 else self.activities
                )

                is_anomaly = activity_type in risky_activities and hour not in range(9, 18)

                activity = {
                    'user_id': user_id,
                    'timestamp': timestamp.isoformat(),
                    'activity_type': activity_type,
                    'risk_score': random.uniform(0.5, 0.95) * risk_multiplier,
                    'location': random.choice(['Office', 'Home', 'Unknown']),
                    'device': f'DEVICE_{random.randint(1, 5)}',
                    'is_anomaly': is_anomaly
                }
                activities.append(activity)

        return activities

    def generate_dataset(self, num_normal: int = 20, num_leavers: int = 5) -> List[Dict]:
        """Generate a complete dataset with normal users and leavers."""
        all_activities = []

        # Generate normal users
        for i in range(num_normal):
            user_id = f"USER_{i:03d}"
            activities = self.generate_normal_user(user_id, days=30)
            all_activities.extend(activities)

        # Generate leavers
        for i in range(num_leavers):
            user_id = f"LEAVER_{i:03d}"
            activities = self.generate_leaver_behavior(user_id, days_before_leaving=14)
            all_activities.extend(activities)

        # Sort by timestamp
        all_activities.sort(key=lambda x: x['timestamp'])
        return all_activities

    def save_to_csv(self, activities: List[Dict], filename: str):
        """Save activities to CSV file."""
        if not activities:
            print("No activities to save.")
            return

        keys = activities[0].keys()
        with open(filename, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(activities)
        print(f"Saved {len(activities)} activities to {filename}")


if __name__ == "__main__":
    generator = UserBehaviorGenerator()
    dataset = generator.generate_dataset(num_normal=20, num_leavers=5)
    generator.save_to_csv(dataset, "../data/sample_data.csv")
