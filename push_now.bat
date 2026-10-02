@echo off
echo ========================================
echo Pushing Leaver Detection Agent to GitHub
echo ========================================
echo.

REM Set Git in PATH temporarily
set PATH=%PATH%;C:\Program Files\Git\cmd;C:\Program Files\Git\bin

REM Verify Git is available
git --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Git is not installed or not found in PATH
    echo Please install Git from: https://git-scm.com/download/win
    echo Then restart your terminal and run this script again.
    pause
    exit /b 1
)

echo Git found!
echo.

REM Initialize repository
echo Initializing Git repository...
git init
if errorlevel 1 (
    echo ERROR: Failed to initialize Git repository
    pause
    exit /b 1
)

REM Configure git user if needed
git config user.name >nul 2>&1
if errorlevel 1 (
    echo Configuring Git user...
    git config user.name "varungi788"
    git config user.email "varungi788@users.noreply.github.com"
)

REM Add all files
echo Adding files...
git add .
if errorlevel 1 (
    echo ERROR: Failed to add files
    pause
    exit /b 1
)

REM Create commit
echo Creating commit...
git commit -m "Initial commit: Leaver Detection Agentic System - Multi-agent insider threat detection platform with LLM analysis, 19+ parallel checks, and automated investigation workflow"
if errorlevel 1 (
    echo ERROR: Failed to create commit
    pause
    exit /b 1
)

REM Add remote
echo Adding GitHub remote...
git remote add origin https://github.com/varungi788/leaver-detection-agent.git 2>nul

REM Rename branch to main
echo Setting branch to main...
git branch -M main

REM Push to GitHub
echo Pushing to GitHub...
git push -u origin main
if errorlevel 1 (
    echo.
    echo ERROR: Failed to push. This might be because:
    echo   1. Authentication is needed
    echo   2. Repository already has content
    echo.
    echo Try running this in PowerShell:
    echo   gh repo view --web
    echo   git push -u origin main --force
    pause
    exit /b 1
)

echo.
echo ========================================
echo SUCCESS! Code pushed to GitHub
echo ========================================
echo.
echo View your repository:
echo https://github.com/varungi788/leaver-detection-agent
echo.

REM Open repository in browser
start https://github.com/varungi788/leaver-detection-agent

pause

