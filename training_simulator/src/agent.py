"""AI Agent for intelligent leaver detection analysis."""

from typing import List, Dict
import json


class LeaverDetectionAgent:
    """AI-driven agent for analyzing user behavior and detecting leavers."""

    def __init__(self, model_type: str = "rule-based"):
        """
        Initialize the agent.

        Args:
            model_type: Type of model to use ("rule-based", "llm-claude", "llm-openai")
        """
        self.model_type = model_type
        self.behavior_patterns = {
            'data_hoarding': {
                'indicators': ['file_download', 'data_export', 'usb_usage'],
                'weight': 0.8
            },
            'unusual_timing': {
                'indicators': ['after_hours_access', 'weekend_access'],
                'weight': 0.6
            },
            'communication_changes': {
                'indicators': ['external_email', 'email_sent'],
                'weight': 0.7
            },
            'access_expansion': {
                'indicators': ['permission_change', 'config_change'],
                'weight': 0.9
            }
        }

    def analyze_user(self, user_activities: List[Dict]) -> Dict:
        """Analyze a single user's activities using AI reasoning."""
        if self.model_type == "rule-based":
            return self._rule_based_analysis(user_activities)
        else:
            # Placeholder for future LLM integration
            return self._llm_analysis(user_activities)

    def _rule_based_analysis(self, activities: List[Dict]) -> Dict:
        """Rule-based AI analysis using behavior patterns."""
        pattern_scores = {pattern: 0 for pattern in self.behavior_patterns}
        activity_types = [act['activity_type'] for act in activities]

        # Analyze each behavior pattern
        for pattern_name, pattern_data in self.behavior_patterns.items():
            indicators = pattern_data['indicators']
            weight = pattern_data['weight']

            # Count matching indicators
            matches = sum(1 for act_type in activity_types if any(ind in act_type for ind in indicators))

            if matches > 0:
                # Normalize and apply weight
                normalized_score = min(matches / 10.0, 1.0)
                pattern_scores[pattern_name] = normalized_score * weight

        # Calculate overall AI confidence score
        ai_confidence = sum(pattern_scores.values()) / len(pattern_scores)

        # Generate reasoning
        detected_patterns = [name for name, score in pattern_scores.items() if score > 0.3]

        reasoning = self._generate_reasoning(detected_patterns, pattern_scores, activities)

        return {
            'ai_confidence': round(ai_confidence, 3),
            'detected_patterns': detected_patterns,
            'pattern_scores': {k: round(v, 3) for k, v in pattern_scores.items()},
            'reasoning': reasoning,
            'recommendation': self._generate_recommendation(ai_confidence, detected_patterns)
        }

    def _generate_reasoning(self, patterns: List[str], scores: Dict, activities: List[Dict]) -> str:
        """Generate human-readable reasoning for the detection."""
        if not patterns:
            return "No significant behavioral patterns detected. User activity appears normal."

        reasoning_parts = []
        reasoning_parts.append(f"Analysis of {len(activities)} activities revealed:")

        for pattern in patterns:
            score = scores[pattern]
            if score > 0.5:
                reasoning_parts.append(f"- Strong {pattern.replace('_', ' ')} pattern (score: {score:.2f})")
            else:
                reasoning_parts.append(f"- Moderate {pattern.replace('_', ' ')} pattern (score: {score:.2f})")

        return " ".join(reasoning_parts)

    def _generate_recommendation(self, confidence: float, patterns: List[str]) -> str:
        """Generate actionable recommendation."""
        if confidence > 0.8:
            return "IMMEDIATE REVIEW: High confidence of leaver behavior. Escalate to security team."
        elif confidence > 0.6:
            return "MONITOR CLOSELY: Moderate risk detected. Increase monitoring frequency."
        elif confidence > 0.4:
            return "WATCHLIST: Some concerning patterns. Continue routine monitoring."
        else:
            return "NORMAL: No significant risk indicators detected."

    def _llm_analysis(self, activities: List[Dict]) -> Dict:
        """
        Placeholder for LLM-based analysis using Claude API or OpenAI.

        To implement:
        1. Install: pip install anthropic (or openai)
        2. Set API key as environment variable
        3. Send activities to LLM with prompt for analysis
        """
        return {
            'ai_confidence': 0.0,
            'detected_patterns': [],
            'pattern_scores': {},
            'reasoning': "LLM analysis not yet configured. Set API keys and model type.",
            'recommendation': "Configure LLM integration to enable advanced AI analysis."
        }

    def batch_analyze(self, user_profiles: Dict[str, List[Dict]]) -> Dict[str, Dict]:
        """Analyze multiple users in batch."""
        results = {}

        for user_id, activities in user_profiles.items():
            results[user_id] = self.analyze_user(activities)

        return results

    def generate_agent_report(self, user_id: str, analysis: Dict) -> str:
        """Generate detailed AI agent report for a user."""
        report = []
        report.append(f"\n{'='*60}")
        report.append(f"AI AGENT ANALYSIS: {user_id}")
        report.append(f"{'='*60}")
        report.append(f"AI Confidence Score: {analysis['ai_confidence']:.1%}")
        report.append(f"Detected Patterns: {', '.join(analysis['detected_patterns']) if analysis['detected_patterns'] else 'None'}")
        report.append(f"\nPattern Breakdown:")

        for pattern, score in analysis['pattern_scores'].items():
            status = "🔴" if score > 0.5 else "🟡" if score > 0.3 else "🟢"
            report.append(f"  {status} {pattern.replace('_', ' ').title()}: {score:.2f}")

        report.append(f"\nReasoning:")
        report.append(f"  {analysis['reasoning']}")
        report.append(f"\nRecommendation:")
        report.append(f"  {analysis['recommendation']}")
        report.append(f"{'='*60}\n")

        return "\n".join(report)


if __name__ == "__main__":
    # Example usage
    agent = LeaverDetectionAgent(model_type="rule-based")

    # Sample activities
    sample_activities = [
        {'activity_type': 'file_download', 'timestamp': '2024-01-01T22:30:00'},
        {'activity_type': 'data_export', 'timestamp': '2024-01-02T23:15:00'},
        {'activity_type': 'external_email', 'timestamp': '2024-01-03T21:00:00'},
    ]

    analysis = agent.analyze_user(sample_activities)
    print(agent.generate_agent_report("TEST_USER", analysis))
