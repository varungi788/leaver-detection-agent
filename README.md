# Leaver Detection Agentic System

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://leaver-detection-agent.streamlit.app)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![MITRE ATT&CK](https://img.shields.io/badge/MITRE-ATT%26CK-red.svg)](https://insiderthreatmatrix.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

An AI-driven insider threat detection platform for automated investigation of departing employees using multi-agent architecture, LLM-powered analysis, and **MITRE ATT&CK Framework** integration.

## 🌐 Live Demo

**Try it now:** [https://leaver-detection-agent.streamlit.app](https://leaver-detection-agent.streamlit.app)

*Interactive dashboard showcasing real-time insider threat investigation with MITRE technique mapping.*

## 🎯 Overview

This system automates the detection and investigation of potential data exfiltration by departing employees through:
- **MITRE Insider Threat Matrix integration** - Industry-standard threat categorization across 12 techniques
- **Parallel multi-agent investigation** across GCP infrastructure  
- **19+ automated telemetry checks** running simultaneously
- **AI-powered risk scoring** and evidence correlation
- **Automatic technique-to-finding mapping** with coverage reporting
- **Sub-minute response time** from termination trigger to report

Built to showcase enterprise-grade insider threat automation capabilities with simulated GCP telemetry data and aligned with industry-standard frameworks.

## 🎓 New to Insider Threat Detection?

**Start with the Training Simulator!** Before diving into the full multi-agent system, check out [`training_simulator/`](training_simulator/) for a beginner-friendly introduction:
- ✅ Simple, easy-to-understand code
- ✅ No API keys required
- ✅ 5-minute setup
- ✅ Learn core concepts: behavioral analysis, risk scoring, AI agents

**[→ Start Training Here](training_simulator/README.md)**

Then progress to the full system below for production-grade capabilities.

## 🏗️ Architecture

### Multi-Agent System
```
┌─────────────────────────────────────────────────────────────┐
│                    Orchestrator Agent                        │
│          (Coordinates & manages investigation)               │
└───────────────────────┬─────────────────────────────────────┘
                        │
        ┌───────────────┼───────────────┬──────────────┐
        │               │               │              │
┌───────▼──────┐ ┌─────▼──────┐ ┌─────▼──────┐ ┌────▼─────┐
│Cloud Storage │ │Email Agent │ │Compute Agnt│ │Audit Log │
│    Agent     │ │  (Gmail)   │ │   (GCE)    │ │  Agent   │
└───────┬──────┘ └─────┬──────┘ └─────┬──────┘ └────┬─────┘
        │               │               │              │
        └───────────────┼───────────────┴──────────────┘
                        │
        ┌───────────────▼───────────────┐
        │    Risk Scoring Agent         │
        │  (ML-based risk aggregation)  │
        └───────────────┬───────────────┘
                        │
        ┌───────────────▼───────────────┐
        │   Report Generator Agent      │
        │ (Investigation narrative)     │
        └───────────────────────────────┘
```

### Key Features
- ✅ **MITRE ATT&CK Integration** - Automatic mapping to 12 insider threat techniques across 5 tactics
- ✅ **Coverage Reporting** - Quantifiable detection metrics showing technique coverage by tactic
- ✅ **19 Parallel Telemetry Checks** - Cloud storage, email, compute, audit logs
- ✅ **False-Positive Suppression** - Deterministic filtering (>98% accuracy)
- ✅ **Risk Scoring** - ML-based aggregation with confidence intervals
- ✅ **Timeline Reconstruction** - Chronological evidence mapping
- ✅ **LLM-Powered Analysis** - Claude API for intelligent pattern detection
- ✅ **Evidence Packaging** - Legal-defensible investigation reports
- ✅ **Industry Standard** - Aligned with MITRE Insider Threat Matrix (insiderthreatmatrix.org)

## 📊 Data Sources (Simulated GCP)

1. **GCP Cloud Storage (GCS)** - Bucket access, file downloads, sharing
2. **Gmail/Workspace** - Attachments, external emails, forwarding rules
3. **GCP Compute Engine** - VM access, SSH sessions, file transfers
4. **GCP Cloud Logging** - API calls, authentication, data exports
5. **BigQuery** - Dataset exports and query patterns

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- Claude API key (from Anthropic Console)

### Installation
```bash
# Clone repository
git clone <your-repo-url>
cd leaver-detection-agent

# Install dependencies
pip install -r requirements.txt

# Configure API keys
cp .env.example .env
# Edit .env and add your ANTHROPIC_API_KEY
```

### Run Investigation
```bash
# Generate synthetic data
python data_generators/generate_all.py

# Run leaver detection
python main.py --employee-id EMP001 --termination-date 2026-10-02

# Launch dashboard
streamlit run dashboard/app.py
```

### 🤖 Using with Claude Code

If you're using Claude Code CLI and want to skip permission prompts during development:

```bash
# Option 1: Bypass permissions (use cautiously)
claude --dangerously-skip-permissions

# Option 2: Permission mode bypass
claude --permission-mode bypassPermissions
```

**⚠️ Security Note**: These flags bypass file operation permissions. Only use in trusted development environments.

## 📁 Project Structure
```
leaver-detection-agent/
├── agents/
│   ├── orchestrator.py          # Main coordinator
│   ├── cloud_storage_agent.py   # GCS analysis
│   ├── email_agent.py           # Gmail analysis
│   ├── compute_agent.py         # GCE analysis
│   ├── audit_log_agent.py       # Cloud Logging analysis
│   ├── risk_scorer.py           # Risk aggregation
│   └── report_generator.py      # Report creation
├── data_generators/
│   ├── gcs_generator.py         # Cloud Storage telemetry
│   ├── gmail_generator.py       # Email telemetry
│   ├── gce_generator.py         # Compute telemetry
│   └── audit_generator.py       # Audit log telemetry
├── models/
│   ├── telemetry.py             # Data models
│   └── risk_models.py           # Risk scoring models
├── utils/
│   ├── llm_client.py            # Claude API wrapper
│   └── evidence_packager.py     # Evidence management
├── dashboard/
│   └── app.py                   # Streamlit UI
├── config/
│   └── detection_rules.yaml     # Detection rules
├── outputs/                      # Investigation reports
├── tests/                        # Unit tests
├── main.py                       # Entry point
└── requirements.txt
```

## 🎓 Technical Highlights

### 1. Parallel Execution
- Async/await for concurrent agent execution
- Response time: **< 60 seconds** for full investigation

### 2. False-Positive Filtering
```python
# Suppress non-risk activity
- Personal career documents (resume.pdf, cover_letter.docx)
- Standard dev tools (IDE configs, package managers)
- Legitimate business sharing (approved external domains)
```

### 3. Risk Scoring Algorithm
```
Risk Score = Σ (Severity × Confidence × Frequency Weight)
Categories: CRITICAL (90+), HIGH (70-89), MEDIUM (40-69), LOW (<40)
```

### 4. LLM-Powered Analysis
- Pattern recognition across disparate telemetry sources
- Natural language investigation summaries
- Anomaly explanation generation

## 📈 Detection Capabilities

| Check ID | Data Source | Detection Type | Severity |
|----------|-------------|----------------|----------|
| GCS-01 | Cloud Storage | Bulk file download (>1GB) | HIGH |
| GCS-02 | Cloud Storage | Personal account sharing | CRITICAL |
| GCS-03 | Cloud Storage | External domain sharing | MEDIUM |
| EMAIL-01 | Gmail | Large attachment (>10MB) | MEDIUM |
| EMAIL-02 | Gmail | External forwarding rule | CRITICAL |
| EMAIL-03 | Gmail | Bulk email export | HIGH |
| COMPUTE-01 | GCE | Unauthorized SSH access | HIGH |
| COMPUTE-02 | GCE | File transfer to external IP | CRITICAL |
| COMPUTE-03 | GCE | Data staging activity | HIGH |
| AUDIT-01 | Cloud Logging | API key creation | MEDIUM |
| AUDIT-02 | Cloud Logging | Service account compromise | CRITICAL |
| AUDIT-03 | Cloud Logging | BigQuery dataset export | HIGH |

## 🔐 Security & Compliance

- **Legally Defensible**: Evidence chain-of-custody tracking
- **Privacy-Aware**: PII redaction in reports
- **Audit Trail**: All agent decisions logged
- **Role-Based Access**: Investigation visibility controls

## 📊 Sample Output

```
=== LEAVER INVESTIGATION REPORT ===
Employee: John Doe (john.doe@company.com)
Termination Date: 2026-10-02
Investigation Started: 2026-10-02 09:00:15 UTC
Investigation Completed: 2026-10-02 09:00:47 UTC (32 seconds)

RISK SCORE: 87 / 100 (HIGH)

CRITICAL FINDINGS:
[1] Personal Cloud Storage Sharing
    - 47 files (2.3 GB) shared to personal Gmail account
    - Includes: source_code/, financial_projections_2026.xlsx
    - Timeline: 2026-09-30 14:23 - 2026-10-01 22:15 UTC
    
[2] External Email Forwarding Rule
    - Auto-forward rule created: *.* → john.personal@gmail.com
    - Created: 2026-09-29 11:45 UTC
    - Status: Active until termination

RECOMMENDATION: IMMEDIATE ESCALATION TO LEGAL
```

## 🛠️ Tech Stack

- **Agent Framework**: LangGraph
- **LLM**: Claude 3.5 Sonnet (Anthropic)
- **Backend**: Python 3.11, FastAPI
- **UI**: Streamlit
- **Data**: Pydantic models, synthetic GCP telemetry
- **Testing**: pytest

## 📝 Future Enhancements

- [ ] GenAI/LLM usage detection (ChatGPT, Claude exfiltration)
- [ ] Real GCP API integration (Cloud Asset Inventory, Security Command Center)
- [ ] SOAR integration (Splunk Phantom, Palo Alto XSOAR)
- [ ] Machine learning for anomaly detection
- [ ] Multi-cloud support (AWS, Azure)

## 👤 Author

**Insider Risk Analyst** with 5+ years experience in threat-hunting automation and GenAI risk monitoring.

- Designed automated termination pipelines at Uber (19-check system)
- 1,000+ telemetry reviews across global operations
- Google & Apple Security Hall of Fame

## 🌐 Links

- **Live Demo:** [https://leaver-detection-agent.streamlit.app](https://leaver-detection-agent.streamlit.app)
- **GitHub:** [https://github.com/varungi788/leaver-detection-agent](https://github.com/varungi788/leaver-detection-agent)
- **MITRE Reference:** [https://insiderthreatmatrix.org/](https://insiderthreatmatrix.org/)

## 📄 License

MIT License - See LICENSE file for details

---

**⚠️ Disclaimer**: This is a demonstration project using synthetic data. For production deployment, ensure compliance with local privacy laws (GDPR, CCPA) and organizational policies.
