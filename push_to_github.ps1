# Push Leaver Detection Project to GitHub
# Run this script after Git is fully installed

Write-Host "🚀 Pushing Leaver Detection Agent to GitHub..." -ForegroundColor Cyan
Write-Host ""

# Check if git is available
try {
    git --version | Out-Null
    Write-Host "✅ Git is installed" -ForegroundColor Green
} catch {
    Write-Host "❌ Git is not installed or not in PATH" -ForegroundColor Red
    Write-Host ""
    Write-Host "Please install Git first:" -ForegroundColor Yellow
    Write-Host "  1. Download from: https://git-scm.com/download/win" -ForegroundColor Yellow
    Write-Host "  2. Restart your terminal" -ForegroundColor Yellow
    Write-Host "  3. Run this script again" -ForegroundColor Yellow
    exit 1
}

# Check if gh CLI is available
try {
    gh auth status 2>&1 | Out-Null
    Write-Host "✅ GitHub CLI is authenticated" -ForegroundColor Green
} catch {
    Write-Host "⚠️  GitHub CLI not authenticated" -ForegroundColor Yellow
    Write-Host "Run: gh auth login" -ForegroundColor Yellow
    exit 1
}

Write-Host ""
Write-Host "📦 Initializing Git repository..." -ForegroundColor Cyan

# Initialize git repo if not already done
if (-not (Test-Path ".git")) {
    git init
    Write-Host "✅ Git repository initialized" -ForegroundColor Green
} else {
    Write-Host "✅ Git repository already exists" -ForegroundColor Green
}

# Configure git user if not set
$gitUser = git config user.name 2>$null
if (-not $gitUser) {
    Write-Host ""
    Write-Host "⚙️  Configuring Git user..." -ForegroundColor Cyan
    $userName = Read-Host "Enter your name"
    $userEmail = Read-Host "Enter your email"
    git config user.name "$userName"
    git config user.email "$userEmail"
    Write-Host "✅ Git user configured" -ForegroundColor Green
}

Write-Host ""
Write-Host "📝 Adding files to Git..." -ForegroundColor Cyan
git add .
Write-Host "✅ Files staged" -ForegroundColor Green

Write-Host ""
Write-Host "💾 Creating initial commit..." -ForegroundColor Cyan
git commit -m "Initial commit: Leaver Detection Agentic System

- Multi-agent architecture for insider threat detection
- 4 specialist agents (Cloud Storage, Email, Compute, Audit Log)
- LLM-powered analysis using Claude API
- 19+ parallel telemetry checks
- Risk scoring with false-positive suppression
- Streamlit dashboard for visualization
- Synthetic GCP data generation
- Production-ready investigation pipeline"

Write-Host "✅ Commit created" -ForegroundColor Green

Write-Host ""
Write-Host "🌐 Creating GitHub repository..." -ForegroundColor Cyan
gh repo create leaver-detection-agent `
    --public `
    --source=. `
    --description "AI-driven insider threat detection platform with multi-agent architecture, LLM analysis, and automated leaver investigation" `
    --push

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "🎉 SUCCESS! Project pushed to GitHub" -ForegroundColor Green
    Write-Host ""
    Write-Host "📍 Your repository:" -ForegroundColor Cyan
    gh repo view --web
} else {
    Write-Host ""
    Write-Host "⚠️  Repository might already exist. Trying to push to existing repo..." -ForegroundColor Yellow

    # Get username
    $username = gh api user --jq .login

    # Set remote
    git remote add origin "https://github.com/$username/leaver-detection-agent.git" 2>$null

    # Push
    git branch -M main
    git push -u origin main

    if ($LASTEXITCODE -eq 0) {
        Write-Host ""
        Write-Host "🎉 SUCCESS! Pushed to existing repository" -ForegroundColor Green
        Write-Host ""
        Write-Host "📍 View your repository at:" -ForegroundColor Cyan
        Write-Host "https://github.com/$username/leaver-detection-agent" -ForegroundColor Cyan
    } else {
        Write-Host ""
        Write-Host "❌ Failed to push. Manual steps:" -ForegroundColor Red
        Write-Host ""
        Write-Host "1. Create repository manually on GitHub.com" -ForegroundColor Yellow
        Write-Host "2. Run these commands:" -ForegroundColor Yellow
        Write-Host "   git remote add origin https://github.com/YOUR_USERNAME/leaver-detection-agent.git" -ForegroundColor Yellow
        Write-Host "   git branch -M main" -ForegroundColor Yellow
        Write-Host "   git push -u origin main" -ForegroundColor Yellow
    }
}

Write-Host ""
Write-Host "✨ Done!" -ForegroundColor Green
