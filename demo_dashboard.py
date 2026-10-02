"""
Demo Dashboard for Streamlit Cloud Deployment
Displays pre-generated investigation report without requiring API keys
"""
import streamlit as st
import json
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path
import pandas as pd

st.set_page_config(
    page_title="Leaver Detection System - Demo",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .reportview-container {
        background: #0E1117;
    }
    .metric-card {
        background-color: #262730;
        padding: 20px;
        border-radius: 10px;
        border-left: 4px solid #FF4B4B;
    }
</style>
""", unsafe_allow_html=True)


def create_demo_report():
    """Create a demo investigation report for display"""
    return {
        'metadata': {
            'investigation_id': 'INV-demo001',
            'employee': {
                'name': 'John Doe',
                'email': 'john.doe@company.com',
                'department': 'Engineering',
                'role': 'Senior Software Engineer',
                'termination_date': '2026-10-02T09:00:00'
            },
            'generated_at': '2026-10-02T09:00:47'
        },
        'risk_assessment': {
            'overall_score': 87.5,
            'risk_level': 'HIGH',
            'confidence_interval': (82.3, 92.7),
            'escalation_required': True
        },
        'findings': {
            'critical': [
                {
                    'finding_id': 'GCS-001',
                    'title': 'Bulk File Download to Personal Account',
                    'severity': 'CRITICAL',
                    'category': 'DATA_EXFILTRATION',
                    'description': 'Employee downloaded 47 files (2.3 GB) from company-source-code bucket and shared to personal Gmail account (john.personal@gmail.com) over 2-day period. Files include proprietary source code, configuration files, and internal documentation.',
                    'confidence_score': 0.95,
                    'recommended_action': 'IMMEDIATE ESCALATION TO LEGAL - Initiate legal hold, preserve all evidence',
                    'evidence': [
                        {'file': 'app/core/authentication.py', 'size_mb': 2.3, 'timestamp': '2026-09-30T14:23:00'},
                        {'file': 'config/production_secrets.yaml', 'size_mb': 0.8, 'timestamp': '2026-09-30T14:25:00'},
                        {'file': 'docs/internal_architecture.pdf', 'size_mb': 15.2, 'timestamp': '2026-10-01T22:15:00'}
                    ]
                },
                {
                    'finding_id': 'EMAIL-001',
                    'title': 'Email Forwarding Rule to External Account',
                    'severity': 'CRITICAL',
                    'category': 'DATA_EXFILTRATION',
                    'description': 'Auto-forward email rule created to forward all incoming emails to john.personal@gmail.com. Rule created 3 days before termination date and remained active until account deactivation.',
                    'confidence_score': 0.98,
                    'recommended_action': 'Disable forwarding rule immediately, audit forwarded emails',
                    'evidence': [
                        {'action': 'create_rule', 'destination': 'john.personal@gmail.com', 'timestamp': '2026-09-29T11:45:00'}
                    ]
                },
                {
                    'finding_id': 'AUDIT-001',
                    'title': 'BigQuery Customer Data Export',
                    'severity': 'CRITICAL',
                    'category': 'DATA_EXFILTRATION',
                    'description': 'Exported customer analytics dataset (2.1M records) from BigQuery to external GCS bucket. Export includes PII, email addresses, and purchase history.',
                    'confidence_score': 0.92,
                    'recommended_action': 'Legal hold on exported data, notify privacy team',
                    'evidence': [
                        {'dataset': 'customer_analytics.users', 'records': 2100000, 'timestamp': '2026-10-01T16:30:00'}
                    ]
                }
            ],
            'high': [
                {
                    'finding_id': 'COMPUTE-001',
                    'title': 'Large File Transfer to External IP',
                    'severity': 'HIGH',
                    'category': 'SUSPICIOUS_BEHAVIOR',
                    'description': 'Multiple large file transfers (total 1.8 GB) from production VM to external IP address via SCP protocol.',
                    'confidence_score': 0.88,
                    'recommended_action': 'Review transferred files, block external IP',
                    'evidence': []
                }
            ],
            'all': []  # Will be populated by combining critical and high
        },
        'statistics': {
            'total_telemetry_reviewed': 727,
            'anomalies_detected': 42,
            'false_positives_suppressed': 8,
            'fp_suppression_rate': 98.3
        },
        'analysis': {
            'executive_summary': '''Investigation of John Doe (john.doe@company.com) conducted on 2026-10-02 revealed a risk score of 87.5/100 (HIGH). Analysis of multiple findings across cloud storage, email, compute, and audit logs indicates deliberate data exfiltration activity during the week preceding the employee's termination date of 2026-10-02.

The investigation identified three CRITICAL findings representing coordinated exfiltration across multiple attack vectors: (1) bulk download and sharing of 2.3 GB of proprietary source code to personal Gmail account, (2) creation of email forwarding rule to external address, and (3) export of customer analytics dataset containing 2.1M records with PII.

Temporal analysis shows all suspicious activity concentrated in 72-hour window before termination, consistent with insider threat behavioral patterns. Evidence quality is high (confidence scores 0.92-0.98) with multiple corroborating data sources. Immediate escalation to Legal and HR recommended with legal hold on all identified data.''',
            'detailed_analysis': '''Automated investigation pipeline analyzed 727 telemetry events across four data sources: GCP Cloud Storage (123 events), Gmail/Workspace (161 events), GCE compute logs (132 events), and Cloud Audit Logs (311 events).

**Key Patterns Identified:**

1. **Data Staging and Exfiltration (Days -3 to -1)**
   - Progressive escalation from reconnaissance to exfiltration
   - Initial small file downloads evolving to bulk transfers
   - Use of personal accounts to bypass DLP controls

2. **Multiple Attack Vectors**
   - Cloud storage sharing (GCS → personal Gmail)
   - Email forwarding rules (persistent access post-termination)
   - Direct data exports (BigQuery → external bucket)
   - VM-based file transfers (SCP to external IPs)

3. **Timing and Intent Indicators**
   - All activity clustered in final week of employment
   - After-hours access patterns (22:15, weekend activity)
   - Targeting of high-value assets (source code, customer data, credentials)

4. **False-Positive Suppression**
   - 8 benign activities correctly filtered (resume downloads, dev tools)
   - 98.3% suppression rate maintained
   - All reported findings verified with high confidence

**Risk Factors:**
- Privileged access level (elevated permissions)
- Access to sensitive systems (production databases, source code repos)
- Knowledge of security controls (attempted evasion patterns observed)
- Clear intent demonstrated by coordinated multi-vector approach''',
            'timeline': [
                {'timestamp': '2026-09-29T11:45:00', 'severity': 'CRITICAL', 'category': 'DATA_EXFILTRATION', 'description': 'Email forwarding rule created'},
                {'timestamp': '2026-09-30T14:23:00', 'severity': 'CRITICAL', 'category': 'DATA_EXFILTRATION', 'description': 'Bulk source code download started'},
                {'timestamp': '2026-10-01T16:30:00', 'severity': 'CRITICAL', 'category': 'DATA_EXFILTRATION', 'description': 'BigQuery customer data export'},
                {'timestamp': '2026-10-01T22:15:00', 'severity': 'HIGH', 'category': 'SUSPICIOUS_BEHAVIOR', 'description': 'After-hours file transfers'},
            ]
        },
        'recommendations': {
            'action': 'IMMEDIATE ESCALATION TO LEGAL - Initiate legal hold, preserve all evidence, notify General Counsel',
            'legal_hold': True
        }
    }


def main():
    # Header
    st.title("🔍 Leaver Detection Agentic System")
    st.markdown("**AI-Powered Insider Threat Investigation Platform**")
    st.markdown("---")

    # Sidebar
    with st.sidebar:
        st.markdown("### 🎯 DEMO MODE")
        st.markdown("### About This Demo")
        st.info("""
        This is a demonstration of an AI-driven insider threat detection platform
        built with multi-agent architecture and LLM-powered analysis.

        **Key Features:**
        - 4 specialist AI agents
        - 19+ parallel telemetry checks
        - <60 second investigation time
        - 98%+ false-positive suppression
        - LLM-powered risk analysis
        """)

        st.markdown("---")
        st.markdown("### Tech Stack")
        st.markdown("""
        - **AI/LLM:** Claude API (Anthropic)
        - **Agents:** LangGraph
        - **Backend:** Python 3.11+
        - **Dashboard:** Streamlit
        - **Data:** Pydantic models
        """)

        st.markdown("---")
        st.markdown("### Links")
        st.markdown("🌐 [Live Demo](https://leaver-detection-agent.streamlit.app)")
        st.markdown("💻 [GitHub Repo](https://github.com/varungi788/leaver-detection-agent)")
        st.markdown("📚 [MITRE Matrix](https://insiderthreatmatrix.org/)")

    # Load demo report
    report = create_demo_report()
    metadata = report['metadata']
    risk = report['risk_assessment']
    findings = report['findings']
    stats = report['statistics']
    analysis = report['analysis']
    recommendations = report['recommendations']

    # Combine all findings
    findings['all'] = findings['critical'] + findings['high']

    # Top metrics
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Risk Score",
            f"{risk['overall_score']}/100",
            delta=None
        )

    with col2:
        risk_color = {
            'CRITICAL': '🔴',
            'HIGH': '🟠',
            'MEDIUM': '🟡',
            'LOW': '🟢'
        }
        st.metric(
            "Risk Level",
            f"{risk_color.get(risk['risk_level'], '⚪')} {risk['risk_level']}"
        )

    with col3:
        st.metric(
            "Total Findings",
            len(findings['all'])
        )

    with col4:
        st.metric(
            "Execution Time",
            "47 seconds"
        )

    st.markdown("---")

    # Employee info
    st.subheader("👤 Employee Investigation")
    employee = metadata['employee']

    col1, col2 = st.columns(2)

    with col1:
        st.write(f"**Name:** {employee['name']}")
        st.write(f"**Email:** {employee['email']}")
        st.write(f"**Department:** {employee['department']}")

    with col2:
        st.write(f"**Role:** {employee['role']}")
        st.write(f"**Termination Date:** {employee['termination_date'][:10]}")
        st.write(f"**Investigation ID:** {metadata['investigation_id']}")

    st.markdown("---")

    # Findings breakdown
    st.subheader("🎯 Findings Breakdown")

    findings_data = {
        'Severity': ['Critical', 'High', 'Medium', 'Low'],
        'Count': [
            len(findings['critical']),
            len(findings['high']),
            0,
            0
        ],
        'Color': ['#FF4136', '#FF851B', '#FFDC00', '#2ECC40']
    }

    fig = go.Figure(data=[
        go.Bar(
            x=findings_data['Severity'],
            y=findings_data['Count'],
            marker_color=findings_data['Color'],
            text=findings_data['Count'],
            textposition='auto',
        )
    ])

    fig.update_layout(
        title="Findings by Severity",
        xaxis_title="Severity Level",
        yaxis_title="Count",
        height=400,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
    )

    st.plotly_chart(fig, use_container_width=True)

    # Critical findings
    if findings['critical']:
        st.markdown("---")
        st.subheader("🚨 Critical Findings")

        for i, finding in enumerate(findings['critical'], 1):
            with st.expander(f"[{i}] {finding['title']}", expanded=(i == 1)):
                st.write(f"**Category:** {finding['category']}")
                st.write(f"**Confidence:** {finding['confidence_score']:.0%}")
                st.write(f"**Description:** {finding['description']}")
                st.write(f"**Recommendation:** {finding['recommended_action']}")

                if finding.get('evidence'):
                    st.write("**Evidence:**")
                    for evidence in finding['evidence'][:3]:
                        st.json(evidence)

    # Statistics
    st.markdown("---")
    st.subheader("📊 Investigation Statistics")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Telemetry Records Reviewed", stats['total_telemetry_reviewed'])
        st.metric("Anomalies Detected", stats['anomalies_detected'])

    with col2:
        st.metric("False Positives Suppressed", stats['false_positives_suppressed'])
        st.metric("FP Suppression Rate", f"{stats['fp_suppression_rate']:.1f}%")

    # Timeline
    if analysis.get('timeline'):
        st.markdown("---")
        st.subheader("⏱️ Activity Timeline")

        timeline_df = pd.DataFrame(analysis['timeline'])
        timeline_df['timestamp'] = pd.to_datetime(timeline_df['timestamp'])

        fig_timeline = px.scatter(
            timeline_df,
            x='timestamp',
            y='severity',
            color='category',
            hover_data=['description'],
            title="Suspicious Activity Timeline",
            color_discrete_map={
                'DATA_EXFILTRATION': '#FF4136',
                'SUSPICIOUS_BEHAVIOR': '#FF851B'
            }
        )

        fig_timeline.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
        )

        st.plotly_chart(fig_timeline, use_container_width=True)

    # Executive Summary
    st.markdown("---")
    st.subheader("📝 Executive Summary")
    st.write(analysis['executive_summary'])

    # Detailed Analysis
    with st.expander("📄 Detailed Analysis"):
        st.write(analysis['detailed_analysis'])

    # Recommendations
    st.markdown("---")
    st.subheader("💼 Recommendations")
    st.error(f"⚠️ {recommendations['action']}")

    if recommendations['legal_hold']:
        st.warning("⚠️ **Legal Hold Recommended** - Preserve all evidence immediately")

    # Footer
    st.markdown("---")
    st.caption(f"Demo Report | Built by Insider Risk Analyst | [View on GitHub](https://github.com/varungi788/leaver-detection-agent)")


if __name__ == "__main__":
    main()
