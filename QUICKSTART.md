# Quick Start Guide

Get your leaver detection system running in 5 minutes!

## Prerequisites

- Python 3.11+
- Anthropic API key ([Get one here](https://console.anthropic.com/))

## Installation

### 1. Clone/Navigate to Project
```bash
cd leaver-detection-agent
```

### 2. Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure API Key
```bash
# Copy example environment file
copy .env.example .env

# Edit .env and add your API key
notepad .env
```

Add your Anthropic API key:
```
ANTHROPIC_API_KEY=sk-ant-xxxxxxxxxxxxx
```

## Run Your First Investigation

### Generate Synthetic Data & Run Investigation
```bash
python main.py --generate-data
```

This will:
1. Generate realistic GCP telemetry data (GCS, Gmail, GCE, Audit Logs)
2. Run 4 AI agents in parallel
3. Detect suspicious activity patterns
4. Generate investigation report
5. Save results to `outputs/`

### View Results in Dashboard
```bash
streamlit run dashboard/app.py
```

Then open your browser to: http://localhost:8501

## Understanding the Output

### Console Output
The investigation will display:
- Agent execution summary
- Risk score (0-100)
- Finding counts by severity
- Execution time
- Recommendations

### Report Location
Full JSON reports saved to:
```
outputs/investigation_<ID>_<timestamp>.json
```

### Dashboard
Interactive Streamlit dashboard showing:
- Risk metrics
- Findings breakdown
- Activity timeline
- Executive summary

## Example Output

```
🔍 LEAVER INVESTIGATION: INV-abc123de
Employee: John Doe (john.doe@company.com)
Termination Date: 2026-10-02
Investigation Completed: 45 seconds

🎯 RISK ASSESSMENT
Overall Risk Score: 87/100
Risk Level: HIGH
Escalation Required: YES ⚠️

🚨 CRITICAL FINDINGS: 3
  [1] Personal Cloud Storage Sharing
      47 files (2.3 GB) shared to personal Gmail
  
  [2] Email Forwarding Rule to External Account
      Auto-forward created 3 days before termination
  
  [3] BigQuery Dataset Export
      Customer data exported to external bucket
```

## Next Steps

### Customize Detection Rules
Edit `config/detection_rules.yaml` to adjust:
- Threshold values
- Suspicious patterns
- False-positive filters

### Generate Different Scenarios
Modify `data_generators/generate_all.py`:
- Change employee profile
- Adjust suspicion levels
- Add/remove activities

### Add Real Data Sources
Replace synthetic data with real GCP APIs:
- Cloud Asset Inventory
- Cloud Logging API
- Gmail API
- BigQuery Audit Logs

## Troubleshooting

### "ANTHROPIC_API_KEY not found"
Make sure `.env` file exists and contains your API key.

### "No module named 'anthropic'"
Activate your virtual environment and run `pip install -r requirements.txt`

### "Investigation failed"
Check:
1. API key is valid
2. Data files exist in `data/generated/`
3. Run with `--generate-data` first

## Performance Notes

**Typical execution times:**
- Data generation: ~5 seconds
- Investigation (4 agents): 30-60 seconds
- Report generation: ~10 seconds

**API usage per investigation:**
- ~4 Claude API calls (one per agent)
- ~10,000-15,000 tokens per investigation
- Cost: ~$0.30 per investigation (Sonnet 3.5)

## Support

For issues or questions:
1. Check README.md for detailed documentation
2. Review example reports in `outputs/`
3. Open an issue on GitHub

---

**🎉 You're ready to detect insider threats!**
