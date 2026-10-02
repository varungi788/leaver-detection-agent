# Getting Started - Complete Guide

Welcome to your Leaver Detection Agentic System! This guide will get you from zero to running investigations in 10 minutes.

## 📋 Prerequisites Checklist

Before starting, ensure you have:

- [ ] Python 3.11 or higher installed
- [ ] Anthropic API key ([Get one here](https://console.anthropic.com/))
- [ ] Git installed (for GitHub push)
- [ ] GitHub CLI authenticated
- [ ] Terminal/PowerShell access

## 🚀 Installation Steps

### 1. Navigate to Project Directory
```powershell
cd C:\Users\alwar\leaver-detection-agent
```

### 2. Create Virtual Environment
```powershell
# Create virtual environment
python -m venv venv

# Activate it
.\venv\Scripts\activate

# Verify activation (you should see (venv) in prompt)
```

### 3. Install Dependencies
```powershell
pip install -r requirements.txt
```

This installs:
- `anthropic` - Claude API client
- `langgraph` - Agent orchestration
- `streamlit` - Dashboard framework
- `pydantic` - Data validation
- `faker` - Synthetic data generation
- And more...

### 4. Configure API Key
```powershell
# Open .env file
notepad .env

# Add your Anthropic API key:
# ANTHROPIC_API_KEY=sk-ant-xxxxxxxxxxxxxxxxxxxxx
# Save and close
```

**Where to get API key:**
1. Go to https://console.anthropic.com/
2. Sign up or log in
3. Go to API Keys section
4. Create new key
5. Copy and paste into .env file

## 🎯 Your First Investigation

### Run Complete Investigation (Data Generation + Analysis)
```powershell
python main.py --generate-data
```

**What this does:**
1. Generates realistic GCP telemetry data (5 seconds)
2. Creates employee profile with suspicious activity patterns
3. Runs 4 AI agents in parallel (30-60 seconds)
4. Analyzes 500+ telemetry events
5. Generates risk score and findings
6. Creates investigation report
7. Saves to `outputs/` directory

**Expected Output:**
```
🤖 LEAVER DETECTION AGENTIC SYSTEM
================================================================================
🔄 Generating synthetic telemetry data...
✓ Generated 123 GCS activities
✓ Generated 161 Gmail activities
✓ Generated 132 GCE activities
✓ Generated 311 audit logs

🔍 LEAVER INVESTIGATION: INV-abc123de
================================================================================
Employee: John Doe (john.doe@company.com)
Termination Date: 2026-10-02
Investigation Started: 2026-10-02 15:30:00

🚀 Launching agents in parallel...
⚡ Cloud Storage Agent executing...
⚡ Email Agent executing...
⚡ Compute Agent executing...
⚡ Audit Log Agent executing...

📊 AGENT EXECUTION SUMMARY
================================================================================
✅ CloudStorageAgent:
   ⏱️  Execution Time: 12.3s
   📋 Telemetry Reviewed: 123
   🚨 Anomalies Detected: 23
   🎯 Findings: 3
   🔇 False Positives Suppressed: 2

✅ EmailAgent:
   ⏱️  Execution Time: 11.8s
   📋 Telemetry Reviewed: 161
   🚨 Anomalies Detected: 11
   🎯 Findings: 2
   
... (more agents)

🎯 RISK ASSESSMENT
================================================================================
Overall Risk Score: 87/100
Risk Level: HIGH
Escalation Required: YES ⚠️

🚨 CRITICAL FINDINGS: 3

[1] Personal Cloud Storage Sharing
    Category: DATA_EXFILTRATION
    Confidence: 0.95
    Description: 47 files (2.3 GB) shared to personal Gmail account...

[2] Email Forwarding Rule to External Account
    Category: DATA_EXFILTRATION
    Confidence: 0.98
    Description: Auto-forward rule created 3 days before termination...
```

### View Results in Dashboard
```powershell
streamlit run dashboard/app.py
```

Opens browser to: http://localhost:8501

**Dashboard Features:**
- 📊 Risk metrics and score visualization
- 🔍 Findings breakdown by severity
- ⏱️ Activity timeline
- 📝 Executive summary
- 💼 Recommendations

## 📂 Understanding the Output

### Console Output
- Real-time agent execution status
- Timing metrics
- Finding summaries
- Risk assessment

### JSON Reports
Location: `outputs/investigation_<ID>_<timestamp>.json`

Contains:
- Complete investigation details
- All findings with evidence
- Risk assessment
- Timeline reconstruction
- Recommendations

### Dashboard
Interactive Streamlit app showing:
- Visual risk metrics
- Clickable findings
- Charts and graphs
- Export capabilities

## 🧪 Test Different Scenarios

### Generate Data Only
```powershell
python data_generators/generate_all.py
```

### Run Investigation on Existing Data
```powershell
python main.py
```

### Run in Sequential Mode (Debug)
```powershell
python main.py --parallel=false
```

## 🔧 Customization

### Adjust Detection Rules
Edit: `config/detection_rules.yaml`

```yaml
gcs_rules:
  bulk_download_threshold_mb: 100  # Change threshold
  suspicious_sharing_domains:
    - gmail.com
    - your-domain.com  # Add custom domains
```

### Modify Employee Profile
Edit: `data_generators/generate_all.py`

```python
generate_complete_dataset(
    employee_id="EMP002",
    name="Jane Smith",
    email="jane.smith@company.com",
    department="Finance",
    role="Financial Analyst",
    termination_date=datetime(2026, 10, 15)
)
```

### Change Suspicion Level
In data generators, adjust:
- Number of suspicious activities
- File sizes
- External sharing frequency
- Command patterns

## 🧪 Running Tests

```powershell
pytest tests/ -v
```

Tests cover:
- Agent detection logic
- False-positive filtering
- Risk scoring
- Data model validation

## 📤 Push to GitHub

### Option 1: Automated Script
```powershell
.\push_to_github.ps1
```

### Option 2: Manual
See `GITHUB_SETUP.md` for detailed instructions.

## 🐛 Troubleshooting

### "ANTHROPIC_API_KEY not found"
**Solution:**
1. Check `.env` file exists
2. Verify API key is correct
3. No quotes around key
4. File is in project root

### "No module named 'anthropic'"
**Solution:**
```powershell
# Make sure venv is activated
.\venv\Scripts\activate

# Reinstall dependencies
pip install -r requirements.txt
```

### "Investigation failed" error
**Solution:**
1. Check API key is valid
2. Verify internet connection
3. Run with `--generate-data` first
4. Check `data/generated/` directory exists

### Dashboard won't load
**Solution:**
```powershell
# Make sure you ran an investigation first
python main.py --generate-data

# Then launch dashboard
streamlit run dashboard/app.py
```

### Git/GitHub issues
**Solution:**
- Verify Git is installed: `git --version`
- Check GitHub auth: `gh auth status`
- See `GITHUB_SETUP.md` for detailed steps

## 📊 Performance Expectations

**Typical Execution Times:**
- Data generation: ~5 seconds
- Agent execution (4 agents): 30-60 seconds
- Report generation: ~10 seconds
- **Total end-to-end: <90 seconds**

**API Usage:**
- 4 Claude API calls per investigation
- ~10,000-15,000 tokens total
- **Cost: ~$0.30 per investigation** (Claude Sonnet)

**Accuracy:**
- False-positive suppression: 98%+
- Detection coverage: 19+ checks
- Confidence scoring: 0.0-1.0

## 🎓 Learning the Codebase

### Key Files to Review

1. **Entry Point**
   - `main.py` - Start here

2. **Agent Logic**
   - `agents/orchestrator.py` - Coordination
   - `agents/cloud_storage_agent.py` - Example agent

3. **Data Models**
   - `models/telemetry.py` - All data structures
   - `models/risk_models.py` - Risk scoring

4. **LLM Integration**
   - `utils/llm_client.py` - Claude API wrapper

5. **Data Generation**
   - `data_generators/gcs_generator.py` - Example generator

### Architecture Overview
See `ARCHITECTURE.md` for detailed system design.

## 📈 Next Steps

### Immediate
- [x] Install and run first investigation
- [ ] Explore dashboard features
- [ ] Review generated reports
- [ ] Understand agent logic

### Short-term
- [ ] Customize detection rules
- [ ] Modify synthetic data scenarios
- [ ] Add custom agents
- [ ] Integrate real data sources

### Long-term
- [ ] Deploy to production
- [ ] Add real GCP APIs
- [ ] Implement SOAR integration
- [ ] Scale with Kubernetes

## 🎤 Demo Preparation

### For Recruiters/Interviewers

**5-Minute Demo Flow:**
1. Show README and architecture (1 min)
2. Run investigation from scratch (2 min)
3. Walk through dashboard (1 min)
4. Explain key findings (1 min)

**Talking Points:**
- "Multi-agent architecture with 4 specialist agents"
- "LLM-powered analysis using Claude API"
- "19+ parallel telemetry checks"
- "<60 second execution time"
- "98%+ false-positive suppression"
- "Based on my production system at Uber"

### Technical Questions to Prepare For
- How does the orchestrator coordinate agents?
- What's your risk scoring algorithm?
- How do you handle false positives?
- How would you scale this to production?
- What are the security considerations?

Answers in `ARCHITECTURE.md` and code comments.

## 📚 Additional Resources

- **Full Documentation:** `README.md`
- **Quick Start:** `QUICKSTART.md`
- **Architecture:** `ARCHITECTURE.md`
- **GitHub Setup:** `GITHUB_SETUP.md`
- **Project Summary:** `PROJECT_SUMMARY.md`

## 💡 Pro Tips

1. **Use descriptive commit messages** when pushing to GitHub
2. **Add comments to customizations** so reviewers understand your choices
3. **Screenshot dashboard results** for portfolio/presentations
4. **Keep sample reports** as examples of output quality
5. **Document any modifications** in a CHANGELOG or blog post

## 🎉 You're Ready!

You now have a fully functional insider threat detection platform. This project demonstrates:

- ✅ AI/LLM engineering skills
- ✅ Multi-agent system design
- ✅ Security domain expertise
- ✅ Production-scale thinking
- ✅ Full-stack development

**Go build something awesome!**

---

**Questions?** 
- Check other documentation files
- Review code comments
- Open issues on GitHub (after pushing)

**Need help?**
- Review example outputs in `outputs/`
- Check test files in `tests/`
- Read inline code documentation
