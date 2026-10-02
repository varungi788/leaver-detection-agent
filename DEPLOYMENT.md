# Deployment Guide - FREE Hosting Options

## 🎯 Best Option: Streamlit Community Cloud (FREE Forever!)

**Perfect for this project because:**
- ✅ Built for Streamlit apps
- ✅ 100% FREE with no time limit
- ✅ Direct GitHub integration
- ✅ Custom URL: `your-app.streamlit.app`
- ✅ Automatic deployments on push
- ✅ No credit card required

### Step-by-Step Deployment

#### 1. Push Your Code to GitHub

First, get your code on GitHub (see PUSH_INSTRUCTIONS.md)

#### 2. Sign Up for Streamlit Cloud

1. Go to: https://streamlit.io/cloud
2. Click **"Sign up"**
3. Choose **"Continue with GitHub"**
4. Authorize Streamlit to access your GitHub

#### 3. Deploy Your App

1. Click **"New app"**
2. Select:
   - **Repository:** `varungi788/leaver-detection-agent`
   - **Branch:** `main`
   - **Main file path:** `demo_dashboard.py`
3. Click **"Advanced settings"** (optional)
   - Python version: `3.11`
4. Click **"Deploy!"**

#### 4. Your App is Live! 🎉

Your app will be available at:
```
https://varungi788-leaver-detection-agent.streamlit.app
```

### Configuration for Streamlit Cloud

Files already created for you:
- ✅ `.streamlit/config.toml` - Theme and settings
- ✅ `requirements-streamlit.txt` - Lighter dependencies for demo
- ✅ `demo_dashboard.py` - Public-facing demo version

### Features in Demo Version

The `demo_dashboard.py` includes:
- ✅ Pre-generated investigation report
- ✅ Interactive dashboard
- ✅ Risk metrics visualization
- ✅ Timeline charts
- ✅ No API keys needed (demo data)
- ✅ Fast loading (<5 seconds)

### Update Your Deployment

After making changes:
```bash
git add .
git commit -m "Update dashboard"
git push
```

Streamlit Cloud auto-deploys in ~1 minute!

---

## 🔄 Alternative FREE Options

### Option 2: Render (FREE Tier)

**Good for:** Python web services with more control

**Pros:**
- Python backend support
- PostgreSQL database (free)
- Custom domains

**Cons:**
- Spins down after inactivity (cold starts)
- 750 hours/month free limit

**Deploy:**
1. Go to: https://render.com
2. Sign up with GitHub
3. New → Web Service
4. Connect repository
5. Settings:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `streamlit run demo_dashboard.py --server.port $PORT`
6. Deploy

**URL:** `https://your-app.onrender.com`

---

### Option 3: Hugging Face Spaces (FREE)

**Good for:** ML/AI demos and showcases

**Pros:**
- AI/ML community visibility
- Gradio or Streamlit support
- GPU access (paid tier)

**Cons:**
- Slower build times
- Public by default

**Deploy:**
1. Go to: https://huggingface.co/spaces
2. Sign up
3. Create New Space
4. Choose Streamlit
5. Upload files or connect GitHub

**URL:** `https://huggingface.co/spaces/username/leaver-detection`

---

### Option 4: Railway (FREE $5 Credit/Month)

**Good for:** Full-stack apps with databases

**Pros:**
- Easy deployment
- PostgreSQL, Redis support
- Good free tier

**Cons:**
- Credit-based (runs out eventually)

**Deploy:**
1. Go to: https://railway.app
2. Sign up with GitHub
3. New Project → Deploy from GitHub
4. Select your repo
5. Railway auto-detects Python

**URL:** `https://your-app.up.railway.app`

---

## ⚙️ Environment Variables (For Full Version)

If deploying the full investigation system (not demo):

### Streamlit Cloud:
1. Go to app settings
2. Secrets section
3. Add in TOML format:
```toml
ANTHROPIC_API_KEY = "sk-ant-xxxxx"
```

### Render/Railway:
Environment Variables tab:
```
ANTHROPIC_API_KEY=sk-ant-xxxxx
```

---

## 📊 Comparison Chart

| Platform | Cost | Python | Database | Auto-Deploy | Best For |
|----------|------|--------|----------|-------------|----------|
| **Streamlit Cloud** | FREE | ✅ | ❌ | ✅ | Dashboards, demos |
| Render | FREE* | ✅ | ✅ | ✅ | Web services |
| Hugging Face | FREE | ✅ | ❌ | ✅ | ML showcases |
| Railway | $5/mo | ✅ | ✅ | ✅ | Full-stack |
| Vercel | FREE* | ⚠️ | ❌ | ✅ | Frontend only |
| Netlify | FREE* | ⚠️ | ❌ | ✅ | Static sites |

*With limitations

---

## 🎯 Recommended: Streamlit Cloud

**Why?**
1. **Purpose-built** for Streamlit apps
2. **Zero configuration** - just click deploy
3. **FREE forever** - no trial period
4. **Instant updates** - git push = auto-deploy
5. **Community visibility** - Streamlit gallery

**Your deployment:**
```bash
# 1. Push to GitHub (one time)
git push

# 2. Deploy on Streamlit Cloud (one time)
# Visit: https://streamlit.io/cloud

# 3. Auto-updates forever!
# Just git push for updates
```

---

## 🔒 Security Notes

### For Demo Version (`demo_dashboard.py`)
- ✅ No API keys needed
- ✅ Pre-generated data
- ✅ Safe to make public
- ✅ Shows capabilities without risk

### For Full Version (`main.py`)
- ⚠️ Requires API keys
- ⚠️ Use environment variables
- ⚠️ Consider private deployment
- ⚠️ API costs for each investigation

---

## 📈 After Deployment

### Share Your Work

**LinkedIn Post:**
```
🚀 Excited to share my AI-powered Insider Threat Detection Platform!

Live demo: https://your-app.streamlit.app

Features:
✅ Multi-agent architecture
✅ LLM-powered analysis
✅ <60 second investigations
✅ 98%+ false-positive suppression

Built with Claude AI, Python, and Streamlit.

#AI #CyberSecurity #InsiderThreat #Python #MachineLearning
```

**Add to Resume:**
```
• Deployed production-ready insider threat detection platform to 
  Streamlit Cloud with public demo showcasing multi-agent architecture 
  and LLM-powered risk analysis
```

**Portfolio Website:**
- Link to live demo
- Link to GitHub
- Screenshot of dashboard
- Video walkthrough (optional)

---

## 🐛 Troubleshooting

### App won't start on Streamlit Cloud
**Solution:** 
- Check `requirements-streamlit.txt` has all dependencies
- View logs in Streamlit Cloud dashboard
- Make sure `demo_dashboard.py` exists

### App is slow
**Solution:**
- Use `demo_dashboard.py` (no API calls)
- Optimize data loading
- Cache with `@st.cache_data`

### Deployment failed
**Solution:**
- Check Python version (3.11)
- Verify all files pushed to GitHub
- Check Streamlit Cloud logs

---

## ✅ Quick Deployment Checklist

- [ ] Code pushed to GitHub
- [ ] `demo_dashboard.py` exists
- [ ] `requirements-streamlit.txt` exists
- [ ] `.streamlit/config.toml` exists
- [ ] Signed up for Streamlit Cloud
- [ ] Connected GitHub account
- [ ] Deployed app
- [ ] Tested live URL
- [ ] Shared on LinkedIn/portfolio

---

## 🎉 You're Ready to Deploy!

**Recommended path:**
1. Push code to GitHub ✅ (you did this)
2. Deploy to Streamlit Cloud (5 minutes)
3. Share your live demo (instant credibility!)

Your app will be live at:
```
https://varungi788-leaver-detection-agent.streamlit.app
```

**FREE, fast, and impressive!** 🚀
