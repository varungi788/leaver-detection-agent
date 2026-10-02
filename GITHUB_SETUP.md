# GitHub Setup Guide

## Option 1: Automated Push (Recommended)

Once Git is fully installed and configured:

```powershell
# Run the automated push script
.\push_to_github.ps1
```

This will:
1. Initialize Git repository
2. Add all files
3. Create initial commit
4. Create GitHub repository
5. Push code to GitHub

## Option 2: Manual Setup

If the script doesn't work, follow these manual steps:

### Step 1: Initialize Git Repository
```bash
git init
```

### Step 2: Configure Git User
```bash
git config user.name "Your Name"
git config user.email "your.email@example.com"
```

### Step 3: Add Files
```bash
git add .
```

### Step 4: Create Commit
```bash
git commit -m "Initial commit: Leaver Detection Agentic System"
```

### Step 5: Create GitHub Repository
```bash
gh repo create leaver-detection-agent --public --source=. --push
```

### Step 6: Verify
Visit: https://github.com/YOUR_USERNAME/leaver-detection-agent

## Option 3: Using GitHub Website

1. **Create repository on GitHub.com**
   - Go to https://github.com/new
   - Repository name: `leaver-detection-agent`
   - Description: `AI-driven insider threat detection platform`
   - Public repository
   - Click "Create repository"

2. **Push code from command line**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/leaver-detection-agent.git
   git push -u origin main
   ```

## Troubleshooting

### Git not found
**Solution:** Restart your terminal after installing Git, or add Git to PATH manually.

### Authentication failed
**Solution:** Run `gh auth login` to authenticate with GitHub.

### Repository already exists
**Solution:** 
```bash
# If you want to push to existing repo
git remote add origin https://github.com/YOUR_USERNAME/leaver-detection-agent.git
git branch -M main
git push -u origin main --force
```

## Repository Description

Use this for GitHub description:
```
AI-driven insider threat detection platform for automated leaver investigation. 
Multi-agent architecture with LLM-powered analysis, 19+ parallel telemetry checks, 
risk scoring, and false-positive suppression. Built with Claude API, LangGraph, 
Python, and Streamlit.
```

## Topics/Tags

Add these topics to your GitHub repository:
- insider-threat
- security-automation
- ai-agents
- llm
- claude-ai
- gcp-security
- threat-detection
- multi-agent-system
- langgraph
- streamlit
- python
- cybersecurity

## README Badges (Optional)

Add these to the top of your README.md:

```markdown
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Claude API](https://img.shields.io/badge/Claude-API-orange.svg)](https://www.anthropic.com/claude)
```

## Post-Push Checklist

After pushing to GitHub:

- [ ] Verify all files are present
- [ ] Check README renders correctly
- [ ] Add repository description and tags
- [ ] Enable GitHub Actions (optional)
- [ ] Add to your portfolio
- [ ] Share on LinkedIn
- [ ] Add to your resume

## Share Your Work

**LinkedIn Post Template:**
```
🚀 Excited to share my latest project: Leaver Detection Agentic System

Built an AI-driven insider threat detection platform that automates investigations 
for departing employees using multi-agent architecture.

Key features:
✅ 4 specialist AI agents (Cloud Storage, Email, Compute, Audit Log)
✅ LLM-powered analysis with Claude API
✅ 19+ parallel telemetry checks
✅ <60 second investigation time
✅ 98%+ false-positive suppression
✅ Legal-defensible evidence packaging

Tech stack: Python, Claude AI, LangGraph, Streamlit, GCP

This project demonstrates enterprise-scale security automation with modern AI/ML 
techniques, drawing from my 5+ years of insider threat experience.

🔗 GitHub: https://github.com/YOUR_USERNAME/leaver-detection-agent

#CyberSecurity #InsiderThreat #AI #LLM #SecurityAutomation #Python
```

---

**Need help?** Check the README.md or open an issue on GitHub.
