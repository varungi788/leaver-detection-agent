"""
Main entry point for leaver detection system
"""
import argparse
import json
from datetime import datetime
from pathlib import Path
from models.telemetry import (
    GCSActivity, GmailActivity, GCEActivity, CloudAuditLog,
    EmployeeProfile
)
from agents.orchestrator import OrchestratorAgent
from utils.llm_client import ClaudeClient
from dotenv import load_dotenv

load_dotenv()


def load_telemetry_data(data_dir: Path) -> tuple:
    """Load generated telemetry data from JSON files"""

    print("📂 Loading telemetry data...")

    # Load employee profile
    with open(data_dir / "employee_profile.json") as f:
        employee_data = json.load(f)
        employee = EmployeeProfile(**employee_data)

    # Load GCS activity
    with open(data_dir / "gcs_activity.json") as f:
        gcs_data = [GCSActivity(**item) for item in json.load(f)]

    # Load Gmail activity
    with open(data_dir / "gmail_activity.json") as f:
        gmail_data = [GmailActivity(**item) for item in json.load(f)]

    # Load GCE activity
    with open(data_dir / "gce_activity.json") as f:
        gce_data = [GCEActivity(**item) for item in json.load(f)]

    # Load audit logs
    with open(data_dir / "audit_logs.json") as f:
        audit_logs = [CloudAuditLog(**item) for item in json.load(f)]

    print(f"✅ Loaded {len(gcs_data)} GCS activities")
    print(f"✅ Loaded {len(gmail_data)} Gmail activities")
    print(f"✅ Loaded {len(gce_data)} GCE activities")
    print(f"✅ Loaded {len(audit_logs)} audit logs\n")

    return employee, gcs_data, gmail_data, gce_data, audit_logs


def main():
    """Main execution function"""

    parser = argparse.ArgumentParser(
        description="Leaver Detection Agentic System - Automated Insider Threat Investigation"
    )

    parser.add_argument(
        "--data-dir",
        type=str,
        default="data/generated",
        help="Directory containing generated telemetry data"
    )

    parser.add_argument(
        "--parallel",
        action="store_true",
        default=True,
        help="Run agents in parallel (default: True)"
    )

    parser.add_argument(
        "--generate-data",
        action="store_true",
        help="Generate synthetic data before running investigation"
    )

    args = parser.parse_args()

    print("\n" + "="*80)
    print("🤖 LEAVER DETECTION AGENTIC SYSTEM")
    print("="*80)
    print("AI-Powered Insider Threat Investigation Platform")
    print("Multi-Agent Architecture | LLM-Powered Analysis | GCP Telemetry")
    print("="*80 + "\n")

    # Generate data if requested
    if args.generate_data:
        print("🔄 Generating synthetic telemetry data...\n")
        from data_generators.generate_all import generate_complete_dataset
        generate_complete_dataset(termination_date=datetime(2026, 10, 2, 9, 0, 0))
        print()

    # Verify data directory exists
    data_dir = Path(args.data_dir)
    if not data_dir.exists():
        print(f"❌ Error: Data directory '{data_dir}' not found.")
        print("Run with --generate-data flag to create synthetic data first.")
        return

    # Load telemetry data
    try:
        employee, gcs_data, gmail_data, gce_data, audit_logs = load_telemetry_data(data_dir)
    except Exception as e:
        print(f"❌ Error loading data: {str(e)}")
        print("Run with --generate-data flag to create synthetic data.")
        return

    # Initialize LLM client
    print("🤖 Initializing Claude AI client...")
    try:
        llm_client = ClaudeClient()
        print("✅ Claude client initialized\n")
    except ValueError as e:
        print(f"❌ Error: {str(e)}")
        print("Please set ANTHROPIC_API_KEY in your .env file")
        return

    # Initialize orchestrator
    print("🎭 Initializing multi-agent orchestrator...")
    orchestrator = OrchestratorAgent(llm_client)
    print("✅ Orchestrator ready\n")

    # Run investigation
    try:
        report = orchestrator.investigate(
            employee=employee,
            gcs_data=gcs_data,
            gmail_data=gmail_data,
            gce_data=gce_data,
            audit_logs=audit_logs,
            parallel_execution=args.parallel
        )

        print("\n" + "="*80)
        print("✅ INVESTIGATION COMPLETE")
        print("="*80)
        print(f"Investigation ID: {report.investigation_id}")
        print(f"Risk Score: {report.overall_risk_score}/100 ({report.risk_level.value})")
        print(f"Total Findings: {len(report.all_findings)}")
        print(f"Execution Time: {report.total_execution_time_seconds}s")
        print(f"Report saved to: outputs/")
        print("="*80 + "\n")

        print("💡 Next Steps:")
        print("   1. Review the full report in outputs/ directory")
        print("   2. Launch dashboard: streamlit run dashboard/app.py")
        print("   3. Share findings with HR/Legal if escalation required")
        print()

    except Exception as e:
        print(f"\n❌ Investigation failed: {str(e)}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
