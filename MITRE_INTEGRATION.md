# MITRE Insider Threat Matrix Integration

## 🎯 Overview

This project integrates the **MITRE Insider Threat Matrix** framework, providing industry-standard threat categorization and detection aligned with recognized insider threat patterns.

**Reference:** https://insiderthreatmatrix.org/

## 🏗️ Architecture

### MITRE Framework Components

```
MITRE Insider Threat Matrix
├── 11 Tactics (Attack Lifecycle Phases)
└── 12+ Techniques (Specific Attack Methods)
    ├── T0001: Exfiltration to Personal Cloud Storage
    ├── T0002: Exfiltration via Email
    ├── T0003: Exfiltration via Removable Media
    ├── T0004: Exfiltration via Web Services
    ├── T0005: Data Staging
    ├── T0006: Automated Collection
    ├── T0007: Service Account Credential Theft
    ├── T0008: Valid Account Abuse
    ├── T0009: Email Forwarding Rule
    ├── T0010: Scheduled Transfer
    ├── T0011: Data from Cloud Storage
    └── T0012: Data from Databases
```

## 📊 Tactics Covered

### 1. **Reconnaissance**
Gathering information about the target organization and systems.

### 2. **Resource Development**
Establishing resources to support operations (accounts, tools, infrastructure).

### 3. **Initial Access**
Gaining entry into the target environment using valid credentials.
- **T0008:** Valid Account Abuse

### 4. **Persistence**
Maintaining access to systems over time.

### 5. **Privilege Escalation**
Gaining higher-level permissions.

### 6. **Defense Evasion**
Avoiding detection by security systems.

### 7. **Credential Access**
Stealing credentials for authentication.
- **T0007:** Service Account Credential Theft

### 8. **Discovery**
Exploring the environment to understand what's available.

### 9. **Collection**
Gathering data of interest.
- **T0005:** Data Staging
- **T0006:** Automated Collection
- **T0009:** Email Forwarding Rule
- **T0011:** Data from Cloud Storage
- **T0012:** Data from Databases

### 10. **Exfiltration**
Stealing data from the target environment.
- **T0001:** Exfiltration to Personal Cloud Storage
- **T0002:** Exfiltration via Email
- **T0003:** Exfiltration via Removable Media
- **T0004:** Exfiltration via Web Services
- **T0010:** Scheduled Transfer

### 11. **Impact**
Manipulating, interrupting, or destroying systems and data.

## 🔍 Detection Mapping

### How Findings Map to MITRE Techniques

Each detected finding is automatically mapped to one or more MITRE techniques:

```python
Finding: "Bulk File Download to Personal Account"
├── Techniques Detected:
│   ├── T0001 (Exfiltration to Personal Cloud Storage)
│   └── T0011 (Data from Cloud Storage)
├── Tactics:
│   ├── Exfiltration
│   └── Collection
└── Confidence: 0.95
```

### Example Mappings

| Finding | MITRE Technique | Tactic | Detection Logic |
|---------|----------------|--------|-----------------|
| GCS sharing to personal Gmail | T0001 | Exfiltration | Personal cloud domain detected |
| Email forwarding rule created | T0009, T0002 | Collection, Exfiltration | Forwarding rule + external domain |
| BigQuery dataset export | T0012 | Collection | Large database query/export |
| Service account key creation | T0007 | Credential Access | API key generation event |
| Bulk file downloads | T0011, T0005 | Collection | Large transfer + staging patterns |

## 📈 Coverage Reporting

### What Gets Reported

Each investigation report includes:

1. **Techniques Detected** - List of MITRE technique IDs found
   ```
   ["T0001", "T0002", "T0009", "T0012"]
   ```

2. **Tactics Covered** - High-level attack phases observed
   ```
   ["Exfiltration", "Collection", "Credential Access"]
   ```

3. **Coverage Report** - Detection coverage per tactic
   ```json
   {
     "Exfiltration": {
       "total": 5,
       "detected": 3,
       "techniques": ["T0001", "T0002", "T0010"],
       "coverage_percent": 60.0
     }
   }
   ```

## 🎨 Visualization

### MITRE Matrix Heatmap (in Dashboard)

The enhanced dashboard shows:
- ✅ **Detected techniques** highlighted in red
- ⚪ **Coverage gaps** shown in gray
- 📊 **Percentage coverage** per tactic
- 🔍 **Clickable techniques** with details

Example visualization:
```
┌─────────────────────────────────────────┐
│ MITRE Insider Threat Coverage          │
├─────────────────────────────────────────┤
│ Exfiltration          ████░░ 60%        │
│ Collection            ████░░ 67%        │
│ Credential Access     ██░░░░ 33%        │
│ Discovery             ░░░░░░  0%        │
└─────────────────────────────────────────┘
```

## 💻 Implementation

### Auto-Mapping in Agents

Each agent automatically maps findings:

```python
# After creating a finding
mitre_techniques = ThreatMapping.map_finding_to_technique(
    finding.title,
    finding.description,
    finding.evidence
)
finding.mitre_techniques = mitre_techniques
```

### Detection Logic

```python
# models/insider_threat_matrix.py
def map_finding_to_technique(finding_title, finding_description, evidence):
    techniques = []
    
    # Cloud storage exfiltration
    if 'personal cloud' in description.lower():
        techniques.append("T0001")
    
    # Email forwarding
    if 'forwarding rule' in description.lower():
        techniques.append("T0009")
    
    # Database export
    if 'bigquery' in description.lower():
        techniques.append("T0012")
    
    return techniques
```

## 📊 Benefits

### 1. **Industry Standard Alignment**
- Uses recognized MITRE framework
- Consistent with CIRT/SOC terminology
- Familiar to security professionals

### 2. **Better Communication**
- Common language across teams
- Clear attack lifecycle understanding
- Easier handoff to incident response

### 3. **Coverage Metrics**
- Quantify detection capabilities
- Identify blind spots
- Prioritize detection improvements

### 4. **Threat Intelligence Integration**
- Compare against known insider TTPs
- Track emerging insider threat trends
- Inform detection rule updates

### 5. **Regulatory Compliance**
- Demonstrates structured approach
- Supports audit requirements
- Shows defense-in-depth

## 🎓 Using MITRE Data

### Accessing Technique Details

```python
from models.insider_threat_matrix import ThreatMapping, INSIDER_THREAT_TECHNIQUES

# Get technique details
tech = ThreatMapping.get_technique_details("T0001")
print(tech.name)  # "Exfiltration to Personal Cloud Storage"
print(tech.description)
print(tech.detection)
print(tech.examples)
```

### Filtering by Tactic

```python
from models.insider_threat_matrix import ThreatTactic, ThreatMapping

# Get all exfiltration techniques
exfil_techniques = ThreatMapping.get_techniques_by_tactic(
    ThreatTactic.EXFILTRATION
)
```

### Coverage Analysis

```python
# Generate coverage report
detected = ["T0001", "T0002", "T0009"]
coverage = ThreatMapping.get_coverage_report(detected)

for tactic, stats in coverage.items():
    print(f"{tactic}: {stats['coverage_percent']}% coverage")
```

## 📚 Technique Reference

### T0001: Exfiltration to Personal Cloud Storage

**Description:** Adversary exfiltrates data by uploading to personal cloud storage (Google Drive, Dropbox, OneDrive).

**Detection:**
- Monitor file uploads to personal cloud domains
- Track large file transfers to external accounts
- Detect authentication to personal cloud accounts

**Examples:**
- Uploading source code to personal Google Drive
- Syncing confidential files to Dropbox
- Bulk transfer to personal OneDrive

### T0002: Exfiltration via Email

**Description:** Adversary sends emails with sensitive attachments to personal/external addresses.

**Detection:**
- Monitor emails with large attachments
- Track emails to personal domains
- Detect bulk email sends to external

**Examples:**
- Emailing documents to personal Gmail
- Creating auto-forward rule
- Sending customer lists externally

### T0009: Email Forwarding Rule

**Description:** Adversary creates email forwarding rules to automatically send copies to external addresses.

**Detection:**
- Monitor email rule creation events
- Detect forwarding rules to external domains
- Track inbox rule modifications

**Examples:**
- Forward all emails to personal Gmail
- Auto-forward before termination
- Forward emails with keywords

### T0012: Data from Databases

**Description:** Adversary queries and exports data from databases.

**Detection:**
- Monitor large query results
- Detect bulk data exports
- Track unusual access patterns
- Monitor SELECT * queries

**Examples:**
- Exporting customer table to CSV
- Bulk BigQuery download
- MongoDB database dump

## 🔄 Future Enhancements

### Planned Additions

1. **More Techniques**
   - T0013: Exfiltration via Mobile Device
   - T0014: Print Screen Collection
   - T0015: Cloud Service Dashboard

2. **Advanced Mapping**
   - Machine learning for technique prediction
   - Historical pattern matching
   - Behavioral analysis

3. **Threat Intelligence**
   - Integration with threat feeds
   - Known insider threat campaigns
   - Industry-specific patterns

4. **Automated Playbooks**
   - Technique-specific response actions
   - Escalation workflows
   - Remediation steps

## 📖 References

- **MITRE Insider Threat Matrix:** https://insiderthreatmatrix.org/
- **MITRE ATT&CK:** https://attack.mitre.org/
- **CISA Insider Threat Mitigation:** https://www.cisa.gov/topics/physical-security/insider-threat-mitigation

## 💼 Business Value

### For Security Teams
- ✅ Structured detection framework
- ✅ Standardized terminology
- ✅ Gap analysis capabilities

### For Management
- ✅ Quantifiable coverage metrics
- ✅ Industry-standard reporting
- ✅ Compliance documentation

### For Incident Response
- ✅ Clear attack lifecycle
- ✅ Technique-specific playbooks
- ✅ Threat intelligence correlation

---

**Integration Status:** ✅ Fully Implemented  
**Coverage:** 12 techniques across 5 tactics  
**Auto-mapping:** Enabled in all agents  
**Reporting:** Included in all investigation reports
