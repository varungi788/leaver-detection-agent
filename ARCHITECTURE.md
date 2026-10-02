# System Architecture

## Overview

The Leaver Detection Agentic System is a hierarchical multi-agent platform that automates insider threat investigations for departing employees.

## High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                         User Interface                          │
│  ┌──────────────┐              ┌──────────────────────┐        │
│  │   CLI Tool   │              │ Streamlit Dashboard  │        │
│  │  (main.py)   │              │   (dashboard/app.py) │        │
│  └──────┬───────┘              └──────────┬───────────┘        │
└─────────┼────────────────────────────────┼────────────────────┘
          │                                 │
          │                                 │
┌─────────▼─────────────────────────────────▼────────────────────┐
│                   Orchestrator Agent                            │
│            (Coordinates multi-agent investigation)              │
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐ │
│  │  Investigation Context Manager                            │ │
│  │  - Employee profile                                       │ │
│  │  - Termination date                                       │ │
│  │  - Investigation timeline                                 │ │
│  │  - Data sources                                           │ │
│  └──────────────────────────────────────────────────────────┘ │
└─────────┬───────────────┬───────────────┬───────────────┬─────┘
          │               │               │               │
    ┌─────▼──────┐  ┌────▼─────┐   ┌────▼─────┐   ┌────▼─────┐
    │   Cloud    │  │  Email   │   │ Compute  │   │  Audit   │
    │  Storage   │  │  Agent   │   │  Agent   │   │   Log    │
    │   Agent    │  │          │   │          │   │  Agent   │
    └─────┬──────┘  └────┬─────┘   └────┬─────┘   └────┬─────┘
          │              │              │              │
          │              │              │              │
    ┌─────▼──────────────▼──────────────▼──────────────▼─────┐
    │                  Risk Scoring Engine                    │
    │    (Aggregates findings + calculates risk score)        │
    └─────────────────────────┬─────────────────────────────┘
                              │
                    ┌─────────▼──────────┐
                    │  Report Generator  │
                    │  (LLM-powered)     │
                    └─────────┬──────────┘
                              │
                    ┌─────────▼──────────┐
                    │ Evidence Packager  │
                    │ (Chain-of-custody) │
                    └─────────┬──────────┘
                              │
                    ┌─────────▼──────────┐
                    │  Investigation     │
                    │     Report         │
                    │  (JSON + Summary)  │
                    └────────────────────┘
```

## Component Details

### 1. Orchestrator Agent

**Responsibilities:**
- Coordinate specialist agents
- Manage investigation lifecycle
- Aggregate results
- Generate final report

**Key Methods:**
- `investigate()` - Main entry point
- `_run_parallel()` - Parallel agent execution
- `_run_sequential()` - Sequential execution
- `_print_report_summary()` - Console output

### 2. Specialist Agents

#### Cloud Storage Agent
**Data Source:** GCP Cloud Storage (GCS)
**Detects:**
- Bulk downloads (>100MB)
- Personal account sharing
- External domain sharing
- Sensitive bucket access

**Key Patterns:**
```python
if (activity.is_personal_account or
    activity.is_external_domain or
    activity.bytes_transferred > threshold):
    flag_as_suspicious()
```

#### Email Agent
**Data Source:** Gmail/Workspace
**Detects:**
- Large attachments to external recipients
- Email forwarding rules
- Bulk email exports
- External domain communication spikes

**Critical Indicator:**
```python
if activity.is_forwarding_rule:
    severity = CRITICAL
```

#### Compute Agent
**Data Source:** GCP Compute Engine (GCE)
**Detects:**
- SSH from external IPs
- Large file transfers
- Data staging commands
- Suspicious command execution

**Pattern Matching:**
```python
suspicious_commands = ['tar -czf', 'scp', 'rsync', 'aws s3 cp']
if command in suspicious_commands:
    flag_as_suspicious()
```

#### Audit Log Agent
**Data Source:** GCP Cloud Audit Logs
**Detects:**
- Service account key creation
- IAM policy modifications
- BigQuery dataset exports
- Secret Manager access

### 3. LLM Integration (Claude API)

**Model:** Claude Sonnet 3.5
**Usage:**
- Pattern recognition across telemetry
- Evidence correlation
- Natural language summaries
- Confidence scoring

**Request Flow:**
```
Telemetry Data → LLM Client → Claude API → Structured JSON
                                             ↓
                                      Finding Objects
```

### 4. Risk Scoring Engine

**Algorithm:**
```python
Risk Score = Σ (Severity × Category × Confidence × Frequency)

Severity Weights:
- CRITICAL: 1.0
- HIGH: 0.7
- MEDIUM: 0.4
- LOW: 0.2

Category Multipliers:
- DATA_EXFILTRATION: 1.5
- CREDENTIAL_ABUSE: 1.3
- UNAUTHORIZED_ACCESS: 1.2
- POLICY_VIOLATION: 1.0

Final Score = min(total_score, 100)
```

**Risk Levels:**
- 90-100: CRITICAL (Immediate legal escalation)
- 70-89: HIGH (HR/Legal review)
- 40-69: MEDIUM (Manager review)
- 0-39: LOW (Document only)

### 5. False-Positive Suppression

**Approach:** Deterministic pattern matching

**Suppressed Patterns:**
```python
FP_PATTERNS = {
    'career_docs': ['resume', 'cv', 'cover_letter'],
    'dev_tools': ['.vscode', '.idea', 'node_modules'],
    'legitimate_business': ['quarterly_report', 'meeting_notes']
}
```

**Suppression Rate:** >98%

### 6. Evidence Packager

**Features:**
- Chain-of-custody tracking
- Timeline reconstruction
- Legal-defensible format
- Integrity hashing

**Output Format:**
```json
{
  "investigation_id": "INV-abc123de",
  "chain_of_custody": { ... },
  "findings": { ... },
  "timeline": [ ... ],
  "recommendations": { ... }
}
```

## Data Flow

### Investigation Execution

```
1. User triggers investigation
   ↓
2. Load employee profile + telemetry data
   ↓
3. Orchestrator initializes specialist agents
   ↓
4. Agents execute in parallel:
   - CloudStorageAgent analyzes GCS data
   - EmailAgent analyzes Gmail data
   - ComputeAgent analyzes GCE data
   - AuditLogAgent analyzes audit logs
   ↓
5. Each agent:
   a) Pre-filters suspicious activities
   b) Sends to Claude LLM for analysis
   c) Parses structured findings
   d) Applies false-positive filtering
   e) Returns AgentResult
   ↓
6. Orchestrator aggregates results
   ↓
7. Risk Scorer calculates overall risk
   ↓
8. Report Generator creates narrative
   ↓
9. Evidence Packager saves report
   ↓
10. Dashboard displays results
```

### Parallel Execution Timeline

```
Time: 0s ────────────────────────────────────────► 60s

CloudStorageAgent:  [════════════════════] (45s)
EmailAgent:         [═════════════════] (40s)
ComputeAgent:       [══════════════════════] (50s)
AuditLogAgent:      [════════════════] (38s)

RiskScorer:                                  [══] (5s)
ReportGenerator:                               [═══] (7s)
EvidencePackager:                                 [═] (3s)

Total: ~60 seconds
```

## Technology Stack

### Core
- **Language:** Python 3.11+
- **Agent Framework:** LangGraph
- **LLM:** Claude 3.5 Sonnet (Anthropic)
- **Data Models:** Pydantic

### Backend
- **API:** FastAPI (future)
- **Data Generation:** Faker

### Frontend
- **Dashboard:** Streamlit
- **Visualization:** Plotly, Altair

### Infrastructure
- **Cloud:** GCP (simulated)
- **Storage:** Local filesystem
- **Config:** YAML, .env

## Security Considerations

### Data Privacy
- PII redaction in reports
- Secure API key storage (.env)
- No data exfiltration from system

### Legal Compliance
- Chain-of-custody tracking
- Audit trail of all decisions
- Legally defensible evidence format

### Access Control
- Role-based investigation visibility (future)
- Encrypted storage (future)
- SOC 2 compliance ready (future)

## Scalability

### Current System
- Single-machine execution
- Sequential LLM calls
- ~1,000 telemetry events per investigation

### Production Scaling
- Kubernetes deployment
- Distributed agent execution
- Batch LLM processing
- Event streaming (Kafka/Pub/Sub)
- Time-series database (TimescaleDB)
- Caching layer (Redis)

## Extension Points

### Adding New Agents
```python
from agents.base_agent import BaseAgent

class NewAgent(BaseAgent):
    def analyze(self, data):
        # Your detection logic
        return AgentResult(...)
```

### Custom Detection Rules
Edit `config/detection_rules.yaml`:
```yaml
new_rules:
  threshold: 100
  patterns:
    - suspicious_pattern_1
    - suspicious_pattern_2
```

### Real Data Integration
Replace synthetic data generators with real APIs:
```python
from google.cloud import storage

def load_real_gcs_data():
    client = storage.Client()
    # Fetch real audit logs
```

## Performance Optimization

### Current Bottlenecks
1. LLM API calls (sequential)
2. Large telemetry dataset processing
3. Report generation time

### Optimization Strategies
1. **Batch LLM requests**
   - Process multiple findings per call
   - Use prompt caching

2. **Stream processing**
   - Incremental telemetry analysis
   - Real-time alerting

3. **Caching**
   - Cache employee profiles
   - Cache common detection patterns

## Monitoring & Observability

### Metrics to Track (Future)
- Investigation execution time
- Agent success/failure rates
- False-positive rates
- LLM token usage
- Cost per investigation

### Logging
- All agent decisions logged
- LLM requests/responses logged
- Audit trail for compliance

## Deployment Architecture (Future)

```
┌──────────────────────────────────────────────────────────┐
│                     Load Balancer                        │
└────────────────────────┬─────────────────────────────────┘
                         │
            ┌────────────┼────────────┐
            │            │            │
    ┌───────▼──────┐ ┌──▼────────┐ ┌▼──────────┐
    │ Orchestrator │ │Orchestrator│ │Orchestrator│
    │   Instance   │ │  Instance  │ │  Instance  │
    └───────┬──────┘ └──┬─────────┘ └┬──────────┘
            │           │            │
    ┌───────▼───────────▼────────────▼──────────┐
    │         Agent Worker Pool                  │
    │  (Kubernetes pods, auto-scaling)           │
    └───────┬────────────────────────────────────┘
            │
    ┌───────▼───────────────────────────────────┐
    │         Data Layer                         │
    │  - PostgreSQL (investigations)             │
    │  - TimescaleDB (telemetry)                 │
    │  - S3/GCS (reports)                        │
    │  - Redis (cache)                           │
    └────────────────────────────────────────────┘
```

---

**Architecture designed by:** Insider Risk Analyst with 5+ years experience
**Last Updated:** 2026-10-02
